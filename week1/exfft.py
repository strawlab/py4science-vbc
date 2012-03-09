import numpy as np
import matplotlib.pyplot as plt

from scipy.io import wavfile
from getfile import get_from_strawlab

rate,data = wavfile.read(get_from_strawlab("week1/sirentone.wav"))
left = data[:,1]

nsamps = len(left)
t = np.arange(nsamps, dtype=float) / rate

plt.plot(t, left) #plot in time domain

xfreq = np.fft.fft(left)
fft_freqs = np.fft.fftfreq(nsamps, d=1./rate)

plt.figure()      #plot in freq domain
plt.loglog(fft_freqs[0:nsamps/2], np.abs(xfreq)[0:nsamps/2])

plt.figure()
plt.specgram(data[:,1])

plt.show()
