import cv2
import numpy as np

def update_dates(image_file_path, dates_to_update):
    image_data = cv2.imread(image_file_path)
    
    defined_date_regions = [
        (256, 472, 443, 494),  # Coordinates for the first date region
        (142, 512, 328, 534),  # Coordinates for the second date region
        (214, 922, 348, 947)   # Coordinates for the third date region
    ]
    
    for region_coordinates in defined_date_regions:
        top_left_x = region_coordinates[0]
        top_left_y = region_coordinates[1]
        bottom_right_x = region_coordinates[2]
        bottom_right_y = region_coordinates[3]
        cv2.rectangle(image_data, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (255, 255, 255), -1)
    
    for index, region_coordinates in enumerate(defined_date_regions):
        region_x1 = region_coordinates[0]
        region_y1 = region_coordinates[1]
        text_position_x = region_x1 + 10
        text_position_y = region_y1 + 20
        cv2.putText(image_data, dates_to_update[index], (text_position_x, text_position_y), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    
    output_image_path = 'updated_image.jpg'
    cv2.imwrite(output_image_path, image_data)

dates_list = ['30 August 2024', '2 September 2024', '29-08-2024']
input_image_path = 'outing.png'
update_dates(input_image_path, dates_list)
