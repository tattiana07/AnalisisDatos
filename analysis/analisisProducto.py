from generators.generadorProducto import generarDatosProductos
import pandas as pd

def analizarDatos():
    datos=generarDatosProductos()
    tabla=pd.DataFrame(datos,columns=["productos","categoria"])
    tabla.to_csv("./data/tipoProductos.csv",index=False)
analizarDatos()