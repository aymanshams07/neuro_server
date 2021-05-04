#coding: utf-8

import tornado.web
import sqlite3

#conn = sqlite3.connect('c:/toz.db')
conn = sqlite3.connect('toz.db')
c = conn.cursor()
try:
    c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, 
                    name text, rating integer, bid integer)''')
except sqlite3.OperationalError:
    pass


class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('page.html')


class Saver(tornado.web.RequestHandler):
    def post(self):
        name = self.get_argument('name')
        rating = int(self.get_argument('rating'))
        bid = int(self.get_argument('bid'))
        c.execute('''insert into users values (?, ?, ?)''', (name, rating, bid))
        conn.commit()
        self.redirect('/success')

class Getter(tornado.web.RequestHandler):
    def get(self):
        c.execute('select * from users')
        res = c.fetchall()
        #search about fetchmany(int), fetchone() to get only some records or one (note that after getting it, the cursor will increment)
        result = []
        for i in res:
            result.append(i)
        self.write(str(result))
