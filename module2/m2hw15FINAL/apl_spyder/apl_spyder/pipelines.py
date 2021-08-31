# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class AplSpyderPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()
        
    def create_connection(self):
        self.conn = sqlite3.connect('xiaomi.db')
        self.curr = self.conn.cursor()
        
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS xiaomi_phone""")
        self.curr.execute("""create table xiaomi_phone(
                        id integer PRIMARY KEY,
                        title text,
                        link text,
                        price text
                        )""")
                        
    def process_item(self, item, spider):   
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into xiaomi_phone(title, link, price) values(?, ?, ?)""",(
        item['title'][0],
        item['link'][0],
        item['price'][0]
        ))
        self.conn.commit()