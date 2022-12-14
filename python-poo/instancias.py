# Definicion

class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}'
    
# Uso

manuel = Persona('Manuel', 43)
maria = Persona('Maria', 20)

# print(manuel.saludar(maria))

# Instancias

class Coordenada:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2
        
        return (x_diff + y_diff)**0.5
    
if __name__ == '__main__':
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)
    
    print(coord_1.distancia(coord_2))
    print(isinstance(coord_1, Coordenada))