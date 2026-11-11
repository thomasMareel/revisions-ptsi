import numpy as np
import matplotlib.pyplot as plt

R = 8.314                          # J/K/mol
n0, DrH = 1.0, -120e3              # mol ; J/mol (réaction exothermique)
C = 3.0e3                          # capacité thermique totale du contenu (J/K)
Ea, k0, T0 = 80e3, 2.0e-4, 298.15  # Arrhenius, avec k(T0) = k0 en s^-1

def k(T):
    return k0 * np.exp(-Ea / R * (1 / T - 1 / T0))

dt, tf = 1.0, 3600.0               # pas et durée de simulation (s)
t = np.arange(0, tf + dt, dt)
xi = np.zeros_like(t)              # avancement (mol)
T = np.full_like(t, T0)            # température (K)

for n in range(len(t) - 1):        # méthode d'Euler explicite
    v = k(T[n]) * (n0 - xi[n])     # vitesse de réaction dxi/dt, ordre 1
    xi[n+1] = xi[n] + v * dt
    T[n+1] = T[n] - DrH / C * v * dt   # bilan : C dT + DrH dxi = 0

plt.plot(t / 60, T - 273.15)
plt.xlabel("t (min)"); plt.ylabel("T (degC)"); plt.grid(); plt.show()
