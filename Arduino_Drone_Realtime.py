import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(i, pitch_command_arr, pitch_value_arr, pitch_error_arr, ser):
    # Read a line from the serial monitor and decode it
    ser.write(b'1')
    
    serial_data = ser.readline().decode('ascii').strip()

    # Split the data by commas and convert to float (double) values
    values = [float(value) for value in serial_data.split(',')]

    if len(values) == 5:
        # Unpack the list of values into individual variables
        Kp, Ki, Kd, pitch_value, pitch_command = values

        print(f"Values: {pitch_command}, {pitch_value}, {Kp}, {Ki}, {Kd}")
    else:
        print("Incorrect number of values received.")

    pitch_command_arr.append(pitch_command)
    pitch_value_arr.append(pitch_value)
    pitch_error = pitch_command - pitch_value
    pitch_error_arr.append(pitch_error)
    
    # Fix the list size so that the animation plot 'window' is x number of points
    pitch_command_arr = pitch_command_arr[-50:]
    pitch_value_arr = pitch_value_arr[-50:]
    pitch_error_arr = pitch_error_arr[-50:]
    
    # Clear the last data frame
    ax1.clear()
    ax2.clear()
    
    # Plot new data frame on the upper subplot
    ax1.plot(pitch_command_arr, color='red', label='Pitch Command')
    ax1.plot(pitch_value_arr, color='blue', label='Pitch Value')
    ax1.set_title("Pitch Command and Pitch Value")
    ax1.set_ylabel("Pitch")
    ax1.set_ylim(-90, 90)
    ax1.legend()
    
    # Plot new data frame on the lower subplot
    ax2.plot(pitch_error_arr, color='green', label='Pitch Error')
    ax2.set_title("Pitch Error")
    ax2.set_ylabel("Error")
    ax2.set_xlabel("Time")
    ax2.set_ylim(-60, 60)
    ax2.legend()

    
# Create empty list variables for later use
pitch_command_arr = []
pitch_value_arr = []
pitch_error_arr = []

# Create Matplotlib plots
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

# Establish Serial object with COM port and BAUD rate to match Arduino Port/rate
ser = serial.Serial("COM3", 115200)

# Time delay for Arduino Serial initialization 
time.sleep(2)

# Matplotlib Animation Function that takes care of real-time plot
# Note that 'fargs' parameter is where we pass in our arrays and Serial object. 
ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(pitch_command_arr, pitch_value_arr, pitch_error_arr, ser), interval=20)

# Keep Matplotlib plot persistent on screen until it is closed
plt.show()

# Close Serial connection when plot is closed
ser.close()
