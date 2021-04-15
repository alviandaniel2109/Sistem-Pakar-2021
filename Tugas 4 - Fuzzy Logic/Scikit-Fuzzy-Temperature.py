# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 22:47:01 2021

@author: hp
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


temprature = ctrl.Antecedent(np.arange(0, 15, 1), 'temperature')
moisture = ctrl.Antecedent(np.arange(0, 11, 1), 'moisture')
humidity = ctrl.Antecedent(np.arange(0, 11, 1), 'humidity')
minutes = ctrl.Consequent(np.arange(0,26, 1), 'minutes')

temprature.automf(3)
moisture.automf(3)
humidity.automf(3)

minutes['low'] = fuzz.trimf(minutes.universe, [0, 0, 13])
minutes['medium'] = fuzz.trimf(minutes.universe, [0, 13, 25])
minutes['high'] = fuzz.trimf(minutes.universe, [13, 25, 25])

temprature.view()
moisture.view()
humidity.view()

rule1 = ctrl.Rule(temprature['poor'] | moisture['poor'] | humidity['poor'], minutes['low'])
rule2 = ctrl.Rule(temprature['average'] | moisture['average'] | humidity['average'], minutes['medium'])
rule3 = ctrl.Rule(temprature['good'] | moisture['good'] | humidity['good'], minutes['high'])

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['temperature'] = 1
tipping.input['moisture'] = 1
tipping.input['humidity'] = 1

tipping.compute()

print ('Waktu ', tipping.output['minutes'])
minutes.view(sim=tipping)