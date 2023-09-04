import cv2

source = "image.jpg"
destination = "resized_"+ source

scale_percent = int(input("Enter the scale percentage (1-100): \n"))


src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", src)


new_width = int(src.shape[1] * scale_percent/100)
new_height = int(src.shape[0] * scale_percent/100)

d_size = (new_width, new_height)

output = cv2.resize(src, d_size)

cv2.imwrite(destination, output)

cv2.waitKey(0)