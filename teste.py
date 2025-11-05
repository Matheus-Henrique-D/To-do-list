import requests
import json

# URL base da API de teste
BASE_URL = 'https://jsonplaceholder.typicode.com'

def listar_posts():
    """Busca e exibe o título de todos os posts."""
    try:
        response = requests.get(f"{BASE_URL}/posts")
        response.raise_for_status()  # Lança um erro para códigos de status ruins (4xx ou 5xx)
        posts = response.json()
        print("\n--- Lista de Posts ---")
        for post in posts[:10]:  # Mostra os 10 primeiros para não poluir a tela
            print(f"ID: {post['id']}, Título: {post['title']}")
        print("----------------------\n")
        return posts
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar posts: {e}")
        return None

def ver_post(post_id):
    """Busca e exibe um post específico."""
    try:
        response = requests.get(f"{BASE_URL}/posts/{post_id}")
        response.raise_for_status()
        post = response.json()
        print("\n--- Detalhes do Post ---")
        print(json.dumps(post, indent=2))
        print("------------------------\n")
        return post
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar o post {post_id}: {e}")
        return None

def modificar_post(post_id):
    """Modifica o título e o corpo de um post existente."""
    print(f"\n--- Modificando Post ID: {post_id} ---")
    novo_titulo = input("Digite o novo título: ")
    novo_corpo = input("Digite o novo corpo: ")

    dados_atualizados = {
        'title': novo_titulo,
        'body': novo_corpo
    }

    try:
        response = requests.patch(f"{BASE_URL}/posts/{post_id}", json=dados_atualizados)
        response.raise_for_status()
        print("\n--- Post Modificado com Sucesso ---")
        print(json.dumps(response.json(), indent=2))
        print("------------------------------------\n")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao modificar o post: {e}")

def main():
    """Função principal que executa o menu interativo."""
    while True:
        print("O que você gostaria de fazer?")
        print("1: Ver lista de posts")
        print("2: Ver um post específico")
        print("3: Modificar um post")
        print("4: Sair")
        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            listar_posts()
        elif escolha == '2':
            post_id = input("Digite o ID do post que você quer ver: ")
            if post_id.isdigit():
                ver_post(int(post_id))
            else:
                print("ID inválido.")
        elif escolha == '3':
            post_id = input("Digite o ID do post que você quer modificar: ")
            if post_id.isdigit():
                modificar_post(int(post_id))
            else:
                print("ID inválido.")
        elif escolha == '4':
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()