from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_name}")
async def get_item_by_id(item_name: str):
    return {"message": f"Você buscou o item: {item_name}"}


# Rota com Query Parameters
@app.get("/items/")
async def search_items(query: str, limit: int = 10):
    return {
        "message": f"Resultados para '{query}' com limite de {limit} itens"
    }

@app.get("/")
async def root():
    return {"message": "Hello World"}

