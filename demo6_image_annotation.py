import cv2
import matplotlib.pyplot as plt

IMAGE_PATH = "./photos/background.jpg"

image1 = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)
plt.imshow(image1[:, :, ::-1])
# plt.show()
image2 = image1
image3 = image1.copy()
image4 = image1[:]
print(type(image1), type(image2), type(image3), type(image4))
print(image1.shape, image2.shape, image3.shape, image4.shape)
print(hex(id(image1)), hex(id(image2)), hex(id(image3)), hex(id(image4)))
print(image1 is image2, image1 is image3, image2 is image3, image1 is image4)

plt.imshow(image2[:, :, ::-1])
plt.title("image2 = image1")
# plt.show()

plt.imshow(image3[:, :, ::-1])
plt.title("image3 = image1.copy()")
# plt.show()

copy1 = image1.copy()
for i in range(0,20):
    cv2.line(copy1, (200,80+20*i), (480,80+20*i), (255,255-10*i,0+10*i),
             thickness=5, lineType=cv2.LINE_AA)

plt.imshow(copy1[:,:,::-1])
plt.show()