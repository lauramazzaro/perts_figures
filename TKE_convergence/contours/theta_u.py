# Plots TKE vs. x for a few heights for all nested runs

# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('../../new_cmaps.py')

# Modify plotting parameters!
execfile('../../new_params.py')

import matplotlib.pyplot as plt
from scipy.io import loadmat
import numpy as np
import matplotlib

# --------- INPUT ----------

y_crop = 5000

crange = [0,0.25,0.5,0.75]

# ------------- Theta 0.5 K ---------------

fig,axs = plt.subplots(4,1,figsize=(8,16))

dh = loadmat('n_009_001_000.mat')

dx = dh['dx'][0][0]
y_ind = np.ceil(y_crop/dx)

X = np.arange(dh['TKE_res'].shape[1])*dx/1000
Z = np.squeeze(np.average(dh['z_axis'][:,:],axis=1))/1000
im = axs.flat[0].contourf(X,Z,dh['TKE_res'],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='max')

axs.flat[0].set_ylabel('z (km)')
#axs.flat[0].set_xlabel('x (km)')
axs.flat[0].set_xlim([0,50])
axs.flat[0].set_xticks([])
axs.flat[0].set_yticks([0.2,0.6,1.0,1.4])
axs.flat[0].text(-10,1.4,'(a)')

# ------------- Theta 0.25 K ---------------

dh = loadmat('n_009_001_001.mat')

dx = dh['dx'][0][0]
y_ind = np.ceil(y_crop/dx)

X = np.arange(dh['TKE_res'].shape[1])*dx/1000
Z = np.squeeze(np.average(dh['z_axis'][:,:],axis=1))/1000
im = axs.flat[1].contourf(X,Z,dh['TKE_res'],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='max')

axs.flat[1].set_ylabel('z (km)')
#axs.flat[1].set_xlabel('x (km)')
axs.flat[1].set_xlim([0,50])
axs.flat[1].set_xticks([])
axs.flat[1].set_yticks([0.2,0.6,1.0,1.4])
axs.flat[1].text(-10,1.4,'(b)')

# ------------- Theta 0.125 K  ---------------

dh = loadmat('n_009_001_003.mat')

dx = dh['dx'][0][0]
y_ind = np.ceil(y_crop/dx)

X = np.arange(dh['TKE_res'].shape[1])*dx/1000
Z = np.squeeze(np.average(dh['z_axis'][:,:],axis=1))/1000
im = axs.flat[2].contourf(X,Z,dh['TKE_res'],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='max')

axs.flat[2].set_ylabel('z (km)')
axs.flat[2].set_xlabel('x (km)')
axs.flat[2].set_xlim([0,50])
axs.flat[2].set_yticks([0.4,0.8,1.2])
axs.flat[2].text(-10,1.4,'(c)')

# ------------- Theta 0.35 K  ---------------

dh = loadmat('n_009_001_004.mat')

dx = dh['dx'][0][0]
y_ind = np.ceil(y_crop/dx)

X = np.arange(dh['TKE_res'].shape[1])*dx/1000
Z = np.squeeze(np.average(dh['z_axis'][:,:],axis=1))/1000
im = axs.flat[3].contourf(X,Z,dh['TKE_res'],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='max')

axs.flat[3].set_ylabel('z (km)')
axs.flat[3].set_xlabel('x (km)')
axs.flat[3].set_xlim([0,50])
axs.flat[3].set_yticks([0.4,0.8,1.2])
axs.flat[3].text(-10,1.4,'(d)')

plt.tight_layout()

fig.subplots_adjust(bottom=0.2)

cbar_ax = fig.add_axes([0.165,0.1,0.79,0.02])
fig.colorbar(im,cax=cbar_ax,ticks=crange,orientation='horizontal')

plt.savefig('../../theta_u_TKE.png', dpi=600)

plt.show()

