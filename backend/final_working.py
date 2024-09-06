import cv2
import numpy as np

def update_dates(image_path, new_dates):
    img = cv2.imread(image_path)
    
    date_regions = [
        (256, 472, 443, 494),  # First date region (Landmark 89, 78, 88)
        (142, 512, 328, 534),  # Second date region (combined Landmark 72, 70, 71)
        (214, 922, 348, 947)   # Third date region (Landmark 5)
    ]
    
    for region in date_regions:
        cv2.rectangle(img, (region[0], region[1]), (region[2], region[3]), (255, 255, 255), -1)
    
    for i, region in enumerate(date_regions):
        cv2.putText(img, new_dates[i], (region[0], region[1] + 20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    
    cv2.imwrite('updated_image.jpg', img)

new_dates = ['2300 Sept 2024', '19 Sept 2024', '4/10/2024']
update_dates('outing.png', new_dates)
