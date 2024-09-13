from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Para testar a calculadora use a porta /soma"}

# Rota para a soma
@app.get("/soma")
def soma(a: float, b: float):
    return {"resultado": a + b}

# Rota para a subtração
@app.get("/subtracao")
def subtracao(a: float, b: float):
    return {"resultado": a - b}

# Rota para a multiplicação
@app.get("/multiplicacao")
def multiplicacao(a: float, b: float):
    return {"resultado": a * b}
