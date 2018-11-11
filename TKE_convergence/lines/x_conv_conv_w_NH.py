# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('/Users/lauramazzaro/Documents/Work/Perts/Article/Figures/new_cmaps.py')

# Modify plotting parameters!
execfile('/Users/lauramazzaro/Documents/Work/Perts/Article/Figures/new_params.py')

import matplotlib.pyplot as plt
from scipy.io import loadmat
import numpy as np
import matplotlib
from matplotlib import gridspec

plt.figure(figsize=(10,10))
 
# --------------------------- z = 500m ----------------------

plt.subplot(3,1,1)


dh = loadmat('c_003_001.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[-2],linewidth=1.5,label=R'$\mathregular{C_{NP}}$')

dh = loadmat('c_003_002.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{C}_{\theta}}$')

dh = loadmat('c_003_004.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{C}_{z1500}}$')

dh = loadmat('c_003_006.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[1],label=R'$\mathregular{{C}_{z2500}}$')

dh = loadmat('c_003_008.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[3],label=R'$\mathregular{{C}_{z5000}}$')

dh = loadmat('c_003_007.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[5],label=R'$\mathregular{{C}_{z10000}}$')

dh = loadmat('c_003_011.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[8],label=R'$\mathregular{{C}_{z15000}}$')

rect = matplotlib.patches.Rectangle((0,0.9),50,0.2,color='#e6e6e6')
plt.gca().add_patch(rect)


plt.ylabel(R'$\mathregular{q/q_o (-)}$')

plt.xlim([0,50])
plt.xticks([])
plt.ylim([0,3])
plt.yticks([0,1,2,3])
plt.text(47, 2.5, '(a)')

# --------------------------- z = 1000m ----------------------

plt.subplot(3,1,2)


dh = loadmat('c_003_001.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[-2],linewidth=1.5,label=R'$\mathregular{C_{NP}}$')

dh = loadmat('c_003_002.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{C}_{\theta}}$')

dh = loadmat('c_003_004.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{C}_{z1500}}$')

dh = loadmat('c_003_006.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[1],label=R'$\mathregular{{C}_{z2500}}$')

dh = loadmat('c_003_008.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[3],label=R'$\mathregular{{C}_{z5000}}$')

dh = loadmat('c_003_007.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[5],label=R'$\mathregular{{C}_{z10000}}$')

dh = loadmat('c_003_011.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[8],label=R'$\mathregular{{C}_{z15000}}$')

rect = matplotlib.patches.Rectangle((0,0.9),50,0.2,color='#e6e6e6')
plt.gca().add_patch(rect)


plt.ylabel(R'$\mathregular{q/q_o (-)}$')

plt.xlim([0,50])
plt.xticks([])
plt.ylim([0,3])
plt.yticks([0,1,2,3])
plt.text(47, 2.5, '(b)')


# --------------------------- z = 1500m ----------------------

plt.subplot(3,1,3)


dh = loadmat('c_003_001.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[-2],linewidth=1.5,label=R'$\mathregular{C_{NP}}$')

dh = loadmat('c_003_002.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{C}_{\theta}}$')

dh = loadmat('c_003_004.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{C}_{z1500}}$')

dh = loadmat('c_003_006.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[1],label=R'$\mathregular{{C}_{z2500}}$')

dh = loadmat('c_003_008.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[3],label=R'$\mathregular{{C}_{z5000}}$')

dh = loadmat('c_003_007.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[5],label=R'$\mathregular{{C}_{z10000}}$')

dh = loadmat('c_003_011.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[8],label=R'$\mathregular{{C}_{z15000}}$')

rect = matplotlib.patches.Rectangle((0,0.9),50,0.2,color='#e6e6e6')
plt.gca().add_patch(rect)

plt.ylabel(R'$\mathregular{q/q_o (-)}$')
plt.xlabel('x [km]')

plt.xlim([0,50])
plt.ylim([0,2])
plt.yticks([0,1,2])
plt.text(47, 1.65, '(c)')

plt.tight_layout()
plt.show()


