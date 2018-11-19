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
crange = [5,6,7,8,9,10,11]

z_plot = 250

# ------------- Theta --------------

fig,axs = plt.subplots(3,1,figsize=(9,12))

with np.load('neutral_008_001_theta_0.50K/d02_0001-01-02_07:00:00.npz') as dh:
     u = dh['u']
     z = np.squeeze(dh['z'])
     dx = dh['dx'][0][0]

z_ind = [i for i in np.arange(len(z)) if z[i] >= z_plot][0]

X = np.arange(u.shape[2])*dx/1000
Y = np.arange(u.shape[1])*dx/1000

axs.flat[0].contourf(X,Y,u[z_ind,:,:],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='both')
axs.flat[0].set_xlim(0,50)
axs.flat[0].set_xticks([])
axs.flat[0].set_ylim(0,20)
axs.flat[0].set_ylabel('y (km)')
axs.flat[0].set_aspect('equal')
axs.flat[0].text(-8.5,19,'(a)')

# ------------- vertical --------------

with np.load('neutral_008_005_w1250/d02_0001-01-02_07:00:00.npz') as dh:
     u = dh['u']
     z = np.squeeze(dh['z'])
     dx = dh['dx'][0][0]

z_ind = [i for i in np.arange(len(z)) if z[i] >= z_plot][0]


X = np.arange(u.shape[2])*dx/1000
Y = np.arange(u.shape[1])*dx/1000

axs.flat[1].contourf(X,Y,u[z_ind,:,:],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='both')
axs.flat[1].set_xlim(0,50)
axs.flat[1].set_xticks([])
axs.flat[1].set_ylim(0,20)
axs.flat[1].set_ylabel('y (km)')
axs.flat[1].set_aspect('equal')
axs.flat[1].text(-8.5,19,'(b)')

# ------------- horizontal --------------

with np.load('neutral_008_003_uv1000/d02_0001-01-02_07:00:00.npz') as dh:
     u = dh['u']
     z = np.squeeze(dh['z'])
     dx = dh['dx'][0][0]

z_ind = [i for i in np.arange(len(z)) if z[i] >= z_plot][0]


X = np.arange(u.shape[2])*dx/1000
Y = np.arange(u.shape[1])*dx/1000

im = axs.flat[2].contourf(X,Y,u[z_ind,:,:],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='both')
plt.gca().set_xlim(0,50)
axs.flat[2].set_ylim(0,20)
axs.flat[2].set_ylabel('y (km)')
axs.flat[2].set_xlabel('x (km)')
axs.flat[2].set_aspect('equal')
axs.flat[2].text(-8.5,19,'(c)')

plt.tight_layout()

fig.subplots_adjust(bottom=0.2)

cbar_ax = fig.add_axes([0.165,0.1,0.74,0.02])
fig.colorbar(im,cax = cbar_ax,ticks=crange,orientation='horizontal')

plt.savefig('../figure_9.png',dpi=600)

plt.show()
