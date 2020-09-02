import cv2
import matplotlib
import matplotlib.pyplot as plt

IMAGE_PATH = "./photos/background.jpg"

image1 = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)

plt.imshow(image1[:, :, ::-1])
plt.show()

image2 = image1
print(type(image1), type(image2))
print(image1.shape, image2.shape)
print(hex(id(image1)), hex(id(image2)))
print(image1 is image2)