#circle detection in OpenCV Python
import cv2 as cv
import numpy as np

img=cv.imread("E:/openCV_images/eye.jpg",cv.IMREAD_COLOR)
grayImg=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
grayBlurred=cv.blur(grayImg,(3,3))

detectedCircle=cv.HoughCircles(grayBlurred,cv.HOUGH_GRADIENT,1,
                               20,param1=50,param2=28,minRadius=1,
                               maxRadius=30)
#draw circle that detected
if detectedCircle is not None:
    #convert the circle parameters to integers
    detectedCircle=np.uint16(np.around(detectedCircle))
    for p in detectedCircle[0,:]:
        a,b,c=p[0],p[1],p[2]
        
        #draw the circumference of the circle
        cv.circle(img,(a,b),c,(0,255,255),3)
        cv.imshow("detected_circle",img)
        cv.waitKey(0)
        