import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

df = pd.read_csv("dados_pendulo.csv")

t = df['t'].values
x_raw = df['x'].values

# Centraliza x na posição de equilíbrio
x0 = np.mean(x_raw)
x = x_raw - x0 

def oha_func(t, A, b, omega, phi):
    return A * np.exp(-b * t) * np.cos(omega * t + phi)

# Estimativa inicial de parâmetros para ajudar o algoritmo a convergir
chute_inicial = [max(x), 0.1, 2 * np.pi, 0.0]

# Compara a função com os dados (x, t) e ajusta
parametros, _ = curve_fit(oha_func, t, x, p0=chute_inicial)

A, b, omega, phi = parametros

Q = omega / (2 * b)

print("--- PARAMETROS OBTIDOS DO OHA ---")
print(f"Amplitude (A): {A:.3f} pixels")
print(f"Coeficiente de Amortecimento (b): {b:.4f} s^-1")
print(f"Frequencia Angular (omega): {omega:.3f} rad/s")
print(f"Fase Inicial (phi): {phi:.3f} rad")
print(f"Fator de Qualidade (Q): {Q:.2f}")

# Plota o Gráfico do Pêndulo
plt.figure(figsize=(10, 6))

# Pontos experimentais
plt.plot(t, x, 'bo', markersize=3, label='Dados Experimentais (OpenCV)')

# Curva teórica ajustada
t_continuo = np.linspace(min(t), max(t), 1000)
x_teorico = oha_func(t_continuo, A, b, omega, phi)
plt.plot(t_continuo, x_teorico, 'r-', linewidth=2, label=f'Ajuste OHA: A={A:.1f}, b={b:.3f}, omega={omega:.2f}')

plt.title('Oscilação do Pêndulo Simples - x(t)', fontsize=14)
plt.xlabel('Tempo (s)', fontsize=12)
plt.ylabel('Posição x (pixels em relação ao centro)', fontsize=12)
plt.grid(True)
plt.legend(fontsize=10)
plt.show()