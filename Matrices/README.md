## Servicio RMI de Matrices
Este servicio permite realizar la operación de multiplicación de matrices.

## Requisitos
- Python 3.8 o superior
- Pyro5 `pip install Pyro5`

## Explicación

- `client/client.py`: Contiene una llamada al servicio de multiplicación de matrices.

- `server/main.py`: Contiene la configuracion del servidor de matrices, donde se define la configuracion para añadirlo al servidor de nombres de Pyro5 en su valor por defecto (host: localhost | port: 9090).

    Funcion expuesta por el servidor (`server/servicioMatrices.py`):

    * **Multiplicar:** Recibe dos matrices y devuelve el resultado de su multiplicación. Si las matrices no son compatibles, se lanza una excepción que recibe el cliente.

## Ejecución

1. Iniciar el servidor de nombres de Pyro5:
```bash
python -m Pyro5.nameserver
```

2. Iniciar el servidor de matrices en una terminal nueva (carpeta `server`):
```bash
python main.py
```

3. Iniciar el cliente de matrices en otra terminal nueva (carpeta `client`):
```bash
python client.py
```
