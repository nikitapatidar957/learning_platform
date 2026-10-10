# Deep Learning for NLP: Keras Preprocessing, Embeddings, RNNs, CNNs & BERT

Master modern neural network architectures for natural language processing using TensorFlow/Keras and Hugging Face: Text Vectorization, trainable Embedding layers, Recurrent Neural Networks (SimpleRNN, LSTM, GRU, Bidirectional), 1D Convolutions for text, and fine-tuning Pretrained BERT transformers.

---

## 1. TensorFlow Text Preprocessing & Tokenization

<table align="left">
  <td>
    <a href="https://colab.research.google.com/github/nyandwi/machine_learning_complete/blob/main/9_nlp_with_tensorflow/1_intro_to_nlp_and_text_preprocessing.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
  </td>
</table>

*This notebook was created by [Jean de Dieu Nyandwi](https://twitter.com/jeande_d) for the love of machine learning community. For any feedback, errors or suggestion, he can be reached on email (johnjw7084 at gmail dot com), [Twitter](https://twitter.com/jeande_d), or [LinkedIn](https://linkedin.com/in/nyandwi).*

<a name='0'></a>
# Intro to NLP and Text Processing with TensorFlow

## Contents 

* [1. Intro to Natural Language Processing](#1)
* [2. Text Processing with TensorFlow](#2)
   * [2.1 Traditional Text Encoding](#2-1)
   * [2.2 Text Encoding with Tokenizer](#2-2)
   * [2.3 Converting Texts into Sequence of Tokens](#2-3)
   * [2.4 Padding Texts Sequences](#2-4)


* [3. Using TextVectorization](#3)

<a name='1'></a>
## 1. Intro to Natural Language Processing

We are surrounded by intelligent machines that can not only see the world, but also can understand and talk with us. 

That is not exagerating. At regular basis, some of us interact with virtual assistants such as Siri, Amazon Alexa, and Google Assistant. And there are thousands of chatbots that we interact with on many software applications and websites.

NLP or Natural Language Processing is an interdisciplinary field. It is a branch of computer science, machine learning, and [computational linguistic](https://en.wikipedia.org/wiki/Computational_linguistics) that is concerned with giving the computers the ability to understand texts and human languages.

### Common tasks involved in NLP

Below are some of the common tasks that can be done with NLP. 

* Text classification
* Sentiment analysis
* Text generation
* Machine translation
* Speech recognition 
* Text to speech conversion
* Optical character recognition

#### Example Applications of NLP

* Spam detection 
* Question answering
* Language to language translation (Machine translation)
* Grammatical error correction (like Grammarly)

One of the classical NLP tool is [NLTK](https://www.nltk.org). Natural Language Toolkit or NLTK provides different functionalities for working with texts and it is commonly used. 

In this lab and later lab, we won't use NLTK. We will use Keras and TensorFlow texts functions. 

There is also a suite of TensorFlow libraries for text processing such as [TensorFlow Text](https://www.tensorflow.org/text/guide/tf_text_intro).

<a name='2'></a>
## 2. Intro to Text Processing with TensorFlow

<a name='2-1'></a>

### 2.1 Text encodings

Most machine learning models (including deep learning ones) can not handle text data. They have to be converted into numerics. In essence, that's what text encoding means: it's converting the text into numerics representation. 

There are 4 main texts encoding techniques which are: 
* Character encoding
* Words based encoding
* One hot encoding
* Word embeddings

Let's talk about these techniques in details. 

#### Character Based Encoding

In this type of encoding technique, each character in a word is represented by unique number. 

One of the traditional character encoding technique is ASCII(American Standard Code Information Interchange). With ASCII, we can nearly convert any character to numeric, and it's pretty standard, but one of the disadvantages is that the antigrams (words with same letters in different order) can have the same encodings, and that can hurt the machine learrning model. 

Example of antigrams include `United` and `Unitied`, `Silent` and `Listen`. 

Character encoding is not widely used and it's less efficient compared to other later techniques. 

The image below shows character encoding done on antigrams.

*[Diagram: Character encoding.png]*

#### Words Based Encoding

In word based encoding, instead of taking a single character in a word, we represent all the individual words with numbers. 

In most cases, words encoding works well than character encodings.

*[Diagram: Word encoding.png]*

#### One Hot Encoding

One hot encoding is another encoding technique that is most known for [encoding categorical features](https://jeande.medium.com/your-onestop-guide-on-handling-categorical-features-5988caaef78a). Although it's not an effective, it can also be used for texts encoding, and the idea is to convert each words in a sentence into one hot vector, where that word will be `1(hot)` and all other words be `0(cold)` in such particular vector. 

Take for instance the sentence `I love this course`. We can take words in such sentence [I, love, this, course] and then create a zero vector with length of 4, and then have 1 on the index that corresponds to the every word as it is shown below.

*[Diagram: Blog Covers-2.png]*

One hot encoding is not a better way to represent texts because most indices are zero and it becomes even harder when you have many words. It will take a lot of space in memory.

By far, in all encoding techniques we saw (character encoding, word encoding, and one hoting words), words encoding is a good way to represent texts. But there is a more better way that is called word embeddings. 

Words embeddings are another way to represent texts where each word is converted into a feature vector, and vectors of the words that have the same semantic meaning will have the same direction in a high dimensional space. We will learn more about embeddings in the next notebook, but if you want you can play with them [here](http://projector.tensorflow.org).

<a name='2-2'></a>

### 2.2 Text Encoding with Keras Tokenizer

Tokenizer is a Keras text preprocessing function that makes it easy to convert a raw text into tokens or sequence of integers.  


We can use [Tokenizer](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer) to encode texts at character or words level. 

We will most of the time prefer words encoding than character encoding to avoid the problems that can be caused by antigram words (the words that has the same characters in different order, ex: united & unitied, listen & silent, restful & fluster).

Let's import TensorFlow and Tokenizer and we will start tokenizing texts right away.

#### Imports

```python
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
```

Before we start converting texts into tokens, let's see all the possibilities available in `Tokenizer`.

Tokenizer arguments

```
■ num_words: the maximum number of words to keep in input text. It's always better to set a high number of you're not sure. If you set a number less than words that you have in texts, the rest will not tokenized.

■ filters: By default, all punctuations and tabs will be removed. If you want to change that, you can provide the punctuations that you want to keep. 

■ lower: This is to be True or False. By default, it is True and that means all texts will be converted to lower case.

split: separator for splitting words. A default separator is a space(" "). If in your texts words are splitted by something else, be sure to mention that there. 

■ char_level: If True, every character will be treated as token. It is False by default.

■ oov_token: This denotes something that to be added to the word_index to replace words that are not available in input text. 

And the last thing to note is that tokens starts at 1.
```

#### Getting the Text

For simplicity, let's explore the all possibilities of Keras's Tokenizer using a simple sentences. Later, we will practice the skills on real world datasets.

```python
# A sample sentence

sentences = ['TensorFlow is a Machine Learning framework',
             'Keras is a well designed deep learning API',
             'TensorFlow and Keras make a great machine learning ecosystem'
              
]
```

```python
sentences
```

**Execution Output:**
```text
['TensorFlow is a Machine Learning framework',
 'Keras is a well designed deep learning API',
 'TensorFlow and Keras make a great machine learning ecosystem']
```

Let's instiate our Tokenizer. We will assume that the number of words are 1000. 

Note that by setting `char_level` to true, we will are converting each character as a token. This is not feasible as we have seen early. It becomes a problems for words that have same characters in different order(antigrams) because their tokens will be ultimately the same.

```python
tokenizer = Tokenizer(num_words=1000, char_level=True)

# Fitting tokenizer on sentences
tokenizer.fit_on_texts(sentences)
```

Let's get the character index, a dictionary that map each character to its token.

```python
char_index = tokenizer.word_index
print(char_index)
```

**Execution Output:**
```text
{' ': 1, 'e': 2, 'a': 3, 'n': 4, 'r': 5, 's': 6, 'i': 7, 'l': 8, 'o': 9, 'm': 10, 'g': 11, 't': 12, 'w': 13, 'k': 14, 'd': 15, 'f': 16, 'c': 17, 'h': 18, 'p': 19, 'y': 20}
```

In real world dataset, you would not want to do that. Let's see what happens when we tokenize words instead of characters. 

It's only just setting `char_level` to `False`.

```python
tokenizer = Tokenizer(num_words=1000)

# Fitting tokenizer on sentences
tokenizer.fit_on_texts(sentences)

word_index = tokenizer.word_index
print(word_index)
```

**Execution Output:**
```text
{'a': 1, 'learning': 2, 'tensorflow': 3, 'is': 4, 'machine': 5, 'keras': 6, 'framework': 7, 'well': 8, 'designed': 9, 'deep': 10, 'api': 11, 'and': 12, 'make': 13, 'great': 14, 'ecosystem': 15}
```

As you can see, rather than having tokens of characters, we have tokens of words and that's more meaningful. By default, punctuations are removed.

Also, we can get how many times each word appears in a sentence/document.

```python
word_counts = tokenizer.word_counts
word_counts
```

**Execution Output:**
```text
OrderedDict([('tensorflow', 2),
             ('is', 2),
             ('a', 3),
             ('machine', 2),
             ('learning', 3),
             ('framework', 1),
             ('keras', 2),
             ('well', 1),
             ('designed', 1),
             ('deep', 1),
             ('api', 1),
             ('and', 1),
             ('make', 1),
             ('great', 1),
             ('ecosystem', 1)])
```

That's it for Tokenization. 

Tokens are not enough and they are not in any order. It's also best to follow the sequence of input sentences.

<a name='2-3'></a>

### 2.3 Converting the Texts into Sequence of Tokens

Instead of getting tokens and stops there, we can also take anoother step further: converting sentence into sequence of tokens. 

This is important because it preserve the sequence of the words in sentence.

```python
sentences
```

**Execution Output:**
```text
['TensorFlow is a Machine Learning framework',
 'Keras is a well designed deep learning API',
 'TensorFlow and Keras make a great machine learning ecosystem']
```

```python
from tensorflow.keras.preprocessing.text import Tokenizer

# Redefining our sentence

sentences = ['TensorFlow is a Machine Learning framework',
             'Keras is a well designed deep learning API',
             'TensorFlow and Keras make a great machine learning ecosystem!',
             'TensorFlow is built on top of Keras',
             'TensorFlow revolves around tensors!'
              
]

tokenizer = Tokenizer(num_words=1000)
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

# Converting text to sequences

text_sequences = tokenizer.texts_to_sequences(sentences)
```

```python
print(f'Words with tokens: {word_index}')
print(f'Sequence of tokens: {text_sequences}')
```

**Execution Output:**
```text
Words with tokens: {'tensorflow': 1, 'is': 2, 'a': 3, 'learning': 4, 'keras': 5, 'machine': 6, 'framework': 7, 'well': 8, 'designed': 9, 'deep': 10, 'api': 11, 'and': 12, 'make': 13, 'great': 14, 'ecosystem': 15, 'built': 16, 'on': 17, 'top': 18, 'of': 19, 'revolves': 20, 'around': 21, 'tensors': 22}
Sequence of tokens: [[1, 2, 3, 6, 4, 7], [5, 2, 3, 8, 9, 10, 4, 11], [1, 12, 5, 13, 3, 14, 6, 4, 15], [1, 2, 16, 17, 18, 19, 5], [1, 20, 21, 22]]
```

From the above words-tokens dictionary and sequences' list, the first list in sequence is `[1, 2, 3, 6, 4, 7]`. It should represent the first sentence in our input sentences(`TensorFlow is a Machine Learning framework`). You can use the word index to verify that.

In the case you expect to provide sentence that have words that tokenizer wasn't fitted at, it's best to create initiate a tokenizer with `oov_token` so that these new words are marked and the oov token will be used to replace these words that are out of vocabulary during text to sequence.

```python
tokenizer = Tokenizer(num_words=1000, oov_token='Word Out of Vocab')
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

# Converting text to sequences

text_sequences = tokenizer.texts_to_sequences(sentences)

print(f'Words with tokens: {word_index}')
print(f'Sequence of tokens: {text_sequences}')
```

**Execution Output:**
```text
Words with tokens: {'Word Out of Vocab': 1, 'tensorflow': 2, 'is': 3, 'a': 4, 'learning': 5, 'keras': 6, 'machine': 7, 'framework': 8, 'well': 9, 'designed': 10, 'deep': 11, 'api': 12, 'and': 13, 'make': 14, 'great': 15, 'ecosystem': 16, 'built': 17, 'on': 18, 'top': 19, 'of': 20, 'revolves': 21, 'around': 22, 'tensors': 23}
Sequence of tokens: [[2, 3, 4, 7, 5, 8], [6, 3, 4, 9, 10, 11, 5, 12], [2, 13, 6, 14, 4, 15, 7, 5, 16], [2, 3, 17, 18, 19, 20, 6], [2, 21, 22, 23]]
```

The `oov_token` takes the first index in dictionary of words-tokens.

So if we now pass new words to the tokenizer(without fitting on them like we did before), it will be replaced by 1 in the output sequence.

```python
new_sentences = ['I like TensorFlow', # like is a new word
                'Keras is a superb deep learning API' # superb is a new word
                
] 

sequences_on_newtexts = tokenizer.texts_to_sequences(new_sentences)
print(f'Sequence of tokens: {sequences_on_newtexts}')
```

**Execution Output:**
```text
Sequence of tokens: [[1, 1, 2], [6, 3, 4, 1, 11, 5, 12]]
```

Looking on the above sequence, you can see that the `oov_token`(having index 1 in word dictionary) has replaced all new words(`I, like, superb`)

To take things further again, let's look into one more thing that is required in nearly all datasets preprocessing: making sure that the inputs data are equal in size.

<a name='2-4'></a>

### 2.4 Padding the Sequences to Have the Same Length

Nearly all machine learning models require the input samples to have the same length/size. Take an example: in computer vision with convolutional neural networks, we always have to resize all images to have the same size. 

This is not an optional step. Below are different options available when padding sequences in Keras.

```
tf.keras.preprocessing.sequence.pad_sequences(
    sequences, maxlen=None, dtype="int32", padding="pre", truncating="pre", value=0.0
)
```
Notes on arguments:

```
• sequence: This is a list of sequences in integer forms (tokenized texts).

• maxlen: Maximum length of all sequences. If not provided, sequences will be padded to the length of the longest sequence in provided sequences.

• padding: 'pre' or `post`. Choose `pre` to padd before the sequence or `post` to padd after the sequence. By default, the sequence are pre-padded. 

• truncating: 'pre' or `post`. Remove the values from sequences larger than maxlen, either at the beginning or at the end of the sequences.

• value: a float or a string that you want to use as a padding value. By default, the sequences are padded with 0.
```

Let's practice it.

```python
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Padding text_sequences 

padded_sequences = pad_sequences(text_sequences, maxlen=10)


print('WORD INDEX')
print(f'Words with tokens: {word_index}')
print("---------")


print('SEQUENCES')
print(f'Words with tokens: {text_sequences}')
print("---------")

print('PADDED SEQUENCES')
print(f'Sequence of tokens: {padded_sequences}')
```

**Execution Output:**
```text
WORD INDEX
Words with tokens: {'Word Out of Vocab': 1, 'tensorflow': 2, 'is': 3, 'a': 4, 'learning': 5, 'keras': 6, 'machine': 7, 'framework': 8, 'well': 9, 'designed': 10, 'deep': 11, 'api': 12, 'and': 13, 'make': 14, 'great': 15, 'ecosystem': 16, 'built': 17, 'on': 18, 'top': 19, 'of': 20, 'revolves': 21, 'around': 22, 'tensors': 23}
---------
SEQUENCES
Words with tokens: [[2, 3, 4, 7, 5, 8], [6, 3, 4, 9, 10, 11, 5, 12], [2, 13, 6, 14, 4, 15, 7, 5, 16], [2, 3, 17, 18, 19, 20, 6], [2, 21, 22, 23]]
---------
PADDED SEQUENCES
Sequence of tokens: [[ 0  0  0  0  2  3  4  7  5  8]
 [ 0  0  6  3  4  9 10 11  5 12]
 [ 0  2 13  6 14  4 15  7  5 16]
 [ 0  0  0  2  3 17 18 19 20  6]
 [ 0  0  0  0  0  0  2 21 22 23]]
```

As you can see, the sequences are pre-padded with 0. In case we want to padd after the sequences, we can set `padding` to `post`. Also we can set padding value to something else, say -1.

```python
padded_sequences = pad_sequences(text_sequences, maxlen=10, padding='post', value=-1)

print('PADDED SEQUENCES')
print(f'Sequence of tokens: {padded_sequences}')
```

**Execution Output:**
```text
PADDED SEQUENCES
Sequence of tokens: [[ 2  3  4  7  5  8 -1 -1 -1 -1]
 [ 6  3  4  9 10 11  5 12 -1 -1]
 [ 2 13  6 14  4 15  7  5 16 -1]
 [ 2  3 17 18 19 20  6 -1 -1 -1]
 [ 2 21 22 23 -1 -1 -1 -1 -1 -1]]
```

That's it for tokenization, sequences and padding. If you have wondered why all of this is done, you are not alone. But this is a basic way of preparing texts before feeding them to a machine learning model. 

And it's basically same for all learning algorithms. We have to prepare data to be in the right format accepted by the learning algorithm. The preparation required for text dataset are different to images for example.

<a name='3'></a>

## 3. Using TextVectorization Layer to Preprocess Texts

TextVectorization layer is a Keras preprocessing that is used to transform strings into a list of tokens. 

This layer will do 3 main things: 


* Standardize text samples(removing punctuations and lowering the text case)
* Splitting a sentence into individual words and converting them to tokens
* And converting the tokens into numbers that can be fed to a model. 

In few words, TextVectorization remove the punctuations from texts and lower the case(standardization), tokenize the sentences, and vectorize the tokens. 

Here are notes about the layer's argument:

```
tf.keras.layers.experimental.preprocessing.TextVectorization(
    max_tokens=None,
    standardize="lower_and_strip_punctuation",
    split="whitespace",
    ngrams=None,
    output_mode="int",
    output_sequence_length=None,
    pad_to_max_tokens=False,
    vocabulary=None
)
```

```
* max_tokens: Maximum number of vocabulary size. A vocabulary is a list of individual or unique words in a sentence. 

* standardize: This is denote the standardization specifics to be applied to input data. By default, it is `lower_and_strip_punctuation' meaning to lower the case and remove punctuations.

* split: This denote what will be considered while splitting the input text. By default it is `whitespace`, but if your text is different, you can mention it here. 

* output mode: Specify the type of output of layer. By default it is 'int', meaning the layer output will be integer indices. 

* vocabulary: an array or (list, set, tuple) of strings or a path to a text file. 

```

Let's put that into practice.

```python
import tensorflow as tf

from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
```

In TensorFlow 2.6 and above, this layer will not be in experimentals. It will be in [Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/).

```python
# Sample sentences

sentences = [
             'TensorFlow is a deep learning library!',
             'Is TensorFlow powered by Keras API?'
]
```

```python
max_features = 1000

text_vect_layer = tf.keras.layers.TextVectorization(
    max_tokens=max_features,
    output_mode='int',
    output_sequence_length=10

)
```

We can use adapt() method to fit the sentences to a layer.

```python
text_vect_layer.adapt(sentences)
```

**Execution Output:**
```text
WARNING:tensorflow:6 out of the last 7 calls to <function PreprocessingLayer.make_adapt_function.<locals>.adapt_step at 0x7fa4e05ca9e0> triggered tf.function retracing. Tracing is expensive and the excessive number of tracings could be due to (1) creating @tf.function repeatedly in a loop, (2) passing tensors with different shapes, (3) passing Python objects instead of tensors. For (1), please define your @tf.function outside of the loop. For (2), @tf.function has experimental_relax_shapes=True option that relaxes argument shapes that can avoid unnecessary retracing. For (3), please refer to https://www.tensorflow.org/guide/function#controlling_retracing and https://www.tensorflow.org/api_docs/python/tf/function for  more details.
```

Let's pass a sample sentence to a layer to see what kind of the output is.

```python
sample_sentence = 'Tensorflow is a machine learning framework!'

vectorized_sentence = text_vect_layer([sample_sentence])

print(f'Orginal sentence: \n {sample_sentence}')
print(f'Vectorized sentence: \n {vectorized_sentence}')
```

**Execution Output:**
```text
Orginal sentence: 
 Tensorflow is a machine learning framework!
Vectorized sentence: 
 [[ 2  3 10  1  6  1  0  0  0  0]]
```

If you can notice, both `machine` and `framework` were not part of the sentences we adapted to the layer before and they are represented by `1` in the vectorized output. This is to mean that indice 1 is reserved for words that are out of vocabulary(`oov_token`).

You can also see that the output is padded with 0 as the output sequence size is 10. 

The layer basically do all required preprocessing at once.

One of the great advantage of having this layer is that it can be used inside a model. So you can have a model that accept texts at the input, transform it, and model it...

We will use this layer in later practice. If you want to learn more, check out the [documentation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TextVectorization). It's pretty detailed.

This is the end of the lab. NLP is a machine learning field that deals with texts. 

Both NLP and Computer Vision are two of the most exciting fields in AI and machine learning and being able to know them can help you build cross applications. For example, given an image of a kid playing basketball, you can use computer vision techniques to recognize image, and generate a caption with NLP techniques. That's awesome, right!? 

So, in the lab we also learned how to represent texts as numbers because the input data to most machine learning models must be vectors or array of numbers. We saw how to tokenize words, convert tokens into sequences, and padd the sequences. Also we saw how to convert texts into vectors or numbers with TextVectorization layer. 

In the next lab, we will learn about another useful texts representation techniques called word embeddings.

## [BACK TO TOP](#0)

---

## 2. Trainable Word Embeddings in Practice

<table align="left">
  <td>
    <a href="https://colab.research.google.com/github/nyandwi/machine_learning_complete/blob/main/9_nlp_with_tensorflow/2_using_word_embeddings_to_represent_texts.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
  </td>
</table>

*This notebook was created by [Jean de Dieu Nyandwi](https://twitter.com/jeande_d) for the love of machine learning community. For any feedback, errors or suggestion, he can be reached on email (johnjw7084 at gmail dot com), [Twitter](https://twitter.com/jeande_d), or [LinkedIn](https://linkedin.com/in/nyandwi).*

<a name='0'></a>
# Using Word Embeddings to Represent Texts

## Contents 

* [1. Intro Word Embeddings](#1)
* [2. Embedding In Practice](#2)
   * [2.1 Getting the data](#2-1)
   * [2.2 Preparing the data](#2-2)
   * [2.3 Building, compiling and training a sentiment analysis model](#2-3)
   * [2.4 Visualizing the model results](#2-4)
   * [2.5 Testing the model on new reviews](#2-5)

<a name='1'></a>
## 1. Intro to Word Embeddings

Word Embeddings are used to represent the words in the form of a feature vectors. The words with similar meaning will have the same representations. 

Embeddings are trainable and that means that during the model training, they will improve. The similar words will end up having the same representation. 

In vector speaking, similar words will have the same direction. 

There is this [Embedding Projector](http://projector.tensorflow.org) that let you visualize and play with embeddings. Have a tour there and search some words. 

For example, searching programming, you will see words similar in meaning to programming in the same vector space.

*[Diagram: Screen Shot 2021-08-24 at 08.07.35.png]*

Keras has an embedding layer. We will use it in later practice, but feel free to learn more in [documentation](https://keras.io/api/layers/core_layers/embedding/).

<a name='2'></a>

## 2. Embeddings In Practice

We are going to practice embeddings on Imdb reviews. Imdb reviews is the hello world of natural language processing, just like mnist is for computer vision.

We will be building a sentiment analysis - classifying the movie reviews.

<a name='2-1'></a>
### 2.1. Getting the Imdb Reviews Data

Imdb reviews contains positive and negative movies reviews. You can learn more about this dataset [here](https://ai.stanford.edu/~amaas/data/sentiment/).

```
@InProceedings{maas-EtAl:2011:ACL-HLT2011,
  author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher},
  title     = {Learning Word Vectors for Sentiment Analysis},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {142--150},
  url       = {http://www.aclweb.org/anthology/P11-1015}
}
```

We will get the data from [Keras datasets built in datasets](https://keras.io/api/datasets/imdb/). It is also available in [TensorFlow datasets](https://www.tensorflow.org/datasets/catalog/imdb_reviews).

#### Imports

```python
import tensorflow as tf
from tensorflow import keras
import numpy as np
```

Loading the training and validation data from Keras datasets. There are 25.000 samples for training and 25.000 samples for validation. 

Also, setting `max_features` to 20000 means we are only considering the first 20000 words, and `sequence_length` of 200 denotes that we will take the first 200 words in each movie review.

```python
max_features = 20000
sequence_length = 200

(train_data, train_labels), (val_data, val_labels) = keras.datasets.imdb.load_data(num_words=max_features)
```

```python
train_data[:2]
```

**Execution Output:**
```text
array([list([1, 14, 22, 16, 43, 530, 973, 1622, 1385, 65, 458, 4468, 66, 3941, 4, 173, 36, 256, 5, 25, 100, 43, 838, 112, 50, 670, 2, 9, 35, 480, 284, 5, 150, 4, 172, 112, 167, 2, 336, 385, 39, 4, 172, 4536, 1111, 17, 546, 38, 13, 447, 4, 192, 50, 16, 6, 147, 2025, 19, 14, 22, 4, 1920, 4613, 469, 4, 22, 71, 87, 12, 16, 43, 530, 38, 76, 15, 13, 1247, 4, 22, 17, 515, 17, 12, 16, 626, 18, 19193, 5, 62, 386, 12, 8, 316, 8, 106, 5, 4, 2223, 5244, 16, 480, 66, 3785, 33, 4, 130, 12, 16, 38, 619, 5, 25, 124, 51, 36, 135, 48, 25, 1415, 33, 6, 22, 12, 215, 28, 77, 52, 5, 14, 407, 16, 82, 10311, 8, 4, 107, 117, 5952, 15, 256, 4, 2, 7, 3766, 5, 723, 36, 71, 43, 530, 476, 26, 400, 317, 46, 7, 4, 12118, 1029, 13, 104, 88, 4, 381, 15, 297, 98, 32, 2071, 56, 26, 141, 6, 194, 7486, 18, 4, 226, 22, 21, 134, 476, 26, 480, 5, 144, 30, 5535, 18, 51, 36, 28, 224, 92, 25, 104, 4, 226, 65, 16, 38, 1334, 88, 12, 16, 283, 5, 16, 4472, 113, 103, 32, 15, 16, 5345, 19, 178, 32]),
       list([1, 194, 1153, 194, 8255, 78, 228, 5, 6, 1463, 4369, 5012, 134, 26, 4, 715, 8, 118, 1634, 14, 394, 20, 13, 119, 954, 189, 102, 5, 207, 110, 3103, 21, 14, 69, 188, 8, 30, 23, 7, 4, 249, 126, 93, 4, 114, 9, 2300, 1523, 5, 64
... [Output truncated for brevity]
```

```python
train_labels[:10]
```

**Execution Output:**
```text
array([1, 0, 0, 1, 0, 0, 1, 0, 1, 0])
```

<a name='2-2'></a>

### 2.2. Preparing the Dataset

The Imbd dataset that we loaded from Keras was already converted to tokens, so we won't have to do much work here. 

We are going to only convert the tokens into sequences.

```python
from tensorflow.keras.preprocessing.sequence import pad_sequences

train_data = pad_sequences(train_data, maxlen=sequence_length)
val_data = pad_sequences(val_data, maxlen=sequence_length)
```

<a name='2-3'></a>

### 2.3. Build, Compile and Train the Model

The purpose of this lab is to learn embeddings. The Keras Embedding layer will take the tokens and represent them into a high dimensional vector, where the vector of the words that has the same semantic meaning will have the same direction. 

In essence, embedding layer will take the number of the words in a vocabulary and the number of dimensions

```python
# embedding layer: represent 100 words into 5 dimensions

embedding_layer = tf.keras.layers.Embedding(100,5)

embed_integers = embedding_layer(tf.constant([1,2,3,4]))

embed_integers.numpy()
```

**Execution Output:**
```text
array([[ 1.2614403e-02, -1.1478484e-02,  8.1606880e-03, -3.9430130e-02,
         2.0547520e-02],
       [-8.9646950e-03, -1.1008494e-03, -3.3753276e-02, -3.0158116e-02,
         4.5642104e-02],
       [ 5.8295615e-03,  2.1967243e-02,  2.9412154e-02,  1.9587997e-02,
        -4.6676543e-02],
       [ 2.0423044e-02, -2.1431793e-02,  2.7912881e-02,  1.5731920e-02,
         3.9350241e-05]], dtype=float32)
```

The above is what the embedding layer will exactly do: representing words into feature vector of a given dimension. 

Embeddings are trainable, and that means as we train the model, words that are similar will get closer and closer. You can have a taste of this notion by visiting [Embedding Projector](http://projector.tensorflow.org).

```python
# Create a model

embedding_dim = 16

model = tf.keras.Sequential([
       tf.keras.layers.Embedding(max_features, embedding_dim, input_length=sequence_length),
       tf.keras.layers.GlobalAveragePooling1D(),
       tf.keras.layers.Dense(6, activation='relu'),
       tf.keras.layers.Dropout(0.5),
       tf.keras.layers.Dense(1, activation='sigmoid')
])
```

We will use Tensorboard to visualize training metrics and embeddings.

```python
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="logs")
```

We will compile the model with the loss of `binary_crossentropy` and `adam` optimizer.

```python
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```

Before training the model, we can see the model summary.

```python
model.summary()
```

**Execution Output:**
```text
Model: "sequential_7"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
embedding_11 (Embedding)     (None, 200, 16)           320000    
_________________________________________________________________
global_average_pooling1d_6 ( (None, 16)                0         
_________________________________________________________________
dense_14 (Dense)             (None, 6)                 102       
_________________________________________________________________
dropout_5 (Dropout)          (None, 6)                 0         
_________________________________________________________________
dense_15 (Dense)             (None, 1)                 7         
=================================================================
Total params: 320,109
Trainable params: 320,109
Non-trainable params: 0
_________________________________________________________________
```

```python
history = model.fit(train_data, 
                    train_labels,
                    validation_data = (val_data, val_labels),
                    epochs = 5,
                    callbacks=[tensorboard_callback])
```

**Execution Output:**
```text
Epoch 1/5
782/782 [==============================] - 7s 8ms/step - loss: 0.6281 - accuracy: 0.6886 - val_loss: 0.5163 - val_accuracy: 0.8107
Epoch 2/5
782/782 [==============================] - 6s 8ms/step - loss: 0.4767 - accuracy: 0.8266 - val_loss: 0.4096 - val_accuracy: 0.8722
Epoch 3/5
782/782 [==============================] - 6s 8ms/step - loss: 0.4086 - accuracy: 0.8503 - val_loss: 0.3566 - val_accuracy: 0.8772
Epoch 4/5
782/782 [==============================] - 6s 8ms/step - loss: 0.3586 - accuracy: 0.8715 - val_loss: 0.3412 - val_accuracy: 0.8788
Epoch 5/5
782/782 [==============================] - 6s 8ms/step - loss: 0.3293 - accuracy: 0.8836 - val_loss: 0.3413 - val_accuracy: 0.8772
```

<a name='2-4'></a>

### 2.4. Visualizing the Model Results

As we have provided TensorBoard callback during the model training, we can visualize the model results and embeddings.

```python
%load_ext tensorboard
%tensorboard --logdir logs
```

**Execution Output:**
```text
The tensorboard extension is already loaded. To reload it, use:
  %reload_ext tensorboard
```

TensorBoard is a fantastic model visualization tool. If you are running this, spend sometime looking over the graphs in TensorBoard.

<a name='2-5'></a>

### 2.5. Testing the Model on New texts

Let's test the sentiment classifier on some sample reviews.

```python
negative_review = ["This was an absolutely terrible movie. Don't be lured in by Christopher Walken or Michael Ironside. This must simply be their worst role in history"]

# Convert the test sentence to tokens and sequences

from tensorflow.keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer(num_words=20000)
tokenizer.fit_on_texts(negative_review)

neg_sequences = tokenizer.texts_to_sequences(negative_review)

# Pad the sequence to have the size of the sequences used for model training

neg_sequences  = pad_sequences(neg_sequences  , maxlen = sequence_length)


# Predict the review
model.predict(neg_sequences)
```

**Execution Output:**
```text
array([[0.54507416]], dtype=float32)
```

```python
positive_review = ["Very beautiful and awesome movie. This is the kind of film for a snowy Sunday afternoon when the rest of the world can go ahead with its own business as you descend into a big arm-chair and mellow for a couple of hours. "]

# Convert the test sentence to tokens 
tokenizer_2 = Tokenizer(num_words=20000)
tokenizer_2.fit_on_texts(positive_review)

pos_sequences = tokenizer_2.texts_to_sequences(positive_review)
pos_sequences = pad_sequences(pos_sequences, maxlen = sequence_length)

model.predict(pos_sequences)
```

**Execution Output:**
```text
array([[0.4356643]], dtype=float32)
```

This is it about word embeddings. Embeddings alone are not enough. In the next notebook, we will introduce Recurrent Neural Networks(RNNs) and Long Short Term Memories(LSTMs). RNNs and LSTMs are some of the fundamental language models that are widely used to day.

[BACK TO TOP](#0)

---

## 3. Recurrent Neural Networks (SimpleRNN, LSTM, GRU)

<table align="left">
  <td>
    <a href="https://colab.research.google.com/github/nyandwi/machine_learning_complete/blob/main/9_nlp_with_tensorflow/3_recurrent_neural_networks.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
  </td>
</table>

*This notebook was created by [Jean de Dieu Nyandwi](https://twitter.com/jeande_d) for the love of machine learning community. For any feedback, errors or suggestion, he can be reached on email (johnjw7084 at gmail dot com), [Twitter](https://twitter.com/jeande_d), or [LinkedIn](https://linkedin.com/in/nyandwi).*

<a name='0'></a>
# Intro to Recurrent Neural Networks(RNNs)

## Contents 

* [1. Intro to Recurrent Neural Networks](#1)
* [2. RNNs In Practice: Movies Sentiment Analysis](#2)
   * [2.1 Getting the data](#2-1)
   * [2.2 Preparing the data](#2-2)
   * [2.3 Building, compiling and training a RNN model](#2-3)
   * [2.4 Visualizing the model results](#2-4)

* [3. Intro to Long Short Terms Memories](#3)
* [4. LSTMs in Practice : News Classification](#4)
   * [4.1 Getting the data](#4-1)
   * [4.2 Preparing the data](#4-2)
   * [4.3 Building and training a RNN model](#4-3)
   * [4.4 Visualizing the model results](#4-4)
   * [4.5 Using Stacked LSTMs](#4-5)
   * [4.6 Using Gate Recurrent Unit(GRU)](#4-6)

* [5. Further Learning](#5)

<a name='1'></a>
# 1. Intro to Recurrent Neural Networks (RNN)

Recurrent Neural Networks (RNNs) are  neural network architecture that is suited for handling sequential datasets. Sequential datasets are these types of datasets that has some forms of sequence such as: sound(a sequence of sound waves), texts (sequence of words or characters), and time series.

When you are working with sequential data (say texts), you want to preserve the sequence of the information. 

Take an example: Given the sentence `To day, I took my cat for a [....]`, can you predict the next word? In order for a machine to predict the next word in that sentence, there should be a way to maintain the flow and the sequence of the words, not only from the input to output, but also having a backward connection at each time step. That is where the notion of `recurrence` comes from.

*[Diagram: W6S2.png]*

The conventional feedforward networks have a constant flow of information: The data goes straight from the input to output, whereas in RNNs, there is a feedback loop of data at each time step. Also, the input dimension of data to be fed to feedforward network is fixed, whereas RNNs can handle the data of variable input lengths/dimension.

*[Diagram: TF RNN.png]*

*[Diagram: 14.png]*

#### Applications of RNNs

RNNs can be used in any application that have the need of mantaining the recurrence of data.

Below are some of the RNN's applications:

* Machine translation
* Artificial music and text generation
* Sentiment analysis and text classification
* Medical signals analysis (such as ECG)
* Self driving cars trajectories

With that said, RNNs possesses some disadvantages. Because they have a small memory, they can not be able to track long term sequences. Also, they suffer from [vanishing and exploding gradients](https://www.youtube.com/watch?v=qhXZsFVxGKo). And these disadvantages motivates the other version of recurrent networks called Long Short Term Memories(LSTMs). More on LSTMs later.

<a name='2'></a>

# 2. RNNs In Practice: Simple RNN

<a name='2-1'></a>

## 2.1 Getting the Data

We are going to use Imdb movie reviews dataset available in [Keras built in datasets.](https://keras.io/api/datasets/)

```python
import tensorflow as tf
from tensorflow import keras
import numpy as np
```

```python
max_features = 20000
sequence_length = 200

(train_data, train_labels), (val_data, val_labels) = keras.datasets.imdb.load_data(num_words=max_features)
```

**Execution Output:**
```text
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb.npz
17465344/17464789 [==============================] - 0s 0us/step
17473536/17464789 [==============================] - 0s 0us/step
```

Loading the training and validation data from Keras datasets. There are 25.000 samples for training and 25.000 samples for validation. 

Also, setting `max_features` to 20000 means we are only considering the first 20000 words, and `sequence_length` of 200 denotes that we will take the first 200 words in each movie review.

```python
train_data[:2]
```

**Execution Output:**
```text
array([list([1, 14, 22, 16, 43, 530, 973, 1622, 1385, 65, 458, 4468, 66, 3941, 4, 173, 36, 256, 5, 25, 100, 43, 838, 112, 50, 670, 2, 9, 35, 480, 284, 5, 150, 4, 172, 112, 167, 2, 336, 385, 39, 4, 172, 4536, 1111, 17, 546, 38, 13, 447, 4, 192, 50, 16, 6, 147, 2025, 19, 14, 22, 4, 1920, 4613, 469, 4, 22, 71, 87, 12, 16, 43, 530, 38, 76, 15, 13, 1247, 4, 22, 17, 515, 17, 12, 16, 626, 18, 19193, 5, 62, 386, 12, 8, 316, 8, 106, 5, 4, 2223, 5244, 16, 480, 66, 3785, 33, 4, 130, 12, 16, 38, 619, 5, 25, 124, 51, 36, 135, 48, 25, 1415, 33, 6, 22, 12, 215, 28, 77, 52, 5, 14, 407, 16, 82, 10311, 8, 4, 107, 117, 5952, 15, 256, 4, 2, 7, 3766, 5, 723, 36, 71, 43, 530, 476, 26, 400, 317, 46, 7, 4, 12118, 1029, 13, 104, 88, 4, 381, 15, 297, 98, 32, 2071, 56, 26, 141, 6, 194, 7486, 18, 4, 226, 22, 21, 134, 476, 26, 480, 5, 144, 30, 5535, 18, 51, 36, 28, 224, 92, 25, 104, 4, 226, 65, 16, 38, 1334, 88, 12, 16, 283, 5, 16, 4472, 113, 103, 32, 15, 16, 5345, 19, 178, 32]),
       list([1, 194, 1153, 194, 8255, 78, 228, 5, 6, 1463, 4369, 5012, 134, 26, 4, 715, 8, 118, 1634, 14, 394, 20, 13, 119, 954, 189, 102, 5, 207, 110, 3103, 21, 14, 69, 188, 8, 30, 23, 7, 4, 249, 126, 93, 4, 114, 9, 2300, 1523, 5, 64
... [Output truncated for brevity]
```

```python
train_labels[:10]
```

**Execution Output:**
```text
array([1, 0, 0, 1, 0, 0, 1, 0, 1, 0])
```

<a name='2-2'></a>

### 2.2. Preparing the Dataset

The Imdb dataset from Keras dataset is already prepared. The only thing left to do is to pad the tokenized sequences in order that all sentences/reviews have the same length, length equivalent to `sequence_length.`

```python
from tensorflow.keras.preprocessing.sequence import pad_sequences

train_data = pad_sequences(train_data, maxlen=sequence_length)
val_data = pad_sequences(val_data, maxlen=sequence_length)
```

<a name='2-3'></a>

### 2.3. Build, Compile and Train the Model

The basic RNN is implemented in Keras as a layer. There are more [recurrent layers (LSTMs and GRUs)](https://keras.io/api/layers/recurrent_layers/) that we will see later, but for now we are going to use [`SimpleRNN`](https://keras.io/api/layers/recurrent_layers/) to classify the movie reviews.

Here is the overview of the Keras SimpleRNN layer. We will have a high level understandingof its some important arguments.

```

tf.keras.layers.SimpleRNN(
    units,
    activation="tanh",
    dropout=0.0,
    recurrent_dropout=0.0,
    return_sequences=False,
    return_state=False,
    go_backwards=False
)
```

* **units**: A positive integer that denotes the dimension of the output.

* **activation**: The activation function to use. The default activation function is `tanh`. 

* **dropout**: A float between 0 and 1 denoting the percentage of units or neurons to drop for the linear transformation of the input. 

* **recurrent_dropout**: A float between 0 and 1 denoting the percentage of units or neurons to drop for the linear transformation of the recurrent state. 

* **return_state**: True or False. Denotes whether to return the last state in addition to the output.

* **go_backwards**: True or False. Denotes whether to process the input sequence backwards and return the reversed sequence. 

That's a few notes about the important parameters. For more about the SimpleRNN layer, there is a well documented help at [keras.io](https://keras.io/api/layers/recurrent_layers/simple_rnn/).

```python
simple_rnn = tf.keras.Sequential([
                          
  # Add an embedding layer to convert input tokens into a feature vector                  
  tf.keras.layers.Embedding(input_dim=max_features, output_dim=32, input_length=sequence_length),
  tf.keras.layers.SimpleRNN(32, return_sequences=True),
  tf.keras.layers.SimpleRNN(16, return_sequences=True),
  tf.keras.layers.Dense(10, activation='relu'),
  tf.keras.layers.Dense(1, activation='sigmoid')
])
```

```python
# Compiling the model

simple_rnn.compile(optimizer='adam', loss='binary_crossentropy', metrics='accuracy')
```

```python
# Training the model 

history = simple_rnn.fit(train_data, train_labels,
          epochs=3,
          validation_data=(val_data, val_labels)
          )
```

**Execution Output:**
```text
Epoch 1/3
782/782 [==============================] - 486s 618ms/step - loss: 0.6143 - accuracy: 0.6478 - val_loss: 0.5477 - val_accuracy: 0.7082
Epoch 2/3
782/782 [==============================] - 483s 617ms/step - loss: 0.5089 - accuracy: 0.7352 - val_loss: 0.5863 - val_accuracy: 0.6944
Epoch 3/3
782/782 [==============================] - 481s 615ms/step - loss: 0.6491 - accuracy: 0.6101 - val_loss: 0.6275 - val_accuracy: 0.6383
```

<a name='2-4'></a>

### 2.4. Visualizing the Model Results

```python
import matplotlib.pyplot as plt
```

```python
# function to plot accuracy and loss

def plot_acc_loss(history):

  model_history = history.history
  acc = model_history['accuracy']
  val_acc = model_history['val_accuracy']
  loss = model_history['loss']
  val_loss = model_history['val_loss']
  epochs = history.epoch

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
plot_acc_loss(history)
```

The downside of RNNs is that they fail to process the long term sequences because their of limited memory. Due to having short term memory, the context will diminish over many time steps. 

In order to handle long term dependencies, another version of RNN called LSTMs were introduced. Because LSTMs perform really well on sequence datasets, Simple RNNs are longer used.

<a name='3'></a>

# 3. Intro to Long Short Term Memory(LSTM)

LSTM is a recurrent neural network type that looks like Simple RNN cell, but it work very much better. In fact, we could have straightly used LSTM without bothering with a basic RNN cell, but hopefully that provided you with the foundations of the recurrent neural networks. And I believe [starting simple](https://jeande.medium.com/getting-started-with-machine-learning-a-learning-path-that-will-take-you-from-zero-to-hero-876545d38240) is always a best way to understand a hard topic.

While Simple RNN cell suffers from handling long sequences, LSTMs have the ability to store and preserve long term sequences over many time steps. A special design difference about LSTM cell is that it has a gate which is the basis of why it can control the flow of information over many time steps. 

In short, LSTM uses gates to control the flow of information from the current time step to next time step in the following 4 ways: 

  * The input gate recognizes the input sequence
  * Forget gate gets rid of all irrelevant information contained in the input sequence and store relevant information in long term memory
  * LTSM cell updates update cell's state values
  * Output gate controls the information that has to be sent to the next time step. 


The ability of LSTMs to handle long term sequences make it a suitable neural network architecture for various sequential tasks such as speech recognition, image caption generation, machine translation, and language modelling. 


Here is a great illustration of LTSMs architecture taken from [MIT Intro to Deep Learning](http://introtodeeplearning.com). MIT Intro Deep Learning is a recommended course to learn more about sequence modelling.

*[Diagram: Screen Shot 2021-09-01 at 09.22.56.png]*

Here is also [a great paper](https://arxiv.org/pdf/1409.2329.pdf) that you can use to learn more about LSTMs. 

Let's put that into practice.

<a name='4'></a>

# 4. LSTMs in Practice : News Classification

<a name='4-1'></a>

## 4.1 Getting the Data

In the quest of learning LTSMs, we are going to use `ag_news_subset` dataset that is available in [TensorFlow datasets](https://www.tensorflow.org/datasets/catalog/ag_news_subset). TensorFlow datasets is a collection of awesome datasets that can be used right away with little preparations. 

AG is a collection of more than 1 million news articles gathered from more than 2000 news sources by ComeToMyHead in more than 1 year of activity. 

The AG dataset contains 4 classes that are: World(0), Sports(1), Business(2), Sci/Tech(3). The total number of training samples is 120,000 and testing 7,600. Each class contains 30,000 training samples and 1,900 testing samples. 

You can learn more about the dataset [here](http://groups.di.unipi.it/~gulli/AG_corpus_of_news_articles.html), or read the orginal paper that used it to explore the use of [character-level convolutional networks (ConvNets) for text classification](https://arxiv.org/abs/1509.01626) by Xiang Zhang, Junbo Zhao, and Yann LeCun.

Let's get the dataset from TensorFlow datasets.

```python
import tensorflow as tf
from tensorflow import keras
import tensorflow_datasets as tfds
import numpy as np
import pandas as pd
```

The dataset that we are going to download has only one version so far. Let's specify it so that when it is updated, our lab will not be affected. If loading the data fails, run the cell again. It happens sometime when loading datasets from TF datasets.

```python
(train_data, val_data), info = tfds.load('ag_news_subset:1.0.0', #version 1.0.0
                                         split=['train', 'test'],
                                         with_info=True, 
                                         as_supervised=True
)
```

**Execution Output:**
```text
[1mDownloading and preparing dataset ag_news_subset/1.0.0 (download: 11.24 MiB, generated: 35.79 MiB, total: 47.03 MiB) to /root/tensorflow_datasets/ag_news_subset/1.0.0...[0m



Shuffling and writing examples to /root/tensorflow_datasets/ag_news_subset/1.0.0.incompleteMVJXV1/ag_news_subset-train.tfrecord
Shuffling and writing examples to /root/tensorflow_datasets/ag_news_subset/1.0.0.incompleteMVJXV1/ag_news_subset-test.tfrecord
[1mDataset ag_news_subset downloaded and prepared to /root/tensorflow_datasets/ag_news_subset/1.0.0. Subsequent calls will reuse this data.[0m
```

Now that we have the data, we can look into some examples. This is always a good practice. 

Printing `info` that we loaded with the dataset, we can see pretty much everything we would need to know about the data.

```python
print(info)
```

**Execution Output:**
```text
tfds.core.DatasetInfo(
    name='ag_news_subset',
    version=1.0.0,
    description='AG is a collection of more than 1 million news articles.
News articles have been gathered from more than 2000  news sources by ComeToMyHead in more than 1 year of activity.
ComeToMyHead is an academic news search engine which has been running since July, 2004.
The dataset is provided by the academic comunity for research purposes in data mining (clustering, classification, etc),
information retrieval (ranking, search, etc), xml, data compression, data streaming,
and any other non-commercial activity.
For more information, please refer to the link http://www.di.unipi.it/~gulli/AG_corpus_of_news_articles.html .

The AG's news topic classification dataset is constructed by Xiang Zhang (xiang.zhang@nyu.edu) from the dataset above.
It is used as a text classification benchmark in the following paper:
Xiang Zhang, Junbo Zhao, Yann LeCun. Character-level Convolutional Networks for Text Classification. Advances in Neural Information Processing Systems 28 (NIPS 2015).

The AG's news topic classification dataset is constructed by choosing 4 largest classes from the original corpus.
Each class contains 30,00
... [Output truncated for brevity]
```

```python
# Displaying the classes

class_names = info.features['label'].names
num_classes = info.features['label'].num_classes

print(f'The news are grouped into {num_classes} classes that are :{class_names}')
```

**Execution Output:**
```text
The news are grouped into 4 classes that are :['World', 'Sports', 'Business', 'Sci/Tech']
```

```python
num_train = info.splits['train'].num_examples
num_val = info.splits['test'].num_examples

print(f'The number of training samples: {num_train} \nThe number of validation samples: {num_val}')
```

**Execution Output:**
```text
The number of training samples: 120000 
The number of validation samples: 7600
```

We can also display the first 10 news samples. We can use [`tfds.as_dataframe`](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe) to display them as dataframe.

```python
news_df = tfds.as_dataframe(train_data.take(10), info)

news_df.head(10)
```

**Execution Output:**
```text
description  label
0  b'AMD #39;s new dual-core Opteron chip is desi...      3
1  b'Reuters - Major League Baseball\\Monday anno...      1
2  b'President Bush #39;s  quot;revenue-neutral q...      2
3  b'Britain will run out of leading scientists u...      3
4  b'London, England (Sports Network) - England m...      1
5  b'TOKYO - Sony Corp. is banking on the \\$3 bi...      0
6  b'Giant pandas may well prefer bamboo to lapto...      3
7  b'VILNIUS, Lithuania - Lithuania #39;s main pa...      0
8  b'Witnesses in the trial of a US soldier charg...      0
9  b'Dan Olsen of Ponte Vedra Beach, Fla., shot a...      1
```

Let's display some full news.

```python
for i in range (0,4):

  print(f"Sample news {i}\n \
  Label: {news_df['label'][i]} {(class_names[i])}\n \
  Description: {news_df['description'][i]}\n----------\n")
```

**Execution Output:**
```text
Sample news 0
   Label: 3 World
   Description: b'AMD #39;s new dual-core Opteron chip is designed mainly for corporate computing applications, including databases, Web services, and financial transactions.'
----------

Sample news 1
   Label: 1 Sports
   Description: b'Reuters - Major League Baseball\\Monday announced a decision on the appeal filed by Chicago Cubs\\pitcher Kerry Wood regarding a suspension stemming from an\\incident earlier this season.'
----------

Sample news 2
   Label: 2 Business
   Description: b'President Bush #39;s  quot;revenue-neutral quot; tax reform needs losers to balance its winners, and people claiming the federal deduction for state and local taxes may be in administration planners #39; sights, news reports say.'
----------

Sample news 3
   Label: 3 Sci/Tech
   Description: b'Britain will run out of leading scientists unless science education is improved, says Professor Colin Pillinger.'
----------
```

```python
news_df.columns
```

**Execution Output:**
```text
Index(['description', 'label'], dtype='object')
```

Now that we understand the data, let's prepare it before we can use LSTMs to classify the news.

<a name='4-2'></a>

## 4.2 Preparing the Data

We can not feed the raw texts that we loaded from the tensorflow datasets to the model. We have to do some preps works.

One of the major thing we have to do is to vectorize the texts or convert them into numeric tokens. 

We will use [TextVectorizer](https://keras.io/api/layers/preprocessing_layers/text/text_vectorization/), but before we get there, let's first shuffle and batch the training data. 

For validation data, we don't shuffle. We only batch it.

```python
buffer_size = 1000
batch_size = 32

train_data = train_data.shuffle(buffer_size)
train_data = train_data.batch(batch_size).prefetch(1)
val_data = val_data.batch(batch_size).prefetch(1)
```

```python
for news, label in train_data.take(1):

  print(f'Sample news\n----\n {news.numpy()[:4]} \n----\nCorresponding labels: {label.numpy()[:4]}')
```

**Execution Output:**
```text
Sample news
----
 [b'Macs still have fewer bugs than Windows PCs, but Apple moves to plug security holes before problems crop up.'
 b'Mexican stocks fell early Monday, dragged lower by cement giant Cemex (CX) after it announced a multibillion dollar acquisition of a British company, the largest by a Mexican firm ever.'
 b'The update for the e-mail program focuses mainly on security enhancements and adds a feature dubbed ScamWatch, which aims to combat "phishing" on the Internet.'
 b'Eight eBay sellers were ordered to pay nearly \\$90,000 (euro 70,000) in restitution and fines after admitting they bid up products online to inflate the prices.'] 
----
Corresponding labels: [3 2 3 2]
```

As you can see from the above, the training data is in batches of descriptions and their corresponding labels.

Now, we can use Keras [TextVectorization layer](https://keras.io/api/layers/preprocessing_layers/text/text_vectorization/) to handle all preprocessing. It will convert the texts into tokens, convert them into sequences, padd the sequences. It also removes punctuations and lower the case. 

That's all it does by default.

```python
max_features = 20000

text_vectorizer = tf.keras.layers.TextVectorization(max_tokens=max_features)
```

After creating the layer, we can use `adapt` to pass the dataset throught it. Notice that we use `lambda function` to get the description separated from the label.

```python
text_vectorizer.adapt(train_data.map(lambda description, label : description))
```

We can get the vocabulary. Vocabulary is the list of individual words making up a particular sentence.

```python
vocab = text_vectorizer.get_vocabulary()
vocab[:10]
```

**Execution Output:**
```text
['', '[UNK]', 'the', 'a', 'to', 'of', 'in', 'and', 'on', 'for']
```

Let's pass some new sentences to `text_vectorizer`. The vectorized sequences will be padded with the maximum sentences, but if you want to hava fixed size, you can set the `output_sequence_length` to any value in the layer initialization.

```python
sample_news = ['This weekend there is a sport match between Man U and Fc Barcelona',
               'Tesla has unveiled its humanoid robot that appeared dancing during the show!']
```

```python
vectorized_news = text_vectorizer(sample_news)
vectorized_news.numpy()
```

**Execution Output:**
```text
array([[   40,   491,   185,    16,     3,  1559,   560,   163,   362,
        13418,     7,  7381,  2517],
       [    1,    20,   878,    14,     1,  4663,    10,  1249, 11657,
          159,     2,   541,     0]])
```

If you can look on the above tensors, the second sentence was padded with 0. Also the words `Tesla` and `humanoid` have an indice of 1 because they were not a part of the training data (that we adapted to the `text_vectorizer`). 

So this means that the indice 1 is reserved for all words that are new to the layer. In the vocabulary, these kind of words are replaced by `UNK`.

We are going to use the `text_vectorizer` as part of the model.

<a name='4-3'></a>

## 4.3 Creating and Training the Model

We are going to create a Keras Sequential model that takes the texts input and output the class of the input texts.

The model is going to be made of the following layers:

* `TextVectorization layer` for converting input texts into tokens.
* `Embedding layer` for representing the tokens into a trainable feature vector of a high dimensional space. Because the feature vector is trainable, after training the words that have the same semantic meaning will end up having the same vectors (and pointing to the same directions).
* `A recurrent neural network (RNN), LSTMs specifically` for processing the sequences. LTSMs are well suited for long sequences and as we saw earlier, SimpleRNN suffers from long term dependencies. We will also wrapp the LSTM layer into [Bidirectional layer](https://keras.io/api/layers/recurrent_layers/bidirectional/ in order to be able to process the sequences from both directions (forward and backward).

* `Dense layer` for classification purpose. It takes the vector and convert it into a single logit output.

```python
input_dim = len(text_vectorizer.get_vocabulary())
input_dim
```

**Execution Output:**
```text
20000
```

```python
model = tf.keras.Sequential([
    text_vectorizer,
    tf.keras.layers.Embedding(input_dim=input_dim, output_dim=64, mask_zero=True),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(4, activation='softmax')
])
```

```python
# Compile the model

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
```

```python
# Train the model

history = model.fit(train_data, 
                    epochs=5,
                    validation_data=val_data
)
```

**Execution Output:**
```text
Epoch 1/5
3750/3750 [==============================] - 237s 42ms/step - loss: 0.3305 - accuracy: 0.8843 - val_loss: 0.2703 - val_accuracy: 0.9075
Epoch 2/5
3750/3750 [==============================] - 155s 41ms/step - loss: 0.2021 - accuracy: 0.9300 - val_loss: 0.3008 - val_accuracy: 0.9061
Epoch 3/5
3750/3750 [==============================] - 155s 41ms/step - loss: 0.1333 - accuracy: 0.9527 - val_loss: 0.3692 - val_accuracy: 0.9036
Epoch 4/5
3750/3750 [==============================] - 155s 41ms/step - loss: 0.0812 - accuracy: 0.9704 - val_loss: 0.4574 - val_accuracy: 0.9032
Epoch 5/5
3750/3750 [==============================] - 157s 42ms/step - loss: 0.0506 - accuracy: 0.9817 - val_loss: 0.5542 - val_accuracy: 0.8955
```

```python
# Evaluating the model

eval_loss, eval_acc = model.evaluate(val_data)
print(f'Loss on validation data: {eval_loss}\n Accuracy on Validation data: {eval_acc}')
```

**Execution Output:**
```text
238/238 [==============================] - 4s 18ms/step - loss: 0.5542 - accuracy: 0.8955
Loss on validation data: 0.5541531443595886
 Accuracy on Validation data: 0.8955262899398804
```

<a name='4-4'></a>

## 4.4 Visualizing the Results

Let's now visualize the results of the training.

```python
import matplotlib.pyplot as plt

loss_acc_df = pd.DataFrame(history.history)

loss_acc_df.plot(figsize=(12,8))
```

<a name='4-5'></a>

## 4.5 Stacking LSTMs Layers

```python
model = tf.keras.Sequential([
    text_vectorizer,
    tf.keras.layers.Embedding(input_dim=input_dim, output_dim=64, mask_zero=True),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64,  return_sequences=True)),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(4, activation='softmax')
])
```

```python
# Compile the model

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
```

```python
# Train the model

history = model.fit(train_data, 
                    epochs=5,
                    validation_data=val_data
)
```

**Execution Output:**
```text
Epoch 1/5
3750/3750 [==============================] - 334s 73ms/step - loss: 0.4098 - accuracy: 0.8626 - val_loss: 0.2883 - val_accuracy: 0.9051
Epoch 2/5
3750/3750 [==============================] - 271s 72ms/step - loss: 0.2557 - accuracy: 0.9201 - val_loss: 0.2944 - val_accuracy: 0.9038
Epoch 3/5
3750/3750 [==============================] - 269s 72ms/step - loss: 0.1988 - accuracy: 0.9360 - val_loss: 0.3246 - val_accuracy: 0.9022
Epoch 4/5
3750/3750 [==============================] - 268s 72ms/step - loss: 0.1455 - accuracy: 0.9522 - val_loss: 0.4522 - val_accuracy: 0.8974
Epoch 5/5
3750/3750 [==============================] - 272s 72ms/step - loss: 0.1078 - accuracy: 0.9641 - val_loss: 0.4931 - val_accuracy: 0.8974
```

```python
# Evaluating the model

eval_loss, eval_acc = model.evaluate(val_data)
print(f'Loss on validation data: {eval_loss}\n Accuracy on Validation data: {eval_acc}')
```

**Execution Output:**
```text
238/238 [==============================] - 7s 27ms/step - loss: 0.4931 - accuracy: 0.8974
Loss on validation data: 0.49308159947395325
 Accuracy on Validation data: 0.8973684310913086
```

```python
import matplotlib.pyplot as plt

loss_acc_df = pd.DataFrame(history.history)

loss_acc_df.plot(figsize=(12,8))
```

```python
# Predicting the class of new news

sample_news = ['The self driving car company Tesla has unveiled its humanoid robot that appeared dancing during the show!']

sample_news = np.array(sample_news)

predictions = model.predict(sample_news)

predicted_class = np.argmax(predictions)

print(f'predicted class: {predicted_class} \nPredicted Class name: {class_names[predicted_class]}')
```

**Execution Output:**
```text
predicted class: 3 
Predicted Class name: Sci/Tech
```

Obviously, our model tried to learn that the the provided sample news is tech or science.

```python
# Predicting the class of new news

sample_news = ['This weekend there is a match between two big footbal teams in the national league']
sample_news = np.array(sample_news)

predictions = model.predict(sample_news)

predicted_class = np.argmax(predictions)

print(f'predicted class: {predicted_class} \nPredicted Class name: {class_names[predicted_class]}')
```

**Execution Output:**
```text
predicted class: 1 
Predicted Class name: Sports
```

And again it also able to learn that the provided news is sports type and that's obvious.

<a name='4-6'></a>

## 4.6 Using Gate Recurrent Unit(GRU)

Gate Recurrent Unit or GRU are almost similar to LSTMs but they are cheaper to run compared to LSTMs. Here is a [paper](https://arxiv.org/abs/1406.1078) that introduced it if you would like to learn more. 

Like LSTMs, and SimpleRNNs, GRU is also implemented in Keras as a layer. Learn more about it on [Keras documentation](https://keras.io/api/layers/recurrent_layers/gru/).

```python
model = tf.keras.Sequential([
    text_vectorizer,
    tf.keras.layers.Embedding(input_dim=input_dim, output_dim=64, mask_zero=True),
    tf.keras.layers.GRU(64, return_sequences=True, dropout=0.2, recurrent_dropout=0.1), 
    tf.keras.layers.GRU(64, dropout=0.2, recurrent_dropout=0.2),
    tf.keras.layers.Dense(4, activation='softmax')
])
```

```python
# Compile the model

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
```

```python
# Train the model

history = model.fit(train_data, 
                    epochs=5,
                    validation_data=val_data
)
```

**Execution Output:**
```text
Epoch 1/5
3750/3750 [==============================] - 697s 185ms/step - loss: 0.3557 - accuracy: 0.8750 - val_loss: 0.2788 - val_accuracy: 0.9051
Epoch 2/5
3750/3750 [==============================] - 692s 184ms/step - loss: 0.2300 - accuracy: 0.9220 - val_loss: 0.2925 - val_accuracy: 0.9042
Epoch 3/5
3750/3750 [==============================] - 692s 185ms/step - loss: 0.1876 - accuracy: 0.9359 - val_loss: 0.2956 - val_accuracy: 0.9070
Epoch 4/5
3750/3750 [==============================] - 685s 183ms/step - loss: 0.1517 - accuracy: 0.9474 - val_loss: 0.3269 - val_accuracy: 0.9017
Epoch 5/5
3750/3750 [==============================] - 688s 183ms/step - loss: 0.1209 - accuracy: 0.9578 - val_loss: 0.3570 - val_accuracy: 0.9033
```

You see even with using dropouts within recurrent layers didn't improve the performance. The validation set is resonably small. One can try to increase it and see if that might increase the performance on the validation set.

```python
import matplotlib.pyplot as plt

loss_acc_df = pd.DataFrame(history.history)

loss_acc_df.plot(figsize=(12,8))
```

<a name='5'></a>

# 5. Futher Learning

This notebook has introduced Recurrent Neural Networks or RNNs. RNNs are suitable networks for natural language processing and all sequencial applications in general. We have seen different types of recurrent networks such as basic RNN cell, Long Short Term Memory(LSTM), and Gate Recurrent Unit(GRU). 

If you would like to learn more about sequence models, I recommend the following courses:

* Deep Learning Specialization - Course 5 of Sequence models. This course is available on [Coursera](https://www.coursera.org/learn/nlp-sequence-models) and [Youtube](https://www.youtube.com/watch?v=_i3aqgKVNQI&list=PLkDaE6sCZn6F6wUI9tvS_Gw1vaFAx6rd6). 
* Intro to Deep Learning MIT - Lecture 2 of Recurrent Neural Networks, available on [Youtube](https://www.youtube.com/watch?v=qjrad0V0uJE&t=168s).

## [BACK TO TOP](#0)

---

## 4. 1D Convolutional Neural Networks (Conv1D) for Text Classification

<table align="left">
  <td>
    <a href="https://colab.research.google.com/github/nyandwi/machine_learning_complete/blob/main/9_nlp_with_tensorflow/4_using_cnns_and_rnns_for_texts_classification.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
  </td>
</table>

*This notebook was created by [Jean de Dieu Nyandwi](https://twitter.com/jeande_d) for the love of machine learning community. For any feedback, errors or suggestion, he can be reached on email (johnjw7084 at gmail dot com), [Twitter](https://twitter.com/jeande_d), or [LinkedIn](https://linkedin.com/in/nyandwi).*

<a name='0'></a>
# Using Convolutional Neural Networks for Texts Classification

## Contents 

* [1. Intro Convolutional Neural Networks for Texts](#1)
* [2. CNN for Texts in Practice: News Classification](#2)
   * [2.1 Getting the data](#2-1)
   * [2.2 Preparing the data](#2-2)
   * [2.3 Building, compiling and training a RNN model](#2-3)
   * [2.4 Visualizing the model results](#2-4)

* [3.Combining ConvNets and RNNs](#3)
   * [3.1 ConvNets and RNNs model](#3-1)
   * [3.2 Visualizing the model results](#3-2)
   * [3.3 Performing Inference On New Texts](#3-3)

* [4. Further Learning](#4)

<a name='1'></a>
# 1. Intro to CNNs for Texts

Convolutional neural networks are remarkably a suitable network architectures for images, or computer vision tasks in general because of their ability to extract features from images using filters. 

A recent studies([Text Understanding from Scratch by Xiang Zhang & Yann LeCun](https://arxiv.org/pdf/1502.01710.pdf), [Recurrent Convolutional Neural Networks for Text Classification by Siwei Lai & Liheng Xu & Kang Liu & Jun Zhao](https://www.aaai.org/ocs/index.php/AAAI/AAAI15/paper/view/9745/9552)) has shown that CNNs can also perform wel on texts just as they do on images.

Quoting [LeCun paper](https://arxiv.org/pdf/1502.01710.pdf), 

* CNNs don't require knowledge of words. And that means it is fine to pass characters to the network. We have previously been using words.
* CNNs do not require knowledge of syntax or semantic structures. 
* While RNNs can be expensive to run, CNNs are away cheaper.


In text applications or any sequential datasets in general, we use [Conv1D](https://keras.io/api/layers/convolution_layers/convolution1d/) instead of Conv2D.  The design of Conv1D is quite similar to Conv2D, the only difference is the dimension of the input. So, it is made of convolution and pooling layers.

Below is a typical CNN inspired design for texts. Source: Text Understanding from Scratch, Yann LeCun.

*[Diagram: Contexts.png]*

Here is the overview of the main parameters of Conv1D. 

If you worked with CNNs before, you probably don't see any new thing. `filters` specify the number of filters, `kernel_size` denotes the size of each filter (remember it is one dimension), `strides` is the number of steps the filter will take as it go through the input texts, `padding` for ading zeros (`valid` for not padding, `same` for padding). And `activation` denotes the activation function to use. 

```
tf.keras.layers.Conv1D(
    filters,
    kernel_size,
    strides=1,
    padding="valid",
    activation=None,
)
```

<a name='2'></a>

# 2. CNN's for Texts In Practice: News Classification

<a name='2-1'></a>
## 2.1 Getting the Data

In this practice, we will use [news dataset, `ag_news_subset`](https://www.tensorflow.org/datasets/catalog/ag_news_subset) that is available on TensorFlow datasets. 

TensorFlow datasets is a collection of awesome datasets that can be used right away with little preparations. 

AG is a collection of more than 1 million news articles gathered from more than 2000 news sources by ComeToMyHead in more than 1 year of activity. 

The AG dataset contains 4 classes that are: World(0), Sports(1), Business(2), Sci/Tech(3). The total number of training samples is 120,000 and testing 7,600. Each class contains 30,000 training samples and 1,900 testing samples. 

You can learn more about the dataset [here](http://groups.di.unipi.it/~gulli/AG_corpus_of_news_articles.html), or read the orginal paper that used it to explore the use of [character-level convolutional networks (ConvNets) for text classification](https://arxiv.org/abs/1509.01626) by Xiang Zhang, Junbo Zhao, and Yann LeCun.

Let's get the dataset from TensorFlow datasets.

```python
import tensorflow as tf
from tensorflow import keras
import tensorflow_datasets as tfds
import numpy as np
import pandas as pd
```

The dataset that we are going to download has only one version so far. Let's specify it so that when it is updated, our lab will not be affected. If loading the data fails, run the cell again. It happens sometime when loading datasets from TF datasets.

Orginally, the training set contains 120.000 news samples, whereas test set contain 7600 samples. Let's take 10% percent of news from training set to validation set so we can increase it a little bit.

```python
(train_data, val_data), info = tfds.load('ag_news_subset:1.0.0', #version 1.0.0
                                         split=['train[:90%]', 'train[90%:]+test'],
                                         with_info=True, 
                                         as_supervised=True
)
```

We can display the `info` that we loaded with dataset.

```python
print(info)
```

**Execution Output:**
```text
tfds.core.DatasetInfo(
    name='ag_news_subset',
    version=1.0.0,
    description='AG is a collection of more than 1 million news articles.
News articles have been gathered from more than 2000  news sources by ComeToMyHead in more than 1 year of activity.
ComeToMyHead is an academic news search engine which has been running since July, 2004.
The dataset is provided by the academic comunity for research purposes in data mining (clustering, classification, etc),
information retrieval (ranking, search, etc), xml, data compression, data streaming,
and any other non-commercial activity.
For more information, please refer to the link http://www.di.unipi.it/~gulli/AG_corpus_of_news_articles.html .

The AG's news topic classification dataset is constructed by Xiang Zhang (xiang.zhang@nyu.edu) from the dataset above.
It is used as a text classification benchmark in the following paper:
Xiang Zhang, Junbo Zhao, Yann LeCun. Character-level Convolutional Networks for Text Classification. Advances in Neural Information Processing Systems 28 (NIPS 2015).

The AG's news topic classification dataset is constructed by choosing 4 largest classes from the original corpus.
Each class contains 30,00
... [Output truncated for brevity]
```

```python
# Displaying the classes

class_names = info.features['label'].names
num_classes = info.features['label'].num_classes

print(f'The news are grouped into {num_classes} classes that are :{class_names}')
```

**Execution Output:**
```text
The news are grouped into 4 classes that are :['World', 'Sports', 'Business', 'Sci/Tech']
```

```python
num_train = info.splits['train'].num_examples
num_val = info.splits['test'].num_examples

print(f'The number of training samples: {num_train} \nThe number of validation samples: {num_val}')
```

**Execution Output:**
```text
The number of training samples: 120000 
The number of validation samples: 7600
```

We can also display the first 10 news samples. We can use [`tfds.as_dataframe`](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe) to display them as dataframe.

```python
news_df = tfds.as_dataframe(train_data.take(10), info)

news_df.head(10)
```

**Execution Output:**
```text
description  label
0  b'AMD #39;s new dual-core Opteron chip is desi...      3
1  b'Reuters - Major League Baseball\\Monday anno...      1
2  b'President Bush #39;s  quot;revenue-neutral q...      2
3  b'Britain will run out of leading scientists u...      3
4  b'London, England (Sports Network) - England m...      1
5  b'TOKYO - Sony Corp. is banking on the \\$3 bi...      0
6  b'Giant pandas may well prefer bamboo to lapto...      3
7  b'VILNIUS, Lithuania - Lithuania #39;s main pa...      0
8  b'Witnesses in the trial of a US soldier charg...      0
9  b'Dan Olsen of Ponte Vedra Beach, Fla., shot a...      1
```

Let's display some full news.

```python
for i in range (0,4):

  print(f"Sample news {i}\n \
  Label: {news_df['label'][i]} {(class_names[i])}\n \
  Description: {news_df['description'][i]}\n----------\n")
```

**Execution Output:**
```text
Sample news 0
   Label: 3 World
   Description: b'AMD #39;s new dual-core Opteron chip is designed mainly for corporate computing applications, including databases, Web services, and financial transactions.'
----------

Sample news 1
   Label: 1 Sports
   Description: b'Reuters - Major League Baseball\\Monday announced a decision on the appeal filed by Chicago Cubs\\pitcher Kerry Wood regarding a suspension stemming from an\\incident earlier this season.'
----------

Sample news 2
   Label: 2 Business
   Description: b'President Bush #39;s  quot;revenue-neutral quot; tax reform needs losers to balance its winners, and people claiming the federal deduction for state and local taxes may be in administration planners #39; sights, news reports say.'
----------

Sample news 3
   Label: 3 Sci/Tech
   Description: b'Britain will run out of leading scientists unless science education is improved, says Professor Colin Pillinger.'
----------
```

<a name='2-2'></a>

## 2.2 Preparing the Data

We can not feed the raw texts that we loaded from the tensorflow datasets to the model. We have to do some preps works.

One of the major thing we have to do is to vectorize the texts or convert them into numeric tokens. 

We will use [TextVectorizer](https://keras.io/api/layers/preprocessing_layers/text/text_vectorization/), but before we get there, let's first shuffle and batch the training data. 

For validation data and test data, we don't shuffle. We only batch it.

```python
buffer_size = 1000
batch_size = 32

train_data = train_data.shuffle(buffer_size)
train_data = train_data.batch(batch_size).prefetch(1)
val_data = val_data.batch(batch_size).prefetch(1)
```

```python
for news, label in train_data.take(1):

  print(f'Sample news\n----\n {news.numpy()[:4]} \n----\nCorresponding labels: {label.numpy()[:4]}')
```

**Execution Output:**
```text
Sample news
----
 [b'About seven or eight years ago, Harry Shatel had that conversation with Charlie Weis about the future. Shatel, the Morristown High School baseball coach, doesn #39;t remember the exact date '
 b"AFP - Australia's foreign minister will pay a rare visit to North Korea this week for talks on its nuclear programme after creating a stir here by warning a North Korean missile would be able to hit Sydney."
 b' quot;The Electoral Commission set the date of January 30 as the date of the election, quot; spokesman Farid Ayar told Reuters on Sunday.'
 b'That photo above is no longer accurate. I #39;ve shaven my head to protest the firing of ... Kevin from The Apprentice. Dude has a bachelor #39;s from Penn, an MBA from Emory and is working on a law degree from the '] 
----
Corresponding labels: [1 0 0 1]
```

As you can see from the above, the training data is in batches of descriptions and their corresponding labels.

Now, we can use Keras [TextVectorization layer](https://keras.io/api/layers/preprocessing_layers/text/text_vectorization/) to handle all required text preprocessing. It will convert the texts into tokens, convert them into sequences, padd the sequences. It also removes punctuations and lower the case. 

That's all it does by default.

```python
max_features = 10000

text_vectorizer = tf.keras.layers.TextVectorization(max_tokens=max_features)
```

After creating the layer, we can use `adapt` to pass the dataset throught it. Notice that we use `lambda function` to get the description separated from the label.

```python
text_vectorizer.adapt(train_data.map(lambda description, label : description))
```

We can get the vocabulary. Vocabulary is the list of individual words making up a particular sentence.

```python
vocab = text_vectorizer.get_vocabulary()
vocab[:10]
```

**Execution Output:**
```text
['', '[UNK]', 'the', 'a', 'to', 'of', 'in', 'and', 'on', 'for']
```

Let's pass some new sentences to `text_vectorizer`. The vectorized sequences will be padded with the maximum sentences, but if you want to hava fixed size, you can set the `output_sequence_length` to any value in the layer initialization.

```python
sample_news = ['This weekend there is a sport match between Man U and Fc Barcelona',
               'Tesla has unveiled its humanoid robot that appeared dancing during the show!']
```

```python
vectorized_news = text_vectorizer(sample_news)
vectorized_news.numpy()
```

**Execution Output:**
```text
array([[  40,  494,  186,   16,    3, 1567,  570,  159,  370,    1,    7,
        7486, 2556],
       [   1,   20,  876,   13,    1, 4845,   10, 1273,    1,  160,    2,
         532,    0]])
```

If you can look on the above tensors, the second sentence was padded with 0. Also the words `Tesla` and `humanoid` have an indice of 1 because they were not a part of the training data (that we adapted to the `text_vectorizer`). 

So this means that the indice 1 is reserved for all words that are new to the layer. In the vocabulary, these kind of words are replaced by `UNK`.

We will use `text_vectorizer` as part of the model.

<a name='2-3'></a>

## 2.3 Creating and Training the Model

We are going to create a Keras Sequential model that takes the texts input and output the class of the input texts.

The model is going to be made of the following layers:

* `TextVectorization layer` for texts preprocessing.

* `Embedding layer` for representing the tokens into a trainable feature vector of a high dimensional space. Because the feature vector is trainable, after training the words that have the same semantic meaning will end up having the same vectors (and pointing to the same directions).

* `A Conv1D` for processing the sequences. Yes, Convnets can be used for texts processing. We will start off with only Convnets, and later use RNNs as well.

* `Dense layer` for classification purpose. It takes the vector and convert it into a single logit output.

```python
input_dim = len(text_vectorizer.get_vocabulary())
input_dim
```

**Execution Output:**
```text
10000
```

```python
model = tf.keras.Sequential([
    text_vectorizer,
    tf.keras.layers.Embedding(input_dim=input_dim, output_dim=64, mask_zero=True),
    tf.keras.layers.Conv1D(64, 5, activation='relu'),
    tf.keras.layers.MaxPooling1D(),
    tf.keras.layers.Conv1D(64, 5, activation='relu'),
    tf.keras.layers.GlobalMaxPool1D(),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(4, activation='softmax')
])
```

Getting the model summary

```python
model.summary()
```

**Execution Output:**
```text
Model: "sequential_7"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
text_vectorization (TextVect (None, None)              0         
_________________________________________________________________
embedding_7 (Embedding)      (None, None, 64)          640000    
_________________________________________________________________
conv1d_8 (Conv1D)            (None, None, 64)          20544     
_________________________________________________________________
max_pooling1d_4 (MaxPooling1 (None, None, 64)          0         
_________________________________________________________________
conv1d_9 (Conv1D)            (None, None, 64)          20544     
_________________________________________________________________
global_max_pooling1d_1 (Glob (None, 64)                0         
_________________________________________________________________
dense_14 (Dense)             (None, 32)                2080      
_________________________________________________________________
dropout_7 (Dropout)          (None, 32)                0
... [Output truncated for brevity]
```

We can also plot the model with Keras util's `plot_model`.

```python
from tensorflow.keras.utils import plot_model

plot_model(model)
```

**Execution Output:**
```text
<IPython.core.display.Image object>
```

```python
# Compile the model

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
```

```python
batch_size = 32

train_steps = int(len(train_data)/batch_size)
val_steps = int(len(val_data)/batch_size)
```

```python
# Train the model

history = model.fit(train_data, 
                    epochs=25,
                    validation_data=val_data,
                    steps_per_epoch=train_steps,
                    validation_steps=val_steps
)
```

**Execution Output:**
```text
Epoch 1/25
105/105 [==============================] - 3s 23ms/step - loss: 1.3313 - accuracy: 0.3470 - val_loss: 1.0612 - val_accuracy: 0.4753
Epoch 2/25
105/105 [==============================] - 2s 22ms/step - loss: 0.9455 - accuracy: 0.5565 - val_loss: 0.7538 - val_accuracy: 0.7368
Epoch 3/25
105/105 [==============================] - 2s 21ms/step - loss: 0.6512 - accuracy: 0.7580 - val_loss: 0.4937 - val_accuracy: 0.8240
Epoch 4/25
105/105 [==============================] - 2s 21ms/step - loss: 0.4899 - accuracy: 0.8339 - val_loss: 0.4605 - val_accuracy: 0.8339
Epoch 5/25
105/105 [==============================] - 2s 21ms/step - loss: 0.4775 - accuracy: 0.8318 - val_loss: 0.4126 - val_accuracy: 0.8586
Epoch 6/25
105/105 [==============================] - 2s 21ms/step - loss: 0.4359 - accuracy: 0.8518 - val_loss: 0.3818 - val_accuracy: 0.8783
Epoch 7/25
105/105 [==============================] - 2s 22ms/step - loss: 0.4106 - accuracy: 0.8717 - val_loss: 0.3710 - val_accuracy: 0.8799
Epoch 8/25
105/105 [==============================] - 2s 21ms/step - loss: 0.4174 - accuracy: 0.8679 - val_loss: 0.3561 - val_accuracy: 0.8980
Epoch 9/25
105/105 [==============================] - 2s
... [Output truncated for brevity]
```

<a name='2-4'></a>

## 2.4 Visualizing the Results

It is always a good practice to plot the model results. When doing error analysis, plotting learning curve becomes helpful. 

Let's plot the loss and accuracy over on the course of epochs.

```python
import matplotlib.pyplot as plt

# function to plot accuracy and loss

def plot_acc_loss(history):

  model_history = history.history
  acc = model_history['accuracy']
  val_acc = model_history['val_accuracy']
  loss = model_history['loss']
  val_loss = model_history['val_loss']
  epochs = history.epoch

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
plot_acc_loss(history)
```

That's not pretty bad. Let's combine CNNs and LSTMs to see if we can improve the results further.

<a name='3'></a>

# 3. Combining CNNs and RNNs for Text Classification

<a name='3-1'></a>

## 3.1 Convnets and RNNs Model

Just like how CNNs extract the features in images, they are also able to `learn the hierarchical representations of words, phrases and sentences in order to understand text`[(Yann LeCun, 2016)](https://arxiv.org/pdf/1502.01710.pdf). The downside of using CNNs alone is that they don't maintain the order of timesteps.

We can also introduce Recurrent Neural Networks (LSTMs specifically) to give the network the sequence handling capability. So, `Conv1D` can extract meaningful words in input sentences, and RNNs can preverve the sequence contained in the output features from the CNNs.

I am only going to add one bidirectional LSTM layer to handle the CNNs features from both directions.

```python
conv_rnn_model = tf.keras.Sequential([
    text_vectorizer,
    tf.keras.layers.Embedding(input_dim=input_dim, output_dim=64, mask_zero=True),
    tf.keras.layers.Conv1D(64, 5, activation='relu'),
    tf.keras.layers.MaxPooling1D(),
    tf.keras.layers.Conv1D(64, 5, activation='relu'),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(4, activation='softmax')
])
```

```python
conv_rnn_model.summary()
```

**Execution Output:**
```text
Model: "sequential_9"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
text_vectorization (TextVect (None, None)              0         
_________________________________________________________________
embedding_9 (Embedding)      (None, None, 64)          640000    
_________________________________________________________________
conv1d_12 (Conv1D)           (None, None, 64)          20544     
_________________________________________________________________
max_pooling1d_6 (MaxPooling1 (None, None, 64)          0         
_________________________________________________________________
conv1d_13 (Conv1D)           (None, None, 64)          20544     
_________________________________________________________________
bidirectional_1 (Bidirection (None, 128)               66048     
_________________________________________________________________
dense_18 (Dense)             (None, 32)                4128      
_________________________________________________________________
dropout_9 (Dropout)          (None, 32)                0
... [Output truncated for brevity]
```

```python
# Compile the model

conv_rnn_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
```

```python
batch_size = 32

train_steps = int(len(train_data)/batch_size)
val_steps = int(len(val_data)/batch_size)


# Train the model

history = conv_rnn_model.fit(train_data, 
                    epochs=25,
                    validation_data=val_data,
                    steps_per_epoch=train_steps,
                    validation_steps=val_steps
)
```

**Execution Output:**
```text
Epoch 1/25
105/105 [==============================] - 9s 53ms/step - loss: 1.3051 - accuracy: 0.3119 - val_loss: 0.9660 - val_accuracy: 0.5164
Epoch 2/25
105/105 [==============================] - 5s 47ms/step - loss: 0.8398 - accuracy: 0.5753 - val_loss: 0.6016 - val_accuracy: 0.7122
Epoch 3/25
105/105 [==============================] - 5s 45ms/step - loss: 0.6768 - accuracy: 0.6732 - val_loss: 0.5675 - val_accuracy: 0.7023
Epoch 4/25
105/105 [==============================] - 5s 45ms/step - loss: 0.6061 - accuracy: 0.7125 - val_loss: 0.4932 - val_accuracy: 0.8092
Epoch 5/25
105/105 [==============================] - 5s 45ms/step - loss: 0.5031 - accuracy: 0.8176 - val_loss: 0.3908 - val_accuracy: 0.8618
Epoch 6/25
105/105 [==============================] - 5s 45ms/step - loss: 0.4422 - accuracy: 0.8530 - val_loss: 0.3892 - val_accuracy: 0.8651
Epoch 7/25
105/105 [==============================] - 5s 46ms/step - loss: 0.4099 - accuracy: 0.8682 - val_loss: 0.3633 - val_accuracy: 0.8766
Epoch 8/25
105/105 [==============================] - 5s 46ms/step - loss: 0.3913 - accuracy: 0.8723 - val_loss: 0.3623 - val_accuracy: 0.8931
Epoch 9/25
105/105 [==============================] - 5s
... [Output truncated for brevity]
```

<a name='3-2'></a>

## 3.2 Visualizing the Results

Plotting the model results...

```python
plot_acc_loss(history)
```

There is not a much difference with the former, but the results that we get by combining Convnets and RNNs are away good than using RNNs only. And in addition to that, it is cheaper to train it.

For now, let's test our later network on new texts.

<a name='3-3'></a>

## 3.3 Performing Inference on New Texts

```python
def predict(model, sample_news, class_names):

  # Convert sample news into array

  sample_news = np.array(sample_news)

  # Predict the news type

  preds = model.predict(sample_news)

  pred_class = np.argmax(preds[0])

  print(f'predicted class: {pred_class} \nPredicted Class name: {class_names[pred_class]}')
```

```python
sample_news = ['Tesla, a self driving car company is also planning to make a humanoid robot. This humanoid robot appeared dancing in the latest Tesla AI day']

predict(conv_rnn_model, sample_news, class_names)
```

**Execution Output:**
```text
predicted class: 3 
Predicted Class name: Sci/Tech
```

```python
sample_news = ["In the last weeks, there has been many transfer suprises in footbal. Ronaldo went back to Old Trafford, "
                "while Messi went to Paris Saint Germain to join his former colleague Neymar."
                "We can't wait to see these two clubs will perform in upcoming leagues"]
            

predict(conv_rnn_model, sample_news, class_names)
```

**Execution Output:**
```text
predicted class: 1 
Predicted Class name: Sports
```

```python
sample_news = ["In the latest business news: The tech giant NVIDIA has acquired ARM, a microproccessor company"]
            

predict(conv_rnn_model, sample_news, class_names)
```

**Execution Output:**
```text
predicted class: 2 
Predicted Class name: Business
```

<a name='4'></a>

# 4.  Further Learning

This notebook has been about using Convnets for text classification. We also brought RNNs into the picture. 

If you would like to learn more about sequence models, I recommend the following courses:

* Deep Learning Specialization - Course 5 of Sequence models. This course is available on [Coursera](https://www.coursera.org/learn/nlp-sequence-models) and [Youtube](https://www.youtube.com/watch?v=_i3aqgKVNQI&list=PLkDaE6sCZn6F6wUI9tvS_Gw1vaFAx6rd6). 
* Intro to Deep Learning MIT - Lecture 2 of Recurrent Neural Networks, available on [Youtube](https://www.youtube.com/watch?v=qjrad0V0uJE&t=168s). 

For ConvNets and RNNs, I recommend the following two papers:

* [Text Classification from Scratch(Yann LeCun, Xiang Zhang, 2016)](https://arxiv.org/pdf/1502.01710.pdf)
* [Recurrent Convolutional Neural Networks for Text Classification(Siwei Lai, Liheng Xu, Kang Liu, Jun Zhao)](https://www.aaai.org/ocs/index.php/AAAI/AAAI15/paper/view/9745/9552)

## [BACK TO TOP](#0)

---

## 5. Fine-Tuning Pretrained BERT for Text Classification

<table align="left">
  <td>
    <a href="https://colab.research.google.com/github/nyandwi/machine_learning_complete/blob/main/9_nlp_with_tensorflow/5_using_pretrained_bert_for_text_classification.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
  </td>
</table>

*This notebook was created by [Jean de Dieu Nyandwi](https://twitter.com/jeande_d) for the love of machine learning community. For any feedback, errors or suggestion, he can be reached on email (johnjw7084 at gmail dot com), [Twitter](https://twitter.com/jeande_d), or [LinkedIn](https://linkedin.com/in/nyandwi).*

<a name='0'></a>
# Using Pretrained BERT for Text Classification

## Contents 

* [1. Intro to BERT](#1)
* [2. In Practice: Finetuning a Pretrained BERT](#2)
   * [2.1 Getting the data](#2-1)
   * [2.2 Preparing the data](#2-2)
   * [2.3 Getting the BERT and its preprocesing model from TensorFlow Hub](#2-3)
   * [2.4 Building a news classifier](#2-4)
   * [2.5 Training a finetuned BERT model](#2-4)
   * [2.6 Visualizing the model results](#2-4)
   * [2.7 Performing the inference on new texts](#2-4)

* [3. Futher learning](#3)

<a name='1'></a>
## 1. Intro to BERT

BERT stands for Bidirectional Encoder Representations from Transformers. It is one of the recent state of the art language models that can be used for variety of tasks such as question answering, text classification, machine translation and so forth. 

As it sounds and hence the name, BERT is based on Transformers. Transformers are a neural network type architecture that uses attention mechanisms([Attention is All you Need](https://arxiv.org/pdf/1706.03762.pdf))

BERT is deeply bidirectional: it captures the full context of the input text (converted to tokens) from both directions. The traditional language models (e.g [Word2vec](https://arxiv.org/abs/1301.3781)) are undirectional and thus, they don't take into account the context of each occurence of a given word. 

To quote its [paper](https://arxiv.org/pdf/1810.04805.pdf), BERT also uses a `next word prediction` task that jointly pretrains text-pair representations.

TensorFlow Hub contains many version of [BERT](https://tfhub.dev/google/collections/bert/1) such as: [Small BERT](https://tfhub.dev/google/collections/bert/1), [Albert](https://tfhub.dev/google/collections/albert/1), [Electra](https://tfhub.dev/google/collections/albert/1), [BERT Expert](https://tfhub.dev/google/collections/experts/bert/1).

<a name='2'></a>

## 2. In Practice: Finetuning a Pretrained BERT

We are going to use `ag_news_subset` dataset that is available in [TensorFlow datasets](https://www.tensorflow.org/datasets/catalog/ag_news_subset). TensorFlow datasets is a collection of awesome datasets that can be used right away with little preparations. 

AG is a collection of more than 1 million news articles gathered from more than 2000 news sources by ComeToMyHead in more than 1 year of activity. 

The AG dataset contains 4 classes that are: World(0), Sports(1), Business(2), Sci/Tech(3). The total number of training samples is 120,000 and testing 7,600. Each class contains 30,000 training samples and 1,900 testing samples. 

You can learn more about the dataset [here](http://groups.di.unipi.it/~gulli/AG_corpus_of_news_articles.html).


Let's get the dataset from TensorFlow datasets.

<a name='2-1'></a>

## 2.1 Getting the Data

#### Imports

```python
import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
import matplotlib.pyplot as plt
import tensorflow_hub as hub
```

The dataset that we are going to download has only one version so far. Let's specify it so that when it is updated, our lab will not be affected. If loading the data fails, run the cell again. It happens sometime when loading datasets from TF datasets.

```python
(train_data, val_data), info = tfds.load('ag_news_subset:1.0.0', #version 1.0.0
                                         split=('train', 'test'),
                                         with_info=True, 
                                         as_supervised=True)
```

**Execution Output:**
```text
[1mDownloading and preparing dataset ag_news_subset/1.0.0 (download: 11.24 MiB, generated: 35.79 MiB, total: 47.03 MiB) to /root/tensorflow_datasets/ag_news_subset/1.0.0...[0m



Shuffling and writing examples to /root/tensorflow_datasets/ag_news_subset/1.0.0.incompleteIWSQ9J/ag_news_subset-train.tfrecord
Shuffling and writing examples to /root/tensorflow_datasets/ag_news_subset/1.0.0.incompleteIWSQ9J/ag_news_subset-test.tfrecord
[1mDataset ag_news_subset downloaded and prepared to /root/tensorflow_datasets/ag_news_subset/1.0.0. Subsequent calls will reuse this data.[0m
```

Now that we have the data, we can look into some examples. This is always a good practice. 

Printing `info` that we loaded with the dataset, we can see pretty much everything we would need to know about the data.

```python
print(info)
```

**Execution Output:**
```text
tfds.core.DatasetInfo(
    name='ag_news_subset',
    version=1.0.0,
    description='AG is a collection of more than 1 million news articles.
News articles have been gathered from more than 2000  news sources by ComeToMyHead in more than 1 year of activity.
ComeToMyHead is an academic news search engine which has been running since July, 2004.
The dataset is provided by the academic comunity for research purposes in data mining (clustering, classification, etc),
information retrieval (ranking, search, etc), xml, data compression, data streaming,
and any other non-commercial activity.
For more information, please refer to the link http://www.di.unipi.it/~gulli/AG_corpus_of_news_articles.html .

The AG's news topic classification dataset is constructed by Xiang Zhang (xiang.zhang@nyu.edu) from the dataset above.
It is used as a text classification benchmark in the following paper:
Xiang Zhang, Junbo Zhao, Yann LeCun. Character-level Convolutional Networks for Text Classification. Advances in Neural Information Processing Systems 28 (NIPS 2015).

The AG's news topic classification dataset is constructed by choosing 4 largest classes from the original corpus.
Each class contains 30,00
... [Output truncated for brevity]
```

```python
# Displaying the classes

class_names = info.features['label'].names
num_classes = info.features['label'].num_classes

print(f'The news are grouped into {num_classes} classes that are :{class_names}')
```

**Execution Output:**
```text
The news are grouped into 4 classes that are :['World', 'Sports', 'Business', 'Sci/Tech']
```

```python
num_train = info.splits['train'].num_examples
num_val = info.splits['test'].num_examples

print(f'The number of training samples: {num_train} \nThe number of validation samples: {num_val}')
```

**Execution Output:**
```text
The number of training samples: 120000 
The number of validation samples: 7600
```

We can also display the first 10 news samples. We can use [`tfds.as_dataframe`](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe) to display them as dataframe.

```python
news_df = tfds.as_dataframe(train_data.take(10), info)

news_df.head(10)
```

**Execution Output:**
```text
description  label
0  b'AMD #39;s new dual-core Opteron chip is desi...      3
1  b'Reuters - Major League Baseball\\Monday anno...      1
2  b'President Bush #39;s  quot;revenue-neutral q...      2
3  b'Britain will run out of leading scientists u...      3
4  b'London, England (Sports Network) - England m...      1
5  b'TOKYO - Sony Corp. is banking on the \\$3 bi...      0
6  b'Giant pandas may well prefer bamboo to lapto...      3
7  b'VILNIUS, Lithuania - Lithuania #39;s main pa...      0
8  b'Witnesses in the trial of a US soldier charg...      0
9  b'Dan Olsen of Ponte Vedra Beach, Fla., shot a...      1
```

Let's display some full news.

```python
for i in range (0,4):

  print(f"Sample news {i}\n \
  Label: {news_df['label'][i]} {(class_names[i])}\n \
  Description: {news_df['description'][i]}\n----------\n")
```

**Execution Output:**
```text
Sample news 0
   Label: 3 World
   Description: b'AMD #39;s new dual-core Opteron chip is designed mainly for corporate computing applications, including databases, Web services, and financial transactions.'
----------

Sample news 1
   Label: 1 Sports
   Description: b'Reuters - Major League Baseball\\Monday announced a decision on the appeal filed by Chicago Cubs\\pitcher Kerry Wood regarding a suspension stemming from an\\incident earlier this season.'
----------

Sample news 2
   Label: 2 Business
   Description: b'President Bush #39;s  quot;revenue-neutral quot; tax reform needs losers to balance its winners, and people claiming the federal deduction for state and local taxes may be in administration planners #39; sights, news reports say.'
----------

Sample news 3
   Label: 3 Sci/Tech
   Description: b'Britain will run out of leading scientists unless science education is improved, says Professor Colin Pillinger.'
----------
```

```python
news_df.columns
```

**Execution Output:**
```text
Index(['description', 'label'], dtype='object')
```

Now that we understand the data, let's prepare it before we can use LSTMs to classify the news.

<a name='2-2'></a>

## 2.2 Preparing the Data

For this practice of using a pretrained BERT, we will not need to vectorize the data. We will feed the sentences directly to the model. 

Let's just only shuffle and batch the training data. For validation data, we don't shuffle. We only batch it.

```python
buffer_size = 1000
batch_size = 32

train_data = train_data.shuffle(buffer_size)
train_data = train_data.batch(batch_size).prefetch(1)
val_data = val_data.batch(batch_size).prefetch(1)
```

```python
for news, label in train_data.take(1):

  print(f'Sample news\n----\n {news.numpy()[:4]} \n----\nCorresponding labels: {label.numpy()[:4]}')
```

**Execution Output:**
```text
Sample news
----
 [b'RAMALLAH: Palestinian leader Yasser Arafat is  quot;very, very sick quot; and the ex-guerrilla who for decades symbolised a struggle for statehood is slipping in and out of consciousness, officials and medics said today.'
 b'AOL said it was intent on making travel an important part of its content expansion, which increasingly includes general Web properties that all Internet users can access as well as content just '
 b'AP - WHAT WAS FOUND: A microscopic diamond embedded in kimberlite, the molten rock in which diamonds are found, in Montana.'
 b'The US military in Iraq has denied reports that the former Iraqi leader Saddam Hussein is on hunger strike. But a spokesman told the BBC that some of his former aides who are also in custody, including  quot;Chemical '] 
----
Corresponding labels: [0 2 3 0]
```

<a name='2-3'></a>

## 2.3 Getting the BERT Model and its Preprocessing Model from TF Hub

There many versions of BERT that are optimized for different use cases. The choice of a given version is going to depend on computation time & speed, accuracy, and the size of that particular BERT version. 

For our case, we can use [SmallBERT](https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3). It is also worth mentioning that each BERT model has its preprocessing model that will convert the texts into tokens. The BERT models and their corresponding preprocesing models are pretty detailed on [TensorFlow Hub BERT models page](https://tfhub.dev/google/collections/bert/1).

The preprocessing model use [TensorFlow Text](https://www.tensorflow.org/text) operations. We have to install it.

```python
!pip install tensorflow_text
import tensorflow_text as text
```

**Execution Output:**
```text
Collecting tensorflow_text
  Downloading tensorflow_text-2.6.0-cp37-cp37m-manylinux1_x86_64.whl (4.4 MB)
[K     |████████████████████████████████| 4.4 MB 5.1 MB/s 
[?25hRequirement already satisfied: tensorflow-hub>=0.8.0 in /usr/local/lib/python3.7/dist-packages (from tensorflow_text) (0.12.0)
Requirement already satisfied: tensorflow<2.7,>=2.6.0 in /usr/local/lib/python3.7/dist-packages (from tensorflow_text) (2.6.0)
Requirement already satisfied: clang~=5.0 in /usr/local/lib/python3.7/dist-packages (from tensorflow<2.7,>=2.6.0->tensorflow_text) (5.0)
Requirement already satisfied: absl-py~=0.10 in /usr/local/lib/python3.7/dist-packages (from tensorflow<2.7,>=2.6.0->tensorflow_text) (0.12.0)
Requirement already satisfied: google-pasta~=0.2 in /usr/local/lib/python3.7/dist-packages (from tensorflow<2.7,>=2.6.0->tensorflow_text) (0.2.0)
Requirement already satisfied: flatbuffers~=1.12.0 in /usr/local/lib/python3.7/dist-packages (from tensorflow<2.7,>=2.6.0->tensorflow_text) (1.12)
Requirement already satisfied: termcolor~=1.1.0 in /usr/local/lib/python3.7/dist-packages (from tensorflow<2.7,>=2.6.0->tensorflow_text) (1.1.0)
Requirement already satisfied: six~=1.15.0 in /usr/local/
... [Output truncated for brevity]
```

```python
bert_handle = 'https://tfhub.dev/tensorflow/small_bert/bert_en_uncased_L-4_H-512_A-8/2'
preprocessing_model = 'https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3'
```

Let's wrap `preprocessing_model` into a [KerasLayer](https://www.tensorflow.org/hub/api_docs/python/hub/KerasLayer) and test it on some sample sentences.

```python
preprocess_layer = hub.KerasLayer(preprocessing_model)
```

The output of [preprocess model](https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3) is made of 3 elements or keys that are:   `input_word_ids`, `input_mask`, `input_type_ids`. Here are what they mean.

* `input_word_ids`: has the token ids of the input sequences.
* `input_mask`: has value 1 at the position of all input tokens present before padding and value 0 for the padding tokens.

* `input_type_ids`: has the index of the input segment that gave rise to the input token at the respective position. The first input segment (index 0) includes the start-of-sequence token and its end-of-segment token. The second segment (index 1, if present) includes its end-of-segment token. Padding tokens get index 0 again.

Source: [TF Hub doc](https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3).

```python
sample_news = ['Tech rumors: The tech giant Apple is working on its self driving car']

preprocessed_news = preprocess_layer(sample_news)

print(f'Keys       : {list(preprocessed_news.keys())}')
print(f'Shape      : {preprocessed_news["input_word_ids"].shape}')
print(f'Word Ids   : {preprocessed_news["input_word_ids"][0, :5]}')
print(f'Input Mask : {preprocessed_news["input_mask"][0, :5]}')
print(f'Type Ids   : {preprocessed_news["input_type_ids"][0, :5]}')
```

**Execution Output:**
```text
Keys       : ['input_mask', 'input_word_ids', 'input_type_ids']
Shape      : (1, 128)
Word Ids   : [  101  6627 11256  1024  1996]
Input Mask : [1 1 1 1 1]
Type Ids   : [0 0 0 0 0]
```

We can also see what kinds of the output the BERT model will give if we feed it the preprocessed texts. 

The bert model expect 3 input tensors: `input_word_ids`, `input_mask`, `input_type_ids`.

```python
bert_model = hub.KerasLayer(bert_handle)
```

The `bert_model` returns 2 main keys: `pooled_output`, `sequence_output`. 

Here are what they mean:

* `pooled_output` represents the  input sequence.
* `sequence_output` denotes each input token in the context. 

Any of those keys can be used as input to the rest of the model. We will see that later.

```python
bert_outputs = bert_model(preprocessed_news)

print(f'Pooled output shape:{bert_outputs["pooled_output"].shape}')
print(f'Pooled output values:{bert_outputs["pooled_output"][0, :5]}')
print(f'Sequence output shape:{bert_outputs["sequence_output"].shape}')
print(f'Sequence output values:{bert_outputs["sequence_output"][0, :5]}')
```

**Execution Output:**
```text
Pooled output shape:(1, 512)
Pooled output values:[ 0.944598    0.9861868  -0.15102872  0.17372097 -0.6424564 ]
Sequence output shape:(1, 128, 512)
Sequence output values:[[-0.60826176  0.2623035   1.2436793  ... -0.8821719   0.36095393
  -0.00184657]
 [ 0.33820462  0.07993765  1.1374032  ... -1.6438915  -1.0649079
  -0.7371688 ]
 [-0.6054905  -0.14994524  0.8464851  ... -0.74730563  0.84758896
   0.13153419]
 [ 0.06868989  0.6969774   1.5265335  ... -0.7680908  -0.30986136
   0.25017208]
 [-1.2314899   1.4334055  -0.37746784 ... -1.3110946  -0.01984588
   0.7904873 ]]
```

Now that we understand what the ins and outs of [bert model](https://tfhub.dev/tensorflow/small_bert/bert_en_uncased_L-4_H-512_A-8/2) and its [preprocessor](https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3), let's build the rest of the model.

<a name='2-4'></a>

## 2.4 Building a News Classifier with BERT

Since the main purpose of this practice it to finetune BERT, we are going to add few more layers to it. 

We will add dropout for regularization, and dense layers for classification purpose. 

We have been using [Keras Sequential API](https://www.tensorflow.org/api_docs/python/tf/keras/Sequential). There is also a Functional API. This API type make it easy to build flexible models where you can arrange layers in a way you want. Also, Functional API is a suitable API type for the models that take multiple inputs and outputs.

```python
input_text = tf.keras.layers.Input(shape=(), dtype=tf.string, name='Input')

# A preprocesing model before layer BERT
preprocessing_layer = hub.KerasLayer(preprocessing_model, name='preprocessing_layer')

bert_input = preprocessing_layer(input_text)

# Getting a Bert model, set trainable to True
bert_encoder = hub.KerasLayer(bert_handle, trainable=True, name='bert_encoder')

bert_outputs = bert_encoder(bert_input)

# For finetuning, we take pooled_output
pooled_bert_output = bert_outputs['pooled_output']

# Adding a dense layer 

dense_net = tf.keras.layers.Dense(16, activation='relu', name='fully_connected_layer')(pooled_bert_output)
# Add dropout layer for regularization
dense_net = tf.keras.layers.Dropout(0.2)(dense_net)

# Last dense layer for classification purpose
final_output = tf.keras.layers.Dense(4, activation='softmax', name='classifier')(dense_net)

# Combine input and output

news_classifier = tf.keras.Model(input_text, final_output)
```

We can display the model summary.

```python
news_classifier.summary()
```

**Execution Output:**
```text
Model: "model"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
Input (InputLayer)              [(None,)]            0                                            
__________________________________________________________________________________________________
preprocessing_layer (KerasLayer {'input_word_ids': ( 0           Input[0][0]                      
__________________________________________________________________________________________________
bert_encoder (KerasLayer)       {'encoder_outputs':  28763649    preprocessing_layer[0][0]        
                                                                 preprocessing_layer[0][1]        
                                                                 preprocessing_layer[0][2]        
__________________________________________________________________________________________________
fully_connected_layer (Dense)   (None, 16)           8208        bert_encoder[0][5]             
... [Output truncated for brevity]
```

Or plot it with `tf.keras.utils.plot_model()`

```python
tf.keras.utils.plot_model(news_classifier, rankdir='LR', dpi=120)
```

**Execution Output:**
```text
<IPython.core.display.Image object>
```

We can change the model plot orientation by setting the `rankdir` to either `TB` (top-bottom) or `LR` (left-right).

```python
tf.keras.utils.plot_model(news_classifier, rankdir='TB', dpi=120)
```

**Execution Output:**
```text
<IPython.core.display.Image object>
```

<a name='2-5'></a>

## 2.5 Training a Finetuned BERT

Before training a model, we have to compile it. When compiling the model, we specify the loss and optimization function. 

Loss function is there to measure how far the predictions are from the actual outputs, and optimizer to reduce the loss.

```python
news_classifier.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=3e-5), 
                        loss='sparse_categorical_crossentropy', 
                        metrics=['accuracy'])
```

```python
# Train the model

batch_size = 32

train_steps = int(len(train_data)/batch_size)
val_steps = int(len(val_data)/batch_size)

history = news_classifier.fit(train_data, 
                    epochs=15,
                    validation_data=val_data,
                    steps_per_epoch=train_steps,
                    validation_steps=val_steps
)
```

**Execution Output:**
```text
Epoch 1/15
117/117 [==============================] - 872s 7s/step - loss: 0.9071 - accuracy: 0.5710 - val_loss: 0.7042 - val_accuracy: 0.6205
Epoch 2/15
117/117 [==============================] - 865s 7s/step - loss: 0.6153 - accuracy: 0.7639 - val_loss: 0.4422 - val_accuracy: 0.8839
Epoch 3/15
117/117 [==============================] - 867s 7s/step - loss: 0.4662 - accuracy: 0.8288 - val_loss: 0.3497 - val_accuracy: 0.8929
Epoch 4/15
117/117 [==============================] - 865s 7s/step - loss: 0.4057 - accuracy: 0.8632 - val_loss: 0.3616 - val_accuracy: 0.8973
Epoch 5/15
117/117 [==============================] - 866s 7s/step - loss: 0.3775 - accuracy: 0.8659 - val_loss: 0.3295 - val_accuracy: 0.9107
Epoch 6/15
117/117 [==============================] - 863s 7s/step - loss: 0.3795 - accuracy: 0.8657 - val_loss: 0.3112 - val_accuracy: 0.9062
Epoch 7/15
117/117 [==============================] - 859s 7s/step - loss: 0.3613 - accuracy: 0.8707 - val_loss: 0.3071 - val_accuracy: 0.9107
Epoch 8/15
117/117 [==============================] - 862s 7s/step - loss: 0.3399 - accuracy: 0.8835 - val_loss: 0.3287 - val_accuracy: 0.9107
Epoch 9/15
117/117 [==============================] - 85
... [Output truncated for brevity]
```

<a name='2-6'></a>

## 2.6 Visualizing the Model Results

It is always a good practice to plot the model results. When doing error analysis, plotting learning curve becomes helpful. 

Let's plot the loss and accuracy over on the course of epochs.

```python
# function to plot accuracy and loss

def plot_acc_loss(history):

  model_history = history.history
  acc = model_history['accuracy']
  val_acc = model_history['val_accuracy']
  loss = model_history['loss']
  val_loss = model_history['val_loss']
  epochs = history.epoch

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
plot_acc_loss(history)
```

Looking on the learning curve, we could have trained the model for fewer epochs, like 9 or 10 because after 9, there seems to be no improvements.

<a name='2-7'></a>

## 2.7 Performing Inference on New Texts

```python
def predict(model, sample_news, class_names):

  # Convert sample news into array

  sample_news = np.array(sample_news)

  # Predict the news type

  preds = model.predict(sample_news)

  pred_class = np.argmax(preds[0])

  print(f'predicted class: {pred_class} \nPredicted Class name: {class_names[pred_class]}')
```

```python
sample_news = ['Tesla, a self driving car company is also planning to make a humanoid robot. This humanoid robot appeared dancing in the latest Tesla AI day']

predict(news_classifier, sample_news, class_names)
```

**Execution Output:**
```text
predicted class: 3 
Predicted Class name: Sci/Tech
```

```python
sample_news = ["In the last weeks, there has been many transfer suprises in footbal. Ronaldo went back to Old Trafford, "
                "while Messi went to Paris Saint Germain to join his former colleague Neymar."
                "We can't wait to see these two clubs will perform in upcoming leagues"]
            

predict(news_classifier, sample_news, class_names)
```

**Execution Output:**
```text
predicted class: 1 
Predicted Class name: Sports
```

```python
sample_news = ["In the latest tech news: The tech giant NVIDIA has acquired ARM, a microproccessor company"]
            

predict(news_classifier, sample_news, class_names)
```

**Execution Output:**
```text
predicted class: 3 
Predicted Class name: Sci/Tech
```

```python
sample_news = ["Salesforce reported making over 1B sales in last quarter"]
            

predict(news_classifier, sample_news, class_names)
```

**Execution Output:**
```text
predicted class: 2 
Predicted Class name: Business
```

<a name='3'></a>

# 3. Further Learning

We have learned about BERT (Bidirectional Encoder Representation Transformer) and how to finetune it to model basic NLP tasks such as text classification. 

If you would like to learn more about BERT and Text Classification, here are resources to use:

* [TensorFlow official text classification with BERT tutorial](https://tfhub.dev/google/collections/bert/1)
* [BERT: Pre-training of Deep Bidirectional Transformers for
Language Understanding](https://arxiv.org/pdf/1810.04805.pdf)
* [BERT Models in TensorFlow Hub](https://www.tensorflow.org/text/tutorials/classify_text_with_bert)

## [BACK TO TOP](#0)

---

## Key Interview Concepts & Architecture Comparisons

### 1. RNN vs LSTM vs GRU Internal Mechanics
- **SimpleRNN**:
  $$h_t = \tanh(W_{hh} h_{t-1} + W_{xh} x_t + b_h)$$
  Suffers severely from the **Vanishing Gradient Problem** over long sequences because gradients backpropagated through time are repeatedly multiplied by weight matrices, causing exponential decay toward zero.
- **LSTM (Long Short-Term Memory)**:
  Maintains an internal cell state $C_t$ governed by three gates:
  1. **Forget Gate**: $f_t = \sigma(W_f [h_{t-1}, x_t] + b_f)$ (decides what information to discard from cell state).
  2. **Input Gate**: $i_t = \sigma(W_i [h_{t-1}, x_t] + b_i)$ and $\tilde{C}_t = \tanh(W_c [h_{t-1}, x_t] + b_c)$ (decides what new candidate info to store).
  3. **Cell State Update**: $C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$.
  4. **Output Gate**: $o_t = \sigma(W_o [h_{t-1}, x_t] + b_o)$ and $h_t = o_t \odot \tanh(C_t)$.
- **GRU (Gated Recurrent Unit)**:
  Simplifies LSTM by combining cell state and hidden state, using only two gates: **Reset Gate** $r_t$ and **Update Gate** $z_t$. Fewer parameters and faster training.

### 2. Why Conv1D for Text?
- Uses 1-dimensional filters sliding across word sequences.
- Extracts local n-gram patterns (e.g., filter size 3 captures trigrams, filter size 5 captures 5-grams) invariant of position.
- Computationally parallelizable on GPUs unlike sequential RNN loops.

### 3. BERT (Bidirectional Encoder Representations from Transformers)
- Unlike traditional left-to-right language models or unidirectional LSTMs, BERT conditions on both left and right context in all layers simultaneously using self-attention.
- Pretrained on **Masked Language Modeling (MLM)** (predicting 15% randomly masked tokens) and **Next Sentence Prediction (NSP)**.
- Can be fine-tuned with just one additional classification layer on top of the `[CLS]` token output.
