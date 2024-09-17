class informacion:

    def mi_lista(self):
        print("---Lista---")
        lista_nomperros=["Body","Dollar","Fany"]
        for x in lista_nomperros:
            print(x)

    def mi_tupla(self):
        print("---Tupla Color---")
        tupla_colperros=("Cafe","Negro","Blanco")
        for x in tupla_colperros:
            print(x)

    def mi_conjunto(self):
        print("---Conjunto Edades---")
        con_edaperros={"5","7","11"}
        for x in con_edaperros:
            print(x)

    def mi_diccionario(self):
        print("---Diccionario Razas---")
        lista_razperros={
        "body": "Pastor",
        "Dollar": "Rottweiler",
        "Fany": "Chihuahua"
        }
        for x,y in lista_razperros.items():
            print(x,y)

# creando el objeto

datos=informacion()
print("Listado de nombres de perros")
datos.mi_lista()
datos.mi_tupla()
datos.mi_conjunto()
datos.mi_diccionario()