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

def probabilidad_binomial(n, x, p):
    """Calcula la probabilidad usando la fórmula Binomial."""
    return math.comb(n, x) * (p ** x) * ((1 - p) ** (n - x))

def main():
    print("=" * 60)
    print(" PROBLEMA 3: Motores de Podadoras para Pasto")
    print("=" * 60)
    
    print("\n[JUSTIFICACIÓN]")
    print("La solución es de tipo BINOMIAL.")
    print("¿Por qué? Porque tenemos un número fijo y determinado de ensayos independientes")
    print("en un lote (n = 1,000 motores). En cada ensayo solo hay dos resultados posibles:")
    print("el motor es defectuoso o no lo es. Además, la probabilidad de éxito (defecto)")
    print("se mantiene constante para cada motor analizado (p = 0.001)[cite: 410].")
    print("*(Nota: Por ser n grande y p pequeña, también podría aproximarse por Poisson, ")
    print("pero conceptualmente cumple las 4 propiedades del experimento Binomial).*")
    
    n = 1000
    p = 0.001
    
    prob_0 = probabilidad_binomial(n, 0, p)
    prob_3 = probabilidad_binomial(n, 3, p)
    prob_4 = probabilidad_binomial(n, 4, p)
    
    print("\nCálculos para un embarque de 1,000 motores:")
    
    print("\n1. ¿Cuál es la probabilidad de que ninguno sea defectuoso?")
    print(f"   P(X = 0) = {prob_0:.6f} (Aprox. {prob_0 * 100:.2f}%)")
    
    print("\n2. ¿Cuál es la probabilidad de que tres sean defectuosos?")
    print(f"   P(X = 3) = {prob_3:.6f} (Aprox. {prob_3 * 100:.2f}%)")
    
    print("\n3. ¿Cuál es la probabilidad de que cuatro sean defectuosos?")
    print(f"   P(X = 4) = {prob_4:.6f} (Aprox. {prob_4 * 100:.2f}%)")

if __name__ == "__main__":
    main()
