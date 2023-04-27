import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definição das variáveis de entrada e saída
luz_natural = ctrl.Antecedent(np.arange(0, 101, 1), 'luz_natural')
luminosidade_desejada = ctrl.Antecedent(np.arange(0, 101, 1), 'luminosidade_desejada')
potencia_lampadas = ctrl.Consequent(np.arange(0, 101, 1), 'potencia_lampadas')

# Definição dos conjuntos fuzzy para as variáveis de entrada
luz_natural['escuro'] = fuzz.trimf(luz_natural.universe, [0, 0, 50])
luz_natural['claro'] = fuzz.trimf(luz_natural.universe, [0, 50, 100])

luminosidade_desejada['baixa'] = fuzz.trimf(luminosidade_desejada.universe, [0, 0, 50])
luminosidade_desejada['alta'] = fuzz.trimf(luminosidade_desejada.universe, [0, 50, 100])

# Definição dos conjuntos fuzzy para a variável de saída
potencia_lampadas['baixa'] = fuzz.trimf(potencia_lampadas.universe, [0, 0, 50])
potencia_lampadas['alta'] = fuzz.trimf(potencia_lampadas.universe, [0, 50, 100])

# Regras fuzzy
regra1 = ctrl.Rule(luz_natural['escuro'] & luminosidade_desejada['baixa'], potencia_lampadas['alta'])
regra2 = ctrl.Rule(luz_natural['escuro'] & luminosidade_desejada['alta'], potencia_lampadas['alta'])
regra3 = ctrl.Rule(luz_natural['claro'] & luminosidade_desejada['baixa'], potencia_lampadas['baixa'])
regra4 = ctrl.Rule(luz_natural['claro'] & luminosidade_desejada['alta'], potencia_lampadas['baixa'])

# Criação do sistema de controle fuzzy
controle_luminosidade = ctrl.ControlSystem([regra1, regra2, regra3, regra4])

# Simulação do sistema fuzzy
simulacao = ctrl.ControlSystemSimulation(controle_luminosidade)

# Definição dos valores de entrada
simulacao.input['luz_natural'] = 30
simulacao.input['luminosidade_desejada'] = 70

# Computação do resultado
simulacao.compute()

# Visualização dos resultados
print('Potência das lâmpadas: ', simulacao.output['potencia_lampadas'])
potencia_lampadas.view(sim=simulacao, pause=30)
plt.show()
