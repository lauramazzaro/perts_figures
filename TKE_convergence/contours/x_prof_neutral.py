# 'x_prof.py'

from scipy.io import loadmat
dh = loadmat('n_008_013.mat')


# Plots TKE vs. x for a few heights for all nested runs

# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('/Users/lauramazzaro/Documents/Work/Perts/Article/Figures/new_cmaps.py')

# Modify plotting parameters!
execfile('/Users/lauramazzaro/Documents/Work/Perts/Article/Figures/new_params.py')

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# --------- INPUT ----------

y_crop = 5000

crange = [0,0.25,0.5,0.75]

# --------------------------

fh = plt.figure(figsize=(9,5))
ax = fh.add_subplot(111)

dx = dh['dx'][0][0]
y_ind = np.ceil(y_crop/dx)

X = np.arange(dh['TKE_res'].shape[1])*dx/1000
Z = np.squeeze(np.average(dh['z_axis'][:,:],axis=1))/1000
plot=ax.contourf(X,Z,dh['TKE_res'],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='max')
#plot=ax.contourf(X,Z,dh['TKE_res'],50,cmap=cmaps['viridis'],extend='max')

cbar = plt.colorbar(plot,ticks=crange)
#cbar = plt.colorbar(plot)

# Plot height lines:
#plt.plot([min(X),max(X)],[Z[np.ceil(100/20)],Z[np.ceil(100/20)]],'--',color=line_cols[1],)
#plt.plot([min(X),max(X)],[Z[np.ceil(250/20)],Z[np.ceil(250/20)]],'--',color=line_cols[5],)
#plt.plot([min(X),max(X)],[Z[np.ceil(350/20)],Z[np.ceil(350/20)]],'--',color=line_cols[8])

plot.ax.set_ylabel('z (km)')
plot.ax.set_xlabel('x (km)')

ax.set_xlim([0,50])
#ax.set_ylim([0.02,1.48])

plt.tight_layout()
plt.show()

