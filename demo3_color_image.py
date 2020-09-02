import cv2
import matplotlib
import matplotlib.pyplot as plt

IMAGE_PATH = "./photos/demo3.color.jpg"
image1 = cv2.imread(IMAGE_PATH)

print(dir(image1))
print("image dimension={}".format(image1.shape))

plt.imshow(image1)
plt.title("load image directly from jpg")
plt.show()
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

plt.imshow(image2)
plt.title("load image, transfer blue&Red channel")
plt.show()

image3 = image1[:, :, ::-1]
plt.imshow(image3)
plt.title("load image, reverse order color channel")
plt.show()

matplotlib.rcParams['image.cmap'] = 'gray'
plt.figure(figsize=[20, 5])
plt.subplot(131)
plt.imshow(image1[:, :, 0])
plt.title("B channel")
plt.subplot(132)  # 一列三欄的第二欄
plt.imshow(image1[:, :, 1])
plt.title("G channel")
plt.subplot(133)  # 一列三欄的第三欄
plt.imshow(image1[:, :, 2])
plt.title("R channel")
plt.show()

b, g, r = cv2.split(image1)
plt.figure(figsize=[18,5])
plt.subplot(1,4,1)
plt.imshow(b)
plt.title("blue channel")
plt.subplot(1,4,2)
plt.imshow(g)
plt.title("green channel")
plt.subplot(1,4,3)
plt.imshow(r)
plt.title("red channel")
plt.subplot(1,4,4)
imageMerged = cv2.merge((b,g,r))
plt.imshow(imageMerged[:,:,::-1])
plt.title("merge output")
plt.show()
