def get_finger_state(pseudoFixKeyPointDescripption, landmarks): 
    
    i, coordinate, inverse = pseudoFixKeyPointDescripption
    pseudoFixKeyPoint = landmarks[i][coordinate]
    
    if (landmarks[i+1][coordinate] < pseudoFixKeyPoint and landmarks[i+2][coordinate] < landmarks[i+1][coordinate]):
        if inverse:
            return 'CLOSE'
        return 'OPEN' 
            
    elif (pseudoFixKeyPoint < landmarks[i+1][coordinate] and landmarks[i+1][coordinate] < landmarks[i+2][coordinate]):
        
        if inverse:
            return 'OPEN'
        return 'CLOSE'
             
        
    return "UNKNOW"     
        
def get_fingers_states(landmarks):
    
    fingers_points_starts = [(2,'x', 1), # thumb_points_start, coordinate, inverse
                             (6, 'y', 0), # index_points_start,
                             (10, 'y',0), # middle_points_start,
                             (14, 'y', 0), # ring_points_start,
                             (18, 'y', 0)] # little_points_start 
    
    fingers_states = tuple([get_finger_state(x, landmarks) for x in fingers_points_starts])
    return fingers_states
    