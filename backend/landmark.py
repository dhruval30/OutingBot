import cv2
import pytesseract
import numpy as np

def find_date_regions(image_path, date_strings):
    # Read the image
    img = cv2.imread(image_path)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
    
    date_regions = []
    
    # Loop through the recognized text
    for i, text in enumerate(data['text']):
        for date_string in date_strings:
            if date_string in text:
                # Get bounding box
                x = data['left'][i]
                y = data['top'][i]
                w = data['width'][i]
                h = data['height'][i]
                
                # Add some padding
                x -= 5
                y -= 5
                w += 10
                h += 10
                
                date_regions.append((x, y, x+w, y+h))
    
    return date_regions

# Example usage
image_path = 'outing.png'
date_strings = ['23rd August 2024', '26th August 2024', '22-08-2024']

regions = find_date_regions(image_path, date_strings)

for i, region in enumerate(regions):
    print(f"Region {i+1}: {region}")