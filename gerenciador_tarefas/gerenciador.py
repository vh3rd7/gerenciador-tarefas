from fastapi import FastAPI

app = FastAPI()
TAREFAS = []

"""
TAREFAS = [
    {
        "id": 1,
        "titulo": "titulo",
        "descricao": "descrição",
        "estado": "finalizado",
    },
    {
        "id": 2,
        "titulo": "titulo2",
        "descricao": "descrição",
        "estado": "finalizado",
    }
]
"""

@app.get("/tarefas")
def listar_tarefas():
    # "", [], TAREFAS
    return TAREFAS