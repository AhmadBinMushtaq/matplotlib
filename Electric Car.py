import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class AnimationPlot:

    def animate(self, i, dataList, ser):

        ser.write(b'x')  # Transmit the char 'g' to receive the Arduino data point
        arduinoData_string = ser.readline().decode('ascii')  # Decode receive Arduino data as a formatted string
        #print(i)                                           # 'i' is a incrementing variable based upon frames = x argument

        try:
            arduinoData_float = float(arduinoData_string)  # Convert to float
            dataList.append(arduinoData_float)  # Add to the list holding the fixed number of points to animate

        except:  # Pass if data point is bad
            pass

        dataLis…
[24:19, 12/23/2022] Shehryar: import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


class AnimationPlot:

    def animate(self, i, dataList, ser):

        ser.write(b'x')  # Transmit the char 'g' to receive the Arduino data point
        arduinoData_string = ser.readline().decode('ascii')  # Decode receive Arduino data as a formatted string
        #print(i)                                           # 'i' is a incrementing variable based upon frames = x argument

        try:
            arduinoData_float = float(arduinoData_string)  # Convert to float
            dataList.append(arduinoData_float)  # Add to the list holding the fixed number of points to animate

        except:  # Pass if data point is bad
            pass

        dataList = dataList[-500000:]  # Fix the list size so that the animation plot 'window' is x number of points

        ax.clear()  # Clear last data frame

        self.getPlotFormat()
        ax.plot(dataList)  # Plot new data frame

    def getPlotFormat(self):
        ax.set_ylim([-1200000, 1200000])  # Set Y axis limit of plot
        ax.set_title("Real Time Arduino Data")  # Set title of figure
        ax.set_ylabel("Value")  # Set title of y axis


dataList = []  # Create empty list variable for later use

#fig, axs = plt.subplots(4)


fig = plt.figure()  # Create Matplotlib plots fig is the 'higher level' plot window
ax = fig.add_subplot(441)  # Add subplot to main fig window
#plt.scatter(x,y)
#ax = fig.add_subplot(412)







#fig.add_subplot(221)   #top left
fig.add_subplot(442).set_title('2nd graph')  #top right
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
xpoints = np.array([0,12000])
ypoints = np.array([-1000, 1000])



fig.add_subplot(443).set_title('2nd graph')  #bottom left
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")


fig.add_subplot(444).set_title('2nd graph')   #bottom right
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")


fig.add_subplot(445).set_title('power ')   #bottom right
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")


fig.add_subplot(446)   #bottom right
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")


fig.add_subplot(447)   #bottom right
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")


fig.add_subplot(448)   #bottom right
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")


fig.add_subplot(449)   #bottom right
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")



fig.add_subplot(4,4,10)   #bottom right
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")


fig.add_subplot(4,4,11)   #bottom right
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")


fig.add_subplot(4,4,12)   #bottom right
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")



fig.add_subplot(4,4,13)   #bottom right
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")


fig.add_subplot(4,4,14)   #bottom right
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")



fig.add_subplot(4,4,15)   #bottom right
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")


fig.add_subplot(4,4,16)   #bottom right
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")


fig.tight_layout()
plt.xlabel("Currrent")
plt.ylabel("Power")




realTimePlot = AnimationPlot()

ser = serial.Serial("COM5", 9600)  # Establish Serial object with COM port and BAUD rate to match Arduino Port/rate
time.sleep(2)  # Time delay for Arduino Serial initialization

# Matplotlib Animation Fuction that takes takes care of real time plot.
# Note that 'fargs' parameter is where we pass in our dataList and Serial object.
ani = animation.FuncAnimation(fig, realTimePlot.animate, frames=100, fargs=(dataList, ser), interval=100)

plt.show()  # Keep Matplotlib plot persistent on screen until it is closed
ser.close()