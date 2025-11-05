# [cite_start]Mini Projeto 3: Consumo de APIs - Lista de Tarefas [cite: 1]

[cite_start]Este repositório contém o "Terceiro Mini Projeto" da Fatec Rio Claro, focado no tema "Consumo de APIs"[cite: 2, 3].

[cite_start]O objetivo do projeto é implementar um servidor de API (backend) em Python e um cliente (frontend) que consome os dados dessa API[cite: 7]. [cite_start]A colaboração foi realizada seguindo o requisito de contribuição via Pull Requests no GitHub[cite: 9].

## 📝 Tema: API de Lista de Tarefas (To-Do List)

Foi implementada uma API RESTful simples para gerenciar uma lista de tarefas (To-Do List). O servidor permite criar e listar tarefas. Os dados são armazenados em memória (em uma lista Python) enquanto o servidor está em execução.

## 🛠️ Tecnologias Utilizadas

* [cite_start]**Servidor (Backend):** Python 3, **FastAPI**[cite: 8], **Uvicorn**
* [cite_start]**Cliente (Frontend):** Python 3, **Requests** [cite: 8]
* [cite_start]**Colaboração:** Git e GitHub (Fork & Pull Requests) [cite: 9]

## 📂 Estrutura de Diretórios

[cite_start]O projeto segue a estrutura de diretórios sugerida no documento da atividade [cite: 10-25]:

```
projeto-api-tarefas/
├── .gitignore
├── README.md
├── requirements.txt   # Dependências do projeto (FastAPI, Uvicorn, Requests)
[cite_start]├── server/            [cite: 13]
[cite_start]│   └── app/           [cite: 14]
[cite_start]│       └── main.py    # O servidor FastAPI (Backend) [cite: 15]
[cite_start]└── client/            [cite: 21]
    [cite_start]└── main.py        # O cliente 'requests' (Frontend) [cite: 22]
```

*(Nota: O `cliente.py` do nosso plano deve ser este `client/main.py`, e o `main_api.py` deve ser este `server/app/main.py`)*

## 🚀 Como Executar o Projeto

Para rodar o projeto, você precisará de **dois terminais** abertos simultaneamente.

### 1. Pré-requisitos

1.  Clone este repositório:
    ```bash
    git clone [URL-DO-SEU-REPOSITÓRIO]
    cd projeto-api-tarefas
    ```

2.  (Opcional, mas recomendado) Crie um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: .\venv\Scripts\activate
    ```

3.  Instale as dependências (FastAPI, Uvicorn e Requests):
    ```bash
    pip install -r requirements.txt
    ```

### 2. Terminal 1: Rodar o Servidor (Backend)

Neste terminal, vamos iniciar o servidor FastAPI.

```bash
# Navegue até a pasta do servidor
cd server/app

# Inicie o servidor Uvicorn
# (Ele irá recarregar automaticamente se você mudar o código)
uvicorn main:app --reload
```

O terminal deve mostrar que o servidor está rodando em `http://127.0.0.1:8000`. **Deixe este terminal aberto.**

### 3. Terminal 2: Usar o Cliente (Frontend)

Abra um **novo terminal** na pasta raiz do projeto.

```bash
# Navegue até a pasta do cliente
cd client
```

Agora você pode usar o cliente para interagir com a API:

```bash
# Para ADICIONAR uma nova tarefa:
python main.py adicionar "Comprar pão"
python main.py adicionar "Estudar para a prova de APIs"

# Para LISTAR todas as tarefas:
python main.py listar

# Para ver os comandos disponíveis:
python main.py
```

## 👥 Colaboração

[cite_start]Este projeto foi desenvolvido em dupla, seguindo o requisito de contribuição via Pull Requests[cite: 9].

* **Dono do Repositório:** [Nome ou @UsuárioGitHub da Pessoa A]
* **Colaborador:** [Nome ou @UsuárioGitHub da Pessoa B]

O fluxo de trabalho seguiu o modelo Fork & Pull Request para registrar as contribuições de cada integrante.