import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import wave
import sounddevice as sd
import glob
import os.path

myPath = 'C:/python/kkmmoouu/fft/wavsamples/realuse/roop2/why'
myExt = '*.wav'
freqframe = []
frqs = [70, 104, 150, 3700, 3260, 6813]

for filename in glob.glob(os.path.join(myPath, myExt)):
    rate, data0 = wav.read(filename)
    data1 = data0
    original = wave.open(filename, 'rb')
    nChannel = original.getnchannels()
    length = original.getnframes()
    original.close()

    if nChannel == 2:
        data2 = data0[:, 0]
        spectre = np.fft.fft(data2)
        freq = np.fft.fftfreq(data2.size, 1/rate)
        mask = 0 < freq
    else:
        spectre = np.fft.fft(data0)
        freq = np.fft.fftfreq(data0.size, 1 / rate)
        mask = 0 < freq

    maxamp = np.abs(np.max(spectre[mask]))

    #보통 500만대고 317만이 최소다 250만 ㄱㄱ
    #sliding window 써보자
    # sliding window
     #avgspectre = []
     #slicerange = 300
     #for i in range(0, np.alen(freq)-(slicerange*2), slicerange):
     #    j = i
     #    spectresum = 0
     #    for j in range(j, j+((slicerange*2)-1), 1):
     #        spectresum = spectresum + np.abs(int(spectre[j]))
     #
     #    avgspectre.append(spectresum/200)
     #
     #for i in range(0, np.alen(freq) - (slicerange*2), slicerange):
     #    j = i
     #    for j in range(j, j+((slicerange*2)-1), 1):
     #        spectre[j] = avgspectre[int(i/slicerange)]

    masks = freq[mask]
    number = 0
    frews = []

    for mask in masks:

        number = number + 1
        if np.abs(spectre[number]) == maxamp:
            maxfreq = round(freq[number], 2)

        if freq[number] < 2000:
            if spectre[number] < 3000000:
                spectre[number] = 0
                freq[number] = 0
        else:
            if spectre[number] < 450000:
                spectre[number] = 0
                freq[number] = 0
        spectre[number] = 0

        for num in range(0, 3):
            if freq[number] > 0:
                if abs(abs(frqs[num]) - freq[number]) < 7:
                    frews.append(frqs[num])

        for num in range(3, 6):
            if freq[number] > 0:
                if abs(abs(frqs[num]) - freq[number]) < 20:
                    frews.append(frqs[num])

    plt.title(filename + " " + np.str(maxfreq) + " hz")
    f = set(frews)
    print(f)

   # plt.title(filename + " " + np.str(maxfreq) + " hz, amp = " + np.str(maxamp))
    #freqframe.append((maxfreq))

    plt.plot(freq, np.abs(spectre), '.')
    plt.xlabel('freq')
    plt.ylabel('amp')
    plt.xlim(0, 10000)
    plt.ylim(0)
    plt.grid()
    plt.show()