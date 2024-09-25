from src.main import *


def test_root():
    result = root()
    yield result
    assert result == {"message": "Use as portas: /soma, /subtracao, /multiplicacao, /divisao ou /docs para usar interface interativa!"}

def test_soma(a: float, b: float):
    assert soma() == {"resultado": a + b}

def test_subtracao(a: float, b: float):
    assert subtracao() == {"resultado": a - b}

def test_multiplicacao(a: float, b: float):
    assert multiplicacao() == {"resultado": a * b}

def test_divisao(a: float, b: float):
    assert divisao() == {"resultado": a / b}