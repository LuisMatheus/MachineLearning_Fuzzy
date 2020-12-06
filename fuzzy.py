import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl

temp = ctrl.Antecedent(np.arange(0, 50, 1), 'Temperatura')
hum_rel = ctrl.Antecedent(np.arange(0, 100, 1), 'Humidade Relativa')
temp_var = ctrl.Consequent(np.arange(-15, 15, 1), 'Variacao da temperatura')

temp['frio'] = fuzzy.trapmf(temp.universe, [0, 0, 1, 12])
temp['normal'] = fuzzy.trapmf(temp.universe, [10 , 18, 25, 30])
temp['quente'] = fuzzy.trapmf(temp.universe, [27, 30, 50, 50])

hum_rel['baixa'] = fuzzy.trapmf(hum_rel.universe, [0, 0, 35, 50])
hum_rel['normal'] = fuzzy.trapmf(hum_rel.universe, [45, 70, 100, 100])

temp_var['ruim'] = fuzzy.trapmf(temp_var.universe, [-15,-15,-13,-2])
temp_var['normal'] = fuzzy.trimf(temp_var.universe, [-5,0,5])
temp_var['alta'] = fuzzy.trapmf(temp_var.universe, [2,15,15,15])

#temp.view()
#hum_rel.view()
#temp_var.view()

rule1 = ctrl.Rule(temp['frio'] & hum_rel['normal'], temp_var['normal'])
rule2 = ctrl.Rule(temp['normal'] & hum_rel['normal'], temp_var['normal'])
rule3 = ctrl.Rule(temp['quente'] & hum_rel['normal'], temp_var['normal'])

rule4 = ctrl.Rule(temp['frio'] & hum_rel['baixa'], temp_var['ruim'])
rule5 = ctrl.Rule(temp['normal'] & hum_rel['baixa'], temp_var['normal'])
rule6 = ctrl.Rule(temp['quente'] & hum_rel['baixa'], temp_var['alta'])


temp_var_ctrl = ctrl.ControlSystem([
    rule1,
    rule2,
    rule3,
    rule4,
    rule5,
    rule6
    ])

res = ctrl.ControlSystemSimulation(temp_var_ctrl)
res.input['Temperatura'] = 35
res.input['Humidade Relativa'] = 60
res.compute()
print(res.output['Variacao da temperatura'])
temp_var.view(sim=res)