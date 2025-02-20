def add(a: float, b:float) -> float:
    return a + b

def sub(a: float, b: float) -> float:
    return a - b

def mult(a: float, b: float) -> float:
    return a * b

def div(a: float, b: float) -> float:
    assert b != 0, "division error"
    return a / b
