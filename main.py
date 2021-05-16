from ImageMonitoring.gesture_tracking import track_gesture
from Controll.mapping_gestures import map_command_to_gesture

if __name__ == "__main__":
    track_gesture(track_gesture(function_on_change=map_command_to_gesture))
