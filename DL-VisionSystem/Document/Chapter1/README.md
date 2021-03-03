# Computer vision

## 1 Components of the vision system
***
The core concept of any AI system is that it can perceive its environment and take
actions based on its perceptions. Computer vision is concerned with the `visual perception` 
part: it is the science of perceiving and understanding the world through images
and videos by constructing a physical model of the world so that an AI system can then
take appropriate actions. For humans, vision is only one aspect of perception.

### 1.1 Visual perception
Visual perception, at its most basic, is the act of observing patterns and objects through
sight or visual input.

### 1.2 Vision systems
Scientists were inspired by the human vision system and in recent years have done an
amazing job of copying visual ability with machines. To mimic the human vision system, need 
two main components: a sensing device to mimic the function of the eye and a powerful 
algorithm to mimic the brain function in interpreting and classifying image content.

### 1.3 Sensing devices
Vision systems are designed to fulfill a specific task. An important aspect of design is
selecting the best sensing device to capture the surroundings of a specific environment, whether that is a camera, radar, X-ray, CT scan, Lidar, or a combination of
devices to provide the full scene of an environment to fulfill the task at hand.

### 1.4 Interpreting devices
The interpreter is the brain of the vision system. Its role is to take the output image 
from the sensing device and learn features and patterns to identify objects. Scientists 
were inspired by how our brains work and tried to reverse engineer the central nervous system to get some insight on how to build an artificial brain.

The learning behavior of biological neurons inspired scientists to create a network
of neurons that are connected to each other. Imitating how information is processed
in the human brain, each artificial neuron fires a signal to all the neurons that it’s connected to when enough of its input signals are activated. Thus, neurons have a very
simple mechanism on the individual level, but when millions of these neurons stacked in 
layers and connected together, each neuron is connected to thousands of other neurons, 
yielding a learning behavior. Building a multilayer neural network is called deep learning.

DL methods learn representations through a sequence of transformations of data
through layers of neurons. 

## 2 Applications of computer vision
***
### 2.1 Image classification

Image classification is the task of assigning to an image a label from a predefined set 
of categories. A convolutional neural network is a neural network type that truly shines 
in processing and classifying images in many different applications:
- **Lung cancer diagnosis**: DL networks, specifically CNNs, are now able to learn these 
  features automatically from X-ray and CT scan images and detect small nodules early,
  before they become deadly
- **Traffic sign recognition**

### 2.2 Object detection and localization

Image classification problems are the most basic applications for CNNs. In these problems, each image contains only one object, and the task is to identify it. But if 
aim to reach human levels of understanding, have to add complexity to these networks
so they can recognize multiple objects and their locations in an image. To do that, it 
can be build object detection systems like YOLO (you only look once), SSD (single-shot
detector), and Faster R-CNN, which not only classify images but also can locate and 
detect each object in images that contain multiple objects. These DL systems can look at an image, break it up into smaller regions, and label each region with a class so that a 
variable number of objects in a given image can be localized and labeled. it can be imagined that such a task is a basic prerequisite for applications like autonomous systems

### 2.3 Generating art (style transfer)
Neural style transfer, one of the most interesting CV applications, is used to transfer 
the style from one image to another. The basic idea of style transfer is this: take one 
image—say, of a city—and then apply a style of art to that image—say, The Starry Night
(by Vincent Van Gogh)—and output the same city from the original image, but looking as though it was painted by Van Gogh.

### 2.4 Creating images
In 2014, Ian Goodfellow invented a new DL model that can imagine new things called 
generative adversarial networks (GANs).  GANs are sophisticated DL models that generate 
stunningly accurate synthesized images of objects, people, and places, among other 
things. If you give them a set of images, they can make entirely new, realistic-looking 
images. For example, StackGAN is one of the GAN architecture variations that can use a 
textual description of an object to generate a high-resolution image of the object 
matching that description. This is not just running an image search on a database.

### 2.5 Face recognition
Face recognition (FR) allows us to exactly identify or tag an image of a person. 
Day-today applications include searching for celebrities on the web and auto-tagging 
friends and family in images. Face recognition is a form of fine-grained classification.

The famous categorizes two modes of an FR system:
- `Face identification`: Face identification involves one-to-many matches that compare a query face image against all the template images in the database to determine the identity of the query face. Another face recognition scenario involves
a watchlist check by city authorities, where a query face is matched to a list of
suspects (one-to-few matches).
- `Face verification`: Face verification involves a one-to-one match that compares a
query face image against a template face image whose identity is being claimed

### 2.6 Image recommendation system
In this task, a user seeks to find similar images with respect to a given query image.
Shopping websites provide product suggestions (via images) based on the selection of
a particular product, for example, showing a variety of shoes similar to those the user
selected.

## 3 Understanding the computer vision pipeline
Applications of CV vary, but a typical vision system uses a sequence of distinct steps 
to process and analyze image data. These steps are referred to as a computer vision 
pipeline. Many vision applications follow the flow of acquiring images and data, 
processing that data, performing some analysis and recognition steps, and then finally 
making a prediction based on the extracted information:
1. `Input data`: Images, videos
2. `Preprocessing`: Standardize images, Color transformation, More...
3. `Feature extraction`: Find distinguishing information about the image
4. `ML model`: Learn from the extracted features to predict and classify objects

## 4 Image Input
***
### 4.1 Image as functions
An image can be represented as a function of two variables x and y, which define a 
twodimensional area. A digital image is made of a grid of pixels. The pixel is the raw building 
block of an image. Every image consists of a set of pixels in which their values represent the 
`intensity` of light that appears in a given place in the image.

### 4.2 How computers see images
the image looks like a 2D matrix of the pixels’ values, which represent intensities across the 
color spectrum. There is no context here, just a massive pile of data.

### 4.3 Color images
In grayscale images, each pixel represents the intensity of only one color, whereas
in the standard RGB system, color images have three channels (red, green, and
blue). In other words, color images are represented by three matrices: one represents
the intensity of red in the pixel, one represents green, and one represents blue

## 5 Image preprocessing
***
The goal of this step is to make your data ready for the ML model to make it easier to analyze 
and process computationally. The same thing is true with images. Based on the problem you are
solving and the dataset in hand, some data massaging is required before you feed your
images to the ML model. 

### Converting color images to grayscale to reduce computation complexity
- `Standardizing images`: One important constraint that exists in some ML algorithms, such as 
CNNs, is the need to resize the images in your dataset to unified dimensions. This implies that 
your images must be preprocessed and scaled to have identical widths and heights before being 
fed to the learning algorithm.
- `Data augmentation`: Another common preprocessing technique involves augmenting the existing 
dataset with modified versions of the existing images. Scaling, rotations, and other affine 
transformations are typically used to enlarge your dataset and expose the neural network to a 
wide variety of variations of your images. This makes it more likely that your model will 
recognize objects when they appear in any form and shape.
- `Other technique`: Many more preprocessing techniques are available to get your
images ready for training an ML model. In some projects, you might need to
remove the background color from your images to reduce noise. Other projects
might require that you brighten or darken your images. In short, any adjustments
that you need to apply to your dataset are part of preprocessing. You will select the 
appropriate processing techniques based on the dataset at hand and the
problem you are solving

## 6 Feature extraction
***
Feature extraction is a core component of the CV pipeline. In fact, the entire DL model
works around the idea of extracting useful features that clearly define the objects in
the image. 

### 6.1 Feature in computer vision
In CV, a feature is a measurable piece of data in your image that is unique to that specific 
object. It may be a distinct color or a specific shape such as a line, edge, or image
segment. A good feature is used to distinguish objects from one another.

### 6.2 Good (useful) feature
In ML projects, there is usually no one feature that can classify all objects on its own. 
That’s why, in machine learning, we almost always need multiple features, where each feature 
captures a different type of information.

A good feature will help us recognize an object in all the ways it may appear. Characteristics 
of a good feature follow:
- Identifiable
- Easily tracked and compared
- Consistent across different scales, lighting conditions, and viewing angles
- Still visible in noisy images or when only part of an object is visible

### 6.3 Extracting features (handcrafted vs. automatic extracting)
This is a large topic in machine learning that could take up an entire book. It’s typically 
described in the context of a topic called `feature engineering`.

Some of the handcrafted feature sets are these:
- Histogram of oriented gradients (HOG)
- Haar Cascades
- Scale-invariant feature transform (SIFT)
- Speeded-Up Robust Feature (SURF)

#### DEEP LEARNING USING AUTOMATICALLY EXTRACTED FEATURES
In DL, however, we do not need to manually extract features from the image. The network extracts 
features automatically and learns their importance on the output by applying weights to its 
connections. You just feed the raw image to the network, and while it passes through the network 
layers, the network identifies patterns within the image with which to create features. Neural 
networks can be thought of as feature extractors plus classifiers that are end-to-end 
trainable, as opposed to traditional ML models that use handcrafted features.

## 7 Classifier learning algorithm
***
The classification task is done one of these ways: traditional ML algorithms like SVMs, or deep 
neural network algorithms like CNNs. While traditional ML algorithms might get decent results 
for some problems, CNNs truly shine in processing and classifying images in the most complex 
problems.

Neural networks automatically extract useful features from dataset, and they act as a classifier 
to output class labels for your images. Input images pass through the layers of the neural 
network to learn their features layer by layer. The deeper your network is (the more layers), 
the more it will learn the features of the dataset: hence the name deep learning. The last layer 
of the neural network usually acts as the classifier that outputs the class label.