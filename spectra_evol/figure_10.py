# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('/Users/lauramazzaro/Documents/Work/Perts/Article/Figures/new_cmaps.py')

# Modify plotting parameters!
execfile('/Users/lauramazzaro/Documents/Work/Perts/Article/Figures/new_params.py')

from scipy.io import loadmat
import matplotlib.pyplot as plt
import matplotlib.pyplot
import numpy as np

# Close all open images:
plt.close('all')

# ---------- PLOT ----------

# Create figure handle:
plt.figure(figsize = (16,12))

xs_ind = [1,5,9,13,17,21,25,29,33,37,41,45,49,53,57,61,65,69,73,77,81]

# make colormap:
cols = cmaps['viridis'](np.linspace(0,1,len(xs_ind)))


# -------- theta --------

# Load chosen file: 
dh = loadmat('n_008_001.mat')

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

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    plt.loglog(X,Y,c=cols[i],linewidth=1)

# Plotting stuff:
#plt.xlabel(R'$k_y$ (m$^{-1}$)')
plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
#	plt.ylabel(R'$k_yF_{\theta y}$ (K m s$^{-1}$)')
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

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    plt.loglog(X,Y,c=cols[i],linewidth=1)

# Plotting stuff:
#plt.xlabel(R'$k_y$ (m$^{-1}$)')
#plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
#plt.ylabel(R'$k_yF_{\theta y}$ (K m s$^{-1}$)')
plt.ylabel(R'$k_yF_{wy}$ (m$^2$ s$^{-2}$)')


plt.gca().set_xlim([0.0004,0.1])
plt.xticks([])
# uv
#plt.gca().set_ylim([10**(-11),10**(-4)])
# theta
#plt.gca().set_ylim([10**(-15),10**(-5)])
# w
plt.gca().set_ylim([10**(-11),10**(-5)])
plt.yticks([1e-11,1e-9,1e-7,1e-5])

plt.text(0.08,0.09,'(b)',transform=plt.gca().transAxes)


#        ------- Thetaspect:

# Create axes:
plt.subplot(3,3,7)

u_spect = dh['T_spect_n'][0]

# Ask which height to plot:
print 'Plot 3/9: These are the heights available:'
for h_ind in np.arange(len(zs[0][0])):
    print '[' + str(h_ind + 1) + '] ' + str(zs[0][0][h_ind]) + 'm'
print 'Which one would you like to plot?'
zs_ind = input('> ')-1

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    plt.loglog(X,Y,c=cols[i],linewidth=1)

# Plotting stuff:
plt.xlabel(R'$k_y$ (m$^{-1}$)')
#plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
plt.ylabel(R'$k_yF_{\theta y}$ (K m s$^{-1}$)')
#plt.ylabel(R'$k_yF_{wy}$ (m$^2$ s$^{-2}$)')


plt.gca().set_xlim([0.0004,0.1])
# u-spect:
#plt.gca().set_ylim([10**(-11),10**(-4)])
#theta-spect:
plt.gca().set_ylim([10**(-15),10**(-5)])
# w-spect:
#plt.gca().set_ylim([10**(-11),10**(-5)])
plt.yticks([1e-14,1e-12,1e-10,1e-8,1e-6])

plt.text(0.08,0.09,'(c)',transform=plt.gca().transAxes)

# -------- W-force --------

# Load chosen file: 
dh = loadmat('n_008_005.mat')

# Extract important data:
zs = dh['zs_n'][0]
xs = dh['xs_n'][0]
f_axis = dh['f_axis_n'][0]


#        ------- Uspect:

# Create axes:
plt.subplot(3,3,2)

u_spect = dh['u_spect_n'][0]

# Ask which height to plot:
print 'Plot 9/6: These are the heights available:'
for h_ind in np.arange(len(zs[0][0])):
    print '[' + str(h_ind + 1) + '] ' + str(zs[0][0][h_ind]) + 'm'
print 'Which one would you like to plot?'
zs_ind = input('> ')-1

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    plt.loglog(X,Y,c=cols[i],linewidth=1)

# Plotting stuff:
#plt.xlabel(R'$k_y$ (m$^{-1}$)')
#plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
#plt.ylabel(R'$k_yF_{\theta y}$ (K m s$^{-1}$)')
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

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    plt.loglog(X,Y,c=cols[i],linewidth=1)

# Plotting stuff:
#plt.xlabel(R'$k_y$ (m$^{-1}$)')
#plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
#plt.ylabel(R'$k_yF_{\theta y}$ (K m s$^{-1}$)')
#plt.ylabel(R'$k_yF_{wy}$ (m$^2$ s$^{-2}$)')

plt.gca().set_xlim([0.0004,0.1])
plt.xticks([])
# u
#plt.gca().set_ylim([10**(-11),10**(-4)])
# theta
#plt.gca().set_ylim([10**(-15),10**(-5)])
# w
plt.gca().set_ylim([10**(-11),10**(-5)])
#plt.yticks([1e-11,1e-9,1e-7,1e-5])
plt.yticks([])

plt.text(0.08,0.09,'(e)',transform=plt.gca().transAxes)


#        ------- Thetaspect:

# Create axes:
plt.subplot(3,3,8)

u_spect = dh['T_spect_n'][0]

# Ask which height to plot:
print 'Plot 6/9: These are the heights available:'
for h_ind in np.arange(len(zs[0][0])):
    print '[' + str(h_ind + 1) + '] ' + str(zs[0][0][h_ind]) + 'm'
print 'Which one would you like to plot?'
zs_ind = input('> ')-1

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    plt.loglog(X,Y,c=cols[i],linewidth=1)

# Plotting stuff:
plt.xlabel(R'$k_y$ (m$^{-1}$)')
#plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
#plt.ylabel(R'$k_yF_{\theta y}$ (K m s$^{-1}$)')
#plt.ylabel(R'$k_yF_{wy}$ (m$^2$ s$^{-2}$)')


plt.gca().set_xlim([0.0004,0.1])
# u-spect:
#plt.gca().set_ylim([10**(-11),10**(-4)])
# theta-spect:
plt.gca().set_ylim([10**(-15),10**(-5)])
# w-spect:
#plt.gca().set_ylim([10**(-11),10**(-5)])
#plt.yticks([1e-14,1e-12,1e-10,1e-8,1e-6])

plt.yticks([])
plt.text(0.08,0.09,'(f)',transform=plt.gca().transAxes)

# -------- UV-force --------

# Load chosen file: 
dh = loadmat('n_008_003.mat')

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

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    plt.loglog(X,Y,c=cols[i],linewidth=1)

# Plotting stuff:
#plt.xlabel(R'$k_y$ (m$^{-1}$)')
#plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
#plt.ylabel(R'$k_yF_{\theta y}$ (K m s$^{-1}$)')
#plt.ylabel(R'$k_yF_{wy}$ (m$^2$ s$^{-2}$)')

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

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    plt.loglog(X,Y,c=cols[i],linewidth=1)

# Plotting stuff:
#plt.xlabel(R'$k_y$ (m$^{-1}$)')
#plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
#plt.ylabel(R'$k_yF_{\theta y}$ (K m s$^{-1}$)')
#plt.ylabel(R'$k_yF_{wy}$ (m$^2$ s$^{-2}$)')


plt.gca().set_xlim([0.0004,0.1])
plt.xticks([])
# uv
#plt.gca().set_ylim([10**(-11),10**(-4)])
# theta
#plt.gca().set_ylim([10**(-15),10**(-5)])
# w
plt.gca().set_ylim([10**(-11),10**(-5)])
#plt.yticks([1e-11,1e-9,1e-7,1e-5])
plt.yticks([])

plt.text(0.08,0.09,'(h)',transform=plt.gca().transAxes)


#        ------- Thetaspect:

# Create axes:
plt.subplot(3,3,9)

u_spect = dh['T_spect_n'][0]

# Ask which height to plot:
print 'Plot 9/9: These are the heights available:'
for h_ind in np.arange(len(zs[0][0])):
    print '[' + str(h_ind + 1) + '] ' + str(zs[0][0][h_ind]) + 'm'
print 'Which one would you like to plot?'
zs_ind = input('> ')-1

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    if i == 0:
         plt.loglog(X,Y,c=cols[i],linewidth=1,label=R'x$\approx$1 km')
    elif i == len(xs_ind)-1:
         plt.loglog(X,Y,c=cols[i],linewidth=1,label=R'x$\approx$49.8 km')
    else:
         plt.loglog(X,Y,c=cols[i],linewidth=1)

# Plotting stuff:
plt.xlabel(R'$k_y$ (m$^{-1}$)')
#plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
#plt.ylabel(R'$k_yF_{\theta y}$ (K m s$^{-1}$)')
#plt.ylabel(R'$k_yF_{wy}$ (m$^2$ s$^{-2}$)')
plt.legend(frameon=False,fontsize=18,loc=2)

plt.gca().set_xlim([0.0004,0.1])
# u-spect:
#plt.gca().set_ylim([10**(-11),10**(-4)])
# theta-spect:
plt.gca().set_ylim([10**(-15),10**(-5)])
# w-spect:
#plt.gca().set_ylim([10**(-11),10**(-5)])
#plt.yticks([1e-14,1e-12,1e-10,1e-8,1e-6])
plt.yticks([])


plt.tight_layout()

plt.savefig('../figure_10.png',dpi=600)

plt.show()

