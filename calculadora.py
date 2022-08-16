#calculadora con funciones

def sumar(a,b):
    return a+b


def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b





while True:
    print("""\tCalculadora
1.Sumar
2.Restar
3.Multiplicar
4.dividir 
5. Salir""")
    opcion = int(input("Digite una opcion: "))
    print()
    if opcion==1:
        a = int(input("Digite el primer numero: "))
        b = int(input("Digite el segundo numero: "))
        print(f"La suma de {a} + {b} = {sumar(a,b)}")
    elif opcion==2:
        a= int(input("Digite el primer numero: "))
        b= int(input("Digite el segundo numero: "))
        print(f"La resta de {a} - {b} = {restar(a,b)}")
    elif opcion==3:
        a = int(input("Digite el primer numero: "))
        b = int(input("Digite el segundo numero: "))
        print(f"la multiplicacion de {a} * {b} = {multiplicar(a,b)}")
    elif opcion==4:
        a = int(input("Digite el primer numero: "))
        b = int(input("Digite el segundo numero: "))
        print(f"la division es de {a} / {b} = {dividir(a,b)}")
    elif opcion ==5:
        break
    else:
        print("Se equivoco de opcion")
    print()
