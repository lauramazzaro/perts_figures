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

# 018_000_d01:
crange = [-4,-2,0,2,4]

z_plot = 1000

# ------------- No Perts --------------

fig,axs = plt.subplots(2,2,figsize=(14,8))

with np.load('convective_003_001_noperts/d02_0001-01-01_10:00:00.npz') as dh:
     u = dh['w']
     z = np.squeeze(dh['z'])
     dx = dh['dx'][0][0]

z_ind = [i for i in np.arange(len(z)) if z[i] >= z_plot][0]

X = np.arange(u.shape[2])*dx/1000
Y = np.arange(u.shape[1])*dx/1000

axs.flat[0].contourf(X,Y,u[z_ind,:,:],np.linspace(crange[0],crange[-1],75),cmap='bwr',extend='both')
axs.flat[0].set_xlim(0,50)
axs.flat[0].set_xticks([])
axs.flat[0].set_ylim(0,20)
axs.flat[0].set_ylabel('y (km)')
axs.flat[0].set_aspect('equal')
axs.flat[0].text(-9,19,'(a)')

# ------------- Theta --------------

with np.load('convective_003_002_theta_0.33K/d02_0001-01-01_10:00:00.npz') as dh:
     u = dh['w']
     z = np.squeeze(dh['z'])
     dx = dh['dx'][0][0]

z_ind = [i for i in np.arange(len(z)) if z[i] >= z_plot][0]

X = np.arange(u.shape[2])*dx/1000
Y = np.arange(u.shape[1])*dx/1000

axs.flat[1].contourf(X,Y,u[z_ind,:,:],np.linspace(crange[0],crange[-1],75),cmap='bwr',extend='both')
axs.flat[1].set_xlim(0,50)
axs.flat[1].set_xticks([])
axs.flat[1].set_yticks([])
axs.flat[1].set_ylim(0,20)
axs.flat[1].set_aspect('equal')
axs.flat[1].text(51,19,'(b)')

# ------------- vertical --------------

with np.load('convective_003_011_w15000/d02_0001-01-01_10:00:00.npz') as dh:
     u = dh['w']
     z = np.squeeze(dh['z'])
     dx = dh['dx'][0][0]

z_ind = [i for i in np.arange(len(z)) if z[i] >= z_plot][0]


X = np.arange(u.shape[2])*dx/1000
Y = np.arange(u.shape[1])*dx/1000

axs.flat[2].contourf(X,Y,u[z_ind,:,:],np.linspace(crange[0],crange[-1],75),cmap='bwr',extend='both')
axs.flat[2].set_xlim(0,50)
axs.flat[2].set_xlabel('x (km)')
axs.flat[2].set_ylim(0,20)
axs.flat[2].set_ylabel('y (km)')
axs.flat[2].set_aspect('equal')
axs.flat[2].text(-9,19,'(c)')

# ------------- horizontal --------------

with np.load('convective_003_007_uv5000/d02_0001-01-01_10:00:00.npz') as dh:
     u = dh['w']
     z = np.squeeze(dh['z'])
     dx = dh['dx'][0][0]

z_ind = [i for i in np.arange(len(z)) if z[i] >= z_plot][0]


X = np.arange(u.shape[2])*dx/1000
Y = np.arange(u.shape[1])*dx/1000

im = axs.flat[3].contourf(X,Y,u[z_ind,:,:],np.linspace(crange[0],crange[-1],75),cmap='bwr',extend='both')
axs.flat[3].set_xlim(0,50)
axs.flat[3].set_ylim(0,20)
axs.flat[3].set_yticks([])
axs.flat[3].set_xlabel('x (km)')
axs.flat[3].set_aspect('equal')
axs.flat[3].text(51,19,'(d)')

plt.tight_layout()

fig.subplots_adjust(bottom=0.2)

cbar_ax = fig.add_axes([0.165,0.1,0.74,0.02])
fig.colorbar(im,cax = cbar_ax,ticks=crange,orientation='horizontal')

plt.savefig('../figure_12.png',dpi=600)

plt.show()
