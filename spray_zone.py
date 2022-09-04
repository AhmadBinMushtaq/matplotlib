import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

#Calculation Parameters
t0 = 0 # Starting time (Seconds)
t_end = 60 # Ending time (Seconds)
dt = 0.04 # increment value for time
paths = (64,64,64,88,88,32,32,32,32,16) # Length of each path
drag = (0.350317,-0.202576,0)
lift = (0.0350823,0.00372739,0)
mass = 6.9
power = (0.0000373344395,0.109504955,0)
