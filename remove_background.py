import cv2
import numpy as np
from rembg import remove

def remove_background(image_path, output_path):
    
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image {image_path}")
        return

    
    with open(image_path, "rb") as img_file:
        img_data = img_file.read()
        result = remove(img_data)

    
    np_result = np.frombuffer(result, dtype=np.uint8)
    bg_removed = cv2.imdecode(np_result, cv2.IMREAD_UNCHANGED)

    
    cv2.imwrite(output_path, bg_removed)
    print(f"Background removed image saved as {output_path}")


input_image_path = 'input.jpg'
output_image_path = 'output.png'
remove_background(input_image_path, output_image_path)
