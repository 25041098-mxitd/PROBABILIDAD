"""
INSTITUTO TECNOLÓGICO DE DURANGO
Departamento de Sistemas y Computación
Probabilidad y Estadística

Datos del Alumno:
- Autor: Vargas Calderón Yahir Fernando
- Número de Control: 25041098
- Carrera: Ingeniería en Sistemas Computacionales
"""

import math

def probabilidad_poisson(lmbda, x):
    """Calcula la probabilidad usando la fórmula de Poisson."""
    return (math.exp(-lmbda) * (lmbda ** x)) / math.factorial(x)

def main():
    print("=" * 60)
    print(" PROBLEMA 2: Unidad de Cuidados Intensivos (Hospital)")
    print("=" * 60)
    
    
    print("\n[JUSTIFICACIÓN]")
    print("La solución es de tipo POISSON.")
    print("¿Por qué? Primero, porque el enunciado lo establece explícitamente[cite: 409].")
    print("Segundo, porque modela el número de eventos independientes (pacientes ingresados) ")
    print("que ocurren en un intervalo de tiempo continuo (un día), conociendo una tasa ")
    print("promedio de ocurrencia (\u03bb = 5 personas por día).")
    
    lmbda = 5
    
    prob_2 = probabilidad_poisson(lmbda, 2)
    print("\na). ¿Cuál es la probabilidad de que el número de personas sea 2?")
    print(f"    P(X = 2) = {prob_2:.6f} (Aprox. {prob_2 * 100:.2f}%)")
    
    prob_acumulada = 0
    for i in range(11):  
        prob_acumulada += probabilidad_poisson(lmbda, i)
        
    prob_mayor_10 = 1 - prob_acumulada
    print("\nb). ¿Es probable que x exceda de 10? Explicar")
    print(f"    P(X > 10) = {prob_mayor_10:.6f} (Aprox. {prob_mayor_10 * 100:.2f}%)")
    print("\n    Explicación: NO es probable. La probabilidad de que ingresen más de 10")
    print("    personas es apenas del 1.37%. Dado que el promedio es 5, exceder 10 es un")
    print("    evento sumamente raro.")
    
if __name__ == "__main__":
    main()
