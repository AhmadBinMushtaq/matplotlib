import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

type = 3

# Setting up the duration for animation
t0 = 0 # Starting time (Hours)
t_end = 10 # Ending time (Hours)
dt = 0.02 # increment value for time

# Creating time array
t = np.arange(t0,t_end + dt, dt)
if type == 1:
    # Creating x - axis array
    x_i = 1000
    v_x = 200
    x = x_i+v_x*t
    # Creating y - axis array
    y_i = 1500
    v_y = 100
    y = y_i-v_y*t
elif type == 2:
    # Creating x - axis array
    x_i = 1000
    v_x = 200
    x = x_i+v_x*t
    # Creating y - axis array
    y_i = 1000
    A_y = 500
    w_y = 0.2*np.pi
    y = y_i + A_y*np.sin(w_y*t)
else:
    r=200
    f=0.4*np.pi
    x_i=1000
    y_i=500
    x=x_i+r*np.cos(f*t)+50*t
    y=y_i+r*np.sin(f*t)+50*t


#####################Animation#########################

frame_amount = len(t)


def update_plot(num):

    plane_1.set_data([x[num]-40,x[num]+20],[y[num],y[num]])
    plane_2.set_data([x[num]-15,x[num]+10],[y[num],y[num]])
    plane_3.set_data([x[num]-45,x[num]-30],[y[num]+80,y[num]])
    plane_4.set_data([x[num]-55,x[num]-40],[y[num],y[num]])

    plane_trajectory.set_data(x[0:num],y[0:num])

    pos_arrow_f = ax0.arrow(0,0,x[num],y[num],length_includes_head=True,head_width=80,head_length=80,color='b',linewidth=2)
    displacement_arrow = ax0.arrow(x_i,y_i,x[num]-x_i-50,y[num]-y_i,length_includes_head=True,head_width=60,head_length=60,color='purple',linewidth=2)
    displacement_arrow_x = ax0.arrow(x_i,y_i,x[num]-x_i,0,length_includes_head=True,head_width=60,head_length=60,color='g',linewidth=2)
    displacement_arrow_y = ax0.arrow(x[num],y_i,0,y[num]-y_i+50,length_includes_head=True,head_width=60,head_length=60,color='r',linewidth=2)



    x_dist.set_data(t[0:num],x[0:num])
    y_dist.set_data(t[0:num],y[0:num])

    x_arrow = ax1.arrow(t[num],x_i,0,x[num]-x_i,length_includes_head=True,head_width=0.4,head_length=200,color='g',linewidth=2)
    y_arrow = ax2.arrow(t[num],y_i,0,y[num]-y_i,length_includes_head=True,head_width=0.4,head_length=200,color='r',linewidth=2)

    return plane_1,plane_2,plane_3,plane_4,plane_trajectory,\
    x_dist,y_dist,pos_arrow_f,displacement_arrow,\
    displacement_arrow_x,displacement_arrow_y,\
    x_arrow,y_arrow

fig = plt.figure(figsize=(16,9), dpi=80, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,2)

# Subplot 01
ax0 = fig.add_subplot(gs[0,:], facecolor=(0.9,0.9,0.9))

# Draw airplane
plane_1, = ax0.plot([],[],'k',linewidth=10)
plane_2, = ax0.plot([],[],'w',linewidth=5)
plane_3, = ax0.plot([],[],'k',linewidth=4)
plane_4, = ax0.plot([],[],'w',linewidth=3)

plane_trajectory ,= ax0.plot([],[],'--k',linewidth=2)

pos_arrow_i = ax0.arrow(0,0,x_i,y_i,length_includes_head=True,head_width=80,head_length=80,color='k',linewidth=2)

# Subplot properties
plt.xlabel("Horizontal Distance [m]", size=10)
plt.ylabel("Vertical Elevation [m]", size=10)
plt.title("Airplane Projection", size=12)
plt.grid(True)
plt.xlim(0,np.max(x))
plt.ylim(0,np.max(y)+100)

# Subplot 02
ax1 = fig.add_subplot(gs[1,0], facecolor=(0.9,0.9,0.9))
x_dist, = ax1.plot([],[],'-b',linewidth=3)

plt.xlabel("Time [sec]", size=10)
plt.ylabel("Horizontal Distance [m]", size=10)
plt.title("X-Axis", size=12)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(0,np.max(x)*3/2)
plt.legend(loc='upper left', fontsize='medium')

# Subplot 03
ax2 = fig.add_subplot(gs[1,1], facecolor=(0.9,0.9,0.9))
y_dist, = ax2.plot([],[],'-b',linewidth=3)

plt.xlabel("Time [sec]", size=10)
plt.ylabel("Vertical Elevation [m]", size=10)
plt.title("Y-Axis", size=12)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(0,np.max(y)*3/2)
plt.legend(loc='upper left', fontsize='medium')

plane_ani = animation.FuncAnimation(fig, update_plot,
    frames=frame_amount, interval=5, repeat=True, blit=True)
plt.show()