import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

temp = np.arange(0, 51, 1)
hum_rel = np.arange(0, 101, 1)
temp_var  = np.arange(-15, 16, 1)

# Generate fuzzy membership functions
temp_frio = fuzz.trapmf(temp, [0, 0, 1, 12])
temp_normal = fuzz.trapmf(temp, [10 , 18, 25, 30])
temp_quente = fuzz.trapmf(temp, [27, 30, 50, 50])

hum_rel_baixa = fuzz.trapmf(hum_rel, [0, 0, 35, 50])
hum_rel_normal = fuzz.trapmf(hum_rel, [45, 70, 100, 100])

temp_var_ruim = fuzz.trapmf(temp_var, [-15,-15,-13,-2])
temp_var_normal = fuzz.trimf(temp_var, [-5,0,5])
temp_var_alta = fuzz.trapmf(temp_var, [2,15,15,15])

# Visualize these universes and membership functions
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(temp, temp_frio, 'b', linewidth=1.5, label='Frio')
ax0.plot(temp, temp_normal, 'g', linewidth=1.5, label='Normal')
ax0.plot(temp, temp_quente, 'r', linewidth=1.5, label='Quente')
ax0.set_title('Temperatura')
ax0.legend()

ax1.plot(hum_rel, hum_rel_baixa, 'b', linewidth=1.5, label='Baixa')
ax1.plot(hum_rel, hum_rel_normal, 'g', linewidth=1.5, label='Normal')
ax1.set_title('Humidade relativa do ar')
ax1.legend()

ax2.plot(temp_var, temp_var_ruim, 'b', linewidth=1.5, label='Ruim')
ax2.plot(temp_var, temp_var_normal, 'g', linewidth=1.5, label='Normal')
ax2.plot(temp_var, temp_var_alta, 'r', linewidth=1.5, label='alta')
ax2.set_title('Variacao da temperatura')
ax2.legend()

# Turn off top/right axes
for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

