import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import wave
import glob
import os.path

myPath = 'C:/python/kkmmoouu/fft/wavsamples/realuse/roop2/why'
myExt = '*.wav'
freqframe = []
frqs = [70, 104, 150, 3700, 3260, 6813]

for filename in glob.glob(os.path.join(myPath, myExt)):
    rate, data0 = wav.read(filename)
    data1 = np.full(np.alen(data0), 0)
    data2 = np.full(np.alen(data0), 0)
    data1 = np.array(data0)
    times = np.arange(len(data0)) / float(rate)
    original = wave.open(filename, 'rb')
    nChannel = original.getnchannels()
    length = original.getnframes()
    original.close()
    type(data1)

    if nChannel == 2:
        data2 = data0[:, 0]

    #보통 500만대고 317만이 최소다 250만 ㄱㄱ
    # sliding window
    avgdata = []
    slicerange = 200
    data00 = np.full(np.alen(data0), 0)

    if nChannel == 2:
        data1 = data2

    for i in range(0, np.alen(data1)-(slicerange*2), slicerange):
        if nChannel == 2:
            j = i
        datasum = 0
        for j in range(j, j+((slicerange*2)-1), 1):
            datasum = datasum + np.abs(int(data1[j]))

        avgdata.append(datasum/slicerange)

    for i in range(0, np.alen(data1) - (slicerange*2), slicerange):
        j = i
        for j in range(j, j+((slicerange*2)-1), 1):
            data00[j] = avgdata[(int(i/slicerange))].copy()

    ccount = [[0 for j in range(len(data00))] for i in range(300)]
    i = 0
    j = 0
    for num in range(0, len(data00)):
        if data00[num] < 2500:
            data00[num] = 0

    for num in range(0, len(data1)):
        if data00[num] != 0:
            ccount[i][j] = data1[num]
            j = j + 1
        elif (data00[num] == 0) & (data00[num-1] != 0):
            i = i + 1
            j = 0

    for num in range(0, 300):
        for number in range(0, ccount[num].count(0)):
            ccount[num].pop()

    #plt.plot(times, count[0])
    #plt.plot(times, count[1])
    #plt.show()

    if nChannel == 2:
        data1 = ccount[0]
        spectre = np.fft.fft(data1)
        freq = np.fft.fftfreq(len(data1), 1/rate)
        mask = 0 < freq
    else:
        data1 = ccount[0]
        spectre = np.fft.fft(data1)
        freq = np.fft.fftfreq(len(data1), 1 / rate)
        mask = 0 < freq

    maxamp = np.abs(np.max(spectre[mask]))

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
                if abs(abs(frqs[num]) - freq[number]) < 40:
                    frews.append(frqs[num])

    plt.title(filename + " " + np.str(maxfreq) + " hz")
    f = set(frews)
    print(f)

    print(np.alen(ccount[0]))
    print(np.alen(ccount[1]))
    print(np.alen(ccount[2]))
    print(np.alen(ccount[3]))
    print(np.alen(ccount[4]))
    print(np.alen(ccount[5]))
    print(np.alen(ccount[6]))
    print(np.alen(ccount[7]))
   # plt.title(filename + " " + np.str(maxfreq) + " hz, amp = " + np.str(maxamp))
    #freqframe.append((maxfreq))

    #plt.plot(freq, np.abs(spectre), '.')
    plt.xlabel('freq')
    #plt.ylabel('amp')
    plt.xlim(0, 10000)
    #plt.ylim(0)
    plt.grid()
    #plt.show()

plt.plot(freq, np.abs(spectre), '.')
plt.show()
