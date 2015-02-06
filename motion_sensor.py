# Creates differential images by subtracting to subsequent images. 
# If two subsequent images are the same, then the difference is zero, therefore there is 
# no image. Basically, it shows movement.

import cv2
import pygame

pygame.init()
pygame.mixer.music.load("Industrial Alarm-SoundBible.com-1012301296.wav")
pygame.mixer.music.set_volume(1)

def differential_image(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    diff = d1 - d2
    return cv2.bitwise_and(d1, d2), diff

camera = cv2.VideoCapture(0)

winName = "Movement Indicator"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

img_minus = cv2.cvtColor(camera.read()[1], cv2.COLOR_RGB2GRAY)
img = cv2.cvtColor(camera.read()[1], cv2.COLOR_RGB2GRAY)
img_plus = cv2.cvtColor(camera.read()[1], cv2.COLOR_RGB2GRAY)

while True:
    cv2.imshow( winName, differential_image(img_minus, img, img_plus)[0])
    diff = differential_image(img_minus, img, img_plus)[1]
    lst = range(100,110)
    for num in lst:
        if num in diff:
            print "INTRUDER"
            pygame.mixer.music.play()
    img_minus = img
    img = img_plus
    img_plus = cv2.cvtColor(camera.read()[1], cv2.COLOR_RGB2GRAY)

    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyWindow(winName)
        break

print "Goodbye"

