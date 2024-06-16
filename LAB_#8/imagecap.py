import numpy as np
import cv2 as cv

tag = cv.imread('ref-point.jpg', cv.IMREAD_GRAYSCALE)
mode = 2
params = [20, 40, 60, 80, 100]

def point_normalize(pts):
    array_x=[i[0] for i in pts]
    array_y=[i[1] for i in pts]
    array_x.sort()
    array_y.sort()
    center_x=(max(array_x)-min(array_x))//2
    center_y=(max(array_y)-min(array_y))//2
    length_min_x=(center_x-min(array_x))
    length_max_x=(max(array_x)-center_x)
    length_min_y=(center_y-min(array_y))
    length_max_y=(max(array_y)-center_y)
    return [max(min(array_x)-200,0),max(array_x)+200,max(min(array_y)-200,0),max(array_y)+200]     


cap = cv.VideoCapture(0)

# take first frame of the video
ret, frame = cap.read()
image = frame
dimensions = frame.shape
print(dimensions)
# setup initial location of window
x, y, w, h = 0, 0, dimensions[0], dimensions[1] # simply hardcoded the values
track_window = (x, y, w, h)
# set up the ROI for tracking
roi = frame[y:y+h, x:x+w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((30., 30., 30.)), np.array((255., 255., 255.)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)
# Setup the termination criteria, either 10 iteration or move by at least 1 pt
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)



# def get_poz_maker():
right_count = 0
left_count = 0
old_pos = 2
new_pos = 0
while(True):
    ret, frame = cap.read()
    if ret == True:
        if mode == 1:
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
            # apply camshift to get the new location
            ret, track_window = cv.CamShift(dst, track_window, term_crit)
            # Draw it on image
            pts = cv.boxPoints(ret)
            pts = np.int0(pts)
            #print(pts)


            detectWindow = cv.medianBlur(detectWindow, 5)

            img2 = cv.polylines(frame, [pts], True, 255, 2)
            cv.imshow('img2', img2)

            borders  = point_normalize(pts.tolist())
            #print(pts.tolist())

            detectWindow = frame[borders[0]:borders[1], borders[2]:borders[3]]
        elif mode == 2:
            detectWindow = frame

        fly = cv.imread("fly64.png")
        fly_h, fly_w = fly.shape[:2]
        # fly = cv.resize(fly, (64, 64))
        detectWindow = cv.cvtColor(detectWindow, cv.COLOR_RGB2GRAY)
        cimg = cv.cvtColor(detectWindow, cv.COLOR_GRAY2BGR)
        for i in params:
            circles = cv.HoughCircles(detectWindow, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=i,
                                      minRadius=0, maxRadius=100)
            if type(circles) != type(None):
                if len(circles[0]) == 1:
                    
                    dx = int(circles[0][0][0])
                    dy = int(circles[0][0][1])
                    frame[(dx - fly_w//2):(dx + fly_w//2), (dy - fly_h//2):(dy + fly_h//2)] = fly
                    # frame[dy][dx] = fly
                    centre_x = frame.shape[1] // 2
                    # print(centre_x)
                    if dx > centre_x:
                        new_pos = 2
                    if dx < centre_x:
                        new_pos = 1
                    if new_pos != old_pos:
                        if old_pos == 2:
                            left_count += 1
                        if old_pos == 1:
                            right_count += 1
                        old_pos = new_pos
                        # print('r', right_count)
                        # print('l', left_count)
                    cv.putText(frame, str(left_count), (100, 100),
                               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 140, 255), 2)
                    cv.putText(frame, str(right_count), (500, 100),
                               cv.FONT_HERSHEY_SIMPLEX, 1, (148, 0, 211), 2)

                    circles = np.uint16(np.around(circles))
                    for i in circles[0, :]:
                        # draw the outer circle
                        cv.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
                        # draw the center of the circle
                        cv.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
                    break
            else:
                pass

        # cv.imshow('fly_imgimg', fly)
        # cv.imshow('detected circles', cimg)
        cv.imshow('photo_point', frame)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
         break

