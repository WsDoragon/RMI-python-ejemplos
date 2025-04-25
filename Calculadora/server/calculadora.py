import Pyro5.api

@Pyro5.api.expose
class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b
    
    def multiplicacion(self, a, b):
        return a * b