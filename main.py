from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Para testar a calculadora use as portas: /soma, /subtracao"}

@app.get("/multiplicacao")
def multiplicacao(a: float, b: float):
    return {"resultado": a * b}

@app.get("/divisao")
def divisao(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Divisão por zero não é permitida.")
    return {"resultado": a / b}