import cv2
import numpy as np

def rotate_image(image, angle):
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

def flip_image(image, flip_code):
    flipped_image = cv2.flip(image, flip_code)
    return flipped_image

def zoom_image(image, scale):
    height, width = image.shape[:2]
    new_height, new_width = int(height * scale), int(width * scale)
    zoomed_image = cv2.resize(image, (new_width, new_height))
    return zoomed_image

def translate_image(image, tx, ty):
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
    return translated_image

# Baca citra
image_path = 'ss1.jpg'  
original_image = cv2.imread(image_path)

# Rotasi
angle = 45
rotated_image = rotate_image(original_image, angle)

# Flipping
flip_code = 1  # 0 untuk flipping horizontal, 1 untuk flipping vertical
flipped_image = flip_image(original_image, flip_code)

# Zooming
scale = 1.5
zoomed_image = zoom_image(original_image, scale)

# Translasi
tx, ty = 50, 30
translated_image = translate_image(original_image, tx, ty)

# Menampilkan citra asli dan hasil operasi geometri
cv2.imshow('Original Image', original_image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Flipped Image', flipped_image)
cv2.imshow('Zoomed Image', zoomed_image)
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
