import cv2
import matplotlib.pyplot as plt
import matplotlib

imagePath = "./photos/transparent.gif"

# (imagePath, 0) ==> B/W 1 channel
# (imagePath, 1) ==> BGR 3 channels
# (imagePath, -1) ==> keep original settings
image1 = cv2.imread(imagePath, -1)
plt.imshow(image1)
plt.show()
print("original image dimension={}".format(image1.shape))
matplotlib.rcParams['image.cmap'] = 'gray'
image1BGR = image1[:, :, 0:3]
image1MASK = image1[:, :, 3]
plt.figure(figsize=[10, 5])
plt.subplot(1, 2, 1)
plt.imshow(image1BGR[:, :, ::-1])
plt.title("color channel")
plt.subplot(1, 2, 2)
plt.imshow(image1MASK)
plt.title("alpha channel")
plt.show()
