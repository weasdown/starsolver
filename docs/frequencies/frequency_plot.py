# Plot of frequency components for the Easy #1 board from the Star Battle app.

import matplotlib.pyplot as plt

frequency_components = [2 ** i for i in range(9)]
print(f'{frequency_components = }')

coefficients = [130, 40, 257, 80, 5, 160, 10, 320, 20]
print(f'{coefficients = }')

ax = plt.axes()
plt.plot(frequency_components, coefficients)
plt.title('Frequency plot for solved Easy #1 board')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Coefficient')
ax.set_xscale('log', base=2)

plt.show()
