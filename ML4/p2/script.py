import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    cv2.imshow("Press 's' to Save",frame)
    key =  cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite("sd.jpeg",frame)
        print("sd.jpeg is saved")
        break
    elif key == ord('q'):
        print("Exiting without saving")
        break

cap.release()
cv2.destroyAllWindows()
