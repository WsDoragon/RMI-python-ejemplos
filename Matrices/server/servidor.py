import Pyro5.api
from matrices import MatrizServicio

def main():
    daemon = Pyro5.api.Daemon()
    uri = daemon.register(MatrizServicio)

    ns = Pyro5.api.locate_ns()
    ns.register("matriz.servicio", uri)

    print("Servidor de matrices activo. URI:", uri)
    daemon.requestLoop()

if __name__ == "__main__":
    main()