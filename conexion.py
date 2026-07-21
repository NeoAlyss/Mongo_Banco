from pymongo import MongoClient


def conectar():
    client = MongoClient("mongodb://localhost:27017")
    db = client["banco"]
    coleccion = db["clientes"]
    return coleccion

