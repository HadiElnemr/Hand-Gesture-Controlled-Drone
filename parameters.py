import numpy as np

# fingers configs
track_hand = [1,0,0,0,0]
up = [0,1,0,0,0]
down = [0,1,1,0,0]
idle = [0,1,1,1,0]
exit = [0,0,0,0,1]

# define the black colour BGR boundaries
# For black colour
lower = [0, 0, 0]
upper = [60, 60, 60]
# # For Red colour
# lower = [0, 0, 0]
# upper = [25, 25, 250]

# create NumPy arrays from the boundaries
lower = np.array(lower, dtype = "uint8")
upper = np.array(upper, dtype = "uint8")
