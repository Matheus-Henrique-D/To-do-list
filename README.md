# API de Lista de Tarefas (To-Do List)

Este projeto é uma API RESTful simples para gerenciar uma lista de tarefas (To-Do List), desenvolvida com FastAPI.

## 🛠️ Tecnologias Utilizadas

*   **Servidor (Backend):** Python 3, FastAPI, Uvicorn
*   **Cliente (Exemplo):** Python 3, Requests

## 📂 Estrutura de Diretórios

```
ToDo/
└── To-do-list/
    ├── .venv/
    ├── main_api.py        # O servidor FastAPI (Backend)
    ├── cliente.py         # Um cliente de exemplo para a API
    ├── tarefas.py         # Módulo de lógica de negócio das tarefas
    ├── requirements.txt   # Dependências do projeto
    └── README.md
```

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos

1.  Clone o repositório (ou certifique-se de estar no diretório do projeto).

2.  (Opcional, mas recomendado) Crie e ative um ambiente virtual:
    ```bash
    python -m venv .venv
    # No Windows:
    .venv\Scripts\activate
    # No macOS/Linux:
    # source .venv/bin/activate
    ```

3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    pip install fastapi uvicorn
    ```

### 2. Rodar o Servidor (Backend)

Em um terminal, na pasta `To-do-list`, inicie o servidor FastAPI:

```bash
uvicorn app:app --reload
```

O terminal indicará que o servidor está rodando em `http://127.0.0.1:8000`. Mantenha este terminal aberto. Você também pode acessar a documentação interativa da API em `http://127.0.0.1:8000/docs`.

### 3. Usar o Cliente (Exemplo)

O arquivo `cliente.py` contém um exemplo de como interagir com a API. Você pode executá-lo em um **novo terminal** (na mesma pasta `To-do-list`) para testar o backend.

## 📖 Endpoints da API

A API fornece os seguintes endpoints para gerenciar tarefas:

### Listar todas as tarefas

*   **GET** `/tarefas`
*   **Descrição:** Retorna um dicionário com todas as tarefas cadastradas.
*   **Exemplo de Resposta:**
    ```json
    {
      "1": {
        "id": 1,
        "tarefa": "Comprar leite",
        "data": "2025-11-10",
        "hora": null
      }
    }
    ```

### Obter uma tarefa por ID

*   **GET** `/tarefas/{item_id}`
*   **Descrição:** Retorna uma única tarefa com base no ID fornecido.
*   **Exemplo de Resposta:**
    ```json
    {
      "id": 1,
      "tarefa": "Comprar leite",
      "data": "2025-11-10",
      "hora": null
    }
    ```

### Obter próximas tarefas

*   **GET** `/tarefas/proximos`
*   **Descrição:** Retorna uma lista de tarefas com data de vencimento futura, ordenadas da mais próxima para a mais distante.

### Adicionar uma nova tarefa

*   **POST** `/tarefas`
*   **Descrição:** Adiciona uma nova tarefa à lista.
*   **Corpo da Requisição (JSON):**
    ```json
    {
      "tarefa": "Estudar para a prova",
      "data": "2025-12-01",
      "hora": "14:00"
    }
    ```
*   **Exemplo de Resposta:**
    ```json
    {
      "id": 2,
      "tarefa": "Estudar para a prova",
      "data": "2025-12-01",
      "hora": "14:00"
    }
    ```

### Remover uma tarefa

*   **DELETE** `/tarefas/{item_id}`
*   **Descrição:** Remove uma tarefa da lista com base no ID fornecido.
*   **Exemplo de Resposta:**
    ```json
    {
      "message": "Tarefa 1 removida com sucesso!"
    }
    ```
