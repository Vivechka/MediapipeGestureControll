import cv2
import mediapipe as mp
from datetime import datetime

from GestureRecognition.recognition import recognizeHandGesture
from .monitoring import monitor_gesture_changing

def track_gesture(function_on_change = print, time_to_track_gesture_s = 1, min_detection_confidence=0.6):
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    initial_gesture = "Unknown gesture"
    previous_gesture_stored = initial_gesture
    previous_gesture = initial_gesture
    
    initial_time = datetime.now()
    time_gesture_changed = initial_time

    # For webcam input:
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
    
    hands = mp_hands.Hands(min_detection_confidence=0.6,
                           min_tracking_confidence=0.5)

    while cap.isOpened():
        _, image = cap.read()

        # Flip image 
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        
        # Detect hands
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                recognizedHandGesture = recognizeHandGesture(hand_landmarks)

                gesture_monitoring_state = monitor_gesture_changing(previous_gesture_stored, 
                                                                    previous_gesture, 
                                                                    time_gesture_changed, 
                                                                    recognizedHandGesture, 
                                                                    time_to_track_gesture_s,
                                                                    function_on_change)

                previous_gesture_stored, previous_gesture, time_gesture_changed, recognizedHandGesture = gesture_monitoring_state

            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        out.write(image)
        cv2.imshow('Hands Light Controll', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
    cap.release()
    out.release()
