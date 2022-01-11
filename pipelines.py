# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class MeeshoappPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="12345", database="list")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS scrapy2""")
        self.curr.execute("""create table scrapy2(name text,price text,
                 image text)""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into scrapy2 values(%s,%s,%s)""",
                          (item['name'][0],
                           item['price'][1],
                           item['image'][0]
                           ))
        self.conn.commit()

