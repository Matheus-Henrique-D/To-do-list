from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import date
from tarefas import adicionar_tarefa, todo

app = FastAPI(
)

class Tarefa(BaseModel):
    tarefa: str
    data: Optional[str] = None
    hora: Optional[str] = None

@app.get("/tarefas", summary="Listar todas as tarefas")
async def listar_tarefas():
    return todo

@app.get("/tarefas/{item_id}", summary="Obter uma tarefa por ID")
async def obter_tarefa(item_id: int):
    if item_id not in todo:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return todo[item_id]

@app.get("/tarefas/proximos", summary="Obter próximas tarefas")
async def obter_tarefas_proximas():
    hoje = date.today()
    tarefas_proximas = []
    for tarefa in todo.values():
        if tarefa.get("data"):
            try:
                data_tarefa = date.fromisoformat(tarefa["data"])
                if data_tarefa >= hoje:
                    tarefas_proximas.append(tarefa)
            except (ValueError, TypeError):
                continue

    def obter_data(tarefa):
        return date.fromisoformat(tarefa["data"])

    tarefas_proximas.sort(key=obter_data)

    return tarefas_proximas

@app.post("/tarefas", summary="Adicionar uma nova tarefa")
async def adicionar_nova_tarefa(tarefa: Tarefa):
    nova_tarefa = adicionar_tarefa(tarefa.dict())
    return nova_tarefa

@app.delete("/tarefas/{item_id}", summary="Remover uma tarefa")
async def remover_tarefa(item_id: int):
    if item_id not in todo:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    del todo[item_id]
    return {"message": f"Tarefa {item_id} removida com sucesso!"}
