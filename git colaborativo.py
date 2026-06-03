class GestorCalificaciones:
    def __init__(self):
        self.estudiantes = {}

    def agregar_estudiante(self, nombre, calificaciones):
        self.estudiantes[nombre] = calificaciones

    def calcular_promedio(self, nombre):
        if nombre not in self.estudiantes:
            return 0.0 
        notas = self.estudiantes[nombre]
        suma = 0
        for nota in notas:
            # BUG 1: Solucionado
            suma = sum(notas)
        
        
        # BUG 2 Resuelto: Validación para evitar división por cero
    if len(notas) == 0:
        return 0  # O el valor por defecto que tu equipo decida retornar si no hay notas
    
    promedio = suma / len(notas)
    return promedio

    def obtener_mejor_estudiante(self):
        mejor_promedio = 0
        mejor_estudiante = ""
        
        # BUG 3: solucionado
        for estudiante, notas in self.estudiantes.items():
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