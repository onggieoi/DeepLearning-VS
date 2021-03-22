# scenario 3: A pretrained network as a feature extractor 
- The target dataset is small and very different from the source dataset.
- use the VGG16 network trained on the ImageNet dataset. 

## The details of dataset:
- Number of classes = 10 (digits 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9)
- Image size = 100 × 100
- Color space = RGB
- 1,712 images in the training set
- 300 images in the validation set
- 50 images in the test set

### Dataset Preview:

| <img src="examples/example_0.JPG"> | <img src="examples/example_1.JPG"> | <img src="examples/example_2.JPG"> | <img src="examples/example_3.JPG"> | <img src="examples/example_4.JPG"> |
| :--------------------------------: | :--------------------------------: | :--------------------------------: | :--------------------------------: | :--------------------------------: |
|                 0                  |                 1                  |                 2                  |                 3                  |                 4                  |
| <img src="examples/example_5.JPG"> | <img src="examples/example_6.JPG"> | <img src="examples/example_7.JPG"> | <img src="examples/example_8.JPG"> | <img src="examples/example_9.JPG"> |
|                 5                  |                 6                  |                 7                  |                 8                  |                 9                  |

## The process to fine-tune a pretrained network is as follows:
1. Import the necessary libraries.
2. Preprocess the data to make it ready for the neural network.
3. Load in pretrained weights from the VGG16 network trained on a large dataset (ImageNet).
4. Freeze part of the feature extractor part.
5. Add the new classifier layers.
6. Compile the network, and run the training process to optimize the model for the smaller dataset.
7. Evaluate the model.