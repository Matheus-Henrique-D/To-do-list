import requests
import sys

# URL da API. Certifique-se de que esta é a URL correta do servidor do seu colega.
API_URL = "http://127.0.0.1:8000"

def listar_tarefas():
    """
    Busca e exibe todas as tarefas no servidor.
    """
    print("Buscando tarefas no servidor...")
    try:
        resposta = requests.get(f"{API_URL}/tarefas")
        # Lança uma exceção se a resposta for um erro (4xx ou 5xx)
        resposta.raise_for_status()
        
        tarefas = resposta.json()
        
        if not tarefas:
            print("Nenhuma tarefa encontrada no servidor.")
            return
            
        print("\n--- Lista de Tarefas ---")
        # Assumindo que cada tarefa é um dicionário com 'id' e 'descricao'
        for tarefa in tarefas:
            print(f"  ID: {tarefa.get('id', '?')} | Descrição: {tarefa.get('descricao', 'Sem descrição')}")
        print("------------------------\n")

    except requests.exceptions.ConnectionError:
        print(f"\n[ERRO] Não foi possível conectar ao servidor em {API_URL}.")
        print("Verifique se o servidor está rodando e se a URL está correta.")
    except requests.exceptions.RequestException as e:
        print(f"\n[ERRO] Ocorreu um problema com a requisição: {e}")

def adicionar_tarefa(descricao):
    """
    Envia uma nova tarefa para o servidor.
    """
    if not descricao:
        print("[ERRO] A descrição da tarefa não pode ser vazia.")
        return

    print(f"Adicionando nova tarefa: '{descricao}'")
    # O formato do dicionário deve ser o que o servidor espera
    dados = {"descricao": descricao}
    
    try:
        resposta = requests.post(f"{API_URL}/tarefas", json=dados)
        resposta.raise_for_status()
        
        # 201 Created é o status ideal para um POST que cria um recurso
        if resposta.status_code == 201 or resposta.status_code == 200:
            print("\nTarefa adicionada com sucesso!")
            tarefa_criada = resposta.json()
            print(f"  ID: {tarefa_criada.get('id', '?')} | Descrição: {tarefa_criada.get('descricao', '?')}")
        else:
            print(f"\nFalha ao adicionar tarefa. O servidor respondeu com status: {resposta.status_code}")

    except requests.exceptions.ConnectionError:
        print(f"\n[ERRO] Não foi possível conectar ao servidor em {API_URL}.")
        print("Verifique se o servidor está rodando e se a URL está correta.")
    except requests.exceptions.RequestException as e:
        print(f"\n[ERRO] Ocorreu um problema com a requisição: {e}")

def mostrar_ajuda():
    """
    Exibe a mensagem de ajuda com os comandos disponíveis.
    """
    print("\nUso: python cliente.py [comando] [argumentos]")
    print("\nComandos:")
    print("  listar                  - Lista todas as tarefas.")
    print("  adicionar \"<descricao>\" - Adiciona uma nova tarefa com a descrição fornecida.")
    print("\nExemplos:")
    print("  python cliente.py listar")
    print("  python cliente.py adicionar \"Fazer compras para o jantar\"")

# --- O \"Cérebro\" (Controle Principal) ---
if __name__ == "__main__":
    # sys.argv contém os argumentos da linha de comando
    # sys.argv[0] é o nome do script ("cliente.py")
    # sys.argv[1] seria o comando ("listar", "adicionar")
    
    if len(sys.argv) < 2:
        mostrar_ajuda()
        sys.exit(1) # Sai do script indicando um erro

    comando = sys.argv[1].lower()

    if comando == "listar":
        listar_tarefas()
    elif comando == "adicionar":
        if len(sys.argv) > 2:
            # Pega todos os argumentos depois de "adicionar" e os junta em uma única string
            descricao_da_tarefa = " ".join(sys.argv[2:])
            adicionar_tarefa(descricao_da_tarefa)
        else:
            print("\n[ERRO] O comando 'adicionar' precisa de uma descrição.")
            mostrar_ajuda()
    else:
        print(f"\n[ERRO] Comando '{comando}' não reconhecido.")
        mostrar_ajuda()
