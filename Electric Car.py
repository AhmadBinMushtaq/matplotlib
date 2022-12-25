import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate (i, velocity_arr, current_arr, power_arr, motorSpeed_arr, ser):
    ser.write(b'1')                                     # Transmit the char 'g' to receive the Arduino data point
    velocity = ser.readline().decode('ascii') # Decode receive Arduino data as a formatted string
    #print(velocity)
    ser.write(b'2')
    current = ser.readline().decode('ascii')
    ser.write(b'3')
    power = ser.readline().decode('ascii')
    ser.write(b'4')
    motorSpeed = ser.readline().decode('ascii')
    #ser.write(b'5')
    #current4 = ser.readline().decode('ascii')
    #print(i)                                           # 'i' is a incrementing variable based upon frames = x argument

    try:
        velocity_float = float(velocity)   # Convert to float
        velocity_arr.append(velocity_float)              # Add to the list holding the fixed number of points to animate
        current_float = float(current)/10
        current_arr.append(current_float)
        power_float = float(power)
        power_arr.append(power_float)
        motorSpeed_float = float(motorSpeed)
        motorSpeed_arr.append(motorSpeed_float)
        #current4_float = float(current4)
        #current4_arr.append(current4_float)

    except:                                             # Pass if data point is bad                               
        pass

    velocity_arr = velocity_arr[-50:]                           # Fix the list size so that the animation plot 'window' is x number of points
    current_arr = current_arr[-50:]
    power_arr = power_arr[-50:]
    motorSpeed_arr = motorSpeed_arr[-50:]
    #current4_arr = current4_arr[-50:]
    
    ax.clear()                                          # Clear last data frame
    ax.plot(velocity_arr)                                   # Plot new data frame
    
    ax.set_ylim([0,50])                              # Set Y axis limit of plot
    ax.set_title("Velocity")                        # Set title of figure
    ax.set_ylabel("m/s")                              # Set title of y axis 

    ax1.clear()
    ax1.plot(current_arr)

    ax1.set_ylim([0,50])
    ax1.set_title("current")
    ax1.set_ylabel("Ampere")

    ax2.clear()
    ax2.plot(power_arr)

    ax2.set_ylim([0,500])
    ax2.set_title("power")
    ax2.set_ylabel("Watts")

    ax3.clear()
    ax3.plot(motorSpeed_arr)

    ax3.set_ylim([0,100])
    ax3.set_title("motorSpeed")
    ax3.set_ylabel("Percentage")

    #ax4.clear()
    #ax4.plot(current4_arr)

    #ax4.set_ylim([0,50])
    #ax4.set_title("Current4")
    #ax4.set_ylabel("Ampere")

velocity_arr = []                                           # Create empty list variable for later use
current_arr = []
power_arr = []
motorSpeed_arr = []
#current4_arr = []
                                                        
fig = plt.figure()                                      # Create Matplotlib plots fig is the 'higher level' plot window
ax = fig.add_subplot(221)                               # Add subplot to main fig window
ax1 = fig.add_subplot(222)
ax2 = fig.add_subplot(223)
ax3 = fig.add_subplot(224)
#ax4 = fig.add_subplot(335)

ser = serial.Serial("COM5", 9600)                       # Establish Serial object with COM port and BAUD rate to match Arduino Port/rate
time.sleep(2)                                           # Time delay for Arduino Serial initialization 

                                                        # Matplotlib Animation Fuction that takes takes care of real time plot.
                                                        # Note that 'fargs' parameter is where we pass in our velocity_arr and Serial object. 
ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(velocity_arr, current_arr, power_arr, motorSpeed_arr, ser), interval=100) 

plt.show()                                              # Keep Matplotlib plot persistent on screen until it is closed
ser.close()                                             # Close Serial connection when plot is closed