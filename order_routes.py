from fastapi import APIRouter

order_router = APIRouter(prefix='/pedidos', tags=['pedidos'])

@order_router.get('/')
async def pedidos():
    """
    Para acessa toda e quaisquer rota de pedido é necessario autenticação previa
    """
    return {"message": "você acessou a rota de pedidos"}
