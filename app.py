import cv2
import numpy as np
import streamlit as st
from PIL import Image
import tempfile

def update_dates(image, new_dates):
    img = np.array(image)

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
    
    return img

def main():
    st.title("Outing Form Update")

    uploaded_file = st.file_uploader("Upload your outing form image", type=['png', 'jpg', 'jpeg'])

    new_date1 = st.text_input("Enter the date when you want to leave", 'xx month 20xx')
    new_date2 = st.text_input("Enter the date when you will return", 'xx month 20xx')
    new_date3 = st.text_input("Enter the date when you will fill the form", 'dd/mm/yyyy')

    if uploaded_file is not None:
        img = Image.open(uploaded_file)

        st.image(img, caption="Uploaded Image", use_column_width=True)

        if st.button("Update Dates"):
            new_dates = [new_date1, new_date2, new_date3]
            updated_img = update_dates(img, new_dates)

            st.image(updated_img, caption="Updated Image", use_column_width=True)

            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
            cv2.imwrite(temp_file.name, updated_img)

            with open(temp_file.name, "rb") as file:
                btn = st.download_button(
                    label="Download Updated Image",
                    data=file,
                    file_name="updated_image.jpg",
                    mime="image/jpeg"
                )

if __name__ == "__main__":
    main()
