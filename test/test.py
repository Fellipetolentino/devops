from src.main import *


def test_root():
    result = root()
    yield result
    assert result == {"message": "Use as portas: /soma, /subtracao, /multiplicacao, /divisao ou /docs para usar interface interativa!"}

def test_soma():
    result = soma()
    yield result
    assert result == {"resultado": 10 + 5}

def test_subtracao():
    result = subtracao()
    yield result
    assert result == {"resultado": 11 - 10}

def test_multiplicacao():
    result = multiplicacao()
    yield result
    assert result == {"resultado": 5 * 5}

def test_divisao():
    result = divisao()
    yield result
    assert result == {"resultado": 10 / 2}