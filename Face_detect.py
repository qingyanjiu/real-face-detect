import cv2
import time
from test import testVideo 

class FaceDetection():

    current_frame = 0
    
    cv2.namedWindow('face detect', cv2.WINDOW_KEEPRATIO)

    def detect_video(self, source=0, draw=True, flip=True, max_num_faces = 10):
        # For webcam input:
        if type(source) == int:
            cap = cv2.VideoCapture(source, cv2.CAP_DSHOW)
        else:
            cap = cv2.VideoCapture(source)
            
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue
            
            if flip:
                image = cv2.flip(image, 1)
            
            image.flags.writeable = False
            
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Draw the face detection annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            image = testVideo(image)
                                    
            cv2.imshow('face detect', image)
            
            if cv2.waitKey(1) == ord('q'):  # q to quit
                cv2.destroyAllWindows()
                break
            
            self.current_frame += 1
            
        cap.release()
    

if __name__ == '__main__':
    face_detection = FaceDetection()
    face_detection.detect_video(
        0, 
        draw=True,
        flip=True,
        max_num_faces=10
        )
