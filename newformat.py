import cv2

# Callback function for drawing rectangles
def draw_rectangle(event, x, y, flags, param):
    global x_init, y_init, drawing, frame

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x_init, y_init = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            frame_copy = frame.copy()
            cv2.rectangle(frame_copy, (x_init, y_init), (x, y), (0, 255, 0), 2)
            cv2.imshow('Video Annotation', frame_copy)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(frame, (x_init, y_init), (x, y), (0, 255, 0), 2)
        cv2.imshow('Video Annotation', frame)

# Load the video
video_path = '/home/rahim/Downloads/Using A STIHL Long Reach Hedge Trimmer With Chris Hollins STIHL GB - STIHL GB (720p, h264).mp4'
output_path = 'output_video.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

cv2.namedWindow('Video Annotation')
cv2.setMouseCallback('Video Annotation', draw_rectangle)

x_init, y_init, drawing = -1, -1, False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Video Annotation', frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('s'):
        # Save the current frame with annotations
        cv2.imwrite('annotated_frame.jpg', frame)

    # Write the frame with annotations to the output video
    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()