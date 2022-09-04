import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Setting up the duration for animation
t0 = 0 # Starting time (Hours)
t_end = 1 # Ending time (Hours)
dt = 0.005 # increment value for time

# Creating time array
t = np.arange(t0,t_end + dt, dt)

# Parameters
r1 = 4
f1 = 2*np.pi
alpha1 = f1*t
x1 = r1*np.cos(alpha1)
y1 = r1*np.sin(alpha1)   

r2 = 3
f2 = 4*np.pi
alpha2 = (f1+f2)*t
dx1 = r2*np.cos(alpha2)
dy1 = r2*np.sin(alpha2)
x2 = x1+dx1
y2 = y1+dy1

r3 = 2
f3 = 8*np.pi
alpha3 = (f1+f2+f3)*t
dx2 = r3*np.cos(alpha3)
dy2 = r3*np.sin(alpha3)
x3 = x2+dx2
y3 = y2+dy2

#####################Animation#########################

frame_amount = len(t)


def update_plot(num):

    line_1.set_data([0,x1[num]],[0,y1[num]])
    line_2.set_data([x1[num],x2[num]],[y1[num],y2[num]])
    line_3.set_data([x2[num],x3[num]],[y2[num],y3[num]])
    trajectory.set_data(x3[0:num],y3[0:num])

    alpha1_line.set_data(t[0:num],alpha1[0:num])
    alpha2_line.set_data(t[0:num],alpha2[0:num])
    alpha3_line.set_data(t[0:num],alpha3[0:num])

    return line_1,line_2,line_3,trajectory,\
    alpha1_line,alpha2_line,alpha3_line

fig = plt.figure(figsize=(16,9), dpi=80, facecolor=(0.8,0.8,0.8))
plt.subplots_adjust(left=0.05,right=0.95,top=0.95,bottom=0.05)
gs = gridspec.GridSpec(3,3)

# Subplot 01
ax0 = fig.add_subplot(gs[:,0:2], facecolor=(0.9,0.9,0.9))

# Draw Robot
base_line, = ax0.plot([0,0],[-0.2,0.2],'k',linewidth=20,alpha=0.5)
line_1, = ax0.plot([],[],'b',linewidth=4)
line_2, = ax0.plot([],[],'r',linewidth=4)
line_3, = ax0.plot([],[],'purple',linewidth=4)
trajectory, = ax0.plot([],[],'--k',linewidth=2)


# Subplot properties
ax0.set_xlim(-10,10)
ax0.set_ylim(-10,10)
ax0.set_xlabel('meters [m]',fontsize=12)
ax0.set_ylabel('meters [m]', fontsize=12)
plt.title("Robotic Arm", size=12)
plt.grid(True)
ax0.spines['left'].set_position('center')
ax0.spines['bottom'].set_position('center')
ax0.xaxis.set_label_coords(0.5,-0.01)
ax0.yaxis.set_label_coords(-0.02,0.5)

# Subplot 02
ax1 = fig.add_subplot(gs[0,2], facecolor=(0.9,0.9,0.9))
alpha1_line, = ax1.plot([],[],'b',linewidth=3)

# Subplot properties
plt.ylabel("angle [rad]", size=10)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(0,6*np.pi)
plt.yticks(np.arange(0,6*np.pi+0.1,np.pi),['0','π','2π','3π','4π','5π','6π'])

# Subplot 03
ax2 = fig.add_subplot(gs[1,2], facecolor=(0.9,0.9,0.9))
alpha2_line, = ax2.plot([],[],'b',linewidth=3)

# Subplot properties
plt.ylabel("angle [rad]", size=10)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(0,6*np.pi)
plt.yticks(np.arange(0,6*np.pi+0.1,np.pi),['0','π','2π','3π','4π','5π','6π'])

# Subplot 04
ax3 = fig.add_subplot(gs[2,2], facecolor=(0.9,0.9,0.9))
alpha3_line, = ax3.plot([],[],'b',linewidth=3)

# Subplot properties
plt.xlabel("time [s]", size=10)
plt.ylabel("angle [rad]", size=10)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(0,6*np.pi)
plt.yticks(np.arange(0,6*np.pi+0.1,np.pi),['0','π','2π','3π','4π','5π','6π'])

plane_ani = animation.FuncAnimation(fig, update_plot,
    frames=frame_amount, interval=1, repeat=False, blit=True)
plt.show()