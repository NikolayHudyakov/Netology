import psycopg2


class Clients:
    def __init__(self, conn) -> None:             # Как у параметра метода (conn) указать тип? При попытки это сделать получаю исключение
        self.conn : psycopg2.connection = conn    # (AttributeError: module 'psycopg2' has no attribute 'connection'), хотя если указать тип
                                                  # у атрибута класса то все норм (self.conn : psycopg2.connection = conn)
    def create_db(self) -> None: 
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS clients(
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(40),
                    last_name VARCHAR(40),
                    email VARCHAR(40)
                );
                """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phones(
                    id SERIAL PRIMARY KEY,
                    phone VARCHAR(40),
                    client_id INTEGER REFERENCES clients(id)
                );
                """)
            self.conn.commit()
    
    def __cur_insert_phones(self, cur, phone: str, client_id: int) -> None: # Как у параметра метода (cur) указать тип? Та же проблема что и выше
        cur.execute("""
            INSERT INTO phones(phone, client_id)
            VALUES(%s, %s);
            """, (phone, client_id))
    
    def __cur_update(self, cur, column: str, value: str, client_id: int) -> None:
        cur.execute(f"""
            UPDATE clients 
            SET {column}=%s
            WHERE id=%s;
            """, (value, client_id))
        
    def __cur_select(self, cur, column: str, value: str) -> None:
        cur.execute(f"""
            SELECT * FROM clients c  
            LEFT JOIN phones p ON p.client_id = c.id  
            WHERE c.{column}=%s;
            """, (value,))
        
    def add_client(self, first_name: str, last_name: str, email: str, phones: list[str]=None) -> None:
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO clients(first_name, last_name, email)
                VALUES(%s, %s, %s) RETURNING id;
                """, (first_name, last_name, email))
            if phones != None:
                client_id = cur.fetchone()[0]
                for phone in phones:
                    self.__cur_insert_phones(cur, phone, client_id)
            self.conn.commit()

    def add_phone(self, client_id: int, phone: str) -> None:
        with self.conn.cursor() as cur:
            self.__cur_insert_phones(cur, phone, client_id)
            self.conn.commit()

    def change_client(self, client_id: int, first_name: str=None, last_name: str=None, email: str=None, phones: list[str]=None): # Какая есть альтернатива этому?
        with self.conn.cursor() as cur:                                                                                          # в моем случае выглядит не очень
            if first_name != None:
                self.__cur_update(cur, 'first_name', first_name, client_id)
            if last_name != None:
                self.__cur_update(cur, 'last_name', last_name, client_id)
            if email != None:
                self.__cur_update(cur, 'email', email, client_id)
            if phones != None:
                cur.execute("""
                    DELETE FROM phones WHERE client_id=%s;
                    """, (client_id,))
                for phone in phones:
                    self.__cur_insert_phones(cur, phone, client_id)
            self.conn.commit()

    def delete_phone(self, phone: str):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM phones WHERE phone=%s;
                """, (phone,))
            self.conn.commit()         
               
    def delete_client(self, client_id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM phones WHERE client_id=%s;
                """, (client_id,))
            cur.execute("""
                DELETE FROM clients WHERE id=%s;
                """, (client_id,))
            self.conn.commit() 

    def find_client(self, first_name: str=None, last_name: str=None, email: str=None, phone: str=None):
        with self.conn.cursor() as cur:
            if first_name != None:
                self.__cur_select(cur, 'first_name', first_name)
                return cur.fetchall()
            if last_name != None:
                self.__cur_select(cur, 'last_name', last_name)
                return cur.fetchall()
            if email != None:
                self.__cur_select(cur, 'email', email)
                return cur.fetchall()
            if phone != None:
                cur.execute("""
                SELECT * FROM clients c  
                LEFT JOIN phones p  ON p.client_id  = c.id  
                WHERE c.id = (SELECT p.client_id FROM phones WHERE phone=%s);
                """, (phone,))
                return cur.fetchall()
            

    