# 'contour_w.py'
# 
# Plots contour of vertical velocity at desired height:

# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('/Users/lauramazzaro/Documents/Work/Perts/Article/Figures/new_cmaps.py')

# Modify plotting parameters!
execfile('/Users/lauramazzaro/Documents/Work/Perts/Article/Figures/new_params.py')

from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# ---------- Input ----------

crange = [-4,-2,0,2,4]

z_plot = 500

# ---------------------------

with np.load('d02_0001-01-01_10:00:00.npz') as dh:
     u = dh['w']
     z = np.squeeze(dh['z'])
     dx = dh['dx'][0][0]

z_ind = [i for i in np.arange(len(z)) if z[i] >= z_plot][0]


X = np.arange(u.shape[2])*dx/1000
Y = np.arange(u.shape[1])*dx/1000

fh = plt.figure(figsize=(12,6))
ax = fh.add_subplot(111)

plt.axes().set_aspect('equal')

plot = ax.contourf(X,Y,u[z_ind,:,:],np.linspace(crange[0],crange[-1],75),cmap='bwr',extend='both')
#plot = ax.contourf(X,Y,u[z_ind,:,:],75,cmap='bwr',extend='both')
ax.set_xlim(0,50)
ax.set_ylim(0,20)
plot.ax.set_xlabel('x (km)')
plot.ax.set_ylabel('y (km)')

cbar = plt.colorbar(plot,ticks=crange,format='%.0f',fraction=0.023,aspect=15)
#cbar = plt.colorbar(plot,format='%.1f')
cbar.ax.xaxis.set_tick_params(pad=0.5)

plt.tight_layout()
plt.show()
