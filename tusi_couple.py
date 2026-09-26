import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation  
#define the timesteps that brekas up the figure
t=np.linspace(0,2*np.pi,100,endpoint=False)   
#define x, y coordinates for the Tusi Couple(oscillating)  
x=np.cos(t)
y=np.zeroes_like(t) #this assigns 0 to all values of y(t) nad has a 1D shape
z=x+1j*y    #define horizontal straight line with harmonic motion
fcap=np.fft.fft(z)
speeds=np.round(np.fft.fftfreq(N) * N).astype(int)
radii=np.abs(fcap)/N
angles=np.angle(fcap)
mask=radii > 1e-5
#filtering the useless frequencies
speeds=speeds[mask]
radii=radii[mask]
angles=angles[mask]
#sorting circles from small to big
sortnp=np.argsort(radii)[::-1]
speeds, radii, angles=speeds[idx], radii[idx], angles[idx]

"""Matplotlib????????"""

fig, ax=plt.subplots(figsize=(6,6))

