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

#_____________________________ z = 100m _______________________________
 
plt.subplot(3,1,1)

dh = loadmat('n_008_001.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(100/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{N}_{\theta}}$')

dh = loadmat('n_008_002.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(100/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{N}_{xy750}}$')

dh = loadmat('n_008_003.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(100/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[3],label=R'$\mathregular{{N}_{xy1000}}$')

dh = loadmat('n_008_004.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(100/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[8],label=R'$\mathregular{{N}_{xy1250}}$')

rect = matplotlib.patches.Rectangle((0,0.9),50,0.2,color='#e6e6e6')
plt.gca().add_patch(rect)

#plt.legend(bbox_to_anchor=(1.05,0.5), loc=6, borderaxespad=0.,borderpad=1,fontsize=16)

#plt.xlabel('x (km)')
plt.ylabel(R'$\mathregular{q/q_o (-)}$')
plt.xlim([0,50])
plt.xticks([])
plt.ylim([0,2])
plt.yticks([0,1,2])
plt.text(47, 1.7, '(a)')

#_____________________________ z = 250m _______________________________
 
plt.subplot(3,1,2)

dh = loadmat('n_008_001.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{N}_{\theta}}$')

dh = loadmat('n_008_002.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{N}_{xy750}}$')

dh = loadmat('n_008_003.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[3],label=R'$\mathregular{{N}_{xy1000}}$')

dh = loadmat('n_008_004.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[8],label=R'$\mathregular{{N}_{xy1250}}$')

rect = matplotlib.patches.Rectangle((0,0.9),50,0.2,color='#e6e6e6')
plt.gca().add_patch(rect)

#plt.legend(bbox_to_anchor=(1.05,0.5), loc=6, borderaxespad=0.,borderpad=1,fontsize=16)

#plt.xlabel('x (km)')
plt.ylabel(R'$\mathregular{q/q_o (-)}$')
plt.xlim([0,50])
plt.xticks([])
plt.ylim([0,2])
plt.yticks([0,1,2])
plt.text(47, 1.7, '(b)')

#_____________________________ z = 250m _______________________________
 
plt.subplot(3,1,2)

dh = loadmat('n_008_001.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{N}_{\theta}}$')

dh = loadmat('n_008_002.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{N}_{xy750}}$')

dh = loadmat('n_008_003.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[3],label=R'$\mathregular{{N}_{xy1000}}$')

dh = loadmat('n_008_004.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[8],label=R'$\mathregular{{N}_{xy1250}}$')

rect = matplotlib.patches.Rectangle((0,0.9),50,0.2,color='#e6e6e6')
plt.gca().add_patch(rect)

#plt.legend(bbox_to_anchor=(1.05,0.5), loc=6, borderaxespad=0.,borderpad=1,fontsize=16)

#plt.xlabel('x (km)')
plt.ylabel(R'$\mathregular{q/q_o (-)}$')
plt.xlim([0,50])
plt.xticks([])
plt.ylim([0,2])
plt.yticks([0,1,2])

#_____________________________ z = 350m _______________________________
 
plt.subplot(3,1,3)

dh = loadmat('n_008_001.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{N}_{\theta}}$')

dh = loadmat('n_008_002.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{N}_{xy750}}$')

dh = loadmat('n_008_003.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[3],label=R'$\mathregular{{N}_{xy1000}}$')

dh = loadmat('n_008_004.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[8],label=R'$\mathregular{{N}_{xy1250}}$')

rect = matplotlib.patches.Rectangle((0,0.9),50,0.2,color='#e6e6e6')
plt.gca().add_patch(rect)

#plt.legend(bbox_to_anchor=(1.05,0.5), loc=6, borderaxespad=0.,borderpad=1,fontsize=16)

plt.xlabel('x (km)')
plt.ylabel(R'$\mathregular{q/q_o (-)}$')
plt.xlim([0,50])
plt.ylim([0,2])
plt.yticks([0,1,2])
plt.text(47, 1.7, '(c)')

plt.tight_layout()
plt.show()


