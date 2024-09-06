import cv2
import numpy as np

def visualize_specific_landmarks(img, landmarks):
    for i, (x1, y1, x2, y2) in landmarks.items():
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        label = f'L{i}'
        
        (text_width, text_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
        text_org = (x1, y1 - 10)
        
        cv2.rectangle(img, (text_org[0] - 5, text_org[1] + baseline - text_height - 5), 
                      (text_org[0] + text_width + 5, text_org[1] + baseline + 5), 
                      (0, 0, 0), cv2.FILLED)
        
        cv2.putText(img, label, text_org, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    
    # Resize image for display
    scale_percent = 50  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    
    cv2.imshow('Landmarks', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = 'outing.png'
img = cv2.imread(image_path)


specific_landmarks = {
    5: (214, 922, 348, 947),
    # 89: (256, 472, 307, 494),
    # 78: (311, 473, 388, 499),
    # 88: (392, 472, 443, 494),
    1: (256, 472, 443, 499),
    72: (142, 512, 191, 534),
    70: (192, 513, 269, 539),
    71: (271, 512, 328, 534)
}

visualize_specific_landmarks(img.copy(), specific_landmarks)
