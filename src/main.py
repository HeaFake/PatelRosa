#Erica Cristina Silva Chagas

from fastapi import FastAPI
from settings import HOST, PORT, RELOAD
import uvicorn

from routers import FuncionarioRouter
from routers import ClienteRouter
from routers import ProdutoRouter

app = FastAPI()

# inclusão das rotas
app.include_router(FuncionarioRouter.router)
app.include_router(ClienteRouter.router)
app.include_router(ProdutoRouter.router)

@app.get("/", tags=["Root"])
def root():
    return {
        "msg": "API Pastelaria do Zé",
        "docs": "http://localhost:8000/docs"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=int(PORT), reload=RELOAD)