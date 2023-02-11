# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 19:44:57 2023

@author: jesus
"""
import numpy as np
import matplotlib.pyplot as mpl
from scipy.spatial import Delaunay
import scipy.special as ei

ax = mpl.axes(projection ='3d')
ax.set_aspect('auto')

n=20
[u0,v0]=np.linspace(-1*np.ones(2),1*np.ones(2),n,endpoint=True).T
[u,v]=np.meshgrid(1*u0,v0)

# Params
[c,a]=[1.00,-.20]
p1=2/(a+c)
p2=np.sqrt((c**2-a**2)/c**2)
p3=(c**2-a**2)/2
p4=(c**2+a**2)/2
o=0
t=np.pi/p1
u=(u+o)*t

z=a*ei.ellipeinc(p1*u-np.pi/4,p2)+c*ei.ellipeinc(p1*u-np.pi/4,p2)
x=np.sqrt(p3*np.sin(p1*u)+p4)*np.cos(np.pi*v)
y=np.sqrt(p3*np.sin(p1*u)+p4)*np.sin(np.pi*v)
# x=u**3+v**3
# y=u+v
# z=u**2+v**2

[x,y,z]=[x.flatten(),y.flatten(),z.flatten()]
[u,v]=[u.flatten(),v.flatten()]
inputData=np.array([u,v]).T
tri = Delaunay(inputData)
tris=tri.simplices
    
ax.plot_trisurf(x,y,z,triangles=tri.simplices)