from PIL import Image
import glob
import os.path
import cv2
import sounddevice as sd

myPath = 'C:/python/1/'
myExt = '*.png'

#for filename in glob.glob(os.path.join(myPath, myExt)):
#    im = Image.open(filename)
#    for num in range(0, 10):
#        first = ""
#        second = ".png"
#        abc = first + str(num) + second
#        abcd = os.path.join(myPath, abc)
#        print(abcd)
#        im.save(abcd)

default = cv2.imread("C:/Users/변윤석/Desktop/drum/default.png",cv2.IMREAD_REDUCED_COLOR_4)
crash = cv2.imread("C:/Users/변윤석/Desktop/drum/1/crash.png", cv2.IMREAD_REDUCED_COLOR_4)
ride = cv2.imread("C:/Users/변윤석/Desktop/drum/1/ride.png", cv2.IMREAD_REDUCED_COLOR_4)
hihat = cv2.imread("C:/Users/변윤석/Desktop/drum/1/hihat.png", cv2.IMREAD_REDUCED_COLOR_4)
tom = cv2.imread("C:/Users/변윤석/Desktop/drum/1/tom.png", cv2.IMREAD_REDUCED_COLOR_4)
kick = cv2.imread("C:/Users/변윤석/Desktop/drum/1/kick.png", cv2.IMREAD_REDUCED_COLOR_4)
snare = cv2.imread("C:/Users/변윤석/Desktop/drum/1/snare.png", cv2.IMREAD_REDUCED_COLOR_4)
crashride = cv2.imread("C:/Users/변윤석/Desktop/drum/2/crash ride.png", cv2.IMREAD_REDUCED_COLOR_4)
hihatcrash = cv2.imread("C:/Users/변윤석/Desktop/drum/2/hihat crash.png", cv2.IMREAD_REDUCED_COLOR_4)
hihatride = cv2.imread("C:/Users/변윤석/Desktop/drum/2/hihat ride.png", cv2.IMREAD_REDUCED_COLOR_4)
kickcrash = cv2.imread("C:/Users/변윤석/Desktop/drum/2/kick crash.png", cv2.IMREAD_REDUCED_COLOR_4)
kickhihat = cv2.imread("C:/Users/변윤석/Desktop/drum/2/kcik hihat.png", cv2.IMREAD_REDUCED_COLOR_4)
kickride = cv2.imread("C:/Users/변윤석/Desktop/drum/2/kick ride.png", cv2.IMREAD_REDUCED_COLOR_4)
snarecrash = cv2.imread("C:/Users/변윤석/Desktop/drum/2/snare crash.png", cv2.IMREAD_REDUCED_COLOR_4)
snarehihat = cv2.imread("C:/Users/변윤석/Desktop/drum/2/snare hihat.png", cv2.IMREAD_REDUCED_COLOR_4)
snarekick = cv2.imread("C:/Users/변윤석/Desktop/drum/2/snare kick.png", cv2.IMREAD_REDUCED_COLOR_4)
snareride = cv2.imread("C:/Users/변윤석/Desktop/drum/2/snare ride.png", cv2.IMREAD_REDUCED_COLOR_4)
snaretom = cv2.imread("C:/Users/변윤석/Desktop/drum/2/snare tom.png", cv2.IMREAD_REDUCED_COLOR_4)
tomcrash = cv2.imread("C:/Users/변윤석/Desktop/drum/2/tom crash.png", cv2.IMREAD_REDUCED_COLOR_4)
tomhihat = cv2.imread("C:/Users/변윤석/Desktop/drum/2/tom hihat.png", cv2.IMREAD_REDUCED_COLOR_4)
tomkick = cv2.imread("C:/Users/변윤석/Desktop/drum/2/tom kick.png", cv2.IMREAD_REDUCED_COLOR_4)
tomride = cv2.imread("C:/Users/변윤석/Desktop/drum/2/tom ride.png", cv2.IMREAD_REDUCED_COLOR_4)
kickcrashride = cv2.imread("C:/Users/변윤석/Desktop/drum/3/kick crash ride.png", cv2.IMREAD_REDUCED_COLOR_4)
kickhihatcrash = cv2.imread("C:/Users/변윤석/Desktop/drum/3/kick hihat crash.png", cv2.IMREAD_REDUCED_COLOR_4)
kickhihayride = cv2.imread("C:/Users/변윤석/Desktop/drum/3/kick hihat ride.png", cv2.IMREAD_REDUCED_COLOR_4)
kicksnarecrash = cv2.imread("C:/Users/변윤석/Desktop/drum/3/kick snare crash.png", cv2.IMREAD_REDUCED_COLOR_4)
kicksnarehihat = cv2.imread("C:/Users/변윤석/Desktop/drum/3/kick snare hihat.png", cv2.IMREAD_REDUCED_COLOR_4)
kicksnareride = cv2.imread("C:/Users/변윤석/Desktop/drum/3/kick snare ride.png", cv2.IMREAD_REDUCED_COLOR_4)
kicksnaretom = cv2.imread("C:/Users/변윤석/Desktop/drum/3/kick snare tom.png", cv2.IMREAD_REDUCED_COLOR_4)
kicktomcrash = cv2.imread("C:/Users/변윤석/Desktop/drum/3/kick tom crash.png", cv2.IMREAD_REDUCED_COLOR_4)
kicktomhihat = cv2.imread("C:/Users/변윤석/Desktop/drum/3/kick tom hihat.png", cv2.IMREAD_REDUCED_COLOR_4)
kicktomride = cv2.imread("C:/Users/변윤석/Desktop/drum/3/kick tom ride.png", cv2.IMREAD_REDUCED_COLOR_4)

image = cv2.imread("C:/python/1/default.png", cv2.IMREAD_REDUCED_COLOR_4) # cv2.IMREAD_UNCHANGED : 원본 사용
image1 = cv2.imread("C:/python/1/2/crash.png", cv2.IMREAD_REDUCED_COLOR_4)
cv2.imshow("Moon", image) #cv2.imshow("윈도우 창 제목", 이미지)를 이용하여 윈도우 창에 이미지를 띄웁니다.
cv2.waitKey(167) #cv2.waitkey(time)이며 time마다 키 입력상태를 받아옵니다. 0일 경우, 지속적으로 검사하여 해당 구문을 넘어가지 않습니다.
cv2.imshow("Moon", image1)
cv2.waitKey(167)
cv2.imshow("Moon", image) #cv2.imshow("윈도우 창 제목", 이미지)를 이용하여 윈도우 창에 이미지를 띄웁니다.
cv2.waitKey(167)
cv2.imshow("Moon", image1)
cv2.waitKey(167)
cv2.imshow("Moon", image) #cv2.imshow("윈도우 창 제목", 이미지)를 이용하여 윈도우 창에 이미지를 띄웁니다.
cv2.waitKey(167) #cv2.waitkey(time)이며 time마다 키 입력상태를 받아옵니다. 0일 경우, 지속적으로 검사하여 해당 구문을 넘어가지 않습니다.
cv2.imshow("Moon", image1)
cv2.waitKey(167)