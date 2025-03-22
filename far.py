import cv2
import matplotlib.pyplot as plt

def process_video_frames(video_path, max_display_frames=20):
    """Process video frames and display a grid of frames"""
    # Create video capture object
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        raise ValueError(f"Could not open video: {video_path}")

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print(f"Video Info: {total_frames} frames | {fps:.2f} FPS")

    # Read all frames
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    cap.release()

    if not frames:
        raise ValueError("No frames could be read from the video")

    # Limit number of displayed frames for practicality
    display_frames = frames[:max_display_frames]
    num_frames = len(display_frames)
    
    # Create grid layout
    cols = 5  # Number of columns in the grid
    rows = (num_frames + cols - 1) // cols  # Calculate needed rows

    # Create subplots with proper spacing
    fig, axes = plt.subplots(rows, cols, figsize=(20, 3 * rows))
    if rows == 1:  # Handle single row case
        axes = [axes]
    
    plt.subplots_adjust(wspace=0.1, hspace=0.3)
    
    # Plot frames in grid
    for i, ax in enumerate(axes.flat if rows > 1 else axes):
        if i < num_frames:
            ax.imshow(display_frames[i])
            ax.set_title(f"Frame {i+1}\n({i//int(fps)}s {i%int(fps)}f)")
            ax.axis("off")
        else:
            ax.axis("off")  # Hide empty subplots

    plt.show()
    return len(frames)

# Example usage
video_path = "/home/rahim/Downloads/Using A STIHL Long Reach Hedge Trimmer With Chris Hollins STIHL GB - STIHL GB (720p, h264).mp4"

try:
    total_frames = process_video_frames(video_path)
    print(f"Successfully processed {total_frames} frames")
except Exception as e:
    print(f"Error: {str(e)}")