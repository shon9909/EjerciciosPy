def par(entero):
    respuesta=entero%2
    if respuesta==0:
        return True
    else:
        return False
def main():
    print("Bienvenido al programa para saber si es par o no")
    entero =int(input("ingrese el numero: "))
    respueta=par(entero)
    print("True: Par\nFalse: Impar\nLa respuesta es: ", respueta)
if __name__ == '__main__':
    main()