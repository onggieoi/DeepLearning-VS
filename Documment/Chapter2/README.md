# Handling Files, Cameras, and GUIs

## Basic I/O scripts
Most CV applications need to get images as input. Most also produce images as output. An interactive 
CV application might require a camera as an input source and a window as an output destination. However, 
other possible sources and destinations include image files, video files, and raw bytes.

## Reading/writing an image file
OpenCV provides the `imread` function to load an image from a file and the `imwrite` function to write an 
image to a file. These functions support various file formats for still images (*not videos*). The 
supported formats vary—as formats can be added or removed in a custom build of OpenCV but normally BMP, 
PNG, JPEG, and TIFF are among the supported formats.

An image is a multidimensional array; it has columns and rows of pixels, and each pixel has a value. 
For different kinds of image data, the pixel value may be formatted in different ways.

- Grayscale image: where `0 is black`, `255 is white`, and the in-between values are shades of `gray`.
- Blue-green-red (BGR) format using the `cv2.cvtColor`. each pixel is now represented by a three-element 
array, with each integer representing one of the three color channels: B, G, and R.
- HSV color model has a range of 0-180

By default, `imread` returns an image in the BGR color format even if the file uses a grayscale format. BGR 
represents the same color model as red-green-blue (RGB), but the byte order is reversed.

Optionally, we may specify the mode of `imread`
- `cv2.IMREAD_COLOR`: This is the default option, providing a 3-channel BGR image with an 8-bit value 
(0-255) for each channel.
- `cv2.IMREAD_GRAYSCALE`: This provides an 8-bit grayscale image.
- `cv2.IMREAD_ANYCOLOR`: This provides either an 8-bit-per-channel BGR image or an 8-bit grayscale image, 
depending on the metadata in the file.
- `cv2.IMREAD_UNCHANGED`: This reads all of the image data, including the alpha or transparency channel 
(if there is one) as a fourth channel.
- `cv2.IMREAD_ANYDEPTH`: This loads an image in grayscale at its original bit depth. For example, it provides 
a 16-bit-per-channel grayscale image if the file represents an image in this format.
- `cv2.IMREAD_ANYDEPTH `| `cv2.IMREAD_COLOR`: This combination loads an image in BGR color at its original 
bit depth.
- `cv2.IMREAD_REDUCED_GRAYSCALE_2`: This loads an image in grayscale at half its original resolution. 
For example, if the file contains a 640 x 480 image, it is loaded as a 320 x 240 image.
- `cv2.IMREAD_REDUCED_COLOR_2`: This loads an image in 8-bit-per-channel BGR color at half its original 
resolution.
- `cv2.IMREAD_REDUCED_GRAYSCALE_4`: This loads an image in grayscale at onequarter of its original 
resolution.
- `cv2.IMREAD_REDUCED_COLOR_4`: This loads an image in 8-bit-per-channel color at one-quarter of its 
original resolution.
- `cv2.IMREAD_REDUCED_GRAYSCALE_8`: This loads an image in grayscale at oneeighth of its original resolution.
- `cv2.IMREAD_REDUCED_COLOR_8`: This loads an image in 8-bit-per-channel color at one-eighth of its 
original resolution.

## Converting between an image and raw bytes

Conceptually, a byte is an integer ranging from 0 to 255. Throughout real-time graphic applications today,
a pixel is typically represented by one byte per channel, though other representations are also possible.

- An OpenCV image is a 2D or 3D array of the `numpy.array` type
- An 8-bit grayscale image is a 2D array containing byte values
- A 24-bit BGR image is a 3D array, which also contains byte values

image[0, 0] or image[0, 0, 0]

- The first index is the pixel's y coordinate or row, 0 being the top. 
- The second index is the pixel's x coordinate or column, 0 being the leftmost. 
- The third index (if applicable) represents a color channel. The array's three dimensions can be visualized 
in the following `Cartesian coordinate system`.

## Accessing image data with `numpy.array`

The numpy.array class is greatly optimized for array operations, and it allows certain kinds of bulk 
manipulations that are not available in a plain Python list. These kinds of numpy.array type-specific 
operations come in handy for image manipulations in OpenCV.

The` numpy.array` type provides a handy method, `item`, which takes three parameters: the x (or left) 
position, the y (or top) position, and the index within the array at the (x, y) position (remember that 
in a BGR image, the data at a certain position is a three-element array containing the B, G, and R values 
in this order) and returns the value at the index position. 

Another method, `itemset`, sets the value of a  particular channel of a particular pixel to a specified 
value. itemset takes two arguments: a threeelement tuple (x, y, and index) and the new value.

There are several interesting things we can do by accessing raw pixels with NumPy's array
slicing; one of them is defining regions of interests (ROI). Once the region is defined, we
can perform a number of operations.

Access the properties of numpy.array:
- `shape`: This is a tuple describing the shape of the array. For an image, it contains
(in order) the height, width, and—if the image is in color—the number of
channels. The length of the shape tuple is a useful way to determine whether an
image is grayscale or color
- `size`: This is the number of elements in the array. In the case of a grayscale
image, this is the same as the number of pixels. In the case of a BGR image, it is
three times the number of pixels because each pixel is represented by three
elements (B, G, and R).
- dtype: This is the datatype of the array's elements. For an 8-bit-per-channel
image, the datatype is numpy.uint8.

## Reading/writing a video file
OpenCV provides the `VideoCapture` and `VideoWriter` classes, which support various
video file formats. The supported formats vary depending on the operating system and the
build configuration of OpenCV, but normally it is safe to assume that the AVI format is
supported. Via its read method, a VideoCapture object may be polled for new frames
until it reaches the end of its video file. Each frame is an image in a BGR format.

Conversely, an image may be passed to the `write` method of the `VideoWriter` class,
which appends the image to a file in `VideoWriter`. 