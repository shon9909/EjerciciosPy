def caracter(palabra):
    inicial=palabra[0]
    final=palabra[len(palabra)-1]
    print("Los caracteres de la palabra ", palabra,"son:\nInicial: ",inicial,"\nFinal: ", final)
    return inicial+final
def main():
    print("Bienvenido al programa para determinar caracter inicial y final")
    palabra =input("ingrese el la palabra: ")
    caracter(palabra)
if __name__ == '__main__':
    main()