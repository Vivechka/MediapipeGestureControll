def get_structured_from_landmarks(landmarks):
    keypoints = []
    for data_point in landmarks.landmark:
        keypoints.append({
                         'x': data_point.x,
                         'y': data_point.y
                         })
    return keypoints
    