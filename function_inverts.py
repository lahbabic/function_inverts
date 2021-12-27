import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

W = '\033[0m'   # white 
G = '\033[32m'  # green

def f(x, y):
	return y*np.exp(x)

print("Creating dimensions ... ", end="")
x = np.linspace(1, 26, 30)
y = np.linspace(1, 26, 30)
x0 = np.linspace(1, 26, 30)
z0 = np.linspace(1, 26, 30)
z1 = np.linspace(1, 26, 30)
y1 = np.linspace(1, 26, 30)

X, Y = np.meshgrid(x, y)
X0, Z0 = np.meshgrid(x0, z0)
Y1, Z1 = np.meshgrid(y1, z1)
print("["+G+"Done"+W+"]", end="\n")
print("Running functions ... ", end="")
Z = f(X, Y)
Y0 = Z0/np.exp(-X0)
x1= -np.log(z1)+22.5
print("["+G+"Done"+W+"]", end="\n")
print("Generating graph ... ", end="")
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 1000, cmap="Blues")
ax.contour3D(X0, Z0, Y0, 10, cmap="autumn")
ax.plot3D(x1, y1, z1, "red")

#ax.contour3D(X1, Y1, Z1, 50)
ax.set_title("function z=y*exp(x) and it\'s inverts y = z/exp(x) and x = ln(z)")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(45, 120)
print("["+G+"Done"+W+"]", end="\n")
print("Saving graph to graph.png ... ", end="")
plt.savefig("graph.png")
print("["+G+"Done"+W+"]", end="\n")
# red dashes, blue squares and green triangles
#plt.plot(t, u*np.exp(t), 'r--', t, t**2, 'bs', t, t**3, 'g^')
