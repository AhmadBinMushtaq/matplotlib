from this import d
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Flight Parameters
g = 9.8
t0 = 0 # Starting time (Hours)
t_end = 1.2 # Ending time (Hours)
dt = 0.002 # increment value for time
drag_function = (0.350317,-0.202576,0) # Drag as function of velocity
lift_function = (0.350823,0.00372739,0) # Lift as function of velocity
mass = 6.9 # MTOW of UAV
thrust = 12*g # Constant Thrust during transition
power = (0.0000373344395*(thrust*250/g)**2 + 0.109504955*(thrust*250/g))*4 # Power as function of thrust

# Initializing all arrays
t = np.arange(t0,t_end + dt, dt)
tilt_angle = np.ones(len(t))*np.pi/2
drag = np.zeros(len(t))
lift = np.zeros(len(t))
velocity = np.zeros(len(t))
distance = np.zeros(len(t))
total_energy = np.zeros(len(t))
horizontal_thrust = np.zeros(len(t))

# Calculations
transition_completed = False
completion_index = 0
for i in range(1,len(t)):
    horizontal_thrust[i] = (thrust**2 - (mass*g - lift[i])**2)**0.5
    velocity[i] = velocity[i-1] + horizontal_thrust[i]*dt/mass
    distance[i] = distance[i-1] + velocity[i]*dt
    drag[i] = drag_function[0]*velocity[i]**2 + drag_function[1]*velocity[i] + drag_function[2]
    lift[i] = lift_function[0]*velocity[i]**2 + drag_function[1]*velocity[i] + drag_function[2]
    if lift[i]>mass*g:
        lift[i]=mass*g
        if transition_completed == False:
            transition_completed = True
            completion_index = i
    tilt_angle[i] = np.arctan((mass*g-lift[i])/horizontal_thrust[i])
    total_energy[i] = total_energy[i-1] + power*dt

#####################Animation#########################

frame_amount = len(t)
dot = np.zeros(frame_amount)
n = 20
for i in range(0,frame_amount):
    if(i==n):
        dot[i]=distance[n]
        n+=20
    else:
        dot[i]=distance[n-20]


def update_plot(num):

    # Subplot 1
    horizontal_line.set_data(dot[0:num],2)
    vertical_line.set_data([distance[num],distance[num]],[0,2])
    plane_1.set_data([distance[num]-0.5,distance[num]+0.5],[2,2])
    plane_2.set_data([distance[num]+0.3-np.cos(tilt_angle[num])/4,distance[num]+0.3+np.cos(tilt_angle[num])/4],\
        [2-np.sin(tilt_angle[num])/4,2+np.sin(tilt_angle[num])/4])
    plane_3.set_data([distance[num]-0.3-np.cos(tilt_angle[num])/4,distance[num]-0.3+np.cos(tilt_angle[num])/4],\
        [2-np.sin(tilt_angle[num])/4,2+np.sin(tilt_angle[num])/4])
    plane_2_line.set_data([distance[num]+0.3-np.cos(tilt_angle[num])*1000,distance[num]+0.3+np.cos(tilt_angle[num])*1000],\
        [2-np.sin(tilt_angle[num])*1000,2+np.sin(tilt_angle[num])*1000])
    plane_3_line.set_data([distance[num]-0.3-np.cos(tilt_angle[num])*1000,distance[num]-0.3+np.cos(tilt_angle[num])*1000],\
        [2-np.sin(tilt_angle[num])*1000,2+np.sin(tilt_angle[num])*1000])

    # Subplot 2
    x_dist_2.set_data(t[0:num],distance[0:num])
    horizontal_line_2.set_data([0,t[num]],[distance[num],distance[num]])
    vertical_line_2.set_data([t[num],t[num]],[0,distance[num]])

    # Subplot 3
    speed_line.set_data(t[0:num],velocity[0:num])
    horizontal_line_3.set_data([0,t[num]],[velocity[num],velocity[num]])
    vertical_line_3.set_data([t[num],t[num]],[0,velocity[num]])

    # Subplot 4
    angle_line.set_data(t[0:num],tilt_angle[0:num])
    horizontal_line_4.set_data([0,t[num]],[tilt_angle[num],tilt_angle[num]])
    vertical_line_4.set_data([t[num],t[num]],[0,tilt_angle[num]])

    # Subplot 5
    energy_line.set_data(t[0:num],total_energy[0:num])
    horizontal_line_5.set_data([0,t[num]],[total_energy[num],total_energy[num]])
    vertical_line_5.set_data([t[num],t[num]],[0,total_energy[num]])

    # Subplot 6
    lift_line.set_data(t[0:num],lift[0:num])
    horizontal_line_6.set_data([0,t[num]],[lift[num],lift[num]])
    vertical_line_6.set_data([t[num],t[num]],[0,lift[num]])

    # Subplot 7
    drag_line.set_data(t[0:num],drag[0:num])
    horizontal_line_7.set_data([0,t[num]],[drag[num],drag[num]])
    vertical_line_7.set_data([t[num],t[num]],[0,drag[num]])


    return horizontal_line,vertical_line,plane_1,plane_2,plane_3,plane_2_line,plane_3_line,\
        x_dist_2,horizontal_line_2,vertical_line_2,\
        speed_line,horizontal_line_3,vertical_line_3,\
        angle_line,horizontal_line_4,vertical_line_4,\
        energy_line,horizontal_line_5,vertical_line_5,\
        lift_line,horizontal_line_6,vertical_line_6,\
        drag_line,horizontal_line_7,vertical_line_7

fig = plt.figure(figsize=(16,9), dpi=80, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(3,3)

# Subplot 01
ax0 = fig.add_subplot(gs[0,:], facecolor=(0.9,0.9,0.9))

# Draw plane trajectory
horizontal_line, = ax0.plot([],[],'r:o', linewidth=2)
vertical_line, = ax0.plot([],[],'k:o',linewidth=2)
red_line, = ax0.plot([distance[completion_index],distance[completion_index]],[0,50000],'r',linewidth=2)

# Draw airplane
plane_1, = ax0.plot([],[],'k',linewidth=5)
plane_2, = ax0.plot([],[],'k',linewidth=5)
plane_3, = ax0.plot([],[],'k',linewidth=5)
plane_2_line, = ax0.plot([],[],'g:o',linewidth=2)
plane_3_line, = ax0.plot([],[],'g:o',linewidth=2)

# Subplot properties
plt.xticks(np.arange(distance[0],distance[-1]+1,int(distance[-1]-distance[0])/4),size=7)
plt.yticks(np.arange(0,4,1),size=7)
ax0.xaxis.set_label_coords(0.5,0)
plt.xlabel("Horizontal Distance [m]", size=8)
plt.title("Airplane Projection", size=10, pad=-20)
plt.grid(True)
plt.xlim(distance[0],distance[-1]+2)
plt.ylim(0,5)


# Subplot 02
ax1 = fig.add_subplot(gs[1,0], facecolor=(0.9,0.9,0.9))
x_dist_2, = ax1.plot([],[],'-b',linewidth=3,label='X=800*t')
horizontal_line_2, = ax1.plot([],[],'r:o',linewidth=2,label='horizontal line')
vertical_line_2, = ax1.plot([],[],'g:o',linewidth=2,label='vertical line')
red_line2, = ax1.plot([t[completion_index],t[completion_index]],[0,50000],'r',linewidth=2)


plt.xticks(np.arange(t[0],t[-1]+0.5,(t[-1]-t[0])/4),size=7)
plt.yticks(np.arange(distance[0],distance[-1]*3/2,(distance[-1]-distance[0])/4), size=7)
plt.ylabel("Distance [m]", size=8)
plt.title("Distance", size=10, pad=-20)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(distance[0],distance[-1]*3/2)

# Subplot 03
ax2 = fig.add_subplot(gs[1,1], facecolor=(0.9,0.9,0.9))
speed_line, = ax2.plot([],[],'b',linewidth=3,label='dx/dt')
horizontal_line_3, = ax2.plot([],[],'r:o',linewidth=2,label='horizontal line')
vertical_line_3, = ax2.plot([],[],'g:o',linewidth=2,label='vertical line')
red_line3, = ax2.plot([t[completion_index],t[completion_index]],[0,50000],'r',linewidth=2)

plt.xticks(np.arange(t[0],t[-1]+0.5,(t[-1]-t[0])/4),size=7)
plt.yticks(np.arange(velocity[0],velocity[-1]*3/2,int(velocity[-1]/4)), size=7)
plt.ylabel("Speed [m\s]", size=8)
plt.title("Speed", size=10, pad=-20)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(velocity[0],velocity[-1]*3/2)

# Subplot 04
ax3 = fig.add_subplot(gs[1,2], facecolor=(0.9,0.9,0.9))
angle_line, = ax3.plot([],[],'b',linewidth=3,label='dx/dt')
horizontal_line_4, = ax3.plot([],[],'r:o',linewidth=2,label='horizontal line')
vertical_line_4, = ax3.plot([],[],'g:o',linewidth=2,label='vertical line')
red_line4, = ax3.plot([t[completion_index],t[completion_index]],[0,50000],'r',linewidth=2)

plt.ylabel("Tilt Angle [rad]", size=7)
plt.title("Tilt Angle", size=10, pad=-20)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(0,np.max(tilt_angle)*3/2)

# Subplot 05
ax4 = fig.add_subplot(gs[2,0], facecolor=(0.9,0.9,0.9))
energy_line, = ax4.plot([],[],'b',linewidth=3,label='dx/dt')
horizontal_line_5, = ax4.plot([],[],'r:o',linewidth=2,label='horizontal line')
vertical_line_5, = ax4.plot([],[],'g:o',linewidth=2,label='vertical line')
red_line5, = ax4.plot([t[completion_index],t[completion_index]],[0,50000],'r',linewidth=2)

plt.xlabel("Time [sec]", size=7)
plt.ylabel("Energy [Joules]", size=7)
ax0.xaxis.set_label_coords(0.5,0)
plt.title("Energy Consumption", size=10, pad=-20)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(0,np.max(total_energy)*3/2)

# Subplot 06
ax5 = fig.add_subplot(gs[2,1], facecolor=(0.9,0.9,0.9))
lift_line, = ax5.plot([],[],'b',linewidth=3,label='dx/dt')
horizontal_line_6, = ax5.plot([],[],'r:o',linewidth=2,label='horizontal line')
vertical_line_6, = ax5.plot([],[],'g:o',linewidth=2,label='vertical line')
red_line6, = ax5.plot([t[completion_index],t[completion_index]],[0,50000],'r',linewidth=2)

plt.xlabel("Time [sec]", size=7)
plt.ylabel("Lift [N]", size=7)
plt.title("Lift", size=10, pad=-20)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(0,np.max(lift)*3/2)

# Subplot 07
ax6 = fig.add_subplot(gs[2,2], facecolor=(0.9,0.9,0.9))
drag_line, = ax6.plot([],[],'b',linewidth=3,label='dx/dt')
horizontal_line_7, = ax6.plot([],[],'r:o',linewidth=2,label='horizontal line')
vertical_line_7, = ax6.plot([],[],'g:o',linewidth=2,label='vertical line')
red_line7, = ax6.plot([t[completion_index],t[completion_index]],[0,50000],'r',linewidth=2)

plt.xlabel("Time [sec]", size=7)
plt.ylabel("Drag [N]", size=7)
plt.title("Drag", size=10, pad=-20)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(0,np.max(drag)*3/2)

plane_ani = animation.FuncAnimation(fig, update_plot,
    frames=frame_amount, interval=1, repeat=True, blit=True)
plt.show()