# 'contour_u.py'
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

# 018_000_d01:
crange = [5,7,9,11]

fig,axs = plt.subplots(1,2,figsize=(15,4))

# ------------ Neutral + z = 250m ---------------

z_plot = 100;

with np.load('neutral_parent/d01_0001-01-02_07:00:00.npz') as dh:
     u = dh['u']
     z = np.squeeze(dh['z'])
     dx = dh['dx'][0][0]

z_ind = [i for i in np.arange(len(z)) if z[i] >= z_plot][0]

X = np.arange(u.shape[2])*dx/1000
Y = np.arange(u.shape[1])*dx/1000

im = axs.flat[0].contourf(X,Y,u[z_ind,:,:],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='both')
axs.flat[0].set_aspect('equal')
axs.flat[0].set_xlim(0,50)
axs.flat[0].set_ylim(0,20)
axs.flat[0].set_xlabel('x (km)')
axs.flat[0].set_ylabel('y (km)')
axs.flat[0].text(-8,20,'(a)')

# ------------ Convective + z = 1000m ---------------

z_plot = 400;

with np.load('convective_parent/d01_0001-01-01_09:55:00.npz') as dh:
     u = dh['u']
     z = np.squeeze(dh['z'])
     dx = dh['dx'][0][0]

z_ind = [i for i in np.arange(len(z)) if z[i] >= z_plot][0]


X = np.arange(u.shape[2])*dx/1000
Y = np.arange(u.shape[1])*dx/1000

im = axs.flat[1].contourf(X,Y,u[z_ind,:,:],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='both')
axs.flat[1].set_aspect('equal')
axs.flat[1].set_xlim(0,50)
axs.flat[1].set_ylim(0,20)
axs.flat[1].set_xlabel('x (km)')
axs.flat[1].set_yticks([])
axs.flat[1].text(-4,20,'(b)')

plt.tight_layout()

fig.subplots_adjust(right=0.9)

cbar_ax = fig.add_axes([0.93,0.24,0.01,0.6])
cb = fig.colorbar(im,cax=cbar_ax,ticks=crange,orientation='vertical')

plt.savefig('../figure_4.png',dpi=600)

plt.show()
