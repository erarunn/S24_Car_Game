import cv2
import numpy as np

# Create a blank image
height, width = 200, 300
image = cv2.imread("OIP_mask.png")
# Padding values (top, bottom, left, right)
top, bottom, left, right = 50, 50, 30, 30

# Pad the image with a border (constant color)
padded_image = cv2.copyMakeBorder(
    image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=(255, 255, 255)
)  # Blue padding

# Show the padded image
cv2.imshow("Padded Image", padded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
