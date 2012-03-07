import scipy.misc
import matplotlib.pyplot as plt

import getfile

im = scipy.misc.imread(getfile.get_from_strawlab("week1/lena-gray.png"))
plt.imshow(im)
plt.colorbar()

plt.show()
