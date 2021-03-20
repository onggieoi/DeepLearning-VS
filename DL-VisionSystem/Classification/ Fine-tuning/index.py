from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.applications import imagenet_utils
from keras.applications import vgg16
from keras.optimizers import Adam, SGD
from keras.metrics import categorical_crossentropy

from keras.layers import Dense, Flatten, Dropout, BatchNormalization
from keras.models import Model

from sklearn.metrics import confusion_matrix
import itertools
import matplotlib.pyplot as plt

from keras.callbacks import ModelCheckpoint

from sklearn.datasets import load_files
from keras.utils import np_utils
import numpy as np

from keras.applications.vgg16 import preprocess_input
from tqdm import tqdm

from sklearn.metrics import confusion_matrix

train_path = 'dataset/train'
valid_path = 'dataset/valid'
test_path = 'dataset/test'

# ImageDataGenerator generates batches of tensor image data with real-time data augmentation.
# The data will be looped over (in batches).
# in this example, we won't be doing any image augmentation
train_batches = ImageDataGenerator().flow_from_directory(
    train_path, target_size=(224, 224), batch_size=10)

valid_batches = ImageDataGenerator().flow_from_directory(
    valid_path, target_size=(224, 224), batch_size=30)

test_batches = ImageDataGenerator().flow_from_directory(
    test_path, target_size=(224, 224), batch_size=50, shuffle=False)

base_model = vgg16.VGG16(
    weights="imagenet", include_top=False, input_shape=(224, 224, 3), pooling='avg')
# base_model.summary()

# lock classification layers to make them not trainable with this code
for layer in base_model.layers[:-5]:
    layer.trainable = False
# base_model.summary()

# use “get_layer” method to save the last layer of the network
last_layer = base_model.get_layer('global_average_pooling2d_1')

# save the output of the last layer to be the input of the next layer
last_output = last_layer.output

# add our new softmax layer with 3 hidden units
x = Dense(10, activation='softmax', name='softmax')(last_output)

# instantiate a new_model using keras’s Model class
new_model = Model(inputs=base_model.input, outputs=x)

# new_model.summary()

# Train New Model
new_model.compile(
    Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

checkpointer = ModelCheckpoint(
    filepath='signlanguage.model.hdf5', save_best_only=True)

history = new_model.fit_generator(train_batches, steps_per_epoch=18,
                                  validation_data=valid_batches, validation_steps=3, epochs=20, verbose=1, callbacks=[checkpointer])

# create the confusion matrix to evaluate the model


def load_dataset(path):
    data = load_files(path)
    paths = np.array(data['filenames'])
    targets = np_utils.to_categorical(np.array(data['target']))
    return paths, targets


test_files, test_targets = load_dataset('dataset/test')


def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)


def paths_to_tensor(img_paths):
    list_of_tensors = [path_to_tensor(img_path)
                       for img_path in tqdm(img_paths)]
    return np.vstack(list_of_tensors)


test_tensors = preprocess_input(paths_to_tensor(test_files))

new_model.load_weights('signlanguage.model.hdf5')

print('\nTesting loss: {:.4f}\nTesting accuracy: {:.4f}'.format(
    *new_model.evaluate(test_tensors, test_targets)))

# Plot
cm_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

cm = confusion_matrix(np.argmax(test_targets, axis=1),
                      np.argmax(new_model.predict(test_tensors), axis=1))
plt.imshow(cm, cmap=plt.cm.Blues)
plt.colorbar()
indexes = np.arange(len(cm_labels))

for i in indexes:
    for j in indexes:
        plt.text(j, i, cm[i, j])

plt.xticks(indexes, cm_labels, rotation=90)
plt.xlabel('Predicted label')
plt.yticks(indexes, cm_labels)
plt.ylabel('True label')
plt.title('Confusion matrix')
plt.show()
