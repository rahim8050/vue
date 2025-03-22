import cv2
import matplotlib.pyplot as plt

# Load the video
video_path = "/home/rahim/Downloads/Using A STIHL Long Reach Hedge Trimmer With Chris Hollins STIHL GB - STIHL GB (720p, h264).mp4"
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Read the first frame
ret, frame = cap.read()

# Convert the frame from BGR to RGB (for correct display in matplotlib)
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Display the frame
plt.imshow(frame)
plt.title(f"Original Frame from Video: {video_path.split('/')[-1]}")
plt.axis("off")
plt.show()

# Release the video capture object
cap.release()