import numpy
import cv2
import os


# convert color
img = numpy.zeros((3, 3), dtype=numpy.uint8)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# imread mode
grayImage = cv2.imread('../../image.jpg', cv2.IMREAD_GRAYSCALE)

# change format
image = cv2.imread('../../image.jpg')
cv2.imwrite('MyPic.png', image)

##### convert bytearray that contains random bytes into a grayscale image and a BGR image ##

# Make an array of 120,000 random bytes.
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)  # generate random raw bytes
# Convert the array to make a 400x300 grayscale image.
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('RandomGray.png', grayImage)
# Convert the array to make a 400x100 color image.
bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('RandomColor.png', bgrImage)

#### Access img with numpy.array ####

#  turn a pixel at coordinates (0, 0) into a white pixel
img[0, 0] = [255, 255, 255]

# Sets the value of a pixel's blue channel
img.itemset((150, 120, 0), 255)


# Read Video
videoCapture = cv2.VideoCapture('../../video.mp4')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter(
    'MyOutputVid.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'),
    fps, size)
success, frame = videoCapture.read()
while success:  # Loop until there are no more frames.
    videoWriter.write(frame)
    success, frame = videoCapture.read()
