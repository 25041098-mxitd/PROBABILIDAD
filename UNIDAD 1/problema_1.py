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

def calcular_z(x, mu, sigma):
    """Calcula el valor Z para la distribución normal."""
    return (x - mu) / sigma

def normal_cdf(z):
    """Calcula el área bajo la curva (probabilidad acumulada)."""
    # Función de error para calcular la probabilidad normal
    return (1.0 + math.erf(z / math.sqrt(2.0))) / 2.0

def main():
    print("=" * 60)
    print(" PROBLEMA 1: Distribución Normal de Pesos (ITD)")
    print("=" * 60)
    
    # Datos del problema
    mu = 70      # Media poblacional
    sigma = 4    # Desviación estándar
    N = 500      # Población total de estudiantes
    
    # Límites de peso a evaluar
    x1 = 68
    x2 = 72
    
    # 1. Transformación a valores Z
    z1 = calcular_z(x1, mu, sigma)
    z2 = calcular_z(x2, mu, sigma)
    
    # 2. Búsqueda de probabilidad acumulada
    prob_z1 = normal_cdf(z1)
    prob_z2 = normal_cdf(z2)
    
    # 3. Resta de límites para el área central
    prob_total = prob_z2 - prob_z1
    
    # 4. Cálculo de cantidad de estudiantes (redondeado)
    estudiantes = round(prob_total * N)
    
    print("\n[ DATOS INICIALES ]")
    print(f"- Media (μ) = {mu} kg")
    print(f"- Desviación estándar (σ) = {sigma} kg")
    
    print("\n[ DESARROLLO Y CÁLCULOS ]")
    print(f"- Límite inferior ({x1} kg) -> Z1 = {z1:.2f}")
    print(f"- Límite superior ({x2} kg) -> Z2 = {z2:.2f}")
    
    print("\n[ CONCLUSIÓN ]")
    print(f"La probabilidad de que un estudiante pese entre 68 y 72 kg es:")
    print(f"P(-0.50 < Z < 0.50) = {prob_total:.4f} (Es decir, el {prob_total*100:.2f}%)")
    
    print(f"\nMultiplicando por la población total ({N} estudiantes):")
    print(f"{N} x {prob_total:.4f} = {prob_total * N:.1f}")
    print(f"Se estima que aproximadamente {estudiantes} estudiantes pesan dentro de este rango.")

if __name__ == "__main__":
    main()
