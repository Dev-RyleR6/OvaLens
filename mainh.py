from ultralytics import YOLO
import cv2

# 1. Load your newly downloaded egg fertility model
# Because best.pt is in the same folder as mainh.py, we just use the file name
model = YOLO('weights/best.pt') 

# 2. Open webcam (0 is usually the default built-in camera)
cap = cv2.VideoCapture(1)

print("🥚 Egg Fertility Detection Live! - Press 'q' to quit")

# 3. Start the live video loop
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Run detection on the current frame (verbose=False keeps the terminal clean)
    results = model(frame, verbose=False)
    
    # Draw the bounding boxes and labels on the frame
    annotated_frame = results[0].plot()
    
    # Show the frame in a pop-up window
    cv2.imshow("Egg Fertility Detection", annotated_frame)
    
    # Press 'q' on your keyboard to quit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 4. Clean up the camera and close windows
cap.release()
cv2.destroyAllWindows()