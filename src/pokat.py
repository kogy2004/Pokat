class Pokat:
    
    def __init__(self, nombre: str, nivel: int, exp: int) -> None:
        self.nombre = nombre
        self.nivel = nivel
        self.exp = exp
        
    def subir_nivel(self) -> None:
        self.nivel += 1
        self.exp = 0
    
    def ganar_exp(self, cantidad: int) -> str:
        self.exp += cantidad
        if self.exp >= 100:
            self.subir_nivel()
            
        return f"{self.nombre} ha ganado {cantidad} puntos de experiencia. Experiencia actual: {self.exp}"
    
    def cambiar_nombre ( self, nuevo_nombre: str):
        self.nombre = nuevo_nombre
        
    @property
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Nivel: {self.nivel}, Experiencia: {self.exp}"
    
    
