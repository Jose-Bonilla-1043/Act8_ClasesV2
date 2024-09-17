print("Clases versión 2 el constructor")

class Perro:
    # Función constructor
    def __init__(self, color, edad):
        self.color = color
        self.edad = edad
    
    # Funciones creadas por el usuario
    def morder(self):
        print("Chale, el perro me mordió")
    
    def chatperro(self, mensaje):
        print(f"Chat perro: {mensaje}")
    
    def chatperra(self, mensajepe):
        print(f"Chat perra: {mensajepe}")
    
    def datos(self):
        print(f"Color: {self.color}, Edad: {self.edad}")

# Crear objetos
chihuas = Perro("Negro", 2)

# Llamadas de funciones
chihuas.datos()
chihuas.morder()
chihuas.chatperro("Hola canina")
chihuas.chatperra("Hola body")
chihuas.chatperro("¿Quieres ser mi guggu?")
chihuas.chatperra("grrru.......")
