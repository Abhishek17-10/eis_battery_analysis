import numpy as np
import matplotlib.pyplot as plt

def calculate_dQdV(voltage, capacity):
    dV = np.diff(voltage)
    dQ = np.diff(capacity)
    dQdV = dQ / dV
    return voltage[:-1], dQdV

def plot_dQdV(V, dQdV):
    plt.plot(V, dQdV)
    plt.xlabel('Voltage (V)')
    plt.ylabel('dQ/dV (Ah/V)')
    plt.title('Incremental Capacity Analysis')
    plt.grid(True)
    plt.show()