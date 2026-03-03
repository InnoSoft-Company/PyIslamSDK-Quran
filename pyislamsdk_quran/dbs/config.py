import sqlite3

class DBConnect:
  def __init__(self, db_path):
    self.db_path = db_path
    self.conn = sqlite3.connect(db_path)
    self.conn.row_factory = sqlite3.Row
    self.cur = self.conn.cursor()

  def fetch(self, table, columns='*', where=None):
    query = f"SELECT {columns} FROM {table}"
    if where: query += f" WHERE {where}"
    self.cur.execute(query)
    return [dict(row) for row in self.cur.fetchall()]

  def execute(self, query, params=()):
    self.cur.execute(query, params)
    self.conn.commit()
    return self.cur

  def close(self): self.conn.close()
