# API de Lista de Tarefas (To-Do List)

Este projeto é uma API RESTful simples para gerenciar uma lista de tarefas (To-Do List), desenvolvida em dupla para o Mini Projeto de Consumo de APIs.

## 👥 Colaboração e Avaliação

Este projeto foi desenvolvido em dupla, seguindo os requisitos de avaliação individual e contribuição via Pull Request:

* **Backend (Servidor):** Nicolas Ferreira
    * Responsável pela implementação do servidor FastAPI (`main_api.py`), definição dos endpoints, e a lógica de negócio no `tarefas.py`.

* **Cliente (Consumidor):** Matheus Henrique D.
    * Responsável pela implementação do script `cliente.py` para consumir a API com `requests` (comandos `listar` e `adicionar`).
    * Responsável pelo `requirements.txt` inicial do cliente.

O fluxo de desenvolvimento seguiu o modelo Fork & Pull Request para registrar as contribuições de cada integrante.

## 🛠️ Tecnologias Utilizadas

* **Servidor (Backend):** Python 3, FastAPI, Uvicorn
* **Cliente (Consumidor):** Python 3, Requests

## 📂 Estrutura de Diretórios
```
ToDo/
└── To-do-list/
    ├── .venv/
    ├── main_api.py         # O servidor FastAPI (Backend)
    ├── cliente.py          # O cliente 'requests' (Frontend)
    ├── tarefas.py          # Módulo de lógica de negócio das tarefas
    ├── requirements.txt    # Dependências do projeto
    └── README.md
```

## 🚀 Como Executar o Projeto

Para rodar o projeto, você precisará de **dois terminais** abertos simultaneamente.

### 1. Pré-requisitos

1. Clone o repositório (ou certifique-se de estar no diretório do projeto).

2. (Opcional, mas recomendado) Crie e ative um ambiente virtual:
```bash
   python -m venv .venv
   # No Windows:
   .venv\Scripts\activate
   # No macOS/Linux:
   # source .venv/bin/activate
```

3. Instale todas as dependências (do cliente e do servidor):
```bash
   pip install -r requirements.txt
```
   *(**Nota:** O `requirements.txt` atual só contém `requests`. Para rodar o servidor, é necessário instalar o `fastapi` e `uvicorn` também: `pip install fastapi uvicorn`)*

### 2. Terminal 1: Rodar o Servidor (Backend)

Em um terminal, na pasta `To-do-list`, inicie o servidor FastAPI (observe que o nome do arquivo é `main_api` e o objeto da app é `app`):
```bash
uvicorn main_api:app --reload
```

O terminal indicará que o servidor está rodando em `http://127.0.0.1:8000`. Mantenha este terminal aberto. Você também pode acessar a documentação interativa da API em `http://127.0.0.1:8000/docs`.

### 3. Terminal 2: Usar o Cliente (Frontend)

O arquivo `cliente.py` é um script de linha de comando para interagir com a API. Você pode executá-lo em um novo terminal (na mesma pasta `To-do-list`):
```bash
# Para LISTAR todas as tarefas:
python cliente.py listar

# Para ADICIONAR uma nova tarefa (use aspas):
python cliente.py adicionar "Comprar leite"
python cliente.py adicionar "Estudar para a prova de APIs"

# Para ver a ajuda:
python cliente.py
```

## 📖 Endpoints da API

A API fornece os seguintes endpoints para gerenciar tarefas (conforme `main_api.py`):

### Listar todas as tarefas

* **GET** `/tarefas`
* **Descrição:** Retorna um dicionário com todas as tarefas cadastradas.

### Obter uma tarefa por ID

* **GET** `/tarefas/{item_id}`
* **Descrição:** Retorna uma única tarefa com base no ID fornecido.

### Obter próximas tarefas

* **GET** `/tarefas/proximos`
* **Descrição:** Retorna uma lista de tarefas com data de vencimento futura.

### Adicionar uma nova tarefa

* **POST** `/tarefas`
* **Descrição:** Adiciona uma nova tarefa à lista.
* **Corpo da Requisição (JSON):**
```json
  {
    "tarefa": "Estudar para a prova",
    "data": "2025-12-01",
    "hora": "14:00"
  }
```

### Remover uma tarefa

* **DELETE** `/tarefas/{item_id}`
* **Descrição:** Remove uma tarefa da lista com base no ID fornecido.