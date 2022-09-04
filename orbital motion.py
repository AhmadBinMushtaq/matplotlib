import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Setting up the duration for animation
t0 = 0 # Starting time (Hours)
t_end = 10 # Ending time (Hours)
dt = 0.01 # increment value for time

# Creating time array
t = np.arange(t0,t_end + dt, dt)

# Setting up orbit arrays
f1=2*np.pi
r1=3
alpha1=0
phi1=f1*t
x1=r1*np.sin(phi1)*np.cos(alpha1)
y1=r1*np.sin(phi1)*np.sin(alpha1)
z1=r1*np.cos(phi1)

f2=2*np.pi
r2=3
alpha2=np.pi/2
phi2=f2*t
x2=r2*np.sin(phi2)*np.cos(alpha2)
y2=r2*np.sin(phi2)*np.sin(alpha2)
z2=r2*np.cos(phi2)

f3=2*np.pi
r3=3
alpha3=f3*t
phi3=np.pi/2
x3=r3*np.sin(phi3)*np.cos(alpha3)
y3=r3*np.sin(phi3)*np.sin(alpha3)
z3=np.ones(len(t))*r3*np.cos(phi3)

#####################Animation#########################

frame_amount = len(t)


def update_plot(num):
    if num<1/dt:
        red_line.set_data(x1[0:num],y1[0:num])
        red_line.set_3d_properties(z1[0:num])

        green_line.set_data(x2[0:num],y2[0:num])
        green_line.set_3d_properties(z2[0:num])

        blue_line.set_data(x3[0:num],y3[0:num])
        blue_line.set_3d_properties(z3[0:num])
    else:
        red_line.set_data(x1[int(num-1/dt+2):num],y1[int(num-1/dt+2):num])
        red_line.set_3d_properties(z1[int(num-1/dt+2):num])

        green_line.set_data(x2[int(num-1/dt+2):num],y2[int(num-1/dt+2):num])
        green_line.set_3d_properties(z2[int(num-1/dt+2):num])

        blue_line.set_data(x3[int(num-1/dt+2):num],y3[int(num-1/dt+2):num])
        blue_line.set_3d_properties(z3[int(num-1/dt+2):num])

    return red_line,green_line,blue_line

fig = plt.figure(figsize=(16,9), dpi=80, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(1,1)

# Subplot 01
ax0 = fig.add_subplot(gs[0,0], projection='3d', facecolor=(0.9,0.9,0.9))

# Draw trajectory
red_line, = ax0.plot([],[],[],'r',linewidth=3)
green_line, = ax0.plot([],[],[],'g',linewidth=3)
blue_line, = ax0.plot([],[],[],'b',linewidth=3)

w_red_line, = ax0.plot([],[],[],'w',linewidth=5)
w_green_line, = ax0.plot([],[],[],'w',linewidth=5)
w_blue_line, = ax0.plot([],[],[],'w',linewidth=5)

# Subplot properties
ax0.set_xlim(min(np.min(x1),np.min(x2),np.min(x3)),max(np.max(x1),np.max(x2),np.max(x3)))
ax0.set_ylim(min(np.min(y1),np.min(y2),np.min(y3)),max(np.max(y1),np.max(y2),np.max(y3)))
ax0.set_zlim(min(np.min(z1),np.min(z2),np.min(z3)),max(np.max(z1),np.max(z2),np.max(z3)))
ax0.set_xlabel('Position X [m]',fontsize=12)
ax0.set_ylabel('Position Y [m]', fontsize=12)
ax0.set_zlabel('Position Z [m]', fontsize=12)
plt.title("Orbits", size=12)
plt.grid(True)

plane_ani = animation.FuncAnimation(fig, update_plot,
    frames=frame_amount, interval=5, repeat=True, blit=True)
plt.show()