# 😂 Frases Dev API

Uma API simples + interface web para gerar, buscar e adicionar frases engraçadas do mundo da programação.

---

## 🚀 Funcionalidades

* 🔀 Gerar frase aleatória
* 🔍 Buscar frase por ID
* 📜 Listar todas as frases
* ➕ Adicionar novas frases via API
* 🌐 Interface web integrada

---

## 🛠️ Tecnologias

* **Backend:** FastAPI (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Comunicação:** Fetch API (HTTP requests)

---

## 📦 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/frases-dev-api.git
cd frases-dev-api
```

---

### 2. Instale as dependências

```bash
pip install fastapi uvicorn
```

---

### 3. Execute a API

```bash
uvicorn main:app --reload
```

A API estará disponível em:
👉 http://127.0.0.1:8000

Documentação automática:
👉 http://127.0.0.1:8000/docs

---

### 4. Abra o frontend

Basta abrir o arquivo:

```bash
index.html
```

---

## 🔗 Endpoints da API

### 🔀 GET /

Retorna uma frase aleatória

```json
{
  "frase": "Funciona na minha máquina 🤡"
}
```

---

### 📜 GET /frases

Retorna todas as frases

---

### 🔍 GET /frase/{id}

Retorna uma frase específica pelo índice

---

### ➕ POST /addfrase

Adiciona uma nova frase

```json
{
  "texto": "Nova frase aqui"
}
```
ps: Frases novas começam no índice 50
---

## 💡 Aprendizados

Este projeto foi desenvolvido com foco em aprendizado prático de:

* Criação de APIs REST
* Diferença entre métodos HTTP (GET, POST)
* Integração frontend ↔ backend
* Manipulação de JSON
* Uso de FastAPI
* Consumo de APIs com JavaScript (fetch)

---

## 📸 Preview

<img width="491" height="510" alt="image" src="https://github.com/user-attachments/assets/c0f75830-a9a6-4390-a8df-16ba4fc503a0" />


---

## 📌 Próximos passos (melhorias futuras)

* 💾 Persistência com banco de dados (SQLite/MySQL)
* 👍 Sistema de likes nas frases
* 🏷️ Categorias de frases
* 🌍 Deploy da aplicação
* 🎨 Melhorias na interface

---

## 👨‍💻 Autor

Desenvolvido por **Maurício Silva**

---

## ⭐ Contribuição

Sinta-se livre para abrir issues ou contribuir com melhorias!
