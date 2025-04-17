import time
# Tecnicas de programacion orientada a objetos

"""
Herencia (multiple)
- La herencia es un mecanismo que permite crear una nueva clase a partir de una clase existente.
Polimorfismo
- El polimorfismo es la capacidad de un objeto de tomar muchas formas.
    En Python, esto se logra mediante la sobrecarga de métodos y la sobrecarga de operadores.
Abstraccion
- La abstracción es el proceso de ocultar los detalles de implementación y 
    mostrar solo la funcionalidad esencial.
Encapsulacion
- La encapsulación 
"""

# class Individuo:
#     """Clase abstracta"""
#     def __init__(self, nombre, apellido):
#         self.nombre = nombre
#         self.apellido = apellido

#     def ver_caracter(self):
#         pass


# class Persona(Individuo):
#     def ver_caracter(self):
#         return 'Mal caracter'

#     def ejemplo_objeto(self):
#         print("Imprimimos la referencia a si mismo")
#         print(id(self))
#         return self


# class Emplado(Persona):
#     pass


# persona = Persona("Juan", "Perez")
# print(persona)
# print(id(persona))


# print(id(persona.ejemplo_objeto()))





class Persona:
    def __init__(self, auto):
        self.auto = auto

    def acelerar(self, tope):
        # Ejecutar una acción
        self.auto.acelerar(tope)


class Auto:
    def __init__(self, marca, modelo):
        """ Caracteristicas del auto """
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.kilometraje = None

    def acelerar(self, tope=0):
        # Responsabilidad de que esa accion se lleve acabo
        print(f"Acelerando de 0 a {tope}")
        for i in range(1, tope + 1):
            self.velocidad += 1
            time.sleep(0.1)
            print(self.velocidad)
        print("Velocidad alcanzada")
        return self.velocidad


auto = Auto(marca="Ford", modelo="Focus")
print(auto.marca)
print(auto.modelo)
persona = Persona(auto)
persona.auto.acelerar(50)









class Imagen:
    pass


class ProcesadorImagenes:
    """La responsabilidad es aplicar cambios a una imagen y tener la imagen dentro de la instancia"""
    # Orquestador (el que dirige todo)
    def __init__(self, imagen: Imagen):
        self.imagen = imagen
        self.procesar_color = ProcesarColor()

    def cambiar_color(self, nuevo_color):
        self.imagen = self.procesar_color.procesar(self.imagen, nuevo_color)


class ReProcesadorImagenes(ProcesadorImagenes):
    """La responsabilidad es aplicar cambios a una imagen y tener la imagen dentro de la instancia"""
    def __init__(self):
        super().__init__()
        self.procesar_color = ReprocesadorColor()


class ProcesarColor:
    """La responsabilidad de saber cambiar el color de una imagen
        y aplicar eso a la imagen que le pasemos.
    """
    def procesar(self, imagen, nuevo_color):
        pass


class ReprocesadorColor:
    pass


class ProcesarTamaño:
    """"""
    pass


procesador_imagenes = ProcesadorImagenes(b"1010101010101")
procesador_imagenes.cambiar_color("rojo")


procesador_imagenes.imagen

