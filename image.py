import cv2
import matplotlib.pyplot as plt

# Load the video
video_path = "/home/rahim/Downloads/Using A STIHL Long Reach Hedge Trimmer With Chris Hollins STIHL GB - STIHL GB (720p, h264).mp4"
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video file")
    exit()

# Read first two frames
success, frame1 = cap.read()
success, frame2 = cap.read()

if not success:
    print("Error: Could not read frames from video")
    cap.release()
    exit()

# Convert frames from BGR to RGB
frame1_rgb = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
frame2_rgb = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)

# Create figure and axes
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Display frames
axes[0].imshow(frame1_rgb)
axes[0].set_title("Frame 1")
axes[0].axis("off")

axes[1].imshow(frame2_rgb)
axes[1].set_title("Frame 2")
axes[1].axis("off")

plt.show()

# Release video capture
cap.release()