import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_eis_3d(df):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    grouped = df.groupby('Cycle')
    for cycle, group in grouped:
        ax.plot(group['Re(Z)'], group['-Im(Z)'], zs=cycle, zdir='z', label=f"Cycle {cycle}")

    ax.set_xlabel('Re(Z) [Ohm]')
    ax.set_ylabel('-Im(Z) [Ohm]')
    ax.set_zlabel('Cycle')
    plt.title("3D EIS Plot Over Aging")
    plt.legend()
    plt.show()