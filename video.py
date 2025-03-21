import cv2
import datetime

def annotate_video(input_path, output_path):
    # Open video file
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print("Error: Could not open video file")
        return

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Create video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Add timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(frame, timestamp, (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Add bounding box (example: top-left corner)
        cv2.rectangle(frame, (50, 50), (200, 200), (0, 0, 255), 2)

        # Add text label
        cv2.putText(frame, "Security Feed", (frame_width-300, 30),
                   cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        # Add custom annotation (example: circle)
        cv2.circle(frame, (frame_width//2, frame_height//2), 30, (255, 0, 0), -1)

        # Write annotated frame to output
        out.write(frame)

        # Display preview (optional)
        cv2.imshow('Annotated Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Annotation complete! Saved to: {output_path}")

# Usage with your specific paths
input_video = "/home/rahim/Downloads/Using A STIHL Long Reach Hedge Trimmer With Chris Hollins STIHL GB - STIHL GB (720p, h264).mp4"
output_video = "/home/rahim/Desktop/New Folder 3/vids/annotated_output.mp4"  # Added filename

annotate_video(input_video, output_video)