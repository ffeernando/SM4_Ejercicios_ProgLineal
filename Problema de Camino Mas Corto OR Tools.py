# Problema de Camino Más Corto con  ORTOOLS

# Encontrar el camino más corto entre los nodos $s$ y $t$ del grafo de la presentación.

# Importamos librería
from ortools.graph.python import min_cost_flow

# Constantes y parámetros del problema
grafo = [
    (0, 1, 1, 4),
    (0, 2, 1, 3),
    (1, 2, 1, 3),
    (1, 3, 1, 2),
    (2, 1, 1, 6),
    (2, 3, 1, 1),
    (3, 5, 1, 0.5),
    (3, 7, 1, 10),
    (5, 1, 1, 1.5),
    (5, 7, 1, 8),
    (7, 6, 1, 4),
    (6, 9, 1, 9),
    (6, 8, 1, 1),
    (8, 5, 1, 0.1),
    (8, 9, 1, 2)
]

# Creación del Solver
smcf = min_cost_flow.SimpleMinCostFlow()

# Agregamos aristas e insumos al modelo
nodos_inicio = [i[0] for i in grafo]
nodos_finales = [i[1] for i in grafo]
capacidades = [i[2] for i in grafo]
costos = [i[3] for i in grafo]

smcf.add_arcs_with_capacity_and_unit_cost(nodos_inicio, nodos_finales, capacidades, costos)

# Suministros
suministros = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: -1}
for nodo, sumnistro in suministros.items():
    smcf.set_node_supply(nodo, sumnistro)

# Solver
estatus = smcf.solve()

# Verificación del estado de la solución
if estatus == smcf.OPTIMAL:
    print("Costo minimo total:", smcf.optimal_cost())
    print("Camino más corto:")
    for i in range(smcf.num_arcs()):
        if smcf.flow(i) > 0:
            print(f"{smcf.tail(i)} -> {smcf.head(i)} (costo: {smcf.unit_cost(i)})")
else:
    print("No se encontró solución óptima")



