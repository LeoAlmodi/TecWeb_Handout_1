import sqlite3

class Database():
    def __init__(self, nome_do_banco):
        self.conn = sqlite3.connect(nome_do_banco + ".db")
        self.conn.execute("CREATE TABLE note(id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL)")
