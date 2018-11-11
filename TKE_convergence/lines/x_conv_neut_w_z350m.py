# 'x_conv_neut_amp_w.py'

# Plots TKE vs. x for a few heights for all nested runs without perturbations

# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('/Users/lauramazzaro/Documents/Work/Perts/Article/Figures/new_cmaps.py')

# Modify plotting parameters!
execfile('/Users/lauramazzaro/Documents/Work/Perts/Article/Figures/new_params.py')

import matplotlib.pyplot as plt
from scipy.io import loadmat
import numpy as np
import matplotlib
from matplotlib import gridspec

plt.figure(figsize=(13,5))
 
plt.subplot(gridspec.GridSpec(1,4)[0,0:3])

dh = loadmat('n_008_001.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{N}_{\theta}}$')

dh = loadmat('n_008_011.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{N}_{z1000}}$')

dh = loadmat('n_008_005.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[1],label=R'$\mathregular{{N}_{z1250}}$')

dh = loadmat('n_008_006.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[2],label=R'$\mathregular{{N}_{z1500}}$')

dh = loadmat('n_008_007.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[5],label=R'$\mathregular{{N}_{z1750}}$')


rect = matplotlib.patches.Rectangle((0,0.9),50,0.2,color='#e6e6e6')
plt.gca().add_patch(rect)

plt.legend(bbox_to_anchor=(1.05,0.5), loc=6, borderaxespad=0.,borderpad=1,fontsize=16)

plt.xlabel('x (km)')
plt.ylabel('TKE (m$^\mathregular{2}$ s$^\mathregular{-2}$)')

plt.xlim([0,50])
plt.ylim([0,2])
plt.yticks([0,1,2])

plt.tight_layout()
plt.show()


