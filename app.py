from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return jsonify([dict(task) for task in tasks])

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO tasks (titulo, descricao, concluida) VALUES (?, ?, ?)',
        (data['titulo'], data.get('descricao', ''), False)
    )
    conn.commit()
    conn.close()
    return jsonify({'message': 'Tarefa criada com sucesso'}), 201

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.json
    conn = get_db_connection()
    conn.execute(
        'UPDATE tasks SET titulo = ?, descricao = ?, concluida = ? WHERE id = ?',
        (data['titulo'], data['descricao'], data['concluida'], id)
    )
    conn.commit()
    conn.close()
    return jsonify({'message': 'Tarefa atualizada'})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Tarefa deletada'})

if __name__ == '__main__':
    app.run(debug=True)
