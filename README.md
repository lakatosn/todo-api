# 📝 To-Do API (Flask)

API REST simples desenvolvida em **Python + Flask**, com operações básicas de CRUD (Create, Read, Update e Delete) para gerenciamento de tarefas.

Projeto criado com foco em **aprendizado prático**, versionamento com GitHub e testes de API utilizando o **Postman**.

---

## 🚀 Tecnologias utilizadas

- Python 3
- Flask
- Git
- GitHub
- Postman

---

## 📌 Funcionalidades

- Criar tarefas
- Listar todas as tarefas
- Atualizar tarefas
- Deletar tarefas
- API REST com respostas em JSON

---

## ▶️ Como executar o projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/lakat0sn/todo-api.git
2️⃣ Entrar na pasta do projeto
bash
Copiar código
cd todo-api
3️⃣ Criar ambiente virtual (opcional, recomendado)
bash
Copiar código
python -m venv venv
4️⃣ Ativar o ambiente virtual
Windows

bash
Copiar código
venv\Scripts\activate
5️⃣ Instalar dependências
bash
Copiar código
pip install flask
6️⃣ Executar a aplicação
bash
Copiar código
python app.py
A API estará disponível em:

cpp
Copiar código
http://127.0.0.1:5000
🔗 Endpoints da API
📄 Listar tarefas
http
Copiar código
GET /tasks
➕ Criar tarefa
h
Copiar código
POST /tasks
Body (JSON):

json
Copiar código
{
  "title": "Estudar Flask",
  "done": false
}
✏️ Atualizar tarefa
http
Copiar código
PUT /tasks/<id>
Body (JSON):

json
Copiar código
{
  "title": "Estudar Flask",
  "done": true
}
❌ Deletar tarefa
http
Copiar código
DELETE /tasks/<id>
🧪 Testes
Os endpoints foram testados utilizando o Postman, validando respostas e status HTTP.

📚 Objetivo do projeto
Este projeto tem como objetivo:

Consolidar conceitos de API REST

Praticar Flask

Utilizar Git/GitHub na prática

Servir como projeto inicial para estágio/júnior

👤 Autor
Desenvolvido por Nicolas Lakatos
