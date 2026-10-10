"""
Natural Language Processing (NLP) seed data: Topics and Lessons.
Covers Tokenization, SpaCy linguistic annotations (POS, NER, Matcher), Vectorization (BoW, TF-IDF, Word2Vec), and Deep Learning NLP (Embeddings, RNNs, LSTMs, CNNs, BERT).
"""

NLP_TOPICS = [
    {
        "subjectSlug": "nlp",
        "title": "NLP Foundations & Text Preprocessing",
        "slug": "nlp-foundations",
        "description": "Natural language pipeline, language ambiguity, tokenization mechanics (prefixes, suffixes, infixes), stopwords, and stemming vs lemmatization.",
        "order": 1,
        "isPublished": True,
    },
    {
        "subjectSlug": "nlp",
        "title": "Linguistic Annotations with SpaCy",
        "slug": "spacy-linguistic-annotations",
        "description": "Rule-based pattern matching (Matcher), coarse/fine-grained POS tagging, Named Entity Recognition (NER), and sentence segmentation.",
        "order": 2,
        "isPublished": True,
    },
    {
        "subjectSlug": "nlp",
        "title": "Text Vectorization & Embeddings",
        "slug": "vectorization-embeddings",
        "description": "Statistical and neural representations: Bag of Words, N-Grams, TF-IDF mathematics, cosine similarity, and Word2Vec (CBOW vs Skip-Gram).",
        "order": 3,
        "isPublished": True,
    },
    {
        "subjectSlug": "nlp",
        "title": "Deep Learning for NLP & Transformers",
        "slug": "deep-learning-nlp",
        "description": "Keras text preprocessing, trainable Embedding layers, Recurrent Neural Networks (LSTM, GRU), Conv1D for text, and fine-tuning BERT.",
        "order": 4,
        "isPublished": True,
    },
]

NLP_LESSONS = [
    {
        "topicSlug": "nlp-foundations",
        "subjectSlug": "nlp",
        "title": "NLP Foundations, Tokenization & Text Preprocessing",
        "slug": "nlp-foundations-tokenization-and-preprocessing",
        "description": "Master natural language processing fundamentals, tokenization mechanics, stopwords filtering, and stemming vs lemmatization.",
        "estimatedTime": "40 mins",
        "difficulty": "Beginner to Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Why Computers Struggle with Natural Language",
                    "content": (
                        "Over 80% of enterprise data is unstructured text. Human language presents 3 fundamental types of ambiguity:\n\n"
                        "• **Lexical Ambiguity**: A single word has multiple meanings depending on context (e.g., 'river bank' vs 'investment bank'; 'ran out of milk' vs 'run down').\n"
                        "• **Syntactic Ambiguity**: Sentences permit multiple parse trees ('I saw the man with the telescope').\n"
                        "• **Referential Ambiguity**: Unclear pronoun references ('The trophy didn't fit in the suitcase because it was too large')."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Stemming vs Lemmatization: When to Use Which",
                    "content": (
                        "• **Stemming**: Rule-based chopping of word affixes (prefixes/suffixes) using heuristics like Porter or Snowball algorithms. Fast, non-linguistic, may output non-words ('universe' -> 'univers', 'ponies' -> 'poni').\n\n"
                        "• **Lemmatization**: Dictionary-based morphological analysis using part-of-speech context to return the true canonical base form (lemma) ('better' -> 'good', 'was' -> 'be', 'running' as noun -> 'running', as verb -> 'run')."
                    )
                },
                {
                    "type": "code",
                    "title": "SpaCy Tokenization and Stopwords Management",
                    "language": "python",
                    "code": (
                        "import spacy\n\n"
                        "nlp = spacy.load('en_core_web_sm')\n"
                        "doc = nlp('Apple is looking at buying U.K. startup for $1 billion!')\n\n"
                        "# Inspect tokens and stopwords\n"
                        "for token in doc:\n"
                        "    print(f'{token.text:12} | Lemma: {token.lemma_:10} | Stopword: {token.is_stop}')\n\n"
                        "# Add custom domain stopword\n"
                        "nlp.Defaults.stop_words.add('startup')\n"
                        "nlp.vocab['startup'].is_stop = True"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "spacy-linguistic-annotations",
        "subjectSlug": "nlp",
        "title": "Linguistic Annotations: POS Tagging, NER, Matcher & Segmentation",
        "slug": "spacy-linguistic-annotations-pos-ner-matching",
        "description": "Deep dive into linguistic analysis using SpaCy: Part-of-Speech tagging, Named Entity Recognition, Matcher rules, and sentence segmentation.",
        "estimatedTime": "45 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "SpaCy Linguistic Components: POS, NER, and Matcher",
                    "content": (
                        "SpaCy processes raw text through a statistical NLP pipeline:\n\n"
                        "• **Part-of-Speech (POS)**: Coarse universal tags (`token.pos_` like `NOUN`, `VERB`, `ADJ`) and fine-grained Penn Treebank tags (`token.tag_` like `NNP`, `VBD`, `NNS`).\n"
                        "• **Named Entity Recognition (NER)**: Identifies real-world named entities (`doc.ents`) like `PERSON`, `ORG`, `GPE` (locations), `DATE`, `MONEY`.\n"
                        "• **Rule-Based Matcher**: Enables finding complex patterns across token attributes (e.g. `[{'LOWER': 'solar'}, {'IS_PUNCT': True, 'OP': '?'}, {'LOWER': 'power'}]`)."
                    )
                },
                {
                    "type": "code",
                    "title": "Pattern Matching and Custom NER Injection",
                    "language": "python",
                    "code": (
                        "import spacy\n"
                        "from spacy.matcher import Matcher\n"
                        "from spacy.tokens import Span\n\n"
                        "nlp = spacy.load('en_core_web_sm')\n"
                        "matcher = Matcher(nlp.vocab)\n\n"
                        "# Pattern: 'Solar Power' or 'Solar-power'\n"
                        "pattern = [{'LOWER': 'solar'}, {'IS_PUNCT': True, 'OP': '?'}, {'LOWER': 'power'}]\n"
                        "matcher.add('SolarPower', [pattern])\n\n"
                        "doc = nlp('Solar-power energy is advancing fast at Tesla Inc.')\n"
                        "matches = matcher(doc)\n"
                        "for match_id, start, end in matches:\n"
                        "    print(f'Matched span: {doc[start:end].text}')"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "vectorization-embeddings",
        "subjectSlug": "nlp",
        "title": "Vectorization: Bag of Words, N-Grams, TF-IDF & Word2Vec",
        "slug": "vectorization-bow-tfidf-and-word2vec",
        "description": "Understand text representation: CountVectorizer, N-Gram modeling, Term Frequency-Inverse Document Frequency (TF-IDF), and Word2Vec embeddings.",
        "estimatedTime": "45 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "TF-IDF Mathematical Foundations",
                    "content": (
                        "TF-IDF measures the relative statistical importance of a word in a specific document relative to a corpus:\n\n"
                        "• **Term Frequency (TF)**: `TF(t, d) = count(t, d) / total_words(d)`.\n"
                        "• **Inverse Document Frequency (IDF)**: `IDF(t, D) = log(N / n_t) + 1`.\n"
                        "• Frequent stop words appear in almost all documents (`n_t ≈ N`), so their IDF approaches zero.\n"
                        "• Domain-specific informative terms have low document counts `n_t`, producing high positive weights."
                    )
                },
                {
                    "type": "code",
                    "title": "Text Classification Pipeline with TF-IDF Vectorizer",
                    "language": "python",
                    "code": (
                        "from sklearn.feature_extraction.text import TfidfVectorizer\n"
                        "from sklearn.naive_bayes import MultinomialNB\n"
                        "from sklearn.pipeline import Pipeline\n\n"
                        "pipeline = Pipeline([\n"
                        "    ('tfidf', TfidfVectorizer(ngram_range=(1, 2), stop_words='english', max_features=5000)),\n"
                        "    ('clf', MultinomialNB())\n"
                        "])\n\n"
                        "pipeline.fit(X_train, y_train)\n"
                        "predictions = pipeline.predict(X_test)\n"
                        "print(f'Accuracy: {pipeline.score(X_test, y_test):.4f}')"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "deep-learning-nlp",
        "subjectSlug": "nlp",
        "title": "Deep Learning for NLP: Keras Preprocessing, Embeddings, RNNs, CNNs & BERT",
        "slug": "tensorflow-nlp-embeddings-rnns-and-bert",
        "description": "Master deep learning architectures for NLP: Keras Tokenizer, trainable Embedding layers, LSTMs, GRUs, 1D Convolutions, and fine-tuning BERT.",
        "estimatedTime": "50 mins",
        "difficulty": "Advanced",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Sequence Architectures: RNN vs LSTM vs BERT",
                    "content": (
                        "• **SimpleRNN**: Standard recurrence loop. Gradients vanish exponentially across sequence lengths > 10-20 steps.\n\n"
                        "• **LSTM (Long Short-Term Memory)**: Solves vanishing gradients with an additive cell state `C_t` regulated by 3 gates: Forget Gate, Input Gate, and Output Gate.\n\n"
                        "• **GRU (Gated Recurrent Unit)**: Lightweight variant combining hidden and cell states with 2 gates (Reset, Update).\n\n"
                        "• **BERT (Bidirectional Encoder Representations from Transformers)**: Eliminates sequential bottlenecks with bidirectional multi-head self-attention, pre-trained on Masked Language Modeling (MLM)."
                    )
                },
                {
                    "type": "code",
                    "title": "Bidirectional LSTM Sequence Classifier in Keras",
                    "language": "python",
                    "code": (
                        "import tensorflow as tf\n"
                        "from tensorflow.keras import layers, models\n\n"
                        "vocab_size = 10000\n"
                        "embedding_dim = 64\n"
                        "max_length = 120\n\n"
                        "model = models.Sequential([\n"
                        "    layers.Embedding(vocab_size, embedding_dim, input_length=max_length),\n"
                        "    layers.Bidirectional(layers.LSTM(64, return_sequences=True)),\n"
                        "    layers.Bidirectional(layers.LSTM(32)),\n"
                        "    layers.Dense(32, activation='relu'),\n"
                        "    layers.Dropout(0.3),\n"
                        "    layers.Dense(1, activation='sigmoid')\n"
                        "])\n\n"
                        "model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])"
                    )
                }
            ]
        }
    },
]
