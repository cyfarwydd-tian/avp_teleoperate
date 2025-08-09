import sys, cv2
idx = int(sys.argv[1]) if len(sys.argv) > 1 else 0
cap = cv2.VideoCapture(idx, cv2.CAP_V4L2)
print("open:", cap.isOpened())
ok, frame = cap.read()
print("read:", ok)
if ok:
    print("shape:", frame.shape)
cap.release()

