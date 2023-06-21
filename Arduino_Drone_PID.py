import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Setting up the duration for animation
t0 = 0 # Starting time (Hours)
t_end = 5 # Ending time (Hours)
dt = 0.02 # increment value for time

# Creating time array
t = np.arange(t0,t_end + dt, dt)


command = np.zeros(len(t))
for i in range(int(len(t)/5), int(len(t))):
    command[i] = 0.1

Kp = 12
Ki = 11
Kd = 7

# Kp = 20
# Ki = 10
# Kd = 0

I = 4.1

max_torque = 640

int_min = -10
int_max = 10

pitch = np.zeros(len(t))
error = np.zeros(len(t))
integral = np.zeros(len(t))
derivative = np.zeros(len(t))
pid = np.zeros(len(t))

drone_x1 = np.zeros(len(t))
drone_x2 = np.zeros(len(t))
drone_y1 = np.zeros(len(t))
drone_y2 = np.zeros(len(t))
drone_z1 = np.zeros(len(t))
drone_z2 = np.zeros(len(t))

acceleration = np.zeros(len(t))
velocity = np.zeros(len(t))

for i in range(1, len(t)):
    error[i] = command[i-1] - pitch[i-1]
    integral[i] = min(int_max, max(int_min, integral[i-1] + error[i] * dt))
    derivative[i] = (error[i] - error[i-1]) / dt
    pid[i] = (Kp * error[i]) + (Ki * integral[i]) + (Kd * derivative[i])
    acceleration[i] = (max_torque * pid[i]) / (100 * I)
    velocity[i] = velocity[i-1] + acceleration[i] * dt
    pitch[i] = pitch[i-1] + velocity[i] * dt
    drone_x1[i] = np.sin(np.pi/2 - pitch[i])*np.cos(np.pi/4)
    drone_y1[i] = np.sin(np.pi/2 - pitch[i])*np.sin(np.pi/4)
    drone_z1[i] = np.cos(np.pi/2 - pitch[i])

#####################Animation#########################

frame_amount = len(t)


def update_plot(num):

    drone1.set_data((drone_x1[num], -1* drone_x1[num]), (drone_y1[num], -1* drone_y1[num]))
    drone1.set_3d_properties((drone_z1[num], -1* drone_z1[num]))

    drone2.set_data((drone_x1[num], -1* drone_x1[num]), (-1 * drone_y1[num], drone_y1[num]))
    drone2.set_3d_properties((drone_z1[num], -1* drone_z1[num]))

    command_value.set_data(t[0:num],command[0:num])
    pitch_value.set_data(t[0:num],pitch[0:num])
    pid_value.set_data(t[0:num],pid[0:num])

    error_value.set_text(str(round(error[num], 5)))

    return drone1, drone2, command_value, pitch_value, pid_value ,error_value

fig = plt.figure(figsize=(16,9), dpi=80, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,2)

# Subplot 01
ax0 = fig.add_subplot(gs[1,0], projection='3d', facecolor=(0.9,0.9,0.9))



# Draw trajectory
drone1, = ax0.plot([],[],[],'k',linewidth=3)
drone2, = ax0.plot([],[],[],'k',linewidth=3)

# Subplot properties
ax0.set_xlim(-1.2, 1.2)
ax0.set_ylim(-1.2, 1.2)
ax0.set_zlim(-1.2, 1.2)
ax0.set_xlabel('Position X [m]',fontsize=12)
ax0.set_ylabel('Position Y [m]', fontsize=12)
ax0.set_zlabel('Position Z [m]', fontsize=12)
plt.title("Airplane Projection", size=12)
plt.grid(True)
plt.legend(loc='upper left',fontsize='large')

# Subplot 02
ax1 = fig.add_subplot(gs[0,:], facecolor=(0.9,0.9,0.9))
command_value, = ax1.plot([],[],'b',linewidth=3, label="Pitch Command")
pitch_value, = ax1.plot([],[], 'r', linewidth=3, label="Measured Pitch")

# Insert stopwatch1 & distance text
circle = dict(boxstyle='circle', fc=(0.7,0.7,0.7), ec='r', lw=2)
square = dict(boxstyle="square", fc=(0.7,0.7,0.7), ec = 'g', lw=2)

pid_P = ax1.text(0.3,-0.08,"Kp = "+str(Kp), size=15, color='b', bbox=square)
pid_I = ax1.text(0.3,-0.17,"Ki = "+str(Ki), size=15, color='b', bbox=square)
pid_D = ax1.text(0.3,-0.26,"Kd = "+str(Kd), size=15, color='b', bbox=square)
err = ax1.text(4, -0.26, "Error = ", size=18, color = 'r', bbox=square)
error_value = ax1.text(4.4, -0.26, "", size=18, color = 'r', bbox=square)

# Subplot properties
plt.ylabel("Position X [m]", size=10)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(-0.3, 0.3)
plt.legend(loc='upper left', fontsize='medium')

# Subplot 03
ax2 = fig.add_subplot(gs[1,1], facecolor=(0.9,0.9,0.9))
pid_value, = ax2.plot([],[],'b',linewidth=3, label="PID Signal")

# Subplot properties
plt.ylabel("Error", size=10)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(min(pid), max(pid))
plt.legend(loc='upper left', fontsize='medium')


plane_ani = animation.FuncAnimation(fig, update_plot,
    frames=frame_amount, interval=1, repeat=True, blit=True)
# plt.show()

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
plane_ani.save('animation.mp4', writer=writer)