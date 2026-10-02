import threading  # Librería que permite trabajar con hilos

# Cantidad de boletos disponibles para la compra
boletos_disponibles = 10

# Lock para controlar el acceso a los boletos
lock = threading.Lock()


# Función que representa la compra de boletos de cada usuario
def comprar_boletos(usuario, cantidad):
    global boletos_disponibles

    # Muestra la intención de compra del usuario
    print(usuario, "quiere comprar", cantidad, "boletos")

    # Sección crítica: solo un hilo puede entrar aquí a la vez
    with lock:

        # Verificamos si todavía hay suficientes boletos
        if cantidad <= boletos_disponibles:

            # Actualizamos la cantidad de boletos disponibles
            boletos_disponibles -= cantidad

            print(usuario, "realizó la compra.",
                  "Boletos restantes:", boletos_disponibles)

        else:

            # Si no hay suficientes boletos, no se realiza la compra
            print(usuario, "no pudo comprar.",
                  "No hay suficientes boletos.")


# Usuarios que intentan comprar boletos
# Cada usuario será representado por un hilo
usuarios = [
    ("Ana", 3),
    ("Carlos", 4),
    ("Laura", 2),
    ("Pedro", 5),
    ("Sofia", 3)
]


# Lista donde guardamos los hilos creados
hilos = []


# Crear y ejecutar los hilos
for usuario, cantidad in usuarios:

    hilo = threading.Thread(
        target=comprar_boletos,
        args=(usuario, cantidad)
    )

    hilos.append(hilo)

    # Iniciar el hilo
    hilo.start()


# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()


# Mostrar la cantidad de boletos que quedaron disponibles
print("Boletos disponibles al final:", boletos_disponibles)