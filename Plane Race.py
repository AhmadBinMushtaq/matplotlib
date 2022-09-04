import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Setting up the duration for animation
t0 = -1 # Starting time (Hours)
t_end = 2 # Ending time (Hours)
dt = 0.005 # increment value for time

# Creating time array
t = np.arange(t0,t_end + dt, dt)
for x in range(0,len(t),1):
    if t[x]<0:
        t[x]=0

# Creating x - axis arrays
c1=300
c2=700
c3=900
i1=3.5
i2=1.64
i3=0.1
x1 = c1*t**i1
x2 = c2*t**i2
x3 = c3*t**i3

# Creating x - axis speed arrays
x_speed1 = np.zeros(len(t))
x_speed2 = np.zeros(len(t))
x_speed3 = np.zeros(len(t))
for i in range(1,len(t)):
    x_speed1[i] = (x1[i]-x1[i-1])/dt
    x_speed2[i] = (x2[i]-x2[i-1])/dt
    x_speed3[i] = (x3[i]-x3[i-1])/dt

# Creating y - axis arrays
altitude1 = 2 # Altitude is constant for whole flight
altitude2 = 4 # Altitude is constant for whole flight
altitude3 = 6 # Altitude is constant for whole flight


#####################Animation#########################

frame_amount = len(t)
dot1 = np.zeros(frame_amount)
dot2 = np.zeros(frame_amount)
dot3 = np.zeros(frame_amount)

n = 20
for i in range(0,frame_amount):
    if(i==n):
        dot1[i]=x1[n]
        dot2[i]=x2[n]
        dot3[i]=x3[n]
        n+=20
    else:
        dot1[i]=x1[n-20]
        dot2[i]=x2[n-20]
        dot3[i]=x3[n-20]


def update_plot(num):

    # Subplot 1
    horizontal_line_1_1.set_data(dot1[0:num],altitude1)
    vertical_line_1_1.set_data([x1[num],x1[num]],[0,altitude1])
    plane_1_1.set_data((x1[num]-30,x1[num]+30),(altitude1,altitude1))
    plane_1_2.set_data((x1[num],x1[num]+20),(altitude1-0.5,altitude1))
    plane_1_3.set_data((x1[num],x1[num]+20),(altitude1+0.5,altitude1))
    plane_1_4.set_data((x1[num]-50,x1[num]-35),(altitude1-0.2,altitude1))
    plane_1_5.set_data((x1[num]-50,x1[num]-35),(altitude1+0.2,altitude1))
    stopwatch1.set_text(str(round(t[num],1)) + " hrs")
    distance_counter1.set_text(str(int(x1[num])) + " km")

    horizontal_line_1_2.set_data(dot2[0:num],altitude2)
    vertical_line_1_2.set_data([x2[num],x2[num]],[0,altitude2])
    plane_2_1.set_data((x2[num]-30,x2[num]+30),(altitude2,altitude2))
    plane_2_2.set_data((x2[num],x2[num]+20),(altitude2-0.5,altitude2))
    plane_2_3.set_data((x2[num],x2[num]+20),(altitude2+0.5,altitude2))
    plane_2_4.set_data((x2[num]-50,x2[num]-35),(altitude2-0.2,altitude2))
    plane_2_5.set_data((x2[num]-50,x2[num]-35),(altitude2+0.2,altitude2))
    stopwatch2.set_text(str(round(t[num],1)) + " hrs")
    distance_counter2.set_text(str(int(x2[num])) + " km")

    horizontal_line_1_3.set_data(dot3[0:num],altitude3)
    vertical_line_1_3.set_data([x3[num],x3[num]],[0,altitude3])
    plane_3_1.set_data((x3[num]-30,x3[num]+30),(altitude3,altitude3))
    plane_3_2.set_data((x3[num],x3[num]+20),(altitude3-0.5,altitude3))
    plane_3_3.set_data((x3[num],x3[num]+20),(altitude3+0.5,altitude3))
    plane_3_4.set_data((x3[num]-50,x3[num]-35),(altitude3-0.2,altitude3))
    plane_3_5.set_data((x3[num]-50,x3[num]-35),(altitude3+0.2,altitude3))
    stopwatch3.set_text(str(round(t[num],1)) + " hrs")
    distance_counter3.set_text(str(int(x3[num])) + " km")

    # Subplot 2
    x_dist_2_1.set_data(t[0:num],x1[0:num])
    horizontal_line_2_1.set_data([t[0],t[num]],[x1[num],x1[num]])
    vertical_line_2_1.set_data([t[num],t[num]],[x1[0],x1[num]])
    
    x_dist_2_2.set_data(t[0:num],x2[0:num])
    horizontal_line_2_2.set_data([t[0],t[num]],[x2[num],x2[num]])
    vertical_line_2_2.set_data([t[num],t[num]],[x2[0],x2[num]])
    
    x_dist_2_3.set_data(t[0:num],x3[0:num])
    horizontal_line_2_3.set_data([t[0],t[num]],[x3[num],x3[num]])
    vertical_line_2_3.set_data([t[num],t[num]],[x3[0],x3[num]])

    # Subplot 3
    speed_line_1.set_data(t[0:num],x_speed1[0:num])
    horizontal_line_3_1.set_data([t[0],t[num]],[x_speed1[num],x_speed1[num]])
    vertical_line_3_1.set_data([t[num],t[num]],[x_speed1[0],x_speed1[num]])

    speed_line_2.set_data(t[0:num],x_speed2[0:num])
    horizontal_line_3_2.set_data([t[0],t[num]],[x_speed2[num],x_speed2[num]])
    vertical_line_3_2.set_data([t[num],t[num]],[x_speed2[0],x_speed2[num]])

    speed_line_3.set_data(t[0:num],x_speed3[0:num])
    horizontal_line_3_3.set_data([t[0],t[num]],[x_speed3[num],x_speed3[num]])
    vertical_line_3_3.set_data([t[num],t[num]],[x_speed3[0],x_speed3[num]])


    return stopwatch1,distance_counter1,horizontal_line_1_1,vertical_line_1_1,plane_1_1,plane_1_2,plane_1_3,plane_1_4,plane_1_5,\
    stopwatch2,distance_counter2,horizontal_line_1_2,vertical_line_1_2,plane_2_1,plane_2_2,plane_2_3,plane_2_4,plane_2_5,\
    stopwatch3,distance_counter3,horizontal_line_1_3,vertical_line_1_3,plane_3_1,plane_3_2,plane_3_3,plane_3_4,plane_3_5,\
    x_dist_2_1,horizontal_line_2_1,vertical_line_2_1,\
    x_dist_2_2,horizontal_line_2_2,vertical_line_2_2,\
    x_dist_2_3,horizontal_line_2_3,vertical_line_2_3,\
    speed_line_1,horizontal_line_3_1,vertical_line_3_1,\
    speed_line_2,horizontal_line_3_2,vertical_line_3_2,\
    speed_line_3,horizontal_line_3_3,vertical_line_3_3

fig = plt.figure(figsize=(16,9), dpi=80, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,2)

# Subplot 01
ax0 = fig.add_subplot(gs[0,:], facecolor=(0.9,0.9,0.9))

# Draw plane trajectories
horizontal_line_1_1, = ax0.plot([],[],'b:o', linewidth=2)
vertical_line_1_1, = ax0.plot([],[],'b:o',linewidth=2)

horizontal_line_1_2, = ax0.plot([],[],'g:o', linewidth=2)
vertical_line_1_2, = ax0.plot([],[],'g:o',linewidth=2)

horizontal_line_1_3, = ax0.plot([],[],'r:o', linewidth=2)
vertical_line_1_3, = ax0.plot([],[],'r:o',linewidth=2)

# Insert stopwatch1 & distance text
circle = dict(boxstyle='circle', fc=(0.7,0.7,0.7), ec='r', lw=2)
square = dict(boxstyle="square", fc=(0.7,0.7,0.7), ec = 'g', lw=2)

# Draw airplanes
plane_1_1, = ax0.plot([],[],'k',linewidth=5)
plane_1_2, = ax0.plot([],[],'k',linewidth=5)
plane_1_3, = ax0.plot([],[],'k',linewidth=5)
plane_1_4, = ax0.plot([],[],'k',linewidth=5)
plane_1_5, = ax0.plot([],[],'k',linewidth=5)
distance_counter1 = ax0.text(1370,1,"", size=12, color='b', bbox=square)
stopwatch1 = ax0.text(1500,1,"", size=12, color='k', bbox=square)

plane_2_1, = ax0.plot([],[],'k',linewidth=5)
plane_2_2, = ax0.plot([],[],'k',linewidth=5)
plane_2_3, = ax0.plot([],[],'k',linewidth=5)
plane_2_4, = ax0.plot([],[],'k',linewidth=5)
plane_2_5, = ax0.plot([],[],'k',linewidth=5)
distance_counter2 = ax0.text(1370,3,"", size=12, color='g', bbox=square)
stopwatch2 = ax0.text(1500,3,"", size=12, color='k', bbox=square)

plane_3_1, = ax0.plot([],[],'k',linewidth=5)
plane_3_2, = ax0.plot([],[],'k',linewidth=5)
plane_3_3, = ax0.plot([],[],'k',linewidth=5)
plane_3_4, = ax0.plot([],[],'k',linewidth=5)
plane_3_5, = ax0.plot([],[],'k',linewidth=5)
distance_counter3 = ax0.text(1370,5,"", size=12, color='r', bbox=square)
stopwatch3 = ax0.text(1500,5,"", size=12, color='k', bbox=square)

# Subplot properties
plt.xticks(np.arange(0,1600,400),size=8)
plt.yticks(np.arange(0,8,1),size=8)
plt.xlabel("Horizontal Distance [km]", size=10)
plt.ylabel("Vertical Elevation [km]", size=10)
plt.title("Airplane Projection", size=12)
plt.grid(True)
plt.xlim(0,1600)
plt.ylim(0,8)


# Subplot 02
ax1 = fig.add_subplot(gs[1,0], facecolor=(0.9,0.9,0.9))

x_dist_2_1, = ax1.plot([],[],'b',linewidth=3,label='X='+str(c1)+'*t^'+str(i1))
horizontal_line_2_1, = ax1.plot([],[],'b:o',linewidth=2)
vertical_line_2_1, = ax1.plot([],[],'b:o',linewidth=2)

x_dist_2_2, = ax1.plot([],[],'g',linewidth=3,label='X='+str(c2)+'*t^'+str(i2))
horizontal_line_2_2, = ax1.plot([],[],'g:o',linewidth=2)
vertical_line_2_2, = ax1.plot([],[],'g:o',linewidth=2)

x_dist_2_3, = ax1.plot([],[],'r',linewidth=3,label='X='+str(c3)+'*t^'+str(i3))
horizontal_line_2_3, = ax1.plot([],[],'r:o',linewidth=2)
vertical_line_2_3, = ax1.plot([],[],'r:o',linewidth=2)

plt.xticks(np.arange(t[0],t[-1]+0.5,(t[-1]-t[0])/4),size=8)
plt.yticks(np.arange(x1[0],x1[-1]*3/2,(x1[-1]-x1[0])/4), size=8)
plt.xlabel("Time [sec]", size=10)
plt.ylabel("Distance [km]", size=10)
plt.title("Distance vs Time", size=12)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(x1[0],x1[-1]*3/2)
plt.legend(loc='upper left', fontsize='medium')

# Subplot 03
ax2 = fig.add_subplot(gs[1,1], facecolor=(0.9,0.9,0.9))

speed_line_1, = ax2.plot([],[],'b',linewidth=3)
horizontal_line_3_1, = ax2.plot([],[],'b:o',linewidth=2)
vertical_line_3_1, = ax2.plot([],[],'b:o',linewidth=2)

speed_line_2, = ax2.plot([],[],'g',linewidth=3)
horizontal_line_3_2, = ax2.plot([],[],'g:o',linewidth=2)
vertical_line_3_2, = ax2.plot([],[],'g:o',linewidth=2)

speed_line_3, = ax2.plot([],[],'r',linewidth=3)
horizontal_line_3_3, = ax2.plot([],[],'r:o',linewidth=2)
vertical_line_3_3, = ax2.plot([],[],'r:o',linewidth=2)

plt.xticks(np.arange(t[0],t[-1]+0.5,(t[-1]-t[0])/4),size=8)
plt.yticks(np.arange(np.min(x_speed3),np.max(x_speed3)*3/2,(np.max(x_speed3)-np.min(x_speed3))/4), size=8)
plt.xlabel("Time [sec]", size=10)
plt.ylabel("Speed [kph]", size=10)
plt.title("Speed vs Time", size=12)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(np.min(x_speed3),np.max(x_speed3)*3/2)
plt.legend(loc='upper right', fontsize='medium')

plane_ani = animation.FuncAnimation(fig, update_plot,
    frames=frame_amount, interval=5, repeat=False, blit=True)
plt.show()