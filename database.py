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

    def get_all(self):
        l = []
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            note = Note(id, title, content)
            l.append(note)
        return l

    def update(self, entry):
        self.conn.execute(f"UPDATE note SET title = '{entry.title}', content = '{entry.content}' WHERE id = 2")
        self.conn.commit()
        
    def delete(self, note_id):
        self.conn.execute(f"DELETE FROM note WHERE id = {note_id}")
        self.conn.commit()
