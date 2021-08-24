# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class TestSpyderPipeline:
    def __init__(self) -> None:
        self.create_connection()
        self.create_tables()

    def create_connection(self):
        self.conn = sqlite3.connect("myquotes.db")
        self.curr = self.conn.cursor()

    def create_tables(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""DROP TABLE IF EXISTS tags_tb""")

        self.curr.execute(
            """create table quotes_tb(
                    id INTEGER PRIMARY KEY,
                    title text,
                    author text,
                    author_link text,
                    tags text
                )"""
        )

        self.curr.execute(
            """create table tags_tb(
                    id integer PRIMARY KEY,
                    tag text,
                    quote_id integer,
                    FOREIGN KEY (quote_id) REFERENCES quotes_tb (id)
                )"""
        )

    def process_item(self, item, spider):
        self.store_db(item)
        # print("Pipeline: " + item["author_link"])
        return item

    def store_db(self, item):
        self.curr.execute(
            """insert into quotes_tb(title, author, author_link, tags) values (?,?,?,?)""",
            (
                item["title"][1:-1],
                item["author"][0],
                item["author_link"],
                ",".join(item["tag"]),
            ),
        )

        quote_id = self.curr.lastrowid
        for tag in item["tag"]:
            self.curr.execute(
                """insert into tags_tb(tag, quote_id) values (?,?)""", (tag, quote_id)
            )

        self.conn.commit()
