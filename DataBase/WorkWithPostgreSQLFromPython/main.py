import os
from dotenv import load_dotenv
import psycopg2
from clients import Clients


if __name__ == '__main__':
    load_dotenv()
    
    with psycopg2.connect(database='clients_db', user='postgres', password=os.getenv('POSTGRES_PASSWORD')) as conn:
        clients = Clients(conn)
        # clients.create_db()
        # clients.add_client('FirstName', 'LastName', 'firstName@gmail.com', ['89990000000', '89991111111'])
        # clients.add_client('FirstName1', 'LastName1', 'firstName@gmail.com1')
        # clients.add_phone(3, '89992222222')
        # clients.change_client(3, 'NewFirstName', None, 'newFirstName@gmail.com', ['89993333333', '89994444444'])
        # clients.delete_phone('89994444444')
        # clients.delete_client(3)
        # print(clients.find_client('FirstName'))
        print(clients.find_client(phone='89991111111'))
        conn.close()