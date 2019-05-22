from __future__ import print_function, division
import wave
import numpy as np
import matplotlib.pyplot as plt

wr = wave.open('Snare.wav', 'r')
sz = wr.getframerate()
q = 5  # time window to analyze in seconds
c = 12  # number of time windows to process
sf = 1.5  # signal scale factor

for num in range(c):
    print('Processing from {} to {} s'.format(num*q, (num+1)*q))
    avgf = np.zeros(int(sz / 2) + 1)
    snd = np.array([])
    # The sound signal for q seconds is concatenated. The fft over that
    # period is averaged to average out noise.
    for j in range(q):
        da = np.fromstring(wr.readframes(sz), dtype=np.int16)
        left, right = da[0::2]*sf, da[1::2]*sf
        lf, rf = abs(np.fft.rfft(left)), abs(np.fft.rfft(right))
        snd = np.concatenate((snd, (left+right)/2))
        avgf += (lf + rf) / 2

    avgf /= q
    # Plot both the signal and frequencies.
    plt.figure(1)
    a = plt.subplot(2, 1, 1)  # signal
    r = 2**16/2
    a.set_ylim([-r, r])
    a.set_xlabel('time [s]')
    a.set_ylabel('signal [-]')
    x = np.arange(44100*q)/44100
    plt.plot(x, snd)
    b = plt.subplot(212)  # frequencies
    b.set_xscale('log')
    b.set_xlabel('frequency [Hz]')
    b.set_ylabel('|amplitude|')
    plt.plot(abs(avgf))
    plt.savefig('simple{:02d}.png'.format(num))
    plt.clf()
    plt.show()

