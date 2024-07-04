import random

def generarDatosProductos():
    productos=["Musica","Tv","App","Pc","Cel","Tablet","Accesorios"]
    datos=[]
    for producto in productos:
        tipoProducto={}
        categoria=random.choice(["Plus","Mega","Basic"])
        tipoProducto=[producto,categoria]
        datos.append(tipoProducto)

    return datos
print(generarDatosProductos())
    