import cv2
import datetime

def video_processing_pipeline(input_path=0):
    # Initialize video capture (0 = webcam, or file path)
    cap = cv2.VideoCapture("/home/rahim/Downloads/Using A STIHL Long Reach Hedge Trimmer With Chris Hollins STIHL GB - STIHL GB (720p, h264).mp4")
    
    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Create VideoWriter for saving output
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output_video.avi', fourcc, fps, (width, height))
    
    # Load Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # --------------------------------------------------
        # Processing Pipeline (Add your effects here)
        # --------------------------------------------------
        
        # 1. Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # 2. Edge detection
        edges = cv2.Canny(gray, 100, 200)
        
        # 3. Face detection
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # 4. Add timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(frame, timestamp, (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        
        # 5. Add FPS counter
        cv2.putText(frame, f"FPS: {int(fps)}", (10, 60),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        
        # --------------------------------------------------
        # Display and save
        # --------------------------------------------------
        
        # Show original frame with annotations
        cv2.imshow('Live Processing', frame)
        
        # Show edge detection
        cv2.imshow('Edge Detection', edges)
        
        # Write processed frame to output file
        out.write(frame)
        
        # Exit on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    # Cleanup
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # For webcam input (default)
    video_processing_pipeline()
    
    # For video file input
    # video_processing_pipeline("input_video.mp4")