# NLP Foundations, Tokenization & Text Preprocessing

Master natural language processing fundamentals, tokenization mechanics (Prefixes, Infixes, Suffixes), Stopwords filtering, Stemming algorithms (Porter vs Snowball), and Lemmatization with SpaCy and NLTK.

---

## 1. Natural Language Processing Fundamentals

### Slide 1: Natural Language Processing



---

### Slide 2: Introduction

• Humans communicate with each other using words and text. The way that humans convey information to each other is called Natural Language. Every day humans share a large quality of information with each other in various languages as speech or text.

• However, computers cannot interpret this data, which is in natural language, as they communicate in 1s and 0s. The data produced is precious and can offer valuable insights. Hence, you need computers to be able to understand, emulate and respond intelligently to human speech.

• Natural Language Processing or NLP refers to the branch of Artificial Intelligence that gives the machines the ability to read, understand and derive meaning from human languages.

---

### Slide 3: Why is NLP important?



---

### Slide 4: Why do computers have difficulty with NLP?

• Computers have mostly been dealing with structured data. But Importantly, 80% of enterprise data is unstructured.

• Human languages are quite unlike the precise and unambiguous nature of computer languages.

• Human languages have plenty of complexities such as ambiguous phrases, colloquialisms, metaphors, puns, or sarcasms.

• The same word or text can have multiple meanings depending on the context.

• Language evolves with time. Worse still, we communicate imperfectly (spelling, grammar or punctuation errors) but still manage to be understood.

• Ambiguities in natural languages can be classified as lexical, syntactic or referential.

• When the source of information is speech, more challenges arise: accent, tone, loudness, background noise or context, pronunciation, emotional content, pauses, and so on​.

---

### Slide 5: Examples of the complexities of English?

• Contextual words and phrases and homonyms :

• For example:

• I ran to the store because we ran out of milk.

• The house is looking really run down.

• Irony and sarcasm:

• For example:

• sarcastic phrases, like “yeah right,” “whatever,” etc.

---

### Slide 6: Common NLP Tasks & Techniques

• Syntactic analysis, also known as parsing or syntax analysis, identifies the syntactic structure of a text and the dependency relationships between words, represented on a diagram called a parse tree.

• Semantic analysis focuses on identifying the meaning of language. Semantic tasks analyze the structure of sentences, word interactions, and related concepts, in an attempt to discover the meaning of words, as well as understand the topic of a text.

• Tokenization is an essential task in natural language processing used to break up a string of words into semantically useful units called tokens.

• Example: Customer service couldn’t be better! = “customer service” “could” “not” “be” “better”.

• Part-of-speech tagging (abbreviated as PoS tagging) involves adding a part of speech category to each token within a text. Some common PoS are verb, adjective, tags, noun, pronoun,conjunction, preposition, intersection, among others.

• Example: In above eg “Customer service”: NOUN, “could”: VERB, “not”: ADVERB, be”: VERB, “better”: ADJECTIVE, “!”: PUNCTUATION

• Word Sense Disambiguation

• You should read this book | You should book the flights | You should close the books by the end of the year.

• Techniques used - (WSD): knowledge-based (or dictionary approach) or supervised approach.

---

### Slide 7: Common NLP Tasks & Techniques

• Lemmatization & Stemming transform words back to their root form.

• The word as it appears in the dictionary – its root form – is called a lemma.

• E.g. of Lemmatization  African elephants have four nails on their front feet = “African,” “elephant,” “have,” “4”, “nail,” “on,” “their,” “foot”]

• E.g of Stemming the words “consult,” “consultant,” “consulting,” and “consultants” would result in the root form “consult.”

• While lemmatization is dictionary-based and chooses the appropriate lemma based on context, stemming operates on single words without considering the context.

• Stopword: Stop words are those words that do not contribute to the deeper meaning of the phrase. They are the most common words such as: the, a, & is.

• Named Entity Recognition (NER), involves extracting entities from within a text. Entities can be names, places, organizations, email addresses, and more.

• Relationship extraction, another sub-task of NLP, goes one step further and finds relationships between two nouns.

---

### Slide 8: Applications of NLP

• Email filters

• Quickly sorting customer feedback

• Predictive text and autocorrect

• Natural language generation

• Monitor brand sentiment on social media

• Online search engines

• Virtual assistants, voice assistants, or smart speakers

• Machine translation

• Chatbots

• Automatic summarization

---

### Slide 9: Overview



---

### Slide 10: Creating Features from Text

• The concepts of Bag-of-Words (BoW) and TF-IDF are techniques that help us convert text sentences into numeric vectors.

• Taking an Example:

• Sample reviews of a horror movie

• Review 1: This movie is very scary and long

• Review 2: This movie is not scary and is slow

• Review 3: This movie is spooky and good

• We cannot simply give these sentences to a machine learning model and ask it to tell us whether a review was positive or negative . Solution to it is creating vectors from text.

• Word Embedding is one such technique where we can represent the text using vectors. The more popular forms of word embeddings are:

• BoW, which stands for Bag of Words

• TF-IDF, which stands for Term Frequency-Inverse Document Frequency

• Word2vec

---

### Slide 11: Bag of Word (BoW) Model

• Simplest form of text representation in numbers

• Represent a sentence as a bag of words vector (a string of numbers)

• Example:

• Review 1: This movie is very scary and long

• Review 2: This movie is not scary and is slow

• Review 3: This movie is spooky and good

• Build a vocabulary from all the unique words in the above three reviews. The vocabulary consists of these 11 words: ‘This’, ‘movie’, ‘is’, ‘very’, ‘scary’, ‘and’, ‘long’, ‘not’,  ‘slow’, ‘spooky’,  ‘good’.

• We can now take each of these words and mark their occurrence in the three movie reviews above with 1s and 0s. This will give us 3 vectors for 3 reviews:

• Vector of Review 1: [1 1 1 1 1 1 1 0 0 0 0]

• Vector of Review 2: [1 1 2 0 0 1 1 0 1 0 0]

• Vector of Review 3: [1 1 1 0 0 0 1 0 0 1 1]

---

### Slide 12: Drawbacks of using a Bag-of-Words (BoW) Model

• If the new sentences contain new words, then our vocabulary size would increase and thereby, the length of the vectors would increase too.

• Additionally, the vectors would also contain many 0s, thereby resulting in a sparse matrix (which is what we would like to avoid)

• We are retaining no information on the grammar of the sentences nor on the ordering of the words in the text.

---

### Slide 13: Term Frequency-Inverse Document Frequency (TF-IDF)

• “Term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus.”

• Term Frequency (TF)

• It is a measure of how frequently a term, t, appears in a document, d:

• Here, in the numerator, n is the number of times the term “t” appears in the document “d”. Thus, each document and term would have its own TF value.

• E.g. Review 2: This movie is not scary and is slow

• Here,

• Vocabulary: ‘This’, ‘movie’, ‘is’, ‘very’, ‘scary’, ‘and’, ‘long’, ‘not’,  ‘slow’, ‘spooky’,  ‘good’

• Number of words in Review 2 = 8

• TF for the word ‘this’ = (number of times ‘this’ appears in review 2)/(number of terms in review 2) = 1/8

---

### Slide 14: Term Frequency-Inverse Document Frequency (TF-IDF)

• Inverse Document Frequency (IDF)

• IDF is a measure of how important a term is. We need the IDF value because computing just the TF alone is not sufficient to understand the importance of words:

• E.g.

• We can calculate the IDF values for the all the words in Review 2:

• IDF(‘this’) =  log(number of documents/number of documents containing the 	word ‘this’)

• = log(3/3) = log(1) = 0

• Hence, we see that words like “is”, “this”, “and”, etc., are reduced to 0 and have little importance; while words like “scary”, “long”, “good”, etc. are words with more importance and thus have a higher value.

---

### Slide 15: Term Frequency-Inverse Document Frequency (TF-IDF)

• We can now compute the TF-IDF score for each word in the corpus. Words with a higher score are more important, and those with a lower score are less important:

• Example:

• We can now calculate the

• TF-IDF score for every word in Review 2:

• TF-IDF(‘this’, Review 2) = TF(‘this’, Review 2) * IDF(‘this’) = 1/8 * 0 = 0

• TF-IDF also gives larger values for less frequent words and is high when both IDF and TF values are high i.e the word is rare in all the documents combined but frequent in a single document.

• While both Bag-of-Words and TF-IDF have been popular in their own regard, there still remained a void where understanding the context of words was concerned. Detecting the similarity between the words ‘spooky’ and ‘scary’, or translating our given documents into another language, requires a lot more information on the documents.

---

### Slide 16: Word2Vec

• Word2vec is a two-layer neural net that processes text by “vectorizing” words. Its input is a text corpus and its output is a set of vectors: feature vectors that represent words in that corpus.

• The Word2Vec objective function causes the words that have a similar context to have similar embeddings. Thus in this vector space, these words are really close.

• Mathematically, the cosine of the angle (Q) between such vectors should be close to 1, i.e. angle close to 0.

• As seen in the image below where word embeddings are plotted, similar meaning words are closer in space, indicating their semantic similarity.

---

### Slide 17: Word2Vec

• Two different model architectures that can be used by Word2Vec to create the word embeddings are the Continuous Bag of Words (CBOW) model & the Skip-Gram model.

• The CBOW architecture comprises a deep learning classification model in which we take in context words as input, X, and try to predict our target word, Y.

• In the skip-gram model, given a target (Centre) word, the context words are predicted.

---

### Slide 18: Intro to Language Modelling

• What is Language Modelling?

• Language model in NLP is a model that computes probability of a sentence( sequence of words) or the probability of a next word in a sequence.

• Language Model v/s Word Embedding

• Language models, word order matters because it tries to capture the context between words

• Words embeddings, only semantic similarity is captured because it is trained by predicting words in a window regardless of the order.

• Application of Language models

• Sentimental Analysis

• Question-Answering

• Summarization

• Machine Translation

• Speech recognition

---

### Slide 19: Language Modelling

• Making a Language model

• Using N-grams

• Using Neural Networks

• Using Long Short Term Memory Networks (LSTM)

• Evaluation of a Language model

• Perplexity is used to evaluate Language models. It is a measurement of how well a probability model predicts test data.

• Like the word ‘perplexed’, which means puzzled or confused, we measure how confused our model is, low perplexity means coherent/well-made sentences are generated by the model, whereas, high perplexity denotes incoherent and jumbled sentences. Therefore, low perplexity is good and high perplexity is bad.

---

### Slide 20: THANK YOU FOR YOURATTENTATION



---

## 2. Tokenization with SpaCy & NLTK

# 01 Tokenization by Python

- **Tokenization is a way of separating a piece of text into smaller units called tokens. Here, tokens can be either words, characters, or subwords.**
- **Tokenization is the act of breaking up a sequence of strings into pieces such as words, keywords, phrases, symbols and other elements called tokens. Tokens can be individual words, phrases or even whole sentences. In the process of tokenization, some characters like punctuation marks are discarded.**

```python
# Split by Whitespace

import re
text = "I\'ll always be there with you forever in your heart.!"
words = re.split(r'\W+', text)
print(words[:100])
```

**Execution Output:**
```text
['I', 'll', 'always', 'be', 'there', 'with', 'you', 'forever', 'in', 'your', 'heart', '']
```

Here It didn't recognise **`.`** at the last of the sentence.

**Remove punctuations and separate the word**

```python
import string
import re

# split into words by white space
words = text.split()

# prepare regex for char filtering
re_punc = re.compile('[%s]' % re.escape(string.punctuation))

# remove punctuation from each word
stripped = [re_punc.sub('', w) for w in words]
print(stripped[:100])
```

**Execution Output:**
```text
['Ill', 'always', 'be', 'there', 'with', 'you', 'forever', 'in', 'your', 'heart']
```

```python
# string.printable inverse of string.punctuation

re_print = re.compile('[^%s]' % re.escape(string.printable))
result = [re_print.sub('', w) for w in words]
print(result)
```

**Execution Output:**
```text
["I'll", 'always', 'be', 'there', 'with', 'you', 'forever', 'in', 'your', 'heart.!']
```

```python
# Normalizing Case

# split into words by white space
words = text.split()
# convert to lower case
words = [word.lower() for word in words]
print(words[:100])
```

**Execution Output:**
```text
["i'll", 'always', 'be', 'there', 'with', 'you', 'forever', 'in', 'your', 'heart.!']
```

# Spacy

Spacy is an open-source software python library used in advanced natural language processing and machine learning. It will be used to build information extraction, natural language understanding systems, and to pre-process text for deep learning.

Install:
```py
!pip install -U spacy
!python -m spacy download en_core_web_sm
```

```python
!pip install -U spacy
!python -m spacy download en_core_web_sm
```

```python
import spacy
nlp = spacy.load('en_core_web_sm')
# Here en_core means core english,web_sm means small language,We import core english language here.
# This is spacy's internal english language
```

```python
string = '"I\'ll always be there with you forever in your mind!"'
print(string)
```

**Execution Output:**
```text
"I'll always be there with you forever in your mind!"
```

```python
# Here we will break the string into token and print in text

doc = nlp(string)
for token in doc:
    print(token.text, end=' | ')
```

**Execution Output:**
```text
" | I | 'll | always | be | there | with | you | forever | in | your | mind | ! | " |
```

```python
doc
```

**Execution Output:**
```text
"I'll always be there with you forever in your mind!"
```

```python
# Here we break the string into unicode token

doc2 = nlp(u"I'm always here to help you all! Email:milaanparmar9@gmail.com or visit more at https://github.com/")
for t in doc2:
    print(t)
```

**Execution Output:**
```text
I
'm
always
here
to
help
you
all
!
Email:milaanparmar9@gmail.com
or
visit
more
at
https://github.com/
```

```python
doc3 = nlp(u'A 5km NYC cab ride costs $10.30')
for t in doc3:
    print(t)
```

**Execution Output:**
```text
A
5
km
NYC
cab
ride
costs
$
10.30
```

```python
doc4 = nlp(u"Let's visit St. Louis in the U.S. next year.")
for t in doc4:
    print(t)
```

**Execution Output:**
```text
Let
's
visit
St.
Louis
in
the
U.S.
next
year
.
```

**See the number of word used in the string**

```python
len(doc4)
```

**Execution Output:**
```text
11
```

**See the number of vocabolary or character used in the string**

```python
# How many vocabolary present in token
len(doc.vocab)
```

**Execution Output:**
```text
793
```

**Print the 3rd word from the string**

```python
doc5 = nlp(u'It is better to give than to receive.')
# Retrieve the third token:
doc5[2]
```

**Execution Output:**
```text
better
```

**Print the words from 3rd word to 4th word**

```python
# Retrieve three tokens from the middle:
doc5[2:5]
```

**Execution Output:**
```text
better to give
```

```python
# Retrieve the last four tokens:
doc5[-4:]
```

**Execution Output:**
```text
than to receive.
```

```python
doc6 = nlp(u'My dinner was horrible.')
doc7 = nlp(u'Your dinner was delicious.')
```

**We can't store any word from one line to the any word of other line/sentence**

```python
# Try to change "My dinner was horrible" to "My dinner was delicious"
doc6[3] = doc7[3]
```

### Explain which type of token is this

```python
# We can explain which type of token is this
doc8 = nlp(u'Apple to build a Hong Kong factory for $6 million')

for token in doc8:
    print(token.text, end=' | ')

print('\n----')
# ents shows all entities present in all tokens
for ent in doc8.ents:
    print(ent.text+' - '+ent.label_+' - '+str(spacy.explain(ent.label_)))
```

**Execution Output:**
```text
Apple | to | build | a | Hong | Kong | factory | for | $ | 6 | million | 
----
Hong Kong - GPE - Countries, cities, states
$6 million - MONEY - Monetary values, including unit
```

Here it shows "Apple" may be a companies,agencies,institution.Similarly like Hong Kong may be a countries,cities.....etc

```python
len(doc8.ents)
```

**Execution Output:**
```text
2
```

```python
doc9 = nlp(u"Autonomous cars shift insurance liability toward manufacturers.")
# noun_chunks finds all noun present in all tokens
for chunk in doc9.noun_chunks:
    print(chunk.text)
```

**Execution Output:**
```text
Autonomous cars
insurance liability
manufacturers
```

```python
doc10 = nlp(u"Red cars do not carry higher insurance rates.")

for chunk in doc10.noun_chunks:
    print(chunk.text)
```

**Execution Output:**
```text
Red cars
higher insurance rates
```

```python
doc11 = nlp(u"He was a one-eyed, one-horned, flying, purple people-eater.")

for chunk in doc11.noun_chunks:
    print(chunk.text)
```

**Execution Output:**
```text
He
a one-eyed, one-horned, flying, purple people-eater
```

```python
# Here we can see how "displacy render" shows which type of token are these
# and relationships between them 
from spacy import displacy

doc = nlp(u'Apple is going to build a U.K. factory for $6 million.')
displacy.render(doc, style='dep', jupyter=True, options={'distance': 110})
```

```python
# Showing types of token and there relationships in a line
doc = nlp(u'Over the last quarter Apple sold nearly 20 thousand iPods for a profit of $6 million.')
displacy.render(doc, style='ent', jupyter=True)
```

# **Tokenization - KN**

```python
!pip install nltk
```

```python
# Tokenization of paragraphs/sentences
import nltk
# nltk.download("popular") # use this to download all popular libraries in nltk
# nltk.download('all')
```

```python
paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them. 
               Why? Because we respect the freedom of others.That is why my 
               first vision is that of freedom. I believe that India got its first vision of 
               this in 1857, when we started the War of Independence. It is this freedom that
               we must protect and nurture and build on. If we are not free, no one will respect us.
               My second vision for India’s development. For fifty years we have been a developing nation.
               It is time we see ourselves as a developed nation. We are among the top 5 nations of the world
               in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.
               Our achievements are being globally recognised today. Yet we lack the self-confidence to
               see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
               I have a third vision. India must stand up to the world. Because I believe that unless India 
               stands up to the world, no one will respect us. Only strength respects strength. We must be 
               strong not only as a military power but also as an economic power. Both must go hand-in-hand. 
               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of 
               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. 
               I see four milestones in my career"""
```

```python
# Tokenizing sentences
sentences = nltk.sent_tokenize(paragraph)

# Tokenizing words
words = nltk.word_tokenize(paragraph)
```

```python
sentences
```

**Execution Output:**
```text
['I have three visions for India.',
 'In 3000 years of our history, people from all over \n               the world have come and invaded us, captured our lands, conquered our minds.',
 'From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,\n               the French, the Dutch, all of them came and looted us, took over what was ours.',
 'Yet we have not done this to any other nation.',
 'We have not conquered anyone.',
 'We have not grabbed their land, their culture, \n               their history and tried to enforce our way of life on them.',
 'Why?',
 'Because we respect the freedom of others.That is why my \n               first vision is that of freedom.',
 'I believe that India got its first vision of \n               this in 1857, when we started the War of Independence.',
 'It is this freedom that\n               we must protect and nurture and build on.',
 'If we are not free, no one will respect us.',
 'My second vision for India’s development.',
 'For fifty years we have been a developing nation.',
 'It is time we see ourselves as a developed nation.',
 'We are among the top 5 nations of the world\n               in terms of GDP.',
 'We
... [Output truncated for brevity]
```

```python
words
```

**Execution Output:**
```text
['I',
 'have',
 'three',
 'visions',
 'for',
 'India',
 '.',
 'In',
 '3000',
 'years',
 'of',
 'our',
 'history',
 ',',
 'people',
 'from',
 'all',
 'over',
 'the',
 'world',
 'have',
 'come',
 'and',
 'invaded',
 'us',
 ',',
 'captured',
 'our',
 'lands',
 ',',
 'conquered',
 'our',
 'minds',
 '.',
 'From',
 'Alexander',
 'onwards',
 ',',
 'the',
 'Greeks',
 ',',
 'the',
 'Turks',
 ',',
 'the',
 'Moguls',
 ',',
 'the',
 'Portuguese',
 ',',
 'the',
 'British',
 ',',
 'the',
 'French',
 ',',
 'the',
 'Dutch',
 ',',
 'all',
 'of',
 'them',
 'came',
 'and',
 'looted',
 'us',
 ',',
 'took',
 'over',
 'what',
 'was',
 'ours',
 '.',
 'Yet',
 'we',
 'have',
 'not',
 'done',
 'this',
 'to',
 'any',
 'other',
 'nation',
 '.',
 'We',
 'have',
 'not',
 'conquered',
 'anyone',
 '.',
 'We',
 'have',
 'not',
 'grabbed',
 'their',
 'land',
 ',',
 'their',
 'culture',
 ',',
 'their',
 'history',
 'and',
 'tried',
 'to',
 'enforce',
 'our',
 'way',
 'of',
 'life',
 'on',
 'them',
 '.',
 'Why',
 '?',
 'Because',
 'we',
 'respect',
 'the',
 'freedom',
 'of',
 'others.That',
 'is',
 'why',
 'my',
 'first',
 'vision',
 'is',
 'that',
 'of',
 'freedom',
 '.',
 'I',
 'believe',
 'that',
 'India',
 'got',
... [Output truncated for brevity]
```

---

## 3. Stopwords Management in NLP Pipelines

# 03 Stop Words
Stop words are those words that do not contribute to the deeper meaning of the phrase. They are the most common words such as: the, a, and is. For some applications like documentation classification, it may make sense to remove stop words. NLTK provides a list of commonly agreed upon stop words for a variety of languages, such as English..

```python
# Perform standard imports:
import spacy
nlp = spacy.load('en_core_web_sm')
```

```python
import nltk
nltk.download('stopwords')
```

**Execution Output:**
```text
True
```

```python
# Print the set of spaCy's default stop words (remember that sets are unordered):
print(nlp.Defaults.stop_words)
```

**Execution Output:**
```text
{'otherwise', 'last', 'will', 'sixty', 'that', 'yourself', 'hereafter', 'became', 'in', 'get', 'anywhere', 'everything', 'my', 'former', 'amongst', 'already', 'been', 'however', 'quite', 'should', 'once', 'whole', 'thru', 'your', 'do', 'next', '‘ve', 'toward', 'again', 'is', 'then', 'about', 'fifteen', 'seem', 'into', 'you', 'this', 'alone', 'due', 'beforehand', 'above', 'who', 'ours', 'really', 'regarding', 'amount', 'everyone', 'forty', 'by', 'why', 'nobody', '‘s', 'first', 'were', "'ll", 'twelve', 'up', 'itself', 'never', 'often', 'what', 'very', 'whatever', 'rather', 'same', 'more', 'somewhere', 'after', 'below', 'only', 'did', 'yet', 'call', 'so', 'am', 'few', 'since', 'enough', 'whereupon', 'nowhere', 'back', 'but', 'yourselves', 'throughout', 'go', 'while', 'n’t', 'empty', 'take', 'whither', 'seeming', 'i', 'onto', 'least', 'own', 'name', 'become', 'two', 'sometimes', 'between', 'side', 'moreover', 'therefore', 'becomes', 'both', 'her', 'someone', 'anything', 'somehow', 'on', 'well', 'beyond', 'yours', 'either', 'wherever', 'part', 'among', 'seemed', 'three', 'where', 'therein', 'may', 'before', 'whence', 'anyway', 'their', 'under', 'myself', 'not', 'per', 'anyhow', 'over', 
... [Output truncated for brevity]
```

```python
from nltk.corpus import stopwords 
stopwords.words('english') # all stopwords in english language
```

**Execution Output:**
```text
['i',
 'me',
 'my',
 'myself',
 'we',
 'our',
 'ours',
 'ourselves',
 'you',
 "you're",
 "you've",
 "you'll",
 "you'd",
 'your',
 'yours',
 'yourself',
 'yourselves',
 'he',
 'him',
 'his',
 'himself',
 'she',
 "she's",
 'her',
 'hers',
 'herself',
 'it',
 "it's",
 'its',
 'itself',
 'they',
 'them',
 'their',
 'theirs',
 'themselves',
 'what',
 'which',
 'who',
 'whom',
 'this',
 'that',
 "that'll",
 'these',
 'those',
 'am',
 'is',
 'are',
 'was',
 'were',
 'be',
 'been',
 'being',
 'have',
 'has',
 'had',
 'having',
 'do',
 'does',
 'did',
 'doing',
 'a',
 'an',
 'the',
 'and',
 'but',
 'if',
 'or',
 'because',
 'as',
 'until',
 'while',
 'of',
 'at',
 'by',
 'for',
 'with',
 'about',
 'against',
 'between',
 'into',
 'through',
 'during',
 'before',
 'after',
 'above',
 'below',
 'to',
 'from',
 'up',
 'down',
 'in',
 'out',
 'on',
 'off',
 'over',
 'under',
 'again',
 'further',
 'then',
 'once',
 'here',
 'there',
 'when',
 'where',
 'why',
 'how',
 'all',
 'any',
 'both',
 'each',
 'few',
 'more',
 'most',
 'other',
 'some',
 'such',
 'no',
 'nor',
 'not',
 'only',
 'own',
 'same',
 'so',
 'than',
 'too',
 'very',
 's',
 't',
 'can',
 'will',
 'just',
 'don',
 "don't",
 'sho
... [Output truncated for brevity]
```

```python
len(nlp.Defaults.stop_words)
```

**Execution Output:**
```text
326
```

### **Check if a word is a stop word or not( use "vocab" method)**

```python
# We can check a word that is stopword or not by using vocab method
nlp.vocab['myself'].is_stop # check "myself" is stopword or not
```

**Execution Output:**
```text
True
```

```python
nlp.vocab['mystery'].is_stop
```

**Execution Output:**
```text
False
```

### **Make a word as stopword**

```python
# step-1: Add the word to the set of stop words. Use lowercase!
nlp.Defaults.stop_words.add('mystery')
```

```python
# step-2: Set the stop_word tag on the lexeme
nlp.vocab['mystery'].is_stop = True
```

```python
len(nlp.Defaults.stop_words)
```

**Execution Output:**
```text
327
```

```python
nlp.vocab['mystery'].is_stop
```

**Execution Output:**
```text
True
```

### **To remove a stop word**
Alternatively, you may decide that `'beyond'` should not be considered a stop word.

```python
# step-1: Remove the word from the set of stop words
nlp.Defaults.stop_words.remove('and')

# step-2: Remove the stop_word tag from the lexeme
nlp.vocab['and'].is_stop = False
```

```python
len(nlp.Defaults.stop_words)
```

**Execution Output:**
```text
326
```

```python
nlp.vocab['and'].is_stop
```

**Execution Output:**
```text
False
```

### **Print all stopwords from a line**

```python
import string
import re
import nltk
nltk.download('punkt')
from nltk import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
# load data
text = 'The Quick brown fox jump over the lazy dog!'
```

```python
# split into words
tokens = word_tokenize(text)
print(tokens)
```

**Execution Output:**
```text
['The', 'Quick', 'brown', 'fox', 'jump', 'over', 'the', 'lazy', 'dog', '!']
```

```python
# convert to lower case
tokens = [w.lower() for w in tokens]
print(tokens)
```

**Execution Output:**
```text
['the', 'quick', 'brown', 'fox', 'jump', 'over', 'the', 'lazy', 'dog', '!']
```

```python
# prepare regex for char filtering
re_punc = re.compile('[%s]' % re.escape(string.punctuation))
print(re_punc)
```

**Execution Output:**
```text
re.compile('[!"\\#\\$%\\&\'\\(\\)\\*\\+,\\-\\./:;<=>\\?@\\[\\\\\\]\\^_`\\{\\|\\}\\~]')
```

```python
# remove punctuation from each word
stripped = [re_punc.sub('', w) for w in tokens]
print(stripped)
```

**Execution Output:**
```text
['the', 'quick', 'brown', 'fox', 'jump', 'over', 'the', 'lazy', 'dog', '']
```

```python
# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]
print(words)
```

**Execution Output:**
```text
['the', 'quick', 'brown', 'fox', 'jump', 'over', 'the', 'lazy', 'dog']
```

```python
# filter out non-stop words
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print(words)
```

**Execution Output:**
```text
['quick', 'brown', 'fox', 'jump', 'lazy', 'dog']
```

```python
# Check remaining tokens are stopword or not
nlp.vocab['dog'].is_stop
```

**Execution Output:**
```text
False
```

---

## 4. Stemming vs Lemmatization Deep Dive

### Porter Stemmer & Snowball Stemmer
# 08 Stemming

```python
import spacy
nlp = spacy.load('en_core_web_sm')
doc2 = nlp(u"I'm always here to help you all! Email:milaanparmar9@gmail.com or visit more at https://github.com/")
for t in doc2:
    print(t)
```

**Execution Output:**
```text
I
'm
always
here
to
help
you
all
!
Email:milaanparmar9@gmail.com
or
visit
more
at
https://github.com/
```

```python
doc3 = nlp(u'A 5km NYC cab ride costs $10.30')
for t in doc3:
    print(t)
```

**Execution Output:**
```text
A
5
km
NYC
cab
ride
costs
$
10.30
```

```python
doc4 = nlp(u"Let's visit St. Louis in the U.S. next year.")
for t in doc4:
    print(t)
```

**Execution Output:**
```text
Let
's
visit
St.
Louis
in
the
U.S.
next
year
.
```

### ----   Porter Stemmer   ------

```python
# Import the toolkit and the full Porter Stemmer library
import nltk
from nltk.stem.porter import *
```

```python
p_stemmer = PorterStemmer()
words = ['run','runner','running','ran','runs','easily','fairly']
```

```python
for word in words:
    print(word+' --> '+p_stemmer.stem(word))
```

**Execution Output:**
```text
run --> run
runner --> runner
running --> run
ran --> ran
runs --> run
easily --> easili
fairly --> fairli
```

```python
#SnowballStemmer
from nltk.stem.snowball import SnowballStemmer
# The Snowball Stemmer requires that you pass a language parameter
s_stemmer = SnowballStemmer(language='english')
```

```python
words = ['run','runner','running','ran','runs','easily','fairly']
# words = ['generous','generation','generously','generate']
```

```python
for word in words:
    print(word+' --> '+s_stemmer.stem(word))
```

**Execution Output:**
```text
run --> run
runner --> runner
running --> run
ran --> ran
runs --> run
easily --> easili
fairly --> fair
```

```python
# ----Do Some more practice -----
```

```python
words = ['consolingly']
```

```python
print('Porter Stemmer:')
for word in words:
    print(word+' --> '+p_stemmer.stem(word))
```

**Execution Output:**
```text
Porter Stemmer:
consolingly --> consolingli
```

```python
print('Porter2 Stemmer:')
for word in words:
    print(word+' --> '+s_stemmer.stem(word))
```

**Execution Output:**
```text
Porter2 Stemmer:
consolingly --> consol
```

```python
# Stemming has its drawbacks. If given the token saw, stemming might always return saw, whereas lemmatization would likely return either
# see or saw depending on whether the use of the token was as a verb or a noun. As an example, consider the following:

phrase = 'I am meeting him tomorrow at the meeting'
for word in phrase.split():
    print(word+' --> '+p_stemmer.stem(word))
```

**Execution Output:**
```text
I --> i
am --> am
meeting --> meet
him --> him
tomorrow --> tomorrow
at --> at
the --> the
meeting --> meet
```

```python
# Perform standard imports:
import spacy
nlp = spacy.load('en_core_web_sm')
```

```python
var1 = nlp(u"John Adam is one the researcher who invent the direction of way towards success!")

for token in var1:
    print(token.text, '\t', token.pos_, '\t', token.lemma, '\t', token.lemma_)
```

**Execution Output:**
```text
John 	 PROPN 	 11174346320140919546 	 John
Adam 	 PROPN 	 14264057329400597350 	 Adam
is 	 AUX 	 10382539506755952630 	 be
one 	 NUM 	 17454115351911680600 	 one
the 	 DET 	 7425985699627899538 	 the
researcher 	 NOUN 	 1317581537614213870 	 researcher
who 	 PRON 	 3876862883474502309 	 who
invent 	 VERB 	 5373681334090504585 	 invent
the 	 DET 	 7425985699627899538 	 the
direction 	 NOUN 	 895834437038626927 	 direction
of 	 ADP 	 886050111519832510 	 of
way 	 NOUN 	 6878210874361030284 	 way
towards 	 ADP 	 9315050841437086371 	 towards
success 	 NOUN 	 16089821935113899987 	 success
! 	 PUNCT 	 17494803046312582752 	 !
```

```python
def show_lemmas(text):
    for token in text:
        print(f'{token.text:{12}} {token.pos_:{6}} {token.lemma:<{22}} {token.lemma_}')
```

```python
var2 = nlp(u"John Adam is one the researcher who invent the direction of way towards success!")
show_lemmas(var2)
```

**Execution Output:**
```text
John         PROPN  11174346320140919546   John
Adam         PROPN  14264057329400597350   Adam
is           AUX    10382539506755952630   be
one          NUM    17454115351911680600   one
the          DET    7425985699627899538    the
researcher   NOUN   1317581537614213870    researcher
who          PRON   3876862883474502309    who
invent       VERB   5373681334090504585    invent
the          DET    7425985699627899538    the
direction    NOUN   895834437038626927     direction
of           ADP    886050111519832510     of
way          NOUN   6878210874361030284    way
towards      ADP    9315050841437086371    towards
success      NOUN   16089821935113899987   success
!            PUNCT  17494803046312582752   !
```

```python
var3 = nlp(u"I am meeting him tomorrow at the meeting.")
show_lemmas(var3)
```

**Execution Output:**
```text
I            PRON   4690420944186131903    I
am           AUX    10382539506755952630   be
meeting      VERB   6880656908171229526    meet
him          PRON   1655312771067108281    he
tomorrow     NOUN   3573583789758258062    tomorrow
at           ADP    11667289587015813222   at
the          DET    7425985699627899538    the
meeting      NOUN   14798207169164081740   meeting
.            PUNCT  12646065887601541794   .
```

```python
var4 = nlp(u"That's of the greate person in the world")
show_lemmas(var4)
```

**Execution Output:**
```text
That         PRON   4380130941430378203    that
's           AUX    10382539506755952630   be
of           ADP    886050111519832510     of
the          DET    7425985699627899538    the
greate       ADJ    4429768169814447593    greate
person       NOUN   14800503047316267216   person
in           ADP    3002984154512732771    in
the          DET    7425985699627899538    the
world        NOUN   1703489418272052182    world
```

### SpaCy Morphological Lemmatization & POS Alignment
# 02 Stemming and Lemmatization

## Stemming
**Stemming** is the process of reducing a word to its word stem that affixes to suffixes and prefixes or to the roots of words known as a **lemma**. For example: words such as “Likes”, ”liked”, ”likely” and ”liking” will be reduced to “like” after stemming.

1. PorterStemmer
2. SnowballStemmer

## **Lemmatization**
**Lemmatization** usually refers to doing things properly with the use of a vocabulary and morphological analysis of words, normally aiming to remove inflectional endings only and to return the base or dictionary form of a word, which is known as the **lemma** .
- The difference between stemming and lemmatization is that stemming is faster as it cuts words without knowing the context, while lemmatization is slower as it knows the context of words before processing.
- For example, in stemming "historical" word'll convert to "histori", while in Lemmatization this word'll convert to "history"
- In stemming the converted base word may have or haven't a proper meaning while in lemmatization converted base word has proper meaning.

```python
import spacy
nlp = spacy.load('en_core_web_sm')
doc2 = nlp(u"We're here to help! Send snail-mail, email fahad@gmail.com or visit us at http://www.fahadhussaincs.blogspot.com!")
for t in doc2:
    print(t)
```

**Execution Output:**
```text
We
're
here
to
help
!
Send
snail
-
mail
,
email
fahad@gmail.com
or
visit
us
at
http://www.fahadhussaincs.blogspot.com
!
```

```python
doc3 = nlp(u'A 5km NYC cab ride costs $10.30')
for t in doc3:
    print(t)
```

**Execution Output:**
```text
A
5
km
NYC
cab
ride
costs
$
10.30
```

```python
doc4 = nlp(u"Let's visit St. Louis in the U.S. next year.")
for t in doc4:
    print(t)
```

**Execution Output:**
```text
Let
's
visit
St.
Louis
in
the
U.S.
next
year
.
```

```python
# ----   Porter Stemmer   ------
```

## **Stemming**
**Stemming** is the process of reducing a word to its word stem that affixes to suffixes and prefixes or to the roots of words known as a lemma. For example: words such as “Likes”, ”liked”, ”likely” and ”liking” will be reduced to “like” after stemming.

1. PorterStemmer
2. SnowballStemmer

```python
# Import the toolkit and the full Porter Stemmer library
import nltk
from nltk.stem.porter import *
```

```python
p_stemmer = PorterStemmer()
words = ['run','runner','running','ran','runs','easily','fairly']
```

```python
for word in words:
    print(word+' --> '+p_stemmer.stem(word))
```

**Execution Output:**
```text
run --> run
runner --> runner
running --> run
ran --> ran
runs --> run
easily --> easili
fairly --> fairli
```

```python
#SnowballStemmer
from nltk.stem.snowball import SnowballStemmer
# The Snowball Stemmer requires that you pass a language parameter
s_stemmer = SnowballStemmer(language='english')
```

```python
words = ['run','runner','running','ran','runs','easily','fairly']
# words = ['generous','generation','generously','generate']
```

```python
for word in words:
    print(word+' --> '+s_stemmer.stem(word))
```

**Execution Output:**
```text
run --> run
runner --> runner
running --> run
ran --> ran
runs --> run
easily --> easili
fairly --> fair
```

```python
# ----Do Some more practice -----
```

```python
words = ['consolingly']
```

```python
print('Porter Stemmer:')
for word in words:
    print(word+' --> '+p_stemmer.stem(word))
```

**Execution Output:**
```text
Porter Stemmer:
consolingly --> consolingli
```

```python
print('Porter2 Stemmer:')
for word in words:
    print(word+' --> '+s_stemmer.stem(word))
```

**Execution Output:**
```text
Porter2 Stemmer:
consolingly --> consol
```

```python
# Stemming has its drawbacks. If given the token saw, stemming might always return saw, whereas lemmatization would likely return either
# see or saw depending on whether the use of the token was as a verb or a noun. As an example, consider the following:

phrase = 'I am meeting him tomorrow at the meeting'
for word in phrase.split():
    print(word+' --> '+p_stemmer.stem(word))
```

**Execution Output:**
```text
I --> i
am --> am
meeting --> meet
him --> him
tomorrow --> tomorrow
at --> at
the --> the
meeting --> meet
```

```python
# Perform standard imports:
import spacy
nlp = spacy.load('en_core_web_sm')
```

```python
var1 = nlp(u"John Adam is one the researcher who invent the direction of way towards success!")

for token in var1:
    print(token.text, '\t', token.pos_, '\t', token.lemma, '\t', token.lemma_)
```

**Execution Output:**
```text
John 	 PROPN 	 11174346320140919546 	 John
Adam 	 PROPN 	 14264057329400597350 	 Adam
is 	 AUX 	 10382539506755952630 	 be
one 	 NUM 	 17454115351911680600 	 one
the 	 DET 	 7425985699627899538 	 the
researcher 	 NOUN 	 1317581537614213870 	 researcher
who 	 PRON 	 3876862883474502309 	 who
invent 	 VERB 	 5373681334090504585 	 invent
the 	 DET 	 7425985699627899538 	 the
direction 	 NOUN 	 895834437038626927 	 direction
of 	 ADP 	 886050111519832510 	 of
way 	 NOUN 	 6878210874361030284 	 way
towards 	 ADP 	 9315050841437086371 	 towards
success 	 NOUN 	 16089821935113899987 	 success
! 	 PUNCT 	 17494803046312582752 	 !
```

```python
def show_lemmas(text):
    for token in text:
        print(f'{token.text:{12}} {token.pos_:{6}} {token.lemma:<{22}} {token.lemma_}')
```

```python
var2 = nlp(u"John Adam is one the researcher who invent the direction of way towards success!")
show_lemmas(var2)
```

**Execution Output:**
```text
John         PROPN  11174346320140919546   John
Adam         PROPN  14264057329400597350   Adam
is           AUX    10382539506755952630   be
one          NUM    17454115351911680600   one
the          DET    7425985699627899538    the
researcher   NOUN   1317581537614213870    researcher
who          PRON   3876862883474502309    who
invent       VERB   5373681334090504585    invent
the          DET    7425985699627899538    the
direction    NOUN   895834437038626927     direction
of           ADP    886050111519832510     of
way          NOUN   6878210874361030284    way
towards      ADP    9315050841437086371    towards
success      NOUN   16089821935113899987   success
!            PUNCT  17494803046312582752   !
```

```python
var3 = nlp(u"I am meeting him tomorrow at the meeting.")
show_lemmas(var3)
```

**Execution Output:**
```text
I            PRON   4690420944186131903    I
am           AUX    10382539506755952630   be
meeting      VERB   6880656908171229526    meet
him          PRON   1655312771067108281    he
tomorrow     NOUN   3573583789758258062    tomorrow
at           ADP    11667289587015813222   at
the          DET    7425985699627899538    the
meeting      NOUN   14798207169164081740   meeting
.            PUNCT  12646065887601541794   .
```

```python
var4 = nlp(u"That's of the greate person in the world")
show_lemmas(var4)
```

**Execution Output:**
```text
That         PRON   4380130941430378203    that
's           AUX    10382539506755952630   be
of           ADP    886050111519832510     of
the          DET    7425985699627899538    the
greate       ADJ    4429768169814447593    greate
person       NOUN   14800503047316267216   person
in           ADP    3002984154512732771    in
the          DET    7425985699627899538    the
world        NOUN   1703489418272052182    world
```

# **Stemming - KN**

```python
import nltk
nltk.download('popular')

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
```

```python
paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them. 
               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of 
               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. 
               I see four milestones in my career"""
```

```python
sentences = nltk.sent_tokenize(paragraph)
stemmer = PorterStemmer()

# Stemming
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)
```

```python
sentences
```

**Execution Output:**
```text
['i three vision india .',
 'in 3000 year histori , peopl world come invad us , captur land , conquer mind .',
 'from alexand onward , greek , turk , mogul , portugues , british , french , dutch , came loot us , took .',
 'yet done nation .',
 'we conquer anyon .',
 'we grab land , cultur , histori tri enforc way life .',
 'my good fortun work three great mind .',
 'dr. vikram sarabhai dept .',
 'space , professor satish dhawan , succeed dr. brahm prakash , father nuclear materi .',
 'i lucki work three close consid great opportun life .',
 'i see four mileston career']
```

**Problem :** Produced intermediate representation of the word may not have any meaning.

# **Lemmatization - KN**

```python
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
```

```python
paragraph = """Thank you all so very much. Thank you to the Academy. 
               Thank you to all of you in this room. I have to congratulate 
               the other incredible nominees this year. The Revenant was 
               the product of the tireless efforts of an unbelievable cast
               support leaders around the world who do not speak for the 
               big polluters, but who speak for all of humanity, for the
               indigenous people of the world, for the billions and 
               billions of underprivileged people out there who would be
               most affected by this. For our children’s children, and 
               for those people out there whose voices have been drowned
               out by the politics of greed. I thank you all for this 
               amazing award tonight. Let us not take this planet for 
               granted. I do not take tonight for granted. Thank you so very much."""
```

```python
sentences = nltk.sent_tokenize(paragraph)
lemmatizer = WordNetLemmatizer()

# Lemmatization
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)
```

---

## 5. Practical Preprocessing Exercises & Solutions

### Q. Import spacy library and load ‘en_core_web_sm’ model for english language. Load ‘xx_ent_wiki_sm’ for multi language support.

```python
import spacy
import re
```

```python
import warnings
```

```python
warnings.filterwarnings("ignore")
```

```python
from spacy.lang.en.examples import sentences 

nlp = spacy.load("en_core_web_sm")
```

```python
#! python -m spacy download xx_ent_wiki_sm
```

```python
nlp = spacy.load("xx_ent_wiki_sm")
```

## Q. Tokenize the given text in encoded form using the tokenizer of Huggingface’s transformer package. text="Last week, the University of Cambridge shared its own research that shows if everyone wears a mask outside home,dreaded ‘second wave’ of the pandemic can be avoided."

```python
text="Last week, the University of Cambridge shared its own research that shows if everyone wears a mask outside home,dreaded ‘second wave’ of the pandemic can be avoided."
```

```python
#! pip install transformers
```

```python
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
tokenizer.tokenize(text)
```

**Execution Output:**
```text
['dancing',
 'is',
 'an',
 'art',
 '.',
 'students',
 'should',
 'be',
 'taught',
 'dance',
 'as',
 'a',
 'subject',
 'in',
 'schools',
 '.',
 'i',
 'danced',
 'in',
 'many',
 'of',
 'my',
 'school',
 'function',
 '.',
 'some',
 'people',
 'are',
 'always',
 'he',
 '##sit',
 '##ating',
 'to',
 'dance',
 '.']
```

```python
#! pip install sentencepiece
```

```python
from transformers import XLNetTokenizerFast
# tokenizer = XLNetTokenizer.from_pretrained("xlnet-base-cased")
```

```python
tokenizer = XLNetTokenizerFast.from_pretrained('xlnet-base-cased', do_lower_case=True)
```

```python
tokenizer.tokenize(text)
```

**Execution Output:**
```text
['▁Last',
 '▁week',
 ',',
 '▁the',
 '▁University',
 '▁of',
 '▁Cambridge',
 '▁shared',
 '▁its',
 '▁own',
 '▁research',
 '▁that',
 '▁shows',
 '▁if',
 '▁everyone',
 '▁wears',
 '▁a',
 '▁mask',
 '▁outside',
 '▁home',
 ',',
 'd',
 'read',
 'ed',
 '▁‘',
 'second',
 '▁wave',
 '’',
 '▁of',
 '▁the',
 '▁pandemic',
 '▁can',
 '▁be',
 '▁avoided',
 '.']
```

## Q. Add the custom stopwords “NIL” and “JUNK” in spaCy and remove the stopwords in below text

```python
import spacy
nlp = spacy.load("en")
```

```python
text= "Dancing is an art. Students should be taught dance as a subject in schools . I danced in many of my school function. Some people are always hesitating to dance."
```

```python
from spacy.lang.en.stop_words import STOP_WORDS

print(STOP_WORDS)
```

**Execution Output:**
```text
{'whither', 'regarding', 'next', 'among', 'give', 'four', 'empty', 'even', 'below', 'sixty', 'thence', 'would', 'my', 'by', 'without', 'six', 'thereby', 'so', 'very', 'ca', 'should', 'i', 'neither', '‘d', 'therein', 'sometimes', 'never', 'more', 'seems', 'thru', 'above', 'some', 'also', 'until', 'seemed', 'noone', 'whence', 'two', 'twenty', 'he', 'JUNK', 'been', 'except', 'otherwise', 'beside', 'n’t', 'down', 'name', 'since', 'yours', 'those', 'keep', 'various', 'be', 'namely', 'his', 'towards', 'onto', 'through', 'are', 'whenever', 'nobody', 'wherever', "'s", 'well', 'ten', 'ever', 'was', '‘re', 'seem', 'really', 'full', 'did', 'such', 'becoming', 'not', 'latter', 'fifteen', 'using', 'but', 'few', 'all', 'me', "'ve", 'how', 'toward', 'why', 'out', 'does', 'have', '’s', 'them', 'as', 'am', 'than', 'they', 'mostly', 'get', 'from', 'each', 'afterwards', 'everything', 'across', 'thus', 'still', 'we', 'might', 'per', 'became', '‘s', 'herself', 'us', 'who', 'besides', 'hereafter', "'d", 'along', 'nor', '’ve', 'will', 'latterly', 'n‘t', 'another', 'wherein', 'take', 'whom', 'with', 'put', 'someone', 'other', 'mine', "'m", 'were', 'when', '’m', 'during', 'anyhow', 'one', 'part', '‘ve', 'a
... [Output truncated for brevity]
```

```python
STOP_WORDS.add("NIL")
STOP_WORDS.add("JUNK")
```

```python
def clean_text(text):

    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = text.replace("#","")
    text = text.split()
    text =[re.sub(r'[^\w\s]','',word) for word in text]
    text = ' '.join(text).strip()
    return text
```

```python
final_text = [clean_text(text) for text in tokenizer.tokenize(text) if text not in STOP_WORDS]
```

## Perform stemming/ through 3 different stemmers, convert each token to it’s root form in the given text text= "Dancing is an art. Students should be taught dance as a subject in schools . I danced in many of my school function. Some people are always hesitating to dance."

```python
from nltk.stem import PorterStemmer

porter = PorterStemmer()

for word in final_text:
    print(word,"--->",porter.stem(word))
```

**Execution Output:**
```text
dancing ---> danc
art ---> art
 ---> 
students ---> student
taught ---> taught
dance ---> danc
subject ---> subject
schools ---> school
 ---> 
danced ---> danc
school ---> school
function ---> function
 ---> 
people ---> peopl
sit ---> sit
ating ---> ate
dance ---> danc
 --->
```

```python
from nltk.stem import SnowballStemmer

snowball = SnowballStemmer(language='english')


for word in final_text:
    print(word,"--->",snowball.stem(word))
```

**Execution Output:**
```text
dancing ---> danc
art ---> art
 ---> 
students ---> student
taught ---> taught
dance ---> danc
subject ---> subject
schools ---> school
 ---> 
danced ---> danc
school ---> school
function ---> function
 ---> 
people ---> peopl
sit ---> sit
ating ---> ate
dance ---> danc
 --->
```

```python
from nltk.stem import LancasterStemmer

lancaster = LancasterStemmer()


for word in final_text:
    print(word,"--->",lancaster.stem(word))
```

**Execution Output:**
```text
dancing ---> dant
art ---> art
 ---> 
students ---> stud
taught ---> taught
dance ---> dant
subject ---> subject
schools ---> schools
 ---> 
danced ---> dant
school ---> school
function ---> funct
 ---> 
people ---> peopl
sit ---> sit
ating ---> at
dance ---> dant
 --->
```

## Q. Find the similarity between any two words using spacy library.

```python
nlp = spacy.load('en_core_web_sm')

tokens = nlp(text)

for i in range(len(tokens)-1):
  token1, token2 = tokens[i], tokens[i+1]

  print(f"Similarity between {token1} and {token2} are {token1.similarity(token2)}")
```

**Execution Output:**
```text
Similarity between Dancing and is are 0.08921847492456436
Similarity between is and an are -0.02279028855264187
Similarity between an and art are 0.15128077566623688
Similarity between art and . are 0.0397493951022625
Similarity between . and Students are 0.14362917840480804
Similarity between Students and should are -0.0788043886423111
Similarity between should and be are -0.03701809048652649
Similarity between be and taught are 0.015718594193458557
Similarity between taught and dance are 0.12317228317260742
Similarity between dance and as are 0.1455344259738922
Similarity between as and a are -0.008473770692944527
Similarity between a and subject are 0.22243037819862366
Similarity between subject and in are 0.17231208086013794
Similarity between in and schools are -0.004667080473154783
Similarity between schools and . are 0.1460227072238922
Similarity between . and I are -0.05847412720322609
Similarity between I and danced are -0.12739694118499756
Similarity between danced and in are 0.017842913046479225
Similarity between in and many are 0.06421512365341187
Similarity between many and of are 0.14072491228580475
Similarity between of and my are 0.11980316787958145
Similarity betw
... [Output truncated for brevity]
```

```python
len(tokens)
```

**Execution Output:**
```text
33
```

---

## Key Interview Takeaways: Preprocessing & Tokenization

1. **Why computers struggle with NLP**:
   - 80% of enterprise data is unstructured.
   - Ambiguities in natural language fall into three major buckets:
     - **Lexical Ambiguity**: A single word has multiple meanings depending on context (e.g., "bank" of a river vs financial "bank"; "run" a company vs "run" a mile).
     - **Syntactic Ambiguity**: A sentence can have multiple parse trees (e.g., "I saw the man with the telescope").
     - **Referential Ambiguity**: Unclear pronoun references (e.g., "The trophy didn't fit in the suitcase because it was too large").
2. **Tokenization Pipeline**:
   - SpaCy processes text left-to-right, splitting on whitespace, then checking prefix (e.g. `$`, `(`, `"`), suffix (e.g. `km`, `)`, `,`), infix (e.g. `-`, `--`, `/`), and exception rules (e.g. `U.S.`, `don't`).
3. **Stemming vs Lemmatization**:
   - **Stemming**: Heuristic-based chopping of word ends (affixes). Fast, rule-based, non-linguistic, may produce non-dictionary words (e.g., "universe" -> "univers", "ponies" -> "poni").
   - **Lemmatization**: Dictionary-based morphological analysis utilizing part-of-speech context to return the true root word (lemma) (e.g., "better" -> "good", "was" -> "be", "mice" -> "mouse").
