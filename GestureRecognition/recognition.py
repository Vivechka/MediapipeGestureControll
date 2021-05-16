from .utils.fingers_state_scanning import get_fingers_states
from .utils.landmarks_processing import get_structured_from_landmarks

def recognizeHandGesture(landmarks):
    
    landmarks = get_structured_from_landmarks(landmarks)
    
    recognizedHandGesture = None

    fingers_states  = get_fingers_states(landmarks)
  
    gestures ={('OPEN', 'OPEN', 'OPEN', 'OPEN', 'OPEN'): "FIVE",
               ('CLOSE','CLOSE','CLOSE','CLOSE','CLOSE'):"FIST",
               ('CLOSE','OPEN', 'CLOSE','CLOSE','OPEN'): "HARD",
               ('CLOSE','CLOSE', 'OPEN','CLOSE','CLOSE'): "FUCK"}
    
    recognizedHandGesture = gestures.get(fingers_states, "Unknown gesture")
                                         
    return recognizedHandGesture
