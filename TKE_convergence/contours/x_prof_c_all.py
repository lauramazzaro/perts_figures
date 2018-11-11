# Plots TKE vs. x for a few heights for all nested runs

# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('/Users/lauramazzaro/Documents/Work/Perts/Article/Figures/new_cmaps.py')

# Modify plotting parameters!
execfile('/Users/lauramazzaro/Documents/Work/Perts/Article/Figures/new_params.py')

import matplotlib.pyplot as plt
from scipy.io import loadmat
import numpy as np
import matplotlib

# --------- INPUT ----------

y_crop = 5000

crange = [0,0.5,1,1.5,2,2.5]

# ------------- No Perts ---------------

fig,axs = plt.subplots(2,2,figsize=(14,8))

dh = loadmat('c_003_001.mat')

dx = dh['dx'][0][0]
y_ind = np.ceil(y_crop/dx)

X = np.arange(dh['TKE_res'].shape[1])*dx/1000
Z = np.squeeze(np.average(dh['z_axis'][:,:],axis=1))/1000
im = axs.flat[0].contourf(X,Z,dh['TKE_res'],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='max')

axs.flat[0].set_ylabel('z (km)')
#axs.flat[0].set_xlabel('x (km)')
axs.flat[0].set_xlim([0,50])
axs.flat[0].set_xticks([])
axs.flat[0].set_yticks([1,2,3])
axs.flat[0].text(-8,3.2,'(a)')

# ------------- Theta ---------------

dh = loadmat('c_003_002.mat')

dx = dh['dx'][0][0]
y_ind = np.ceil(y_crop/dx)

X = np.arange(dh['TKE_res'].shape[1])*dx/1000
Z = np.squeeze(np.average(dh['z_axis'][:,:],axis=1))/1000
im = axs.flat[1].contourf(X,Z,dh['TKE_res'],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='max')

#axs.flat[1].set_xlabel('x (km)')
axs.flat[1].set_xlim([0,50])
axs.flat[1].set_xticks([])
axs.flat[1].set_yticks([])
axs.flat[1].text(51,3.2,'(b)')

# ------------- z-force ---------------

dh = loadmat('c_003_011.mat')

dx = dh['dx'][0][0]
y_ind = np.ceil(y_crop/dx)

X = np.arange(dh['TKE_res'].shape[1])*dx/1000
Z = np.squeeze(np.average(dh['z_axis'][:,:],axis=1))/1000
im = axs.flat[2].contourf(X,Z,dh['TKE_res'],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='max')

axs.flat[2].set_ylabel('z (km)')
#axs.flat[2].set_xlabel('x (km)')
axs.flat[2].set_xlim([0,50])
axs.flat[2].set_xlabel('x (km)')
axs.flat[2].set_yticks([1,2,3])
axs.flat[2].text(-8,3.2,'(c)')

# ------------- xy-Force  ---------------

dh = loadmat('c_003_017.mat')

dx = dh['dx'][0][0]
y_ind = np.ceil(y_crop/dx)

X = np.arange(dh['TKE_res'].shape[1])*dx/1000
Z = np.squeeze(np.average(dh['z_axis'][:,:],axis=1))/1000
im = axs.flat[3].contourf(X,Z,dh['TKE_res'],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='max')

axs.flat[3].set_xlabel('x (km)')
axs.flat[3].set_xlim([0,50])
axs.flat[3].set_yticks([])
axs.flat[3].text(51,3.2,'(d)')
plt.tight_layout()

fig.subplots_adjust(bottom=0.25)

cbar_ax = fig.add_axes([0.25,0.1,0.5,0.03])
fig.colorbar(im,cax=cbar_ax,ticks=crange,orientation='horizontal')

plt.show()

