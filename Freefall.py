import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Setting up the duration for animation
t0 = 0 # Starting time (Seconds)
t_end = 9 # Ending time (Seconds)
dt = 0.02 # increment value for time

# Creating time array
t = np.arange(t0,t_end + dt, dt)

# Gravitational Acceleration
g_earth=-9.807
g_mars=-3.721
g_moon=-1.62

# Position Arrays
y_initial=100

y_earth=y_initial+g_earth*t**2
velocity_earth=g_earth*t
acceleration_earth=g_earth*np.ones(len(t))
for i in range(0,len(t)):
    if(y_earth[i]<0):
        y_earth[i]=0
        velocity_earth[i]=0
        acceleration_earth[i]=0

y_mars=y_initial+g_mars*t**2
velocity_mars=g_mars*t
acceleration_mars=g_mars*np.ones(len(t))
for i in range(0,len(t)):
    if(y_mars[i]<0):
        y_mars[i]=0
        velocity_mars[i]=0
        acceleration_mars[i]=0

y_moon=y_initial+g_moon*t**2
velocity_moon=g_moon*t
acceleration_moon=g_moon*np.ones(len(t))
for i in range(0,len(t)):
    if(y_moon[i]<0):
        y_moon[i]=0
        velocity_moon[i]=0
        acceleration_moon[i]=0

# Create Circles
def create_circle(r):
    angle=np.arange(0,2*np.pi,0.01)
    x_coordinate=r*np.cos(angle)
    y_coordinate=r*np.sin(angle)
    return x_coordinate,y_coordinate

circle_x,circle_y=create_circle(5)


################ ANIMATION ######################

frame_amount=len(t)

# Function to update plot
def update_plot(num):

    if y_earth[num]>0:
        sphere_earth.set_data(circle_x,circle_y+y_earth[num]+5)
        sphere_mars.set_data(circle_x,circle_y+y_mars[num]+5)
        sphere_moon.set_data(circle_x,circle_y+y_moon[num]+5)
        position_earth.set_data(t[0:num],y_earth[0:num])
        position_mars.set_data(t[0:num],y_mars[0:num])
        position_moon.set_data(t[0:num],y_moon[0:num])
        speed_earth.set_data(t[0:num],velocity_earth[0:num])
        speed_mars.set_data(t[0:num],velocity_mars[0:num])
        speed_moon.set_data(t[0:num],velocity_moon[0:num])
        accel_earth.set_data(t[0:num],acceleration_earth[0:num])
        accel_mars.set_data(t[0:num],acceleration_mars[0:num])
        accel_moon.set_data(t[0:num],acceleration_moon[0:num])

    return sphere_earth,sphere_mars,sphere_moon,position_earth,position_mars,position_moon,\
    speed_earth,speed_mars,speed_moon,accel_earth,accel_mars,accel_moon

# Figure Properties
fig=plt.figure(figsize=(16,9),dpi=80,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(3,4)

# Subplot for Earth
ax0=fig.add_subplot(gs[:,0],facecolor=(0.9,0.9,0.9))
sphere_earth,=ax0.plot([],[],'k',linewidth=3)
land_earth,=ax0.plot([-6,6],[-5,-5],'g',linewidth=35)

# Subplot properties
plt.xticks(np.arange(-6,6,2),size=8)
plt.yticks(np.arange(-10,y_initial+10,(y_initial)/10),size=8)
plt.ylabel("Vertical Elevation [m]", size=10)
plt.title("Earth", size=12)
plt.grid(True)
plt.xlim(-6,6)
plt.ylim(-10,y_initial+10)

# Subplot for Mars
ax1=fig.add_subplot(gs[:,1],facecolor=(0.9,0.9,0.9))
sphere_mars,=ax1.plot([],[],'k',linewidth=3)
land_mars,=ax1.plot([-6,6],[-5,-5],'brown',linewidth=35)

# Subplot properties
plt.xticks(np.arange(-6,6,2),size=8)
plt.yticks(np.arange(-10,y_initial+10,(y_initial)/10),size=8)
plt.ylabel("Vertical Elevation [m]", size=10)
plt.title("Mars", size=12)
plt.grid(True)
plt.xlim(-6,6)
plt.ylim(-10,y_initial+10)

# Subplot for Moon
ax2=fig.add_subplot(gs[:,2],facecolor=(0.9,0.9,0.9))
sphere_moon,=ax2.plot([],[],'k',linewidth=3)
land_moon,=ax2.plot([-6,6],[-5,-5],'grey',linewidth=35)

# Subplot properties
plt.xticks(np.arange(-6,6,2),size=8)
plt.yticks(np.arange(-10,y_initial+10,(y_initial)/10),size=8)
plt.ylabel("Vertical Elevation [m]", size=10)
plt.title("Moon", size=12)
plt.grid(True)
plt.xlim(-6,6)
plt.ylim(-10,y_initial+10)

# Position Graph
ax3=fig.add_subplot(gs[0,3],facecolor=(0.9,0.9,0.9))
position_earth,=ax3.plot([],[],'g',linewidth=2,label='Earth Altitude')
position_mars,=ax3.plot([],[],'brown',linewidth=2,label='Mars Altitude')
position_moon,=ax3.plot([],[],'grey',linewidth=2,label='Moon Altitude')

# Subplot properties
plt.xticks(np.arange(t[0],t[-1]+0.1,t[-1]/3),size=8)
plt.yticks(np.arange(0,y_initial,(y_initial)/10),size=8)
plt.ylabel("Vertical Elevation [m]", size=10)
plt.title("Position Graph", size=12)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(0,y_initial)
plt.legend(loc='upper right', fontsize='small')

# Velocity Graph
ax4=fig.add_subplot(gs[1,3],facecolor=(0.9,0.9,0.9))
speed_earth,=ax4.plot([],[],'g',linewidth=2,label='Speed on earth')
speed_mars,=ax4.plot([],[],'brown',linewidth=2,label='Speed on Mars')
speed_moon,=ax4.plot([],[],'grey',linewidth=2,label='Speed on Moon')

# Subplot properties
plt.xticks(np.arange(t[0],t[-1]+0.1,t[-1]/3),size=8)
plt.yticks(np.arange(int(np.min(velocity_earth)),3,int((np.min(velocity_earth))/5)*-1),size=8)
plt.ylabel("Speed [m/s]", size=10)
plt.title("Velocity Graph", size=12)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(min(velocity_earth),3)
plt.legend(loc='lower right', fontsize='small')

# Acceleration Graph
ax5=fig.add_subplot(gs[2,3],facecolor=(0.9,0.9,0.9))
accel_earth,=ax5.plot([],[],'g',linewidth=2,label='Acceleration on earth')
accel_mars,=ax5.plot([],[],'brown',linewidth=2,label='Acceleration on Mars')
accel_moon,=ax5.plot([],[],'grey',linewidth=2,label='Acceleration on Moon')

# Subplot properties
plt.xticks(np.arange(t[0],t[-1]+0.1,t[-1]/3),size=8)
plt.yticks(np.arange(int(g_earth*1.5),3,int(g_earth/5)*-1),size=8)
plt.ylabel("Acceleration [m/s^2]", size=10)
plt.title("Acceleration Graph", size=12)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(g_earth*1.5,3)
plt.legend(loc='lower right', fontsize='small')

plane_ani = animation.FuncAnimation(fig, update_plot,
    frames=frame_amount, interval=5, repeat=True, blit=True)
plt.show()