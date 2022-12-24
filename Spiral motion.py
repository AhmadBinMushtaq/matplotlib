import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Setting up the duration for animation
t0 = 0 # Starting time (Hours)
t_end = 10 # Ending time (Hours)
dt = 0.02 # increment value for time

# Creating time array
t = np.arange(t0,t_end + dt, dt)

# Setting up X & Y arrays
f1=2*np.pi
r1=3
phi1=f1*t
x=r1*np.cos(phi1)
y=r1*np.sin(phi1)
z=t



#####################Animation#########################

frame_amount = len(t)


def update_plot(num):

    plane_trajectory.set_data(x[0:num],y[0:num])
    plane_trajectory.set_3d_properties(z[0:num])

    x_dist.set_data(t[0:num],x[0:num])
    y_dist.set_data(t[0:num],y[0:num])
    z_dist.set_data(t[0:num],z[0:num])

    return plane_trajectory, x_dist, y_dist, z_dist

fig = plt.figure(figsize=(16,9), dpi=80, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(3,4)

# Subplot 01
ax0 = fig.add_subplot(gs[:,0:3], projection='3d', facecolor=(0.9,0.9,0.9))

# Draw trajectory
plane_trajectory, = ax0.plot([],[],[],'k',linewidth=3)

# Subplot properties
ax0.set_xlim(min(x),max(x))
ax0.set_ylim(min(y),max(y))
ax0.set_zlim(min(z),max(z))
ax0.set_xlabel('Position X [m]',fontsize=12)
ax0.set_ylabel('Position Y [m]', fontsize=12)
ax0.set_zlabel('Position Z [m]', fontsize=12)
plt.title("Airplane Projection", size=12)
plt.grid(True)
plt.legend(loc='upper left',fontsize='large')

# Subplot 02
ax1 = fig.add_subplot(gs[0,3], facecolor=(0.9,0.9,0.9))
x_dist, = ax1.plot([],[],'b',linewidth=3)

# Subplot properties
plt.ylabel("Position X [m]", size=10)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(np.min(x),np.max(x)*3/2)
plt.legend(loc='upper left', fontsize='medium')

# Subplot 03
ax2 = fig.add_subplot(gs[1,3], facecolor=(0.9,0.9,0.9))
y_dist, = ax2.plot([],[],'b',linewidth=3)

# Subplot properties
plt.ylabel("Position Y [m]", size=10)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(np.min(y),np.max(y)*3/2)
plt.legend(loc='upper left', fontsize='medium')

# Subplot 04
ax3 = fig.add_subplot(gs[2,3], facecolor=(0.9,0.9,0.9))
z_dist, = ax3.plot([],[],'b',linewidth=3,label='Z=t')

# Subplot properties
plt.xlabel("Time [sec]", size=10)
plt.ylabel("Position Z [m]", size=10)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(np.min(z),np.max(z)*3/2)
plt.legend(loc='upper left', fontsize='medium')

plane_ani = animation.FuncAnimation(fig, update_plot,
    frames=frame_amount, interval=5, repeat=True, blit=True)
plt.show()