'''
Using SciPy to do FFT
Version 0.1 - 01/10/2022
Alex Anderson
'''
# import scipy modules we need
from scipy.fft import fft, fftfreq

# we'll use numpy to generate a signal
import numpy as np
from matplotlib import pyplot as plt

SAMPLE_RATE = 44100     # Hertz
DURATION = 5            # Seconds

# method for creating a sine wave
def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)    # returns evenly spaced samples over the interval
    frequencies = x * freq
    # 2*pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

# generate a 2 hertz sine wave that lasts for 5 seconds
x, y = generate_sine_wave(2, SAMPLE_RATE, DURATION)
plt.plot(x, y)
plt.show()

# generate two audio signals
_, nice_tone = generate_sine_wave(400, SAMPLE_RATE, DURATION)
_, noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
noise_tone = noise_tone * 0.3   # multiply by 0.3 to reduce power

# add the signals together
mixed_tone = nice_tone + noise_tone

# normalization; target format is a 16-bit integer which has a range from -32768 to 32767
normalized_tone = np.int16( (mixed_tone / mixed_tone.max()) * 3267)

plt.plot(normalized_tone[:1000])
plt.show()

# number of samples in normalized tone
N = SAMPLE_RATE * DURATION      # Samples = Samples/second * seconds

yf = fft(normalized_tone)
xf = fftfreq(N, 1/ SAMPLE_RATE)

plt.plot(xf, np.abs(yf))
plt.show()