# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('../new_cmaps.py')

# Modify plotting parameters!
execfile('../new_params.py')

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# --------- INPUT ----------

crange = [6,7,8,9,10,11]

# ------------- Theta ---------------

fig,axs = plt.subplots(2,2,figsize=(14,8))

dh = np.load('neutral_009_001_000_theta_0.5K/d02_0001-01-02_07:00:00.npz')

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
#axs.flat[0].set_yticks([])
axs.flat[0].text(-8,20,'(a)')

# ------------- z-force ---------------

dh = np.load('neutral_009_001_004_theta_0.35K/d02_0001-01-02_07:00:00.npz')

dx = dh['dx']

X = np.squeeze(np.arange(dh['u'].shape[2])*dx/1000)
Y = np.squeeze(np.arange(dh['u'].shape[1])*dx/1000)
im = axs.flat[1].contourf(X,Y,dh['u'][z_ind,:,:],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='both')

#axs.flat[1].set_ylabel('z (km)')
#axs.flat[1].set_xlabel('x (km)')
axs.flat[1].set_xlim([0,50])
axs.flat[1].set_ylim([0,20])
axs.flat[1].set_xticks([])
axs.flat[1].set_yticks([])
#axs.flat[1].set_yticks([0,5,10,15,20])
axs.flat[1].text(-4,20,'(b)')

# ------------- Theta ---------------

dh = np.load('neutral_009_001_000_theta_0.5K/d02_0001-01-02_07:00:00.npz')

dx = dh['dx']
z_ind = 5

X = np.squeeze(np.arange(dh['u'].shape[2])*dx/1000)
Y = np.squeeze(np.arange(dh['u'].shape[1])*dx/1000)
im = axs.flat[2].contourf(X,Y,dh['u'][z_ind,:,:],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='both')

axs.flat[2].set_ylabel('z (km)')
axs.flat[2].set_xlabel('x (km)')
axs.flat[2].set_xlim([0,50])
axs.flat[2].set_ylim([0,20])
#axs.flat[2].set_xticks([])
axs.flat[2].set_yticks([0,5,10,15,20])
#axs.flat[2].set_yticks([])
axs.flat[2].text(-8,20,'(c)')

# ------------- z-force ---------------

dh = np.load('neutral_009_001_004_theta_0.35K/d02_0001-01-02_07:00:00.npz')

dx = dh['dx']

X = np.squeeze(np.arange(dh['u'].shape[2])*dx/1000)
Y = np.squeeze(np.arange(dh['u'].shape[1])*dx/1000)
im = axs.flat[3].contourf(X,Y,dh['u'][z_ind,:,:],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='both')

#axs.flat[3].set_ylabel('z (km)')
axs.flat[3].set_xlabel('x (km)')
axs.flat[3].set_xlim([0,50])
axs.flat[3].set_ylim([0,20])
#axs.flat[3].set_xticks([])
axs.flat[3].set_yticks([])
#axs.flat[3].set_yticks([0,5,10,15,20])
axs.flat[3].text(-4,20,'(d)')


plt.tight_layout()

fig.subplots_adjust(bottom=0.25)

cbar_ax = fig.add_axes([0.15,0.1,0.75,0.03])
cbar = fig.colorbar(im,cax=cbar_ax,ticks=crange,orientation='horizontal')
plt.savefig('../figure_5.png', dpi=600)

plt.show()
