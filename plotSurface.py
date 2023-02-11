# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 11:10:24 2023

@author: jesus
"""

import numpy as np
import matplotlib.pyplot as mpl
from scipy.spatial import Delaunay
import scipy.special as ei

ax = mpl.axes(projection ='3d')
#ax.set_aspect('equal')

n=10
[u0,v0]=np.linspace(-1*np.ones(2),1*np.ones(2),n,endpoint=True).T
[u,v]=np.meshgrid(u0,v0)

inputData=np.array([u.flatten(),v.flatten()]).T
tri = Delaunay(inputData)
tris=tri.simplices

x=1*u
y=1*v
z=0*u

bound=np.max(np.abs([x,y,z]))
ax.set_xlim3d([-bound,bound])
ax.set_ylim3d([-bound,bound])
ax.set_zlim3d([-bound,bound])

[x,y,z]=[x.flatten(),y.flatten(),z.flatten()]
ax.plot_trisurf(x,y,z,triangles=tri.simplices)

E=1.0
F=0.0
G=1.0
l=1
m=1
n=1
H=(l*G-2*m*F+n*E)/(2*(E*G-F**2))
K=(l*n-m*2)/(E*G-F**2)

x=E*u+F*v
y=G*v+F*u
#z=E*u**2+2*F*u*v+G*v**2
# z=E*l*x**2/2+F*m*x*y+G*n*y**2/2
z=l*x**2/2+m*x*y+n*y**2/2

[x,y,z]=[x.flatten(),y.flatten(),z.flatten()]
ax.plot_trisurf(x,y,z,triangles=tri.simplices)
ax.set_title(f"K = {round(K,3)}; H = {round(H,3)}")