import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):

    ret, im = cap.read()
    flip_im = cv2.flip(im, 1)

    h,w = im.shape[:2]
    b = flip_im[int(h/2),int(w/2),0]
    g = flip_im[int(h / 2), int(w / 2),1]
    r = flip_im[int(h / 2), int(w / 2),2]
    print(h,w)


    mask = cv2.inRange(flip_im,(80,30,0),(150,100,50))
    mask2 = cv2.inRange(flip_im,(80, 100,50),(80, 150, 80))
    mask3 = cv2.inRange(flip_im,(0, 0,90),(50, 50, 255))

    cv2.imshow('mask',mask)
    cv2.imshow('mask2', mask2)
    cv2.imshow('mask3', mask3)
    cv2.putText(flip_im, str(b) + ',' + str(g) + ',' + str(r), (20,20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))

    if(np.sum(mask) > 0.1*h*w):
        cv2.putText(flip_im,'Pepsi',(int(h/2),int(w/2)),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255))
    elif(np.sum(mask2) > 0.1*h*w):
        cv2.putText(flip_im, 'Fanta', (int(h / 2), int(w / 2)), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255))
    elif (np.sum(mask3) > 0.1 * h * w):
        cv2.putText(flip_im, 'Coke', (int(h / 2), int(w / 2)), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255))

    cv2.imshow('camera',flip_im)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


