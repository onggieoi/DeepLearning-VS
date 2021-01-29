# Depth Estimation and Segmentation

## Capturing frames from a depth camera
The concept that a computer can have multiple video capture devices and each device can have multiple
channels. Suppose a given device is a depth camera. Each channel might correspond to a
different lens and sensor. Also, each channel might correspond to different kinds of data,
such as a normal color image versus a depth map. OpenCV, via its optional support for
OpenNI 2, allows us to request any of the following channels from a depth camera (though
a given camera might support only some of these channels):
- `cv2.CAP_OPENNI_DEPTH_MAP`: This is a depth map—a grayscale image in which
each pixel value is the estimated distance from the camera to a surface.
Specifically, each pixel value is a 16-bit unsigned integer representing a depth
measurement in millimeters.
- `cv2.CAP_OPENNI_POINT_CLOUD_MAP`: This is a point cloud map—a color image
in which each color corresponds to an x, y, or z spatial dimension. Specifically,
the channel yields a BGR image, where B is x (blue is right), G is y (green is up),
and R is z (red is deep), from the camera's perspective. The values are in meters.
- `cv2.CAP_OPENNI_DISPARITY_MAP` or `cv2.CAP_OPENNI_DISPARITY_MAP_32F`:
These are disparity maps—grayscale images in which each pixel value is the
stereo disparity of a surface. To conceptualize stereo disparity, let's suppose we
overlay two images of a scene, shot from different viewpoints. The result would
be similar to seeing double. For points on any pair of twin objects in the scene,
we can measure the distance in pixels. This measurement is the stereo disparity.
Nearby objects exhibit greater stereo disparity than far-off objects. Thus, nearby
objects appear brighter in a disparity map. cv2.CAP_OPENNI_DISPARITY_MAP is
a disparity map with 8-bit unsigned integer values and
- `cv2.CAP_OPENNI_DISPARITY_MAP_32F` is a disparity map with 32-bit floatingpoint values.
- `cv2.CAP_OPENNI_VALID_DEPTH_MASK`: This is a valid depth mask that shows
whether the depth information at a given pixel is believed to be valid (shown by
a non-zero value) or invalid (shown by a value of zero). For example, if the depth
camera depends on an infrared illuminator (an infrared flash), depth information
is invalid in regions that are occluded (shadowed) from this light.
- `cv2.CAP_OPENNI_BGR_IMAGE`: This is an ordinary BGR image from a camera
that captures visible light. Each pixel's B, G, and R values are unsigned 8-bit
integers.
- `cv2.CAP_OPENNI_GRAY_IMAGE`: This is an ordinary monochrome image from a
camera that captures visible light. Each pixel value is an unsigned 8-bit integer.
- `cv2.CAP_OPENNI_IR_IMAGE`: This is a monochrome image from a camera that
captures infrared (IR) light, specifically the near infrared (NIR) part of the
spectrum. Each pixel value is an unsigned 16-bit integer. Typically, the camera
will not actually use this entire 16-bit range but, instead, just a portion of it such
as a 10-bit range; still, the data type is a 16-bit integer. Although NIR light is
invisible to the human eye, it is physically quite similar to red light. Thus, NIR
images from a camera do not necessarily look strange to a human being.
However, a typical depth camera not only captures NIR light, but also projects a
grid-like pattern of NIR lights for the benefit of the depth-finding algorithm.
Thus, we might see a recognizable face in the depth camera's NIR image, but the
face might be dotted with bright white lights.

## Converting 10-bit images to 8-bit
Some of the channels of a depth camera use a range larger than 8 bits for their data. 
A large range tends to be useful for computations, but inconvenient for display, since 
most computer monitors are only capable of using an 8-bit range, [0, 255], per channel.

OpenCV's `cv2.imshow` function *re-scales* and *truncates* the given input data in order to
convert the image for display. Specifically, if the input image's data type is unsigned 16-bit
or signed 32-bit integers, `cv2.imshow` divides the data by 256 and truncates it to the 8-bit
unsigned integer range, [0, 255]. If the input image's data type is 32-bit or 64-bit floatingpoint 
numbers, `cv2.imshow` assumes that the data's range is [0.0, 1.0], so it multiplies the
data by 255 and truncates it to the 8-bit unsigned integer range, [0, 255]. By re-scaling the
data, `cv2.imshow` is relying on its naive assumptions about the original scale. These
assumptions will be wrong in some cases

## Creating a mask from a disparity map
The image contains some other content that is not of interest. By analyzing the disparity map, 
we can tell that some pixels within the rectangle are outliers—too near or too far to really 
be a part of the face or another object of interest.

To identify outliers in the disparity map, we first find the median using `numpy.median`,
which takes an array as an argument. If the array is of an odd length, median returns the
value that would lie in the middle of the array if the array were sorted. If the array is of an
even length, median returns the average of the two values that would be sorted nearest to
the middle of the array.

To generate a mask based on per-pixel Boolean operations, we use `numpy.where` with
three arguments. In the first argument, where takes an array whose elements are evaluated
for truth or falsity. An output array of the same dimensions is returned. Wherever an
element in the input array is True, the where function's second argument is assigned to the
corresponding element in the output array. Conversely, wherever an element in the input
array is False, the where function's third argument is assigned to the corresponding
element in the output array.

## Depth estimation with a normal camera
A typical depth camera does not work well outdoors because the
infrared component of sunlight is much brighter than the camera's own infrared light
source. Blinded by the sun, the camera cannot see the infrared pattern that it normally uses
to estimate depth.

As an alternative, we can use one or more normal cameras and we can estimate relative
distances to objects based on triangulation from different camera perspectives. If we use
two cameras simultaneously, this approach is called `stereo vision`. If we use one camera,
but we move it over time to obtain different perspectives, this approach is called `structure
from motion`. Broadly, techniques for stereo vision are also helpful in SfM, but in SfM we
face additional problems if we are dealing with a moving subject.

More to the point,` epipolar geometry` is the foundation of stereo vision. Conceptually, it 
traces imaginary lines from the camera to each object in the image, then does the same on 
the second image, and calculates the distance to an object based on the intersection of the 
lines corresponding to the same object.

OpenCV's `cv2.StereoSGBM` class. SGBM stands for semiglobal block matching, which is an algorithm 
used for computing disparity maps.

The parameters supported by `StereoSGBM`:
- `minDisparity`: Minimum possible disparity value. Normally, it is zero, but sometimes
rectification algorithms can shift images so this parameter needs to be
adjusted accordingly.
- `numDisparities`: Maximum disparity minus minimum disparity. The value is always
greater than zero. In the current implementation, this parameter must
be divisible by 16.
- `blockSize`:  Matched block size. It must be an odd number >=1 . Normally, it should
be somewhere in the 3-11 range.
- `P1`: The first parameter controlling the disparity smoothness.
- `P2`: The second parameter controlling the disparity smoothness. The larger the values, 
the smoother the disparity. P1 is the penalty on the disparity change by plus or minus 1 
between neighbor pixels. P2 is the penalty on the disparity change by more than 1 between 
neighbor pixels. The algorithm requires P2 > P1.
- `disp12MaxDiff`: Maximum allowed difference (in integer pixel units) in the left-right
disparity check. Set it to a non-positive value to disable the check.
- `preFilterCap`: Truncation value for the prefiltered image pixels. The algorithm first
computes the x-derivative at each pixel and clips its value by the `[-preFilterCap, preFilterCap] `
interval. The resulting values are passed to the Birchfield-Tomasi pixel cost function.
- `uniquenessRatio`: Margin in percentage by which the best (minimum) computed cost
function value should win the second best value to consider the found
match correct. Normally, a value within the 5-15 range is good enough.
- `speckleWindowSize`: Maximum size of smooth disparity regions to consider their noise
speckles and invalidate. Set it to 0 to disable speckle filtering.
Otherwise, set it somewhere in the 50-200 range.
- `speckleRange`: Maximum disparity variation within each connected component. If you
do speckle filtering, set the parameter to a positive value; it will be
implicitly multiplied by 16. Normally, 1 or 2 is good enough.
- `mode`: Set it to `StereoSGBM::MODE_HH` to run the full-scale, two-pass dynamic programming 
algorithm. It will consume `O(W*H*numDisparities)` bytes, which is large for 640x480 stereo and
huge for HD-size pictures. By default, it is set to false.

## Foreground detection with the GrabCut algorithm
Calculating a disparity map is a useful way to segment the foreground and background of
an image, but `StereoSGBM` is not the only algorithm that can accomplish this and, in fact,
`StereoSGBM` is more about gathering three-dimensional information from two-dimensional
pictures than anything else. `GrabCut`, however, is a perfect tool for foreground/background
segmentation. The `GrabCut` algorithm consists of the following steps:
1. A rectangle including the subject(s) of the picture is defined.
2. The area lying outside the rectangle is automatically defined as a background.
3. The data contained in the background is used as a reference to distinguish
background areas from foreground areas within the user-defined rectangle.
4. A Gaussian Mixture Model (GMM) models the foreground and background,
and labels undefined pixels as probable background and probable foreground.
5. Each pixel in the image is virtually connected to the surrounding pixels through
virtual edges, and each edge is assigned a probability of being foreground or
background, based on how similar it is in color to the pixels surrounding it.
6. Each pixel (or node as it is conceptualized in the algorithm) is connected to either
a foreground or a background node
7. After the nodes have been connected to either terminal (the background or
foreground, also called the source or sink, respectively), the edges between nodes
belonging to different terminals are cut (hence the name, GrabCut). Thus, the
image is segmented into two parts.

## Image segmentation with the Watershed algorithm
The algorithm is called `Watershed` because its conceptualization involves water. Imagine areas with 
low density (little to no change) in an image as valleys, and areas with high density (lots of change) as
peaks. Start filling the valleys with water to the point where water from two different
valleys is about to merge. To prevent the merging of water from different valleys, you build
a barrier to keep them separated. The resulting barrier is the image segmentation.
1. converting the image from color to grayscale, run a threshold on it. This
operation helps by dividing the image into two regions, blacks and whites
2. remove noise from the thresholded image by applying a morphological
transformation to it. `Morphology` consists of `dilating` (expanding) or `eroding`
(contracting) the white regions of the image in some series of steps.
apply the morphological open operation, which consists of an erosion step
followed by a dilation step. The open operation makes big white regions swallow
up little black regions (noise), while leaving big black regions (real objects)
relatively unchanged. The `cv2.morphologyEx` function, with the `cv2.MORPH_OPEN` argument
3. By dilating (`dilate`) the result of the open transformation, we can obtain regions of the
image that are most certainly background
4. obtained the distanceTransform representation of the image,
we apply a threshold to select regions that are most surely part of the
foreground
5. what about the regions in between? We can find these unsure or unknown
regions by subtracting (`subtract`) the sure foreground from background
6.  build our famous barriers to stop the water from merging. This is done with the `connectedComponents` 
function. We took a glimpse at graph theory when we analyzed the GrabCut algorithm and
conceptualized an image as a set of nodes that are connected by edges. Given the
sure foreground areas, some of these nodes will be connected together, but some
will not. The disconnected nodes belong to different water valleys, and there
should be a barrier between them
7. add 1 to the labels for all regions because we only want unknowns to stay at 0
8. open the gates! Let the water flow! The `cv2.watershed` function
assigns the label -1 to pixels that are edges between components