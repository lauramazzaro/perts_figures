# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('/Users/lauramazzaro/Documents/Work/Perts/Article/Figures/new_cmaps.py')

# Modify plotting parameters!
execfile('/Users/lauramazzaro/Documents/Work/Perts/Article/Figures/new_params.py')

from scipy.io import loadmat
import matplotlib.pyplot as plt
import matplotlib.pyplot
import numpy as np
import glob

# -------- INPUT --------

line_cols = [line_cols[0],line_cols[1],line_cols[7],line_cols[5],line_cols[8],line_cols[2],line_cols[7],line_cols[3],line_cols[6]]

# Ask which component spectra to plot:
#print 'Which spectra component are you interested in plotting? (u = 1 ; T = 2 ; w = 3)'
#comp = input('> ')

# Ask which component spectra to plot:
#print 'Plot neutral or convective? (neutral = 1 ; convective = 2)'
#stab = input('> ')
# -----------------------

# Close all open images:
plt.close('all')

# Find list of available '*mat' files:
file_list = ['n_008_001.mat','n_008_003.mat','n_008_005.mat']#,'n_008_009.mat','n_008_010.mat','n_008_008.mat']

# ---------- PLOT ----------

# Create figure handle:
fh = plt.figure(figsize = (20,5))

# ----- u:

# Create axes:
ax = fh.add_subplot(131)

# x-location to plot:
xs_ind = 161

# For each file:
for i in np.arange(len(file_list)):

     dh = loadmat(file_list[i])

     # Extract important data:
     zs = dh['zs_n'][0]
     f_axis = dh['f_axis_n'][0]
     u_spect = dh['u_spect_n'][0]

     # Ask which height to plot:
     print 'These are the heights available for file "' + file_list[i] + '":'
     for h_ind in np.arange(len(zs[0][0])):
         print '[' + str(h_ind + 1) + '] ' + str(zs[0][0][h_ind]) + 'm'
     print 'Which one would you like to plot?'
     zs_ind = input('> ')-1

     X = np.squeeze(f_axis[0])
     Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind][0,zs_ind])
     plt.loglog(X,Y,c=line_cols[i],label=file_list[i])

# Plotting stuff:
plt.xlabel(R'$k_y$ (m$^{-1}$)')
plt.yticks([1e-10,1e-8,1e-6,1e-4])
plt.ylabel(R'$\mathregular{k_yF_{uy} (m^2 s^{-2}}$)')
plt.gca().set_xlim([0.0004,0.1])
plt.text(0.08,0.09,'(a)',transform=plt.gca().transAxes)

# ----- w:

# Create axes:
ax = fh.add_subplot(132)

# x-location to plot:
xs_ind = 161

# For each file:
for i in np.arange(len(file_list)):

     dh = loadmat(file_list[i])

     # Extract important data:
     zs = dh['zs_n'][0]
     f_axis = dh['f_axis_n'][0]
     u_spect = dh['w_spect_n'][0]

     # Ask which height to plot:
     print 'These are the heights available for file "' + file_list[i] + '":'
     for h_ind in np.arange(len(zs[0][0])):
         print '[' + str(h_ind + 1) + '] ' + str(zs[0][0][h_ind]) + 'm'
     print 'Which one would you like to plot?'
     zs_ind = input('> ')-1

     X = np.squeeze(f_axis[0])
     Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind][0,zs_ind])
     plt.loglog(X,Y,c=line_cols[i],label=file_list[i])

# Plotting stuff:
plt.xlabel(R'$k_y$ (m$^{-1}$)')
plt.ylabel(R'$\mathregular{k_yF_{wy} (m^2 s^{-2}}$)')
plt.yticks([1e-10,1e-8,1e-6])
plt.gca().set_xlim([0.0004,0.1])
plt.text(0.08,0.09,'(b)',transform=plt.gca().transAxes)

# ----- theta:

# Create axes:
ax = fh.add_subplot(133)

# x-location to plot:
xs_ind = 161

# For each file:
for i in np.arange(len(file_list)):

     dh = loadmat(file_list[i])

     # Extract important data:
     zs = dh['zs_n'][0]
     f_axis = dh['f_axis_n'][0]
     u_spect = dh['T_spect_n'][0]

     # Ask which height to plot:
     print 'These are the heights available for file "' + file_list[i] + '":'
     for h_ind in np.arange(len(zs[0][0])):
         print '[' + str(h_ind + 1) + '] ' + str(zs[0][0][h_ind]) + 'm'
     print 'Which one would you like to plot?'
     zs_ind = input('> ')-1

     X = np.squeeze(f_axis[0])
     Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind][0,zs_ind])
     plt.loglog(X,Y,c=line_cols[i],label=file_list[i])

# Plotting stuff:
plt.xlabel(R'$k_y$ (m$^{-1}$)')
plt.ylabel(R'$\mathregular{k_yF_{\theta y} (K m s ^{-1}}$)')
plt.yticks([1e-14,1e-12,1e-10,1e-8])
plt.gca().set_xlim([0.0004,0.1])
plt.text(0.08,0.09,'(c)',transform=plt.gca().transAxes)


plt.tight_layout()
plt.show()


