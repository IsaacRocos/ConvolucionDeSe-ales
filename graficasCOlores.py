import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi)
offsets = np.linspace(0, 2*np.pi, 4, endpoint=False)
# Create array with shifted-sine curve along each column
yy = np.transpose([np.sin(x + phi) for phi in offsets])

offsets2 = np.linspace(0, 2*np.pi, 50, endpoint=False)
w = np.sin(offsets2)
w2 = np.cos(offsets2)

plt.rc('lines', linewidth=4)

fig, (ax0, ax1)  = plt.subplots(nrows=2)

plt.rc('axes', color_cycle=['r', 'g', 'b', 'y'])
ax0.plot(offsets2, w)
ax0.plot(offsets2,w2)
ax0.set_title('Entradas')

ax1.set_color_cycle(['c', 'm', 'y', 'k'])
ax1.plot(yy)
ax1.set_title('Set axes color cycle to cmyk')

# Tweak spacing between subplots to prevent labels from overlapping
plt.subplots_adjust(hspace=0.3)
plt.show()