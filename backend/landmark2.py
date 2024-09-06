import cv2
import numpy as np

def find_landmarks(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    
    kernel = np.ones((3,3), np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=2)
    
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    landmarks = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:  
            x, y, w, h = cv2.boundingRect(contour)
            landmarks.append((x, y, x+w, y+h))
    
    return landmarks, img

def visualize_landmarks(img, landmarks):
    for i, (x1, y1, x2, y2) in enumerate(landmarks):
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
        
        label = f'L{i+1}'
        
        (text_width, text_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
        text_org = (x1, y1 - 10)
        
        cv2.rectangle(img, (text_org[0] - 5, text_org[1] + baseline - text_height - 5), 
                      (text_org[0] + text_width + 5, text_org[1] + baseline + 5), 
                      (0, 0, 0), cv2.FILLED)
        
        cv2.putText(img, label, text_org, cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
    

    scale_percent = 75  
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    
    cv2.imshow('Landmarks', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = 'outing.jpg'
landmarks, img = find_landmarks(image_path)

print(f"Found {len(landmarks)} potential landmarks:")
for i, landmark in enumerate(landmarks):
    print(f"Landmark {i+1}: {landmark}")

visualize_landmarks(img.copy(), landmarks)
