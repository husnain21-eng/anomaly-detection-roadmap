import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 60, 3000)
x = np.sin(t) + np.sin(np.sqrt(2) * t)

dt = t[1] - t[0]
spectrum = np.abs(np.fft.rfft(x))
omega = 2 * np.pi * np.fft.rfftfreq(len(x), d=dt)

plt.figure(figsize=(10, 5))
plt.plot(omega, spectrum)
plt.xlim(0, 3)
plt.title("FFT spectrum of sin(t) + sin(sqrt(2) t)")
plt.xlabel("Angular frequency (omega)")
plt.ylabel("Amplitude")
plt.tight_layout()

plt.savefig("day31_plot.png")
plt.show()

# Print the tallest peak in each region
low = (omega > 0.5) & (omega < 1.2)
high = (omega > 1.2) & (omega < 2.0)
print("Peak 1 near:", round(omega[low][np.argmax(spectrum[low])], 2))
print("Peak 2 near:", round(omega[high][np.argmax(spectrum[high])], 2))