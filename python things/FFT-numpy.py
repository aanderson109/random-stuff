from numpy.fft import fft, ifft
import matplotlib.pyplot as plt
import numpy as np


'''
First block here is to generate a signal for analysis
'''
plt.style.use('seaborn-poster')

#sampling rate
sr = 2000

#sampling interval
ts = 1.0/sr
t = np.arange(0,1,ts)

freq = 1.
x = 3*np.sin(2*np.pi*freq*t)

freq = 4
x += np.sin(2*np.pi*freq*t)

freq = 7
x += 0.5*np.sin(2*np.pi*freq*t)

plt.figure(figsize = (8, 6))
plt.plot(t, x, 'r')
plt.ylabel('Amplitude')
#plt.show()

'''
Now we use the fft and ifft functions form numpy to calculate the FFT
'''
X = fft(x)
N = len(X)
n = np.arange(N)
T = N/sr 
freq = n/T

plt.figure(figsize = (12,6))
plt.subplot(121)

plt.stem(freq, np.abs(X), 'b', \
    markerfmt=" ", basefmt="-b")
plt.xlabel('Freq(Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.xlim(0, 10)

plt.subplot(122)
plt.plot(t, ifft(X), 'r')
plt.xlabel("time (s)")
plt.ylabel('amplitude')
plt.tight_layout()
plt.show()