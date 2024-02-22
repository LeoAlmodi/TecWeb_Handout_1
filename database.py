import sqlite3

class Note:
    def __init__(self, id=None, title=None, content=""):
        self.id = id
        self.title = title
        self.content = content
class Database():
    def __init__(self, nome_do_banco):
        self.conn = sqlite3.connect(nome_do_banco + ".db")
        self.conn.execute("CREATE TABLE note(id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL)")

    def add(self, note):
        self.conn.execute(f"INSERT INTO note(title, content) VALUES ('{note.title}', '{note.content}')")
        self.conn.commit()

