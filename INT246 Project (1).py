#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install Scikit-fuzzy')


# In[4]:


import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


# In[94]:


velocity_traffic=ctrl.Antecedent(np.arange(-40,50,10),'velocity_traffic')
velocity_traffic['battery_off']=fuzzy.trimf(velocity_traffic.universe,[0,20,40])
velocity_traffic['battery_on']=fuzzy.trimf(velocity_traffic.universe,[-40,-20,0])
velocity_traffic.view()
plt.show()


# In[39]:


battery_capacity=ctrl.Antecedent(np.arange(1,101,1),'battery_capacity')
battery_capacity['battery_off']=fuzzy.trimf(battery_capacity.universe,[0,1,20])
battery_capacity['battery_on']=fuzzy.trimf(battery_capacity.universe,[20,60,100])
battery_capacity.view()
plt.show()


# In[40]:


torque_demand=ctrl.Antecedent(np.arange(1,101,1),'torque_demand')
torque_demand['battery_off']=fuzzy.trimf(torque_demand.universe,[0,1,25])
torque_demand['battery_on']=fuzzy.trimf(torque_demand.universe,[25,65,100])
torque_demand.view()
plt.show()


# In[99]:


battery_active=ctrl.Consequent(np.arange(0,1.1,0.1),'battery_active')
battery_active['not active-mode'] = fuzzy.trimf(battery_active.universe,[0,0.4,0.8])
battery_active['active-mode'] = fuzzy.trimf(battery_active.universe,[0.8,0.9,1.0])
battery_active.view()
plt.show()


# In[100]:


rule1=ctrl.Rule(velocity_traffic['battery_off'] & battery_capacity['battery_off'] & torque_demand['battery_off'], battery_active['not active-mode'])
rule2=ctrl.Rule(velocity_traffic['battery_off'] & battery_capacity['battery_on'] & torque_demand['battery_on'], battery_active['not active-mode'])
rule3=ctrl.Rule(velocity_traffic['battery_off'] & battery_capacity['battery_on'] & torque_demand['battery_off'], battery_active['not active-mode'])
rule4=ctrl.Rule(velocity_traffic['battery_off'] & battery_capacity['battery_off'] & torque_demand['battery_on'], battery_active['not active-mode'])
rule5=ctrl.Rule(velocity_traffic['battery_on'] & battery_capacity['battery_on'] & torque_demand['battery_on'], battery_active['active-mode'])
rule6=ctrl.Rule(velocity_traffic['battery_on'] & battery_capacity['battery_off'] & torque_demand['battery_off'], battery_active['not active-mode'])
rule7=ctrl.Rule(velocity_traffic['battery_on'] & battery_capacity['battery_on'] & torque_demand['battery_off'], battery_active['not active-mode'])
rule8=ctrl.Rule(velocity_traffic['battery_on'] & battery_capacity['battery_off'] & torque_demand['battery_on'], battery_active['not active-mode'])
rule9=ctrl.Rule(velocity_traffic['battery_on'] & battery_capacity['battery_on'] & torque_demand['battery_off'], battery_active['not active-mode'])
rule_over_head=[rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9]


# In[101]:


x=ctrl.ControlSystem(rule_over_head)
y=ctrl.ControlSystemSimulation(x)


# In[102]:


y.input['velocity_traffic'] = 20
y.input['battery_capacity'] = 40
y.input['torque_demand'] = 40
y.compute()
print(y.output['battery_active'])


# In[103]:


battery_active.view(sim=y)
plt.show()


# In[104]:


y.input['velocity_traffic'] = -20
y.input['battery_capacity'] = 40
y.input['torque_demand'] = 40
y.compute()
print(y.output['battery_active'])


# In[105]:


battery_active.view(sim=y)
plt.show()


# In[ ]:




