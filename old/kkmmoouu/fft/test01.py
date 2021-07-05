import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
from pydub import AudioSegment

sound = AudioSegment.from_wav("Test.wav")
sound = sound.set_channels(1)
sound.export("out_Test.wav", format="wav")

spf = wave.open('out_Test.wav', 'r')

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, dtype=np.int16)
framerate = spf.getframerate()

# If Stereo
if spf.getnchannels() == 2:
    print
    'Just mono files'
    sys.exit(0)

Time = np.linspace(0, len(signal)/framerate, num=len(signal))

plt.figure(1)
plt.title('Signal Wave...')
plt.plot(Time, signal)
plt.show()
