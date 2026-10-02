import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation  
N=100
#define the timesteps that brekas up the figure
t=np.linspace(0,2*np.pi,100,endpoint=False)   
#define x, y coordinates for the Tusi Couple(oscillating)  
x=np.cos(t)
y=np.zeroes_like(t) #this assigns 0 to all values of y(t) nad has a 1D shape
z=x+1j*y    #define horizontal straight line with harmonic motion
#dividing by n normalizes the coefficients for fourier convention
coeff=np.fft.fft(z)/N
n=np.fft.fftfreq(N,d=1/N)    #n=frequency
v=coeff*np.exp(1j*n*t)
reconstruct=np.zeroes(N,dtype=complex)
for c, freq in zip(coeff, n):
  reconstructed+=c*np.exp(1j*n*t)

