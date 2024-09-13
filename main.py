from fastapi import FastAPI, HTTPException

app = FastAPI()




# Rota para a soma
@app.get("/soma")
def soma(a: float, b: float):
    return {"resultado": a + b}

# Rota para a subtração
@app.get("/subtracao")
def subtracao(a: float, b: float):
    return {"resultado": a - b}
