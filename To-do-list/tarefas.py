todo = {} 
proximo_id = 1

def adicionar_tarefa(dados_da_tarefa):
    global proximo_id 
    if dados_da_tarefa is None:
        raise ValueError("Sem tarefa informada, tente novamente")
    id_atual = proximo_id

    nova_tarefa = {
        "id": id_atual,
        "tarefa": dados_da_tarefa["tarefa"],
        "data": dados_da_tarefa.get("data", None),
        "hora": dados_da_tarefa.get("hora", None)
    }
    
    todo[id_atual] = nova_tarefa
    proximo_id += 1
    return nova_tarefa
