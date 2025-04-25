# Servicio RMI en Python

Los codigos de ejemplo incluidos en este repositorio contienen implementaciones de un servicio RMI en Python utilizando la libreria Pyro5, con la cual se simulan los servicios RMI de Java.

## Requisitos
- python 3.8 o superior
- Pyro5 `pip install Pyro5`
    - [Documentacion Pyro5](https://pyro5.readthedocs.io/en/latest/index.html)

## Ejecución
Cada carpeta contiene un readme dedicado a explicar como se ejecutan los codigos, estos deben ejecutarse en un orden especifico y siempre mantener un servidor de nombres de Pyro5 en ejecucion.
### Codigos:
* **Calculadora:** Implementacion de una calculadora que permite realizar operaciones de Suma - Resta - Multiplicación.
* **Matrices:** Implementacion de operacion de multiplicación sobre matrices.
* **Chat:** Implementacion de Chat entre multiples clientes, que acceden a servicios RMI, mediante un servidor el cual recibe mensajes y ejecuta servicios RMI establecidos por los clientes registrados para entregar los mensajes.
