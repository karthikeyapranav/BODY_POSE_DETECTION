import cv2
import mediapipe as mp
import numpy as np

pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
mp_pose = pose.Pose()
capture = cv2.VideoCapture("D:\BODY_POSE_DETECTION\\videos\\Video.mp4")
#capture = cv2.VideoCapture(0)

while True:
    ret,img = capture.read()
    img = cv2.resize(img,(700,700))
    results = mp_pose.process(img)
    h,w,c = img.shape
    output = np.zeros([h,w,c])
    output.fill(225)
    mp_draw.draw_landmarks(output,results.pose_landmarks,pose.POSE_CONNECTIONS)
    cv2.imshow("skeleton output",output)
    mp_draw.draw_landmarks(img,results.pose_landmarks,pose.POSE_CONNECTIONS)
    print(results.pose_landmarks)
    cv2.imshow("pose detection",img)
    cv2.waitKey(5)