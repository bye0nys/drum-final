import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import wave
import glob
import os.path
import cv2
import sounddevice as sd

# 음원 불러오기
myPath = 'C:/python/samples/realuse/roop2/why'
myExt = '*.wav'
freqframe = []
frqs = [70, 104, 158, 3260, 3700, 6813]
# 70   104 158   3260  3700  6813
# kick tom snare ride crash hihat

def bubblesort(li):
    list_length = len(li)
    for i in range(list_length-1):
        for j in range(list_length-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

# 이미지 불러오기 (한가지 악기)
default = cv2.imread("C:/drum/default.png",cv2.IMREAD_REDUCED_COLOR_4)
crash = cv2.imread("C:/drum/1/crash.png", cv2.IMREAD_REDUCED_COLOR_4)
ride = cv2.imread("C:/drum/1/ride.png", cv2.IMREAD_REDUCED_COLOR_4)
hihat = cv2.imread("C:/drum/1/hihat.png", cv2.IMREAD_REDUCED_COLOR_4)
tom = cv2.imread("C:/drum/1/tom.png", cv2.IMREAD_REDUCED_COLOR_4)
kick = cv2.imread("C:/drum/1/kick.png", cv2.IMREAD_REDUCED_COLOR_4)
snare = cv2.imread("C:/drum/1/snare.png", cv2.IMREAD_REDUCED_COLOR_4)

# 이미지 불러오기 (두가지 악기)
crashride = cv2.imread("C:/drum/2/crash ride.png", cv2.IMREAD_REDUCED_COLOR_4)
hihatcrash = cv2.imread("C:/drum/2/hihat crash.png", cv2.IMREAD_REDUCED_COLOR_4)
hihatride = cv2.imread("C:/drum/2/hihat ride.png", cv2.IMREAD_REDUCED_COLOR_4)
kickcrash = cv2.imread("C:/drum/2/kick crash.png", cv2.IMREAD_REDUCED_COLOR_4)
kickhihat = cv2.imread("C:/drum/2/kick hihat.png", cv2.IMREAD_REDUCED_COLOR_4)
kickride = cv2.imread("C:/drum/2/kick ride.png", cv2.IMREAD_REDUCED_COLOR_4)
snarecrash = cv2.imread("C:/drum/2/snare crash.png", cv2.IMREAD_REDUCED_COLOR_4)
snarehihat = cv2.imread("C:/drum/2/snare hihat.png", cv2.IMREAD_REDUCED_COLOR_4)
snarekick = cv2.imread("C:/drum/2/snare kick.png", cv2.IMREAD_REDUCED_COLOR_4)
snareride = cv2.imread("C:/drum/2/snare ride.png", cv2.IMREAD_REDUCED_COLOR_4)
snaretom = cv2.imread("C:/drum/2/snare tom.png", cv2.IMREAD_REDUCED_COLOR_4)
tomcrash = cv2.imread("C:/drum/2/tom crash.png", cv2.IMREAD_REDUCED_COLOR_4)
tomhihat = cv2.imread("C:/drum/2/tom hihat.png", cv2.IMREAD_REDUCED_COLOR_4)
tomkick = cv2.imread("C:/drum/2/tom kick.png", cv2.IMREAD_REDUCED_COLOR_4)
tomride = cv2.imread("C:/drum/2/tom ride.png", cv2.IMREAD_REDUCED_COLOR_4)

# 이미지 불러오기 (세가지 악기)
kickcrashride = cv2.imread("C:/drum/3/kick crash ride.png", cv2.IMREAD_REDUCED_COLOR_4)
kickhihatcrash = cv2.imread("C:/drum/3/kick hihat crash.png", cv2.IMREAD_REDUCED_COLOR_4)
kickhihatride = cv2.imread("C:/drum/3/kick hihat ride.png", cv2.IMREAD_REDUCED_COLOR_4)
kicksnarecrash = cv2.imread("C:/drum/3/kick snare crash.png", cv2.IMREAD_REDUCED_COLOR_4)
kicksnarehihat = cv2.imread("C:/drum/3/kick snare hihat.png", cv2.IMREAD_REDUCED_COLOR_4)
kicksnareride = cv2.imread("C:/drum/3/kick snare ride.png", cv2.IMREAD_REDUCED_COLOR_4)
kicksnaretom = cv2.imread("C:/drum/3/kick snare tom.png", cv2.IMREAD_REDUCED_COLOR_4)
kicktomcrash = cv2.imread("C:/drum/3/kick tom crash.png", cv2.IMREAD_REDUCED_COLOR_4)
kicktomhihat = cv2.imread("C:/drum/3/kick tom hihat.png", cv2.IMREAD_REDUCED_COLOR_4)
kicktomride = cv2.imread("C:/drum/3/kick tom ride.png", cv2.IMREAD_REDUCED_COLOR_4)

#파일을 불러와서 rate, data에 저장
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

# stereo 전용 변수 할당 (data2)
    if nChannel == 2:
        data2 = data0[:, 0]
        data1 = data2

# sliding window
    avgdata = []
    slicerange = 300
    data00 = np.full(np.alen(data0), 0)

    for i in range(0, np.alen(data0) - (slicerange * 2), int(slicerange / 4)):
        j = i
        datasum = 0
        for j in range(j, j + (slicerange - 1), 1):
            datasum = datasum + np.abs(int(data1[j]))

        avgdata.append(datasum / int(slicerange / 4))

    for i in range(0, np.alen(data0) - (slicerange * 2), int(slicerange / 4)):
        j = i
        for j in range(j, j + (slicerange - 1), 1):
            data00[j] = avgdata[int(i / (slicerange / 4))].copy()

# fft할 구간 ccount로 설정
    ccount = [[0 for j in range(len(data00))] for i in range(300)]
    i = 0
    j = 0

# 374보다 작으면 진폭 0으로 설정 (잡음 제거)
    for num in range(0, len(data00)):
        if data00[num] < 374:
            data00[num] = 0

# 한 리듬의 시작시간, 끝시간 설정
    starttime = []
    endtime = []
    for num in range(0, len(data1)):
        if data00[num] != 0:
            ccount[i][j] = data1[num]
            j = j + 1
            if data00[num-1] == 0:
                starttime.append(num)
        elif (data00[num] == 0) & (data00[num-1] != 0):
            i = i + 1
            j = 0
            endtime.append(num)
    starttime.append(len(times) - 1)
    #print(len(starttime))
    #print(len(endtime))

# 2차원 배열 r 생성 (행 : 리듬 갯수, 열 : 최대악기 3개니까 3)
    rhythmcount = i
    r = [[] for i in range(rhythmcount)]
    #print(i)

# 리듬 사이의 유지시간 탐지
    defaulttime = [[] for i in range(rhythmcount + 1)]
    playtime = [[] for i in range(rhythmcount)]

    for j in range(1, rhythmcount + 1):
        defaulttime[j - 1] = round(times[starttime[j]]-times[endtime[j - 1]], 3)

    for j in range(0, rhythmcount):
        playtime[j] = round(times[endtime[j]]-times[starttime[j]], 3)

# ccount 배열의 0 제거
    for num in range(0, 300):
        for number in range(0, ccount[num].count(0)):
            ccount[num].pop()

# fft 실행
    k = 0
    for x in range(i):
        if nChannel == 2:
            data1 = ccount[x]
            spectre = np.fft.fft(data1)
            freq = np.fft.fftfreq(len(data1), 1/rate)
            mask = 0 < freq
        #    plt.plot(freq, np.abs(spectre), '.')
        #    plt.show()
        else:
            data1 = ccount[x]
            spectre = np.fft.fft(data1)
            freq = np.fft.fftfreq(len(data1), 1 / rate)
            mask = 0 < freq
        #    plt.plot(freq, np.abs(spectre), '.')
        #    plt.show()

        maxamp = np.abs(np.max(spectre[mask]))

        masks = freq[mask]
        number = 0
        frews = []

# 변환 후 값 처리
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
                    if abs(abs(frqs[num]) - freq[number]) < 8:
                        frews.append(frqs[num])

            for num in range(3, 6):
                if freq[number] > 0:
                    if abs(abs(frqs[num]) - freq[number]) < 50:
                        frews.append(frqs[num])

# 2차원 배열에 탐지한 주파수값 저장 (r배열)
        plt.title(filename + " " + np.str(maxfreq) + " hz")
        f = set(frews)
        f1 = list(f)
        r[k] = f1
        k = k + 1

    for num in range(rhythmcount):
        bubblesort(r[num])
    #print(r)

        #r[k]
        #print(f)
        #print(f1)
        #print(len(f1))
        #print(f1[0])

       # plt.title(filename + " " + np.str(maxfreq) + " hz, amp = " + np.str(maxamp))
        #freqframe.append((maxfreq))

        #plt.plot(freq, np.abs(spectre), '.')
        #plt.xlabel('freq')
        #plt.ylabel('amp')
        #plt.xlim(0, 10000)
        #plt.ylim(0)
        #plt.grid()
        #plt.show()

        #print(f[0])

    #plt.plot(freq, np.abs(spectre), '.')
    #plt.show()

    sd.play(data0, rate)
    for n in range(0, rhythmcount):
# 1개짜리
        if r[n] == [70]:
            cv2.imshow("drum", kick)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [104]:
            cv2.imshow("drum", tom)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [158]:
            cv2.imshow("drum", snare)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [3260]:
            cv2.imshow("drum", ride)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [3700]:
            cv2.imshow("drum", crash)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [6813]:
            cv2.imshow("drum", hihat)
            cv2.waitKey(int(playtime[n] * 1000))

# 2개짜리
        if r[n] == [70, 104]:
            cv2.imshow("drum", tomkick)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [70, 158]:
            cv2.imshow("drum", snarekick)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [70, 3700]:
            cv2.imshow("drum", kickcrash)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [70, 3260]:
            cv2.imshow("drum", kickride)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [70, 6813]:
            cv2.imshow("drum", kickhihat)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [104, 158]:
            cv2.imshow("drum", snaretom)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [104, 3700]:
            cv2.imshow("drum", tomcrash)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [104, 3260]:
            cv2.imshow("drum", tomride)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [104, 6813]:
            cv2.imshow("drum", tomhihat)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [158, 3700]:
            cv2.imshow("drum", snarecrash)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [158, 3260]:
            cv2.imshow("drum", snareride)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [158, 6813]:
            cv2.imshow("drum", snarehihat)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [3260, 3700]:
            cv2.imshow("drum", crashride)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [3700, 6813]:
            cv2.imshow("drum", hihatcrash)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [3260, 6813]:
            cv2.imshow("drum", hihatride)
            cv2.waitKey(int(playtime[n] * 1000))

# 3개짜리
        if r[n] == [70, 104, 158]:
            cv2.imshow("drum", kicksnaretom)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [70, 104, 3260]:
            cv2.imshow("drum", kicktomride)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [70, 104, 3700]:
            cv2.imshow("drum", kicktomcrash)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [70, 104, 6813]:
            cv2.imshow("drum", kicktomhihat)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [70, 158, 3260]:
            cv2.imshow("drum", kicksnareride)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [70, 158, 3700]:
            cv2.imshow("drum", kicksnarecrash)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [70, 158, 6813]:
            cv2.imshow("drum", kicksnarehihat)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [70, 3260, 3700]:
            cv2.imshow("drum", kickcrashride)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [70, 3260, 6813]:
            cv2.imshow("drum", kickhihatride)
            cv2.waitKey(int(playtime[n] * 1000))

        if r[n] == [70, 3700, 6813]:
            cv2.imshow("drum", kickhihatcrash)
            cv2.waitKey(int(playtime[n] * 1000))

# 비어있는 시간
        if n >= rhythmcount:
            cv2.imshow("drum", default)
            cv2.waitKey(int(defaulttime[n] * 1000))

        if n != rhythmcount:
            cv2.imshow("drum", default)
            cv2.waitKey(int(defaulttime[n] * 1000))

        if len(r[n]) > 3:
            cv2.imshow("drum", default)
            cv2.waitKey(int(playtime[n] * 1000))
