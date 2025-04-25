import Pyro5.api
from calculadora import Calculadora

def main():
    daemon = Pyro5.api.Daemon() # Crear un daemon Pyro
    uri = daemon.register(Calculadora) # Registrar la clase Calculadora
    print("URI del objeto:", uri)

    ns = Pyro5.api.locate_ns(host="localhost", port=9090)
    ns.register("ejemplo.calculadora", uri)

    print("Servicio RMI Python corriendo...")
    daemon.requestLoop()

if __name__ == "__main__":
    main()