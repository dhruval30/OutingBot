import cv2
import numpy as np

def find_landmarks(image_path):
    # Read the image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply edge detection
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    
    # Dilate the edges to connect nearby edges
    kernel = np.ones((3,3), np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=2)
    
    # Find contours
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    landmarks = []
    for contour in contours:
        # Filter contours based on area to remove noise
        area = cv2.contourArea(contour)
        if area > 100:  # Adjust this threshold as needed
            x, y, w, h = cv2.boundingRect(contour)
            landmarks.append((x, y, x+w, y+h))
    
    return landmarks, img

def visualize_landmarks(img, landmarks):
    for i, (x1, y1, x2, y2) in enumerate(landmarks):
        # Draw the rectangle with a thicker border
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
        
        # Label the landmark with L1, L2, ...
        label = f'L{i+1}'
        
        # Calculate label size and position with a smaller font and thickness
        (text_width, text_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
        text_org = (x1, y1 - 10)
        
        # Draw a larger background rectangle for better visibility
        cv2.rectangle(img, (text_org[0] - 5, text_org[1] + baseline - text_height - 5), 
                      (text_org[0] + text_width + 5, text_org[1] + baseline + 5), 
                      (0, 0, 0), cv2.FILLED)
        
        # Put the label text on top of the background rectangle with a smaller font and white color
        cv2.putText(img, label, text_org, cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
    
    # Resize image for display with a slightly larger scale
    scale_percent = 75  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    
    # Show the image with landmarks
    cv2.imshow('Landmarks', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = 'tania_outing.jpg'
landmarks, img = find_landmarks(image_path)

print(f"Found {len(landmarks)} potential landmarks:")
for i, landmark in enumerate(landmarks):
    print(f"Landmark {i+1}: {landmark}")

# Visualize the landmarks with labels
visualize_landmarks(img.copy(), landmarks)
