from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Para testar a calculadora use a porta /soma, /subtracao, /multiplicacao e /divisao"}

