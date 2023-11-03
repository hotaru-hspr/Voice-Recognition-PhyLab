import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Read the audio file (replace with the correct file path)

#Cow
sample_rate, audio_data = wavfile.read(r"C:\Users\pavit\Downloads\Inek\inek_8.wav")
# sample_rate, audio_data = wavfile.read(r"C:\Users\pavit\Downloads\Inek")
# sample_rate, audio_data = wavfile.read(r"C:\Users\pavit\Downloads\Kedi-Part1")
# sample_rate, audio_data = wavfile.read(r"C:\Users\pavit\Downloads\Kedi-Part2")
# sample_rate, audio_data = wavfile.read(r"C:\Users\pavit\Downloads\Kopek-Part1")
# sample_rate, audio_data = wavfile.read(r"C:\Users\pavit\Downloads\Kopek-Part2")
# sample_rate, audio_data = wavfile.read(r"C:\Users\pavit\Downloads\Koyun")
# sample_rate, audio_data = wavfile.read(r"C:\Users\pavit\Downloads\Maymun")



n = len(audio_data)
frequencies = np.fft.fftfreq(n, 1 / sample_rate)
audio_fft = np.fft.fft(audio_data)
positive_frequencies = frequencies[:n // 2]
magnitude_spectrum = np.abs(audio_fft[:n // 2])

plt.figure(figsize=(10, 6))
plt.plot(positive_frequencies, magnitude_spectrum)
plt.title("Fourier Transform of Audio Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()
plt.show()