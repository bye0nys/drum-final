import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import wave

filename = "Kick05.wav"
rate, data = wav.read(filename)
original = wave.open(filename, 'rb')
nChannel = original.getnchannels()
original.close()

if nChannel == 2:
    data0 = data[:, 0]
    spectre = np.fft.fft(data0)
    freq = np.fft.fftfreq(data0.size, 1/rate)
    mask = 0 < freq
    plt.title(filename + "stereo '.wav' FFT")
else:
    spectre = np.fft.fft(data)
    freq = np.fft.fftfreq(data.size, 1/rate)
    mask = 0 < freq
    plt.title(filename + "mono '.wav' FFT")

plt.plot(freq[mask], np.abs(spectre[mask]))
plt.xlabel('freq')
plt.ylabel('amp')
plt.xlim(0, 1000)
plt.grid()
plt.show()
