# Convolutional Neural Networks (CNN) & Image Augmentation

Deep dive into Convolutional Neural Network architectures for computer vision: convolution filters/kernels, stride, padding, feature maps, pooling layers, image folder generators, and data augmentation techniques to defeat overfitting.

---

## 1. Convolutional Neural Network Architecture Fundamentals

<a name='0'></a>
# Intro to Computer Vision and Convolutional Neural Networks(CNN)

### Contents 

* [1. Intro to Computer Vision with Convolutional Neural Networks(CNN)](#1)

   * [What is Convolutional Neural Networks?](#1-1)
   * [A Typical Architecture of Convolutional Neural Networks](#1-2)
* [2. Coding ConvNets: Image Classification](#2)
   * [2.1 Loading the Data](#2-1)
   * [2.2 Looking in the Data](#2-2)
   * [2.3 Preparing the data for a Model](#2-3)
   * [2.4 Creating, Compiling and Training a Model](#2-4)
   * [2.5 Visualizing the Model Results](#2-5)
   * [2.6 Evaluating the Model](#2-6)
   * [2.7 Improving a Model](#2-7)
   * [2.8 Saving and Loading](#2-8)

<a name='1'></a>
## Intro to Computer Vision with Convolutional Neural Networks

We humans we are blessed to have got the ability to interact with the real world, and make sense of things around us. With our natural vision/perception, it takes us a fractions of milliseconds to see something and quickly tell what it is. 

Computers are not like that. It is extremely hard for a machine to interact with the external environment. Thankfully, due to the advent of computation power, availability of datasets, advance in intelligent tools like TensorFlow/PyTorch, and active researchers who always surprises day after day, a number of techniques and architectures to help a machine to see the real world have been emerged. 

One of the neural networks architectures that has accelerated various computer vision applications, from image recognition, image segmentation to object detection is `Convolutional Neural Networks(CNN)`, a.k.a `ConvNets`.

CNN overcomes some of the challenges of using fully connected network(or densely connected networks) in image tasks. Fully connected networks doesn't hold spatial features, and they have many parameters which can complicate the network and thus hindering its performance.

<a name='1-1'></a>
## What is Convolutional Neural Networks(CNN)?

Convolutional Neural Networks is a neural network architecture used to exract features in data(images mosty). One special thing about CNN (that make it different to other neural networks types) is that it uses convolutional filters to extract features in images. 

Convolutional Neural Networks were inspired by the human's brain visual cortex, an area in brain that process visual information. Up to now, they are on top of many applications: image and video classification, image search, driveless cars and other autonomous vehicles, medical images diagnosis, inteligent robots, and much more.

<a name='1-2'></a>
### A Typical Architecture of Convolutional Neural Networks

CNN is made of 3 main layers, in sequential order: 

* **Convolutional layer**
* **Pooling layer**
* **Fully connected layer**

*[Diagram: Social Filters.png]*

Let's talk about each layer. 

#### 1. Convolutional layers

The convolution layers are the backbone of the whole CNN. They are used to extract the features in the images using filters. These filters learn both low-level features such as lines, edges and high-level features such as the face, ear, nose, etc...High-level features are what later become useful during image recognition.

The process of convolution is that we pass the filter to each pixel in an image, we multiply the corresponding pixels and then we calculate the sum, such sum making the new pixel. We repeat the process until the filter is slid over all image pixels.

*The image below summarizes how convolutional operation is done*

*[Diagram: CapKf4DpH.png]*

Most popular deep learning frameworks such as TensorFlow or PyTorch allow you to create the convolutional layer in one line of code. 

```
tf.keras.layers.Conv2D(.....)
```

The output of the convolutional layer will be high dimensional feature maps and its dimension will depend on the number of filters we have in a layer. Take an example, if the layer has 32 filters, then you will have 32 feature maps at the output. 

The more the filters, the many features maps you will have and that's not cool. How do we reduce the dimensions of feature maps while retaining as much as information in the image? Such question brings me to pooling layers.

#### 2. Pooling layers

Pooling layers are used to compress or shrink the feature maps. There are various pooling options but to preserve the best part of the images, Maxpooling is used. It will reduce the image size by keeping the highest pixels of the image. 

Implementing a pooling layer in many framework is very simple..

```
tf.keras.layers.MaxPooling2D(...)
```

The output of the pooling layers is reduced size feature maps. How does the network make sense of what these features represent? 

#### 3. Fully connected layers/Dense layers

At the end of the ConvNets, there is always going to be a fully connected layer whose job is to match the produced feature maps from the pooling layer with the exact labels of the original image.

Take an example. If the input image to a ConvNet layer is a human, the high-level features will be something like ear, noses, eye, face, etc. Once the neural network has learned that, these features will need to be matched to their labels. That is what fully connected layers do. 

FC layers are typically dense layers, activated with either `softmax` or `sigmoid` activation depending on the problem. 

```
tf.keras.layers.Dense(....)
```

A ConvNets may have multiple blocks of convolutional and pooling layers. The right number of these layers will depend on the scope of the work at hand and the size of the dataset.

<a name='2'></a>

## 2. Coding ConvNets: Image Classification

Image recognition is one of the common tasks in computer vision. We may be given two or more images, in two or more categories/classes and the task be to recognize them. 

In this notebook, we are going to practice ConvNets on classical dataset called `cifar10`. 

CIFAR-10 consists of 60000 colour images, in 10 classes or categories, and the good thing is that the dataset is quite balanced - each class contains 6000 images. 50.000 images are allocated for training, and 10.000 for test. 

Those 10 classes are: `airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck`. 

Although we will use cifar-10, there is a big version of cifar (cifar-100) with 100 classes. 

Cifar-10 is available in [Keras built in datasets](https://keras.io/api/datasets/cifar10/) and [TensorFlow datasets](https://www.tensorflow.org/datasets/catalog/cifar10).

<a name='2-1'></a>

## 2.1 Loading the Data

While it could easier to load the data from Keras, let's use TensorFlow datasets this time. 

We will learn along the way, and also, since TF datasets is adding many datasets, let's familiarize ourselves with how to use TensorFlow datasets.

### Imports

```python
import tensorflow as tf
from tensorflow import keras
import tensorflow_datasets as tfds

import numpy as np
import matplotlib.pyplot as plt
```

```python
# Print the version of tf, and tfds

print("TensorFlow's version used in notebook:{}".format(tf.__version__))
print("TensorFlow datasets's version used in notebook:{}".format(tfds.__version__))
```

**Execution Output:**
```text
TensorFlow's version used in notebook:2.5.0
TensorFlow datasets's version used in notebook:4.0.1
```

Below is how you would laod cifar-10 dataset from keras built in datasets.

```python
# (train_data, train_label), (test_data, test_label) = keras.datasets.cifar10.load_data()
```

And here is how to load the data from TensorFlow datasets. 

Here are few notes about loading data with `tfds.load(...)`

* The first thing to be provided while loading the dataset, it is the name of such dataset. The names are pretty clear in [TFDS catalog](https://www.tensorflow.org/datasets/catalog/overview). 
* We can directly split the data into training and test with `split` argument. With `split=['train', 'test[:50%]','test[50%:]']`, full train is assigned to training data, and 50% of test set is allocated to validation set. 

A quick note about these 3 sets: training set is used for training the model, validation set is for evaluating the model during training, and test set is a new data that we use to test the model. In the real world projects, validation set should have the same distribution as test set. 

* Setting `as_supervised` to true will return a tuple of image and label`(image, label)`instead of a dictionary`({'image': img, 'label': label})`.

* And `with_info=True` will return the information of the concerned dataset.

```python
(train_data, val_data, test_data), info = tfds.load('cifar10', 
                                          split=['train', 'test[:50%]','test[50%:]'],
                                          as_supervised=True, 
                                          shuffle_files=False,
                                          with_info=True
)
```

**Execution Output:**
```text
[1mDownloading and preparing dataset cifar10/3.0.2 (download: 162.17 MiB, generated: 132.40 MiB, total: 294.58 MiB) to /root/tensorflow_datasets/cifar10/3.0.2...[0m







Shuffling and writing examples to /root/tensorflow_datasets/cifar10/3.0.2.incompleteDB9DNF/cifar10-train.tfrecord

Shuffling and writing examples to /root/tensorflow_datasets/cifar10/3.0.2.incompleteDB9DNF/cifar10-test.tfrecord
[1mDataset cifar10 downloaded and prepared to /root/tensorflow_datasets/cifar10/3.0.2. Subsequent calls will reuse this data.[0m
```

We can see the dataset size by....

```python
print("The number images in training set: {}".format(len(train_data)))
print("The number images in validation set: {}".format(len(val_data)))
print("The number images in test set: {}".format(len(test_data)))
```

**Execution Output:**
```text
The number images in training set: 50000
The number images in validation set: 5000
The number images in test set: 5000
```

Or use `info` to get number of examples.

```python
# Getting the number of examples 

info.splits['train'].num_examples
```

**Execution Output:**
```text
50000
```

```python
# Getting the number of examples 

info.splits['test'].num_examples
```

**Execution Output:**
```text
10000
```

Let's also get class names from `info.features`

```python
# getting class names

info.features['label'].names
```

**Execution Output:**
```text
['airplane',
 'automobile',
 'bird',
 'cat',
 'deer',
 'dog',
 'frog',
 'horse',
 'ship',
 'truck']
```

```python
# Number of classes

info.features['label'].num_classes
```

**Execution Output:**
```text
10
```

Now that the data is loaded, let's visualize some images. It's always a cool thing to do.

<a name='2-2'></a>

## 2.2 Looking in Images

As always, it's good to peep in images and see if there are images that are labelled incorrectly, or have an extenstion of `.pdf` when in fact all images should be `.png` or `jpg.`

As you might guess, TensorFlow datasets are remarkably prepared, but in real life, incorrect labelling and formats can exist. 

Let's use `tfds.visualization(..)` to visualize some images.

```python
fig = tfds.show_examples(train_data, info)
```

<a name='2-3'></a>

## 2.3 Preparing Data: Building a Training Pipeline

Now, let's prepare the data, specifically, building an input pipeline.

First, the tensorflow datasets are returned as `uint8`, we need to normalize the images while also converting it to `float32`.

```python
def preprocess(image, label):

  """ 
  Take image and label, 
  convert images to float32, and return converted image &label
  """

    normalized_img = tf.cast(image, tf.float32)/255.0
    return normalized_img, label
```

Now, we can apply the above function to the dataset with `map`. Along the way, we will shuffle it, and batch the images. 

We do not shuffle the test set.

```python
def train_data_prep(data, shuffle_size, batch_size):
    data = data.map(preprocess)
    data = data.cache()
    data = data.shuffle(shuffle_size).repeat()
    data = data.batch(batch_size)
    data = data.prefetch(1)
    return data
```

Let's do the same thing for test, but on test, we will not shuffle the images.

```python
def test_data_prep(data, batch_size):
    data = data.map(preprocess)
    data = data.batch(batch_size)
    data = data.cache()
    data = data.prefetch(1)
    return data
```

```python
train_data_prepared = train_data_prep(train_data, 1000, 32)
```

```python
test_data_prepared = test_data_prep(test_data, 32)
```

Validation set is also preprocessed as test set. So, we can use `test_data_prep` on validation set.

```python
val_data_prepared = test_data_prep(val_data, 32)
```

Now, we have training and test data that are fully prepared to be fed to a ConvNets.

<a name='2-4'></a>

## 2.4 Creating, Compiling and Training a Model

To recall what we saw at the beginning, a Convolutional Neural Network is made of 3 main layers:

* **Convolutional layers** for extracting features in image and returning feature maps

Below are the arguments that Convolutional layer has in TensorFlow:

```
* filters: Number of filters in the layer. It can be compared to number of units in dense layers. 
* kernel_size: A tuple of two integer specifying the height and width of each filter. Setting kernel_size=3, and kernel_size=(3,3), they are all the same. 
* activation: activation function to use. In most cases, try relu! 

``` 

* **Pooling layers** for shrinking/compressing feature maps. We specify the pooling size with `pool_size` argument. 

```tf.keras.layers.MaxPooling2D(pool_size=2)```

* And **Fully Connected Layers** for doing the rest: matching the compressed features maps to their labels.


***Other notes***:

* Before compiling and training, a TensorFlow model is an empty graph(we will plot it)
* When compiling the model, it is where we specify the loss function and optimizer. Loss/cost function is there to calculate the distance between prediction and actual output and optimizer is there to reduce such distance. 

In our problem, we have 10 classes. Our loss is [`sparse_categorical_crossentropy`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalCrossentropy) and we can use [Adam](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adam) optimizer since it work well for many problems. 

* Training the model is nothing other than feeding the data(image and their labels) to the model. We specify the number of iterations the training has to happen, and also we will allocate `0.15 of training dataset to validation set` with `validation_split=0.15`. 

Now that we understand everything we are going to do, let's build the model, compile it, and train it. 

One last thing: cifar-10 images are 32*32, and are colored. So the input shape is `(32, 32, 3)`. Also, as we have 10 classes, the output neurons will be 10, activated by a `softmax` activation function.

```python
input_shape = [32,32,3]


cifar_cnn = tf.keras.models.Sequential([
    # First Convolutional layer: 64 filters, kernel/filter size of 3

    tf.keras.layers.Conv2D(filters=64, kernel_size=(3,3), activation='relu', input_shape=input_shape),
  
    # First Pooling layer
    tf.keras.layers.MaxPooling2D(pool_size=2),

    # Second Convolutional layer & Pooling

    tf.keras.layers.Conv2D(filters=128, kernel_size=(3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=2),

    # Third Convolutional & Pooling layer

    tf.keras.layers.Conv2D(filters=256, kernel_size=(3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=2),

    # Flattening layer: For converting previous output into 1D column vector

    tf.keras.layers.Flatten(),

    # Fully Connected layers

    tf.keras.layers.Dense(units=128, activation='relu'),
    tf.keras.layers.Dense(units=64, activation='relu'),

    # Last layer: 10 neurons for 10 classes, activated by softmax
    tf.keras.layers.Dense(units=10, activation='softmax')

])
```

Now that our model is created, we can peep into its architecture with `cifar_cnn.summary()`.

```python
# Model summary

cifar_cnn.summary()
```

**Execution Output:**
```text
Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_3 (Conv2D)            (None, 30, 30, 64)        1792      
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 15, 15, 64)        0         
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 13, 13, 128)       73856     
_________________________________________________________________
max_pooling2d_4 (MaxPooling2 (None, 6, 6, 128)         0         
_________________________________________________________________
conv2d_5 (Conv2D)            (None, 4, 4, 256)         295168    
_________________________________________________________________
max_pooling2d_5 (MaxPooling2 (None, 2, 2, 256)         0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 1024)              0         
_________________________________________________________________
dense_3 (Dense)              (None, 128)               1
... [Output truncated for brevity]
```

We can also plot it with `tf.keras.utils.plot_model(...)`

```python
tf.keras.utils.plot_model(cifar_cnn, rankdir='LR',show_dtype=True)
```

**Execution Output:**
```text
<IPython.core.display.Image object>
```

We can compile the model now...

```python
cifar_cnn.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
```

And here we train the model. For quick training, I will enable GPU. In Google Colab, GPU can be enabled by heading to `Runtime` in menu bar, go to  `Change runtime`, and in `hardware accelerator`, choose `GPU`. 

Thanks to Colab, we can train deep computer vision models fast than it could take on ordinary machines!!

```python
batch_size = 32
train_size = info.splits["train"].num_examples

val_size = len(val_data_prepared)


train_steps = int(train_size/batch_size)
val_steps = int(val_size/batch_size)

model_history = cifar_cnn.fit(train_data_prepared, 
              validation_data=val_data_prepared,
              epochs=9,
              steps_per_epoch=train_steps,
              validation_steps=val_steps)
```

**Execution Output:**
```text
Epoch 1/9
1562/1562 [==============================] - 8s 5ms/step - loss: 1.0155 - accuracy: 0.6438 - val_loss: 1.1868 - val_accuracy: 0.5859
Epoch 2/9
1562/1562 [==============================] - 8s 5ms/step - loss: 0.8516 - accuracy: 0.7007 - val_loss: 0.9781 - val_accuracy: 0.6484
Epoch 3/9
1562/1562 [==============================] - 8s 5ms/step - loss: 0.7368 - accuracy: 0.7428 - val_loss: 0.9412 - val_accuracy: 0.6797
Epoch 4/9
1562/1562 [==============================] - 8s 5ms/step - loss: 0.6447 - accuracy: 0.7745 - val_loss: 0.8999 - val_accuracy: 0.6719
Epoch 5/9
1562/1562 [==============================] - 7s 5ms/step - loss: 0.5623 - accuracy: 0.8032 - val_loss: 0.9244 - val_accuracy: 0.6641
Epoch 6/9
1562/1562 [==============================] - 7s 5ms/step - loss: 0.5041 - accuracy: 0.8230 - val_loss: 1.0261 - val_accuracy: 0.6953
Epoch 7/9
1562/1562 [==============================] - 7s 5ms/step - loss: 0.4413 - accuracy: 0.8441 - val_loss: 1.0780 - val_accuracy: 0.6562
Epoch 8/9
1562/1562 [==============================] - 7s 5ms/step - loss: 0.3939 - accuracy: 0.8621 - val_loss: 1.0975 - val_accuracy: 0.7031
Epoch 9/9
1562/1562 [==============================] - 7
... [Output truncated for brevity]
```

Now that our model is trained, let's visualize the resulting metrics: loss and accuracy during training and validation.

<a name='2-5'></a>

## 2.5 Visualizing the Model Results

```python
import pandas as pd
 
 # Getting the model training history
model_history = model_history.history

# Model history into a pandas dataframe
loss_acc_df = pd.DataFrame(model_history)

# Plotting the loss and accuracy 

loss_acc_df.plot(figsize=(10,5))
```

Let's elaborate the plot more by plotting the loss accuracy separately.

```python
acc = model_history['accuracy']
val_acc = model_history['val_accuracy']
loss = model_history['loss']
val_loss = model_history['val_loss']

epochs = cifar_cnn.history.epoch

# function to plot accuracy 

def plot_acc(acc, val_acc, epochs):

    plt.figure(figsize=(10,5))
    plt.plot(epochs, acc, 'r', label='Training Accuracy')
    plt.plot(epochs, val_acc, 'g', label='Validation Accuracy')
    plt.title('Training and validation accuracy')
    plt.legend(loc=0)
    plt.figure()

def plot_loss(loss, val_loss, epochs):

    plt.figure(figsize=(10,5))
    plt.plot(epochs, loss, 'b', label='Training Loss')
    plt.plot(epochs, val_loss, 'y', label='Validation Loss')
    plt.title('Training and Validation Loss')
    plt.legend(loc=0)
    plt.figure()
```

```python
#Plotting acc

plot_acc(acc, val_acc, epochs)
```

Looking at the plot above, it seems that the model is overfitting. 

Overfitting happens when the model is doing well on the training set but can't have the same performance on validation data. 

Overfitting can be avoided by adding more data and regularizing the model. In later section, we will add [reguralization layers](https://keras.io/api/layers/regularization_layers/) such as [Dropout](https://keras.io/api/layers/regularization_layers/dropout/). 

Overfitting can also be reduced by stopping the training early. This happens when you train for many epochs, but in our case, we trained for 9 epochs. This is not an issue here, but if we had to bet the epochs, [early stopping](https://keras.io/api/callbacks/early_stopping/) can help to stop the model training when there is no improvements in the results.

Let's plot the loss.

```python
plot_loss(loss, val_loss, epochs)
```

The training loss kept decreasing as it should, but the validation loss started to diverge at the third epoch. 

In the next section, we are going to attempt improving the model.

<a name='2-6'></a>

## 2.6 Improving the Model

We are going to do two things to improve the model. 

First, I will increase validation images. Currently, they are 5000, it is 10% of the training set. I will double it. 

Another thing to try is to tweak the model layers. One would use tools like [Keras Tuner](https://keras.io/keras_tuner/) to search the optimal number of filters, etc, but for now, we will add dropout layer. 

The idea of [dropout](https://keras.io/api/layers/regularization_layers/dropout/) is very simple: During the training, at each iteration, a given number of neurons are randomly disabled. This can increase both performance and generalization of the neural network.

```python
# reloading the data

# Training set = 80% of orginal training set (50,000 images)
# Validation set = 20% of training set = 10,000 images
# Test set = full orginal test set = 10,000 images

(train_data, val_data, test_data), info = tfds.load('cifar10', 
                                          split=['train[:80%]', 'train[80%:]','test'],
                                          as_supervised=True, 
                                          shuffle_files=True,
                                          with_info=True
)
```

Let's preprocess these 3 sets with the functions that we defined at the beginning.

```python
train_final = train_data_prep(train_data, 1000, 32)

val_final = test_data_prep(val_data, 32)
test_final = test_data_prep(test_data, 32)
```

Now, we can redefine the model.

```python
input_shape = [32,32,3]

cifar_cnn_2 = tf.keras.models.Sequential([
  
    tf.keras.layers.Conv2D(filters=64, kernel_size=(3,3), padding='same',activation='relu', input_shape=input_shape),
    tf.keras.layers.MaxPooling2D(pool_size=2),

    tf.keras.layers.Conv2D(filters=128, kernel_size=(3,3), padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=2),

    tf.keras.layers.Conv2D(filters=256, kernel_size=(3,3), padding='same',  activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=2),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.5),

    tf.keras.layers.Dense(units=128, activation='relu'),
    tf.keras.layers.Dropout(0.5),

    tf.keras.layers.Dense(units=10, activation='softmax')

])

# Nadam optimizer is a version of adam

cifar_cnn_2.compile(loss='sparse_categorical_crossentropy',
                    optimizer='nadam',
                    metrics='accuracy')
```

```python
# Training the model for 10 epochs

batch_size = 32
train_size = 40000
val_size = 10000


train_steps = int(train_size/batch_size)
val_steps = int(val_size/batch_size)

model_history_2 = cifar_cnn_2.fit(train_final, 
              validation_data=val_final,
              epochs=10,
              steps_per_epoch=train_steps,
              validation_steps=val_steps)
```

**Execution Output:**
```text
Epoch 1/10
1250/1250 [==============================] - 8s 6ms/step - loss: 1.6176 - accuracy: 0.4100 - val_loss: 1.2067 - val_accuracy: 0.5677
Epoch 2/10
1250/1250 [==============================] - 7s 6ms/step - loss: 1.2107 - accuracy: 0.5696 - val_loss: 0.9822 - val_accuracy: 0.6585
Epoch 3/10
1250/1250 [==============================] - 7s 6ms/step - loss: 1.0364 - accuracy: 0.6356 - val_loss: 0.8793 - val_accuracy: 0.6897
Epoch 4/10
1250/1250 [==============================] - 7s 6ms/step - loss: 0.9407 - accuracy: 0.6689 - val_loss: 0.7914 - val_accuracy: 0.7224
Epoch 5/10
1250/1250 [==============================] - 8s 6ms/step - loss: 0.8663 - accuracy: 0.7006 - val_loss: 0.7671 - val_accuracy: 0.7341
Epoch 6/10
1250/1250 [==============================] - 8s 6ms/step - loss: 0.8183 - accuracy: 0.7145 - val_loss: 0.7386 - val_accuracy: 0.7490
Epoch 7/10
1250/1250 [==============================] - 8s 6ms/step - loss: 0.7659 - accuracy: 0.7297 - val_loss: 0.7462 - val_accuracy: 0.7378
Epoch 8/10
1250/1250 [==============================] - 7s 6ms/step - loss: 0.7292 - accuracy: 0.7430 - val_loss: 0.7406 - val_accuracy: 0.7443
Epoch 9/10
1250/1250 [==========================
... [Output truncated for brevity]
```

Seems that the difference between val and training accuracy is not as high as it was. 

Let's plot loss and accuracy.

```python
model_history = model_history_2.history

acc = model_history['accuracy']
val_acc = model_history['val_accuracy']
loss = model_history['loss']
val_loss = model_history['val_loss']

epochs = model_history_2.epoch
```

```python
# Plot accuracy 

plot_acc(acc, val_acc, epochs)
```

```python
# Plot loss 

plot_loss(loss, val_loss, epochs)
```

This is much better. We only trained for 10 epochs and it seems that the loss was still decreasing. 

Dropout is remarkably one of the powerful regularization technique.

<a name='2-7'></a>

## 2.7 Evaluating on Test set

```python
# Evaluating a model on test set 

loss, acc = cifar_cnn_2.evaluate(test_final)
```

**Execution Output:**
```text
313/313 [==============================] - 2s 7ms/step - loss: 0.7157 - accuracy: 0.7552
```

```python
# Print loss and acc with 3 only decimal points

print('Test Loss: {:.3f}'.format(loss))
print('Test Accuracy: {:.3f}'.format(acc))
```

**Execution Output:**
```text
Test Loss: 0.716
Test Accuracy: 0.755
```

Test set is a new data to the model, but as you can see, the accuracy is not really bad, given that the training accuracy is 76%.

<a name='2-8'></a>

## 2.8 Saving and Loading the Model for Prediction

```python
# Saving a model

cifar_cnn_2.save('Cifar Best.h5')
```

```python
# Loading a saved model
from keras.models import load_model

load_cifar = load_model('Cifar Best.h5')
```

```python
load_cifar.summary()
```

**Execution Output:**
```text
Model: "sequential_8"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_24 (Conv2D)           (None, 32, 32, 64)        1792      
_________________________________________________________________
max_pooling2d_24 (MaxPooling (None, 16, 16, 64)        0         
_________________________________________________________________
conv2d_25 (Conv2D)           (None, 16, 16, 128)       73856     
_________________________________________________________________
max_pooling2d_25 (MaxPooling (None, 8, 8, 128)         0         
_________________________________________________________________
conv2d_26 (Conv2D)           (None, 8, 8, 256)         295168    
_________________________________________________________________
max_pooling2d_26 (MaxPooling (None, 4, 4, 256)         0         
_________________________________________________________________
flatten_8 (Flatten)          (None, 4096)              0         
_________________________________________________________________
dropout_10 (Dropout)         (None, 4096)              0
... [Output truncated for brevity]
```

---

## 2. Real-World Datasets & Data Augmentation Pipelines

<a name='0'></a>

# CNN for Real World Dataset and Image Augmentation

### Contents 

* [1. Intro - Real World Datasets and Data Augmentation](#1)
* [2. Getting Started: Real World Datasets and Overfitting](#2)
   * [2.1 Loading and Preparing the Data](#2-1)
   * [2.2 Buiding, Compiling and Training a Model](#2-2)
   * [2.3 Visualizing the Model Results](#2-3)
   
* [3. Image Augmentation with ImageDataGenerator ](#3)
   * [3.1 Loading the Data Again](#3-1)
   * [3.2 Applying Data Augmentation](#3-2)
   * [3.3 Visualizing Augmented Images](#3-3)
   * [3.4 Retraining a Model on Augmented Data](#3-4)
   * [3.5 Visualizing the Model Resuts](#3-5)
   * [3.6 Further Improvements: Using Pretrained Models](#3-6)
   * [3.7 Saving, Loading, and Testing a Model on New Images](#3-7)

* [4. Image Augmentation with Keras Image Augmentation Layers ](#4)
   * [4.1 Getting the Data again](#4-1)
   * [4.2 Looking in the Data](#4-2)
   * [4.3 Preprocessing Data](#4-3)
   * [4.4 Augmenting the Images with Auggmentation Layers](#4-4)
   * [4.5 First Option: Building a Model with an Augmented Images](#4-5)
   * [4.6 Second Option: Augmenting the Images Inside a Model](#4-6)

<a name='1'></a>

## 1. Intro - Real World Datasets and Image Augmentation

Real world image datasets are not always prepared and most of the time, they are not enough in quantity.

We can not emphasize enough the advantages of having both good and enough data although such blend is not always possible. 

Given that sometime we may have a handful of images, how can we go about it? Are there ways to expand the small image dataset? And boost the performance of the machine learning model as a result?

With the advancement of machine learning techniques, it has become possible to add a boost to the performance metrics by just expanding the existing dataset. The technique of synthetizing new data(images) from existing data is called data augmentation.

Image datasets can be augmented in various ways including: 

* Flipping the image, vertically or horizontally. 
* Cropping the image.
* Changing contrast and color of the image.
* Adding noise to the data.
* Rotating the image at a given degree.

Below image summarize all possibilities that can be done in image data augmentation. 

![Image Augmentation](https://cdn.hashnode.com/res/hashnode/image/upload/v1623166213173/JTRR1Btgm.png)

<a name='3'></a>

## 2. Getting Started: Real World Datasets and Overfitting

One of the most challenges in training machine learning models on real world datasets is `overfitting`. 

A model overfits when it memorized the training data due to insufficient training samples, or lack of diversity in training samples. By doing data augmentation, we are increasing the training samples, as well as introducing some diversity in the images. 

It's fair to say that data augmentation is the cure to overfitting. To test that, let's train a quick cat and dog classifier. After that, we will augment the images to ovoid overfitting.

### Without Data Augmentation: Training Cat and Dog Classifier

We are going to see the need of data augmentation by training a cat and dog classifier. 

Along the way, we will let the results guide the latter.

<a name='2-1'></a>

### 2.1 Loading and Preparing Cat and Dog Data

#### Imports

```python
import tensorflow as tf
from tensorflow import keras
import os 
import zipfile
import matplotlib.pyplot as plt
import numpy as np
```

#### Getting the data

The version of the data that we are going to use here is a filtered version. Orginally, it contains [over 20.000 images](https://www.microsoft.com/en-us/download/details.aspx?id=54765).

```python
# Load the data into the workspace

!wget --no-check-certificate \
    https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip \
    -O /tmp/cats_and_dogs_filtered.zip
```

**Execution Output:**
```text
--2021-09-18 06:21:48--  https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip
Resolving storage.googleapis.com (storage.googleapis.com)... 209.85.147.128, 142.250.125.128, 142.250.136.128, ...
Connecting to storage.googleapis.com (storage.googleapis.com)|209.85.147.128|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 68606236 (65M) [application/zip]
Saving to: ‘/tmp/cats_and_dogs_filtered.zip’

/tmp/cats_and_dogs_ 100%[===================>]  65.43M   178MB/s    in 0.4s    

2021-09-18 06:21:48 (178 MB/s) - ‘/tmp/cats_and_dogs_filtered.zip’ saved [68606236/68606236]
```

```python
# Extract the zip file

zip_dir = '/tmp/cats_and_dogs_filtered.zip'
zip_ref = zipfile.ZipFile(zip_dir, 'r')
zip_ref.extractall('/tmp')
zip_ref.close()
```

Now that the images are extracted (you can verify that by looking in Colab directory), let's get the training and validation directories from the main directory.

```python
main_dir = '/tmp/cats_and_dogs_filtered'

train_dir = os.path.join(main_dir, 'train')
val_dir = os.path.join(main_dir, 'validation')
```

We will continue with getting the cats and dogs in the above defined directories.

```python
train_cat_dir = os.path.join(train_dir, 'cats')
train_dog_dir = os.path.join(train_dir, 'dogs')

val_cat_dir = os.path.join(val_dir, 'cats')
val_dog_dir = os.path.join(val_dir, 'dogs')
```

Now, our directories are quite arranged. Let's see peep into the directories.

```python
os.listdir(main_dir)
```

**Execution Output:**
```text
['vectorize.py', 'train', 'validation']
```

```python
os.listdir(train_cat_dir)[:10]
```

**Execution Output:**
```text
['cat.504.jpg',
 'cat.148.jpg',
 'cat.560.jpg',
 'cat.506.jpg',
 'cat.182.jpg',
 'cat.300.jpg',
 'cat.178.jpg',
 'cat.791.jpg',
 'cat.260.jpg',
 'cat.328.jpg']
```

Let's walk through the directories and see the number of images in each directory.

```python
for dir, dirname, filename in os.walk(main_dir):
    print(f"Found {len(dirname)} directories and {len(filename)} images in {dir}")
```

**Execution Output:**
```text
Found 2 directories and 1 images in /tmp/cats_and_dogs_filtered
Found 2 directories and 0 images in /tmp/cats_and_dogs_filtered/train
Found 0 directories and 1000 images in /tmp/cats_and_dogs_filtered/train/dogs
Found 0 directories and 1000 images in /tmp/cats_and_dogs_filtered/train/cats
Found 2 directories and 0 images in /tmp/cats_and_dogs_filtered/validation
Found 0 directories and 500 images in /tmp/cats_and_dogs_filtered/validation/dogs
Found 0 directories and 500 images in /tmp/cats_and_dogs_filtered/validation/cats
```

There are 3000 images, 2000 in training set, 1000 in validation set. Cats and dogs images are evenly splitted. 

Let's now generate a dataset to train the model.

#### Preparing the Dataset

```python
from keras.preprocessing.image import ImageDataGenerator

# Rescale the image to values between 0 and 1

train_gen = ImageDataGenerator(rescale=1/255.0)
val_gen = ImageDataGenerator(rescale=1/255.0)

batch_size = 20
image_size = (180,180)

train_data = train_gen.flow_from_directory(train_dir, 
                                           batch_size=batch_size,
                                           class_mode='binary',
                                           target_size=image_size)

val_data = val_gen.flow_from_directory(val_dir, 
                                           batch_size=batch_size,
                                           class_mode='binary',
                                           target_size=image_size)
```

**Execution Output:**
```text
Found 2000 images belonging to 2 classes.
Found 1000 images belonging to 2 classes.
```

Before building a model, let's visualize the images. It's always a best practice.

```python
data_for_viz = tf.keras.preprocessing.image_dataset_from_directory(
    
          train_dir,
          image_size=(180,180))
```

**Execution Output:**
```text
Found 2000 files belonging to 2 classes.
```

```python
def image_viz(dataset):
  
  plt.figure(figsize=(12, 8))
  
  index = 0
    for image, label in dataset.take(12):
        index +=1
        ax = plt.subplot(4, 4, index)
        plt.imshow(image[index].numpy().astype("uint8"))
        plt.title(int(label[index]))
        plt.axis("off")
```

```python
image_viz(data_for_viz)
```

<a name='2-2'></a>

### 2.2 Building, Compiling and Training a Model

```python
def classifier():

    model = tf.keras.models.Sequential([
        
    # First convolution and pooling layer                                  
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(180, 180, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
        
    # Second convolution and pooling layer
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    # Third convolution and pooling layer
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    # Flattening layer for converting the feature maps into 1D column vector
    
    tf.keras.layers.Flatten(),

    # Fully connected layers

    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')

  ])


  # Compiling the model: Specifying optimizer, loss and metric to track during training

    model.compile(
        optimizer=tf.keras.optimizers.RMSprop(),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    return model
```

```python
# Training a model

model = classifier()

train_steps = 2000 / batch_size
val_steps = 1000 / batch_size

history = model.fit(train_data, 
          validation_data=val_data,
          epochs=50,
          steps_per_epoch=train_steps,
          validation_steps=val_steps)
```

**Execution Output:**
```text
Epoch 1/50
100/100 [==============================] - 45s 121ms/step - loss: 0.8243 - accuracy: 0.5435 - val_loss: 0.7136 - val_accuracy: 0.5000
Epoch 2/50
100/100 [==============================] - 12s 118ms/step - loss: 0.6378 - accuracy: 0.6455 - val_loss: 0.5870 - val_accuracy: 0.6690
Epoch 3/50
100/100 [==============================] - 12s 118ms/step - loss: 0.5446 - accuracy: 0.7245 - val_loss: 0.5848 - val_accuracy: 0.6990
Epoch 4/50
100/100 [==============================] - 12s 117ms/step - loss: 0.4387 - accuracy: 0.7955 - val_loss: 0.5780 - val_accuracy: 0.7310
Epoch 5/50
100/100 [==============================] - 12s 117ms/step - loss: 0.3505 - accuracy: 0.8525 - val_loss: 0.5507 - val_accuracy: 0.7550
Epoch 6/50
100/100 [==============================] - 12s 119ms/step - loss: 0.2380 - accuracy: 0.8940 - val_loss: 0.7112 - val_accuracy: 0.7190
Epoch 7/50
100/100 [==============================] - 12s 118ms/step - loss: 0.1427 - accuracy: 0.9425 - val_loss: 0.8400 - val_accuracy: 0.7560
Epoch 8/50
100/100 [==============================] - 12s 118ms/step - loss: 0.1045 - accuracy: 0.9620 - val_loss: 0.9308 - val_accuracy: 0.7460
Epoch 9/50
100/100 [====================
... [Output truncated for brevity]
```

<a name='2-3'></a>

### 2.3 Visualizing the Model Results

```python
# function to plot accuracy and loss

def plot_acc_loss(acc, val_acc, loss, val_loss, epochs):

    plt.figure(figsize=(10,5))
    plt.plot(epochs, acc, 'r', label='Training Accuracy')
    plt.plot(epochs, val_acc, 'g', label='Validation Accuracy')
    plt.title('Training and validation accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend(loc=0)

    # Create a new figure with plt.figure()
    plt.figure()

    plt.figure(figsize=(10,5))
    plt.plot(epochs, loss, 'b', label='Training Loss')
    plt.plot(epochs, val_loss, 'y', label='Validation Loss')
    plt.title('Training and Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend(loc=0)
    plt.show()
```

```python
model_history = history.history

acc = model_history['accuracy']
val_acc = model_history['val_accuracy']
loss = model_history['loss']
val_loss = model_history['val_loss']

epochs = history.epoch
```

```python
plot_acc_loss(acc, val_acc, loss, val_loss, epochs)
```

Clearly, the our classifier overfitted. If you can look at the plots above, there is so much gap between the training and validation accuracy/loss. 

The classifier is overly confident at recognizing training images, but not so good when evaluated on the validation images. 

This goes to show that data augmentation is very useful technique. By just expanding the images, and introducing different image scenes, overfitting can potentially be handled. That is what we are going to do iin the next section.

<a name='3'></a>

## 3. Image Augmentation with ImageDataGenerator

`ImageDataGenerator` is a powerful Keras image processing functionality used to augment images. It is a part of [image data processing functions](https://keras.io/api/preprocessing/image/). 

The single most advantage of ImageDataGenerator is that it allows you to augment images in realtime, as you load them from a directory for example. 

The orginal directory of the data is not affected at all. The image will be loaded & augmented at the same time, while not affecting the orginal directory.

<a name='3-1'></a>

### 3.1 Loading the Data Again

```python
# Download the data into the workspace

!wget --no-check-certificate \
    https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip \
    -O /tmp/cats_and_dogs_filtered.zip


# Extract the zip file

zip_dir = '/tmp/cats_and_dogs_filtered.zip'
zip_ref = zipfile.ZipFile(zip_dir, 'r')
zip_ref.extractall('/tmp')
zip_ref.close()

# Get training and val directories

main_dir = '/tmp/cats_and_dogs_filtered'

train_dir = os.path.join(main_dir, 'train')
val_dir = os.path.join(main_dir, 'validation')

train_cat_dir = os.path.join(train_dir, 'cats')
train_dog_dir = os.path.join(train_dir, 'dogs')

val_cat_dir = os.path.join(val_dir, 'cats')
val_dog_dir = os.path.join(val_dir, 'dogs')
```

**Execution Output:**
```text
--2021-09-18 06:32:33--  https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip
Resolving storage.googleapis.com (storage.googleapis.com)... 74.125.70.128, 74.125.201.128, 74.125.202.128, ...
Connecting to storage.googleapis.com (storage.googleapis.com)|74.125.70.128|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 68606236 (65M) [application/zip]
Saving to: ‘/tmp/cats_and_dogs_filtered.zip’

/tmp/cats_and_dogs_ 100%[===================>]  65.43M   169MB/s    in 0.4s    

2021-09-18 06:32:34 (169 MB/s) - ‘/tmp/cats_and_dogs_filtered.zip’ saved [68606236/68606236]
```

<a name='3-2'></a>

### 3.2 Apply Data Augmentation

We are going to use `ImageDataGenerator` to generate augmented images. 


Below are some of the options available in [ImageDataGenerator](https://keras.io/api/preprocessing/image/) and their explainations. 

```
train_imagenerator = ImageDataGenerator(
      rotation_range=40,
      width_shift_range=0.2,
      height_shift_range=0.2,
      shear_range=0.2,
      zoom_range=0.2,
      horizontal_flip=True,
      fill_mode='nearest')
```

* **rotation_range** is a value in degrees (0–180) to randomly rotate images.

* **width_shift and height_shift** are ranges of fraction of total width or height within which to translate pictures, either vertically or horizontally.

* **shear_range** is for applying shearing randomly.

* **zoom_range** is for zooming pictures randomly. 

* **horizontal_flip** is for flipping half of the images horizontally. There is also `vertical_flip` option. 

* **fill_mode** is for completing newly created pixels, which can appear after a rotation or a width/height shift. 

Let's see this in practice! We will start by creating `train_imagenerator` which is an image generator for training set.

```python
# Creating training image data generator

from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_imagenerator = ImageDataGenerator(
    
    rescale=1/255.,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
    
)
```

We will also create `val_imagenerator`, but different to training generator, there are no augmentation. It's only rescaling the images pixels to values between 0 and 1. Images pixels are normally between 0 and 255. Rescaling the values improve the performance of the neural network and reduce training time as well.

```python
# Validation image generator

val_imagenerator = ImageDataGenerator(rescale=1/255.)
```

After creating train and validation generators, let's use `image_dataset_from_directory function` to generate a TensorFlow dataset from images files located in our two directories. 

Below is how training and validation directories are structured:

```
cats_dogs_filtered/
..train/
....cats/
......cat.0.jpg
......cat.1.jpg
......cat.2.jpg
....dogs/
......dog.0.jpg
......dog.1.jpg
......dog.2.jpg
..validation/
....cats/
......cat.0.jpg
......cat.1.jpg
....dogs/
......dog.0.jpg
......dog.1.jpg
```

```python
# Load training images in batches of 20 while applying aumgmentation

batch_size = 20
target_size = (180,180)

train_generator = train_imagenerator.flow_from_directory(
        train_dir, #parent directory must be specified
        target_size = target_size, # All images will be resized to (180,180)
        batch_size=batch_size,
        class_mode='binary' # since we need binary labels(0,1) and we will use binary_crossentropy

)
```

**Execution Output:**
```text
Found 2000 images belonging to 2 classes.
```

```python
val_generator = val_imagenerator.flow_from_directory(
        val_dir, #parent directory must be specified
        target_size = target_size, # All images will be resized to (180,180)
        batch_size=batch_size,
        class_mode='binary' # since we need binary labels(0,1) and we will use binary_crossentropy

)
```

**Execution Output:**
```text
Found 1000 images belonging to 2 classes.
```

Another great advantage of `ImageDataGenerator` is that it generates the labels of the images based off their folders. During the model training, we won't need to specify the labels.

We are ready to train our machine learning model now, but before we could try to visualize the augmented images.

<a name='3-3'></a>

### 3.3 Visualizing Augmented Images

```python
# Get images in batch of 20
augmented_image, label = train_generator.next()

plt.figure(figsize=(12,8))
for i in range(6):
        ax = plt.subplot(2, 3, i + 1)
        plt.imshow(augmented_image[i])
        plt.title(int(label[i]))
        plt.axis("off")
```

It may be hard to spot since we are not comparing them with non augmented images, but if you can observe well, some images are zoomed in, rotated, and flipped horizantally. 

Below images are not augmented. You can see that no zoom were applied for example.

```python
non_augmented_image, label = train_data.next()

plt.figure(figsize=(12,8))
for i in range(6):
        ax = plt.subplot(2, 3, i + 1)
        plt.imshow(non_augmented_image[i])
        plt.title(int(label[i]))
        plt.axis("off")
```

Now that we have visualized the augmented images, let's retrain the model on augmented images.

<a name='3-4'></a>

### 3.4 Retraining a Model on Augmented Images

You noticed that during training, we didn't have to provide the labels. `ImageDataGenerator` took care of it. As the images are loaded from their directories(cats, dogs), they are augmented and labelled at the same time. 

Another thing we can shed light on is the batch size. We have loaded our images in batch size of 20. Usually, the default batch size is 32. The value of the batch size only affect training time. The larger the size, the faster the training, and the smaller the size, the slower the training. 

The only issue with the large batch size is that it would requires many steps per epoch in order to give optimal model performance. I have merely used 20 based off the number of images we have in both sets, to facilitate the computation and steps per epochs. But a rule of thumb is to always start with 32. 


To be able to see what the difference data augmentation will make, we will use the same model as before. Let's call it.

```python
model_2 = classifier()

batch_size = 20

train_steps = 2000/batch_size
val_steps = 1000/batch_size

history_2 = model_2.fit(
      train_generator,
      steps_per_epoch=train_steps,  
      epochs=100,
      validation_data=val_generator,
      validation_steps=val_steps)
```

**Execution Output:**
```text
Epoch 1/100
100/100 [==============================] - 27s 262ms/step - loss: 0.9125 - accuracy: 0.5150 - val_loss: 0.6847 - val_accuracy: 0.5680
Epoch 2/100
100/100 [==============================] - 26s 260ms/step - loss: 0.7163 - accuracy: 0.5620 - val_loss: 0.7020 - val_accuracy: 0.5400
Epoch 3/100
100/100 [==============================] - 26s 260ms/step - loss: 0.6724 - accuracy: 0.6190 - val_loss: 0.6039 - val_accuracy: 0.6670
Epoch 4/100
100/100 [==============================] - 26s 261ms/step - loss: 0.6502 - accuracy: 0.6325 - val_loss: 0.6332 - val_accuracy: 0.6580
Epoch 5/100
100/100 [==============================] - 26s 261ms/step - loss: 0.6322 - accuracy: 0.6530 - val_loss: 0.5951 - val_accuracy: 0.6880
Epoch 6/100
100/100 [==============================] - 26s 261ms/step - loss: 0.6466 - accuracy: 0.6570 - val_loss: 0.5699 - val_accuracy: 0.6920
Epoch 7/100
100/100 [==============================] - 26s 259ms/step - loss: 0.6135 - accuracy: 0.6610 - val_loss: 0.5892 - val_accuracy: 0.6930
Epoch 8/100
100/100 [==============================] - 26s 260ms/step - loss: 0.6110 - accuracy: 0.6825 - val_loss: 0.7350 - val_accuracy: 0.5930
Epoch 9/100
100/100 [===========
... [Output truncated for brevity]
```

<a name='3-5'></a>

### 3.5 Visualizing The Model Results

```python
model_history_2 = history_2.history

acc = model_history_2['accuracy']
val_acc = model_history_2['val_accuracy']
loss = model_history_2['loss']
val_loss = model_history_2['val_loss']

epochs = history_2.epoch
```

```python
plot_acc_loss(acc, val_acc, loss, val_loss, epochs)
```

This is not excellent, but it's alot better than the results we had without data augmentation. you remember that our model was overfitting, but now although it's not smooth, there is a big improvement. 

How to improve the results? One might try to tweak layers and filters. Machine Learning is very experimental. It's rare that the first model will work well. The result is a function of time and experimentation. 

So, in this case, we can try pretrained models. Pretrained models are open source models that are built by other engineers(often researchers) and we can use them instead of building a network from scratch. 

The technique of reusing a pretrained model into a given(similar) task is called [`transfer learning`](https://jeande.medium.com/transfer-learning-explained-a80d38ee1564). Although this will be covered in the next notebook, let's give it a shot right away.

<a name='3-6'></a>

### 3.6 Further Improvements: Using Pretrained Models

Pretrained models works so well for many problems, without the need of building models from scratch.

Imagine how far you get by standing on the shoulder of the giant! By using powerful models trained on big datasets, the results are pretty impressive. 

Let's practice that. For more about pretrained models, check the next notebook.

You can find available pretrained models in Keras on Keras [Applications](https://keras.io/api/applications/).

```python
pretrained_base_model = keras.applications.InceptionResNetV2(
    weights='imagenet',
    include_top=False, # Drop imagenet classifier on the top
    input_shape=(180,180,3)

)
```

**Execution Output:**
```text
Downloading data from https://storage.googleapis.com/tensorflow/keras-applications/inception_resnet_v2/inception_resnet_v2_weights_tf_dim_ordering_tf_kernels_notop.h5
219062272/219055592 [==============================] - 2s 0us/step
219070464/219055592 [==============================] - 2s 0us/step
```

We then freeze the pretrained base model to avoid retraining the bottom layers.

```python
for layer in pretrained_base_model.layers:
    layer.trainable = False
```

Let's see the summary of the base model.

```python
pretrained_base_model.summary()
```

**Execution Output:**
```text
Model: "inception_resnet_v2"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_1 (InputLayer)            [(None, 180, 180, 3) 0                                            
__________________________________________________________________________________________________
conv2d_9 (Conv2D)               (None, 89, 89, 32)   864         input_1[0][0]                    
__________________________________________________________________________________________________
batch_normalization (BatchNorma (None, 89, 89, 32)   96          conv2d_9[0][0]                   
__________________________________________________________________________________________________
activation (Activation)         (None, 89, 89, 32)   0           batch_normalization[0][0]        
__________________________________________________________________________________________________
conv2d_10 (Conv2D)              (None, 87, 87, 32)   9216        activation[0][0] 
... [Output truncated for brevity]
```

Let's create a new model on top of the pretrained network.

```python
# Define the input shape
inputs = tf.keras.Input(shape=(180, 180, 3))

# stack the inputs to pretrained model and set training to false
x = pretrained_base_model(inputs, training=False)

# Add a pooling layer
x = tf.keras.layers.GlobalAveragePooling2D()(x)

# Add drop out layer

x = tf.keras.layers.Dropout(0.4)(x)

# Last output dense layer with 1 unit and sigmoid
output = tf.keras.layers.Dense(1, activation='sigmoid')(x)

# Build a model
model_3 = tf.keras.Model(inputs, output)
```

Now let's compile the model and train on our augmented data.

```python
model_3.compile(
    optimizer='rmsprop',
    loss='binary_crossentropy',
    metrics='accuracy'

)
```

```python
history_3 = model_3.fit(
      train_generator,
      steps_per_epoch=train_steps,  
      epochs=25,
      validation_data=val_generator,
      validation_steps=val_steps)
```

**Execution Output:**
```text
Epoch 1/25
100/100 [==============================] - 55s 412ms/step - loss: 0.2161 - accuracy: 0.9185 - val_loss: 0.0763 - val_accuracy: 0.9730
Epoch 2/25
100/100 [==============================] - 37s 372ms/step - loss: 0.1294 - accuracy: 0.9485 - val_loss: 0.0546 - val_accuracy: 0.9840
Epoch 3/25
100/100 [==============================] - 37s 369ms/step - loss: 0.1255 - accuracy: 0.9535 - val_loss: 0.0502 - val_accuracy: 0.9810
Epoch 4/25
100/100 [==============================] - 37s 372ms/step - loss: 0.1168 - accuracy: 0.9590 - val_loss: 0.0553 - val_accuracy: 0.9810
Epoch 5/25
100/100 [==============================] - 38s 376ms/step - loss: 0.1173 - accuracy: 0.9615 - val_loss: 0.0504 - val_accuracy: 0.9850
Epoch 6/25
100/100 [==============================] - 37s 373ms/step - loss: 0.1046 - accuracy: 0.9610 - val_loss: 0.0433 - val_accuracy: 0.9840
Epoch 7/25
100/100 [==============================] - 37s 374ms/step - loss: 0.1292 - accuracy: 0.9545 - val_loss: 0.0440 - val_accuracy: 0.9860
Epoch 8/25
100/100 [==============================] - 37s 372ms/step - loss: 0.1085 - accuracy: 0.9605 - val_loss: 0.0384 - val_accuracy: 0.9850
Epoch 9/25
100/100 [====================
... [Output truncated for brevity]
```

This is soo impressive, over 97% accuracy on training. You can see we didn't have to even train for 25 epochs, 10 would give great results. Let's plot the results and also later change the epochs to 10.

```python
model_history_3 = history_3.history

acc = model_history_3['accuracy']
val_acc = model_history_3['val_accuracy']
loss = model_history_3['loss']
val_loss = model_history_3['val_loss']

epochs = history_3.epoch

plot_acc_loss(acc, val_acc, loss, val_loss, epochs)
```

We have said that using a pretrained model is like standing on the shoulder of the giant. And that's pretty clear on the above graph, the accuracy started at ~90%. 

N.B. Calling model.fit(...) continue where the training left. To avoid adding up on previous training, you have to redefine & compile the model.

```python
# Define the input shape
inputs = tf.keras.Input(shape=(180, 180, 3))

# stack the inputs to pretrained model and set training to false
x = pretrained_base_model(inputs, training=False)

# Add a pooling layer
x = tf.keras.layers.GlobalAveragePooling2D()(x)

# Add drop out layer

x = tf.keras.layers.Dropout(0.4)(x)

# Last output dense layer with 1 unit and sigmoid
output = tf.keras.layers.Dense(1, activation='sigmoid')(x)

# Build a model
model_4 = tf.keras.Model(inputs, output)
```

```python
model_4.compile(
    optimizer='rmsprop',
    loss='binary_crossentropy',
    metrics='accuracy'

)
```

```python
# Train for 10 epochs

history_4 = model_4.fit(
      train_generator,
      steps_per_epoch=train_steps,  
      epochs=10,
      validation_data=val_generator,
      validation_steps=val_steps)
```

**Execution Output:**
```text
Epoch 1/10
100/100 [==============================] - 53s 409ms/step - loss: 0.2150 - accuracy: 0.9175 - val_loss: 0.0557 - val_accuracy: 0.9830
Epoch 2/10
100/100 [==============================] - 37s 369ms/step - loss: 0.1386 - accuracy: 0.9460 - val_loss: 0.0491 - val_accuracy: 0.9830
Epoch 3/10
100/100 [==============================] - 37s 369ms/step - loss: 0.1041 - accuracy: 0.9595 - val_loss: 0.0511 - val_accuracy: 0.9830
Epoch 4/10
100/100 [==============================] - 37s 368ms/step - loss: 0.1119 - accuracy: 0.9610 - val_loss: 0.0522 - val_accuracy: 0.9820
Epoch 5/10
100/100 [==============================] - 37s 368ms/step - loss: 0.1112 - accuracy: 0.9615 - val_loss: 0.0539 - val_accuracy: 0.9810
Epoch 6/10
100/100 [==============================] - 37s 371ms/step - loss: 0.1100 - accuracy: 0.9645 - val_loss: 0.0483 - val_accuracy: 0.9820
Epoch 7/10
100/100 [==============================] - 37s 372ms/step - loss: 0.0999 - accuracy: 0.9615 - val_loss: 0.0463 - val_accuracy: 0.9840
Epoch 8/10
100/100 [==============================] - 37s 372ms/step - loss: 0.0949 - accuracy: 0.9610 - val_loss: 0.0455 - val_accuracy: 0.9860
Epoch 9/10
100/100 [====================
... [Output truncated for brevity]
```

```python
model_history_4 = history_4.history

acc = model_history_4['accuracy']
val_acc = model_history_4['val_accuracy']
loss = model_history_4['loss']
val_loss = model_history_4['val_loss']

epochs = history_4.epoch

plot_acc_loss(acc, val_acc, loss, val_loss, epochs)
```

The reason why validation accuracy is better than training accuracy, or why validation loss is less than training loss, it's because the pretrained model has Batch Normalization and dropout layers. These regularization layers affects the accuracy during training, but they are turned off during validation. 

Also, during the training, accuracy and loss are averaged per epoch, while during validation phase, accuracy and loss are computed on a model that has already trained longer. 

You can notice this if you keep the eye on progress bar during the training. The training metrics change per step/epoch, and at the end of the epoch, the average loss/accuracy are reported. On the other hand, the validation metrics are computed after training on each epoch.

<a name='3-7'></a>

### 3.7 Saving, Loading, and Testing a Model on New Images

```python
# Saving a model

model_4.save('final_model.h5')

# or 

#tf.keras.models.save_model(model_4, 'final_model.h5')
```

```python
# load a saved model

loaded_model = tf.keras.models.load_model('/content/final_model.h5')
```

```python
# function to download some images from the internet

def get_image(image_name,url):

    image = tf.keras.utils.get_file(image_name,url)
    return image
```

```python
# Urls of cats and dogs images

cat_1 = 'https://upload.wikimedia.org/wikipedia/commons/b/b6/Felis_catus-cat_on_snow.jpg'
cat_2 = 'https://upload.wikimedia.org/wikipedia/commons/6/69/June_odd-eyed-cat_cropped.jpg'

dog_1 = 'https://upload.wikimedia.org/wikipedia/commons/b/b5/2008-08-28_White_German_Shepherd_ready.jpg'
dog_2 = 'https://upload.wikimedia.org/wikipedia/commons/d/df/Dogs_were_not_around_in_the_early_Cenozoic.png'
```

```python
cat_im1 = get_image('cat_1',cat_1)
cat_im2 = get_image('cat_2',cat_2)

dog_im1 = get_image('dog_1',dog_1)
dog_im2 = get_image('dog_2',dog_2)
```

**Execution Output:**
```text
Downloading data from https://upload.wikimedia.org/wikipedia/commons/b/b6/Felis_catus-cat_on_snow.jpg
2129920/2125399 [==============================] - 0s 0us/step
2138112/2125399 [==============================] - 0s 0us/step
Downloading data from https://upload.wikimedia.org/wikipedia/commons/6/69/June_odd-eyed-cat_cropped.jpg
581632/580625 [==============================] - 0s 0us/step
589824/580625 [==============================] - 0s 0us/step
Downloading data from https://upload.wikimedia.org/wikipedia/commons/b/b5/2008-08-28_White_German_Shepherd_ready.jpg
4276224/4271571 [==============================] - 0s 0us/step
4284416/4271571 [==============================] - 0s 0us/step
Downloading data from https://upload.wikimedia.org/wikipedia/commons/d/df/Dogs_were_not_around_in_the_early_Cenozoic.png
1966080/1959233 [==============================] - 0s 0us/step
1974272/1959233 [==============================] - 0s 0us/step
```

```python
def predict(model, image):
  ''' Take model & image, preprocess image, make predictions, and return results'''

    image = tf.keras.preprocessing.image.load_img(image, target_size=(180,180))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = image/255.0
    image = tf.expand_dims(image, 0)

    predicted_class = model.predict(image)[0]
    rounded_predicted_class = tf.round(predicted_class)

    print(f"DISPLAYING THE PREDICTION RESULTS:\n \
    ---------- \n \
    Predicted class probability: {predicted_class}\n \
    Predicted class: {rounded_predicted_class}\n \
    Predicted class name: {'Dog' if rounded_predicted_class == 1 else 'Cat'}")
```

```python
predict(loaded_model, dog_im1)
plt.imshow(tf.keras.preprocessing.image.load_img(dog_im1, target_size=(180,180)));
```

**Execution Output:**
```text
DISPLAYING THE PREDICTION RESULTS:
     ---------- 
     Predicted class probability: [0.99823844]
     Predicted class: [1.]
     Predicted class name: Dog
```

```python
predict(loaded_model, cat_im1)
plt.imshow(tf.keras.preprocessing.image.load_img(cat_im1, target_size=(180,180)));
```

**Execution Output:**
```text
DISPLAYING THE PREDICTION RESULTS:
     ---------- 
     Predicted class probability: [0.00061188]
     Predicted class: [0.]
     Predicted class name: Cat
```

```python
predict(loaded_model, dog_im2)
plt.imshow(tf.keras.preprocessing.image.load_img(dog_im2, target_size=(180,180)));
```

**Execution Output:**
```text
DISPLAYING THE PREDICTION RESULTS:
     ---------- 
     Predicted class probability: [0.9991021]
     Predicted class: [1.]
     Predicted class name: Dog
```

```python
predict(loaded_model, cat_im2)
plt.imshow(tf.keras.preprocessing.image.load_img(cat_im2, target_size=(180,180)));
```

**Execution Output:**
```text
DISPLAYING THE PREDICTION RESULTS:
     ---------- 
     Predicted class probability: [2.567915e-06]
     Predicted class: [0.]
     Predicted class name: Cat
```

<a name='4'></a>

## 4. Image Augmentation with Keras Image Augmentation Layers

`ImageDataGenerator` makes it easy to augment images while while loading them from the directory at the same time. 

But there is a time you may want the augmentation to takes place inside the model. In that case, you can use [Keras Image Augmentation layers](https://keras.io/api/layers/preprocessing_layers/image_augmentation/). These layers can be part of the model, and what that means is that the input image to a model will be augmented first before undergoing further preprocessing. 

But why would you want the images to be augmented inside the model? The single most advantage of it is that when you save a model, these layers are saved too. If you deploy a model to the mobile device for example, the images will be preprocessed automatically, and you won't have to write custom preprocessing codes. Also, as they are together with other model layers, you will benefit from GPU acceleration.

These types of layers can also be used to preprocess and augment images directly, or outside the model. 

A something worth noting is that just like [dropout](https://keras.io/api/layers/regularization_layers/dropout/) and [batch normalization](https://keras.io/api/layers/normalization_layers/batch_normalization/) layers, data augmentation layers are only active during model training(`model.fit()`), and inactive during model evaluation(`model.evaluate()`) and predictions (`model.predict()`)

Before TensorFlow 2.6, these layers were in experimentation. But in version 2.6, they can be used as other layers and there is no worries that they will go anywhere. 

Here is a list of available image augmentation layers: 

* [RandomCrop layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_crop)
* [RandomFlip layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_flip)
* [RandomTranslation layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_translation)
* [RandomRotation layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_rotation)
* [RandomZoom layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_zoom)
* [RandomHeight layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_height)
* [RandomWidth layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_width)
* [RandomContrast layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_contrast)

We are going to practice how to use these layers inside and outside the model. We are also going to do something different: We will use [TensorFlow Datasets](https://www.tensorflow.org/datasets).

<a name='4-1'></a>

## 4.1 Getting the Data Again

Let's use the same dataset (cats_vs_dogs), but we will get it from TensorFlow datasets to also learn how to work with TF datasets. 

The [cats_vs_dogs](https://www.tensorflow.org/datasets/catalog/cats_vs_dogs) is available in TensorFlow datasets and it contains 23,262 images.

```python
import tensorflow as tf
from tensorflow import keras
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import numpy as np
```

Here are few notes about loading data with `tfds.load(...)`

* The first thing to be provided while loading the dataset, it is the name of such dataset. The names are pretty clear in [TFDS catalog](https://www.tensorflow.org/datasets/catalog/overview). 
* We can directly split the data into training and test with `split` argument. With `split=('train[:80%]','train[80%:]')`, 80% of train is assigned to training data, and 20% of it is allocated to validation data. 

A quick note about these 3 popular sets: training set is used for training the model, validation set is for evaluating the model during training, and test set is a new data that we use to test the model. In the real world projects, validation set should have the same distribution as test set. 

* Setting `as_supervised` to true will return a tuple of image and label`(image, label)`instead of a dictionary`({'image': img, 'label': label})`.

* And `with_info=True` will return the information of the concerned dataset.

```python
(train_data, val_data), info = tfds.load('cats_vs_dogs:4.0.0',
                                         split=('train[:80%]','train[80%:]'),
                                         as_supervised=True,
                                         with_info = True
)
```

**Execution Output:**
```text
[1mDownloading and preparing dataset cats_vs_dogs/4.0.0 (download: 786.68 MiB, generated: Unknown size, total: 786.68 MiB) to /root/tensorflow_datasets/cats_vs_dogs/4.0.0...[0m


Shuffling and writing examples to /root/tensorflow_datasets/cats_vs_dogs/4.0.0.incompleteRB4W93/cats_vs_dogs-train.tfrecord
[1mDataset cats_vs_dogs downloaded and prepared to /root/tensorflow_datasets/cats_vs_dogs/4.0.0. Subsequent calls will reuse this data.[0m
```

We can see the dataset size by...

```python
print("The number images in training set: {}".format(len(train_data)))
print("The number images in validation set: {}".format(len(val_data)))
```

**Execution Output:**
```text
The number images in training set: 18610
The number images in validation set: 4652
```

Or use `info` to get number of examples.

```python
# Getting the number of examples 

info.splits['train'].num_examples
```

**Execution Output:**
```text
23262
```

Let's also get class names from `info.features`

```python
# getting class names
# Only display the first 10 classes..There are 120 classes

class_names = info.features['label'].names
class_names
```

**Execution Output:**
```text
['cat', 'dog']
```

```python
# Number of classes

info.features['label'].num_classes
```

**Execution Output:**
```text
2
```

Now that the data is loaded, let's visualize some images. It's always a cool thing to do.

<a name='4-2'></a>

## 4.2 Looking in Images

As always, it's good to peep in images and see if there are images that are labelled incorrectly, or have an extenstion of `.pdf` when in fact all images should be `.png` or `jpg.`

As you might guess, TensorFlow datasets are remarkably prepared, but in real life, incorrect labelling and formats can exist. 

Let's use `tfds.visualization(..)` to visualize some images.

```python
fig = tfds.show_examples(train_data, info)
```

<a name='4-3'></a>

## 4.3 Preparing Data: Building a Training Pipeline

Now, let's prepare the data, specifically, building an input pipeline.

First, the tensorflow datasets are returned as `uint8`, we need to resize and normalize the images while also converting it to `float32`.

```python
def preprocess(image, label):

    """ 
    Take image and label, 
    Resize images to 180, 180
    convert images to float32, and return converted image &label
    """

    resized_image = tf.image.resize(image, [180, 180])
    normalized_img = tf.cast(resized_image, tf.float32)/255.0

    return normalized_img, label
```

Now, we can apply the above function to the dataset with `map`. Along the way, we will shuffle it, and batch the images. 

We do not shuffle the test set.

```python
def train_data_prep(data, shuffle_size, batch_size):

    data = data.map(preprocess)
    data = data.cache()
    data = data.shuffle(shuffle_size)
    data = data.batch(batch_size)
    data = data.prefetch(1)
    return data

def val_data_prep(data, batch_size):

    data = data.map(preprocess)
    data = data.batch(batch_size)
    data = data.cache()
    data = data.prefetch(1)
    return data
```

```python
train_data_prepared = train_data_prep(train_data, 1000, 32)
val_data_prepared = val_data_prep(val_data, 32)
```

<a name='4-4'></a>

## 4.4 Augmenting Images with Augmentation Layers

Learn more about Image Augmentation layers at [Keras doc](https://keras.io/api/layers/preprocessing_layers/image_augmentation/).

```python
augmentation_layers = tf.keras.Sequential([
     tf.keras.layers.RandomFlip('horizontal_and_vertical'),
     tf.keras.layers.RandomRotation(0.2),
     tf.keras.layers.RandomContrast(0.4)
])
```

To illustrate augmentation, let's apply the above layers to the images. Because the images are already converted into batch, running the cell below will plot a given image in a batch (running it again displays a different image). And it will later be augmented.

```python
image = train_data_prepared.take(1)
image, label = next(iter(image))

plt.imshow(image[0])
plt.title(class_names[label[0]]);
```

```python
plt.figure(figsize=(12,12))

for i in range(16):
    augmented_image = augmentation_layers(image)
    ax = plt.subplot(4,4,i+1);
    plt.imshow(augmented_image[0]);
    plt.axis('off');
```

As we can see from the above, it is pretty clear that the input image were transformed into many ways, from flipping, contrast change to being cropped. It's very amazing to just stack layers and use them to augment images on the fly.

<a name='4-5'></a>

## 4.5 First Option: Using the Augmentation layers Outside the Model

Like we have seen, the augmentation layers can be used inside the model or outside the model. To use them outide the model is pretty straight. Just use a `lambda` function to get the image and label and apply the augmentation layers to every single image with a [map](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map) function and return augmented image and label. 

Note that we do not augment the validation and test data.

```python
train_data_augmented = train_data_prepared.map(lambda image, label: (augmentation_layers(image, training=True), label))
```

Now we can build the Convnet model.

```python
model = tf.keras.Sequential([
                             
  # First Conv and maxpooling layer                         
  tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2),

  # Second Conv and maxpooling layer 
  tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2),

  # Third Conv and maxpooling layer 
  tf.keras.layers.Conv2D(128, 3, padding='same', activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2),
  
  # Fourth Conv and maxpooling layer 
  tf.keras.layers.Conv2D(256, 3, padding='same', activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2),

  # Flattening the feature maps into a 1D vector 
  tf.keras.layers.Flatten(),

  # Adding fully connected layers
  tf.keras.layers.Dense(256, activation='relu'),
  
  # Applying dropout to avoid overfitting
  tf.keras.layers.Dropout(0.3),

  tf.keras.layers.Dense(1, activation='sigmoid')
])
```

```python
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
```

```python
history = model.fit(
  train_data_augmented,
  validation_data=val_data_prepared,
  epochs=10
)
```

**Execution Output:**
```text
Epoch 1/10
582/582 [==============================] - 1670s 3s/step - loss: 0.6910 - accuracy: 0.5494 - val_loss: 0.6827 - val_accuracy: 0.5363
Epoch 2/10
582/582 [==============================] - 1658s 3s/step - loss: 0.6480 - accuracy: 0.6238 - val_loss: 0.6178 - val_accuracy: 0.6492
Epoch 3/10
582/582 [==============================] - 1657s 3s/step - loss: 0.6048 - accuracy: 0.6724 - val_loss: 0.5553 - val_accuracy: 0.7104
Epoch 4/10
582/582 [==============================] - 1666s 3s/step - loss: 0.5841 - accuracy: 0.6908 - val_loss: 0.5539 - val_accuracy: 0.7279
Epoch 5/10
582/582 [==============================] - 1659s 3s/step - loss: 0.5639 - accuracy: 0.7081 - val_loss: 0.5472 - val_accuracy: 0.7317
Epoch 6/10
582/582 [==============================] - 1659s 3s/step - loss: 0.5424 - accuracy: 0.7246 - val_loss: 0.5120 - val_accuracy: 0.7569
Epoch 7/10
582/582 [==============================] - 1662s 3s/step - loss: 0.5366 - accuracy: 0.7311 - val_loss: 0.4940 - val_accuracy: 0.7614
Epoch 8/10
582/582 [==============================] - 1658s 3s/step - loss: 0.5133 - accuracy: 0.7475 - val_loss: 0.4917 - val_accuracy: 0.7607
Epoch 9/10
582/582 [============================
... [Output truncated for brevity]
```

```python
model_history_5 = history.history

acc = model_history_5['accuracy']
val_acc = model_history_5['val_accuracy']
loss = model_history_5['loss']
val_loss = model_history_5['val_loss']

epochs = history.epoch

plot_acc_loss(acc, val_acc, loss, val_loss, epochs)
```

That was about training the model with the augmented images. Like we said, we can also have the the augmentation layers inside the model and take the advantage of GPU accelerations.

<a name='4-6'></a>

## 4.6 Second Option: Using the Augmentation layers Inside the Model

The augmentation layers that we created early will be the first layer in the model. At every training epoch, a given image is augmented(as described in the layers we defined above) before undergoing further transformations.

```python
model = tf.keras.Sequential([
                             
  # Augmentation layers

  augmentation_layers,
              
  # First Conv and maxpooling layer                         
  tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2),

  # Second Conv and maxpooling layer 
  tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2),

  # Third Conv and maxpooling layer 
  tf.keras.layers.Conv2D(128, 3, padding='same', activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2),
  
  # Fourth Conv and maxpooling layer 
  tf.keras.layers.Conv2D(256, 3, padding='same', activation='relu'),
  tf.keras.layers.MaxPooling2D(2,2),

  # Flattening the feature maps into a 1D vector 
  tf.keras.layers.Flatten(),

  # Adding fully connected layers
  tf.keras.layers.Dense(256, activation='relu'),
  
  # Applying dropout to avoid overfitting
  tf.keras.layers.Dropout(0.3),

  tf.keras.layers.Dense(1, activation='sigmoid')
])
```

```python
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
```

```python
history = model.fit(
  train_data_prepared,
  validation_data=val_data_prepared,
  epochs=10
)
```

**Execution Output:**
```text
Epoch 1/10
582/582 [==============================] - 1711s 3s/step - loss: 0.6802 - accuracy: 0.5593 - val_loss: 0.6397 - val_accuracy: 0.6182
Epoch 2/10
582/582 [==============================] - 1662s 3s/step - loss: 0.6338 - accuracy: 0.6377 - val_loss: 0.6296 - val_accuracy: 0.6505
Epoch 3/10
582/582 [==============================] - 1656s 3s/step - loss: 0.5885 - accuracy: 0.6877 - val_loss: 0.6099 - val_accuracy: 0.6808
Epoch 4/10
582/582 [==============================] - 1657s 3s/step - loss: 0.5749 - accuracy: 0.7015 - val_loss: 0.5250 - val_accuracy: 0.7367
Epoch 5/10
582/582 [==============================] - 1660s 3s/step - loss: 0.5593 - accuracy: 0.7127 - val_loss: 0.5245 - val_accuracy: 0.7416
Epoch 6/10
582/582 [==============================] - 1655s 3s/step - loss: 0.5433 - accuracy: 0.7236 - val_loss: 0.5365 - val_accuracy: 0.7281
Epoch 7/10
582/582 [==============================] - 1652s 3s/step - loss: 0.5353 - accuracy: 0.7303 - val_loss: 0.4975 - val_accuracy: 0.7620
Epoch 8/10
582/582 [==============================] - 1658s 3s/step - loss: 0.5183 - accuracy: 0.7440 - val_loss: 0.4943 - val_accuracy: 0.7610
Epoch 9/10
582/582 [============================
... [Output truncated for brevity]
```

```python
model_history_6 = history.history

acc = model_history_6['accuracy']
val_acc = model_history_6['val_accuracy']
loss = model_history_6['loss']
val_loss = model_history_6['val_loss']

epochs = history.epoch

plot_acc_loss(acc, val_acc, loss, val_loss, epochs)
```

That's it for using the Keras image augmentation layers. As it looks, the model with the augmentation layers inside seems bstter than the one with pre augmented images. And they were all trained with similar hyperparameters.

## [BACK TO TOP](#0)

---

## Key Interview Concepts: CNN Operations

1. **Why CNNs over Dense MLPs for Images?**:
   - **Parameter Explosion**: A $256 \times 256 \times 3$ image input into an MLP hidden layer of 1000 neurons requires over 196 million weights for layer 1 alone!
   - **Spatial Hierarchy**: CNNs exploit 2D grid structure, learning local low-level features (edges, textures) in early layers and high-level semantic features (eyes, wheels, faces) in deeper layers.
   - **Translation Invariance**: An object recognized in the top-left corner can be recognized anywhere in the image due to parameter sharing.
2. **Convolution Math**:
   - Output spatial dimension given input size $W$, kernel size $K$, padding $P$, and stride $S$:
     $$\text{Output Size} = \left\lfloor \frac{W - K + 2P}{S} \right\rfloor + 1$$
   - **Valid Padding**: $P = 0$ (output shrinks).
   - **Same Padding**: $P = \frac{K - 1}{2}$ (output spatial dimensions match input when $S = 1$).
3. **Data Augmentation Techniques**:
   - Random rotations, horizontal/vertical flips, zoom ranges, shear transformations, width/height shifts.
   - Prevents the network from memorizing training pixels, forcing it to learn invariant structural patterns.
