import cv2

# Configurable Parameters
source = "img.png"
destination = "newImg.jpg"
scale_precentage = 100

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", src)


new_width = int(src.shape[1] * scale_precentage / 100)
new_height = int(src.shape[0] * scale_precentage / 100)

output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
cv2.waitKey(0)