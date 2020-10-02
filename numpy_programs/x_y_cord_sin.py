#Write a NumPy program to compute the x and y coordinates for points on a sine curve

# and plot the points using matplotlib.
 import numpy as np
 import numpy as pi
 import matplotlib.pyplot as plt
 
 x=np.arange(0,2*np.pi,0.2)
 y=np.sin(x)
 plt.plot(x,y)
