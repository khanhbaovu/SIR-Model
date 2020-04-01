import numpy as np
import matplotlib.pyplot as plt

def fwdEuler(s_func, i_func, r_func, s0, i0, r0, delta_t, tN):
    N_t = int(round(tN/delta_t))
    S = np.zeros(N_t + 1)
    I = np.zeros(N_t + 1)
    R = np.zeros(N_t + 1)
    t = np.linspace(0, N_t*delta_t, len(S))
    S[0] = s0
    I[0] = i0
    R[0] = r0
    for i in range(N_t):
        S[i+1] = S[i] + delta_t*s_func(S[i], I[i])
        I[i+1] = I[i] + delta_t*i_func(S[i], I[i])
        R[i+1] = R[i] + delta_t*r_func(I[i])
        

    return S, I, R, t


def s_func(S, I):
    b = 1/2
    return -b*S*I

def r_func(I):
    k = 1/3
    return k*I

def i_func(S, I):
    b = 1/2
    k = 1/3
    return b*S*I - k*I


s0 = 1
i0 = (1.27)*(10**(-6))
r0 = 0

delta_t = 10
tN = 150

S, I, R, t = fwdEuler(s_func, i_func, r_func, s0, i0, r0, delta_t, tN )

plt.plot(S, t, R, t, I, t)
plt.legend(['Susceptible', 'Recovered', 'Infected'])
plt.show()

