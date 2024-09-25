import numpy as np
import matplotlib.pyplot as plt

vector = np.random.rand(720)
matriz = vector.reshape(120, 6)

matriz_T_F = matriz.T
matriz_T_C = matriz.T

plt.figure(figsize=(10, 8))

ax1 = plt.axes([0.05, 0.65, 0.4, 0.3])
ax1.plot(matriz_T_F[0], label='Línea')
ax1.set_title("Plot")
ax1.set_xlabel("Eje X")
ax1.set_ylabel("Eje Y")
ax1.grid(True)
ax1.legend()

ax2 = plt.axes([0.55, 0.65, 0.4, 0.3])
ax2.scatter(np.arange(len(matriz_T_F[1])), matriz_T_F[1], color='r', label='Scatter')
ax2.set_title("Scatter")
ax2.set_xlabel("Eje X")
ax2.set_ylabel("Eje Y")
ax2.grid(True)
ax2.legend()

ax3 = plt.axes([0.05, 0.35, 0.4, 0.3])
ax3.bar(np.arange(len(matriz_T_F[2])), matriz_T_F[2], color='g', label='Barras')
ax3.set_title("Bar")
ax3.set_xlabel("Eje X")
ax3.set_ylabel("Eje Y")
ax3.grid(True)
ax3.legend()

ax4 = plt.axes([0.55, 0.35, 0.4, 0.3])
ax4.hist(matriz_T_F[3], bins=10, color='m', label='Histograma', alpha=0.7)
ax4.set_title("Histograma")
ax4.set_xlabel("Eje X")
ax4.set_ylabel("Eje Y")
ax4.grid(True)
ax4.legend()

ax5 = plt.axes([0.05, 0.05, 0.4, 0.2])
ax5.pie(matriz_T_F[4][:6] / np.sum(matriz_T_F[4][:6]), labels=['A', 'B', 'C', 'D', 'E', 'F'], autopct='%1.1f%%')
ax5.set_title("Pie")
ax5.axis('equal')

ax6 = plt.axes([0.55, 0.05, 0.4, 0.2])
ax6.fill_between(np.arange(len(matriz_T_F[5])), matriz_T_F[5], color='c', alpha=0.5, label='Área')
ax6.set_title("Área")
ax6.set_xlabel("Eje X")
ax6.set_ylabel("Eje Y")
ax6.grid(True)
ax6.legend()

plt.tight_layout()
plt.show()