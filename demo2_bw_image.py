import cv2
import matplotlib
import matplotlib.pylab as plt

imagePath = './photos/mnist0.png'
testImage = cv2.imread(imagePath,0)

print("image type={}".format(type(testImage)))
print("image dimension={}".format(testImage.shape))
print("image data type={}".format(testImage.dtype))
print("image[0][0]={}".format(testImage[0,0]))

# crop 5x5 with black
for i in range(50):
    for j in range(50):
        testImage[i][j]=0
print(testImage)

plt.imshow(testImage)
plt.show()

#config image
matplotlib.rcParams['figure.figsize']=(6.0,6.0)
matplotlib.rcParams['image.cmap']='gray'
plt.imshow(testImage)
plt.colorbar()
plt.show()