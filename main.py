from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Use as portas: /soma, /subtracao, /multiplicacao, /divisao ou /docs para usar interface interativa!"}

@app.get("/soma")
def soma(a: float, b: float):
    return {"resultado": a + b}

@app.get("/subtracao")
def subtracao(a: float, b: float):
    return {"resultado": a - b}

@app.get("/multiplicacao")
def multiplicacao(a: float, b: float):
    return {"resultado": a * b}

@app.get("/divisao")
def divisao(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Divisão por zero não é permitida.")
    return {"resultado": a / b}
