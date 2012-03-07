import numpy as np
import matplotlib.pyplot as plt

from scipy.io import wavfile
from getfile import get_from_strawlab

rate,data = wavfile.read(get_from_strawlab("week1/sirentone.wav"))

plt.specgram(data[:,1])
plt.show()
