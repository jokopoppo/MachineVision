import numpy as np
import cv2

file=[]
for i in range(1,11):
    file.append("coin"+str(i))

n=3
print(file[n])
img = cv2.imread('D:/MachineVision/CoinCounting/'+file[n]+'.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
gray = cv2.medianBlur(gray,25) # eliminate noise
gray = cv2.cvtColor(gray,cv2.COLOR_HSV2BGR)

mask1 = cv2.inRange(gray,(0,100,100),(100,255,255))
gray = cv2.cvtColor(gray,cv2.COLOR_BGR2HSV_FULL)
mask2 = cv2.inRange(gray,(50,100,100),(200,255,255))

y=30
b=56
# e=50
kernel_y = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(y,y))
kernel_b = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(b,b))
# kernel_e = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(e,e))

mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel_y)

# mask2 = cv2.morphologyEx(mask2, cv2.MORPH_OPEN, kernel_b, iterations=1)




temp1 = mask1.copy()
contourMask,contours,hierarchy = cv2.findContours(temp1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # contour object
cv2.drawContours(gray,contours,-1,(0,0,255),3)
print("Yellow = ",len(contours))

temp2 = mask2.copy()
contourMask,contours,hierarchy = cv2.findContours(temp2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) # contour object
cv2.drawContours(gray,contours,-1,(0,0,255),3)
print("Blue = ",len(contours))
while(True):
    cv2.namedWindow('gray', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('gray', 600, 600)
    cv2.imshow("gray",gray)

    cv2.namedWindow('mask1', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('mask1', 600, 600)
    cv2.imshow("mask1",mask1)

    cv2.namedWindow('mask2', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('mask2', 600, 600)
    cv2.imshow("mask2", mask2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
