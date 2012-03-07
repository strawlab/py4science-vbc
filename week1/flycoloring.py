import cv
import time
import getfile

getfile.get_from_strawlab("week1/flies.avi")

movie = cv.CaptureFromFile("flies.avi")
nframes, rows, cols = map(lambda x: int(cv.GetCaptureProperty(movie, x)), 
    [cv.CV_CAP_PROP_FRAME_COUNT, cv.CV_CAP_PROP_FRAME_HEIGHT, cv.CV_CAP_PROP_FRAME_WIDTH])

background = cv.CreateMat(rows, cols, cv.CV_8UC3)
for i in range(nframes):
    cv.Max(cv.QueryFrame(movie), background, background)
cv.ShowImage("background", background)

cv.SetCaptureProperty(movie, cv.CV_CAP_PROP_POS_FRAMES, 0)
for i in range(nframes):
    frame = cv.QueryFrame(movie)
    cv.ShowImage("before", frame)
    cv.Sub(background, frame, frame)
    cv.Smooth(frame, frame, param1=5)
    cv.Threshold(frame, frame, 70, 255, cv.CV_THRESH_BINARY)
    cv.ShowImage("after", frame)
    if cv.WaitKey(20) % 256 == ord('q'):
        break

