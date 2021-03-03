# Setting Up OpenCV

OpenCV stands for Open Source Computer Vision

source code:  https://github.com/opencv/opencv

It is a free computer vision library that allows to manipulate images and videos to accomplish a variety 
of tasks, from displaying frames from a webcam to teaching a robot to recognize real-life objects

The opencv_contrib modules, which offer additional functionality that is maintained by the OpenCV community 
rather than the core development team

Dependencies:
- NumPy: a dependency of OpenCV's Python bindings. It provides numeric computing functionality, including 
efficient arrays.
- SciPy: a scientific computing library that is closely related to NumPy. It is not required by OpenCV, 
but it is useful to manipulate data in OpenCV images.
- OpenNI 2: an optional dependency of OpenCV. It adds support for certain depth cameras
such as the Asus Xtion PRO.

## What's new in OpenCV 4
- `The C++ implementation` of OpenCV has been updated to `C++11`. OpenCV's Python bindings wrap the C++
implementation, so as Python users, we may gain some performance advantages from this update, even though 
we are not using C++ directly.
- Many new machine learning models are available in `OpenCV's DNN module`.
- `The KinectFusion algorithm` (for three-dimensional reconstruction using a Microsoft Kinect 2 camera) is now 
supported.
- `The DIS algorithm` for dense optical flow has been added.
- A new module has been added for detecting and decoding `QR codes`.

## Setup

Python offers some built-in tools that are useful for setting up a `development environment`. These tools 
include a package manager called `pip` and a virtual environment manager called `venv`.

Using a ready-made OpenCV package
> `pip install opencv-contrib-python`

or  include non-free content, such as patented algorithms
> `pip install opencv-contrib-python-nonfree`

Build OpenCV from source

> In order to enable nonstandard features, such as support for depth cameras via OpenNI 2. OpenCV's build 
system uses `CMake` for configuring the system and Visual Studio for compilation.

The build configuration process requires CMake 3 or a later version