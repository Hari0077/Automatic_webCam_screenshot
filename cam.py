import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open webcam")

ret, frame = cap.read()
frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
cv2.imshow('Input', frame)
outpath = "input/input_img.jpg"
cv2.imwrite(outpath, frame)
cv2.waitKey(0)
    #destroy a certain window
cv2.destroyWindow('Input')
cap.release()
cv2.destroyAllWindows()