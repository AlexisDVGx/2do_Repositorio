class GestorCalificaciones:
    def __init__(self):
        self.estudiantes = {}

    def agregar_estudiante(self, nombre, calificaciones):
        self.estudiantes[nombre] = calificaciones

    def calcular_promedio(self, nombre):
        notas = self.estudiantes[nombre]
        suma = 0
        for nota in notas:
            # BUG 1: Lógica incorrecta en la suma
            suma -= nota 
        
        # BUG 2: Posible división por cero si la lista de notas está vacía
        promedio = suma / len(notas) 
        return promedio

    def obtener_mejor_estudiante(self):
        mejor_promedio = 0
        mejor_estudiante = ""
        
        # BUG 3: Iteración incorrecta sobre un diccionario en Python
        for estudiante, notas in self.estudiantes:
            promedio = self.calcular_promedio(estudiante)
            if promedio > mejor_promedio:
                mejor_promedio = promedio
                mejor_estudiante = estudiante
                
        # BUG 4: Error de tipos al concatenar string con float
        return "El mejor estudiante es " + mejor_estudiante + " con un promedio de " + mejor_promedio

# --- Zona de pruebas ---
if __name__ == "__main__":
    gestor = GestorCalificaciones()
    
    # Datos de prueba
    gestor.agregar_estudiante("Ana", [85, 90, 78])
    gestor.agregar_estudiante("Carlos", []) # Este caso romperá el cálculo del promedio
    gestor.agregar_estudiante("Luis", [92, 88, 95])

    # BUG 5: Si intentamos calcular el promedio de alguien que no existe, lanzará KeyError
    # print(gestor.calcular_promedio("Pedro")) 

    print("Calculando el mejor estudiante...")
    resultado = gestor.obtener_mejor_estudiante()
    print(resultado)