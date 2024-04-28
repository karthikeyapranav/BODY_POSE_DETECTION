# BODY_POSE_DETECTION
Body post detection helped us to identify the position of the body and For this, we are using media pipe an open source framework developed by the Google,  Which help to Identify keyboard detection image segmentation, image classification,Object Detection.
This code performs real-time body pose detection using the MediaPipe library in Python. Let's break down the code step by step:

Import Libraries:
cv2: OpenCV library for computer vision tasks.
mediapipe: MediaPipe library for building real-time multi-modal ML pipelines.
numpy: Library for numerical computing.
python
Copy code
import cv2
import mediapipe as mp
import numpy as np
Initialize MediaPipe Pose Detection:
Create instances for pose estimation, drawing utilities, and the Pose model provided by MediaPipe.
python
Copy code
pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
mp_pose = pose.Pose()
Open Video Capture:
Initialize video capture using OpenCV. You can either capture from a video file or from a webcam (commented out).
capture = cv2.VideoCapture("D:\BODY_POSE_DETECTION\\videos\\Video.mp4")
# capture = cv2.VideoCapture(0)
Main Loop:
Continuously read frames from the video capture.
Resize the frame to a specific size (700x700 in this case).
Process the resized frame using the MediaPipe Pose model to detect pose landmarks.
Draw the detected landmarks on the frame and display it.
Draw the detected landmarks on a separate black canvas and display it as the skeleton output.
Print the pose landmarks data.
Wait for a key press for a specified duration (5 milliseconds) before reading the next frame.
python
Copy code
while True:
    ret, img = capture.read()
    img = cv2.resize(img, (700, 700))
    results = mp_pose.process(img)
    h, w, c = img.shape
    output = np.zeros([h, w, c])
    output.fill(225)
    mp_draw.draw_landmarks(output, results.pose_landmarks, pose.POSE_CONNECTIONS)
    cv2.imshow("skeleton output", output)
    mp_draw.draw_landmarks(img, results.pose_landmarks, pose.POSE_CONNECTIONS)
    print(results.pose_landmarks)
    cv2.imshow("pose detection", img)
    cv2.waitKey(5)
Explanation:
The results.pose_landmarks contain the detected pose landmarks, which are the key points on the human body.
The landmarks are drawn using mp_draw.draw_landmarks() function.
The frame is continuously updated within the while loop, allowing real-time pose detection.
This script essentially captures a video stream, processes each frame to detect the landmarks of the human body, and then visualizes these landmarks in real-time both on the original frame and on a separate black canvas showing just the skeleton.






