import Pyro5.api

ns = Pyro5.api.locate_ns(host="localhost", port=9090)  # IP del servidor que corre el Name Server
uri = ns.lookup("ejemplo.calculadora")
calculadora = Pyro5.api.Proxy(uri)

continuar = True

while continuar:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        resultado = calculadora.suma(a, b)
        print(f"Resultado de la suma: {resultado}")

    elif opcion == "2":
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        resultado = calculadora.resta(a, b)
        print(f"Resultado de la resta: {resultado}")

    elif opcion == "3":
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        resultado = calculadora.multiplicacion(a, b)
        print(f"Resultado de la multiplicación: {resultado}")

    elif opcion == "4":
        continuar = False
    else:
        print("Opción no válida. Intente nuevamente.")

    print()  # Espacio en blanco para mejorar la legibilidad

