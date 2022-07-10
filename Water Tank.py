import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Setting up the duration for animation
t0 = 0 # Starting time (Seconds)
t_end = 60 # Ending time (Seconds)
dt = 0.04 # increment value for time

t=np.arange(t0,t_end+dt,dt)

# Calculating volumes for tanks

volume_tank1=np.zeros(len(t))
volume_tank2=np.zeros(len(t))
volume_tank3=np.zeros(len(t))

for i in range(0,len(t)):
    if t[i]<=22.5:
        volume_tank1[i]=50+2*t[i]
    elif t[i]<=32.5:
        volume_tank1[i]=95
    elif t[i]<=32.5+45**0.5:
        volume_tank1[i]=95-(t[i]-32.5)**2
    elif t[i]<=42.5+45**0.5:
        volume_tank1[i]=50+np.sin(2*np.pi*(t[i]-32.5+45**0.5))
    else:
        volume_tank1[i]=50

for i in range(0,len(t)):
    if t[i]<=27.5:
        volume_tank2[i]=40+2*t[i]
    elif t[i]<=32.5:
        volume_tank2[i]=95
    elif t[i]<=32.5+45**0.5:
        volume_tank2[i]=95-(t[i]-32.5)**2
    elif t[i]<=37.5+45**0.5:
        volume_tank2[i]=50+3*np.sin(2*np.pi*(t[i]-32.5+45**0.5))
    elif t[i]<=42.5+45**0.5:
        volume_tank2[i]=50+np.sin(2*np.pi*2*(t[i]-37.5+45**0.5))
    else:
        volume_tank2[i]=50

for i in range(0,len(t)):
    if t[i]<=32.5:
        volume_tank3[i]=30+2*t[i]
    elif t[i]<=32.5+45**0.5:
        volume_tank3[i]=95-(t[i]-32.5)**2
    elif t[i]<=42.5+45**0.5:
        volume_tank3[i]=50-np.sin(2*np.pi*(t[i]-32.5+45**0.5))
    else:
        volume_tank3[i]=50

################ ANIMATION ####################
frame_amount=len(t)

def update_plot(num):
    
    vol_line1.set_data(t[0:num],volume_tank1[0:num])
    vol_line2.set_data(t[0:num],volume_tank2[0:num])
    vol_line3.set_data(t[0:num],volume_tank3[0:num])

    tank_1.set_data([-5,5],[volume_tank1[num],volume_tank1[num]])
    tank_2.set_data([-5,5],[volume_tank2[num],volume_tank2[num]])
    tank_3.set_data([-5,5],[volume_tank3[num],volume_tank3[num]])

    tank_12.set_data([0,0],[-64,volume_tank1[num]-64])
    tank_22.set_data([0,0],[-64,volume_tank2[num]-64])
    tank_32.set_data([0,0],[-64,volume_tank3[num]-64])

    zoom_line1.set_data(t[0:num],volume_tank1[0:num])
    zoom_line2.set_data(t[0:num],volume_tank2[0:num])
    zoom_line3.set_data(t[0:num],volume_tank3[0:num])

    return vol_line1,vol_line2,vol_line3,tank_1,tank_2,tank_3,\
    tank_12,tank_22,tank_32,zoom_line1,zoom_line2,zoom_line3

fig=plt.figure(figsize=(16,9),dpi=80,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(2,3)

# Subplot for Volume Graph
ax0=fig.add_subplot(gs[1,0:2],facecolor=(0.9,0.9,0.9))
vol_line1,=ax0.plot([],[],'-b',linewidth=2,label='Tank 1')
vol_line2,=ax0.plot([],[],'-r',linewidth=2,label='Tank 2')
vol_line3,=ax0.plot([],[],'-g',linewidth=2,label='Tank 3')

# Subplot properties
plt.ylabel("Volume [m^3]", size=10)
plt.xlabel("time [s]", size=10)
plt.xticks([0,22.5,27.5,32.5,39.2,44.2,49.2,60])
plt.yticks(np.arange(0,max(np.max(volume_tank1),np.max(volume_tank2),np.max(volume_tank3)),10))
plt.title("Volume Graph", size=12)
plt.grid(True)
plt.xlim(t[0],t[-1])
plt.ylim(0,max(np.max(volume_tank1),np.max(volume_tank2),np.max(volume_tank3))+10)
plt.legend(loc='upper right', fontsize='large')

# Subplot for Tank 1
ax1=fig.add_subplot(gs[0,0],facecolor=(0.9,0.9,0.9))
tank_1,=ax1.plot([],[],'-r',linewidth=4)
tank_12,=ax1.plot([],[],'-b',linewidth=260)

# Subplot properties
plt.ylabel("Volume [m^3]", size=10)
plt.xticks([-5,0,5])
plt.yticks(np.arange(0,max(np.max(volume_tank1),np.max(volume_tank2),np.max(volume_tank3))+1,20))
plt.title("Tank 1", size=12)
plt.grid(True)
plt.xlim(-5,5)
plt.ylim(0,np.max(volume_tank1))

# Subplot for Tank 2
ax2=fig.add_subplot(gs[0,1],facecolor=(0.9,0.9,0.9))
tank_2,=ax2.plot([],[],'-r',linewidth=4)
tank_22,=ax2.plot([],[],'-b',linewidth=260)

# Subplot properties
plt.title("Tank 2", size=12)
plt.xticks([-5,0,5])
plt.yticks(np.arange(0,max(np.max(volume_tank1),np.max(volume_tank2),np.max(volume_tank3))+1,20))
plt.grid(True)
plt.xlim(-5,5)
plt.ylim(0,np.max(volume_tank2))

# Subplot for Tank 3
ax3=fig.add_subplot(gs[0,2],facecolor=(0.9,0.9,0.9))
tank_3,=ax3.plot([],[],'-r',linewidth=4)
tank_32,=ax3.plot([],[],'-b',linewidth=260)

# Subplot properties
plt.title("Tank 3", size=12)
plt.xticks([-5,0,5])
plt.yticks(np.arange(0,max(np.max(volume_tank1),np.max(volume_tank2),np.max(volume_tank3))+1,20))
plt.grid(True)
plt.xlim(-5,5)
plt.ylim(0,np.max(volume_tank3))

# Subplot for Zoomed Volume Graph
ax4=fig.add_subplot(gs[1,2],facecolor=(0.9,0.9,0.9))
zoom_line1,=ax4.plot([],[],'-b',linewidth=2)
zoom_line2,=ax4.plot([],[],'-r',linewidth=2)
zoom_line3,=ax4.plot([],[],'-g',linewidth=2)

# Subplot properties
plt.xticks([0,22.5,27.5,32.5,39.2,44.2,49.2,60])
plt.yticks(np.arange(0,max(np.max(volume_tank1),np.max(volume_tank2),np.max(volume_tank3)),10))
plt.xlabel("time [s]", size=10)
plt.axis([38,50,46,54])
plt.grid(True)


plane_ani = animation.FuncAnimation(fig, update_plot,
    frames=frame_amount, interval=1, repeat=True, blit=True)
plt.show()