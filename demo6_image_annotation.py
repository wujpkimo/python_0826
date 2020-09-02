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
# plt.show()
plt.clf()
copy2 = image1.copy()
for i in range(0,10):
    cv2.circle(copy2,(250, 5+70*i),100,(0,0+20*i, 255-20*i),
               thickness=5+2*i, lineType=cv2.LINE_AA)
plt.imshow(copy2[:, :, ::-1])
plt.clf()

copy3 = image1.copy()
for i in range(0,10):
    cv2.circle(copy3, (250 + 70*i, 5+70*i), (50+7*i), (0, 0+20*i, 255-20*i),
               thickness=-1, lineType=cv2.LINE_AA)
plt.imshow(copy3[:, :, ::-1])
# plt.show()
# plt.clf()

copy4 = image1.copy()
for i in range(0, 10):
    cv2.ellipse(copy4, (400, 300), (300 - 20 * i, 100 + 40 * i),
                30, 0, 360, (255, 0, 0),
                thickness=3, lineType=cv2.LINE_AA)
plt.imshow(copy4[:, :, ::-1])
# plt.show()

copy5 = image1.copy()
for i in range(0, 10, 2):
    cv2.ellipse(copy5, (400, 300), (300 - 20 * i, 100 + 40 * i),
                0, 36 * i, 360, (255-25*i, 0+25*i, 0),
                thickness=-1, lineType=cv2.LINE_AA)
plt.imshow(copy5[:, :, ::-1])
plt.show()
plt.clf()

copy6 = image1.copy()
text1 = "Gigabyte"
cv2.putText(copy6, text1, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2,
            (255, 0, 0), thickness=5, lineType=cv2.LINE_AA)
cv2.putText(copy6, text1.upper(), (100, 400), cv2.FONT_HERSHEY_SIMPLEX, 2,
            (0, 255, 0), thickness=5, lineType=cv2.LINE_AA)
plt.imshow(copy6[:, :, ::-1])
plt.show()

