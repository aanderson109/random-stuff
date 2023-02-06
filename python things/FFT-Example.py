import numpy as np
import matplotlib.pyplot as plt

Fs = 1      # Hz
N = 100     # Number of points to simulate and our FFT size

# create a random signal in the time domain (sine wave 0.15 Hz, sample rate 1Hz)
t = np.arange(100)
s = np.sin(0.15*2*np.pi*t)

# shifted FFT of our generated signal
S = np.fft.fftshift(np.fft.fft(s))

# calculate the magnitude and phase to cut down on the complex array
S_mag = np.abs(S)           # magnitude of a complex number
S_phase = np.angle(S)       # function to find phase
f = np.arange(Fs/-2, Fs/2, Fs/N)
plt.figure(0)
plt.plot(f, S_mag, '.-')    # plot of the FFT of signal magnitude
plt.figure(1)
plt.plot(f, S_phase, '.-')  # plot of the FFT of signal phase
plt.show()