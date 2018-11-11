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
plt.plot(X/1000,dat,'k',label=R'$\mathregular{C_{\theta}}$')

dh = loadmat('c_003_021.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[2],label=R'$\mathregular{{C}_{xy500}}$')

dh = loadmat('c_003_022.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[3],label=R'$\mathregular{{C}_{xy750}}$')

dh = loadmat('c_003_017.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[4],label=R'$\mathregular{{C}_{xy1000}}$')

dh = loadmat('c_003_016.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[7],label=R'$\mathregular{{C}_{xy2000}}$')

dh = loadmat('c_003_024.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[6],label=R'$\mathregular{{C}_{xy5000}}$')

rect = matplotlib.patches.Rectangle((0,0.9),50,0.2,color='#e6e6e6')
plt.gca().add_patch(rect)

plt.ylabel(R'$\mathregular{q/q_o (-)}$')

plt.legend(fontsize=10)

plt.xlim([0,50])
plt.xticks([])
plt.ylim([0,2])
plt.yticks([0,1,2])
plt.text(47, 1.7, '(a)')

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
plt.plot(X/1000,dat,'k',label=R'$\mathregular{C_{\theta}}$')

dh = loadmat('c_003_021.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[2],label=R'$\mathregular{{C}_{xy500}}$')

dh = loadmat('c_003_022.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[3],label=R'$\mathregular{{C}_{xy750}}$')

dh = loadmat('c_003_017.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[4],label=R'$\mathregular{{C}_{xy1000}}$')

dh = loadmat('c_003_016.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[7],label=R'$\mathregular{{C}_{xy2000}}$')

dh = loadmat('c_003_024.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1000/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[6],label=R'$\mathregular{{C}_{xy5000}}$')

rect = matplotlib.patches.Rectangle((0,0.9),50,0.2,color='#e6e6e6')
plt.gca().add_patch(rect)

plt.ylabel(R'$\mathregular{q/q_o (-)}$')

plt.xlim([0,50])
plt.xticks([])
plt.ylim([0,2])
plt.yticks([0,1,2])
plt.text(47, 1.7, '(b)')

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
plt.plot(X/1000,dat,'k',label=R'$\mathregular{C_{\theta}}$')

dh = loadmat('c_003_021.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[2],label=R'$\mathregular{{C}_{xy500}}$')

dh = loadmat('c_003_022.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[3],label=R'$\mathregular{{C}_{xy750}}$')

dh = loadmat('c_003_017.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[4],label=R'$\mathregular{{C}_{xy1000}}$')

dh = loadmat('c_003_016.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[7],label=R'$\mathregular{{C}_{xy2000}}$')

dh = loadmat('c_003_024.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(1500/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[6],label=R'$\mathregular{{C}_{xy5000}}$')

rect = matplotlib.patches.Rectangle((0,0.9),50,0.2,color='#e6e6e6')
plt.gca().add_patch(rect)

plt.ylabel(R'$\mathregular{q/q_o (-)}$')

plt.xlim([0,50])
plt.ylim([0,2])
plt.yticks([0,1,2])
plt.text(47, 1.7, '(c)')

plt.tight_layout()
plt.show()


