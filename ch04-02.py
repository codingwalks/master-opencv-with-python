import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# Create a blank image
image = np.zeros((512, 512, 3), np.uint8)

# Convert OpenCV image to Pillow's Image object
image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

# Set the Korean font path (specify the exact location of the font file)
fontpath = "fonts/NanumGothic.ttf"
font = ImageFont.truetype(fontpath, 40)

# Creating a Draw object in Pillow
draw = ImageDraw.Draw(image_pil)

# Drawing Korean text
text = "OpenCV 텍스트 예제"
draw.text((50, 200), text, font=font, fill=(255, 255, 255))

# Convert back to OpenCV image
image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)

# Image Output
cv2.imshow('Hangul Text', image)
cv2.waitKey(0)
cv2.destroyAllWindows()