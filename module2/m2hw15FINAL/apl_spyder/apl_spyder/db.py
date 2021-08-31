import sqlite3


conn = sqlite3.connect('xiaomi.db')
curr = conn.cursor()

curr.execute('''
            create table xiaomi(
            title text,
            link text,
            price text
            )''')
            
conn.commit()
conn.close()