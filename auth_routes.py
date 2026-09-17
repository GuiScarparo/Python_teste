from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth', tags=['Auth'])

@auth_router.get("/")
async def autenticar():
    """
    Todas as rotas de autenticação devem ser acessadas através desta rota.
    """
    return {"message": "você acessou a rota padrão de autenticação", "autenticação": False}