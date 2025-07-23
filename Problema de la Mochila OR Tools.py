# Problema de Mochila

Supongamos que tienes $40,000 MXN para invertir y un conjunto de posibles inversiones. Cada inversión requiere cierto capital y proporciona un retorno estimado. El objetivo es maximizar el retorno total sin exceder el capital disponible, y puedes elegir o no cada inversión (no fracciones).

| Inversión | Costo (mxn) | Retorno estimado (mxn) |
|-----------|-------------|------------------------|
| 1         | 10,000      | 8,000                  |
| 2         | 20,000      | 15,000                 |
| 3         | 30,000      | 25,000                 |
| 4         | 25,000      | 16,000                 |
| 5         | 15,000      | 12,000                 |


En este caso, los retornos juegan el papel de los $c_{i}$ y los costos el papel de los $a_{i}$. El valor de b es 100,000.00 y la variable $x_{i}$ indica si se realiza la inversión número $i$, es decir toma el valor 1 si se realiza la inversión y 0 si no.

Resolver 
$$
\max \sum_{i=1}^{n} c_i x_i \quad \text{sujeto a} \quad \sum_{i=1}^{n} a_i x_i \leq 40000, \quad x_i \in \{0, 1\}
$$

# Importamos librería
from ortools.linear_solver import pywraplp

### Constantes y parámetros del problema
costos = [10000, 20000, 30000, 25000, 15000]
retornos = [8000, 15000, 25000, 16000, 12000]
n = len(costos)
presupuesto = 40000

### Creación del Solver
solver = pywraplp.Solver.CreateSolver('CBC') # Coin-or Branch and Cut
if not solver:
    print("No se pudo crear el solver")
    exit()

### Definición de variables
x = [solver.IntVar(0, 1, f"x{i}") for i in range(n)]

### Función objetivo
solver.Maximize(solver.Sum(retornos[i]*x[i] for i in range(n)))

### Restricción de presupuesto
solver.Add(solver.Sum(costos[i]*x[i] for i in range(n))<=presupuesto)

### Resolucion del problema
estatus = solver.Solve()

### Verificación del estado de la solución
print("Resultado del portafolio óptimo")
if estatus == pywraplp.Solver.OPTIMAL:
    for i in range(n):
        estado = "Invertir" if x[i].solution_value() == 1 else "No invertir"
        print(f"Inversión {i+1}: {estado}")
    print(f"Retorno total esperado: ${solver.Objective().Value():,.2f}")
    print(f"Capital usado: ${sum(costos[i] * x[i].solution_value() for i in range(n)):,.2f}")
else:
    print("No se encontró solución óptima")



