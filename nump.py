import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
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

    # Load font using Pillow
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to PIL Image
        pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(pil_image)

        # Add timestamp using Pillow
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        draw.text((10, 30), timestamp, fill=(0, 255, 0), font=font)

        # Add bounding box (converted to RGB colors)
        draw.rectangle([(50, 50), (200, 200)], outline=(255, 0, 0), width=2)

        # Add text label
        draw.text((frame_width-300, 30), "Security Feed", 
                fill=(255, 255, 255), font=font)

        # Add circle using NumPy for coordinate calculation
        center = np.array([frame_width//2, frame_height//2])
        radius = 30
        bbox = [
            tuple(center - radius),
            tuple(center + radius)
        ]
        draw.ellipse(bbox, fill=(0, 0, 255))

        # Convert back to OpenCV format
        annotated_frame = cv2.cvtColor(
            np.array(pil_image), 
            cv2.COLOR_RGB2BGR
        )

        # Write frame to output
        out.write(annotated_frame)

        # Display preview
        cv2.imshow('Annotated Video', annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Annotation complete! Saved to: {output_path}")

# Usage with your paths
input_video = "/home/rahim/Downloads/Using A STIHL Long Reach Hedge Trimmer With Chris Hollins STIHL GB - STIHL GB (720p, h264).mp4"
output_video = "/home/rahim/Desktop/New Folder 3/vids/annotated_output_pillow.mp4"

annotate_video(input_video, output_video)