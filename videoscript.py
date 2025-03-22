import cv2
import matplotlib.pyplot as plt

# Load the video
video_path = "/home/rahim/Downloads/Using A STIHL Long Reach Hedge Trimmer With Chris Hollins STIHL GB - STIHL GB (720p, h264).mp4"
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Video', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Convert frame from BGR to RGB
frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Display the frame
plt.figure(figsize=(10, 6))
plt.imshow(frame_rgb)
plt.title(f"First Frame: {video_path.split('/')[-1]}")
plt.axis("off")
plt.show()

# Release video resources
cap.release()