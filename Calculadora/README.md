# Servicio RMI Calculadora
Este servicio permite realizar operaciones de Suma, Resta y Multiplicación entre dos numeros enteros. Para ello se implementa un servidor que expone los metodos de la calculadora y un cliente que consume el servicio.

## Requisitos
- python 3.8 o superior
- Pyro5 `pip install Pyro5`

## Explicación
- `client/client.py`: Contine una llamada al servicio de calculadora, donde se pueden las configuraciones de la IP y el puerto del servidor. (por defecto Pyro5 utiliza el puerto 9090)

- `server/main.py`: Contiene la implementación del servicio de calculadora, donde se definen los metodos de suma, resta y multiplicación. Podemos observar como establece conexion al servidor de nombres de Pyro5 y lo registra para futuras llamadas.

## Ejecución

1. Iniciar el servidor de nombres de Pyro5:
```bash
python -m Pyro5.nameserver
```
2. Iniciar el servidor de la calculadora en una terminal nueva (carpeta `server`):

```bash
python main.py
```

3. Iniciar el cliente de la calculadora en otra terminal nueva (carpeta `client`):

```bash
python client.py
```



