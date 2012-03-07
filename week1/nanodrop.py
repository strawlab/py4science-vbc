import numpy as np
import matplotlib.pyplot as plt

import getfile

STATE_SKIP, _, STATE_SPEC_NAME, STATE_SPEC_DATE, _, STATE_DATA = range(6)
FREQ_FROM, FREQ_TO = 190, 841

spectrum_names = []
def func():
  state = STATE_SPEC_NAME
  for line in open(getfile.get_from_strawlab("week1/nanodrop-spectra.tsv")):
      if state == STATE_SPEC_NAME:
          spectrum_names.append(line.strip())
      elif state == STATE_DATA:
          wavelength, absorbance = line.strip().split()
          yield absorbance
          if int(wavelength) == (FREQ_TO-1):
              state = STATE_SKIP
          continue
      state += 1
data = np.fromiter(func(), float)

wavelengths = np.arange(FREQ_FROM, FREQ_TO)
spectra = data.reshape(len(spectrum_names),FREQ_TO - FREQ_FROM).transpose()

plt.plot(wavelengths, spectra)
plt.legend(spectrum_names, loc=4)
plt.show()

