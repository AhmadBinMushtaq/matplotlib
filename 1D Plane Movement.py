import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Setting up the duration for animation
t0 = 0 # Starting time (Hours)
t_end = 2 # Ending time (Hours)
dt = 0.005 # increment value for time

# Creating time array
t = np.arange(t0,t_end + dt, dt)

# Creating x - axis array
x = 100*t**4


# Creating x - axis speed
x_speed = np.zeros(len(t))
for i in range(1,len(t)):
    x_speed[i] = (x[i]-x[i-1])/dt

# Creating y - axis array
altitude = 2 # Altitude is constant for whole flight
y = np.ones(len(t))*altitude

#####################Animation#########################

frame_amount = len(t)
dot = np.zeros(frame_amount)
n = 20
for i in range(0,frame_amount):
    if(i==n):
        dot[i]=x[n]
        n+=20
    else:
        dot[i]=x[n-20]


def update_plot(num):

    # Subplot 1
    horizontal_line.set_data(dot[0:num],y[0:num])
    vertical_line.set_data([x[num],x[num]],[0,y[num]])
    plane_1.set_data((x[num]-50,x[num]+50),(y[num],y[num]))
    plane_2.set_data((x[num],x[num]+20),(y[num]-0.5,y[num]))
    plane_3.set_data((x[num],x[num]+20),(y[num]+0.5,y[num]))
    plane_4.set_data((x[num]-50,x[num]-35),(y[num]-0.2,y[num]))
    plane_5.set_data((x[num]-50,x[num]-35),(y[num]+0.2,y[num]))
    stopwatch.set_text(str(round(t[num],1)) + " hrs")
    distance_counter.set_text(str(int(x[num])) + " km")

    # Subplot 2
    x_dist_2.set_data(t[0:num],x[0:num])
    horizontal_line_2.set_data([t[0],t[num]],[x[num],x[num]])
    vertical_line_2.set_data([t[num],t[num]],[x[0],x[num]])

    # Subplot 3
    speed_line.set_data(t[0:num],x_speed[0:num])
    horizontal_line_3.set_data([t[0],t[num]],[x_speed[num],x_speed[num]])
    vertical_line_3.set_data([t[num],t[num]],[x_speed[0],x_speed[num]])


    return horizontal_line,vertical_line,plane_1,plane_2,plane_3,plane_4,plane_5,\
    stopwatch,distance_counter,x_dist_2,horizontal_line_2,vertical_line_2,\
    speed_line,horizontal_line_3,vertical_line_3

fig = plt.figure(figsize=(16,9), dpi=80, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,2)

# Subplot 01
ax0 = fig.add_subplot(gs[0,:], facecolor=(0.9,0.9,0.9))

# Draw plane trajectory
horizontal_line, = ax0.plot([],[],'r:o', linewidth=2)
vertical_line, = ax0.plot([],[],'k:o',linewidth=2)

# Insert stopwatch & distance text
circle = dict(boxstyle='circle', fc=(0.7,0.7,0.7), ec='r', lw=2)
square = dict(boxstyle="square", fc=(0.7,0.7,0.7), ec = 'g', lw=2)
distance_counter = ax0.text(1400,0.4,"", size=12, color='r', bbox=square)
stopwatch = ax0.text(1400,1,"", size=12, color='g', bbox=square)

# Draw airplane
plane_1, = ax0.plot([],[],'k',linewidth=5)
plane_2, = ax0.plot([],[],'k',linewidth=5)
plane_3, = ax0.plot([],[],'k',linewidth=5)
plane_4, = ax0.plot([],[],'k',linewidth=5)
plane_5, = ax0.plot([],[],'k',linewidth=5)

# Subplot properties
plt.xticks(np.arange(x[0],x[-1]+1,(x[-1]-x[0])/4),size=8)
plt.yticks(np.arange(0,4,1),size=8)
plt.xlabel("Horizontal Distance [km]", size=10)
plt.ylabel("Vertical Elevation [km]", size=10)
plt.title("Airplane Projection", size=12)
plt.grid(True)
plt.xlim(x[0],x[-1])
plt.ylim(0,y[0]*3/2)


# Subplot 02
ax1 = fig.add_subplot(gs[1,0], facecolor=(0.9,0.9,0.9))
x_dist_2, = ax1.plot([],[],'-b',linewidth=3,label='X=800*t')
horizontal_line_2, = ax1.plot([],[],'r:o',linewidth=2,label='horizontal line')
vertical_line_2, = ax1.plot([],[],'g:o',linewidth=2,label='vertical line')

plt.xticks(np.arange(t[0],t[-1]+0.5,(t[-1]-t[0])/4),size=8)
plt.yticks(np.arange(x[0],x[-1]*3/2,(x[-1]-x[0])/4), size=8)
plt.xlabel("Time [sec]", size=10)
plt.ylabel("Distance [km]", size=10)
plt.title("Distance vs Time", size=12)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(x[0],x[-1]*3/2)
plt.legend(loc='upper left', fontsize='medium')

# Subplot 03
ax2 = fig.add_subplot(gs[1,1], facecolor=(0.9,0.9,0.9))
speed_line, = ax2.plot([],[],'b',linewidth=3,label='dx/dt')
horizontal_line_3, = ax2.plot([],[],'r:o',linewidth=2,label='horizontal line')
vertical_line_3, = ax2.plot([],[],'g:o',linewidth=2,label='vertical line')

plt.xticks(np.arange(t[0],t[-1]+0.5,(t[-1]-t[0])/4),size=8)
plt.yticks(np.arange(np.min(x_speed),np.max(x_speed)*3/2,(np.max(x_speed)-np.min(x_speed))/4), size=8)
plt.xlabel("Time [sec]", size=10)
plt.ylabel("Speed [kph]", size=10)
plt.title("Speed vs Time", size=12)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(np.min(x_speed),np.max(x_speed)*3/2)
plt.legend(loc='upper right', fontsize='medium')

plane_ani = animation.FuncAnimation(fig, update_plot,
    frames=frame_amount, interval=5, repeat=True, blit=True)
plt.show()