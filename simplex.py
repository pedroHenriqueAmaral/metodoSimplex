# Resolver Método Simplex

import pulp as p
import pandas as pd
from collections import OrderedDict
from tabulate import tabulate

# Valores Diretos
problem = p.LpProblem('Exemplo', p.LpMaximize) # Problema de Maximizar
problem2 = p.LpProblem('Exemplo', p.LpMinimize) # Problema de Minimizar

# Variaveis de Descisão
x1 = p.LpVariable("x1", lowBound = 0)
x2 = p.LpVariable("x2", lowBound = 0)
# x3[...]

# Função Objetivo
# prob += [Função]
problem += 15*x1 + 10*x2

# Restrições
problem += x1 >= 0 # Não negatividade
problem += x2 >= 0 # Não negatividade

# Exemplos de Restrições
# prob += x1 <= 40
# prob += 4*x1 + 12*x2 <= 36
# prob += 15*x1 + 30*x2 <= 90

status = problem.solve()
print(p.LpStatus[status])
print(p.value(problem.objective))

# Dicionário com as variáveis de decisão para exibir o valor otimizado de cada
data = OrderedDict( {
    "x1" : [p.value(x1)],
    "x2" : [p.value(x2)]
})

dataframe = pd.DataFrame(data)
print(tabulate(dataframe, headers="keys", tablefmt="psql")) # Exibe os dados em formato de tabela