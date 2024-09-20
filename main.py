from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/inicio")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# PATH PARAMS

@app.get("/parametros/{nombre}")
def get_parametros(nombre):
    return {"Nombre" : nombre}


@app.get("/incremento/{numero}")
def get_incremento(numero : int):
    numero = numero + 1
    return {"Resultado" : numero}




# QUERY PARAMS

@app.get("/suma")
def get_suma(num1: float, num2: float):
    resultado = num1 + num2
    return {
        "resultado": resultado
    }
# /suma?num1=5&num2=10