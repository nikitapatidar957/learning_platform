# Linguistic Annotations: POS Tagging, NER, Matcher & Segmentation

Deep dive into advanced linguistic analysis using SpaCy: Part-of-Speech (POS) tagging, Named Entity Recognition (NER), Rule-based Pattern Matching with `Matcher`, and Sentence Boundary Disambiguation (SBD).

---

## 1. Rule-Based Vocabulary Matching (`Matcher` & `PhraseMatcher`)

# 04 Vocabulary and Matching
So far we've seen how a body of text is divided into tokens, and how individual tokens are parsed and tagged with parts of speech, dependencies and lemmas.

Lets understand about identify and label specific phrases that match patterns in NLP

## Rule-based Matching
spaCy offers a rule-matching tool called `Matcher` that allows you to build a library of token patterns, then match those patterns against a Doc object to return a list of found matches. You can match on any part of the token including text and annotations, and you can add multiple patterns to the same matcher.
For more: https://spacy.io/usage/linguistic-features#section-rule-based-matching

```python
# Perform standard imports
import spacy
nlp = spacy.load('en_core_web_sm')
```

```python
# Import the Matcher library
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)
```

<font color=green>Here `matcher` is an object that pairs to the current `Vocab` object. We can add and remove specific named matchers to `matcher` as needed.</font>

### Creating patterns
In literature, the phrase 'solar power' might appear as one word or two, with or without a hyphen. In this section we'll develop a matcher named 'SolarPower' that finds all three:

```python
pattern1 = [{'LOWER': 'solarpower'}]
pattern2 = [{'LOWER': 'solar'}, {'LOWER': 'power'}]
pattern3 = [{'LOWER': 'solar'}, {'IS_PUNCT': True}, {'LOWER': 'power'}]

matcher.add('SolarPower', None, pattern1, pattern2, pattern3)
```

Let's break this down:
* `pattern1` looks for a single token whose lowercase text reads 'solarpower'
* `pattern2` looks for two adjacent tokens that read 'solar' and 'power' in that order
* `pattern3` looks for three adjacent tokens, with a middle token that can be any punctuation.<font color=green>*</font>

<font color=green>\* Remember that single spaces are not tokenized, so they don't count as punctuation.</font>
<br>Once we define our patterns, we pass them into `matcher` with the name 'SolarPower', and set *callbacks* to `None` (more on callbacks later).

### Applying the matcher to a Doc object

```python
doc = nlp(u'The Solar Power industry continues to grow as demand \
for solarpower increases. Solar-power cars are gaining popularity.')
```

```python
found_matches = matcher(doc)
print(found_matches)
```

**Execution Output:**
```text
[(8656102463236116519, 1, 3), (8656102463236116519, 10, 11), (8656102463236116519, 13, 16)]
```

`matcher` returns a list of tuples. Each tuple contains an ID for the match, with start & end tokens that map to the span `doc[start:end]`

```python
for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id]  # get string representation
    span = doc[start:end]                    # get the matched span
    print(match_id, string_id, start, end, span.text)
```

**Execution Output:**
```text
8656102463236116519 SolarPower 1 3 Solar Power
8656102463236116519 SolarPower 10 11 solarpower
8656102463236116519 SolarPower 13 16 Solar-power
```

The `match_id` is simply the hash value of the `string_ID` 'SolarPower'

### Setting pattern options and quantifiers
You can make token rules optional by passing an `'OP':'*'` argument. This lets us streamline our patterns list:
Ex: Solar+power: here + is OP.To remove this we should use like this

```python
# Redefine the patterns:
pattern1 = [{'LOWER': 'solarpower'}]
pattern2 = [{'LOWER': 'solar'}, {'IS_PUNCT': True, 'OP':'*'}, {'LOWER': 'power'}]

# Remove the old patterns to avoid duplication:
matcher.remove('SolarPower')

# Add the new set of patterns to the 'SolarPower' matcher:
matcher.add('SolarPower', None, pattern1, pattern2)
```

```python
found_matches = matcher(doc)
print(found_matches)
```

**Execution Output:**
```text
[(8656102463236116519, 1, 3), (8656102463236116519, 10, 11), (8656102463236116519, 13, 16)]
```

This found both two-word patterns, with and without the hyphen!

The following quantifiers can be passed to the `'OP'` key:
<table><tr><th>OP</th><th>Description</th></tr>

<tr ><td><span >\!</span></td><td>Negate the pattern, by requiring it to match exactly 0 times</td></tr>
<tr ><td><span >?</span></td><td>Make the pattern optional, by allowing it to match 0 or 1 times</td></tr>
<tr ><td><span >\+</span></td><td>Require the pattern to match 1 or more times</td></tr>
<tr ><td><span >\*</span></td><td>Allow the pattern to match zero or more times</td></tr>
</table>

### Be careful with lemmas!
If we wanted to match on both 'solar power' and 'solar powered', it might be tempting to look for the *lemma* of 'powered' and expect it to be 'power'. This is not always the case! The lemma of the *adjective* 'powered' is still 'powered':

```python
pattern1 = [{'LOWER': 'solarpower'}]
pattern2 = [{'LOWER': 'solar'}, {'IS_PUNCT': True, 'OP':'*'}, {'LEMMA': 'power'}] # CHANGE THIS PATTERN

# Remove the old patterns to avoid duplication:
matcher.remove('SolarPower')

# Add the new set of patterns to the 'SolarPower' matcher:
matcher.add('SolarPower', None, pattern1, pattern2)
```

```python
doc2 = nlp(u'Solar-powered energy runs solar-powered cars.')
```

```python
found_matches = matcher(doc2)
print(found_matches)
```

**Execution Output:**
```text
[(8656102463236116519, 0, 3), (8656102463236116519, 5, 8)]
```

<font color=green>The matcher found the first occurrence because the lemmatizer treated 'Solar-powered' as a verb, but not the second as it considered it an adjective.<br>For this case it may be better to set explicit token patterns.</font>

```python
pattern1 = [{'LOWER': 'solarpower'}]
pattern2 = [{'LOWER': 'solar'}, {'IS_PUNCT': True, 'OP':'*'}, {'LOWER': 'power'}]
pattern3 = [{'LOWER': 'solarpowered'}]
pattern4 = [{'LOWER': 'solar'}, {'IS_PUNCT': True, 'OP':'*'}, {'LOWER': 'powered'}]

# Remove the old patterns to avoid duplication:
matcher.remove('SolarPower')

# Add the new set of patterns to the 'SolarPower' matcher:
matcher.add('SolarPower', None, pattern1, pattern2, pattern3, pattern4)
```

```python
found_matches = matcher(doc2)
print(found_matches)
```

**Execution Output:**
```text
[(8656102463236116519, 0, 3), (8656102463236116519, 5, 8)]
```

## Other token attributes
Besides lemmas, there are a variety of token attributes we can use to determine matching rules:
<table><tr><th>Attribute</th><th>Description</th></tr>

<tr ><td><span >`ORTH`</span></td><td>The exact verbatim text of a token</td></tr>
<tr ><td><span >`LOWER`</span></td><td>The lowercase form of the token text</td></tr>
<tr ><td><span >`LENGTH`</span></td><td>The length of the token text</td></tr>
<tr ><td><span >`IS_ALPHA`, `IS_ASCII`, `IS_DIGIT`</span></td><td>Token text consists of alphanumeric characters, ASCII characters, digits</td></tr>
<tr ><td><span >`IS_LOWER`, `IS_UPPER`, `IS_TITLE`</span></td><td>Token text is in lowercase, uppercase, titlecase</td></tr>
<tr ><td><span >`IS_PUNCT`, `IS_SPACE`, `IS_STOP`</span></td><td>Token is punctuation, whitespace, stop word</td></tr>
<tr ><td><span >`LIKE_NUM`, `LIKE_URL`, `LIKE_EMAIL`</span></td><td>Token text resembles a number, URL, email</td></tr>
<tr ><td><span >`POS`, `TAG`, `DEP`, `LEMMA`, `SHAPE`</span></td><td>The token's simple and extended part-of-speech tag, dependency label, lemma, shape</td></tr>
<tr ><td><span >`ENT_TYPE`</span></td><td>The token's entity label</td></tr>

</table>

### Token wildcard
You can pass an empty dictionary `{}` as a wildcard to represent **any token**. For example, you might want to retrieve hashtags without knowing what might follow the `#` character:
>`[{'ORTH': '#'}, {}]`

___
## PhraseMatcher
In the above section we used token patterns to perform rule-based matching. An alternative - and often more efficient - method is to match on terminology lists. In this case we use PhraseMatcher to create a Doc object from a list of phrases, and pass that into `matcher` instead.

```python
# Perform standard imports, reset nlp
import spacy
nlp = spacy.load('en_core_web_sm')
```

```python
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab, attr='LOWER')
```

```python
terms = ['Galaxy Note', 'iPhone 11', 'iPhone XS', 'Google Pixel']
patterns = [nlp(text) for text in terms]
matcher.add("TerminologyList", None, *patterns)
```

```python
# Borrowed from https://daringfireball.net/linked/2019/09/21/patel-11-pro
text_doc = nlp("Glowing review overall, and some really interesting side-by-side "
               "photography tests pitting the iPhone 11 Pro against the "
               "Galaxy Note 10 Plus and last year’s iPhone XS and Google Pixel 3.") 
matches = matcher(text_doc)
print(matches)
```

**Execution Output:**
```text
[(3766102292120407359, 17, 19), (3766102292120407359, 22, 24), (3766102292120407359, 30, 32), (3766102292120407359, 33, 35)]
```

```python
match_id, start, end = matches[1]
print(nlp.vocab.strings[match_id], text_doc[start:end])
```

**Execution Output:**
```text
TerminologyList Galaxy Note
```

---

## 2. Part-of-Speech (POS) Tagging & Syntactic Dependencies

# 05 POS - Part Of Speech

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)
```

**Execution Output:**
```text
Apple Apple PROPN NNP nsubj Xxxxx True False
is be AUX VBZ aux xx True True
looking look VERB VBG ROOT xxxx True False
at at ADP IN prep xx True True
buying buy VERB VBG pcomp xxxx True False
U.K. U.K. PROPN NNP dobj X.X. False False
startup startup VERB VBD dep xxxx True False
for for ADP IN prep xxx True True
$ $ SYM $ quantmod $ False False
1 1 NUM CD compound d False False
billion billion NUM CD pobj xxxx True False
```

```python
# Perform standard imports
import spacy
nlp = spacy.load('en_core_web_sm')
```

```python
# Create a simple Doc object
doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")
```

## View token tags
Recall that you can obtain a particular token by its index position.
* To view the coarse POS tag use **`token.pos_`**
* To view the fine-grained tag use **`token.tag_`**
* To view the description of either type of tag use **`spacy.explain(tag)`**

<div class="alert alert-success">Note that `token.pos` and `token.tag` return integer hash values; by adding the underscores we get the text equivalent that lives in **doc.vocab**.</div>

```python
# Print the full text:
print(doc.text)
```

**Execution Output:**
```text
The quick brown fox jumped over the lazy dog's back.
```

```python
# Print the fifth word and associated tags:
print(doc[4].text, doc[4].pos_, doc[4].tag_, spacy.explain(doc[4].tag_))
```

**Execution Output:**
```text
jumped VERB VBD verb, past tense
```

We can apply this technique to the entire Doc object:

```python
for token in doc:
    print(f'{token.text:{10}} {token.pos_:{8}} {token.tag_:{6}} {spacy.explain(token.tag_)}')
```

**Execution Output:**
```text
The        DET      DT     determiner
quick      ADJ      JJ     adjective (English), other noun-modifier (Chinese)
brown      ADJ      JJ     adjective (English), other noun-modifier (Chinese)
fox        NOUN     NN     noun, singular or mass
jumped     VERB     VBD    verb, past tense
over       ADP      IN     conjunction, subordinating or preposition
the        DET      DT     determiner
lazy       ADJ      JJ     adjective (English), other noun-modifier (Chinese)
dog        NOUN     NN     noun, singular or mass
's         PART     POS    possessive ending
back       NOUN     NN     noun, singular or mass
.          PUNCT    .      punctuation mark, sentence closer
```

## Coarse-grained Part-of-speech Tags
Every token is assigned a POS Tag from the following list:


<table><tr><th>POS</th><th>DESCRIPTION</th><th>EXAMPLES</th></tr>
    
<tr><td>ADJ</td><td>adjective</td><td>*big, old, green, incomprehensible, first*</td></tr>
<tr><td>ADP</td><td>adposition</td><td>*in, to, during*</td></tr>
<tr><td>ADV</td><td>adverb</td><td>*very, tomorrow, down, where, there*</td></tr>
<tr><td>AUX</td><td>auxiliary</td><td>*is, has (done), will (do), should (do)*</td></tr>
<tr><td>CONJ</td><td>conjunction</td><td>*and, or, but*</td></tr>
<tr><td>CCONJ</td><td>coordinating conjunction</td><td>*and, or, but*</td></tr>
<tr><td>DET</td><td>determiner</td><td>*a, an, the*</td></tr>
<tr><td>INTJ</td><td>interjection</td><td>*psst, ouch, bravo, hello*</td></tr>
<tr><td>NOUN</td><td>noun</td><td>*girl, cat, tree, air, beauty*</td></tr>
<tr><td>NUM</td><td>numeral</td><td>*1, 2017, one, seventy-seven, IV, MMXIV*</td></tr>
<tr><td>PART</td><td>particle</td><td>*'s, not,*</td></tr>
<tr><td>PRON</td><td>pronoun</td><td>*I, you, he, she, myself, themselves, somebody*</td></tr>
<tr><td>PROPN</td><td>proper noun</td><td>*Mary, John, London, NATO, HBO*</td></tr>
<tr><td>PUNCT</td><td>punctuation</td><td>*., (, ), ?*</td></tr>
<tr><td>SCONJ</td><td>subordinating conjunction</td><td>*if, while, that*</td></tr>
<tr><td>SYM</td><td>symbol</td><td>*$, %, §, ©, +, −, ×, ÷, =, :), 😝*</td></tr>
<tr><td>VERB</td><td>verb</td><td>*run, runs, running, eat, ate, eating*</td></tr>
<tr><td>X</td><td>other</td><td>*sfpksdpsxmsa*</td></tr>
<tr><td>SPACE</td><td>space</td></tr>

___
## Fine-grained Part-of-speech Tags
Tokens are subsequently given a fine-grained tag as determined by morphology:
<table>
<tr><th>POS</th><th>Description</th><th>Fine-grained Tag</th><th>Description</th><th>Morphology</th></tr>
<tr><td>ADJ</td><td>adjective</td><td>AFX</td><td>affix</td><td>Hyph=yes</td></tr>
<tr><td>ADJ</td><td></td><td>JJ</td><td>adjective</td><td>Degree=pos</td></tr>
<tr><td>ADJ</td><td></td><td>JJR</td><td>adjective, comparative</td><td>Degree=comp</td></tr>
<tr><td>ADJ</td><td></td><td>JJS</td><td>adjective, superlative</td><td>Degree=sup</td></tr>
<tr><td>ADJ</td><td></td><td>PDT</td><td>predeterminer</td><td>AdjType=pdt PronType=prn</td></tr>
<tr><td>ADJ</td><td></td><td>PRP\$</td><td>pronoun, possessive</td><td>PronType=prs Poss=yes</td></tr>
<tr><td>ADJ</td><td></td><td>WDT</td><td>wh-determiner</td><td>PronType=int rel</td></tr>
<tr><td>ADJ</td><td></td><td>WP\$</td><td>wh-pronoun, possessive</td><td>Poss=yes PronType=int rel</td></tr>
<tr><td>ADP</td><td>adposition</td><td>IN</td><td>conjunction, subordinating or preposition</td><td></td></tr>
<tr><td>ADV</td><td>adverb</td><td>EX</td><td>existential there</td><td>AdvType=ex</td></tr>
<tr><td>ADV</td><td></td><td>RB</td><td>adverb</td><td>Degree=pos</td></tr>
<tr><td>ADV</td><td></td><td>RBR</td><td>adverb, comparative</td><td>Degree=comp</td></tr>
<tr><td>ADV</td><td></td><td>RBS</td><td>adverb, superlative</td><td>Degree=sup</td></tr>
<tr><td>ADV</td><td></td><td>WRB</td><td>wh-adverb</td><td>PronType=int rel</td></tr>
<tr><td>CONJ</td><td>conjunction</td><td>CC</td><td>conjunction, coordinating</td><td>ConjType=coor</td></tr>
<tr><td>DET</td><td>determiner</td><td>DT</td><td>determiner</td><td></td></tr>
<tr><td>INTJ</td><td>interjection</td><td>UH</td><td>interjection</td><td></td></tr>
<tr><td>NOUN</td><td>noun</td><td>NN</td><td>noun, singular or mass</td><td>Number=sing</td></tr>
<tr><td>NOUN</td><td></td><td>NNS</td><td>noun, plural</td><td>Number=plur</td></tr>
<tr><td>NOUN</td><td></td><td>WP</td><td>wh-pronoun, personal</td><td>PronType=int rel</td></tr>
<tr><td>NUM</td><td>numeral</td><td>CD</td><td>cardinal number</td><td>NumType=card</td></tr>
<tr><td>PART</td><td>particle</td><td>POS</td><td>possessive ending</td><td>Poss=yes</td></tr>
<tr><td>PART</td><td></td><td>RP</td><td>adverb, particle</td><td></td></tr>
<tr><td>PART</td><td></td><td>TO</td><td>infinitival to</td><td>PartType=inf VerbForm=inf</td></tr>
<tr><td>PRON</td><td>pronoun</td><td>PRP</td><td>pronoun, personal</td><td>PronType=prs</td></tr>
<tr><td>PROPN</td><td>proper noun</td><td>NNP</td><td>noun, proper singular</td><td>NounType=prop Number=sign</td></tr>
<tr><td>PROPN</td><td></td><td>NNPS</td><td>noun, proper plural</td><td>NounType=prop Number=plur</td></tr>
<tr><td>PUNCT</td><td>punctuation</td><td>-LRB-</td><td>left round bracket</td><td>PunctType=brck PunctSide=ini</td></tr>
<tr><td>PUNCT</td><td></td><td>-RRB-</td><td>right round bracket</td><td>PunctType=brck PunctSide=fin</td></tr>
<tr><td>PUNCT</td><td></td><td>,</td><td>punctuation mark, comma</td><td>PunctType=comm</td></tr>
<tr><td>PUNCT</td><td></td><td>:</td><td>punctuation mark, colon or ellipsis</td><td></td></tr>
<tr><td>PUNCT</td><td></td><td>.</td><td>punctuation mark, sentence closer</td><td>PunctType=peri</td></tr>
<tr><td>PUNCT</td><td></td><td>''</td><td>closing quotation mark</td><td>PunctType=quot PunctSide=fin</td></tr>
<tr><td>PUNCT</td><td></td><td>""</td><td>closing quotation mark</td><td>PunctType=quot PunctSide=fin</td></tr>
<tr><td>PUNCT</td><td></td><td>``</td><td>opening quotation mark</td><td>PunctType=quot PunctSide=ini</td></tr>
<tr><td>PUNCT</td><td></td><td>HYPH</td><td>punctuation mark, hyphen</td><td>PunctType=dash</td></tr>
<tr><td>PUNCT</td><td></td><td>LS</td><td>list item marker</td><td>NumType=ord</td></tr>
<tr><td>PUNCT</td><td></td><td>NFP</td><td>superfluous punctuation</td><td></td></tr>
<tr><td>SYM</td><td>symbol</td><td>#</td><td>symbol, number sign</td><td>SymType=numbersign</td></tr>
<tr><td>SYM</td><td></td><td>\$</td><td>symbol, currency</td><td>SymType=currency</td></tr>
<tr><td>SYM</td><td></td><td>SYM</td><td>symbol</td><td></td></tr>
<tr><td>VERB</td><td>verb</td><td>BES</td><td>auxiliary "be"</td><td></td></tr>
<tr><td>VERB</td><td></td><td>HVS</td><td>forms of "have"</td><td></td></tr>
<tr><td>VERB</td><td></td><td>MD</td><td>verb, modal auxiliary</td><td>VerbType=mod</td></tr>
<tr><td>VERB</td><td></td><td>VB</td><td>verb, base form</td><td>VerbForm=inf</td></tr>
<tr><td>VERB</td><td></td><td>VBD</td><td>verb, past tense</td><td>VerbForm=fin Tense=past</td></tr>
<tr><td>VERB</td><td></td><td>VBG</td><td>verb, gerund or present participle</td><td>VerbForm=part Tense=pres Aspect=prog</td></tr>
<tr><td>VERB</td><td></td><td>VBN</td><td>verb, past participle</td><td>VerbForm=part Tense=past Aspect=perf</td></tr>
<tr><td>VERB</td><td></td><td>VBP</td><td>verb, non-3rd person singular present</td><td>VerbForm=fin Tense=pres</td></tr>
<tr><td>VERB</td><td></td><td>VBZ</td><td>verb, 3rd person singular present</td><td>VerbForm=fin Tense=pres Number=sing Person=3</td></tr>
<tr><td>X</td><td>other</td><td>ADD</td><td>email</td><td></td></tr>
<tr><td>X</td><td></td><td>FW</td><td>foreign word</td><td>Foreign=yes</td></tr>
<tr><td>X</td><td></td><td>GW</td><td>additional word in multi-word expression</td><td></td></tr>
<tr><td>X</td><td></td><td>XX</td><td>unknown</td><td></td></tr>
<tr><td>SPACE</td><td>space</td><td>_SP</td><td>space</td><td></td></tr>
<tr><td></td><td></td><td>NIL</td><td>missing tag</td><td></td></tr>
</table>

For a current list of tags for all languages visit https://spacy.io/api/annotation#pos-tagging

## Working with POS Tags
In the English language, the same string of characters can have different meanings, even within the same sentence. For this reason, morphology is important. **spaCy** uses machine learning algorithms to best predict the use of a token in a sentence. Is *"I read books on NLP"* present or past tense? Is *wind* a verb or a noun?

```python
doc = nlp(u'I read books on NLP.')
r = doc[1]

print(f'{r.text:{10}} {r.pos_:{8}} {r.tag_:{6}} {spacy.explain(r.tag_)}')
```

**Execution Output:**
```text
read       VERB     VBP    verb, non-3rd person singular present
```

```python
doc = nlp(u'I read a book on NLP.')
r = doc[1]

print(f'{r.text:{10}} {r.pos_:{8}} {r.tag_:{6}} {spacy.explain(r.tag_)}')
```

**Execution Output:**
```text
read       VERB     VBP    verb, non-3rd person singular present
```

In the first example, with no other cues to work from, spaCy assumed that ***read*** was present tense.<br>In the second example the present tense form would be ***I am reading a book***, so spaCy assigned the past tense.

## Counting POS Tags
The `Doc.count_by()` method accepts a specific token attribute as its argument, and returns a frequency count of the given attribute as a dictionary object. Keys in the dictionary are the integer values of the given attribute ID, and values are the frequency. Counts of zero are not included.

```python
doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")

# Count the frequencies of different coarse-grained POS tags:
POS_counts = doc.count_by(spacy.attrs.POS)
POS_counts
```

**Execution Output:**
```text
{90: 2, 84: 3, 92: 3, 100: 1, 85: 1, 94: 1, 97: 1}
```

This isn't very helpful until you decode the attribute ID:

```python
doc.vocab[83].text
```

**Execution Output:**
```text
'LANG'
```

### Create a frequency list of POS tags from the entire document
Since `POS_counts` returns a dictionary, we can obtain a list of keys with `POS_counts.items()`.<br>By sorting the list we have access to the tag and its count, in order.

```python
for k,v in sorted(POS_counts.items()):
    print(f'{k}. {doc.vocab[k].text:{5}}: {v}')
```

**Execution Output:**
```text
84. ADJ  : 3
85. ADP  : 1
90. DET  : 2
92. NOUN : 3
94. PART : 1
97. PUNCT: 1
100. VERB : 1
```

```python
# Count the different fine-grained tags:
TAG_counts = doc.count_by(spacy.attrs.TAG)

for k,v in sorted(TAG_counts.items()):
    print(f'{k}. {doc.vocab[k].text:{4}}: {v}')
```

**Execution Output:**
```text
74. POS : 1
1292078113972184607. IN  : 1
10554686591937588953. JJ  : 3
12646065887601541794. .   : 1
15267657372422890137. DT  : 2
15308085513773655218. NN  : 3
17109001835818727656. VBD : 1
```

<div class="alert alert-success">**Why did the ID numbers get so big?** In spaCy, certain text values are hardcoded into `Doc.vocab` and take up the first several hundred ID numbers. Strings like 'NOUN' and 'VERB' are used frequently by internal operations. Others, like fine-grained tags, are assigned hash values as needed.</div>
<div class="alert alert-success">**Why don't SPACE tags appear?** In spaCy, only strings of spaces (two or more) are assigned tokens. Single spaces are not.</div>

```python
# Count the different dependencies:
DEP_counts = doc.count_by(spacy.attrs.DEP)

for k,v in sorted(DEP_counts.items()):
    print(f'{k}. {doc.vocab[k].text:{4}}: {v}')
```

**Execution Output:**
```text
402. amod: 3
415. det : 2
429. nsubj: 1
439. pobj: 1
440. poss: 1
443. prep: 1
445. punct: 1
8110129090154140942. case: 1
8206900633647566924. ROOT: 1
```

Here we've shown `spacy.attrs.POS`, `spacy.attrs.TAG` and `spacy.attrs.DEP`.<br>Refer back to the **Vocabulary and Matching** lecture from the previous section for a table of **Other token attributes**.

___
## Fine-grained POS Tag Examples
These are some grammatical examples (shown in **bold**) of specific fine-grained tags. We've removed punctuation and rarely used tags:
<table>
<tr><th>POS</th><th>TAG</th><th>DESCRIPTION</th><th>EXAMPLE</th></tr>
<tr><td>ADJ</td><td>AFX</td><td>affix</td><td>The Flintstones were a **pre**-historic family.</td></tr>
<tr><td>ADJ</td><td>JJ</td><td>adjective</td><td>This is a **good** sentence.</td></tr>
<tr><td>ADJ</td><td>JJR</td><td>adjective, comparative</td><td>This is a **better** sentence.</td></tr>
<tr><td>ADJ</td><td>JJS</td><td>adjective, superlative</td><td>This is the **best** sentence.</td></tr>
<tr><td>ADJ</td><td>PDT</td><td>predeterminer</td><td>Waking up is **half** the battle.</td></tr>
<tr><td>ADJ</td><td>PRP\$</td><td>pronoun, possessive</td><td>**His** arm hurts.</td></tr>
<tr><td>ADJ</td><td>WDT</td><td>wh-determiner</td><td>It's blue, **which** is odd.</td></tr>
<tr><td>ADJ</td><td>WP\$</td><td>wh-pronoun, possessive</td><td>We don't know **whose** it is.</td></tr>
<tr><td>ADP</td><td>IN</td><td>conjunction, subordinating or preposition</td><td>It arrived **in** a box.</td></tr>
<tr><td>ADV</td><td>EX</td><td>existential there</td><td>**There** is cake.</td></tr>
<tr><td>ADV</td><td>RB</td><td>adverb</td><td>He ran **quickly**.</td></tr>
<tr><td>ADV</td><td>RBR</td><td>adverb, comparative</td><td>He ran **quicker**.</td></tr>
<tr><td>ADV</td><td>RBS</td><td>adverb, superlative</td><td>He ran **fastest**.</td></tr>
<tr><td>ADV</td><td>WRB</td><td>wh-adverb</td><td>**When** was that?</td></tr>
<tr><td>CONJ</td><td>CC</td><td>conjunction, coordinating</td><td>The balloon popped **and** everyone jumped.</td></tr>
<tr><td>DET</td><td>DT</td><td>determiner</td><td>**This** is **a** sentence.</td></tr>
<tr><td>INTJ</td><td>UH</td><td>interjection</td><td>**Um**, I don't know.</td></tr>
<tr><td>NOUN</td><td>NN</td><td>noun, singular or mass</td><td>This is a **sentence**.</td></tr>
<tr><td>NOUN</td><td>NNS</td><td>noun, plural</td><td>These are **words**.</td></tr>
<tr><td>NOUN</td><td>WP</td><td>wh-pronoun, personal</td><td>**Who** was that?</td></tr>
<tr><td>NUM</td><td>CD</td><td>cardinal number</td><td>I want **three** things.</td></tr>
<tr><td>PART</td><td>POS</td><td>possessive ending</td><td>Fred**'s** name is short.</td></tr>
<tr><td>PART</td><td>RP</td><td>adverb, particle</td><td>Put it **back**!</td></tr>
<tr><td>PART</td><td>TO</td><td>infinitival to</td><td>I want **to** go.</td></tr>
<tr><td>PRON</td><td>PRP</td><td>pronoun, personal</td><td>**I** want **you** to go.</td></tr>
<tr><td>PROPN</td><td>NNP</td><td>noun, proper singular</td><td>**Kilroy** was here.</td></tr>
<tr><td>PROPN</td><td>NNPS</td><td>noun, proper plural</td><td>The **Flintstones** were a pre-historic family.</td></tr>
<tr><td>VERB</td><td>MD</td><td>verb, modal auxiliary</td><td>This **could** work.</td></tr>
<tr><td>VERB</td><td>VB</td><td>verb, base form</td><td>I want to **go**.</td></tr>
<tr><td>VERB</td><td>VBD</td><td>verb, past tense</td><td>This **was** a sentence.</td></tr>
<tr><td>VERB</td><td>VBG</td><td>verb, gerund or present participle</td><td>I am **going**.</td></tr>
<tr><td>VERB</td><td>VBN</td><td>verb, past participle</td><td>The treasure was **lost**.</td></tr>
<tr><td>VERB</td><td>VBP</td><td>verb, non-3rd person singular present</td><td>I **want** to go.</td></tr>
<tr><td>VERB</td><td>VBZ</td><td>verb, 3rd person singular present</td><td>He **wants** to go.</td></tr>
</table>

```python
# Perform standard imports
import spacy
nlp = spacy.load('en_core_web_sm')

# Import the displaCy library
from spacy import displacy
```

```python
# Create a simple Doc object
doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")
```

```python
# Render the dependency parse immediately inside Jupyter:
displacy.render(doc, style='dep', jupyter=True, options={'distance': 110})
```

---

## 3. Named Entity Recognition (NER)

# 06 Named Entity Recognition (NER)
(also known as entity identification, entity chunking and entity extraction) is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into pre-defined categories such as person names, organizations, locations, medical codes

spaCy has an **'ner'** pipeline component that identifies token spans fitting a predetermined set of named entities. These are available as the **`ents`** property of a **`Doc`** object.

https://spacy.io/usage/training#ner

```python
# Perform standard imports
import spacy
nlp = spacy.load('en_core_web_sm')
```

```python
# Write a function to display basic entity info:
def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text+' - '+ent.label_+' - '+str(spacy.explain(ent.label_)))
    else:
        print('No named entities found.')
```

```python
doc = nlp(u'Hi, everyone welcome to Milaan Parmar CS tutorial on NPL')

show_ents(doc)
```

**Execution Output:**
```text
Milaan Parmar CS - ORG - Companies, agencies, institutions, etc.
```

```python
doc = nlp(u'May I go to England or Canada, next month to see the virus report?')

show_ents(doc)
```

**Execution Output:**
```text
England - GPE - Countries, cities, states
Canada - GPE - Countries, cities, states
next month - DATE - Absolute or relative dates or periods
```

## Entity annotations
`Doc.ents` are token spans with their own set of annotations.
<table>
<tr><td>`ent.text`</td><td>The original entity text</td></tr>
<tr><td>`ent.label`</td><td>The entity type's hash value</td></tr>
<tr><td>`ent.label_`</td><td>The entity type's string description</td></tr>
<tr><td>`ent.start`</td><td>The token span's *start* index position in the Doc</td></tr>
<tr><td>`ent.end`</td><td>The token span's *stop* index position in the Doc</td></tr>
<tr><td>`ent.start_char`</td><td>The entity text's *start* index position in the Doc</td></tr>
<tr><td>`ent.end_char`</td><td>The entity text's *stop* index position in the Doc</td></tr>
</table>

```python
doc = nlp(u'Can I please borrow 500 dollars from Blake to buy some Microsoft stock?')

for ent in doc.ents:
    print(ent.text, ent.start, ent.end, ent.start_char, ent.end_char, ent.label_)
```

**Execution Output:**
```text
500 dollars 4 6 20 31 MONEY
Blake 7 8 37 42 PERSON
Microsoft 11 12 55 64 ORG
```

## NER Tags
Tags are accessible through the `.label_` property of an entity.
<table>
<tr><th>TYPE</th><th>DESCRIPTION</th><th>EXAMPLE</th></tr>
<tr><td>`PERSON`</td><td>People, including fictional.</td><td>*Fred Flintstone*</td></tr>
<tr><td>`NORP`</td><td>Nationalities or religious or political groups.</td><td>*The Republican Party*</td></tr>
<tr><td>`FAC`</td><td>Buildings, airports, highways, bridges, etc.</td><td>*Logan International Airport, The Golden Gate*</td></tr>
<tr><td>`ORG`</td><td>Companies, agencies, institutions, etc.</td><td>*Microsoft, FBI, MIT*</td></tr>
<tr><td>`GPE`</td><td>Countries, cities, states.</td><td>*France, UAR, Chicago, Idaho*</td></tr>
<tr><td>`LOC`</td><td>Non-GPE locations, mountain ranges, bodies of water.</td><td>*Europe, Nile River, Midwest*</td></tr>
<tr><td>`PRODUCT`</td><td>Objects, vehicles, foods, etc. (Not services.)</td><td>*Formula 1*</td></tr>
<tr><td>`EVENT`</td><td>Named hurricanes, battles, wars, sports events, etc.</td><td>*Olympic Games*</td></tr>
<tr><td>`WORK_OF_ART`</td><td>Titles of books, songs, etc.</td><td>*The Mona Lisa*</td></tr>
<tr><td>`LAW`</td><td>Named documents made into laws.</td><td>*Roe v. Wade*</td></tr>
<tr><td>`LANGUAGE`</td><td>Any named language.</td><td>*English*</td></tr>
<tr><td>`DATE`</td><td>Absolute or relative dates or periods.</td><td>*20 July 1969*</td></tr>
<tr><td>`TIME`</td><td>Times smaller than a day.</td><td>*Four hours*</td></tr>
<tr><td>`PERCENT`</td><td>Percentage, including "%".</td><td>*Eighty percent*</td></tr>
<tr><td>`MONEY`</td><td>Monetary values, including unit.</td><td>*Twenty Cents*</td></tr>
<tr><td>`QUANTITY`</td><td>Measurements, as of weight or distance.</td><td>*Several kilometers, 55kg*</td></tr>
<tr><td>`ORDINAL`</td><td>"first", "second", etc.</td><td>*9th, Ninth*</td></tr>
<tr><td>`CARDINAL`</td><td>Numerals that do not fall under another type.</td><td>*2, Two, Fifty-two*</td></tr>
</table>

___
### **Adding a Named Entity to a Span**
Normally we would have spaCy build a library of named entities by training it on several samples of text.<br>In this case, we only want to add one value:

```python
doc = nlp(u'Arthur to build a U.K. factory for $6 million')

show_ents(doc)
```

**Execution Output:**
```text
Arthur - ORG - Companies, agencies, institutions, etc.
U.K. - GPE - Countries, cities, states
$6 million - MONEY - Monetary values, including unit
```

Add **Milaan** as **PERSON**

```python
from spacy.tokens import Span

# Get the hash value of the ORG entity label
ORG = doc.vocab.strings[u'PERSON']  

# Create a Span for the new entity
new_ent = Span(doc, 0, 1, label=ORG)

# Add the entity to the existing Doc object
doc.ents = list(doc.ents) + [new_ent]
```

<font color=green>In the code above, the arguments passed to `Span()` are:</font>
-  `doc` - the name of the Doc object
-  `0` - the *start* index position of the span
-  `1` - the *stop* index position (exclusive)
-  `label=PERSON` - the label assigned to our entity

```python
show_ents(doc)
```

**Execution Output:**
```text
Arthur - ORG - Companies, agencies, institutions, etc.
U.K. - GPE - Countries, cities, states
$6 million - MONEY - Monetary values, including unit
```

___
## Adding Named Entities to All Matching Spans
What if we want to tag *all* occurrences of "WORDS"? WE NEED TO use the PhraseMatcher to identify a series of spans in the Doc:

```python
doc = nlp(u'Our company plans to introduce a new vacuum cleaner. '
          u'If successful, the vacuum cleaner will be our first product.')

show_ents(doc)
```

**Execution Output:**
```text
first - ORDINAL - "first", "second", etc.
```

```python
# Import PhraseMatcher and create a matcher object:
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)
```

```python
# Create the desired phrase patterns:
phrase_list = ['vacuum cleaner', 'vacuum-cleaner']
phrase_patterns = [nlp(text) for text in phrase_list]
```

```python
# Apply the patterns to our matcher object:
matcher.add('newproduct', None, *phrase_patterns)

# Apply the matcher to our Doc object:
matches = matcher(doc)

# See what matches occur:
matches
```

**Execution Output:**
```text
[(2689272359382549672, 7, 9), (2689272359382549672, 14, 16)]
```

```python
# Here we create Spans from each match, and create named entities from them:
from spacy.tokens import Span

PROD = doc.vocab.strings[u'PRODUCT']

new_ents = [Span(doc, match[1],match[2],label=PROD) for match in matches]

doc.ents = list(doc.ents) + new_ents
```

```python
show_ents(doc)
```

**Execution Output:**
```text
vacuum cleaner - PRODUCT - Objects, vehicles, foods, etc. (not services)
vacuum cleaner - PRODUCT - Objects, vehicles, foods, etc. (not services)
first - ORDINAL - "first", "second", etc.
```

___
## Counting Entities
While spaCy may not have a built-in tool for counting entities, we can pass a conditional statement into a list comprehension:

```python
doc = nlp(u'Originally priced at $29.50, the sweater was marked down to five dollars.')

show_ents(doc)
```

**Execution Output:**
```text
29.50 - MONEY - Monetary values, including unit
five dollars - MONEY - Monetary values, including unit
```

```python
len([ent for ent in doc.ents if ent.label_=='MONEY'])
```

**Execution Output:**
```text
2
```

```python
spacy.__version__
```

**Execution Output:**
```text
'2.2.4'
```

```python
doc = nlp(u'Originally priced at $29.50,\nthe sweater was marked down to five dollars.')

show_ents(doc)
```

**Execution Output:**
```text
29.50 - MONEY - Monetary values, including unit
five dollars - MONEY - Monetary values, including unit
```

### <font color=blue>However, there is a simple fix that can be added to the nlp pipeline:</font>

https://spacy.io/usage/processing-pipelines

```python
# Quick function to remove ents formed on whitespace:
def remove_whitespace_entities(doc):
    doc.ents = [e for e in doc.ents if not e.text.isspace()]
    return doc

# Insert this into the pipeline AFTER the ner component:
nlp.add_pipe(remove_whitespace_entities, after='ner')
```

```python
# Rerun nlp on the text above, and show ents:
doc = nlp(u'Originally priced at $29.50,\nthe sweater was marked down to five dollars.')

show_ents(doc)
```

**Execution Output:**
```text
29.50 - MONEY - Monetary values, including unit
five dollars - MONEY - Monetary values, including unit
```

For more on **Named Entity Recognition** visit https://spacy.io/usage/linguistic-features#101

___
## Noun Chunks
`Doc.noun_chunks` are *base noun phrases*: token spans that include the noun and words describing the noun. Noun chunks cannot be nested, cannot overlap, and do not involve prepositional phrases or relative clauses.<br>
Where `Doc.ents` rely on the **ner** pipeline component, `Doc.noun_chunks` are provided by the **parser**.

### `noun_chunks` components:
<table>
<tr><td>`.text`</td><td>The original noun chunk text.</td></tr>
<tr><td>`.root.text`</td><td>The original text of the word connecting the noun chunk to the rest of the parse.</td></tr>
<tr><td>`.root.dep_`</td><td>Dependency relation connecting the root to its head.</td></tr>
<tr><td>`.root.head.text`</td><td>The text of the root token's head.</td></tr>
</table>

```python
doc = nlp(u"Autonomous cars shift insurance liability toward manufacturers.")

for chunk in doc.noun_chunks:
    print(chunk.text+' - '+chunk.root.text+' - '+chunk.root.dep_+' - '+chunk.root.head.text)
```

**Execution Output:**
```text
Autonomous cars - cars - nsubj - shift
insurance liability - liability - dobj - shift
manufacturers - manufacturers - pobj - toward
```

### `Doc.noun_chunks` is a  generator function
Previously we mentioned that `Doc` objects do not retain a list of sentences, but they're available through the `Doc.sents` generator.<br>It's the same with `Doc.noun_chunks` - lists can be created if needed:

```python
len(doc.noun_chunks)
```

```python
len(list(doc.noun_chunks))
```

**Execution Output:**
```text
3
```

For more on **noun_chunks** visit https://spacy.io/usage/linguistic-features#noun-chunks

---

## 4. Sentence Segmentation & Custom Pipeline Boundaries

# 07 Sentence Segmentation

Sentence segmentation is the process of determining the longer processing units consisting of one or more words. This task involves identifying sentence boundaries between words in different sentences.

In **spaCy Basics** we saw briefly how Doc objects are divided into sentences. In this section we'll learn how sentence segmentation works, and how to set our own segmentation rules.

```python
# Perform standard imports
import spacy
nlp = spacy.load('en_core_web_sm')
```

```python
# From Spacy Basics:
doc = nlp(u'This is the first sentence. This is another sentence. This is the last sentence.')

for sent in doc.sents:
    print(sent)
```

**Execution Output:**
```text
This is the first sentence.
This is another sentence.
This is the last sentence.
```

### `Doc.sents` is a generator
It is important to note that `doc.sents` is a *generator*. That is, a Doc is not segmented until `doc.sents` is called. This means that, where you could print the second Doc token with `print(doc[1])`, you can't call the "second Doc sentence" with `print(doc.sents[1])`:

```python
print(doc[1])
```

**Execution Output:**
```text
is
```

```python
print(doc.sents[1])
```

However, you *can* build a sentence collection by running `doc.sents` and saving the result to a list:

```python
doc_sents = [sent for sent in doc.sents]
doc_sents
```

**Execution Output:**
```text
[This is the first sentence.,
 This is another sentence.,
 This is the last sentence.]
```

<font color=green>**NOTE**: `list(doc.sents)` also works. We show a list comprehension as it allows you to pass in conditionals.</font>

```python
# Now you can access individual sentences:
print(doc_sents[1])
```

**Execution Output:**
```text
This is another sentence.
```

### `sents` are Spans
At first glance it looks like each `sent` contains text from the original Doc object. In fact they're just Spans with start and end token pointers.

```python
type(doc_sents[1])
```

**Execution Output:**
```text
spacy.tokens.span.Span
```

```python
print(doc_sents[1].start, doc_sents[1].end)
```

**Execution Output:**
```text
6 11
```

## Adding Rules
spaCy's built-in `sentencizer` relies on the dependency parse and end-of-sentence punctuation to determine segmentation rules. We can add rules of our own, but they have to be added *before* the creation of the Doc object, as that is where the parsing of segment start tokens happens:

```python
# Parsing the segmentation start tokens happens during the nlp pipeline
doc2 = nlp(u'This is a sentence. This is a sentence. This is a sentence.')

for token in doc2:
    print(token.is_sent_start, ' '+token.text)
```

**Execution Output:**
```text
True  This
None  is
None  a
None  sentence
None  .
True  This
None  is
None  a
None  sentence
None  .
True  This
None  is
None  a
None  sentence
None  .
```

<font color=green>Notice we haven't run `doc2.sents`, and yet `token.is_sent_start` was set to True on two tokens in the Doc.</font>

Let's add a semicolon to our existing segmentation rules. That is, whenever the sentencizer encounters a semicolon, the next token should start a new segment.

```python
# SPACY'S DEFAULT BEHAVIOR
doc3 = nlp(u'"Management is doing things right; leadership is doing the right things." -Peter Drucker')

for sent in doc3.sents:
    print(sent)
```

**Execution Output:**
```text
"Management is doing things right; leadership is doing the right things."
-Peter
Drucker
```

```python
# ADD A NEW RULE TO THE PIPELINE
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == ';':
            doc[token.i+1].is_sent_start = True
    return doc

nlp.add_pipe(set_custom_boundaries, before='parser')

nlp.pipe_names
```

**Execution Output:**
```text
['tagger', 'set_custom_boundaries', 'parser', 'ner']
```

<font color=green>The new rule has to run before the document is parsed. Here we can either pass the argument `before='parser'` or `first=True`.

```python
# Re-run the Doc object creation:
doc4 = nlp(u'"Management is doing things right; leadership is doing the right things." -Peter Drucker')

for sent in doc4.sents:
    print(sent)
```

**Execution Output:**
```text
"Management is doing things right;
leadership is doing the right things."
-Peter
Drucker
```

```python
# And yet the new rule doesn't apply to the older Doc object:
for sent in doc3.sents:
    print(sent)
```

**Execution Output:**
```text
"Management is doing things right; leadership is doing the right things."
-Peter
Drucker
```

### Why not change the token directly?
Why not simply set the `.is_sent_start` value to True on existing tokens?

```python
# Find the token we want to change:
doc3[7]
```

**Execution Output:**
```text
leadership
```

```python
# Try to change the .is_sent_start attribute:
doc3[7].is_sent_start = True
```

<font color=green>spaCy refuses to change the tag after the document is parsed to prevent inconsistencies in the data.</font>

## Changing the Rules
In some cases we want to *replace* spaCy's default sentencizer with our own set of rules. In this section we'll see how the default sentencizer breaks on periods. We'll then replace this behavior with a sentencizer that breaks on linebreaks.

```python
nlp = spacy.load('en_core_web_sm')  # reset to the original

mystring = u"This is a sentence. This is another.\n\nThis is a \nthird sentence."

# SPACY DEFAULT BEHAVIOR:
doc = nlp(mystring)

for sent in doc.sents:
    print([token.text for token in sent])
```

**Execution Output:**
```text
['This', 'is', 'a', 'sentence', '.']
['This', 'is', 'another', '.', '\n\n']
['This', 'is', 'a', '\n', 'third', 'sentence', '.']
```

```python
# CHANGING THE RULES
from spacy.pipeline import SentenceSegmenter

def split_on_newlines(doc):
    start = 0
    seen_newline = False
    for word in doc:
        if seen_newline:
            yield doc[start:word.i]
            start = word.i
            seen_newline = False
        elif word.text.startswith('\n'): # handles multiple occurrences
            seen_newline = True
    yield doc[start:]      # handles the last group of tokens


sbd = SentenceSegmenter(nlp.vocab, strategy=split_on_newlines)
nlp.add_pipe(sbd)
```

<font color=green>While the function `split_on_newlines` can be named anything we want, it's important to use the name `sbd` for the SentenceSegmenter.</font>

```python
doc = nlp(mystring)
for sent in doc.sents:
    print([token.text for token in sent])
```

**Execution Output:**
```text
['This', 'is', 'a', 'sentence', '.', 'This', 'is', 'another', '.', '\n\n']
['This', 'is', 'a', '\n']
['third', 'sentence', '.']
```

---

## Key Interview Takeaways: Linguistic Annotations

1. **Coarse-grained vs Fine-grained POS Tags**:
   - `token.pos_`: Universal POS tags (e.g., `NOUN`, `VERB`, `ADJ`, `ADV`, `PRON`, `PROPN`, `PUNCT`, `NUM`).
   - `token.tag_`: Detailed Penn Treebank tags capturing tense, number, and aspect (e.g., `VBD` past tense verb, `VBG` gerund/present participle, `NNS` plural noun, `NNP` singular proper noun).
   - Use `spacy.explain(tag)` to inspect any obscure tag definition.
2. **Named Entity Recognition (NER)**:
   - Identifies real-world objects in text such as `PERSON`, `ORG` (companies, institutions), `GPE` (geopolitical entities like countries, cities, states), `DATE`, `TIME`, `MONEY`, `PERCENT`.
   - Spans can be manually injected into `doc.ents` using `Span(doc, start, end, label="ENTITY_LABEL")`.
3. **Rule-Based Matching (`Matcher`)**:
   - Allows finding complex patterns using dictionaries of token attributes:
     - `LOWER`: exact lowercase match.
     - `POS`: part-of-speech match.
     - `IS_PUNCT`, `IS_DIGIT`: boolean flags.
     - Operators `OP`: `'*'` (0 or more), `'+'` (1 or more), `'?'` (0 or 1), `'!'` (negation).
4. **Sentence Segmentation**:
   - In SpaCy, sentences are accessed via `doc.sents` generator.
   - Unlike naive regex splitting on `.` (which breaks on titles like "Dr.", decimals like "3.14", or acronyms like "U.S.A."), SpaCy uses statistical syntactic dependency parse trees to determine true sentence boundaries, or custom pipeline functions modifying `token.is_sent_start`.
