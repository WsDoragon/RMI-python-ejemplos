import Pyro5.api

def main():
    ns = Pyro5.api.locate_ns()
    uri = ns.lookup("matriz.servicio")
    servicio = Pyro5.api.Proxy(uri)

    A = [
        [1, 2, 3],
        [3, 4, 5],
        
    ]

    B = [
        [5, 6, 7],
        [7, 8, 9],
        [7, 8, 9]
    ]

    resultado = servicio.multiplicar(A, B)

    print("Resultado de A * B:")
    for fila in resultado:
        print(fila)

if __name__ == "__main__":
    main()