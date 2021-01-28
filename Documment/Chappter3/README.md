# Processing Images with OpenCV

## Converting images between different color models
- Grayscale is a model that reduces color information by translating it into shades
of gray or brightness. This model is extremely useful for the intermediate
processing of images in problems where brightness information alone is
sufficient, such as face detection. Typically, each pixel in a grayscale image is
represented by a single 8-bit value, ranging from 0 for black to 255 for white.
- BGR is the blue-green-red color model, in which each pixel has a triplet of values
representing the blue, green, and red components or channels of the pixel's color.
Web developers, and anyone who works with computer graphics, will be
familiar with a similar definition of colors, except with the reverse channel order,
red-green-blue (RGB). Typically, each pixel in a BGR image is represented by a
triplet of 8-bit values, such as [0, 0, 0] for black, [255, 0, 0] for blue, [0,
255, 0] for green, [0, 0, 255] for red, and [255, 255, 255] for white.
- The HSV model uses a different triplet of channels. Hue is the color's tone,
saturation is its intensity, and value represents its brightness.

By default, OpenCV uses the BGR color model (with 8 bits per channel) to represent any
image that it loads from a file or captures from a camera.

## Light is not paint
For newcomers to the BGR color space, it might seem that things **do not** add up properly:
for example, the (0, 255, 255) triplet (no blue, full green, and full red) produces the
color yellow. If you have an artistic background, you won't even need to pick up paints and
brushes to know that green and red paint mix together into a muddy shade of brown.
However, the color models that are used in computing are called additive models and they
deal with lights. Lights behave differently from paints (which follow a subtractive color
model), and since software runs on a computer whose medium is a monitor that emits
light, the color model of reference is the additive one.

## Exploring the Fourier transform

### HPFs and LPFs
An HPF is a filter that examines a region of an image and boosts the intensity of certain
pixels based on the difference in the intensity of the surrounding pixels.
- A kernel is a set of weights that are applied to a region in a source image
to generate a single pixel in the destination image.

The preceding kernel gives us the average difference in intensity between the central pixel
and all its immediate horizontal neighbors. If a pixel stands out from the surrounding
pixels, the resulting value will be high. This type of kernel represents a so-called high-boost
filter, which is a type of HPF, and it is particularly effective in edge detection.

## Edge detection

OpenCV provides many edge-finding filters, including `Laplacian`, `Sobel`, and `Scharr`.
These filters are supposed to turn non-edge regions into black and turn edge regions into
white or saturated colors. However, they are prone to misidentifying noise as edges. This
flaw can be mitigated by blurring an image before trying to find its edges. OpenCV also
provides many blurring filters, including `blur` (a simple average), `medianBlur`, and
`GaussianBlur`. The arguments for the edge-finding and blurring filters vary but always
include ksize, an odd whole number that represents the width and height (in pixels) of a
filter's kernel.

## Custom kernels – getting convoluted
many of OpenCV's predefined filters use a kernel. Remember that a kernel is a set of weights that 
determines how each output pixel is calculated from a neighborhood of input pixels. Another term 
for a kernel is a convolution matrix. It mixes up or convolves the pixels in a region. Similarly, 
a kernel-based filter may be called a convolution filter.

OpenCV provides a very versatile `filter2D()` function, which applies any kernel or
convolution matrix that we specify.

## Edge detection with Canny
The Canny edge detection algorithm is complex but also quite interesting. It is a five-step
process:
- Denoise the image with a Gaussian filter.
- Calculate the gradients.
- Apply non-maximum suppression (NMS) on the edges. Basically, this means that the algorithm 
selects the best edges from a set of overlapping edges. We'll discuss the concept of NMS in 
detail in Chapter 7, Building Custom Object Detectors.
- Apply a double threshold to all the detected edges to eliminate any false positives.
- Analyze all the edges and their connection to each other to keep the real edges
and discard the weak ones.

After finding Canny edges, we can do further analysis of the edges in order to determine
whether they match a common shape, such as a line or a circle. The Hough transform is one
algorithm that uses Canny edges in this way

## Contour detection
A vital task in computer vision is contour detection. To detect contours or outlines
of subjects contained in an image or video frame, not only as an end in itself but also as a
step toward other operations. These operations are, namely, computing bounding
polygons, approximating shapes, and generally calculating regions of interest (ROIs).
ROIs considerably simplify interaction with image data because a rectangular region in
NumPy is easily defined with an array slice.