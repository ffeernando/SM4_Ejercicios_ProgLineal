# Problema de Asignación de Visitas

### Importamos librería
from ortools.linear_solver import pywraplp

### Constantes y parámetros del problema
# Grupos
grupos = ['G1', 'G2', 'G3', 'G4']

# Número máximo de visitas por cliente
k_max = 8  

# Total de visitas disponibles 
total_visitas = 2200

# Número de clientes por grupo
poblaciones = {'G1': 280, 'G2': 240, 'G3': 240, 'G4': 240}

# Rentabilidad
r_g = {
    ('G1', 1): 467, ('G1', 2): 210, ('G1', 3): 99, ('G1', 4): 47, ('G1', 5): 22, ('G1', 6): 4, ('G1', 7): -2, ('G1', 8): -2,
    ('G2', 1): 521, ('G2', 2): 241, ('G2', 3): 114, ('G2', 4): 59, ('G2', 5): 34, ('G2', 6): 13, ('G2', 7): 3, ('G2', 8): 5,
    ('G3', 1): 533, ('G3', 2): 238, ('G3', 3): 114, ('G3', 4): 59, ('G3', 5): 34, ('G3', 6): 12, ('G3', 7): 4, ('G3', 8): 3,
    ('G4', 1): 521, ('G4', 2): 238, ('G4', 3): 115, ('G4', 4): 58, ('G4', 5): 33, ('G4', 6): 14, ('G4', 7): 3, ('G4', 8): 6
}

### Creación del Solver
solver = pywraplp.Solver.CreateSolver('SCIP') # Significa Solving Constraint Integer Programs (también GLOP para simplex)
if not solver:
    print("No se pudo crear el solver.")
    exit()

### Definición de variables
x = {}
for g in grupos:
    for k in range(1, k_max + 1):
        x[g, k] = solver.IntVar(0.0, solver.infinity(), f"x_{g}_{k}")

### Función objetivo
funcion_objetivo = solver.Objective()
for g in grupos:
    for k in range(1, k_max + 1):
        funcion_objetivo.SetCoefficient(x[g, k], r_g[g, k])
funcion_objetivo.SetMaximization()

### Restricción del total de visitas
restriccion_total_visitas = solver.Constraint(total_visitas, total_visitas)
for g in grupos:
    for k in range(1, k_max + 1):
        restriccion_total_visitas.SetCoefficient(x[g, k], k)

### Restriccion de visitas minimas
for g in grupos:
    restriccion_visitas_minimas = solver.Constraint(poblaciones[g], poblaciones[g])  
    for k in range(1, k_max + 1):
        restriccion_visitas_minimas.SetCoefficient(x[g, k], 1)  

### Resolucion del problema
estatus = solver.Solve()

### Verificación del estado de la solución
# Verificar el estado de la solución
if estatus == pywraplp.Solver.OPTIMAL:
    print("Solución Óptima Encontrada:")
    print(f"Valor Óptimo: {funcion_objetivo.Value()}")

    for g in grupos:
        for k in range(1, k_max + 1):
            print(f"Visitas al grupo {g}, {k}-ésima visita: {x[g, k].solution_value()}")

else:
    print("No se encontró una solución óptima.")






