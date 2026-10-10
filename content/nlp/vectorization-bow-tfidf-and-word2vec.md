# Vectorization: Bag of Words, N-Grams, TF-IDF & Word2Vec

Understand statistical and neural text representation: CountVectorizer, N-Gram language modeling, Term Frequency-Inverse Document Frequency (TF-IDF) mathematics, Cosine Similarity, and Word2Vec embeddings (CBOW vs Skip-Gram).

---

## 1. Bag of Words (BoW) & N-Gram Modeling

# 09 Bag Of Words and N-Grams

## **Bag Of Words**

- Bag of words is a Natural Language Processing technique of **text modelling**. In technical terms, we can say that it is a method of **feature extraction** with text data. This approach is a simple and flexible way of extracting features from documents.

- A bag of words is a representation of text that describes the occurrence of words within a document. We just keep track of word counts and **disregard the grammatical details and the word order**.
-  It is **called a “bag”** of words because any information about the order or structure of words in the document is discarded.
- The model is only concerned with whether known words occur in the document, not where in the document.

### **Why is the Bag-of-Words algorithm used?**
-  The dataset is **messy and unstructured and not fixed-length inputs**, and machine learning algorithms prefer **structured, well defined fixed-length inputs** and by using the Bag-of-Words technique we can convert variable-length texts into a fixed-length vector.

- The machine learning models work with **numerical data** rather than textual data. By using the bag-of-words (BoW) technique, we convert a text into its equivalent **vector of numbers**.

Sentence 1: ”The Cat sat here” 

Sentence 2: “The Cat sat in the hat” 

Sentence 2: “The Cat is with the hat”

**Step 1:** Convert the above sentences in lower case as the case of the word does not hold any information.

**Step 2:** Remove special characters and stopwords from the text.

After applying the above steps, the sentences are changed to

Sentence 1: ”the cat sat” 

Sentence 2: “the cat sat in the hat” 

Sentence 2: “the cat with the hat”

Although the above sentences do not make much sense the maximum information is contained in these words only.

**Step 3:** Go through all the words in the above text and make a list of all of the words in our model vocabulary.
- ["the", "cat", "sat","in","hat","with"]

Now as the vocabulary has only 6 words, we can use a fixed-length document-representation of 6, with one position in the vector to score each word. 

Sentence 1: [1,1,1,0,0,0] 

Sentence 2: [2,1,1,1,1,0] 

Sentence 2: [2,1,0,0,1,1]

<img src = "https://miro.medium.com/max/1400/1*3IACMnNpwVlCl8kSTJocPA.png"></img>


Disadvantages
- In bag of words we consider all words as same weighted.
ex : His brother is good.
here GOOD is highly weighted word and brother is less weighted. In Bag of word we consider all words as same weighted.
- It disregard the grammatical details and the word order when storing words.

##  **CountVectorizer** 
Used to count the number of words present in a sentence.

```python
!pip install sklearn

from sklearn.feature_extraction.text import CountVectorizer
# list of text documents
text = ["The quick brown fox jumped over the lazy dog."]
```

**Execution Output:**
```text
Requirement already satisfied: sklearn in /srv/conda/envs/notebook/lib/python3.7/site-packages (0.0)
Requirement already satisfied: scikit-learn in /srv/conda/envs/notebook/lib/python3.7/site-packages (from sklearn) (1.0.1)
Requirement already satisfied: joblib>=0.11 in /srv/conda/envs/notebook/lib/python3.7/site-packages (from scikit-learn->sklearn) (1.1.0)
Requirement already satisfied: numpy>=1.14.6 in /srv/conda/envs/notebook/lib/python3.7/site-packages (from scikit-learn->sklearn) (1.21.4)
Requirement already satisfied: scipy>=1.1.0 in /srv/conda/envs/notebook/lib/python3.7/site-packages (from scikit-learn->sklearn) (1.7.2)
Requirement already satisfied: threadpoolctl>=2.0.0 in /srv/conda/envs/notebook/lib/python3.7/site-packages (from scikit-learn->sklearn) (3.0.0)
```

```python
# create the transform
vectorizer = CountVectorizer()
# tokenize and build vocab
vectorizer.fit(text)
# summarize
print(vectorizer.vocabulary_)
```

**Execution Output:**
```text
{'the': 7, 'quick': 6, 'brown': 0, 'fox': 2, 'jumped': 3, 'over': 5, 'lazy': 4, 'dog': 1}
```

```python
# encode document
vector = vectorizer.transform(text)
# summarize encoded vector
print(vector.shape)
print(type(vector))
print(vector.toarray())
```

**Execution Output:**
```text
(1, 8)
<class 'scipy.sparse.csr.csr_matrix'>
[[1 1 1 1 1 1 1 2]]
```

In above array, there is 2 in the end bcz "the" is present twice in that sentence.

```python
import numpy as np
import re

'''The first function we will implement is to extract the words from a document using regular expressions.
 As we do so, we will be converting all words to lower case and exclude our stop words.'''

def tokenize_sentences(sentences):
    words = []
    for sentence in sentences:
        w = extract_words(sentence)
        words.extend(w)
        
    words = sorted(list(set(words)))
    return words
```

```python
'''Next, we implement our tokenize_sentences function. This function builds our vocabulary by looping through
 all our documents (sentences), extracting the words from each, removing duplicates using the set function and 
 returning a sorted list of words.'''

def extract_words(sentence):
    ignore_words = ['a']
    words = re.sub("[^w]", " ",  sentence).split() #nltk.word_tokenize(sentence)
    words_cleaned = [w.lower() for w in words if w not in ignore_words]
    return words_cleaned
```

```python
def bagofwords(sentence, words):
    sentence_words = extract_words(sentence)
    # frequency word count
    bag = np.zeros(len(words))
    for sw in sentence_words:
        for i,word in enumerate(words):
            if word == sw: 
                bag[i] += 1
                
    return np.array(bag)
```

```python
'''Our last function is the implementation of the bag of words model. This function takes an input of a sentence 
and words (our vocabulary). It then extracts the words from the input sentence using the previously defined function. 
It creates a vector of zeros using numpy zeros function with a length of the number of words in our vocabulary.'''


sentences = ["Machine learning is great","Natural Language Processing is a complex field",
"Natural Language Processing is used in machine learning"]
```

```python
vocabulary = tokenize_sentences(sentences)
bagofwords("Machine learning is great", vocabulary)

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, stop_words = None, max_features = 5000) 

train_data_features = vectorizer.fit_transform(sentences)

vectorizer.transform(["Machine learning is great","Natural Language Processing is a complex field",
"Natural Language Processing is used in machine learning"]).toarray()
```

**Execution Output:**
```text
array([[0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
       [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
       [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]])
```

________________________________********************__________________________

## **Bag Of Words - KN**

```python
#!pip install ntlk

import nltk
nltk.download('popular')
```

**Execution Output:**
```text
True
```

```python
paragraph =  """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               strong not only as a military power but also as an economic power. Both must go hand-in-hand. 
               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of 
               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. 
               I see four milestones in my career"""
```

```python
# Cleaning the texts
import re # used for regular expression
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()
wordnet=WordNetLemmatizer()
sentences = nltk.sent_tokenize(paragraph)
corpus = []
for i in range(len(sentences)):

  # here we'll substitute or replace everything(i.e ',','/','\' etc.) except word containing a to z and A to Z ([^a-zA-Z]).
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])

    review = review.lower()
    review = review.split()
    
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500,ngram_range = (1,1))
# cv = CountVectorizer(max_features = 1500,ngram_range = (1,1),stop_words = 'english' )
X = cv.fit_transform(corpus).toarray()
```

```python
X
```

**Execution Output:**
```text
array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
        0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1,
        1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
        0, 0, 0, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
        0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
        1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0,
        0, 0, 0, 0, 
... [Output truncated for brevity]
```

# **What are N-Grams?**

**Sentence 1: “This is a good job. I will not miss it for anything”** 

**Sentence 2: ”This is not good at all”** 

For this example, let us take the vocabulary of 5 words only. The five words being- 
**[ good, job, miss, not, all ]** 

So, the respective vectors for these sentences are:

“This is a good job. I will not miss it for anything”= **[1,1,1,1,0]** 

”This is not good at all”= **[1,0,0,1,1]**

Can you guess what is the problem here? Sentence 2 is a negative sentence and sentence 1 is a positive sentence. Does this reflect in any way in the vectors above? Not at all. So how can we solve this problem? Here come the N-grams to our rescue.

- **An N-gram is an N-token sequence of words**: a 2-gram (more commonly called a **bigram**) is a two-word sequence of words like “really good”, “not good”, or “your homework”, and a 3-gram (more commonly called a **trigram**) is a three-word sequence of words like “not at all”, or “turn off light”.

For example, the bigrams in the first line of text in the previous section: “This is not good at all” are as follows:

“This is” 

“is not”  

“not good” 

“good at” 

“at all”

---

## 2. Term Frequency - Inverse Document Frequency (TF-IDF)

# 10 TF-IDF (Term Frequency-Inverse Document Frequency )

The scoring method being used above takes the count of each word and represents the word in the vector by the number of counts of that particular word. What does a word having high word count signify?

Does this mean that the word is important in retrieving information about documents? The answer is NO. Let me explain, if a word occurs many times in a document but also along with many other documents in our dataset, maybe it is because this word is just a frequent word; not because it is relevant or meaningful.One approach is to rescale the frequency of words
- **TF-IDF is a statistical measure that evaluates how relevant a word is to a document in a collection of documents.**

- **The term frequency (TF)** of a word in a document is number of times nth word  occurred in a document by total number of words in a document. 

- TF(i,j)=n(i,j)/Σ n(i,j)

n(i,j )= number of times nth word  occurred in a document

Σn(i,j) = total number of words in a document. 

- The **inverse document frequency(IDF)** of the word across a set of documents is logarithmic of total number of documents in the dataset by total number of documents in which nth word occur.

- IDF=1+log(N/dN)

N=Total number of documents in the dataset

dN=total number of documents in which nth word occur 

**NOTE:** The 1 added in the above formula is so that terms with zero IDF don’t get suppressed entirely.
 - if the word is very common and appears in many documents, this number will approach 0. Otherwise, it will approach 1.

 The TF-IDF is obtained by **TF-IDF=TF*IDF**

 ## **Limitations of Bag-of-Words**

1.  The model ignores the location information of the word. The location information is a piece of very important information in the text. For example  “today is off” and “Is today off”, have the exact same vector representation in the BoW model.
2. Bag of word models doesn’t respect the semantics of the word. For example, words ‘soccer’ and ‘football’ are often used in the same context. However, the vectors corresponding to these words are quite different in the bag of words model. The problem becomes more serious while modeling sentences. Ex: “Buy used cars” and “Purchase old automobiles” are represented by totally different vectors in the Bag-of-words model.
3. The range of vocabulary is a big issue faced by the Bag-of-Words model. For example, if the model comes across a new word it has not seen yet, rather we say a rare, but informative word like Biblioklept(means one who steals books). The BoW model will probably end up ignoring this word as this word has not been seen by the model yet.

```python
from sklearn.feature_extraction.text import CountVectorizer
# list of text documents
text = ["The car is driven on the road.","The truck is driven on the highway"]
```

```python
# create the transform
vectorizer = CountVectorizer()

# tokenize and build vocab
vectorizer.fit(text)
```

**Execution Output:**
```text
CountVectorizer()
```

```python
# summarize
print(vectorizer.vocabulary_)
```

**Execution Output:**
```text
{'the': 6, 'car': 0, 'is': 3, 'driven': 1, 'on': 4, 'road': 5, 'truck': 7, 'highway': 2}
```

```python
# encode document
newvector = vectorizer.transform(text)

# summarize encoded vector
print(newvector.toarray())
```

**Execution Output:**
```text
[[1 1 0 1 1 1 2 0]
 [0 1 1 1 1 0 2 1]]
```

# TF - IDF

```python
from sklearn.feature_extraction.text import TfidfVectorizer
# list of text documents
text = ["The car is driven on the road.","The truck is driven on the highway"]
```

```python
# create the transform
vectorizer = TfidfVectorizer()
```

```python
# tokenize and build vocab
vectorizer.fit(text)
```

**Execution Output:**
```text
TfidfVectorizer()
```

```python
#Focus on IDF VALUES
print(vectorizer.idf_)
```

**Execution Output:**
```text
[1.40546511 1.         1.40546511 1.         1.         1.40546511
 1.         1.40546511]
```

```python
# summarize
print(vectorizer.vocabulary_)
```

**Execution Output:**
```text
{'the': 6, 'car': 0, 'is': 3, 'driven': 1, 'on': 4, 'road': 5, 'truck': 7, 'highway': 2}
```

# **TF-IDF (KN)**

```python
# import nltk
# nltk.download('popular')
```

```python
import nltk

paragraph =  """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               I see four milestones in my career"""
               
               
# Cleaning the texts
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()
wordnet=WordNetLemmatizer()
sentences = nltk.sent_tokenize(paragraph)
corpus = []
for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])
    review = review.lower()
    review = review.split()
    review = [wordnet.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
```

```python
# Creating the TF-IDF model
from sklearn.feature_extraction.text import TfidfVectorizer
cv = TfidfVectorizer()
X = cv.fit_transform(corpus).toarray()
```

```python
X
```

**Execution Output:**
```text
array([[0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.57735027,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.57735027,
        0.        , 0.57735027, 0.        , 0.        ],
       [0.        , 0.        , 0.31622777, 0.        , 0.31622777,
        0.31622777, 0.        , 0.        , 0.31622777, 0.        ,
        0.31622777, 0.31622777, 0.        , 0.31622777, 0.        ,
        0.        , 0.31622777, 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.31622777, 0.31622777],
       [0.30151134, 0.30151134, 0.        , 0.30151134, 0.        ,
        0.        , 0.30151134, 0.30151134, 0.        , 0.        ,
        0.        , 0.        , 0.30151134, 0.        , 0.30151134,
        0.30151134, 0.        , 0.30151134, 0.30151134, 0.        ,
        0.30151134, 0.        , 0.        , 0.        ]])
```

---

## 3. Hands-On Text Classification with BoW, TF-IDF & Word2Vec

# EXERCISE:

1. List the differences between NLP and NLU.


- Natural language processing (NLP) seeks to convert unstructured language data into a structured data format to enable machines to understand speech and text and formulate relevant, contextual responses. Its subtopics include natural language processing and natural language generation.Natural language understanding (NLU) focuses on machine reading comprehension through grammar and context, enabling it to determine the intended meaning of a sentence.




- If we only talk about an understanding text, then NLU is enough.But if we want more than understanding, such as decision making, then NLP comes into play.

- NLU is a subset of NLP.	NLP is a combination of NLU and NLG for conversational Artificial Intelligence problems.

- It is not necessarily that what is written or said is meant to be the same. There can be flaws and mistakes. NLU makes sure that it will infer correct intent and meaning even data is spoken and written with some errors. It is the ability to understand the text. But, if we talk about NLP, it is about how the machine processes the given data. Such as make decisions, take actions, and respond to the system. It contains the whole End to End process. Every time NLP doesn't need to contain NLU.

- It reads data and converts it to structured data.	NLP converts unstructured data to structured data.

![image.png](attachment:image.png)

2. Which algorithm in NLP supports bidirectional context?

Only BERT (Bidirectional Encoder Representations from Transformers) provides a bidirectional context. The BERT model uses the previous and the next sentence to arrive at the context.Word2Vec and GloVe are word embeddings, they do not provide any context.

3. What is the significance of the Naive Bayes algorithm in NLP?

Naive Bayes are mostly used in natural language processing (NLP) problems. Naive Bayes predict the tag of a text. They calculate the probability of each tag for a given text and then output the tag with the highest one.It is Mostly used in text classification (due to better result in multi class problems and independence rule) have higher success rate as compared to other algorithms. As a result, it is widely used in Spam filtering (identify spam e-mail) and Sentiment Analysis (in social media analysis, to identify positive and negative customer sentiments)

4. List a few(5) libraries that you use for NLP in Python.

1. NLTK = Tokenization,Stemming etc
2. Spacy = multi trained transformers like BERT,Sentiment Analysis, POS
3. Textblob = Tokenization,N-Grams, Part-of-speech tagging
4. Pandas = Handling DataFrames
5. scikit-learn = Modeling like Naive Bayes.

6. What is n- gram model in NLP ?

Natural Language Processing, or NLP for short, n-grams are used for a variety of things. Some examples include auto completion of sentences (such as the one we see in Gmail these days), auto spell check (yes, we can do that as well), and to a certain extent, we can check for grammar in a given sentence.
A model that simply relies on how often a word occurs without looking at previous words is called unigram. If a model considers only the previous word to predict the current word, then it's called bigram. If two previous words are considered, then it's a trigram model.
An n-gram model for the above example would calculate the following probability:

P('There was heavy rain') = P('There', 'was', 'heavy', 'rain') = P('There')P('was'|'There')P('heavy'|'There was')P('rain'|'There was heavy')

Since it's impractical to calculate these conditional probabilities, using Markov assumption, we approximate this to a bigram model:

P('There was heavy rain') ~ P('There')P('was'|'There')P('heavy'|'was')P('rain'|'heavy')

7. What is sentence Embedder and give some example of it.

Suppose, we come across a sentence like ‘I don’t like crowded places’, and a few sentences later, we read ‘However, I like one of the world’s busiest cities, New York’.  How can we make the machine draw the inference between ‘crowded places’ and ‘busy cities’?

Clearly, word embedding would fall short here, and thus, we use Sentence Embedding. Sentence embedding techniques represent entire sentences and their semantic information as vectors. This helps the machine in understanding the context, intention, and other nuances in the entire text.

- TF-IDF
- Doc2Vec
- SentenceBERT

---

## Mathematical Formulation & Core Interview Questions

### 1. Term Frequency - Inverse Document Frequency (TF-IDF) Formula

$$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$

Where:
- **Term Frequency $\text{TF}(t, d)$**:
  $$\text{TF}(t, d) = \frac{\text{count of term } t \text{ in document } d}{\text{total number of words in document } d}$$
- **Inverse Document Frequency $\text{IDF}(t, D)$**:
  $$\text{IDF}(t, D) = \log \left( \frac{N}{n_t} \right) \quad \text{or with smoothing:} \quad \log \left( \frac{1 + N}{1 + n_t} \right) + 1$$
  - $N$ = total number of documents in corpus $D$.
  - $n_t$ = number of documents containing term $t$.

**Why compute IDF?**
Words like "the", "is", "and" appear in almost every document ($n_t \approx N$), so $\log(N/N) = \log(1) = 0$. Rare informative words (e.g. "hypoglycemia", "gradient", "transformer") have low $n_t$, yielding a high IDF weight.

### 2. Limitations of Bag of Words & TF-IDF
1. **Sparsity**: As vocabulary grows (e.g., 50,000 words), vectors become extremely high-dimensional and mostly zeros.
2. **Out of Vocabulary (OOV)**: Cannot represent unseen words during inference.
3. **Lack of Semantic Context**: "scary" and "spooky" are treated as orthogonal independent dimensions with zero dot-product similarity.
4. **Loss of Word Order**: "not bad, really good" and "not good, really bad" have identical bag-of-words representations.

### 3. Word2Vec: Distributed Dense Semantic Representations
- **Continuous Bag of Words (CBOW)**: Given surrounding context words $w_{t-2}, w_{t-1}, w_{t+1}, w_{t+2}$, predict center target word $w_t$. Faster to train, slightly better for frequent words.
- **Skip-Gram**: Given center target word $w_t$, predict surrounding context words. Excels on small datasets and rare words.
- **Semantic Vector Geometry**: Words with similar contexts map to neighboring vectors in continuous space:
  $$\vec{v}_{\text{King}} - \vec{v}_{\text{Man}} + \vec{v}_{\text{Woman}} \approx \vec{v}_{\text{Queen}}$$
