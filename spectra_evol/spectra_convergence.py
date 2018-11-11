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

# Ask which component spectra to plot:
print 'Which spectra component are you interested in plotting? (u = 1 ; T = 2 ; w = 3)'
comp = input('> ')

# Ask which component spectra to plot:
print 'Plot neutral or convective? (neutral = 1 ; convective = 2)'
stab = input('> ')
# -----------------------

# Close all open images:
plt.close('all')

# Find list of available '*mat' files:
if stab == 1:
     file_list = glob.glob('n*.mat')
elif stab == 2:
     file_list = glob.glob('c*.mat')

# If there is more than one file available:
if len(file_list) > 1:

	# Show list of files:
	print('These are the available files:\n')
	for i in np.arange(len(file_list)):
		print('[' + str(i + 1) + '] ' + file_list[i] + '\n')

	# Ask which file to plot:
	print('Which file would you like to plot?')
	file_name = file_list[input('> ') - 1]

# If there is only one file available:
else:
	file_name = file_list[0]

# Load chosen file: 
dh = loadmat(file_name)

# Extract data to create -5/3 and -1 slope lines:
x_ref = dh['x_ref'][0]
y_neg23 = dh['y_neg23'][0]*10**(-2)
y_0 = dh['y_0'][0]*10**(-2)

# ---------- PLOT ----------

# Create figure handle:
fh = plt.figure(figsize = (8,6))

# Create axes:
ax = fh.add_subplot(111)

# ----- Plot Reference Lines:

#plt.loglog(x_ref,y_neg23,'k-')
#ax.text(x_ref[1],y_neg23[2]+0.5*10**(-4),'-2/3')
#plt.loglog(x_ref,y_0,'k-')
#ax.text(x_ref[1],y_0[2]+0.5*10**(-3),'0')

# ----- Nested domain lines:

# Extract important data:
zs = dh['zs_n'][0]
xs = dh['xs_n'][0]
f_axis = dh['f_axis_n'][0]
if comp == 1:
	u_spect = dh['u_spect_n'][0]
elif comp == 2:
	u_spect = dh['T_spect_n'][0]
elif comp == 3:
	u_spect = dh['w_spect_n'][0]

# Ask which height to plot:
print 'These are the heights available:'
for h_ind in np.arange(len(zs[0][0])):
    print '[' + str(h_ind + 1) + '] ' + str(zs[0][0][h_ind]) + 'm'
print 'Which one would you like to plot?'
zs_ind = input('> ')-1

# Ask which x-location to plot:
#print 'These are the x-locations available:'
#for x_ind in np.arange(len(xs[0][0])):
#	print '[' + str(x_ind + 1) + '] ' + str(xs[0][0][x_ind]) + 'm' 
#print 'Which ones would you like to plot? (e.g. "1,2,3,4")'
#xs_ind = raw_input('> ') 
#xs_ind = [np.int(xs_ind.split(',')[i]) for i in np.arange(len(xs_ind.split(',')))]

xs_ind = [1,5,9,13,17,21,25,29,33,37,41,45,49,53,57,61,65,69,73,77,81]

# make colormap:
cols = cmaps['viridis'](np.linspace(0,1,len(xs_ind)))

# For each x:
for i in np.arange(len(xs_ind)):
    X = np.squeeze(f_axis[0])
    Y = np.squeeze(f_axis[0]*u_spect[0][0,xs_ind[i]][0,zs_ind])
    plt.loglog(X,Y,c=cols[i],linewidth=1)

# Plotting stuff:
plt.xlabel(R'$k_y$ (m$^{-1}$)')
if comp == 1:
	plt.ylabel(R'$k_yF_{uy}$ (m$^2$ s$^{-2}$)')
elif comp == 2:
	plt.ylabel(R'$k_yF_{\theta y}$ (K m s$^{-1}$)')
else:
	plt.ylabel(R'$k_yF_{wy}$ (m$^2$ s$^{-2}$)')


if stab == 1:
     plt.gca().set_xlim([0.0004,0.1])
     if zs[0][0][zs_ind] == 100:
        if comp == 1:
           plt.gca().set_ylim([10**(-10),10**(-4)])
        elif comp == 2:
           plt.gca().set_ylim([10**(-15),10**(-5)])
        elif comp == 3:
           plt.gca().set_ylim([10**(-11),10**(-5)])
     elif zs[0][0][zs_ind] == 250:
        if comp == 1:
           plt.gca().set_ylim([10**(-11),10**(-4)])
        elif comp == 2:
           plt.gca().set_ylim([10**(-15),10**(-5)])
        elif comp == 3:
           plt.gca().set_ylim([10**(-11),10**(-5)])
     elif zs[0][0][zs_ind] == 350:
        if comp == 1:
           plt.gca().set_ylim([10**(-12),10**(-4)])
        elif comp == 2:
           plt.gca().set_ylim([10**(-15),10**(-6)])
        elif comp == 3:
           plt.gca().set_ylim([10**(-11),10**(-5)])
elif stab == 2:
     plt.gca().set_xlim([0.0004,0.065])
     if zs[0][0][zs_ind] == 100:
        if comp == 1:
           plt.gca().set_ylim([10**(-9),10**(-4)])
        elif comp == 2:
           plt.gca().set_ylim([10**(-11),10**(-5)])
        elif comp == 3:
           plt.gca().set_ylim([10**(-11),10**(-4)])
     elif zs[0][0][zs_ind] == 500:
        if comp == 1:
           plt.gca().set_ylim([10**(-10),10**(-4)])
        elif comp == 2:
           plt.gca().set_ylim([10**(-12),10**(-5)])
        elif comp == 3:
           plt.gca().set_ylim([10**(-10),10**(-3)])
     elif zs[0][0][zs_ind] == 1000:
        if comp == 1:
           plt.gca().set_ylim([10**(-10),10**(-4)])
        elif comp == 2:
           plt.gca().set_ylim([10**(-12),10**(-5)])
        elif comp == 3:
           plt.gca().set_ylim([10**(-9),10**(-3)])
     elif zs[0][0][zs_ind] == 1500:
        if comp == 1:
           plt.gca().set_ylim([10**(-9),10**(-4)])
        elif comp == 2:
           plt.gca().set_ylim([10**(-12),10**(-6)])
        elif comp == 3:
           plt.gca().set_ylim([10**(-10),10**(-4)])

plt.tight_layout()
plt.show()

