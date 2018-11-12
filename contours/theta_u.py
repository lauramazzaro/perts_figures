# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('../new_cmaps.py')

# Modify plotting parameters!
execfile('../new_params.py')

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# --------- INPUT ----------

crange = [5,6,7,8,9,10,11]

# ------------- Theta ---------------

fig,axs = plt.subplots(3,1,figsize=(8,12))

dh = np.load('n_d02_009_001_000.npz')

dx = dh['dx']
z_ind = 12

X = np.squeeze(np.arange(dh['u'].shape[2])*dx/1000)
Y = np.squeeze(np.arange(dh['u'].shape[1])*dx/1000)
im = axs.flat[0].contourf(X,Y,dh['u'][z_ind,:,:],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='both')

axs.flat[0].set_ylabel('z (km)')
#axs.flat[0].set_xlabel('x (km)')
axs.flat[0].set_xlim([0,50])
axs.flat[0].set_ylim([0,20])
axs.flat[0].set_xticks([])
axs.flat[0].set_yticks([0,5,10,15,20])
axs.flat[0].text(-9,20,'(a)')

# ------------- z-force ---------------

dh = np.load('n_d02_009_001_001.npz')

dx = dh['dx']

X = np.squeeze(np.arange(dh['u'].shape[2])*dx/1000)
Y = np.squeeze(np.arange(dh['u'].shape[1])*dx/1000)
im = axs.flat[1].contourf(X,Y,dh['u'][z_ind,:,:],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='both')

axs.flat[1].set_ylabel('z (km)')
#axs.flat[1].set_xlabel('x (km)')
axs.flat[1].set_xlim([0,50])
axs.flat[1].set_ylim([0,20])
axs.flat[1].set_xticks([])
axs.flat[1].set_yticks([0,5,10,15,20])
axs.flat[1].text(-9,20,'(b)')

# ------------- xy-Force  ---------------

dh = np.load('n_d02_009_001_003.npz')

dx = dh['dx']

X = np.squeeze(np.arange(dh['u'].shape[2])*dx/1000)
Y = np.squeeze(np.arange(dh['u'].shape[1])*dx/1000)
im = axs.flat[2].contourf(X,Y,dh['u'][z_ind,:,:],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='both')

axs.flat[2].set_ylabel('z (km)')
axs.flat[2].set_xlabel('x (km)')
axs.flat[2].set_xlim([0,50])
axs.flat[2].set_ylim([0,20])
axs.flat[2].set_yticks([0,5,10,15,20])
axs.flat[2].text(-9,20,'(c)')

plt.tight_layout()

fig.subplots_adjust(bottom=0.2)

cbar_ax = fig.add_axes([0.165,0.1,0.79,0.02])
fig.colorbar(im,cax=cbar_ax,ticks=crange,orientation='horizontal')

plt.savefig('../theta_u.png', dpi=600)

plt.show()
