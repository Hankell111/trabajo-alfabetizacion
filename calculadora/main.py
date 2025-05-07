from suma import sumar
from resta import restar
from multiplicacion import multiplicar
from division import dividir

def main():
    print("Bienvenido a la calculadora.")
    print("Opciones: suma, resta, multiplicacion, division")

    opcion = input("Elige una operación: ").lower()
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))

    if opcion == "suma":
        print("Resultado:", sumar(a, b))
    elif opcion == "resta":
        print("Resultado:", restar(a, b))
    elif opcion == "multiplicacion":
        print("Resultado:", multiplicar(a, b))
    elif opcion == "division":
        print("Resultado:", dividir(a, b))
    else:
        print("Operación no válida.")

if __name__ == "__main__":
    main()

