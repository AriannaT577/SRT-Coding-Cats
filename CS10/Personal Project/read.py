import cv2

file = 'picture_espeon.jpg'
image = cv2.imread(file)

if image is not None:
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)            # Wait until any key is pressed
    cv2.destroyAllWindows()   
else:
    print("Failed to load image. Check the file path.")

