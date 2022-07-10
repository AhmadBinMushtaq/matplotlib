import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Setting up the duration for animation
t0 = 0 # Starting time (Seconds)
t_end = 16 # Ending time (Seconds)
dt = 0.02 # increment value for time

t=np.arange(t0,t_end+dt,dt)

# Sinusoidal Movements

# Blue Train
f1=0.125 #frequency
A1=7 #amplitude
blue_train=A1*np.sin(2*np.pi*f1*t)

# Red Train
f2=0.125 #frequency
A2=-7 #amplitude
red_train=A2*np.cos(2*np.pi*f2*t)

# Free fall Movements
y_i=13
green_car=np.ones(len(t))*y_i
purple_car=np.ones(len(t))*y_i
for i in range(0,len(t)):
    if t[i]>2:
        green_car[i]=y_i-2*(t[i]-2)**2
    if t[i]>6:
        purple_car[i]=y_i-2*(t[i]-6)

################ ANIMATION ####################
frame_amount=len(t)

def update_plot(num):
    line_blue.set_data(t[0:num],blue_train[0:num])
    line_red.set_data(t[0:num],red_train[0:num])

    line_green.set_data(t[0:num],green_car[0:num])
    line_purple.set_data(t[0:num],purple_car[0:num])

    train_blue.set_data([blue_train[num]-0.45,blue_train[num]+0.45],[3.5,3.5])
    train_red.set_data([red_train[num]-0.45,red_train[num]+0.45],[1.5,1.5])

    car_green.set_data([3.5,3.5],[green_car[num]-0.45,green_car[num]+0.45])
    car_purple.set_data([-3.5,-3.5],[purple_car[num]-0.45,purple_car[num]+0.45])

    return line_blue,line_red,line_green,line_purple,train_blue,train_red,\
    car_green,car_purple


# Figure Properties
fig=plt.figure(figsize=(16,9),dpi=80,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(2,2)

# Subplot for sinusoidal graph
ax0=fig.add_subplot(gs[0,0],facecolor=(0.9,0.9,0.9))
line_blue,=ax0.plot([],[],'-b',linewidth=3,label='X Blue = ' +str(A1)+'*sin(2π*'+str(f1)+'*t)')
line_red,=ax0.plot([],[],'-r',linewidth=3,label='X Red = ' +str(A2)+'*cos(2π*'+str(f2)+'*t)')

# Subplot properties
plt.ylabel("horizontal distance", size=10)
plt.xlabel("time", size=10)
plt.title("Sinusoidal motion", size=12)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(-max(A1,A2)-1,max(A1,A2)+1)
ax0.spines['bottom'].set_position('center')
ax0.xaxis.set_label_coords(0.5,-0.05)
plt.legend(bbox_to_anchor=(1.02,1.15),fontsize='small')

# Subplot for free fall graph
ax1=fig.add_subplot(gs[1,0],facecolor=(0.9,0.9,0.9))
line_green,=ax1.plot([],[],'-g',linewidth=3,label='Y Green = y_i-2*(t-2)^2')
line_purple,=ax1.plot([],[],'purple',linewidth=3,label='Y Purple = y_i-2*(t-6)')

# Subplot properties
plt.ylabel("Vertical distance", size=10)
plt.xlabel("time", size=10)
plt.title("Free fall motion", size=12)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(-10,y_i+10)
plt.legend(bbox_to_anchor=(1.02,1.15),fontsize='small')
ax1.spines['bottom'].set_position(('data',0))
ax1.xaxis.set_label_coords(0.5,-0.05)

# Subplot for Animation
ax2=fig.add_subplot(gs[:,1],facecolor=(0.9,0.9,0.9))
train_blue,=ax2.plot([],[],'-b',linewidth=28)
train_red,=ax2.plot([],[],'-r',linewidth=28)
car_green,=ax2.plot([],[],'-g',linewidth=28)
car_purple,=ax2.plot([],[],'purple',linewidth=28)

bbox_green=dict(boxstyle='square',fc=(0.9,0.9,0.9),ec='g',lw=1)
bbox_purple=dict(boxstyle='square',fc=(0.9,0.9,0.9),ec='purple',lw=1)
ax2.text(2,y_i+1.5,'car green='+str(y_i)+'-2(t-2)^2',size=10,color='g',bbox=bbox_green)
ax2.text(-7.8,y_i+1.5,'car purple='+str(y_i)+'-2(t-6)',size=10,color='purple',bbox=bbox_purple)

# Danger zones
zone1_1,=ax2.plot([3,4],[1,1],'-k',linewidth=3)
zone1_2,=ax2.plot([4,4],[1,2],'-k',linewidth=3)
zone1_3,=ax2.plot([3,4],[2,2],'-k',linewidth=3)
zone1_4,=ax2.plot([3,3],[1,2],'-k',linewidth=3)
zone2_1,=ax2.plot([3,4],[3,3],'-k',linewidth=3)
zone2_2,=ax2.plot([4,4],[3,4],'-k',linewidth=3)
zone2_3,=ax2.plot([3,4],[4,4],'-k',linewidth=3)
zone2_4,=ax2.plot([3,3],[3,4],'-k',linewidth=3)
zone3_1,=ax2.plot([-3,-4],[1,1],'-k',linewidth=3)
zone3_2,=ax2.plot([-4,-4],[1,2],'-k',linewidth=3)
zone3_3,=ax2.plot([-3,-4],[2,2],'-k',linewidth=3)
zone3_4,=ax2.plot([-3,-3],[1,2],'-k',linewidth=3)
zone4_1,=ax2.plot([-3,-4],[3,3],'-k',linewidth=3)
zone4_2,=ax2.plot([-4,-4],[3,4],'-k',linewidth=3)
zone4_3,=ax2.plot([-3,-4],[4,4],'-k',linewidth=3)
zone4_4,=ax2.plot([-3,-3],[3,4],'-k',linewidth=3)


# Subplot properties
plt.ylabel("Vertical Distance", size=10)
plt.xlabel("Horizontal Distance", size=10)
plt.xticks(np.concatenate([np.arange(-max(A1,A2)-1,0,1),np.arange(1,max(A1,A2)+2,1)]),size=8)
plt.yticks(np.concatenate([np.arange(-2,0,1),np.arange(1,y_i+1,1)]),size=8)
plt.title("Animation", size=12)
plt.grid(True)
plt.xlim(-max(A1,A2)-1,max(A1,A2)+1)
plt.ylim(-2,y_i+1)
ax2.spines['bottom'].set_position(('data',0))
ax2.xaxis.set_label_coords(0.5,-0.05)
ax2.spines['left'].set_position(('data',0))
ax2.yaxis.set_label_coords(-0.05,0.5)

plane_ani = animation.FuncAnimation(fig, update_plot,
    frames=frame_amount, interval=3, repeat=True, blit=True)
plt.show()