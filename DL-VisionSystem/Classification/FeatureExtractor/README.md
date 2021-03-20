# scenario 1: A pretrained network as a feature extractor
- The target dataset is small and similar to the source dataset.
- use a very small amount of data to train a classifier that detects
images of dogs and cats
- using the VGG16

The process to use a pretrained model as a feature extractor is well established:
1. Import the necessary libraries.
2. Preprocess the data to make it ready for the neural network.
3. Load pretrained weights from the VGG16 network trained on a large dataset.
4. Freeze all the weights in the convolutional layers (feature extraction part).
Remember, the layers to freeze are adjusted depending on the similarity of the
new task to the original dataset. In our case, we observed that ImageNet has a
lot of dog and cat images, so the network has already been trained to extract
the detailed features of our target object.
5. Replace the fully connected layers of the network with a custom classifier. You
can add as many fully connected layers as you see fit, and each can have as
many hidden units as you want. For simple problems like this, we will just add
one hidden layer with 64 units. You can observe the results and tune up if the
model is underfitting or down if the model is overfitting. For the softmax layer,
the number of units must be set equal to the number of classes (two units, in
our case).
6. Compile the network, and run the training process on the new data of cats and
dogs to optimize the model for the smaller dataset.
7. Evaluate the model