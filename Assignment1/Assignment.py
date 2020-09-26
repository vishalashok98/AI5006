import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

point  = np.array([2, 2, 1])
#Direction ratios of line perpendicular to plane
#Equation of plane ax+by+cz+d=0
normal = np.array([2, 1, 1])
ax = plt.axes(projection="3d")
#d 
d = point.dot(normal)
def plot_lines(x,y,z,k,l):

   ax.plot3D(x, y, z, k,label=l)

x = np.linspace(40, 5000, 1000)
y = np.linspace(-2200, 200, 1000)

xx, yy = np.meshgrid(x, y)   

z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]

#Direction Ratios of line
l1_dir = np.array([1, -1, -6])
#Coordinates of point through which line passes
point1 = np.array([3,-4,-5])
x1 = [];y1 = [];z1 = []
for i in range(0,3000):
    
    x1 +=[l1_dir[0]*i+point1[0]];y1 +=[l1_dir[1]*i+point1[1]]; z1 +=[l1_dir[2]*i+point1[2]]

ax.plot_wireframe(xx, yy, z, color='green')

plot_lines(x1,y1,z1,'Red','line1')
plt.show()

