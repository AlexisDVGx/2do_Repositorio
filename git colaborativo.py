class GestorCalificaciones:
    def __init__(self):
        self.estudiantes = {}

    def agregar_estudiante(self, nombre, calificaciones):
        self.estudiantes[nombre] = calificaciones

    def calcular_promedio(self, nombre):
        if nombre not in self.estudiantes:
            return 0.0 
        
        notas = self.estudiantes[nombre]
        
        # BUG 2 Resuelto: Corrección de indentación y división por cero
        if len(notas) == 0:
            return 0.0  # O el valor por defecto que acuerdes con tu equipo
        
        # BUG 1 Corregido: Ya no iteramos innecesariamente
        suma = sum(notas)
        promedio = suma / len(notas)
        
        return promedio

    def obtener_mejor_estudiante(self):
        mejor_promedio = 0.0
        mejor_estudiante = ""
        
        # BUG 3: solucionado
        for estudiante, notas in self.estudiantes.items():
            promedio = self.calcular_promedio(estudiante)
            if promedio > mejor_promedio:
                mejor_promedio = promedio
                mejor_estudiante = estudiante
                
        # BUG 4 Corregido: Formateo de strings (f-strings)
        return f"El mejor estudiante es {mejor_estudiante} con un promedio de {mejor_promedio}"

# --- Zona de pruebas ---
if __name__ == "__main__":
    gestor = GestorCalificaciones()
    
    # Datos de prueba
    gestor.agregar_estudiante("Ana", [85, 90, 78])
    gestor.agregar_estudiante("Carlos", []) # Ahora es manejado correctamente
    gestor.agregar_estudiante("Luis", [92, 88, 95])

    print("Calculando el mejor estudiante...")
    resultado = gestor.obtener_mejor_estudiante()
    print(resultado)