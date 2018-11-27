# 'x_conv_neut_amp_w.py'

# Plots TKE vs. x for a few heights for all nested runs without perturbations

# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('../../new_cmaps.py')

# Modify plotting parameters!
execfile('../../new_params.py')

import matplotlib.pyplot as plt
from scipy.io import loadmat
import numpy as np
import matplotlib
from matplotlib import gridspec

plt.figure(figsize=(13,13))
 
#_____________________________ z = 100m _______________________________

plt.subplot(3,1,1)

dh = loadmat('c_003_001.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(100/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[-1],label=R'$\mathregular{{N}_{NP}}$')

dh = loadmat('c_003_002.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(100/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{N}_{\theta}}$')

dh = loadmat('c_003_004.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(100/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{C}_{z1500}}$')

dh = loadmat('c_003_006.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(100/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[1],label=R'$\mathregular{{C}_{z2500}}$')

dh = loadmat('c_003_008.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(100/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[2],label=R'$\mathregular{{N}_{z1500}}$')

dh = loadmat('c_003_009.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(100/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[3],label=R'$\mathregular{{C}_{z2500}}$')

dh = loadmat('c_003_011.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(100/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[4],label=R'$\mathregular{{N}_{z1500}}$')

rect = matplotlib.patches.Rectangle((0,0.9),50,0.2,color='#e6e6e6')
plt.gca().add_patch(rect)

#plt.legend(bbox_to_anchor=(1.05,0.5), loc=6, borderaxespad=0.,borderpad=1,fontsize=16)

#plt.xlabel('x (km)')
plt.ylabel(R'$\mathregular{q/q_o (-)}$')

plt.xlim([0,50])
plt.xticks([])
plt.ylim([0,3])
plt.yticks([0,1,2,3])
plt.text(47, 2.7, '(a)')

#_____________________________ z = 250m _______________________________

plt.subplot(3,1,2)

dh = loadmat('c_003_001.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[-1],label=R'$\mathregular{{N}_{NP}}$')

dh = loadmat('c_003_002.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{N}_{\theta}}$')

dh = loadmat('c_003_004.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{C}_{z1500}}$')

dh = loadmat('c_003_006.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[1],label=R'$\mathregular{{C}_{z2500}}$')

dh = loadmat('c_003_008.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[2],label=R'$\mathregular{{N}_{z1500}}$')

dh = loadmat('c_003_009.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[3],label=R'$\mathregular{{C}_{z2500}}$')

dh = loadmat('c_003_011.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[4],label=R'$\mathregular{{N}_{z1500}}$')


rect = matplotlib.patches.Rectangle((0,0.9),50,0.2,color='#e6e6e6')
plt.gca().add_patch(rect)

#plt.legend(bbox_to_anchor=(1.05,0.5), loc=6, borderaxespad=0.,borderpad=1,fontsize=16)

#plt.xlabel('x (km)')
plt.ylabel(R'$\mathregular{q/q_o (-)}$')

plt.xlim([0,50])
plt.xticks([])
plt.ylim([0,3])
plt.yticks([0,1,2,3])
plt.text(47, 2.7, '(b)')

#_____________________________ z = 350m _______________________________

plt.subplot(3,1,3)

dh = loadmat('c_003_001.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[-1],label=R'$\mathregular{{N}_{NP}}$')

dh = loadmat('c_003_002.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{N}_{\theta}}$')

dh = loadmat('c_003_004.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{C}_{z1500}}$')

dh = loadmat('c_003_006.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[1],label=R'$\mathregular{{C}_{z2500}}$')

dh = loadmat('c_003_008.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[2],label=R'$\mathregular{{N}_{z1500}}$')

dh = loadmat('c_003_009.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[3],label=R'$\mathregular{{N}_{z1500}}$')

dh = loadmat('c_003_011.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[4],label=R'$\mathregular{{N}_{z1500}}$')

plt.text(11,0.15,R'$\mathregular{{C}_{NP}}$',color = line_cols[-1],fontsize=20)
plt.text(17,0.15,R'$\mathregular{{C}_{\theta}}$',color = "black",fontsize=20)
plt.text(21,0.15,R'$\mathregular{{C}_{z1500}}$',color = line_cols[0],fontsize=20)
plt.text(25,0.15,R'$\mathregular{{C}_{z2500}}$',color = line_cols[1],fontsize=20)
plt.text(31,0.15,R'$\mathregular{{C}_{z5000}}$',color = line_cols[2],fontsize=20)
plt.text(37,0.15,R'$\mathregular{{C}_{z10000}}$',color = line_cols[3],fontsize=20)
plt.text(43,0.15,R'$\mathregular{{C}_{z15000}}$',color = line_cols[4],fontsize=20)
         

rect = matplotlib.patches.Rectangle((0,0.9),50,0.2,color='#e6e6e6')
plt.gca().add_patch(rect)

#plt.legend(bbox_to_anchor=(1.05,0.5), loc=6, borderaxespad=0.,borderpad=1,fontsize=16)

plt.xlabel('x (km)')
plt.ylabel(R'$\mathregular{q/q_o (-)}$')

plt.xlim([0,50])
plt.ylim([0,3])
plt.yticks([0,1,2,3])
plt.text(47, 2.7, '(c)')

plt.tight_layout()

plt.savefig('../../figure_conv_7.png', dpi=600)

plt.show()


