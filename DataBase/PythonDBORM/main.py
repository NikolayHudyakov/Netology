import sqlalchemy
import sqlalchemy as sq
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
import models



load_dotenv()
    
DSN = os.getenv('DSN')
engine = sqlalchemy.create_engine(DSN)
models.create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# publisher1 = models.Publisher(name='publisher1')
# book1 = models.Book(title='book1', publisher=publisher1)
# shop1 = models.Shop(name='shop1')
# stock1 = models.Stock(book=book1, shop=shop1, count=10)
# sale1 = models.Sale(price=500, date_sale='2023-07-19', stock=stock1, count=5)

# session.add_all([publisher1, book1, shop1, stock1, sale1])
# session.commit()

publisher_name = input()

q = session.query(models.Sale).join(models.Stock).join(models.Shop).join(models.Book).join(models.Publisher).filter(models.Publisher.name == publisher_name)

for p in q:
    print(f'{p.stock.book.title} | {p.stock.shop.name} | {p.price} | {p.date_sale}')