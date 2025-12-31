import sqlite3

conn = sqlite3.connect('database.db')

conn.execute("""
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT,
    concluida BOOLEAN NOT NULL
)
""")

conn.close()
print("Banco criado com sucesso!")
