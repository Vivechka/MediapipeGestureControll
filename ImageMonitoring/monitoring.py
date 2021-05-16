from datetime import datetime, timedelta

def monitor_gesture_changing(previous_gesture_stored, previous_gesture, gesture_changing_ts, recognizedHandGesture, time_to_track_gesture_s, function_on_change):
    if recognizedHandGesture != previous_gesture_stored and recognizedHandGesture != "Unknown gesture":

        if recognizedHandGesture == previous_gesture: # If gesture not changed comparing to last 
            gesture_showing_duration = datetime.now() - gesture_changing_ts

            if gesture_showing_duration > timedelta(0, time_to_track_gesture_s): # if it's holded for long enough
                previous_gesture_stored = recognizedHandGesture
                function_on_change(recognizedHandGesture)

        if recognizedHandGesture != previous_gesture:
            previous_gesture = recognizedHandGesture
            gesture_changing_ts = datetime.now()
            
    return previous_gesture_stored, previous_gesture, gesture_changing_ts, recognizedHandGesture