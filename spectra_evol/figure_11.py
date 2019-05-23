# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('../new_cmaps.py')

# Modify plotting parameters!
execfile('../new_params.py')

from scipy.io import loadmat
import matplotlib.pyplot as plt
import matplotlib.pyplot
import numpy as np
import matplotlib.cm

# Close all open images:
plt.close('all')

# ---------- PLOT ----------

# Create figure handle:
plt.figure(figsize = (16,12))

#xs_ind = [1,20,40,60,80,100,120,140,160,180]
xs_ind = [1,5,10,15,20,40,60,80,120,160]
#xs_ind = np.linspace(1,180,180)

# make colormap:
#cols = cmaps['viridis'](np.linspace(0,1,len(xs_ind)))
cols = matplotlib.cm.get_cmap('jet')(np.linspace(0,1,len(xs_ind)))

# -------- v --------

# Load chosen file: 
dh = loadmat('n_009_001_004_100m.mat')

# Extract important data:
zs = dh['zs_n'][0]
xs = dh['xs_n'][0]
f_axis = dh['f_axis_n'][0]


#        ------- Uspect:

# Create axes:
plt.subplot(3,3,1)

u_spect = dh['u_spect_n'][0]

# Ask which height to plot:
print 'Plot 1/9: These are the heights available:'
for h_ind in np.arange(len(zs[0][0])):
    print '[' + str(h_ind + 1) + '] ' + str(zs[0][0][h_ind]) + 'm'
print 'Which one would you like to plot?'
zs_ind = input('> ')-1

# Plot perturbation wavenumber:
plt.loglog([2.6118*10**(-2),2.6118*10**(-2)],[10**(-15),10**(0)], color='#bbc2cc')

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    plt.loglog(X,Y,c=cols[i],linewidth=2)

# Plotting stuff:
#plt.xlabel(R'$k_y$ (m$^{-1}$)')
plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
#	plt.ylabel(R'$k_yF_{v y}$ (K m s$^{-1}$)')
#	plt.ylabel(R'$k_yF_{wy}$ (m$^2$ s$^{-2}$)')

plt.xlim([0.0004,0.1])
plt.xticks([])
plt.ylim([10**(-11),10**(-4)])
plt.yticks([1e-10,1e-8,1e-6,1e-4])

plt.text(0.08,0.09,'(a)',transform=plt.gca().transAxes)

#        ------- Wspect:

# Create axes:
plt.subplot(3,3,4)

u_spect = dh['w_spect_n'][0]

# Ask which height to plot:
print 'Plot 2/9: These are the heights available:'
for h_ind in np.arange(len(zs[0][0])):
    print '[' + str(h_ind + 1) + '] ' + str(zs[0][0][h_ind]) + 'm'
print 'Which one would you like to plot?'
zs_ind = input('> ')-1

# Plot perturbation wavenumber:
plt.loglog([2.6118*10**(-2),2.6118*10**(-2)],[10**(-15),10**(0)], color='#bbc2cc')

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    plt.loglog(X,Y,c=cols[i],linewidth=2)

# Plotting stuff:
#plt.xlabel(R'$k_y$ (m$^{-1}$)')
#plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
#plt.ylabel(R'$k_yF_{v y}$ (K m s$^{-1}$)')
plt.ylabel(R'$k_yF_{wy}$ (m$^2$ s$^{-2}$)')


plt.gca().set_xlim([0.0004,0.1])
plt.xticks([])
# uv
#plt.gca().set_ylim([10**(-11),10**(-4)])
# v
#plt.gca().set_ylim([10**(-15),10**(-5)])
# w
plt.gca().set_ylim([10**(-11),10**(-5)])
plt.yticks([1e-11,1e-9,1e-7,1e-5])

plt.text(0.08,0.09,'(b)',transform=plt.gca().transAxes)


#        ------- vspect:

# Create axes:
plt.subplot(3,3,7)

u_spect = dh['v_spect_n'][0]

# Ask which height to plot:
print 'Plot 3/9: These are the heights available:'
for h_ind in np.arange(len(zs[0][0])):
    print '[' + str(h_ind + 1) + '] ' + str(zs[0][0][h_ind]) + 'm'
print 'Which one would you like to plot?'
zs_ind = input('> ')-1

# Plot perturbation wavenumber:
plt.loglog([2.6118*10**(-2),2.6118*10**(-2)],[10**(-15),10**(0)], color='#bbc2cc')

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    plt.loglog(X,Y,c=cols[i],linewidth=2)

# Plotting stuff:
plt.xlabel(R'$k_y$ (m$^{-1}$)')
#plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
plt.ylabel(R'$k_yF_{v y}$ (m$^2$ s$^{-2}$)')
#plt.ylabel(R'$k_yF_{wy}$ (m$^2$ s$^{-2}$)')

plt.gca().set_xlim([0.0004,0.1])
# u-spect:
#plt.gca().set_ylim([10**(-11),10**(-4)])
#v-spect:
plt.gca().set_ylim([10**(-12),10**(-4)])
# w-spect:
#plt.gca().set_ylim([10**(-11),10**(-5)])
plt.yticks([1e-12,1e-10,1e-8,1e-6,1e-4])

plt.text(0.08,0.09,'(c)',transform=plt.gca().transAxes)

# -------- W-force --------

# Load chosen file: 
dh = loadmat('n_009_006_100m.mat')

# Extract important data:
zs = dh['zs_n'][0]
xs = dh['xs_n'][0]
f_axis = dh['f_axis_n'][0]


#        ------- Uspect:

# Create axes:
plt.subplot(3,3,2)

u_spect = dh['u_spect_n'][0]

# Ask which height to plot:
print 'Plot 4/9: These are the heights available:'
for h_ind in np.arange(len(zs[0][0])):
    print '[' + str(h_ind + 1) + '] ' + str(zs[0][0][h_ind]) + 'm'
print 'Which one would you like to plot?'
zs_ind = input('> ')-1

# Plot perturbation wavenumber:
plt.loglog([2.6118*10**(-2),2.6118*10**(-2)],[10**(-15),10**(0)], color='#bbc2cc')

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    plt.loglog(X,Y,c=cols[i],linewidth=2)

# Plotting stuff:
#plt.xlabel(R'$k_y$ (m$^{-1}$)')
#plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
#plt.ylabel(R'$k_yF_{v y}$ (K m s$^{-1}$)')
#plt.ylabel(R'$k_yF_{wy}$ (m$^2$ s$^{-2}$)')

plt.xlim([0.0004,0.1])
plt.xticks([])
plt.ylim([10**(-11),10**(-4)])
#plt.yticks([1e-10,1e-8,1e-6,1e-4])
plt.yticks([])

plt.text(0.08,0.09,'(d)',transform=plt.gca().transAxes)

#        ------- Wspect:

# Create axes:
plt.subplot(3,3,5)

u_spect = dh['w_spect_n'][0]

# Ask which height to plot:
print 'Plot 5/9: These are the heights available:'
for h_ind in np.arange(len(zs[0][0])):
    print '[' + str(h_ind + 1) + '] ' + str(zs[0][0][h_ind]) + 'm'
print 'Which one would you like to plot?'
zs_ind = input('> ')-1

# Plot perturbation wavenumber:
plt.loglog([2.6118*10**(-2),2.6118*10**(-2)],[10**(-15),10**(0)], color='#bbc2cc')

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    plt.loglog(X,Y,c=cols[i],linewidth=2)

# Plotting stuff:
#plt.xlabel(R'$k_y$ (m$^{-1}$)')
#plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
#plt.ylabel(R'$k_yF_{v y}$ (K m s$^{-1}$)')
#plt.ylabel(R'$k_yF_{wy}$ (m$^2$ s$^{-2}$)')

plt.gca().set_xlim([0.0004,0.1])
plt.xticks([])
# u
#plt.gca().set_ylim([10**(-11),10**(-4)])
# v
#plt.gca().set_ylim([10**(-15),10**(-5)])
# w
plt.gca().set_ylim([10**(-11),10**(-5)])
#plt.yticks([1e-11,1e-9,1e-7,1e-5])
plt.yticks([])

plt.text(0.08,0.09,'(e)',transform=plt.gca().transAxes)


#        ------- vspect:

# Create axes:
plt.subplot(3,3,8)

u_spect = dh['v_spect_n'][0]

# Ask which height to plot:
print 'Plot 6/9: These are the heights available:'
for h_ind in np.arange(len(zs[0][0])):
    print '[' + str(h_ind + 1) + '] ' + str(zs[0][0][h_ind]) + 'm'
print 'Which one would you like to plot?'
zs_ind = input('> ')-1

# Plot perturbation wavenumber:
plt.loglog([2.6118*10**(-2),2.6118*10**(-2)],[10**(-15),10**(0)], color='#bbc2cc')

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    plt.loglog(X,Y,c=cols[i],linewidth=2)

# Plotting stuff:
plt.xlabel(R'$k_y$ (m$^{-1}$)')
#plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
#plt.ylabel(R'$k_yF_{v y}$ (K m s$^{-1}$)')
#plt.ylabel(R'$k_yF_{wy}$ (m$^2$ s$^{-2}$)')


plt.gca().set_xlim([0.0004,0.1])
# u-spect:
#plt.gca().set_ylim([10**(-11),10**(-4)])
# v-spect:
plt.gca().set_ylim([10**(-12),10**(-4)])
# w-spect:
#plt.gca().set_ylim([10**(-11),10**(-5)])
#plt.yticks([1e-14,1e-12,1e-10,1e-8,1e-6])

plt.yticks([])
plt.text(0.08,0.09,'(f)',transform=plt.gca().transAxes)

# -------- UV-force --------

# Load chosen file: 
dh = loadmat('n_010_001_100m.mat')

# Extract important data:
zs = dh['zs_n'][0]
xs = dh['xs_n'][0]
f_axis = dh['f_axis_n'][0]


#        ------- Uspect:

# Create axes:
plt.subplot(3,3,3)

u_spect = dh['u_spect_n'][0]

# Ask which height to plot:
print 'Plot 7/9: These are the heights available:'
for h_ind in np.arange(len(zs[0][0])):
    print '[' + str(h_ind + 1) + '] ' + str(zs[0][0][h_ind]) + 'm'
print 'Which one would you like to plot?'
zs_ind = input('> ')-1

# Plot perturbation wavenumber:
plt.loglog([2.6118*10**(-2),2.6118*10**(-2)],[10**(-15),10**(0)], color='#bbc2cc')

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    plt.loglog(X,Y,c=cols[i],linewidth=2)

# Plotting stuff:
#plt.xlabel(R'$k_y$ (m$^{-1}$)')
#plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
#plt.ylabel(R'$k_yF_{v y}$ (K m s$^{-1}$)')
#plt.ylabel(R'$k_yF_{wy}$ (m$^2$ s$^{-2}$)')

plt.text(0.2,0.5,'250 m',color=cols[0],transform=plt.gca().transAxes,fontsize=18)
plt.text(0.2,0.4,'1250 m',color=cols[1],transform=plt.gca().transAxes,fontsize=18)
plt.text(0.2,0.3,'2500 m',color=cols[2],transform=plt.gca().transAxes,fontsize=18)
plt.text(0.2,0.2,'3750 m',color=cols[3],transform=plt.gca().transAxes,fontsize=18)
plt.text(0.2,0.1,'5000 m',color=cols[4],transform=plt.gca().transAxes,fontsize=18)
plt.text(0.5,0.5,'10000 m',color=cols[5],transform=plt.gca().transAxes,fontsize=18)
plt.text(0.5,0.4,'15000 m',color=cols[6],transform=plt.gca().transAxes,fontsize=18)
plt.text(0.5,0.3,'20000 m',color=cols[7],transform=plt.gca().transAxes,fontsize=18)
plt.text(0.5,0.2,'30000 m',color=cols[8],transform=plt.gca().transAxes,fontsize=18)
plt.text(0.5,0.1,'40000 m',color=cols[9],transform=plt.gca().transAxes,fontsize=18)

plt.xlim([0.0004,0.1])
plt.xticks([])
plt.ylim([10**(-11),10**(-4)])
#plt.yticks([1e-10,1e-8,1e-6,1e-4])
plt.yticks([])

plt.text(0.08,0.09,'(g)',transform=plt.gca().transAxes)

#        ------- Wspect:

# Create axes:
plt.subplot(3,3,6)

u_spect = dh['w_spect_n'][0]

# Ask which height to plot:
print 'Plot 8/9: These are the heights available:'
for h_ind in np.arange(len(zs[0][0])):
    print '[' + str(h_ind + 1) + '] ' + str(zs[0][0][h_ind]) + 'm'
print 'Which one would you like to plot?'
zs_ind = input('> ')-1

# Plot perturbation wavenumber:
plt.loglog([2.6118*10**(-2),2.6118*10**(-2)],[10**(-15),10**(0)], color='#bbc2cc')

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    plt.loglog(X,Y,c=cols[i],linewidth=2)

# Plotting stuff:
#plt.xlabel(R'$k_y$ (m$^{-1}$)')
#plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
#plt.ylabel(R'$k_yF_{v y}$ (K m s$^{-1}$)')
#plt.ylabel(R'$k_yF_{wy}$ (m$^2$ s$^{-2}$)')


plt.gca().set_xlim([0.0004,0.1])
plt.xticks([])
# uv
#plt.gca().set_ylim([10**(-11),10**(-4)])
# v
#plt.gca().set_ylim([10**(-15),10**(-5)])
# w
plt.gca().set_ylim([10**(-11),10**(-5)])
#plt.yticks([1e-11,1e-9,1e-7,1e-5])
plt.yticks([])

plt.text(0.08,0.09,'(h)',transform=plt.gca().transAxes)


#        ------- vspect:

# Create axes:
plt.subplot(3,3,9)

u_spect = dh['v_spect_n'][0]

# Ask which height to plot:
print 'Plot 9/9: These are the heights available:'
for h_ind in np.arange(len(zs[0][0])):
    print '[' + str(h_ind + 1) + '] ' + str(zs[0][0][h_ind]) + 'm'
print 'Which one would you like to plot?'
zs_ind = input('> ')-1

# Plot perturbation wavenumber:
plt.loglog([2.6118*10**(-2),2.6118*10**(-2)],[10**(-15),10**(0)], color='#bbc2cc')

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    if i == 0:
         plt.loglog(X,Y,c=cols[i],linewidth=2,label=R'x$\approx$1 km')
    elif i == len(xs_ind)-1:
         plt.loglog(X,Y,c=cols[i],linewidth=2,label=R'x$\approx$49.8 km')
    else:
         plt.loglog(X,Y,c=cols[i],linewidth=2)

# Plotting stuff:
plt.xlabel(R'$k_y$ (m$^{-1}$)')
#plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
#plt.ylabel(R'$k_yF_{v y}$ (K m s$^{-1}$)')
#plt.ylabel(R'$k_yF_{wy}$ (m$^2$ s$^{-2}$)')
#plt.legend(frameon=False,fontsize=18,loc=2)

plt.gca().set_xlim([0.0004,0.1])
# u-spect:
#plt.gca().set_ylim([10**(-11),10**(-4)])
# v-spect:
plt.gca().set_ylim([10**(-12),10**(-4)])
# w-spect:
#plt.gca().set_ylim([10**(-11),10**(-5)])
#plt.yticks([1e-14,1e-12,1e-10,1e-8,1e-6])
plt.yticks([])

plt.text(0.08,0.09,'(i)',transform=plt.gca().transAxes)

plt.tight_layout()

plt.savefig('../figure_11.png',dpi=600)

plt.show()

