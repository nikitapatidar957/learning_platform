# Artificial Neural Networks: Regression & Classification with TensorFlow

Master multi-layer perceptron (MLP) architecture design, activation functions, TensorFlow APIs, loss formulation, model compilation, training loops, hyperparameter optimization, and evaluation for continuous and categorical targets.

---

## 1. Intro to Neural Networks & Architecture Fundamentals

<a name='0'></a>
# Intro to Artificial Neural Networks and Deep Learning

Deep Learning is the study of Artificial Neural Networks(ANNs). It is a subset of Machine Learning (ML), ML being a subset of Artificial Intelligence. 

Inspired by the human brain's biological neuron, ANNs has become the building block of modern intelligent systems, from our smartphones that can accurately identify our faces and voices, streaming services (like YouTube and Netflix) that know exactly what we want to watch, cars that can see the visual world and drive themselves, and not to mention AlphaGo that won world chess competition. 


This notebook will introduce a high level overview of Deep Learning.

## Contents 

* [1. Why Deep Learning](#1)
* [2. A Single Layer Neural Network](#2)
* [3. Activation Functions](#3)
* [4. Types of Deep Learning Architectures](#4)
    * [4.1 Densely Connected Networks](#4-1)
    * [4.2 Convolutional Neural Networks](#4-2)
    * [4.3 Recurrent Neural Networks](#4-3)
    * [4.4 Transformers](#4-4)
* [5. Challenges in Training Deep Neural Networks](#5)

<a name='1'></a>

## 1. Why Deep Learning

Deep Learning is used to extract the patterns in (a huge amount of) data. Its potential has been seen in complex problems such as vision oriented and natural language. 

Let's take an example to develop more intuitive understanding of why deep learning has became so popular. Let's say that as an Engineer, you are asked by your city state to build a program that can recognize car and truck moving in a given road. The program can later be deployed in a less loads-road to warn trucks that pass there that the road was not designed for these types of vehicles. 

With normal programming, you would have to provide and to write all instructions (codes) of that particular program. The chance (close to reality) is that it would be hard, mostly because there are different types of cars and trucks and each can be unique in its ways, which can make it hard to write the rules forming such program. 

How can deep learning solve that? Well, by feeding the images of cars and trucks to a deep learning model, say a convolutional neural network (more on this latter), it can learn the underlying features of cars and trucks, and thus will be able to recognize each and each. We will see this in practice in later notebooks.

With the advent of the computation power, both paid and free (Google Colab & Kaggle), open source datasets, and intelligent frameworks such as TensorFlow and PyTorch, it has become very much possible to do deep learning, even at personal level. This was not possible a decade ago.

<a name='2'></a>
## 2. A Single Hidden Layer Neural Network

<img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Neuralnetwork.png" alt="Neuralnetwork.png"><br> Image: A Single hidden layer neural network, Wikimedia

The image above represent a single hidden layer neural network. Usually, any typical neural network has 3 main layers:

* **Input layer** that takes the input data. The input data can be image, text, or numbers but ofcourse whatever the data type is, the input to a neural network will always have to be in a numeric format. 

* **Hidden layer** that is between the input and the output layers. There is a alot of computations that takes place in this layer but that is not in the scope of this notebook. 
* **Output layer** that give the output of the network. Output can be a numerical number (mostly in regression problem) or a probability (mostly in classification problem). 


A neural network having more than one layer is commonly referred to `Deep Neural Network(DNN)`. Also, it is important to note that a neural network can have multiple input layers, multiple hidden layers, and multiple output layers. The structure of how a neural network has to be or its size will mostly depend on the type of a problem being solved. 

With the exception of the input layer, you will find something called activation function being applied to hidden and output layers. What is an activation function?

<a name='3'></a>

## 3. Common Activation Functions

Activation functions are used to introduce nonlinearities in the network. I like to say that they dictate the output format of a given layer. 

Or simply put, these type of mathematical functions are used to make a decision of the layer's output. In later notebooks, this will certainly make sense. 

Here are the 3 most used activation functions:

* **ReLU(Rectified Linear Unit)**: This is mostly used in hidden layers and it is a default activation function in most problems that will work well in most cases. ReLU always give the positive outputs, if the input number is greater than 0, the output will be that number. If it's less than 0, the output will be 0. The whole purpose of this type of activation function is to penalize the negative numbers. ReLu has different versions such as SeLU and LeakyReLU. In most cases, ReLU can only be used in output layer when the problem is a regression type, but this is not a necessity too. 


* **Sigmoid**: A sigmoid function gives the probabilistic output (a number between 0 and 1). It can be used in output layers of a classification problem. 


* **Softmax**: This type of function is also used in output classification layers, but instead of giving probalistic output, its output is an actual classes. This will make sense in later notebooks.

<a name='4'></a>

## 4. Types of Deep Learning Architectures

There are 4 main types of deep learning architectures. This is going to be a high level since they will be covered in the next notebooks.

<a name='4-1'></a>

### 4.1 Densely Connected Networks

Densely connected networks are made of stacks of layers from the input to the output. 

The units (or neurons) of any layer in that type of network are connected to all other units of the next layer. This is why they are also called fully connected layers. 

Densely connected layers are generally used for tabular data. Tabular data are these kinds of data that are in a tabular fashion. An example of tabular data is customer records: you have a column of names, roles, data joined, etc...


![Densely connected.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1631359484854/ioMW08ea2.png)
*Image: Densely connected networks*

Dense layers are also used (in the combination of other architectures) as the last layer in either classification or regression problems. The right number of units in the last layer depends on the problem. Take an example: if you are classifying the news into 4 categories, then the last layer will have 4 units. If you are predicting the price of a house given its features, the last layer will have 1 unit. 


Dense networks are mostly used in simple tasks. When it comes to complex things like image recognition or text processing, they fail because they can't hold spatial features (in image) or can't learn a sequence in text for instance. But above all, the more deep they become, they tend to have many parameters which can results in having a big network/complex computations.

<a name='4-2'></a>

### 4.2 Convolutional Neural Networks

CNN's, a.k.a Convnets are widely known as the go-to neural network architectures for computer vision tasks like image recognition and object detection, but they can also be used in other tasks such as texts and time series processing. 

Convnets are typically made of convolution, pooling layers, and fully connected layers at the end. Convolutional layers are used to extract the spatial features in images, and pooling layers are used to compress the resulted feature maps from convolution layers. And fully connected layers for classification purposes. 

![on-IOL-iG.png-2.webp](https://cdn.hashnode.com/res/hashnode/image/upload/v1630788206761/KF4gj3zPD.webp)
*Image: Convnets architecture*

Convnets are of 3 dimensions. The most popular one is Conv2D that is used in images and videos divided into frames. Conv1D is used in sequential data such as texts, time series, and sounds. A popular sound architecture called [WaveNet](https://deepmind.com/blog/article/wavenet-generative-model-raw-audio) is made of 10 stacked 1D Convnets.

Conv3D is used in videos and volumetric images such as CT scans.

<a name='4-3'></a>

### 4.3 Recurrent Neural Networks (RNNs)

The standard feedforward network (or call them densely connected network) maps the input to output. RNNs go beyond that. They can maintain the recurrence of data at each time step. 


![TF RNN.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1630789332991/7kzTaiwxp.png)
*Image: Feed forward network vs recurrent neural networks*

Due to their ability to preserve the recurrence of information, RNNs are commonly used in sequential data such as texts and time series. 

The basic RNN cells are not efficient at handling large sequences due to a short memory problem. They also suffer from vanishing gradients. 

The variant of RNNs that are able to handle long sequences is called Long Short Term Memory(LSTM). LSTM has also the ability to handle the sequences of variable lengths.  

A special design difference about the LSTM cell is that it has a gate which is the basis of why it can control the flow of information over many time steps. 

In short, LSTM uses gates to control the flow of information from the current time step to the next time step in the following 4 ways: 

  * The input gate recognizes the input sequence.
  * Forget gate gets rid of all irrelevant information contained in the input sequence and store relevant information in long term memory.
  * LTSM cell updates update cell's state values.
  * Output gate controls the information that has to be sent to the next time step. 

![Screen Shot 2021-09-01 at 09.22.56.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1630789390006/avzF2LKrK.png)

*Image: LSTM architecture*

The ability of LSTMs to handle long-term sequences makes it a suitable neural network architecture for various sequential tasks such as text classification, sentiment analysis, speech recognition, image caption generation, machine translation. 

Another recurrent neural network that you will see is [Gate Recurrent Unit(GRU)](https://arxiv.org/pdf/1412.3555.pdf). GRU is a simplified version of LSTMs, and it's cheaper to train.

<a name='4-4'></a>

### 4.4 Transformers

Although recurrent neural networks are still used for sequential modeling, they have short-term memory problems when used for long sequences, and they are computationally expensive. The RNN's inability to handle long sequences and expensiveness are the two most motivations of transformers. 

Transformers are one of the latest groundbreaking researches in the natural language community. They are sorely based on the attention mechanisms that learn the relationships between words of the sentence and pays attention to the relevant words. 

One of the most notable things about transformers is that they don't use any recurrent or convolutional layers. It's just only attention mechanisms and other standard layers like embedding layer, dense layer, and normalization layers. 

They are commonly used in language tasks such as text classification, question answering, and machine translation. 

There have been [researches](https://arxiv.org/pdf/2101.01169.pdf) that show that they can also be used for computer vision tasks, such as image classification, object detection, image segmentation, and image captioning with [visual attention](https://arxiv.org/pdf/1502.03044.pdf).  


![Screen Shot 2021-09-04 at 23.16.48.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1630790223290/99Ltf-fAy.png)

*Image: Transformers architecture, [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf)*

Below is a high level summary of the common neural networks architectures. 

![Deep Learning Architectures.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1631774267019/jzEyGcRBWM.png)

<a name='5'></a>

## 5. Challenges in Training Neural Networks

Training neural networks is a big challenge and this still an area of research. For example, how do you choose a right architecture? Although the type of data can tell the most architecture that should come into picture at first, it is not a trivial question. Take an example, we know CNN as image first algorithm, bit it has been used in some natural language processing and time series tasks and it can perform well. 

Also, deep learning models have many hyperparameters. Hyperparameters include things like number of layers, number of neurons, learning rate, activation functions, and optimizers (optimizers are used to reduce loss during training).  

All these choises to be make it hard to train neural networks. Although there has been some techniques that can reduce number of choices to be made, such as transfer learning which motivates reusing the pretrained models, training this type of models is not an easy thing.

#### Also, before we go into hands-on deep learning in the next notebooks, I would like to invite you to play this game. Tinker with it and try to see how things like activation functions, input data, learning rate,...affects the neural network training. [***Here you Go!***](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.93635&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false).

### [BACK TO TOP](#0)

---

## 2. TensorFlow Deep Learning Core APIs & Tensors

<a name='0'></a>
# Intro to TensorFlow for Deep Learning

## Contents 

* [1. What is TensorFlow?](#1)
* [2. TensorFlow Model APIs](#2)
   * [2.1 Sequential API](#2-1)
   * [2.2 Functional API](#2-2)
   * [2.3 Model SubClassing API](#2-3)

* [3. A Quick Tour into TensorFlow Ecosystem](#3)
   * [3.1 Tools](#3-1)
   * [3.2 Models and Datasets](#3-2)
   * [3.3 Model Deployment](#3-3)

* [4. Basics Tensors](#4)
   * [4.1 Intro to Tensors](#4-1)
   * [4.2 Creating a Tensor with tf.constant()](#4-2)
   * [4.3 Creating a Tensor with tf.variable()](#4-3)
   * [4.4 Creating A Tensor from Existing Functions](#4-4)
   * [4.5 Selecting Data in a Tensor](#4-5)
   * [4.6 Performing operations on Tensors](#4-6)
   * [4.7 Manipulating a Tensor Shape](#4-7)

<a name='1'></a>

## 1. What is TensorFlow

TensorFlow is an open source and an end to end platform used for building machine learning models. Being end to end, you can prepare data, build models, diagnose, improve, and deploy them. 

TensorFlow uses [Keras](https://keras.io) at its backend. Keras is a well beautifully designed API for building deep learning models in popular fields such as Computer Vision and Natural Language Processing. 

TensorFlow has got a strong community, from users, learning resources and whole range of technical supports. Not only it powers majority of Google apps such as YouTube, Maps and Google Photos, it is also widely used across startups and other big techs.

<a name='2'></a>

## 2. TensorFlow Model APIs

TensorFlow being suited for variety of tasks, there are 3 ways to build deep learning models.

<a name='2-1'></a> 
 ### 2.1 Sequential API

This is the simplest model building option. When building a model, you start from the input to the output, no other way around. This API is suited for tasks that don't require multiple inputs or outputs, or skip connections. 

Sequential API can be a good API to use for things like image classification or regression tasks. With things like object detection and segmentation, we need another API, which is Functional API. 

Below is how a sequential model looks like. 

```
# Building a sequential model 

from tensorflow import keras

 
model = keras.models.Sequential([
        
        keras.layers.Dense(16, activation='relu'),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(1, activation='sigmoid')
        
])
    
```

<a name='2-2'></a>
### Functional API

This type of API makes it easy to build models that can take multiple inputs/outputs, or skip connections. 

It is well suited in advanced things like object detection and segmentation. In object detection, there are two main involved things. 

One is recognizing the object(classification) and other is localizing the object(regression: predicting the bounding boxes coordinates).

![kites_detections_output.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1616839653654/-NiIL9N3v.jpeg)

Below is how a functional model looks like.

```
# Building a same model in Functional API

from tensorflow import keras

inputs = keras.Input()
x = keras.layers.Dense(16, activation='relu')(inputs)
x = keras.layers.Dense(32, activation='relu')(x)
output = keras.layers.Dense(1, activation='sigmoid')(x)
    
model = keras.Model(inputs, output)
```

<a name='2-3'></a>

### Model SubClassing

SubClassing API is for building custom models and having full control of every step in model building and training. 

In most cases, Sequential and Functional API will be all you need to build almost anything. 

Below is how a subclassing model looks like.

```
# Building a same custom model 

from tensorflow import keras

class MLP(keras.Model):

  def __init__(self, **kwargs):
    super(MLP, self).__init__(**kwargs)
    self.dense_1 = keras.layers.Dense(16, activation='relu')
    self.dense_2 = keras.layers.Dense(32, activation='relu')
    self.dense_3 = keras.layers.Dense(1, activation='sigmoid')

  def call(self, inputs):
    x = self.dense_1(inputs)
    x = self_dense_2(x)
    x = self_dense_3(x)
    
    return x

# Instantiate the model

mlp = MLP()
```

<a name='3'></a>

## 3. A Quick Tour into TensorFlow Ecosystem

Beside community, one of my favourite things I like about TensorFlow is its whole ecosystem of tools and resources. Below is a list of tools, libraries, and resources that are built to simplify things.

<a name='3-1'></a>

### Tools

#### 1. Colaboratory

[Colaboratory](https://colab.research.google.com/notebooks/intro.ipynb) is a free web version of jupyter notebook that doesn't require any set up. You can import almost any library without having to install it. 

#### 2. TensorBoard

[TensorBoard](https://tensorboard.dev/) provides the engineers and scientists with the visualizations and debugging capabilities for their Machine Learning models. 

With TensorBoard, you can:

   * Track and visualize the loss and accuracy metrics
   * View the weights, biases, and other parameters in plots format such as histogram or line plot
   * Display image, audio, and text data
   * See which hyperparameters might be a good match for the model to converge
   

![Tensorboard.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1616575702847/t9hohDbAY.png)

<a name='3-2'></a>

### Models and Datasets

#### 1. TensorFlow Hub

[TensorFlow Hub](https://tfhub.dev/) is a collection of ready to use models in variety of tasks, from image recognition, object detection, image segmentation, sound recognition, text classification, etc..

#### 2. Model Garden

Model Garden is an [official GitHub repository of TensorFlow models](https://github.com/tensorflow/models/tree/master/official), build with high-level APIs. The models available are Computer Vision, Natural Language Processing, and recommendation.

**************

There are so many tools and functionalities that are provided by TensorFlow. This was a quick walkthrough the TensorFlow ecosystem.

<a name='3-3'></a>
### Models Deployment

#### 1. TensorFlow Extended (TFX)

[TFX](https://www.tensorflow.org/tfx/) is an end to end platform for creating machine learning pipelines. With TFX, you can prepare data, train models, validate them, and deploy them in production environments.

#### 2. TensorFlow.js

[TensorFlow.js](https://www.tensorflow.org/js/) makes it easy to train and deploy model in web browsers. 

#### 3. TensorFlow Lite 

[TF Lite](https://www.tensorflow.org/lite/) makes it possible to train, deploy and optimize models in mobile devices and microcontrollers.

<a name='4'></a>

## 4. The Basics of Tensors

<a name='4-1'></a>
### 4.1 Intro to Tensors

A tensor is a multidimensional array of the same data type. A tensor can be a scalar (single number), a vector, or a matrix. 

If you have used NumPy, tensors are like NumPy arrays, except that tensors have GPU(Graphical Processing Unit) support. 

A typical tensor has the following information:

* **Shape**: The length or number of elements of each of the tensor dimension/axes.
* **Rank**: The number of dimensions/axes in a tensor. A scalar tensor (a single number) has rank 0, a vector has a rank 1 (a vector is a 1D), and a matrix has rank 2 (or 2D). 
* **Axis/Dimension**: This is a particular dimension of a tensor
* **Size**: This is the total number of items in the tensor. 

But why tensor/NumPy array things? 

Well, almost all types of data ca be represented as an array of numbers. Take an example: 

* Image can be represented as an array of pixels. 
* Any text data can be converted into an array of numbers (or tokens representing words)
* Video (made of sequence of images) can be represented as an array of numbers. 

Having the ability to convert these raw data into tensors/arrays make it easy to preprocess it, either when performing conventional numerical computations or when it is the data we are preparing to feed to a machine learning model. Take a simple example, we can not feed a raw text to a machine learning model. That text has to be converted into numbers. 
 

In later parts, we will see how to:

* Create a tensor with tf.constant()
* Create a tensor with tf.variable()
* Create tensors from existing functions
* Select data in a tensor
* Perform operations in tensor
* Manipulate tensor shape

<a name='4-2'></a>

### 4. 2 Creating a Tensor with tf.constant()

A Tensor can be a scalar, a vector or a matrix. 
Let's use `tf.constant()` to create these tensor types. 

A tensor created with `tf.constant()` is immutable.

```python
# I will first import tensorflow as tf
# Also import numpy as np
# If you are using Colab, no need to install them 

import tensorflow as tf
import numpy as np
```

```python
# Creating a scalar tensor
# You can specify dtype but TF will detect its if left unspecified

scalar_tensor = tf.constant(10)
```

```python
# Displaying created tensor

print(scalar_tensor)
```

**Execution Output:**
```text
tf.Tensor(10, shape=(), dtype=int32)
```

```python
# We can also create a vector or rank 1 tensor
# Simply put, a vector is one dimensional
# We can create it from a list of values

vect_tensor = tf.constant([1.0,2.0,3.0,4.0,5.0,6.0])
```

```python
print(vect_tensor)
```

**Execution Output:**
```text
tf.Tensor([1. 2. 3. 4. 5. 6.], shape=(6,), dtype=float32)
```

A vector of 1 dimensional values was created. As you can see, the data type is `float32` because the values were floats. TensorFlow detects that automatically from values if the data type was not mentioned. 

Let's now create a tensor with rank 2 or two dimensions. This is actually a matrix.

```python
mat_tensor = tf.constant([[2,4],
                         [6,8],
                         [10,12]], dtype=tf.int32)
```

```python
print(mat_tensor)
```

**Execution Output:**
```text
tf.Tensor(
[[ 2  4]
 [ 6  8]
 [10 12]], shape=(3, 2), dtype=int32)
```

If you can see in the displayed tensor above, the shape is `(3,2)` which means our tensor has 3 rows and 2 columns. 

You can also check the number of dimensions or axes of a tensor using `tensor_name.ndim`

```python
scalar_tensor.ndim
```

**Execution Output:**
```text
0
```

A scalar tensor does not have any dimension. It's just a single value. But if we do the same thing for a vector or matrix, you will see something different.

```python
# A vector has 1 dimension

vect_tensor.ndim
```

**Execution Output:**
```text
1
```

```python
# A matrix has 2D or more dimensions

mat_tensor.ndim
```

**Execution Output:**
```text
2
```

Just like NumPy array, a tensor can have many dimensions. Let's create a tensor with 3 dimensions.

```python
tensor_3d = tf.constant([
                         [[1,2,3,4,5],
                         [6,7,8,9,8]],
                         [[1,3,5,7,9],
                         [2,4,6,8,1]],
                         [[1,2,3,5,4],
                         [3,4,5,6,7]], ])

print(tensor_3d)
```

**Execution Output:**
```text
tf.Tensor(
[[[1 2 3 4 5]
  [6 7 8 9 8]]

 [[1 3 5 7 9]
  [2 4 6 8 1]]

 [[1 2 3 5 4]
  [3 4 5 6 7]]], shape=(3, 2, 5), dtype=int32)
```

```python
tensor_3d.ndim
```

**Execution Output:**
```text
3
```

A tensor can be converted into NumPy array by calling `tensor_name.numpy` or `np.array(tensor_name)`. 

TensorFlow plays well with NumPy. And if not yet done, TensorFlow recently posted that they are working on gettint the whole of NumPy into TensorFlow.

```python
# Converting a tensor into a NumPy array

n_array = tensor_3d.numpy()

n_array
```

**Execution Output:**
```text
array([[[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 8]],

       [[1, 3, 5, 7, 9],
        [2, 4, 6, 8, 1]],

       [[1, 2, 3, 5, 4],
        [3, 4, 5, 6, 7]]], dtype=int32)
```

```python
# Using np.array(tensor_name)

np.array(tensor_3d)
```

**Execution Output:**
```text
array([[[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 8]],

       [[1, 3, 5, 7, 9],
        [2, 4, 6, 8, 1]],

       [[1, 2, 3, 5, 4],
        [3, 4, 5, 6, 7]]], dtype=int32)
```

<a name='4-3'></a>

### 4. 3 Creating a Tensor with tf.Variable()

A tensor created with `tf.constant()` is immutable, it can not be changed. Such kind of tensor can not be used as weights in neural networks because they need to be changed/updated in backpropogation for example. 

With `tf.Variable()`, we can create tensors that can be mutable and thus can be used in things like updating the weights of neural networks like said above. 

Creating variable tensor is as simple as the former.

```python
var_tensor = tf.Variable([
                         [[1,2,3,4,5],
                         [6,7,8,9,8]],
                         [[1,3,5,7,9],
                         [2,4,6,8,1]],
                         [[1,2,3,5,4],
                         [3,4,5,6,7]], ])

print(var_tensor)
```

**Execution Output:**
```text
<tf.Variable 'Variable:0' shape=(3, 2, 5) dtype=int32, numpy=
array([[[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 8]],

       [[1, 3, 5, 7, 9],
        [2, 4, 6, 8, 1]],

       [[1, 2, 3, 5, 4],
        [3, 4, 5, 6, 7]]], dtype=int32)>
```

It can also be converted to NumPy array, just like tensors created with `tf.constant()`

```python
# Converting a variable tensor into NumPy array

var_tensor.numpy()
```

**Execution Output:**
```text
array([[[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 8]],

       [[1, 3, 5, 7, 9],
        [2, 4, 6, 8, 1]],

       [[1, 2, 3, 5, 4],
        [3, 4, 5, 6, 7]]], dtype=int32)
```

<a name='4-4'></a>

### 4. 4 Creating a Tensor from Existing Functions

There some types of uniform tensors that you would not want to create from scratch, when in fact, they are already built. 

Take an example of 1's tensor, 0's, and random tensors. Let's create them.

```python
# Creating 1's tensor

ones_tensor = tf.ones([4,4])

print(ones_tensor)
```

**Execution Output:**
```text
tf.Tensor(
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]], shape=(4, 4), dtype=float32)
```

```python
# Creating 1's tensor

ones_tensor_1 = tf.ones([1,10])

print(ones_tensor_1)
```

**Execution Output:**
```text
tf.Tensor([[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]], shape=(1, 10), dtype=float32)
```

```python
# Creating zeros' tensor

tensor_0 = tf.zeros([3,3])
print(tensor_0)
```

**Execution Output:**
```text
tf.Tensor(
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]], shape=(3, 3), dtype=float32)
```

We can also create a tensor with random values. During the weights initialization in neural networks, weights take random values. 

You might be thinking that why aren't we building neural networks now and I get you. Understanding the basics of tensors and especially working with TensorFlow is useful when it comes to creating custom neural network layers, loss functions, or optimizers. 

The later labs will not deal with custom layers/losses/optimizers, this is only just an introduction, so that this can serve as a reference whenever you want to take a step back into the backbone of TensorFlow high level API.

```python
# Generating a tensor with random values 

# We first have to create a generator object

rand_tensor = tf.random.Generator.from_seed(3)

rand_tensor = rand_tensor.normal(shape=[3,3])
print(rand_tensor)
```

**Execution Output:**
```text
tf.Tensor(
[[-0.43640924 -1.9633987  -0.06452483]
 [-1.056841    1.0019137   0.6735137 ]
 [ 0.06987712 -1.4077919   1.0278524 ]], shape=(3, 3), dtype=float32)
```

Changing seed number in `tf.random.Generator.from_seed(3)` will change the values returned by random function.

We can also shuffle the existing tensor, created with `tf.constant()` or `tf.Variable()`.

```python
# Create a typical tensor 

example_tensor = tf.constant([[1,3],
                             [3,4],
                             [4,5]])

print(example_tensor)
```

**Execution Output:**
```text
tf.Tensor(
[[1 3]
 [3 4]
 [4 5]], shape=(3, 2), dtype=int32)
```

```python
def shuffle_tensor(tensor):

  """
  Take a tensor as input and return the shuffled tensor
  """
  # Shuffle the order of the created tensor

  tensor_shuffled = tf.random.shuffle(tensor)

  return print(tensor_shuffled)
```

```python
shuffle_tensor(example_tensor)
```

**Execution Output:**
```text
tf.Tensor(
[[4 5]
 [1 3]
 [3 4]], shape=(3, 2), dtype=int32)
```

If you rerun the above cell more than once, you will get different orders of tensor.

```python
shuffle_tensor(example_tensor)
```

**Execution Output:**
```text
tf.Tensor(
[[4 5]
 [3 4]
 [1 3]], shape=(3, 2), dtype=int32)
```

In order to prevent that, we can use `tf.random.set_seed(seed_number)` to always get the same order/values.

```python
# Set seed 

tf.random.set_seed(42)

shuffle_tensor(example_tensor)
```

**Execution Output:**
```text
tf.Tensor(
[[3 4]
 [4 5]
 [1 3]], shape=(3, 2), dtype=int32)
```

Everytime you can run `shuffle_tensor` function with a same seed, you will get the same order.

<a name='4-5'></a>

### 4. 5 Selecting Data in Tensor

We can also select values in any tensor, both single dimensional tensor and multi dimensional tensor.

```python
# Let's create a tensor

tensor_1d = tf.constant([1,2,3,4,5,6,7])
```

Let's select multiple values in tensor created above.

```python
print('The first value:', tensor_1d[0].numpy())
print('The second value:', tensor_1d[2].numpy())
print('From the 3 to 5th values:', tensor_1d[3:5].numpy())
print('From the 3 to last value:', tensor_1d[3:].numpy())
print('The last value:', tensor_1d[-1].numpy())
print('Select value before the last value:', tensor_1d[-2].numpy())
print('Select all tensor values:', tensor_1d[:].numpy())
```

**Execution Output:**
```text
The first value: 1
The second value: 3
From the 3 to 5th values: [4 5]
From the 3 to last value: [4 5 6 7]
The last value: 7
Select value before the last value: 6
Select all tensor values: [1 2 3 4 5 6 7]
```

Selecting/indexing data in tensor is similar to Python list indexing, and NumPy also. 

Let's also select data in 2D tensor.

```python
tensor_2d = tf.constant([[1,3],
                          [3,4],
                          [4,5]])
```

```python
print('The first row:', tensor_2d[0,:].numpy())
print('The second column:', tensor_2d[:,1].numpy())
print('The last low:', tensor_2d[-1,:].numpy())
print('The first value in the last row:', tensor_2d[-1,0].numpy())
print('The last value in the last column:', tensor_2d[-1,-1].numpy())
```

**Execution Output:**
```text
The first row: [1 3]
The second column: [3 4 5]
The last low: [4 5]
The first value in the last row: 4
The last value in the last column: 5
```

<a name='4-6'></a>

### 4. 6 Performing Operations on Tensors

All numeric operations can be performed on tensor. Let's see few of them.

```python
# Creating example tensors 

tensor_1 = tf.constant([1,2,3])
tensor_2 = tf.constant([4,5,6])
```

```python
# Adding a scalar value to a tensor

print(tensor_1 + 4)
```

**Execution Output:**
```text
tf.Tensor([5 6 7], shape=(3,), dtype=int32)
```

```python
# Adding two tensors 

print(tensor_1 + tensor_2)
```

**Execution Output:**
```text
tf.Tensor([5 7 9], shape=(3,), dtype=int32)
```

```python
# Can also add with tf.add() or tf.math.add()

print(tf.add(tensor_1, tensor_2))
```

**Execution Output:**
```text
tf.Tensor([5 7 9], shape=(3,), dtype=int32)
```

```python
# multiplying tensors with tf.multiply()

print(tf.multiply(tensor_1, tensor_2))
```

**Execution Output:**
```text
tf.Tensor([ 4 10 18], shape=(3,), dtype=int32)
```

<a name='4-7'></a>

### 4. 7 Manipulating the Shape of Tensor

There are times you would want to reshape a tensor. Here is how to go about it.

```python
print(example_tensor)
```

**Execution Output:**
```text
tf.Tensor(
[[1 3]
 [3 4]
 [4 5]], shape=(3, 2), dtype=int32)
```

Let's reshape the above tensor into `(2,3)`.

```python
tens_reshaped = tf.reshape(example_tensor, [2,3])
```

```python
print(tens_reshaped)
```

**Execution Output:**
```text
tf.Tensor(
[[1 3 3]
 [4 4 5]], shape=(2, 3), dtype=int32)
```

```python
# Also to (6,1)

print(tf.reshape(example_tensor, [6,1]))
```

**Execution Output:**
```text
tf.Tensor(
[[1]
 [3]
 [3]
 [4]
 [4]
 [5]], shape=(6, 1), dtype=int32)
```

```python
# You can also shape a tensor into a list

print(example_tensor.shape.as_list())
```

**Execution Output:**
```text
[3, 2]
```

```python
# You can also flatten a tensor

print(tf.reshape(example_tensor, [-1]))
```

**Execution Output:**
```text
tf.Tensor([1 3 3 4 4 5], shape=(6,), dtype=int32)
```

There are rules to reshaping a tensor. The new shape has to be resonable. Take an example below, it would create an erroe because there is no way you can reshape the `example_tensor into (5,5).`

```python
# Running the cell below will create an error

# print(tf.reshape(example_tensor, [5,5]))
```

*******************

That's it for the introduction to TensorFlow and the basics of tensors.

## [BACK TO TOP](#0)

---

## 3. Deep Neural Networks for Regression

<a name='0'></a>
# Neural Networks for Regression with TensorFlow

### Contents 

* [1. Intro to Regression with TensorFlow](#1)
* [2. Starting Simple: Fitting a Straight Line](#2)
   * [2.1 Gathering the data](#2-1)
   * [2.2 Looking in the data](#2-2)
   * [2.3 Preparing the data for a model](#2-3)
   * [2.4 Creating, Compiling and Training a model](#2-4)
   * [2.5 Evaluating a model](#2-5)
   * [2.6 Improving a model](#2-6)
  

* [3. Going Beyond: A Real world dataset](#3)
   * [3.1 Gathering the data](#3-1)
   * [3.2 Looking in the data](#3-2)
   * [3.3 Preparing the data for a model](#3-3)
   * [3.4 Creating, Compiling and Training a model](#3-4)
   * [3.5 Evaluating a model](#3-5)
   * [3.6 Improving a model](#3-6)
   * [3.7 Saving a model](#3-7)
   * [3.8 Final notes](#3-8)

<a name='1'></a>
## Intro to Regression with TensorFlow

We know neural networks in taking moonshots but they can also be used for regression problems. 

In regression task/problems, we are interested in predicting the a single or multiple continous numbers. 

Take an example of house price prediction. We can be given the properties/features of the house such as size, region, and number of bedrooms to predict the price of such house. This example is a single number prediction, also termed as `univariate regression`. 

Another example appears in object detection(recognizing & localizing image). In order to localize the object with the bounding box, you have got to find the coordinates of the object's center and the bounding box. The prediction of these coordinates is an example of predicting multiple values at once. It is usually termed as `multivariate regression`.

Any typical architecture for a regression neural network will have common values or ranges of values of **`hyperparameters`** (hyperparameters are all parameters that you as engineer has to set, such as learning rate, number of layers, etc..). 
Let's discuss them. 


#### **Input, hidden, and Output Layers**

The input layer usually has the neurons(or units) equivalent to the number of input features. For example, if our house dataset has 10 variables, 9 input training features, 1 target feature(price of house), then the input neurons will be 9. 

The number of hidden layers depend on the problem and the size of the dataset, but generally, it will be between 1 and 5. Same is true about the number of neurons in each hidden layer, it will depend on the problem & dataset size, but generally, neurons can be between 10 to 100. 

The number of neurons in output layer will depend on the problem. If you are predicting a single number, it will be 1. If you are predicting the coordinates of the object's center and bounding box during object detection, it will be 4 (because there are 4 coordinates, 2 for object's center, 2 for height/width of the box). 


#### **Activation Function**

The choice of activation function depends on the problem, but in most cases, **`relu`** will work well in hidden layers. 

The activation function in the output layer is very specific on the goal of the problem. Unlike neural network classifiers that usually use **`sigmoid`** or **`softmax`**, regressor doesn't need to have an activation since you want the output values as they are. That being said, you may want to prevent the negative values in the output layer. In that case, you can use **`ReLU`**. 


#### Training Loss Function

The loss function used in regression is usually **`Mean Squared Error(MSE)`**. When you are aware that your dataset contain outliers, you can use **`Mean Absolute Error (MAE)`**. MAE can potentialy be used in time series prediction since that type of data tends to have outliers.

Another loss function that is used alot if [Huber loss](https://www.tensorflow.org/api_docs/python/tf/keras/losses/huber). It is combination of both MSE and MAE. 

#### Optimizer

A good rule of thumb when choosing an optimizer is to start with [Adam](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adam). There are other optimizers that you can try, such as SGD(Stockastic Gradient Descent), RMSProp, Nadam, etc...Learn more about them on [TensorFlow optimizer documentation page](https://www.tensorflow.org/api_docs/python/tf/optimizers). 

Below is a summary of hyerparameter best practices in neural network regressors.



| **Hyperparameter** | **Typical value** |
| --- | --- |
| Neurons at input layer | 1 neuron per feature |
| No of hidden layer(s) | depend on problem, start from 1 to 10 |
| Neurons per hidden layer | depend on problem, generally 10 to 100 |
| Neurons at input layer | depend on the desired result, 1 for univariate regression |
| Activation in hidden layers| Relu or its variants(LeakyReLU, SeLU|
| Activation in output layer |None in most cases|
| Loss function | MSE or MAE |
| Optimizer | SGD, Adam, RMSProp |

*Table: Typical values of hyperparameters in neural network regressors*

There are many hyperparameters in neural networks and finding the best values of each and each can be overwhelming. 

When choosing hyperparameters, it is advised to use hyperparameter tuning tools such as [Keras Tuner](https://keras.io/keras_tuner/) to search the best hyperparameters whenever possible. It is nearly impossible to assume that a given value of hyperparamater will work well at first. We usually have to experiment with different values, and a good tool can help you do that quickly. 

Let's put all of the above into practice, starting simple, and later, taking a futher step into real world dataset.

<a name='2'></a>

## 2. Starting Simple: Fitting a Straight Line

One of the simplest things we can model is perhaps a linear equation(it has been proven that [neural networks can model any mathematical function](http://neuralnetworksanddeeplearning.com/chap4.html)). 

So, a linear equation forms a straight line. Its form is **`y=aX+b`** where a is coefficient (or **`weight`**) and b is intercept (or **`bias`**). 

Let's assume that we have this equation **`y=2X+1`** and we are interested in using neural networks to predict y given any value of X. 

But we will start with creating our data based off such equation.

<a name='2-1'></a>
### 2.1  Gathering the data

Let's first import the libraries. I will import `TensorFlow`, `NumPy` and `Matplolib` for plotting the straight line.

```python
import tensorflow as tf
from tensorflow import keras 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
```

After we have imported all relevant libraries, it's time to create our data. We only have one input feature (`X`) and output label `y`. 

We can either create it with `tf.constant()` or `np.array()`. Both will work, but for convenience, let's use `tf.constant()`.

```python
# Create input feature X

X = tf.constant([-2,-1,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,10,12])

# Create label y

y = tf.constant([-3.0,-1.0,1.0,3.0,5.0,7.0,9.0,11.0,13.0,15.0,17.0,21.0,25.0])
```

<a name='2-2'></a>
### 2.2  Looking in the Data

It's always good to look in the data. This can be done in many ways and it depend on the kind of the dataset. If you're working with images, you might want to go through some images and their labels looking if there are no mislabelling. 

In structured data, or data in tabular form, you might have to visualize the distribution of individual features or plot their relationship. 

For us now, we have a simple data. Let's scatter plot X and y.

```python
# Visualizing X and y

plt.plot(X,y) #This will plot a line
plt.scatter(X,y) 
plt.annotate('y=2X+1', xy=(3,4))
plt.xlabel('X')
plt.ylabel('y')
```

**Execution Output:**
```text
Text(0, 0.5, 'y')
```

<a name='2-3'></a>
### 2.3  Preparing data for the model

Usually when working with real world datasets, we need to spend an enourmous amount of time preparing it. The type of things to be done depend on the kind of the dataset, but typically, it can be removing/filling missing values, scaling the features either with normalization or standardization, and so on. 

For now, we can leave our data as it is. In the next labs, we will see some real world datasets that needs extra work before feeding them to the machine learning model.

<a name='2-4'></a>
### 2.4  Creating, Compiling and Training a Model

We are going to create the model having a one layer, one neuron(or unit) and as the input data is a single number, we will set the `input_shape` to `[1]`. 

Later, we will explain everything we did.

```python
model = tf.keras.Sequential([
        keras.layers.Dense(units=1, input_shape=[1])
])
```

And we can see the model summary. Model summary is essential for quick review of the model architecture. As you can see, we only have one dense layer, and 2 parameters(weight and bias).

```python
model.summary()
```

**Execution Output:**
```text
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 1)                 2         
=================================================================
Total params: 2
Trainable params: 2
Non-trainable params: 0
_________________________________________________________________
```

The model that we created is called a  Sequential model. We create it by adding one layer after another. If we had many layers, it would be like a sequence or series of layers, one after another, from the input to the ouput.

After we have created the model, all we have is an empty graphs. We need to do two more things, compiling and training/fitting the model to the presented data.

```python
model.compile(optimizer='sgd', 
              loss='mean_squared_error',
              metrics=['mse'])
```

The single most reason of why we compile the model is to specify the optimizer, loss function and the metrics that we want to track during training. 

During training, loss function will be used to measure the difference between the prediction and the actual output. Such difference is called **`error`**, but we want to measure the **`the mean of squared error`**, hence the name.

**`Error = Actual value – Predicted value`**. 

On the otherhand, optimizer is used to reduce the error between the actual output and predicted value. The optimizer will make continous guesses until the minimum error is reached. There are many optimizers, but for now let's use SGD (Stockastic Gradient Descent). In later labs, we will explore other optimizers. 

By fitting the model to the data, here are what happen:

* The model iterate through each input data point and estimate prediction 
* The difference between the actual and predicted value or error is calculated by loss function
* The error is minimized by optimizer as we go through the data
* The above iteration continue until the number of epochs are reached. 


Let's see that in action, fitting the model to the data, calculating and reducing the error until we make 500 turns.

```python
history = model.fit(X,y, epochs=500)
```

**Execution Output:**
```text
Epoch 1/500
1/1 [==============================] - 1s 583ms/step - loss: 240.2002 - mse: 240.2002
Epoch 2/500
1/1 [==============================] - 0s 7ms/step - loss: 20.7756 - mse: 20.7756
Epoch 3/500
1/1 [==============================] - 0s 7ms/step - loss: 1.9780 - mse: 1.9780
Epoch 4/500
1/1 [==============================] - 0s 10ms/step - loss: 0.3642 - mse: 0.3642
Epoch 5/500
1/1 [==============================] - 0s 12ms/step - loss: 0.2222 - mse: 0.2222
Epoch 6/500
1/1 [==============================] - 0s 8ms/step - loss: 0.2064 - mse: 0.2064
Epoch 7/500
1/1 [==============================] - 0s 8ms/step - loss: 0.2015 - mse: 0.2015
Epoch 8/500
1/1 [==============================] - 0s 8ms/step - loss: 0.1976 - mse: 0.1976
Epoch 9/500
1/1 [==============================] - 0s 11ms/step - loss: 0.1938 - mse: 0.1938
Epoch 10/500
1/1 [==============================] - 0s 5ms/step - loss: 0.1901 - mse: 0.1901
Epoch 11/500
1/1 [==============================] - 0s 7ms/step - loss: 0.1865 - mse: 0.1865
Epoch 12/500
1/1 [==============================] - 0s 6ms/step - loss: 0.1829 - mse: 0.1829
Epoch 13/500
1/1 [==============================] - 0s 10ms/step - loss: 0.1794 - 
... [Output truncated for brevity]
```

As you can see, the loss went from `1.2677e-05` all the way down to `8.5635e-10`. If you run it again, these values may change. There are so many randomness involved in neural network training. Take an example, weights initialization is random.

<a name='2-5'></a>
### 2.5  Evaluating a Model

After we have trained the model, the next step is to evaluate it. 

But first off, we can plot the loss versus the epochs to see how it performed. Plotting the model metrics is a fundamental step in performing the error analysis. 

The training metric `mse` and `loss` are contained in `history.history` and the number of epochs are in `history.epoch`.

```python
loss_df = pd.DataFrame(history.history)

# Plot loss vs epochs

loss_df.plot(figsize=(10,5))
```

There are cowple of things to note from the above graph. 

* First off, the loss and metric we are tracking are all similar. They are both `mean_squared_error` or `mse`.
* The model had no improvement from 80(approx) epochs. This means that 500 epochs was too much, and instead of burning resources or compute power, we would have trained for fewer epochs since the model does not show a significant improvements in the later epochs. 

Training for many epochs beyond what's needed is usually the cause of `overfitting`. We will learn more about overfitting later, but simply, it's when the model is so good on the training set but very poor on the test set or the new data. So, in our case we are forcing the model to fit the data by training it too much. Overfitting can also be caused by using bigger models (for small dataset), etc...


That said, let's make some predictions on unseen data. For simplicity, let's predict `y` of `X=30`. Remember that our equation is `y=2X+1`, so with x=30, y should be equal to `61`.

```python
model.predict([30.0])
```

**Execution Output:**
```text
array([[61.014885]], dtype=float32)
```

Wow! That's so impressive. 

The model was able to determine the relationship between `X` and `y` and can use that relationship to predict `y` for unseen values of `X`. 

One thing to note that it is not guarranted to get the exact predictions, say 61. This is because there are so many randomness and probabilities involved behind the scene. 


One last thing we can try is to get the model parameters, that is weight and bias. And their values should be close to the coeffient and intercept of our linear equation, y=2X+1. 2 is coefficient(or weight), and 1 is the intercept(or bias).

```python
# Getting the model weights

model.get_weights()
```

**Execution Output:**
```text
[array([[2.0006804]], dtype=float32), array([0.994472], dtype=float32)]
```

So, as you can see, the model learned that the relationship between X and y is `y=2.0008771 + 0.9928744` and this is very close to `y=2X+1`. Something intringuing here is that there is no where told the model such relationship - `it simply learned it observing the data that we provided`, and `this is the basis of the idea that machine learning is used to extract patterns in data`. 

With complex data, you might not get such intuition because there will be so many parameters, but in our case, the model was simple, the data was simple, and that allowed us to `uncover` the principal idea behind machine learning - `learning the relationship/pattern between the input features and labels, and using such relationship to make predictions on unseen data.`

<a name='2-6'></a>
### 2.6  Improving the results

Ideally, your model will likely not be good at the first. 

You will need to tweak some hyperparameters, or even improve the data. So, often, all you need is to improve the data than improving the model. There are even state of the art and open source models that you can take an advantages of if you have good data. And in those intances, building model will be out of the equation.  

But of course, improving the model and performing error analysis is not a trivial task and will depend on the results of the model on training and testing set. Here is some ideas that can guide you: 

* If the model is not doing well on the training data, it's a clue that the input data (X) doesn't contain the useful information needed to predict the output y. Or put it simply, the input features do not have `high predictive power`. The right thing to do here is to improve the data. Otherwise, the problem will perssit. 

* If the model is doing well on the training data but poorly on the testing data, it maybe that you overfitted the training data and that resulted in model failing to generalize on test/new data. Overfitting is one thing, there maybe other things not going well or worth improving. The right thing to do here is to plot the learning curve and see what's to be done based off what you are seeing.

Up to now, we have come a long way doing regression with neural networks. We have learned how to create a simple data, how to create, train, and compile a simple model, evaluating the results, and we saw some ideas on perfoming error analysis. 

We started simple with the goal of getting prepared to take a step further into real world scanerios. I wanted to jump quicky to bigger models and computer vision things but I remembered that quite often, it is understanding the basics that can set us off for understanding the bigger picture. 

To make it more exciting, let's not stop on linear equation (we could after all, we did regression already), but let's step into real world dataset, still practicing regression.

<a name='3'></a>

## 3. Going Beyond: A Real world dataset

Welome to the second part of the notebook, where we leap into real world scenarios. 

Still doing regression, we will use the real world forest dataset to predict the burned area of forest fires, in the northeast region of Portugal, by using meteorological and other data.

<a name='3-1'></a>

## 3.1 Loading the data

Before loading the dataset, I will first import all relevant imports.

Here are the information about the attributes: 

1. X - x-axis spatial coordinate within the Montesinho park map: 1 to 9 
2. Y - y-axis spatial coordinate within the Montesinho park map: 2 to 9 
3. month - month of the year: 'jan' to 'dec' 
4. day - day of the week: 'mon' to 'sun' 
5. FFMC - FFMC index from the FWI system: 18.7 to 96.20 
6. DMC - DMC index from the FWI system: 1.1 to 291.3 
7. DC - DC index from the FWI system: 7.9 to 860.6 
8. ISI - ISI index from the FWI system: 0.0 to 56.10 
9. temp - temperature in Celsius degrees: 2.2 to 33.30 
10. RH - relative humidity in %: 15.0 to 100 
11. wind - wind speed in km/h: 0.40 to 9.40 
12. rain - outside rain in mm/m2 : 0.0 to 6.4 
13. area - the burned area of the forest (in ha): 0.00 to 1090.84 

Source: https://archive.ics.uci.edu/ml/datasets/Forest+**Fires

```python
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

Let's download the dataset and load it into a Pandas dataframe using `pd.read_csv()`,

```python
dataset_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv'

forest_df = pd.read_csv(dataset_url)
```

Let's see the features and their data types

```python
forest_df.info()
```

**Execution Output:**
```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 517 entries, 0 to 516
Data columns (total 13 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   X       517 non-null    int64  
 1   Y       517 non-null    int64  
 2   month   517 non-null    object 
 3   day     517 non-null    object 
 4   FFMC    517 non-null    float64
 5   DMC     517 non-null    float64
 6   DC      517 non-null    float64
 7   ISI     517 non-null    float64
 8   temp    517 non-null    float64
 9   RH      517 non-null    int64  
 10  wind    517 non-null    float64
 11  rain    517 non-null    float64
 12  area    517 non-null    float64
dtypes: float64(8), int64(3), object(2)
memory usage: 52.6+ KB
```

The dataset contains 517 examples and 13 columns, 12 features and 1 label (`areas`).

```python
print(forest_df.shape)
```

**Execution Output:**
```text
(517, 13)
```

<a name='3-2'></a>

## 3.2 Looking in the data

We will not go deep into analysis, but let's try to learn about the data we have. Before that, I will first split the dataset into training and test set. 

I will use Scikit-Learn `train_test_split`.

```python
from sklearn.model_selection import train_test_split

train_data, test_data = train_test_split(forest_df, test_size=0.3, random_state=42)
```

```python
print('The shape of training data: {}\nThe shape of testing data: {}'.format(train_data.shape, test_data.shape))
```

**Execution Output:**
```text
The shape of training data: (361, 13)
The shape of testing data: (156, 13)
```

Let's peep into the data.

```python
train_data.head(5)
```

**Execution Output:**
```text
X  Y month  day  FFMC    DMC     DC   ISI  temp  RH  wind  rain   area
311  6  3   sep  sun  92.4  105.8  758.1   9.9  24.8  28   1.8   0.0  14.29
368  6  5   sep  sat  91.2   94.3  744.4   8.4  16.8  47   4.9   0.0  12.64
23   7  4   aug  sat  90.2  110.9  537.4   6.2  19.5  43   5.8   0.0   0.00
271  8  6   aug  tue  92.1  152.6  658.2  14.3  20.1  58   4.5   0.0   9.27
299  6  5   jun  sat  53.4   71.0  233.8   0.4  10.6  90   2.7   0.0   0.00
```

It seems that we have two categorical features, `month` and `day`. We will remember to encode them. For now we can see the number of samples in each month and later in each day.

```python
train_data['month'].value_counts().plot(kind='bar', figsize=(10,5))
```

```python
train_data['day'].value_counts().plot(kind='bar', figsize=(10,5))
```

We can also check the distribution of the area. Area is very skewed, you can see that most values are very close to zero.

```python
sns.kdeplot(data=train_data, x='area', color='red')
```

<a name='3-3'></a>

## 3.3 Preparing the Data for the Model

Here we will do two things, one is to normalize numerical features and the second is to encode categorical features. We can set up a pipeline to handle that. 

For simplicity, we will use Scikit-Learn processing functions. 

I will first separate features and label. We can use a function that can also be applied to test set.

```python
def get_feats_and_labels(data, label):
  """ Take data and label as inputs, return features and labels separated """

  data_feats = data.drop(label, axis=1)
  data_label = data[label]

  return data_feats, data_label
```

Let's use the function created above to get the features and labels.

```python
train_feats, train_label = get_feats_and_labels(train_data, 'area')
```

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder

scaler = StandardScaler()
encoder = OrdinalEncoder()


# The column transformer requires lists of features

num_feats = ['X', 'Y', 'FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH',
       'wind', 'rain']
cat_feats = ['month', 'day']

# define the pipeline to scale the numeric features and handle categorical features
final_pipe = ColumnTransformer([
   ('num',scaler , num_feats),    
   ('cat', encoder , cat_feats)                        

])

training_data_prepared = final_pipe.fit_transform(train_feats)
```

Now, we can see the shape of the transformed dataset. It is a NumPy array.

```python
training_data_prepared.shape
```

**Execution Output:**
```text
(361, 12)
```

```python
type(training_data_prepared)
```

**Execution Output:**
```text
numpy.ndarray
```

Also let's tranform the test set. Note that for the test set, we don't `fit_transform()`. 

I will get the features and labels separated first.

```python
test_feats, test_label = get_feats_and_labels(test_data, 'area')
```

And now we transform the test features.

```python
test_data_prepared = final_pipe.transform(test_feats)
```

Let's convert train and test labels to NumPy array.

```python
train_label = train_label.to_numpy()
test_label = test_label.to_numpy()
```

<a name='3-4'></a>

## 3.4 Creating, Compiling and Training a Model

Now that our data is prepared, it's time to create a neural network regressor. 

Like in the first example, we will use the Sequential API. 

Everytime we are creating a model in TensorFlow, we have to specify the input shape. In this example, the input shape will be:

```python
input_shape = training_data_prepared.shape[1:]
input_shape
```

**Execution Output:**
```text
(12,)
```

```python
model = keras.models.Sequential([
                                 
            # The first layers must specify the input shape always
            keras.layers.Dense(12, activation='relu', input_shape=input_shape),
            keras.layers.Dense(24, activation='relu'),

            # The last layer usually doesn't have activation function in regression
            keras.layers.Dense(1)                

])

# Now we compile the model
model.compile(loss='mean_squared_error', optimizer='adam')
```

Let's see the model summary.

```python
model.summary()
```

**Execution Output:**
```text
Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, 12)                156       
_________________________________________________________________
dense_2 (Dense)              (None, 24)                312       
_________________________________________________________________
dense_3 (Dense)              (None, 1)                 25        
=================================================================
Total params: 493
Trainable params: 493
Non-trainable params: 0
_________________________________________________________________
```

Remember, when the model is created in TensorFlow, it is like an empty graphs. We can even visualize it.

```python
from tensorflow.keras.utils import plot_model

plot_model(model, to_file='model.png')
```

**Execution Output:**
```text
<IPython.core.display.Image object>
```

Before training or fitting the model to the data, a model is nothing other than empty graphs. 

Now let's train the model.

```python
history = model.fit(training_data_prepared, train_label, 
                    validation_data = (test_data_prepared, test_label), epochs=50)
```

**Execution Output:**
```text
Epoch 1/50
12/12 [==============================] - 1s 17ms/step - loss: 2500.8550 - val_loss: 8183.7715
Epoch 2/50
12/12 [==============================] - 0s 3ms/step - loss: 2489.0750 - val_loss: 8166.7290
Epoch 3/50
12/12 [==============================] - 0s 4ms/step - loss: 2480.3232 - val_loss: 8150.3276
Epoch 4/50
12/12 [==============================] - 0s 3ms/step - loss: 2470.4707 - val_loss: 8137.5972
Epoch 5/50
12/12 [==============================] - 0s 4ms/step - loss: 2462.4663 - val_loss: 8124.1401
Epoch 6/50
12/12 [==============================] - 0s 5ms/step - loss: 2453.9116 - val_loss: 8110.1162
Epoch 7/50
12/12 [==============================] - 0s 3ms/step - loss: 2445.4663 - val_loss: 8095.4053
Epoch 8/50
12/12 [==============================] - 0s 6ms/step - loss: 2435.2563 - val_loss: 8077.7803
Epoch 9/50
12/12 [==============================] - 0s 3ms/step - loss: 2426.2720 - val_loss: 8056.7891
Epoch 10/50
12/12 [==============================] - 0s 5ms/step - loss: 2415.6418 - val_loss: 8038.3853
Epoch 11/50
12/12 [==============================] - 0s 4ms/step - loss: 2405.9746 - val_loss: 8021.0791
Epoch 12/50
12/12 [==============================] - 
... [Output truncated for brevity]
```

<a name='3-5'></a>

## 3.5 Evaluating a Model

After we have trained the model, the next step is to evaluate it. 

But first off, we can plot the loss versus the epochs to see how it performed. Plotting the model metrics is a fundamental step in performing the error analysis. 

`loss` and `val_loss` are contained in `history.history` and the number of epochs are in `history.epoch`.

```python
loss_df = pd.DataFrame(history.history)

# Plot loss vs epochs

loss_df.plot(figsize=(10,5))
```

```python
model.evaluate(test_data_prepared, test_label)
```

**Execution Output:**
```text
5/5 [==============================] - 0s 2ms/step - loss: 7934.7148
7934.71484375
```

The results are not impressive. Let's try to think why the model is not doing well. There are some few things to draw from the graph above. 

* Ideally, both validation and training loss should decrease during training. If training doesn't decrease, it's very likely that the input features don't contain enough information to predict the output. 

* Both `loss` and `val_loss` didn't improve alot, and there is no evidence that training for more epochs will improve the results. Quite the opposite, there is evidence that it will not improve.

* How about adding more layers, or neurons? There is a notion that a model is as good as the data it was trained on. In most cases, the sure thing to improve or add more data.

Let's see what we can improve.

<a name='3-6'></a>

## 3.6 Improving the Model

This data is very skewed. The burned area of the forest varies from 0.00 to 1090.84 but it's skewed to ward 0. Take a look at it again below...

```python
sns.kdeplot(data=train_data, x='area', color='red')
```

As the data source suggested, it may make sense to model it with logarithmic loss. Let's use `LogCosh class` that is available in [Keras Regression losses](https://keras.io/api/losses/regression_losses/#logcosh-class). That type of loss function computes the logarithm of the hyperbolic cosine of the prediction error.

Also, as the most values of the target label `area` falls between 0 and 1, we can use the `sigmoid` activation function so that the output of the network doesn't swing above such range.

```python
model_2 = keras.models.Sequential([
                                 
            # The first layers must specify the input shape always
            keras.layers.Dense(12, activation='relu', input_shape=input_shape),
            keras.layers.Dense(6, activation='relu'),

            # The last layer usually doesn't have activation function in regression
            keras.layers.Dense(1, activation='sigmoid')                

])

# Now we compile the model
model_2.compile(loss='log_cosh', optimizer='adam')
```

```python
history = model_2.fit(training_data_prepared, train_label, 
                    validation_data = (test_data_prepared, test_label), epochs=50)
```

**Execution Output:**
```text
Epoch 1/50
12/12 [==============================] - 1s 13ms/step - loss: 11.5257 - val_loss: 14.5699
Epoch 2/50
12/12 [==============================] - 0s 3ms/step - loss: 11.5059 - val_loss: 14.5482
Epoch 3/50
12/12 [==============================] - 0s 4ms/step - loss: 11.4805 - val_loss: 14.5220
Epoch 4/50
12/12 [==============================] - 0s 5ms/step - loss: 11.4523 - val_loss: 14.4939
Epoch 5/50
12/12 [==============================] - 0s 5ms/step - loss: 11.4251 - val_loss: 14.4703
Epoch 6/50
12/12 [==============================] - 0s 5ms/step - loss: 11.4017 - val_loss: 14.4518
Epoch 7/50
12/12 [==============================] - 0s 5ms/step - loss: 11.3838 - val_loss: 14.4395
Epoch 8/50
12/12 [==============================] - 0s 3ms/step - loss: 11.3710 - val_loss: 14.4299
Epoch 9/50
12/12 [==============================] - 0s 5ms/step - loss: 11.3635 - val_loss: 14.4229
Epoch 10/50
12/12 [==============================] - 0s 5ms/step - loss: 11.3571 - val_loss: 14.4192
Epoch 11/50
12/12 [==============================] - 0s 3ms/step - loss: 11.3530 - val_loss: 14.4164
Epoch 12/50
12/12 [==============================] - 0s 5ms/step - loss: 11.3500 - val_loss: 14.4
... [Output truncated for brevity]
```

```python
loss_df = pd.DataFrame(history.history)

# Plot loss vs epochs

loss_df.plot(figsize=(10,5))
```

```python
model.evaluate(test_data_prepared, test_label)
```

**Execution Output:**
```text
5/5 [==============================] - 0s 3ms/step - loss: 18.7532
18.75318717956543
```

<a name='3-7'></a>

## 3.7 Saving and Loading a model

If something went well, from training to evaluating to improving a model, you would want to save it. 

Here is how to save a model and how to load a saved model. The model will be saved in HDF5 `format`. When the model is saved in such format, the whole model things are saved.

```python
model.save('forest_model.h5')
```

And loading the model is simple too...

```python
loaded_model = keras.models.load_model('forest_model.h5')
```

You can make predictions on a loaded model.

<a name='3-8'></a>

## 3.8 Final Notes

It has been a quite long journey, from fitting a straight line to building a neural network for a real world dataset. 

Ideally, for all datasets we used, neural networks would not be a suitable model. But because we are learning, it makes sense to start simple for the sake of understanding the latter.

## [BACK TO TOP](#0)

---

## 4. Deep Neural Networks for Binary & Multi-Class Classification

<a name='0'></a>
# Neural Networks for Classification with TensorFlow

### Contents 

* [1. Intro to Classification with TensorFlow](#1)
* [2. Getting Started: Binary Classification](#2)
   * [2.1 Gathering Data](#2-1)
   * [2.2 Looking in the Data](#2-2)
   * [2.3 Preparing the data for a Model](#2-3)
   * [2.4 Creating, Compiling and Training a Model](#2-4)
   * [2.5 Visualizing the Model Results](#2-5)
   * [2.6 Evaluating the Model](#2-6)
   
* [3. Going Beyond Binary Classifier to Multiclass Classifier: 10 Fashions Classifier](#3)
   * [3.1 Gathering the Data](#3-1)
   * [3.2 Looking in the Data](#3-2)
   * [3.3 Preparing the data for a Model](#3-3)
   * [3.4 Creating, Compiling and Training a Model](#3-4)
   * [3.5 Visualizing the Model Resuts](#3-5)
   * [3.6 Evaluating a Model](#3-6)
   * [3.7 Controlling Training with CallBacks](#3-7)
   * [3.8 Using TensorBoard for Model Visualization](#3-8)

<a name='1'></a>
## 1. Intro to Classification with TensorFlow

Neural networks can also be used for classification problems. In classification, we are mainly predicting the class or categories. 

There are two three types of classification problems: 

* **Binary classification**: For this classification type, we have two classes. Example might be to classify a given tweet as positive or negative depending on its content. 

In binary classification, you only need a single output neuron with a logistic activation function(or sigmoid) that output a number between 0 and 1. A threshold value (by default, 0.5) can be used to differentiate positive and negative classes. Take an example, if the value of the output neuron is 0.7 (which is greater than 0.5), the tweet can be predicted as positive. Else if the the ouput is 0.4(less than 0.5), the predicted class is negative. 

The common loss/cost function used in binary classification is `binary cross entropy`. 


* **Multilabel binary classification**: A good example of this classification type is if you wanted to classify a tweet as sarcastic or not, but also simultaneously predict if its content is techy or not. This is just an example.  
Same as binary classification, the output neurons won't be 1, but it will have a logistic activation function(`sigmoid`). In the example above, the output neurons will be two. One neuron for sarcastic/not, and other for techy/not. While the sum of the probability of positive and negative classes will be 1 in binary classification, in multilabel classification, the outputs won't necessarily add up to 1 because we have more than two neurons. In the given example, the sum of the output neuron's values will be 2. 

The common loss/cost function used in multilabel binary classification is `binary cross entropy`. 

* **Multiclass classification**: For this classification type, we have more than two classes. 

The output neurons are equivalent to the number of classes. Take an example. If we are building a system that can classify 10 different fashions, we will have 10 output neurons activated by the `softmax` function. By using `softmax` function, the output will be a vector whose dimension is equivalent to the number of classes. And one thing I like about softmax, is that instead of getting the probabilities in such output vector, we get an an actual classes (0 or 1). Take an example: if the predicted fashion is a bag, and its position in classes is 3, the output will look like this: [0,0,0,1,0,0,0,0,0,0]. In simple words, the predicted class will be 1, and everything else will be 0. 

The common loss/cost function used in multiclass classification is `categorical cross entropy`.

In both of those classification types, the number of input neurons, the activation functions in the hidden layers, and the number of hidden layers depend on the problem you're solving. 

Below is a summary of hyerparameter best practices in neural network classifiers.



| **Hyperparameter** | **Binary classifier** | **Multilabel binary classifier** | **Multiclass classifier** |
| --- | --- | --- |--- |
| **Neurons at input layer** | depend on the problem |depend on the problem|depend on the problem
| **No of hidden layer(s)** | depend on problem, usually from 1-10 |Same as ◁|Same as ◁
| **Neurons per hidden layer** | depend on problem, usually 10-100|Same as ◁ |Same as ◁
| **Neurons at output layer** | 1 |Neurons equivalent to number of labels |Neurons equivalent to number of classes
| **Activation in hidden layers**|Mostly Relu or its variants(LeakyReLU, SeLU| Same as ◁ | Same as ◁
| **Activation in output layer** |sigmoid | sigmoid | softmax
| **Loss function** |binary cross entropy |binary cross entropy | categorical cross entropy
| **Optimizer** | Mostly: SGD, Adam, RMSProp|Same as ◁|Same as ◁ Same as ◁|

*Table: Typical values of hyperparameters in neural network classifiers*

There are many hyperparameters in neural networks and finding the best values of each and each can be overwhelming. 

In later notebooks, we will use [Keras Tuner](https://keras.io/keras_tuner/) to search the best hyperparameters whenever possible. It is nearly impossible to assume that a given value of hyperparamater will work well at first. We usually have to experiment with different values. 

Let's put all of the above into practice.

<a name='2'></a>

## 2. Getting Started: Binary Classifier

We will first practice building neural networks for binary classifier. In binary classification, we have two classes. 

We will use a classical cancer dataset to predict if a given patient has a malignant or benign based on their medical information. We will get it from sklearn datasets. 

The dataset contains two labels: malignant, benign.

<a name='2-1'></a>

### 2.1 Getting the data

We will get the data from sklearn datasets.

```python
import numpy as np
import pandas as pd
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras
```

```python
from sklearn.datasets import load_breast_cancer
```

```python
data = load_breast_cancer()
```

```python
# the dataset contain the following features

list(data.feature_names)
```

**Execution Output:**
```text
['mean radius',
 'mean texture',
 'mean perimeter',
 'mean area',
 'mean smoothness',
 'mean compactness',
 'mean concavity',
 'mean concave points',
 'mean symmetry',
 'mean fractal dimension',
 'radius error',
 'texture error',
 'perimeter error',
 'area error',
 'smoothness error',
 'compactness error',
 'concavity error',
 'concave points error',
 'symmetry error',
 'fractal dimension error',
 'worst radius',
 'worst texture',
 'worst perimeter',
 'worst area',
 'worst smoothness',
 'worst compactness',
 'worst concavity',
 'worst concave points',
 'worst symmetry',
 'worst fractal dimension']
```

```python
# the dataset contain the following labels

data.target_names
```

**Execution Output:**
```text
array(['malignant', 'benign'], dtype='<U9')
```

```python
# Getting features and labels 

X = data.data
y = data.target
```

```python
# the features and labels are numpy array 

type(X)
```

**Execution Output:**
```text
numpy.ndarray
```

```python
# To quickly look in data we can get the dataframe from X

data_df = pd.DataFrame(X, columns=data.feature_names)
```

<a name='2-2'></a>

## 2.2 Taking a look in the data

```python
# Looking from the head 

data_df.head()
```

**Execution Output:**
```text
mean radius  mean texture  ...  worst symmetry  worst fractal dimension
0        17.99         10.38  ...          0.4601                  0.11890
1        20.57         17.77  ...          0.2750                  0.08902
2        19.69         21.25  ...          0.3613                  0.08758
3        11.42         20.38  ...          0.6638                  0.17300
4        20.29         14.34  ...          0.2364                  0.07678

[5 rows x 30 columns]
```

```python
# Getting the basic information

data_df.info()
```

**Execution Output:**
```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 569 entries, 0 to 568
Data columns (total 30 columns):
 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   mean radius              569 non-null    float64
 1   mean texture             569 non-null    float64
 2   mean perimeter           569 non-null    float64
 3   mean area                569 non-null    float64
 4   mean smoothness          569 non-null    float64
 5   mean compactness         569 non-null    float64
 6   mean concavity           569 non-null    float64
 7   mean concave points      569 non-null    float64
 8   mean symmetry            569 non-null    float64
 9   mean fractal dimension   569 non-null    float64
 10  radius error             569 non-null    float64
 11  texture error            569 non-null    float64
 12  perimeter error          569 non-null    float64
 13  area error               569 non-null    float64
 14  smoothness error         569 non-null    float64
 15  compactness error        569 non-null    float64
 16  concavity error          569 non-null    float64
 17  concave points error     569 non-null    float64
 18  symmetry e
... [Output truncated for brevity]
```

```python
# Getting the basic stats

data_df.describe().transpose()
```

**Execution Output:**
```text
count        mean  ...          75%         max
mean radius              569.0   14.127292  ...    15.780000    28.11000
mean texture             569.0   19.289649  ...    21.800000    39.28000
mean perimeter           569.0   91.969033  ...   104.100000   188.50000
mean area                569.0  654.889104  ...   782.700000  2501.00000
mean smoothness          569.0    0.096360  ...     0.105300     0.16340
mean compactness         569.0    0.104341  ...     0.130400     0.34540
mean concavity           569.0    0.088799  ...     0.130700     0.42680
mean concave points      569.0    0.048919  ...     0.074000     0.20120
mean symmetry            569.0    0.181162  ...     0.195700     0.30400
mean fractal dimension   569.0    0.062798  ...     0.066120     0.09744
radius error             569.0    0.405172  ...     0.478900     2.87300
texture error            569.0    1.216853  ...     1.474000     4.88500
perimeter error          569.0    2.866059  ...     3.357000    21.98000
area error               569.0   40.337079  ...    45.190000   542.20000
smoothness error         569.0    0.007041  ...     0.008146     0.03113
compactness error        569.0    0.025478  ...     0.032
... [Output truncated for brevity]
```

<a name='2-3'></a>

## 2.3 Preparing the Data

The data from sklearn is reasonably cleaned. Let's split the data into train and test sets, and we will follow with scaling the values to be between 0 and 1.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, shuffle=True, random_state=42)
```

After splitting the data into training and testing sets, let's see the number of examples in each set.

```python
print('The number of training samples: {}\nThe number of testing samples: {}'.format(X_train.shape[0], X_test.shape[0]))
```

**Execution Output:**
```text
The number of training samples: 455
The number of testing samples: 114
```

```python
# Scaling the features to be between 0 and 1.

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_train_scaled = scaler.fit_transform(X_train)
```

Let's also scale the test set. We do not fit the scaler on the test set. We only transform it.

```python
X_test_scaled = scaler.transform(X_test)
```

We are now ready to create, compile and train the model.

<a name='2-4'></a>

## 2.4 Creating, Compiling and Training a Model

In TensorFlow, creating a model is only putting together an empty graphs. We are going to use Sequential API to stack the layers, from the input to output. 

In model compilaton, it's where we specify the `optimizer` and `loss` function. Loss function is there for calculating the difference between the predictions and the actual output, and optimizer is there for reducing the loss. 

Also, if we are interested in tracking other metrics during training, we can specify them in `metric`.

```python
# Creating a model 

# Getting the input shape

input_shape = X_train_scaled.shape[1:]

model_1 = tf.keras.models.Sequential([
                                      
              # The first layer has 30 neurons(or units)                    
              tf.keras.layers.Dense(units=30, input_shape=input_shape, activation='relu'),

              # The second layer has 25 neurons 

              tf.keras.layers.Dense(units=15, activation='relu'),

              # The third layer has 1 neuron and activation of sigmoid. 
              # Because of sigmoid, the output of this layer will be a value bwteen 0 and 1
              tf.keras.layers.Dense(1, activation='sigmoid')                     
]) 

# Compiling the model 

model_1.compile(optimizer='sgd',
              loss='binary_crossentropy',
              metrics='accuracy')
```

After the model is created and compiled, it's time to teach it. It's time to train it on the data.

```python
# By setting validation_split=0.15, I am allocating 15% of the dataset to be used for evaluating the model during the training
# Model training returns model history(accuracy, loss, epochs...) 

history = model_1.fit(X_train_scaled, y_train, epochs=60, validation_split=0.15)
```

**Execution Output:**
```text
Epoch 1/60
13/13 [==============================] - 1s 35ms/step - loss: 0.7219 - accuracy: 0.3705 - val_loss: 0.7088 - val_accuracy: 0.4928
Epoch 2/60
13/13 [==============================] - 0s 5ms/step - loss: 0.7113 - accuracy: 0.4793 - val_loss: 0.7006 - val_accuracy: 0.5362
Epoch 3/60
13/13 [==============================] - 0s 5ms/step - loss: 0.7019 - accuracy: 0.5259 - val_loss: 0.6937 - val_accuracy: 0.5362
Epoch 4/60
13/13 [==============================] - 0s 5ms/step - loss: 0.6942 - accuracy: 0.5855 - val_loss: 0.6871 - val_accuracy: 0.5942
Epoch 5/60
13/13 [==============================] - 0s 5ms/step - loss: 0.6871 - accuracy: 0.6606 - val_loss: 0.6801 - val_accuracy: 0.7101
Epoch 6/60
13/13 [==============================] - 0s 5ms/step - loss: 0.6798 - accuracy: 0.7202 - val_loss: 0.6735 - val_accuracy: 0.7536
Epoch 7/60
13/13 [==============================] - 0s 5ms/step - loss: 0.6728 - accuracy: 0.7565 - val_loss: 0.6675 - val_accuracy: 0.7971
Epoch 8/60
13/13 [==============================] - 0s 6ms/step - loss: 0.6662 - accuracy: 0.7798 - val_loss: 0.6610 - val_accuracy: 0.7971
Epoch 9/60
13/13 [==============================] - 0s 5ms/step - loss: 0.6595 
... [Output truncated for brevity]
```

I trained for 60 epochs. That was quick. 

Let's visualize accuracy and loss to actually see how the model did. It is always easy to notice performance on graph than looking on models training progress above. 

‼️ If you retrain again, it will continue where it left. So, for example, if you train for 30 epochs, and you rerun the cell, it will train for same more epochs again.

<a name='2-5'></a>

## 2.5 Visualizing the Results

Visualizing the model results after training is always a good way to learn what you can do to improve the performance. 

Let's get a Pandas dataframe containing training loss and accuracy, and validation loss and accuracy.

```python
# Getting the dataframe of loss and accuracies on both training and validation

loss_acc_metrics_df = pd.DataFrame(history.history)
loss_acc_metrics_df.plot(figsize=(10,5))
```

This is really impressive. Seems that for only 60 epochs, the training accuracy was up to 90% while validation accuracy was 84%. 

This is not bad considering that we have only 455 training samples, and also 15% of such samples are allocated to the validation set. The validation accuracy can be increased by increaing the validation samples. 

Let's evaluate the model on the test set.

<a name='2-6'></a>

## 2.6 Evaluating the Model

Quite often, you will want to test your model on the data that it never saw. This data is normally called `test set` and in more applied practice, you will only feed the test to the model after you have done your best to improve it. 

Let's now evaluate the model on the test set. One thing to note here is that the test set must be preprocessed the same way we preprocessed the training set. The training set was rescaled (with `MinMaxScaler`) and that was applied to the test set. 

If this is not obeyed, you would not know why you're having poor results. Just look up on the next next cell how poor the accuracy will be if I evaluate the model on unscaled data when I trained it on scaled data.

```python
# Evaluating a model on unseen data: test set

model_eval = model_1.evaluate(X_test_scaled, y_test)

# Printing the loss and accuracy 

print('Test loss: {}\nTest accuracy:{}'.format(model_eval[0],model_eval[1]))
```

**Execution Output:**
```text
4/4 [==============================] - 0s 4ms/step - loss: 0.3146 - accuracy: 0.9298
Test loss: 0.3145657181739807
Test accuracy:0.9298245906829834
```

```python
# ‼DON'T DO THIS!! X_test is not scaled. The results will be awful

model_1.evaluate(X_test, y_test)
```

**Execution Output:**
```text
4/4 [==============================] - 0s 4ms/step - loss: 327.3092 - accuracy: 0.3772
[327.3092346191406, 0.37719297409057617]
```

It's very suprising how the model did on the test data. It achieved 93%. 

Accuracy is one classification metric, but there are more metrics such as f1 score, recall, and precision. The easiest way to get these metrics is to use `classification_report` function provided by Scikit-Learn. 

Sometime you would also want to know how your model did on the both positive and negative examples.  In this case you can use confusion matrix to see the predicted and the actual classes.

```python
# Getting the prediction

predictions = model_1.predict(X_test_scaled)
```

```python
predictions[:15]
```

**Execution Output:**
```text
array([[0.68703896],
       [0.19852844],
       [0.37471318],
       [0.78504544],
       [0.8081874 ],
       [0.03121866],
       [0.04509011],
       [0.37985504],
       [0.48416775],
       [0.73546237],
       [0.75935453],
       [0.40290105],
       [0.71097237],
       [0.5158887 ],
       [0.7241085 ]], dtype=float32)
```

If you look at the predictions above, they are probabilities (value between 0 and 1). 

And this make sense because our model is returning the values between 0 and 1 because of the [`sigmoid activation function or logistic function`](https://www.tensorflow.org/api_docs/python/tf/math/sigmoid) at the output layer. 

In order to find the metrics we noted above, we have to round the predictions to either 0 or 1. For this, we can use [`np.round()`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.round.html#numpy.ndarray.round) or [`tf.math.round()`](https://www.tensorflow.org/api_docs/python/tf/math/round). 

Round function will return the closest integer. For example, for a prediction of 0.3, it will be 0. If the prediction is 0.6, the closest integer is 1.

```python
# Rounding the predictions to 0 and 1

predictions = tf.round(predictions)
```

```python
# Display the first 15 preds values 
 
predictions[:15]
```

**Execution Output:**
```text
<tf.Tensor: shape=(15, 1), dtype=float32, numpy=
array([[1.],
       [0.],
       [0.],
       [1.],
       [1.],
       [0.],
       [0.],
       [0.],
       [0.],
       [1.],
       [1.],
       [0.],
       [1.],
       [1.],
       [1.]], dtype=float32)>
```

Great, the predictions are now rounded up to either 0 or 1.

```python
# Getting the confusion matrix

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, predictions)

# Plotting confusion matrix 

plt.figure(figsize=(6,6))
sns.heatmap(cm, square=True, annot=True, fmt='d', cbar=True,
                        xticklabels=['0: Malignant', '1:Benign'],
                        yticklabels=['0: Malignant', '1:Benign'])
plt.ylabel('Actual label')
plt.xlabel('Predicted label');
```

Let's interpret the confusion matrix:

First off, the rows represent the actual classes and the columns represent the predicted classes. 

With that said:

* *36 Malignant samples were correctly classified as Malignant. Also called True Positives*
* *7 Malignant samples were incorrectly classified as Benign.  Also called False Positives*
* *0 Benign samples were incorrectly classified as Malignant.  Also called False Negatives*
* 71 *Benign samples were correctly classified as Benign.  Also called True Negatives*

```python
# Classification report: F1 score, Recall, Precision

from sklearn.metrics import classification_report

print(classification_report(y_test, predictions))
```

**Execution Output:**
```text
precision    recall  f1-score   support

           0       0.95      0.86      0.90        43
           1       0.92      0.97      0.95        71

    accuracy                           0.93       114
   macro avg       0.93      0.92      0.92       114
weighted avg       0.93      0.93      0.93       114
```

Here are notes about these metrics:

* **Accuracy** is the ratio of the correct predicted samples over the total samples.
* **Precision** is the ratio of correct predicted positive samples over the total positive predictions.
* **Recall** is the ration of correct predicted positive samples over total positive samples.

* **F1 score** is the harmonic mean of precision and recall.

<a name='3'></a>

## 3. Going Beyond Binary Classifier to Multiclass Classifier: 10 Fashions Classifier

So far, we have built a neural network for regression(in previous labs) and binary classification. And we have only been working with structured datasets(datasets in tabular format). 

Can the same neural networks we used be able to recognize images? In this next practice, we will turn the page to image classification. We will build a neural network for recognizing 10 different fashions and along the way, we will learn other things such as stopping the training upon a given condition is met, and using TensorBoard to visualize model.

<a name='3-1'></a>

## 3.1 Getting the Fashion data

Fashion MNIST data is made of 70.000 fashions, 60.000 of them are allocated for training set and 10.000 for test set. Each image is 28*28, grayscale. 


!['Fashion Dataset'](https://github.com/zalandoresearch/fashion-mnist/raw/master/doc/img/fashion-mnist-sprite.png)


!['Embedding: Fashion Dataset'](https://github.com/zalandoresearch/fashion-mnist/raw/master/doc/img/embedding.gif)

The fashions are of 10 categories. Below are their labels: 


| Label | Description |
| --- | --- |
| 0 | T-shirt/top |
| 1 | Trouser |
| 2 | Pullover |
| 3 | Dress |
| 4 | Coat |
| 5 | Sandal |
| 6 | Shirt |
| 7 | Sneaker |
| 8 | Bag |
| 9 | Ankle boot |

Let's get the dataset from Keras.

```python
import tensorflow as tf

fashion_mnist = tf.keras.datasets.fashion_mnist

(fashion_train, fashion_train_label), (fashion_test, fashion_test_label) = fashion_mnist.load_data()
```

<a name='3-2'></a>

## Looking in the Fashion Data

As always, it is a best practice to peep into the images to see how they like. 

Let's display the pixels values of a given image, image, and its corresponding label.

```python
index = 10

# Get the pixels

fashion_train[index]
```

**Execution Output:**
```text
array([[  0,   0,   0,   0,   0,   0,   0,  11, 142, 200, 106,   0,   0,
          0,   0,   0,   0,   0,  85, 185, 112,   0,   0,   0,   0,   0,
          0,   0],
       [  0,   0,   0,   0,   0,   0, 152, 214, 217, 194, 236, 216, 187,
        149, 135, 153, 211, 217, 231, 205, 217, 188,  34,   0,   0,   0,
          0,   0],
       [  0,   0,   0,   0,   0,  66, 185, 166, 180, 181, 190, 211, 221,
        197, 146, 198, 206, 191, 168, 190, 172, 188, 175,   0,   0,   0,
          0,   0],
       [  0,   0,   0,   0,   0, 135, 153, 160, 175, 180, 170, 186, 187,
        190, 188, 190, 187, 174, 195, 185, 174, 161, 175,  59,   0,   0,
          0,   0],
       [  0,   0,   0,   0,   0, 161, 147, 160, 170, 178, 177, 180, 168,
        173, 174, 171, 185, 184, 185, 172, 171, 164, 174, 120,   0,   0,
          0,   0],
       [  0,   0,   0,   0,   2, 175, 146, 145, 168, 178, 181, 185, 180,
        184, 178, 179, 187, 191, 193, 190, 181, 171, 172, 158,   0,   0,
          0,   0],
       [  0,   0,   0,   0,  35, 177, 155, 140, 151, 172, 191, 187, 186,
        187, 186, 187, 182, 191, 194, 188, 180, 161, 161, 185,   0,   0,
          0,   0],
       [  0,   0,   0,   0,  59, 170, 153, 14
... [Output truncated for brevity]
```

```python
# A list of label names

class_names = ['T-shirt/top', 'Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']
```

```python
# Show the image

plt.imshow(fashion_train[index])

# Display the label

image_label = fashion_train_label[index]
print('This type of fashion is: {}({})'.format(class_names[image_label], image_label))
```

**Execution Output:**
```text
This type of fashion is: T-shirt/top(0)
```

The fashions with the label 0 is `T-shirt/top`. Normally, the pixels of image range from 0 to 255. If you can look back where we displayed the pixels, you will see that they vary from 0 to 255.

We can also visualize some random images.

```python
import random

plt.figure(figsize=(6,6))

for index in range(6):

  ax = plt.subplot(2,3, index+1)
  random_index = random.choice(range(len(fashion_train)))
  plt.imshow(fashion_train[random_index])
  plt.title(class_names[fashion_train_label[random_index]])
```

You can rerun the above cell to display different fashions.

Another important thing to look at when working with images is to see their size. 

This is important because later when we will be creating a model, we have to specify the input shape and such shape is same as the shape of the images. Each image is 28*28, but let's verify that.

```python
# Getting the image shape

print('The shape of the whole training dataset:{}'.format(fashion_train[0].shape))
print('The shape of the first(and other)image:{}'.format(fashion_train[0].shape))
```

**Execution Output:**
```text
The shape of the whole training dataset:(28, 28)
The shape of the first(and other)image:(28, 28)
```

Now that we know the dataset that we are working with, let us do some few proprocessing before building a model.

<a name='3-3'></a>

## 3.3 Preparing the Data

In many cases, real world images datasets are not that clean like fashion mnist. 

You may have to correct images that were incorrectly labeled, or you have labels in texts that need to be converted to numbers(most machine learning models accept numeric input), or scale the pixels values. 

The latter is what we are going to do. It is inarguable that scaling the images pixels to value between 0 and 1 increase the performance of the neural network, and hence the results. Let's do it!! 

As we have seen, the pixels range from 0 to 255. So we will divide both training and test set by 255.0.

```python
# Scaling the image pixels to be between 0 and 1

fashion_train = fashion_train/255.0

fashion_test = fashion_test/255.0
```

We are now ready to build a neural network.

<a name='3-4'></a>

## 3.4 Creating, Compiling, and Training a Model

There are few points to note before creating a model:

* When working with images, the shape of the input images has to be correctly provided. This is a common error done by many people, including me (before I learned it). 

* This is a multiclass classification, which is different to the binary classifier we did earlier. The difference will be reflected in the choice of output activation function, number of output neurons, and the loss function. 

* That said, we will use `softmax` as activation in the last layer, 10 neurons or units because we have 10 fashions, and the loss will be  `SparseCategoricalCrossentropy` because the labels are pure integer. If the labels were in one hot format, we would use `CategoricalCrossentropy`. 

Documentation is always the top source when learning all the possibilities of any framework. And also, Keras doc is beautifuly organized. Not to mention that the keras API is also well designed as well. 

Let's now create a model.

```python
# Creating a model

fashion_classifier = tf.keras.models.Sequential([
                                                 
        # Flattening layer will convert array of pixels into one dimensional column array                                        
       tf.keras.layers.Flatten(),
       tf.keras.layers.Dense(units=64, activation='relu'),
       tf.keras.layers.Dense(units=32, activation='relu'),
       tf.keras.layers.Dense(units=10, activation='softmax')                           

])

# Compiling a model: Specifying a loss and optimization function

fashion_classifier.compile(optimizer='adam',
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy']
                           
)
```

Now that we built and compiled a model, we can train it. 

In order to train a model, we must have an input data and output(labels). We train the model to get the relationship between the input and output. Such relationship is what we tend to call rules. So, in other words, we provide the data and the answers to a model to get the rules.

```python
# Training a model
# Allocating 15% of training data to validation set

fashion_classifier.fit(fashion_train, fashion_train_label, epochs=20, validation_split=0.15)
```

**Execution Output:**
```text
Epoch 1/20
1594/1594 [==============================] - 6s 3ms/step - loss: 0.5368 - accuracy: 0.8105 - val_loss: 0.4270 - val_accuracy: 0.8456
Epoch 2/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3994 - accuracy: 0.8576 - val_loss: 0.3924 - val_accuracy: 0.8610
Epoch 3/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3631 - accuracy: 0.8678 - val_loss: 0.3694 - val_accuracy: 0.8654
Epoch 4/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3387 - accuracy: 0.8765 - val_loss: 0.3942 - val_accuracy: 0.8583
Epoch 5/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3190 - accuracy: 0.8827 - val_loss: 0.3612 - val_accuracy: 0.8720
Epoch 6/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3068 - accuracy: 0.8861 - val_loss: 0.3365 - val_accuracy: 0.8770
Epoch 7/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.2916 - accuracy: 0.8922 - val_loss: 0.3551 - val_accuracy: 0.8750
Epoch 8/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.2814 - accuracy: 0.8968 - val_loss: 0.3471 - val_accuracy: 0.8734
Epoch 9/20
1594/1594 [==========================
... [Output truncated for brevity]
```

<a name='3-5'></a>

## 3.5 Visualizing the Model Results

Let's visualize the model results to see how training went.

```python
# Getting the dataframe of loss and accuracies on both training and validation

loss_acc_metrics_df = pd.DataFrame(fashion_classifier.history.history)

# Plotting the loss and accuracy

loss_acc_metrics_df.plot(figsize=(10,5))
```

At the end of the training, the accuracy is about 92% while validation accuracy being 88% or so. That's not bad considering that we built a simple model and trained for only 20 epochs. 

Let's see how the model performs on unseed data: test set.

<a name='3-6'></a>

## 3.6 Model Evaluation

```python
# Evaluating the model on unseen data

eval = fashion_classifier.evaluate(fashion_test, fashion_test_label)

# Printing the loss and accuracy 

print('Test loss: {}\nTest accuracy:{}'.format(eval[0],eval[1]))
```

**Execution Output:**
```text
313/313 [==============================] - 1s 2ms/step - loss: 0.3724 - accuracy: 0.8799
Test loss: 0.3724398612976074
Test accuracy:0.8798999786376953
```

The fashion classifier that we built is 88% confident at recognizing unseen fashion. 

We could also find other Classification metrics based on True/False positives & negatives such as precision, recall, but since we already saw how to compute them in the binary classifier, let's see other interesting things: Controlling the training using [callbacks](https://keras.io/api/callbacks/) and using [TensorBoard](https://www.tensorflow.org/tensorboard).

<a name='3-7'></a>

## 3.7 Controlling Training with Callbacks

We can use Callbacks functions to control the training. 

Take an example: we can stop training when the model is lo longer showing significant improvements on validation set. Or we can terminate training when a certain condition is met.

### Implementing Callbacks

There are various functionalities available in Keras Callbacks. 

Let's start with how to use `ModelCheckpoint` to save the model when the performance on the validation set is best so far. By saving the best model on the validation set, we avoid things like overfitting which is a common issue in machine learning model training, neural network specifically. We also train for less time. 

I will rebuild a same model again.

```python
# Creating a same model as used before

def classifier():

  model = tf.keras.models.Sequential([
                                                 
        # Flattening layer will convert array of pixels into one dimensional column array                                        
       tf.keras.layers.Flatten(),
       tf.keras.layers.Dense(units=64, activation='relu'),
       tf.keras.layers.Dense(units=32, activation='relu'),
       tf.keras.layers.Dense(units=10, activation='softmax')                           

  ])

# Compiling a model: Specifying a loss and optimization function

  model.compile(optimizer='adam',
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy']
                           
  )

  return model
```

```python
# Defining callbacks 

from keras.callbacks import ModelCheckpoint

callbacks = ModelCheckpoint('fashion_classifier.h5', save_best_only=True)
```

The `callbacks` defined above is passed into the model fit.

```python
# Controlling training with callbacks

# Get the model

fashion_classifier_2 = classifier()

fashion_classifier_2.fit(fashion_train, fashion_train_label, epochs=20, validation_split=0.15, callbacks=[callbacks])
```

**Execution Output:**
```text
Epoch 1/20
1594/1594 [==============================] - 6s 3ms/step - loss: 0.5474 - accuracy: 0.8101 - val_loss: 0.4271 - val_accuracy: 0.8476
Epoch 2/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.4015 - accuracy: 0.8573 - val_loss: 0.4191 - val_accuracy: 0.8470
Epoch 3/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3643 - accuracy: 0.8689 - val_loss: 0.3805 - val_accuracy: 0.8650
Epoch 4/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3396 - accuracy: 0.8761 - val_loss: 0.3639 - val_accuracy: 0.8667
Epoch 5/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3177 - accuracy: 0.8834 - val_loss: 0.3656 - val_accuracy: 0.8678
Epoch 6/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3048 - accuracy: 0.8870 - val_loss: 0.3419 - val_accuracy: 0.8746
Epoch 7/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.2910 - accuracy: 0.8931 - val_loss: 0.3551 - val_accuracy: 0.8748
Epoch 8/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.2818 - accuracy: 0.8949 - val_loss: 0.3306 - val_accuracy: 0.8814
Epoch 9/20
1594/1594 [==========================
... [Output truncated for brevity]
```

If you look below, the model was saved and the version that is saved will be the best model on the validation set. 

*[Diagram: Screen Shot 2021-07-27 at 06.47.30.png]*

Another easier way to control the model training is to use [`EarlyStopping`](https://keras.io/api/callbacks/early_stopping/). 

By using early stopping, the training will be stopped when a monitored metric is no longer improving for a given number of consecutive epochs. 

The metric to be monitored during the training is `val_accuracy` in our example, and it is assigned to `monitor` argument. The `patience` represent the number of consecutive epochs of which the training will stop when there is no significant improvements in `val_accuracy`.

```python
from keras.callbacks import EarlyStopping

early_stop = EarlyStopping(monitor='val_accuracy', patience=4, restore_best_weights=True)
```

Let's train for 100 epochs to be able to notice if the training stops as soon as there is no improvements in the validation set for 4 epochs in row.

```python
# Stopping training early

# Getting the model

fashion_classifier_2 = classifier()

history = fashion_classifier_2.fit(fashion_train, fashion_train_label, epochs=100, validation_split=0.15, callbacks=[early_stop])
```

**Execution Output:**
```text
Epoch 1/100
1594/1594 [==============================] - 6s 3ms/step - loss: 0.5298 - accuracy: 0.8124 - val_loss: 0.4781 - val_accuracy: 0.8349
Epoch 2/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3938 - accuracy: 0.8577 - val_loss: 0.3845 - val_accuracy: 0.8653
Epoch 3/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3545 - accuracy: 0.8701 - val_loss: 0.3672 - val_accuracy: 0.8672
Epoch 4/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3294 - accuracy: 0.8788 - val_loss: 0.3474 - val_accuracy: 0.8734
Epoch 5/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3124 - accuracy: 0.8864 - val_loss: 0.3533 - val_accuracy: 0.8702
Epoch 6/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.2955 - accuracy: 0.8904 - val_loss: 0.3438 - val_accuracy: 0.8770
Epoch 7/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.2847 - accuracy: 0.8945 - val_loss: 0.3271 - val_accuracy: 0.8862
Epoch 8/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.2748 - accuracy: 0.8987 - val_loss: 0.3329 - val_accuracy: 0.8836
Epoch 9/100
1594/1594 [=================
... [Output truncated for brevity]
```

The training stopped at the epoch of 12, with the accuracy of 88.33%. On epoch 8, the accuracy was 88.48, it is very clear that from the epoch 8 to 12, there was no improvement, and thus the training stopped. 

Early stopping can potentially save our time and resources. 

One last thing before going to custom callbacks, we can combine both `ModelCheckpoint`(for saving the best model on validation set on the course of training) and `EarlyStopping` for saving us time.

```python
# Combining Early stopping and Model Check point

# Getting the model 

fashion_classifier_2 = classifier()

history = fashion_classifier_2.fit(fashion_train, fashion_train_label, epochs=100, validation_split=0.15, callbacks=[callbacks, early_stop])
```

**Execution Output:**
```text
Epoch 1/100
1594/1594 [==============================] - 6s 3ms/step - loss: 0.5287 - accuracy: 0.8138 - val_loss: 0.4567 - val_accuracy: 0.8323
Epoch 2/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3910 - accuracy: 0.8588 - val_loss: 0.3919 - val_accuracy: 0.8586
Epoch 3/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3532 - accuracy: 0.8701 - val_loss: 0.3811 - val_accuracy: 0.8614
Epoch 4/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3329 - accuracy: 0.8783 - val_loss: 0.3745 - val_accuracy: 0.8633
Epoch 5/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3132 - accuracy: 0.8853 - val_loss: 0.3593 - val_accuracy: 0.8720
Epoch 6/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3026 - accuracy: 0.8882 - val_loss: 0.3393 - val_accuracy: 0.8771
Epoch 7/100
1594/1594 [==============================] - 6s 3ms/step - loss: 0.2864 - accuracy: 0.8947 - val_loss: 0.3387 - val_accuracy: 0.8808
Epoch 8/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.2807 - accuracy: 0.8966 - val_loss: 0.3348 - val_accuracy: 0.8842
Epoch 9/100
1594/1594 [=================
... [Output truncated for brevity]
```

### Custom Callback

Keras offers various functions for implementing custom callbacks that are very handy when you want to control the model training with a little bit of customization. 

You can do certain actions on almost every step of the training. Let's stop the training when the accuracy is 95%.

```python
# Custom callbacks

class callback(tf.keras.callbacks.Callback):

  def on_epoch_end(self, epoch, logs={}):

    if (logs.get('accuracy') > 0.95):

      print('\n Training is cancelled at an accuracy of 95%')
      self.model.stop_training = True


# Call callbacks

custom_callback = callback()
```

```python
# Implementing custom ballback

# Getting the model 

fashion_classifier_2 = classifier()

history = fashion_classifier_2.fit(fashion_train, fashion_train_label, epochs=100, validation_split=0.15, callbacks=[custom_callback])
```

**Execution Output:**
```text
Epoch 1/100
1594/1594 [==============================] - 6s 3ms/step - loss: 0.5393 - accuracy: 0.8095 - val_loss: 0.4304 - val_accuracy: 0.8489
Epoch 2/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3875 - accuracy: 0.8606 - val_loss: 0.4043 - val_accuracy: 0.8553
Epoch 3/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3518 - accuracy: 0.8713 - val_loss: 0.3831 - val_accuracy: 0.8613
Epoch 4/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3307 - accuracy: 0.8785 - val_loss: 0.3949 - val_accuracy: 0.8592
Epoch 5/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3134 - accuracy: 0.8834 - val_loss: 0.3427 - val_accuracy: 0.8756
Epoch 6/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.2982 - accuracy: 0.8904 - val_loss: 0.3421 - val_accuracy: 0.8746
Epoch 7/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.2865 - accuracy: 0.8937 - val_loss: 0.3488 - val_accuracy: 0.8768
Epoch 8/100
1594/1594 [==============================] - 5s 3ms/step - loss: 0.2787 - accuracy: 0.8961 - val_loss: 0.3465 - val_accuracy: 0.8731
Epoch 9/100
1594/1594 [=================
... [Output truncated for brevity]
```

Perfect! The training stopped as soon as the training accuracy reached 95% and the specified message was printed. 

There are many customizations available in [Keras custom callbacks](https://keras.io/guides/writing_your_own_callbacks/). Be sure to check that out.

<a name='3-8'></a>

## 3.8 Using TensorBoard for Model Visualization

[Tensorboard](https://www.tensorflow.org/tensorboard/) is incredible tool used by many people (and not just only TensorFlow developers) to experiment with machine learning. 

With TensorBoard, you can:

* Track and visualize the loss and accuracy
* Visualize the model graphs and operations
* Display images and other types of data
* View the histograms of weights and biases.

We first have to load the TensorBoard extension as follows.

```python
# Load the Tensorboard notebook extension
# And import datetime

%load_ext tensorboard
```

And we clear all logs from all runs we did before.

```python
!rm -rf ./logs/
```

Le's get the model from the function `classifier` defined in previous cells.

```python
# Getting the model 

fashion_classifier = classifier()
```

Let's create a Keras callback.

```python
# Create a callback

tfboard_callback = tf.keras.callbacks.TensorBoard(log_dir="logs")
```

Now, train the model and provide the `tfboard_callback` to `callback` argument.

```python
fashion_classifier.fit(fashion_train, fashion_train_label, epochs=20, validation_split=0.15, callbacks=[tfboard_callback])
```

**Execution Output:**
```text
Epoch 1/20
1594/1594 [==============================] - 6s 4ms/step - loss: 0.5468 - accuracy: 0.8092 - val_loss: 0.4526 - val_accuracy: 0.8351
Epoch 2/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3985 - accuracy: 0.8584 - val_loss: 0.3857 - val_accuracy: 0.8616
Epoch 3/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3600 - accuracy: 0.8689 - val_loss: 0.3876 - val_accuracy: 0.8622
Epoch 4/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3338 - accuracy: 0.8776 - val_loss: 0.3388 - val_accuracy: 0.8774
Epoch 5/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3169 - accuracy: 0.8836 - val_loss: 0.3621 - val_accuracy: 0.8713
Epoch 6/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.3049 - accuracy: 0.8876 - val_loss: 0.3392 - val_accuracy: 0.8787
Epoch 7/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.2918 - accuracy: 0.8925 - val_loss: 0.3668 - val_accuracy: 0.8717
Epoch 8/20
1594/1594 [==============================] - 5s 3ms/step - loss: 0.2799 - accuracy: 0.8972 - val_loss: 0.3521 - val_accuracy: 0.8762
Epoch 9/20
1594/1594 [==========================
... [Output truncated for brevity]
```

Now that the training is over, we can start the TensorBoard.

```python
%tensorboard --logdir logs
```

As you can see, TensorBoard is very useful. The fact that you can use it to visualize the performance metrics, model graphs, and datasets as well.

[BACK TO TOP](#0)

---

## Key Interview Insights: ANN Architecture & Training

1. **Activation Functions Overview**:
   - **Sigmoid**: $\sigma(z) = \frac{1}{1 + e^{-z}}$. Range $(0, 1)$. Vanishing gradients for large $|z|$. Used in binary classification output.
   - **Tanh**: $\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$. Range $(-1, 1)$. Zero-centered, but still saturates at extremes.
   - **ReLU (Rectified Linear Unit)**: $f(z) = \max(0, z)$. Fast, non-saturating gradient for $z > 0$. Risk of "Dying ReLU" when neurons output 0 permanently.
   - **Leaky ReLU**: $f(z) = \max(\alpha z, z)$ with small $\alpha = 0.01$, mitigating dead neurons.
   - **Softmax**: Multi-class probability distribution: $\sigma(z)_i = \frac{e^{z_i}}{\sum_j e^{z_j}}$.
2. **Loss Functions Alignment**:
   - **Regression**: Mean Absolute Error (MAE / L1) or Mean Squared Error (MSE / L2).
   - **Binary Classification**: Binary Cross-Entropy (Log Loss) with Sigmoid activation.
   - **Multi-class Classification (One-hot targets)**: Categorical Cross-Entropy with Softmax activation.
   - **Multi-class Classification (Integer index targets)**: Sparse Categorical Cross-Entropy with Softmax activation.
3. **Combatting Overfitting in Deep Networks**:
   - **EarlyStopping callback**: Halts training when validation loss stops improving.
   - **ReduceLROnPlateau**: Dynamically decays learning rate when performance plateaus.
   - **Dropout**: Randomly deactivates a fraction of neurons (e.g. 20-50%) during forward training to break co-adaptations.
   - **Weight Regularization (L1/L2)**: Penalizes large weights in loss function.
