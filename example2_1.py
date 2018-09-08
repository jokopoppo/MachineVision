import numpy as np
import cv2

cap = cv2.VideoCapture('D:/MachineVision/ExampleBGSubtraction.avi')
fps=cap.get(cv2.CAP_PROP_FPS) #read fps for smooth video
# print(fps)

tmp,bg=cap.read()
while(cap.isOpened()):
    haveFrame, im = cap.read()

    if (not haveFrame) or (cv2.waitKey(int(1000/fps)) & 0xFF == ord('q')):
        break

    diffc=cv2.absdiff(im,bg)
    diffg=cv2.cvtColor(diffc,cv2.COLOR_BGR2GRAY)
    bwmask = cv2.inRange(diffg,100,255)

    bwmask = cv2.medianBlur(bwmask,5) # eliminate noise

    kernel = np.ones((55,25),np.uint8)
    bwmask = cv2.morphologyEx(bwmask,cv2.MORPH_CLOSE,kernel)

    temp = bwmask.copy()
    contourMask,contours,hierarchy = cv2.findContours(temp,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) # contour object

    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.drawContours(im,contours,-1,(0,255,0),1)

    cv2.imshow("bwmask",bwmask)
    cv2.moveWindow('bwmask',10,10)
    cv2.imshow('contourMask',contourMask)
    cv2.moveWindow('contourMask', 400, 10)
    cv2.imshow('im',im)
    cv2.moveWindow('im', 800, 10)

cap.release()
cv2.destroyAllWindows()