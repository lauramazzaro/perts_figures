# 'x_conv_conv_amp_uv.py'

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

dh = loadmat('c_003_001.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(2000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[-2],linewidth=1.5,label=R'$\mathregular{C_{NP}}$')

dh = loadmat('c_003_002.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(2000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,'k',label=R'$\mathregular{C_{\theta}}$')

dh = loadmat('c_003_007.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(2000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{C}_{xy5000}}$')

dh = loadmat('c_003_011.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(2000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[1],label=R'$\mathregular{{C}_{z15000}}$')

dh = loadmat('c_003_012.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(2000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[4],label=R'$\mathregular{{C}_{xy1500+z5000}}$')

dh = loadmat('c_003_013.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(2000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[5],label=R'$\mathregular{{C}_{xy1500+\theta}}$')

dh = loadmat('c_003_014.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(2000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[8],label=R'$\mathregular{{C}_{z5000+\theta}}$')

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


