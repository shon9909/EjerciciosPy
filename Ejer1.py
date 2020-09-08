def edad(edad2, x):
    respueta=edad2+(2070-x)
    return respueta
def main():
    g=1
    while g != 2:
        print("Bienvenido al programa de la Edad")
        edad2 =int(input("ingrese su edad: "))
        if edad2 < 0:
            print("El valor de la edad es menor que 0")
            g=2
        else:
            x = int(input("ingrese año actual: "))
            if x<0:
                print("El valor del año es menor que 0")
                g=2
            else:
                respueta=edad(edad2, x)
                print("Tu edad en el 2070 es: ", respueta)
if __name__ == '__main__':
    main()