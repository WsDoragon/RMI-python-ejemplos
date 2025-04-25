import Pyro5.api

@Pyro5.api.expose
class MatrizServicio:
    def multiplicar(self, A, B):
        if len(A[0]) != len(B):
            raise ValueError("Columnas de A deben coincidir con filas de B.")

        resultado = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    resultado[i][j] += A[i][k] * B[k][j]

        return resultado