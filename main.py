import logging
from abc import ABC, abstractmethod

# CONFIGURACION DE LOGS
logging.basicConfig(
    filename="errores.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("Sistema Software FJ")


# EXCEPCION PERSONALIZADA
class ReservaError(Exception):
    pass


# CLASE CLIENTE
class Cliente:

    def __init__(self, nombre, documento, correo):

        if nombre == "":
            raise ValueError("El nombre no puede estar vacío")

        if "@" not in correo:
            raise ValueError("Correo inválido")

        self.nombre = nombre
        self.documento = documento
        self.correo = correo

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Documento:", self.documento)
        print("Correo:", self.correo)


# CLASE ABSTRACTA SERVICIO
class Servicio(ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self):
        pass


# SERVICIO 1
class ReservaSala(Servicio):

    def calcular_costo(self):
        return self.precio * 2

    def describir(self):
        return "Servicio de reserva de salas"


# SERVICIO 2
class AlquilerEquipo(Servicio):

    def calcular_costo(self):
        return self.precio * 1.5

    def describir(self):
        return "Servicio de alquiler de equipos"


# SERVICIO 3
class AsesoriaEspecializada(Servicio):

    def calcular_costo(self):
        return self.precio * 3

    def describir(self):
        return "Servicio de asesorias especializadas"


# CLASE RESERVA
class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ReservaError(
                "La duración debe ser mayor a cero"
            )

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion

    def confirmar(self):

        print("Reserva confirmada para", self.cliente.nombre)
        print("Servicio:", self.servicio.nombre)
        print("Duración:", self.duracion, "horas")

    def cancelar(self):
        print("Reserva cancelada")

    def procesar(self):
        print("Procesando reserva...")


# CLIENTE VALIDO
cliente1 = Cliente(
    "Sergio Diaz Caceres",
    "1012424097",
    "sergiodiaz1224@gmail.com"
)

cliente1.mostrar_datos()


# CLIENTE INVALIDO
try:

    cliente_error = Cliente(
        "",
        "1012424097",
        "sergiodiaz1224@gmail.com"
    )

except ValueError as e:

    print("Error:", e)
    logging.error(e)


# SERVICIOS
sala = ReservaSala(
    "Sala Principal",
    100
)

equipo = AlquilerEquipo(
    "Computador",
    100
)

asesoria = AsesoriaEspecializada(
    "Redes",
    100
)

print("Costo sala:", sala.calcular_costo())
print("Costo equipo:", equipo.calcular_costo())
print("Costo asesoria:", asesoria.calcular_costo())

print(sala.describir())
print(equipo.describir())
print(asesoria.describir())


# RESERVA VALIDA
cliente2 = Cliente(
    "Sergio Diaz",
    "1012424097",
    "sergiodiaz1224@gmail.com"
)

reserva1 = Reserva(
    cliente2,
    sala,
    2
)

reserva1.confirmar()


# RESERVA INVALIDA
try:

    reserva_error = Reserva(
        cliente2,
        sala,
        -1
    )

except ReservaError as e:

    print("Error de reserva:", e)
    logging.error(e)


# TRY - EXCEPT - ELSE
try:

    numero = int("10")

except ValueError:

    print("Error de conversión")

else:

    print("Conversión correcta")


# TRY - EXCEPT - FINALLY
try:

    numero = int("abc")

except ValueError:

    print("Valor inválido")

finally:

    print("Proceso finalizado")


# PRUEBAS DEL SISTEMA
print("\n------ PRUEBAS DEL SISTEMA ------")

try:

    cliente3 = Cliente(
        "Carlos Perez",
        "123456",
        "carlos@gmail.com"
    )

    print("Cliente registrado correctamente")

except Exception as e:

    print(e)

try:

    cliente4 = Cliente(
        "Laura",
        "654321",
        "lauragmail.com"
    )

except Exception as e:

    print("Error:", e)

try:

    cliente5 = Cliente(
        "",
        "111111",
        "correo@gmail.com"
    )

except Exception as e:

    print("Error:", e)

try:

    reserva2 = Reserva(
        cliente2,
        sala,
        3
    )

    reserva2.confirmar()

except Exception as e:

    print(e)

try:

    reserva3 = Reserva(
        cliente2,
        sala,
        0
    )

except Exception as e:

    print("Error:", e)

reserva1.cancelar()
reserva1.procesar()

print("\n--- FIN DE LAS PRUEBAS ---")