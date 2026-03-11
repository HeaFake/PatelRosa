#Erica Cristina Silva Chagas

from fastapi import APIRouter
from domain.schemas.ProdutoSchema import ProdutoCreate, ProdutoUpdate, ProdutoResponse

router = APIRouter()

@router.get("/produto/", tags=["Produto"])
def get_produto():
    return {"msg": "produto get todos executado"}

@router.get("/produto/{id}", tags=["Produto"])
def get_produto_id(id: int):
    return {"msg": "produto get um executado", "id": id}

@router.post("/produto/", tags=["Produto"])
def post_produto(corpo: ProdutoCreate):
    return {
        "msg": "produto criado",
        "nome": corpo.nome,
        "valor": corpo.valor_unitario
    }

@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int, corpo: ProdutoUpdate):
    return {
        "msg": "produto atualizado",
        "id": id,
        "nome": corpo.nome
    }

@router.delete("/produto/{id}", tags=["Produto"])
def delete_produto(id: int):
    return {"msg": "produto deletado", "id": id}