#Nombre: Eduardo Castañón Silva
#Aplicación API-REST

import requests 
#API de productos de DummyJson 

BASE_URL = "https://dummyjson.com/products"

def mostrar_respuesta(respuesta):
    #Mostrar datos del código https y los datos recibidos.
    print("Código HTTP", respuesta.status_code)

    if respuesta.text:
        print("Respuesta Json:")
        print(respuesta.json())

    else:
        print("la respuesta no tiene datos") 

try:
    # ============================
    # 1. GET:Consultar un Producto
    # ============================
    respuesta = requests.get(
        f"{BASE_URL}/12",
        timeout=10
    )

    respuesta.raise_for_status()
    producto = respuesta.json()

    print("Producto", producto["title"])
    print("Precio", producto["price"])
    print("Categoría", producto["category"])
# ==========================
#      2. Método Post
# ==========================
except requests.exceptions.timeout:
    print("Error: se agotó el tiempo de espera")