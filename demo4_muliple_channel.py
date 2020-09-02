import cv2
import matplotlib
import matplotlib.pyplot as plt

IMAGE_PATH = "./photos/mnist0.png"

image1 = cv2.imread(IMAGE_PATH, 1)
print(image1.shape, type(image1))

plt.imshow(image1)
plt.show()
print("first plot={}", format(image1[0, 0]))
print("[2,2] plot={}", format(image1[2, 2]))

plt.figure(figsize=[18, 6])
for i in range(50):
    for j in range(50):
        image1[i, j] = (0, 128, 255)
plt.subplot(1, 3, 1)
plt.imshow(image1[:, :, ::-1])
for i in range(50):
    for j in range(50):
        image1[i + 50, j] = (128, 255, 0)
plt.subplot(1, 3, 2)
plt.imshow(image1[:, :, ::-1])
for i in range(50):
    for j in range(50):
        image1[i, j + 50] = (255, 0, 128)
plt.subplot(1, 3, 3)
plt.imshow(image1[:, :, ::-1])
plt.show()
