# ==========================================
# Code created by Leandro Marques at 02/2019
# Gesar Search Group
# State University of the Rio de Janeiro
# e-mail: marquesleandro67@gmail.com
# ==========================================

# This code is used to apply ALE scheme

import sys
import numpy as np


def rotate(_npoints, _t, _dirichlet_pts):
 # vx = r*cos(wt), where w = 2pi/T
 # vy = r*sin(wt), where w = 2pi/T

 r = 0.2 # Amplitude
 T = 16.0   # Partition
 w = 2.0*np.pi/T

 vx_Ale = np.zeros([_npoints,1], dtype = float)
 vy_Ale = np.zeros([_npoints,1], dtype = float)


 for i in range(0, _npoints): 
  vx_Ale[i] = r*np.cos(w*_t)
  vy_Ale[i] = r*np.sin(w*_t)


 # Boundary Nodes
 for i in range(0, len(_dirichlet_pts)):
  v1 = _dirichlet_pts[i][1] - 1
  v2 = _dirichlet_pts[i][2] - 1

  vx_Ale[v1] = 0.0
  vy_Ale[v1] = 0.0

  vx_Ale[v2] = 0.0
  vy_Ale[v2] = 0.0



 return vx_Ale, vy_Ale


def Quadrotate(_npoints, _nelem, _IEN, _t, _dirichlet_pts):
 # vx = r*cos(wt), where w = 2pi/T
 # vy = r*sin(wt), where w = 2pi/T

 r = 0.1 # Amplitude
 T = 16.0   # Partition
 w = 2.0*np.pi/T

 vx_Ale = np.zeros([_npoints,1], dtype = float)
 vy_Ale = np.zeros([_npoints,1], dtype = float)


 #Linear Nodes
 for e in range(0,_nelem): 
  v1 = _IEN[e][0]
  v2 = _IEN[e][1]
  v3 = _IEN[e][2]

  vx_Ale[v1] = r*np.cos(w*_t)
  vy_Ale[v1] = r*np.sin(w*_t)

  vx_Ale[v2] = r*np.cos(w*_t)
  vy_Ale[v2] = r*np.sin(w*_t)

  vx_Ale[v3] = r*np.cos(w*_t)
  vy_Ale[v3] = r*np.sin(w*_t)


 # Boundary Nodes
 for i in range(0, len(_dirichlet_pts)):
  v1 = _dirichlet_pts[i][1] - 1
  v2 = _dirichlet_pts[i][2] - 1
  v3 = _dirichlet_pts[i][3] - 1

  vx_Ale[v1] = 0.0
  vy_Ale[v1] = 0.0

  vx_Ale[v2] = 0.0
  vy_Ale[v2] = 0.0

  vx_Ale[v3] = 0.0
  vy_Ale[v3] = 0.0


 #Quad Nodes
 for e in range(0,_nelem): 
  v1 = _IEN[e][0]
  v2 = _IEN[e][1]
  v3 = _IEN[e][2]
  v4 = _IEN[e][3]
  v5 = _IEN[e][4]
  v6 = _IEN[e][5]

  vx_Ale[v4] = (vx_Ale[v1] + vx_Ale[v2])/2.0
  vy_Ale[v4] = (vy_Ale[v1] + vy_Ale[v2])/2.0

  vx_Ale[v5] = (vx_Ale[v2] + vx_Ale[v3])/2.0
  vy_Ale[v5] = (vy_Ale[v2] + vy_Ale[v3])/2.0

  vx_Ale[v6] = (vx_Ale[v3] + vx_Ale[v1])/2.0
  vy_Ale[v6] = (vy_Ale[v3] + vy_Ale[v1])/2.0


 return vx_Ale, vy_Ale
