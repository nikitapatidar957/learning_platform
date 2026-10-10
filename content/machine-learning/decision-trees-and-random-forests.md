# Tree-Based Models: Decision Trees & Random Forests

Comprehensive guide to tree-based machine learning algorithms: CART (Classification and Regression Trees), splitting criteria (Gini Impurity, Entropy, Information Gain, Variance Reduction), pre/post-pruning strategies, Ensemble Learning, Bagging (Bootstrap Aggregating), Random Forest architectures, and Out-of-Bag (OOB) error estimation.

---

## 🌳 Introduction to Decision Trees

### Slide 1: Decision Tree



---

### Slide 2: Decision Tree

• A decision tree is a graphical representation of all the possible solutions to a decision based on certain conditions.

• Decision tree is a type of supervised learning algorithm (having a pre-defined target variable) that is mostly used in classification problems.

• The decision tree analyses a data set in order to construct a set of rules, or questions, which are used to predict a class.

• These involve stratifying or segmenting the predictor space into a number of simple regions.

• Example:

• Let us consider a dataset consisting  lots of different animals and some of their characteristics.

• With the help of these characteristics, can predict their class.

• The tree can be explained by two entities, namely decision nodes and leaves. The leaves are the decisions or the final outcomes. And the decision nodes are where the data is split

---

### Slide 3: Types of Decision Tree

• Types of decision tree is based on the type of target variable we have. It can be of two types:

• Categorical Variable Decision Tree: Decision Tree which has categorical target variable. Also we can define it as classification problem.

• Example: based on medical history weather a patient detect with cancer or not.

• Continuous Variable Decision Tree: Decision Tree has continuous target variable or a regression problem.

• Example: to predict the house price based on certain variables.

---

### Slide 4: Terminology used in Decision Tree

• Root Node: It represents entire population or sample and this further gets divided into two or more homogeneous sets.

• Splitting: It is a process of dividing a node into two or more sub-nodes.

• Decision Node: When a sub-node splits into further sub-nodes, then it is called decision node.

• Leaf/ Terminal Node: Nodes do not split is called Leaf or Terminal node.

• Pruning: It reduces the size of decision trees by removing parts of the tree that do not provide power to classify instances.

• Branch / Sub-Tree: A sub section of entire tree is called branch or sub-tree.

• Parent and Child Node: A node, which is divided into sub-nodes is called parent node of sub-nodes where as sub-nodes are the child of parent node.

---

### Slide 5: Split of Tree

• In this procedure all the features are considered and different split points are tried and tested using a cost function. The split with the best cost (or lowest cost) is selected.

• The decision of making strategic splits heavily affects a tree’s accuracy. The decision criteria is different for classification and regression trees.

• we can say that purity of the node increases with respect to the target variable. Decision tree splits the nodes on all available variables and then selects the split which results in most homogeneous sub-nodes.

---

### Slide 6: A Tree Decide Where To Split:

• Gini Index

• The impurity (or purity) measure used in building decision tree in classification is Gini Index.

• It performs only Binary splits

• Higher the value of Gini higher the homogeneity.

• Example:

• There are 30 students, out of which 15 plays cricket.  Identify which split is producing more homogeneous sub-nodes  with the help of Gini index.

---

### Slide 7: A Tree Decide Where To Split:

• Split on Gender:

• Calculate, Gini for sub-node Female = (0.2)*(0.2)+(0.8)*(0.8)=0.68

• Gini for sub-node Male = (0.65)*(0.65)+(0.35)*(0.35)=0.55

• Calculate weighted Gini for Split Gender = (10/30)*0.68+(20/30)*0.55 = 0.59

• Similar for Split on Class:

• Gini for sub-node Class IX = (0.43)*(0.43)+(0.57)*(0.57)=0.51

• Gini for sub-node Class X = (0.56)*(0.56)+(0.44)*(0.44)=0.51

• Calculate weighted Gini for Split Class = (14/30)*0.51+(16/30)*0.51 = 0.51

• Above, Gini score for Split on Gender is higher than Split on Class, hence, the node split will take place on Gender.

---

### Slide 8: Information Gain:

• The attribute with highest information gain is considered the best.

• Less impure node requires less information to describe it.

• And, more impure node requires more information.

• Information theory is measure to define this degree of disorganization in a system known as Entropy.

• If the sample is completely homogenous, then the entropy is zero and if the sample is an equally divided (50% - 50%), it has entropy of one.

---

### Slide 9: Entropy

• Entropy is measure of impurity,  disorder or uncertainty.

• It is measure of randomness, how random the data is.

---

### Slide 10: Let’s consider an example

• Here in the table, Grade and Speed limit are the features and Speed is label

• In the Grade column there are four values and correspond that values there are four labels.

• Lets consider all the labels as a parent node.

• SSFF => parent node

• So, what is the entropy of this parent node ?

• p(slow) = no. of slow examples in parent node / total number of examples

• Similarly, for p(fast)

• Grade

• Speed limit

• Speed

• Steep

• Yes

• Slow

• Steep

• Yes

• Slow

• flat

• no

• fast

• steep

• no

• fast

---

### Slide 11: So, the entropy of parent node:

• Entropy(parent) = - {0.5 log2(0.5) + 0.5 log2(0.5)}                              = - {-0.5 + (-0.5)}                              = 1

• So the entropy of parent node is 1.

• We can derive information gain from entropy as

• Algorithm construct a Decision Tree based on Information gain

• First lets check whether the parent node split by Grade or not.

• To find out Information gain of Grade feature, we need to

• virtually split the parent node by Grade feature.

• Entropy of right child node (F) is 0, because this node belongs

• to the same class.

---

### Slide 12: Lets find out Entropy of the left side node SSF:

• In this node SSF there are two type of examples present, so we need to find out the fraction of slow and fast example separately for this node.

• P(slow) = 2/3 = 0.667      P(fast) = 1/3 = 0.334

• Entropy(SSF) = - {0.667 log2(0.667) + 0.334 log2(0.334)}                       = - {-0.38 + (-0.52)}                        = 0.9

• Now, we need to find out Entropy(children)with weighted average.

• Total number of examples in parent node: 4    # left child node: 3    # right child node: 1

• Entropy(children) with weighted avg. is = 0.675

• So,

• Information gain(Grade) = 1 - 0.675 = 0.325

• Information gain from Grade feature is 0.325 .

---

### Slide 13: Chi-Square

• It is an algorithm to find out the statistical significance between the differences     between sub-nodes and parent node. We measure it by sum of squares of standardized differences between observed and expected frequencies of target variable.

• It works with categorical target variable “Success” or “Failure”.

• It can perform two or more splits.

• Higher the value of Chi-Square, higher the statistical significance of differences between sub-node and Parent node.

• Chi-Square of each node is calculated using formula,

• Chi-square = ((Actual – Expected)^2 / Expected)^1/2

• It generates tree called CHAID (Chi-square Automatic Interaction Detector)

---

### Slide 14: Split on Gender:

• First we are populating for node Female, Populate the actual value for “Play Cricket” and “Not Play Cricket”, here these are 2 and 8 respectively.

• Calculate expected value for “Play Cricket” and “Not Play Cricket”, here it would be 5 for both because parent node has probability of 50% and we have applied same probability on Female count(10).

• Calculate deviations by using formula, Actual — Expected. It is for “Play Cricket” (2–5 = -3) and for “Not play cricket” ( 8–5 = 3).

• Calculate Chi-square of node for “Play Cricket” and “Not Play Cricket” using formula.

• Follow similar steps for calculating Chi-square value for Male node.

• Now add all Chi-square values to calculate Chi-square for split Gender.

---

### Slide 15: Split on Class:

• Perform similar steps of calculation for split on Class and you will come up with below table.

---

### Slide 16: Reduction in Variance

• Reduction in variance is an algorithm used for continuous target variables (regression problems).

• This algorithm uses the standard formula of variance to choose the best split. The split with lower variance is selected as the criteria to split the population:

• variance =

• Above X-bar is mean of the values, X is actual and n is number of values.

• Example:- Let’s assign numerical value 1 for play cricket and 0 for not playing cricket. Now follow the steps to identify the right split:

• Variance for Root node, here mean value is (15*1 + 15*0)/30 = 0.5 and we have 15 one and 15 zero. Now variance would be ((1–0.5)²+(1–0.5)²+….15 times+(0–0.5)²+(0–0.5)²+…15 times) / 30, this can be written as (15*(1–0.5)²+15*(0–0.5)²) / 30 = 0.25

• Mean of Female node = (2*1+8*0)/10=0.2 and Variance = (2*(1–0.2)²+8*(0–0.2)²) / 10 = 0.16

• Mean of Male Node = (13*1+7*0)/20=0.65 and Variance = (13*(1–0.65)²+7*(0–0.65)²) / 20 = 0.23

• Variance for Split Gender = Weighted Variance of Sub-nodes = (10/30)*0.16 + (20/30) *0.23 = 0.21

---

### Slide 17: Reduction in Variance

• Mean of Class IX node = (6*1+8*0)/14=0.43 and Variance = (6*(1–0.43)²+8*(0–0.43)²) / 14= 0.24

• Mean of Class X node = (9*1+7*0)/16=0.56 and Variance = (9*(1–0.56)²+7*(0–0.56)²) / 16 = 0.25

• Variance for Split Gender = (14/30)*0.24 + (16/30) *0.25 = 0.25

• Above, you can see that Gender split has lower variance compare to parent node, so the split would take place on Gender variable.

---

### Slide 18: Pruning

• One of the questions that arises in a decision tree algorithm is the optimal size of the final tree.

• A tree that is too large risks overfitting the training data and poorly generalizing to new samples.

• A small tree might not capture important structural information about the sample space

• A common strategy is to grow the tree until each node contains a small number of instances then use pruning to remove nodes that do not provide additional information.

• We start at the bottom and start removing leaves which are giving us negative returns when compared from the top.

---

### Slide 19: THANK YOU FOR YOURATTENTATION




---

## 🌲 Decision Trees for Regression


<a name='0'></a>
# Decision Trees for Regression

### Contents

* [1 - Imports](#1)
* [2 - Loading the data](#2)
* [3 - Exploratory Analysis](#3)
* [4 - Preprocessing the data](#4)
* [5 - Training Decision Trees](#5)
* [6 - Evaluating Decision Trees](#6)
* [7 - Improving Decision Trees](#7)

<a name='1'></a>
## 1 - Imports

```python
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn
import matplotlib.pyplot as plt
%matplotlib inline
```

<a name='2'></a>

## 2 - Loading the data

In this regression task with decision trees, we will use the Machine CPU (Central Processing Unit) data which is avilable at [OpenML](https://www.openml.org/t/5492). We will load it with Sklearn `fetch_openml` function. 

If you are reading this, it's very likely that you know CPU or you have once(or many times) thought about it when you were buying your computer. In this notebook, we will predict the relative performance of the CPU given the following data: 

* MYCT: machine cycle time in nanoseconds (integer)
* MMIN: minimum main memory in kilobytes (integer)
* MMAX: maximum main memory in kilobytes (integer)
* CACH: cache memory in kilobytes (integer)
* CHMIN: minimum channels in units (integer)
* CHMAX: maximum channels in units (integer)
* PRP: published relative performance (integer) (target variable)

```python
# Let's hide warnings

import warnings
warnings.filterwarnings('ignore')
```

```python
from sklearn.datasets import fetch_openml

machine_cpu = fetch_openml(name='machine_cpu')
```

```python
type(machine_cpu)
```

**Output:**
```text
sklearn.utils.Bunch
```

```python
machine_cpu.data.shape
```

**Output:**
```text
(209, 6)
```

```python
print(machine_cpu.DESCR)
```

**Output:**
```text
**Author**:   
**Source**: Unknown -   
**Please cite**:   

The problem concerns Relative CPU Performance Data. More information can be obtained in the UCI Machine
 Learning repository (http://www.ics.uci.edu/~mlearn/MLSummary.html).
 The used attributes are :
 MYCT: machine cycle time in nanoseconds (integer)
 MMIN: minimum main memory in kilobytes (integer)
 MMAX: maximum main memory in kilobytes (integer)
 CACH: cache memory in kilobytes (integer)
 CHMIN: minimum channels in units (integer)
 CHMAX: maximum channels in units (integer)
 PRP: published relative performance (integer) (target variable)
 
 Original source: UCI machine learning repository. 
 Source: collection of regression datasets by Luis Torgo (ltorgo@ncc.up.pt) at
 http://www.ncc.up.pt/~ltorgo/Regression/DataSets.html
 Characteristics: 209 cases; 6 continuous variables

Downloaded from openml.org.
```

```python
# Displaying feature names

machine_cpu.feature_names
```

**Output:**
```text
['MYCT', 'MMIN', 'MMAX', 'CACH', 'CHMIN', 'CHMAX']
```

```python
# Getting the whole dataframe

machine_cpu.frame
```

**Output:**
```text
MYCT    MMIN     MMAX   CACH  CHMIN  CHMAX  class
0    125.0   256.0   6000.0  256.0   16.0  128.0  198.0
1     29.0  8000.0  32000.0   32.0    8.0   32.0  269.0
2     29.0  8000.0  32000.0   32.0    8.0   32.0  220.0
3     29.0  8000.0  32000.0   32.0    8.0   32.0  172.0
4     29.0  8000.0  16000.0   32.0    8.0   16.0  132.0
..     ...     ...      ...    ...    ...    ...    ...
204  124.0  1000.0   8000.0    0.0    1.0    8.0   42.0
205   98.0  1000.0   8000.0   32.0    2.0    8.0   46.0
206  125.0  2000.0   8000.0    0.0    2.0   14.0   52.0
207  480.0   512.0   8000.0   32.0    0.0    0.0   67.0
208  480.0  1000.0   4000.0    0.0    0.0    0.0   45.0

[209 rows x 7 columns]
```

Now, let's get the data and labels.

```python
machine_data = machine_cpu.data
machine_labels = machine_cpu.target
```

```python
type(machine_data)
```

**Output:**
```text
pandas.core.frame.DataFrame
```

```python
type(machine_labels)
```

**Output:**
```text
pandas.core.series.Series
```

<a name='3'></a>
## 3 - Exploratory Analysis

Before doing exploratory analysis, let's get the training and test data.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(machine_data,machine_labels, test_size=0.2,random_state=20)

print('The size of training data is: {} \nThe size of testing data is: {}'.format(len(X_train), len(X_test)))
```

**Output:**
```text
The size of training data is: 167 
The size of testing data is: 42
```

Let's visualize the histograms of all numeric features.

```python
X_train.hist(bins=50, figsize=(15,10))
plt.show()
```

Or we can quickly use `sns.pairplot()` to look into the data.

```python
sns.pairplot(X_train)
```

```python
# Checking summary stats

X_train.describe()
```

**Output:**
```text
MYCT          MMIN          MMAX        CACH       CHMIN  \
count   167.000000    167.000000    167.000000  167.000000  167.000000   
mean    207.958084   2900.826347  11761.161677   26.071856    4.760479   
std     266.772823   4165.950964  12108.332354   42.410014    6.487439   
min      17.000000     64.000000     64.000000    0.000000    0.000000   
25%      50.000000    768.000000   4000.000000    0.000000    1.000000   
50%     110.000000   2000.000000   8000.000000    8.000000    2.000000   
75%     232.500000   3100.000000  16000.000000   32.000000    6.000000   
max    1500.000000  32000.000000  64000.000000  256.000000   52.000000   

            CHMAX  
count  167.000000  
mean    18.616766  
std     27.489919  
min      0.000000  
25%      5.000000  
50%      8.000000  
75%     24.000000  
max    176.000000
```

```python
# Checking missing values

X_train.isnull().sum()
```

**Output:**
```text
MYCT     0
MMIN     0
MMAX     0
CACH     0
CHMIN    0
CHMAX    0
dtype: int64
```

We don't have any missing values.

<a name='4'></a>

## 4 - Data Preprocessing 

It is here that we prepare the data to be in the proper format for the machine learning model. 

Decision trees don't care if the features are scaled or not. Let's set up a pipeline to scale features, and we will use it to verify that notion.

```python
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

scale_pipe = Pipeline([
    ('scaler', StandardScaler())
    
])

X_train_scaled = scale_pipe.fit_transform(X_train)
```

<a name='5'></a>

## 5 - Training Decision Tree Regressor

```python
from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor()

tree_reg.fit(X_train, y_train)
```

**Output:**
```text
DecisionTreeRegressor()
```

Let's train the same model on the scaled data.

```python
tree_reg_scaled = DecisionTreeRegressor()

tree_reg_scaled.fit(X_train_scaled, y_train)
```

**Output:**
```text
DecisionTreeRegressor()
```

<a name='6'></a>

## 6 - Evaluating Decision Trees

Let's first check the root mean squarred errr on the training. It is not advised to evaluate the model on the test data since we haven't improved it yet. I will make a function to make it easier and to avoid repetitions.

```python
from sklearn.metrics import mean_squared_error

def predict(input_data,model,labels):
    """
    Take the input data, model and labels and return predictions
    
    """
    
    preds = model.predict(input_data)
    mse = mean_squared_error(labels,preds)
    rmse = np.sqrt(mse)
    rmse
    
    return rmse
```

```python
predict(X_train, tree_reg, y_train)
```

**Output:**
```text
9.724590719956222
```

And when the training data is scaled...

```python
predict(X_train_scaled, tree_reg_scaled, y_train)
```

**Output:**
```text
9.724590719956222
```

As you can see, there is no difference at all. So in your future projects using decision trees, whether you scale the data or not, your predictions will not be affected. 

But don't do this....

```python
predict(X_train_scaled, tree_reg, y_train)
```

**Output:**
```text
201.29511805033474
```

If you can inspect the parameters that I passed in predict function above, there are scaled data, model trained on unscaled data, and labels(y_train). As you may have guessed, that is a complete mismatch which led to poor results. If you trained a model on scaled data, the data that you predict the model on should be scaled in the same way too. 

Let's try to improve the model.

<a name='7'></a>

## 7 - Improving Decision Trees

```python
tree_reg.get_params()
```

**Output:**
```text
{'ccp_alpha': 0.0,
 'criterion': 'mse',
 'max_depth': None,
 'max_features': None,
 'max_leaf_nodes': None,
 'min_impurity_decrease': 0.0,
 'min_impurity_split': None,
 'min_samples_leaf': 1,
 'min_samples_split': 2,
 'min_weight_fraction_leaf': 0.0,
 'random_state': None,
 'splitter': 'best'}
```

We have seen that one way to improve the decision tree model is to find the right number of max_depth and some other few parameters. Let's use GridSearch to find best hyperparameters. Note that this may end up overfitting because we have a small dataset. But since we are doing this for learning purpose (you can adapt it to your problem), let's do it.

```python
from sklearn.model_selection import GridSearchCV

params_grid = {'max_leaf_nodes': list(range(0, 10)), 'min_samples_split': [0,1,2, 3, 4], 
              'max_depth':[None,0,1,2,3]}

#refit is true by default. The best estimator is trained on the whole dataset 

grid_search = GridSearchCV(DecisionTreeRegressor(random_state=42), params_grid, verbose=1, cv=3, refit=True)

grid_search.fit(X_train, y_train)
```

**Output:**
```text
Fitting 3 folds for each of 250 candidates, totalling 750 fits
GridSearchCV(cv=3, estimator=DecisionTreeRegressor(random_state=42),
             param_grid={'max_depth': [None, 0, 1, 2, 3],
                         'max_leaf_nodes': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                         'min_samples_split': [0, 1, 2, 3, 4]},
             verbose=1)
```

```python
grid_search.best_params_
```

**Output:**
```text
{'max_depth': None, 'max_leaf_nodes': 9, 'min_samples_split': 4}
```

```python
grid_search.best_estimator_
```

**Output:**
```text
DecisionTreeRegressor(max_leaf_nodes=9, min_samples_split=4, random_state=42)
```

```python
tree_best = grid_search.best_estimator_
```

Let's make prediction on the training data again

```python
predict(X_train, tree_best, y_train)
```

**Output:**
```text
34.999530266023044
```

Like we said, we overfitted. The RMSE on our small dataset was pretty enough (and you probably would not use decision trees for small data like this we are using). 

Finally we can evaluate the model on the test set. Let's use the orginal model.

```python
predict(X_test, tree_reg, y_test)
```

**Output:**
```text
42.89411103991738
```

Clearly, the model overfitted and the improvements we tried didn't improve anything. This is not an issue of the model or our approach to improve the model. Decision trees are complex models for the data we have.

This is the end of the notebook. We have learned the fundamental idea behind the decision trees, and used it to predict the CPU performance. In the next lab, we will use it for classification task and we will use a real world dataset so that we can practically improve the decision trees model.

[Back to top](#0)


---

## 🌲 Decision Trees for Classification


<a name='0'></a>
# 6.6 Decision Trees for Classification

### Contents

* [1 - Imports](#1)
* [2 - Loading the data](#2)
* [3 - Exploratory Analysis](#3)
* [4 - Preprocessing the data](#4)
* [5 - Training Decision Trees](#5)
* [6 - Evaluating Decision Trees](#6)
* [7 - Improving Decision Trees](#7)

<a name='1'></a>
## 1 - Imports

```python
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn
import matplotlib.pyplot as plt
%matplotlib inline
```

<a name='2'></a>

## 2 - Loading the data

In this classification task with decision trees, we will use a car dataset that is avilable at [OpenML](https://www.openml.org/d/21) to predict the car acceptability given the information about the car. We will load it with Sklearn `fetch_openml` function. 

The version of the data we are fetching is 2. In the version 1 of the dataset, the target class had 4 classes (unacc, acc, good, vgood) but in the second version, the majority class is Positive(P) whereas the rest are Negative(P). If you want to see version 1, you can change version parameter in a cell below. 


Here are the informations about the features:

* *buying*: The buying price of the car(vhigh, high, med, low)
* maint: The maintainance price of the car(high, high, med, low)
* *doors*: The number of doors (2,3,4,5more)
* *persons*: The number of persons that can be carried the car. They are 2, 4, and more. 
* *lug_boot*: The size of the luggage boot (small, med, big)
* *safety*: Estimated safefy of the car(low, med, high)
* *BinaryClass(target feature)*: The car acceptability class. Either positive(P) or negative(N).

```python
from sklearn.datasets import fetch_openml

car_data = fetch_openml(name='car', version=2)
```

```python
type(car_data)
```

**Output:**
```text
sklearn.utils.Bunch
```

```python
car_data.details
```

**Output:**
```text
{'id': '991',
 'name': 'car',
 'version': '2',
 'description_version': '1',
 'format': 'ARFF',
 'upload_date': '2014-10-04T22:44:31',
 'licence': 'Public',
 'url': 'https://www.openml.org/data/v1/download/53525/car.arff',
 'file_id': '53525',
 'default_target_attribute': 'binaryClass',
 'tag': ['derived',
  'mythbusting_1',
  'study_1',
  'study_15',
  'study_20',
  'study_41',
  'study_7'],
 'visibility': 'public',
 'minio_url': 'http://openml1.win.tue.nl/dataset991/dataset_991.pq',
 'status': 'active',
 'processing_date': '2020-11-20 20:17:54',
 'md5_checksum': '49c57b793eef1b8e55f297e5e019fdbf'}
```

```python
car_data.details['version']
```

**Output:**
```text
'2'
```

```python
# Data description 

print(car_data.DESCR)
```

**Output:**
```text
**Author**:   
**Source**: Unknown - Date unknown  
**Please cite**:   

Binarized version of the original data set (see version 1). The multi-class target feature is converted to a two-class nominal target feature by re-labeling the majority class as positive ('P') and all others as negative ('N'). Originally converted by Quan Sun.

Downloaded from openml.org.
```

```python
# Displaying feature names

car_data.feature_names
```

**Output:**
```text
['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']
```

```python
# Getting the whole dataframe

car_data = car_data.frame
car_data.head()
```

**Output:**
```text
buying  maint doors persons lug_boot safety binaryClass
0  vhigh  vhigh     2       2    small    low           P
1  vhigh  vhigh     2       2    small    med           P
2  vhigh  vhigh     2       2    small   high           P
3  vhigh  vhigh     2       2      med    low           P
4  vhigh  vhigh     2       2      med    med           P
```

```python
type(car_data)
```

**Output:**
```text
pandas.core.frame.DataFrame
```

<a name='3'></a>
## 3 - Exploratory Analysis

Before doing exploratory analysis, let's get the training and test data.

### Splitting Data into Training and Test sets

```python
from sklearn.model_selection import train_test_split

train_data, test_data = train_test_split(car_data, test_size=0.1,random_state=20)

print('The size of training data is: {} \nThe size of testing data is: {}'.format(len(train_data), len(test_data)))
```

**Output:**
```text
The size of training data is: 1555 
The size of testing data is: 173
```

### Checking Summary Statistics

```python
# Checking summary statistics

train_data.describe()
```

**Output:**
```text
buying maint doors persons lug_boot safety binaryClass
count    1555  1555  1555    1555     1555   1555        1555
unique      4     4     4       3        3      3           2
top       med   low     2       2      med    low           P
freq      402   392   393     521      522    528        1097
```

### Checking Missing Values

```python
# Checking missing values
train_data.isnull().sum()
```

**Output:**
```text
buying         0
maint          0
doors          0
persons        0
lug_boot       0
safety         0
binaryClass    0
dtype: int64
```

We don't have any missing values.

### Checking Categorical Features

Let's inspect some categorical features that are in the dataset, almost all re. Let's see that!

```python
train_data['buying'].value_counts()
```

**Output:**
```text
med      402
vhigh    387
high     385
low      381
Name: buying, dtype: int64
```

```python
plt.figure(figsize=(15,10))
sns.countplot(data=train_data, x='buying')
```

```python
plt.figure(figsize=(15,10))
sns.countplot(data=train_data, x='buying', hue='binaryClass')
```

As you can see above, the majority class in the buying price is median(`med`).

```python
train_data['maint'].value_counts()
```

**Output:**
```text
low      392
med      390
high     387
vhigh    386
Name: maint, dtype: int64
```

```python
plt.figure(figsize=(15,10))
sns.countplot(data=train_data, x='maint')
```

```python
plt.figure(figsize=(15,10))
sns.countplot(data=train_data, x='maint', hue='binaryClass')
```

Let's also check what's in doors.

```python
train_data['doors'].value_counts()
```

**Output:**
```text
2        393
4        393
5more    389
3        380
Name: doors, dtype: int64
```

```python
plt.figure(figsize=(15,10))
sns.countplot(data=train_data, x='doors')
```

```python
plt.figure(figsize=(15,10))
sns.countplot(data=train_data, x='doors', hue='binaryClass')
```

Nothing stunning in the maintenance cost. All cars share the same maintenance costs.

```python
train_data['persons'].value_counts()
```

**Output:**
```text
2       521
more    521
4       513
Name: persons, dtype: int64
```

```python
plt.figure(figsize=(15,10))
sns.countplot(data=train_data, x='persons', hue='binaryClass')
```

```python
train_data['lug_boot'].value_counts()
```

**Output:**
```text
med      522
small    517
big      516
Name: lug_boot, dtype: int64
```

```python
plt.figure(figsize=(15,10))
sns.countplot(data=train_data, x='lug_boot', hue='binaryClass')
```

```python
train_data['safety'].value_counts()
```

**Output:**
```text
low     528
high    514
med     513
Name: safety, dtype: int64
```

```python
plt.figure(figsize=(15,10))
sns.countplot(data=train_data, x='safety', hue='binaryClass')
```

```python
train_data['binaryClass'].value_counts()
```

**Output:**
```text
P    1097
N     458
Name: binaryClass, dtype: int64
```

```python
plt.figure(figsize=(15,10))
sns.countplot(data=train_data, x='binaryClass')
```

As you can see, our data is completely skewed/imbalanced. The positive examples are 2x more than negative examples. 

So we will remember during the model evaluation that accuracy is not the right metric in this case. Real world datasets comes with their unique blends, dataset can be imbalanced. Missing values can be present. We just have to find the effective way to deal with those issues. So again for evaluation, we will not rely on accuracy.

<a name='4'></a>

## 4 - Data Preprocessing 

It is here that we prepare the data to be in the proper format for the machine learning model. 

### Handling Categorical Features

Decision trees don't care if the features are scaled or not, and they can handle the categorical features. There is a [note on documentation](https://scikit-learn.org/stable/modules/tree.html#tree) that the sklearn tree implementation doesn't support categorical features, so I will go ahead and handle them. It's fun anyways :)

Before handling categorical features, let's create a training input data and labels.

```python
car_train = train_data.drop('binaryClass', axis=1)
car_labels = train_data[['binaryClass']]
```

Let's create a pipeline to encode all features in the training input data.

```python
from sklearn.preprocessing import OrdinalEncoder

from sklearn.pipeline import Pipeline

pipe = Pipeline([
    ('ord_enc', OrdinalEncoder())
    
])

car_train_prepared = pipe.fit_transform(car_train)
```

Let's also handle labels. Labels contain P and N, so we want to convert those into numbers. Here instead of using Ordinary Encoder, we will use Label Encoder. Sklearn is explicity that it is used to encode target features.

```python
from sklearn.preprocessing import LabelEncoder


label_enc = LabelEncoder()

car_labels_prepared = label_enc.fit_transform(car_labels)
```

<a name='5'></a>

## 5 - Training Decision Tree Classifier

```python
from sklearn.tree import DecisionTreeClassifier

tree_clf = DecisionTreeClassifier()

tree_clf.fit(car_train_prepared, car_labels_prepared)
```

**Output:**
```text
DecisionTreeClassifier()
```

Let's train the same model on the scaled data.

```python
# if you run this, it will be error. 
# SKlearn tree implementation doesn't support categorical features

#from sklearn.tree import DecisionTreeClassifier

#tree_clf = DecisionTreeClassifier()

#tree_clf.fit(car_train, car_labels)
```

<a name='6'></a>

## 6 - Evaluating Decision Trees

Let's build 3 functions to display accuracy, confusion matrix, and classification report. Classification report contains all useful metrics such as precision, recall, and f1 score.

```python
from sklearn.metrics import accuracy_score

def accuracy(input_data,model,labels):
    """
    Take the input data, model and labels and return accuracy
    
    """
    
    preds = model.predict(input_data)
    acc = accuracy_score(labels,preds)
    
    return acc
```

```python
from sklearn.metrics import confusion_matrix

def conf_matrix(input_data,model,labels):
    """
    Take the input data, model and labels and return confusion matrix
    
    """
    
    preds = model.predict(input_data)
    cm = confusion_matrix(labels,preds)
    
    return cm
```

```python
from sklearn.metrics import classification_report

def class_report(input_data,model,labels):
    """
    Take the input data, model and labels and return confusion matrix
    
    """
    
    preds = model.predict(input_data)
    report = classification_report(labels,preds)
    report = print(report)
    
    return report
```

Let's find the accuracy on the training set.

```python
accuracy(car_train_prepared, tree_clf, car_labels_prepared)
```

**Output:**
```text
1.0
```

Ohh, see! The decision trees overfitted the dataset. Also if we remember well, our data is not balanced. We have many positive examples than negative examples.

```python
conf_matrix(car_train_prepared, tree_clf, car_labels_prepared)
```

**Output:**
```text
array([[ 458,    0],
       [   0, 1097]])
```

```python
class_report(car_train_prepared, tree_clf, car_labels_prepared)
```

**Output:**
```text
precision    recall  f1-score   support

           0       1.00      1.00      1.00       458
           1       1.00      1.00      1.00      1097

    accuracy                           1.00      1555
   macro avg       1.00      1.00      1.00      1555
weighted avg       1.00      1.00      1.00      1555
```

The model clearly overfitted the data. Let's see how we can regularize it.

<a name='7'></a>

## 7 - Improving Decision Trees

```python
tree_clf.get_params()
```

**Output:**
```text
{'ccp_alpha': 0.0,
 'class_weight': None,
 'criterion': 'gini',
 'max_depth': None,
 'max_features': None,
 'max_leaf_nodes': None,
 'min_impurity_decrease': 0.0,
 'min_impurity_split': None,
 'min_samples_leaf': 1,
 'min_samples_split': 2,
 'min_weight_fraction_leaf': 0.0,
 'random_state': None,
 'splitter': 'best'}
```

One way to avoid overfitting is reduce number maximum depth of the tree, set by the hyperparameter `max_depth`. Similarly, we can attempt to reduce all hyperparameters with `max`term while also increasing the `min_` term parameters. 

Also, I set the `class_weight` to `balanced` because our dataset is imbalanced. By setting it to balanced, the model will automatically adjust the class weight based on the number of available samples in all classes. 


Let's use GridSearch to find best values of these hyperparameters.

```python
# Let's hide warnings returned by grid search

import warnings
warnings.filterwarnings('ignore')
```

```python
from sklearn.model_selection import GridSearchCV

params_grid = {'max_leaf_nodes': list(range(0, 10)), 
               'min_samples_split': [0,1,2, 3, 4], 
               'min_samples_leaf': [0,1,2, 3, 4], 
               'max_depth':[0,1,2,3,4,5],
               'max_features':[0,1,2,3,4,5],
              'max_leaf_nodes':[0,1,2,3,4,5]}

#refit is true by default. The best estimator is trained on the whole dataset 

grid_search = GridSearchCV(DecisionTreeClassifier(random_state=42, class_weight='balanced'), params_grid, verbose=1, cv=3, refit=True)

grid_search.fit(car_train_prepared, car_labels_prepared)
```

**Output:**
```text
Fitting 3 folds for each of 5400 candidates, totalling 16200 fits
GridSearchCV(cv=3,
             estimator=DecisionTreeClassifier(class_weight='balanced',
                                              random_state=42),
             param_grid={'max_depth': [0, 1, 2, 3, 4, 5],
                         'max_features': [0, 1, 2, 3, 4, 5],
                         'max_leaf_nodes': [0, 1, 2, 3, 4, 5],
                         'min_samples_leaf': [0, 1, 2, 3, 4],
                         'min_samples_split': [0, 1, 2, 3, 4]},
             verbose=1)
```

```python
grid_search.best_params_
```

**Output:**
```text
{'max_depth': 4,
 'max_features': 5,
 'max_leaf_nodes': 5,
 'min_samples_leaf': 1,
 'min_samples_split': 2}
```

```python
grid_search.best_estimator_
```

**Output:**
```text
DecisionTreeClassifier(class_weight='balanced', max_depth=4, max_features=5,
                       max_leaf_nodes=5, random_state=42)
```

```python
tree_best = grid_search.best_estimator_
```

We can also plot the tree of the improved model.

```python
car_data.columns
```

**Output:**
```text
Index(['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety',
       'binaryClass'],
      dtype='object')
```

```python
from sklearn.tree import plot_tree

plt.figure(figsize=(20,15))
plot_tree(tree_best, feature_names=car_train.columns, class_names=['N','P']);
```

Let's make prediction on the training data again.

```python
accuracy(car_train_prepared, tree_best, car_labels_prepared)
```

**Output:**
```text
0.8926045016077171
```

```python
conf_matrix(car_train_prepared, tree_best, car_labels_prepared)
```

**Output:**
```text
array([[430,  28],
       [139, 958]])
```

In confusion matrix, each row represent an actual class and each column represents predicted class. 

So, from the results above:

* 430 negative examples(N) were correcty predicted as negatives(`true negatives`).
* 28 negatives examples(N) were incorrectly classified as positive examples when they are in fact negatives(`false positives`).
* 139 positive examples were incorrectly classified as negative(N) when in fact they are positives(P) (`false negatives`).
* 958 were correctly classified as positive examples(`true positives`).

```python
class_report(car_train_prepared, tree_best, car_labels_prepared)
```

**Output:**
```text
precision    recall  f1-score   support

           0       0.76      0.94      0.84       458
           1       0.97      0.87      0.92      1097

    accuracy                           0.89      1555
   macro avg       0.86      0.91      0.88      1555
weighted avg       0.91      0.89      0.90      1555
```

Wow, this is much better. By only setting the class weight to `balanced` and finding the best values of the hyperparameters, we were able to improve our model. 

If you remember, the negative class has fewer examples than the positive classes. You can see them in `support` in classification report. But our model is able to identify them correctly at 76%, and also is able to identify the positive examples at 97% without overfitting. That is precision. 

A few notes about Precison/Recall/F1 score:

* Precision is the model accuracy on predicting positive examples correctly. 
* Recall is the ratio of the positive examples that are correctly identified by the model. 

* F1 score is the harmonic mean of precision and recall. 

The higher the precision and recall are, the higher the F1 score. But there is a tradeoff between them. Increasing precision will reduce recall, and vice versa. So it's fair to say that it depends on the problem you're trying to solve and the metrics you want to optimize for.

### Evaluating the model on the test set

It is only after we have improved the model that we can feed it to the test set. If we try to show the test set to the model while we are still training, we may cause a potential leak thus producing misleading predictions. 

Also, we will apply the same processing functions that we applied to the training set.

```python
car_test = test_data.drop('binaryClass', axis=1)
car_test_labels = test_data['binaryClass']
```

```python
# Handling the categorical features with the pipeline that we defined early
# We don't fit on the test data. Only transform

car_test_prepared = pipe.transform(car_test)
```

```python
# Handle labels too

car_test_labels_prepared = label_enc.transform(car_test_labels)
```

Now we can make predictions on the test set. We will only have to call the metrics functions we created previously.

```python
accuracy(car_test_prepared, tree_best, car_test_labels_prepared)
```

**Output:**
```text
0.8554913294797688
```

```python
conf_matrix(car_test_prepared, tree_best, car_test_labels_prepared)
```

**Output:**
```text
array([[53,  7],
       [18, 95]])
```

```python
class_report(car_test_prepared, tree_best, car_test_labels_prepared)
```

**Output:**
```text
precision    recall  f1-score   support

           0       0.75      0.88      0.81        60
           1       0.93      0.84      0.88       113

    accuracy                           0.86       173
   macro avg       0.84      0.86      0.85       173
weighted avg       0.87      0.86      0.86       173
```

The model never saw the test set but as you can see, the results are truly remarkable. The model can generalize well on the test set and that is because we improved it in the right ways.

This is the end of the notebook. We have learned how to build and how to regularize( or handle overfitting) the decion trees classifier.

[Back to top](#0)


---

## 🌲🌲🌲 Random Forest Classifier & Feature Importances


<a class="anchor" id="0"></a>
# **Random Forest Classifier Tutorial with Python**


Random Forest is a supervised machine learning algorithm which is based on ensemble learning. In this kernel, Two Random Forest Classifier models is built to predict the safety of the car, one with 10 decision-trees and another one with 100 decision-trees. The expected accuracy increases with number of decision-trees in the model. **Feature selection process** is also demonstrated using the Random Forest model to find only the important features, rebuild the model using these features and see its effect on accuracy.

<a class="anchor" id="0.1"></a>
# **Table of Contents**


1.	[Introduction to Random Forest algorithm](#1)
2.	[Random Forest algorithm intuition](#2)
3.	[Advantages and disadvantages of Random Forest algorithm](#3)
4.	[Feature selection with Random Forests](#4)
5.	[Difference between Random Forests and Decision-Trees](#5)
6.	[Relationship to nearest neighbours](#6)
7.	[Import libraries](#7)
8.	[Import dataset](#8)
9.	[Exploratory data analysis](#9)
10.	[Declare feature vector and target variable](#10)
11.	[Split data into separate training and test set](#11)
12.	[Feature engineering](#12)
13.	[Random Forest Classifier model with default parameters](#13)
14.	[Random Forest Classifier model with parameter n_estimators=100](#14)
15.	[Find important features with Random Forest model](#15)
16.	[Visualize the feature scores of the features](#16)
17.	[Build the Random Forest model on selected features](#17)
18.	[Confusion matrix](#18)
19.	[Classification report](#19)
20.	[Results and conclusion](#20)
21. [References](#21)
22. [References](#22)

# **1. Introduction to Random Forest algorithm** <a class="anchor" id="1"></a>

[Table of Contents](#0.1)


Random forest is a supervised learning algorithm. It has two variations – one is used for classification problems and other is used for regression problems. It is one of the most flexible and easy to use algorithm. It creates decision trees on the given data samples, gets prediction from each tree and selects the best solution by means of voting. It is also a pretty good indicator of feature importance.


Random forest algorithm combines multiple decision-trees, resulting in a forest of trees, hence the name `Random Forest`. In the random forest classifier, the higher the number of trees in the forest results in higher accuracy.

# **2. Random Forest algorithm intuition** <a class="anchor" id="2"></a>

[Table of Contents](#0.1)


Random forest algorithm intuition can be divided into two stages. 


In the first stage, we randomly select “k” features out of total `m` features and build the random forest. In the first stage, we proceed as follows:-

1.	Randomly select `k` features from a total of `m` features where `k < m`.
2.	Among the `k` features, calculate the node `d` using the best split point.
3.	Split the node into daughter nodes using the best split.
4.	Repeat 1 to 3 steps until `l` number of nodes has been reached.
5.	Build forest by repeating steps 1 to 4 for `n` number of times to create `n` number of trees.


In the second stage, we make predictions using the trained random forest algorithm. 

1.	We take the test features and use the rules of each randomly created decision tree to predict the outcome and stores the predicted outcome.
2.	Then, we calculate the votes for each predicted target.
3.	Finally, we consider the high voted predicted target as the final prediction from the random forest algorithm.

### Random Forest algorithm intuition

![Random Forest](https://i.ytimg.com/vi/goPiwckWE9M/maxresdefault.jpg)

# **3. Advantages and disadvantages of Random Forest algorithm** <a class="anchor" id="3"></a>

[Table of Contents](#0.1)


The advantages of Random forest algorithm are as follows:-


1.	Random forest algorithm can be used to solve both classification and regression problems.
2.	It is considered as very accurate and robust model because it uses large number of decision-trees to make predictions.
3.	Random forests takes the average of all the predictions made by the decision-trees, which cancels out the biases. So, it does not suffer from the overfitting problem. 
4.	Random forest classifier can handle the missing values. There are two ways to handle the missing values. First is to use median values to replace continuous variables and second is to compute the proximity-weighted average of missing values.
5.	Random forest classifier can be used for feature selection. It means selecting the most important features out of the available features from the training dataset.


The disadvantages of Random Forest algorithm are listed below:-


1.	The biggest disadvantage of random forests is its computational complexity. Random forests is very slow in making predictions because large number of decision-trees are used to make predictions. All the trees in the forest have to make a prediction for the same input and then perform voting on it. So, it is a time-consuming process.
2.	The model is difficult to interpret as compared to a decision-tree, where we can easily make a prediction as compared to a decision-tree.

# **4. Feature selection with Random Forests** <a class="anchor" id="4"></a>

[Table of Contents](#0.1)



Random forests algorithm can be used for feature selection process. This algorithm can be used to rank the importance of variables in a regression or classification problem. 


We measure the variable importance in a dataset by fitting the random forest algorithm to the data. During the fitting process, the out-of-bag error for each data point is recorded and averaged over the forest. 


The importance of the j-th feature was measured after training. The values of the j-th feature were permuted among the training data and the out-of-bag error was again computed on this perturbed dataset. The importance score for the j-th feature is computed by averaging the difference in out-of-bag error before and after the permutation over all trees. The score is normalized by the standard deviation of these differences.


Features which produce large values for this score are ranked as more important than features which produce small values. Based on this score, we will choose the most important features and drop the least important ones for model building.

# **5. Difference between Random Forests and Decision Trees** <a class="anchor" id="5"></a>

[Table of Contents](#0.1)


I will compare random forests with decision-trees. Some salient features of comparison are as follows:-

1. Random forests is a set of multiple decision-trees.

2. Decision-trees are computationally faster as compared to random forests.

3. Deep decision-trees may suffer from overfitting. Random forest prevents overfitting by creating trees on random forests.

4. Random forest is difficult to interpret. But, a decision-tree is easily interpretable and can be converted to rules.

# **6. Relationship to nearest neighbours** <a class="anchor" id="6"></a>

[Table of Contents](#0.1)


A relationship between random forests and the k-nearest neighbours algorithm was pointed out by Lin and Jeon in 2002. It turns out that both can be viewed as so-called weighted neighbourhoods schemes. These are models built from a training set that make predictions for new points by looking at the neighbourhood of the point, formalized by a weight function.

# **7. Import libraries** <a class="anchor" id="7"></a>

[Table of Contents](#0.1)

```python
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # data visualization
import seaborn as sns # statistical data visualization
%matplotlib inline
```

```python
import warnings

warnings.filterwarnings('ignore')
```

# **8. Import dataset** <a class="anchor" id="8"></a>

[Table of Contents](#0.1)

```python
data = 'car_evaluation.csv'

df = pd.read_csv(data, header=None)
```

# **9. Exploratory data analysis** <a class="anchor" id="9"></a>

[Table of Contents](#0.1)


Now, Let's explore the data to gain insights about the data.

```python
# view dimensions of dataset

df.shape
```

**Output:**
```text
(1728, 7)
```

We can see that there are 1728 instances and 7 variables in the data set.

### View top 5 rows of dataset

```python
# preview the dataset

df.head()
```

**Output:**
```text
0      1  2  3      4     5      6
0  vhigh  vhigh  2  2  small   low  unacc
1  vhigh  vhigh  2  2  small   med  unacc
2  vhigh  vhigh  2  2  small  high  unacc
3  vhigh  vhigh  2  2    med   low  unacc
4  vhigh  vhigh  2  2    med   med  unacc
```

### Rename column names

We can see that the dataset does not have proper column names. The columns are merely labelled as 0,1,2.... and so on. We should give proper names to the columns. I will do it as follows:-

```python
col_names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']


df.columns = col_names

col_names
```

**Output:**
```text
['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
```

```python
# let's again preview the dataset

df.head()
```

**Output:**
```text
buying  maint doors persons lug_boot safety  class
0  vhigh  vhigh     2       2    small    low  unacc
1  vhigh  vhigh     2       2    small    med  unacc
2  vhigh  vhigh     2       2    small   high  unacc
3  vhigh  vhigh     2       2      med    low  unacc
4  vhigh  vhigh     2       2      med    med  unacc
```

We can see that the column names are renamed. Now, the columns have meaningful names.

### View summary of dataset

```python
df.info()
```

### Frequency distribution of values in variables

Now, I will check the frequency counts of categorical variables.

```python
col_names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']


for col in col_names:
    
    print(df[col].value_counts())
```

**Output:**
```text
vhigh    432
med      432
high     432
low      432
Name: buying, dtype: int64
vhigh    432
med      432
high     432
low      432
Name: maint, dtype: int64
5more    432
4        432
3        432
2        432
Name: doors, dtype: int64
4       576
more    576
2       576
Name: persons, dtype: int64
small    576
big      576
med      576
Name: lug_boot, dtype: int64
med     576
high    576
low     576
Name: safety, dtype: int64
unacc    1210
acc       384
good       69
vgood      65
Name: class, dtype: int64
```

We can see that the `doors` and `persons` are categorical in nature. So, I will treat them as categorical variables.

### Summary of variables


- There are 7 variables in the dataset. All the variables are of categorical data type.


- These are given by `buying`, `maint`, `doors`, `persons`, `lug_boot`, `safety` and `class`.


- `class` is the target variable.

### Explore `class` variable

```python
df['class'].value_counts()
```

**Output:**
```text
unacc    1210
acc       384
good       69
vgood      65
Name: class, dtype: int64
```

The `class` target variable is ordinal in nature.

### Missing values in variables

```python
# check missing values in variables

df.isnull().sum()
```

**Output:**
```text
buying      0
maint       0
doors       0
persons     0
lug_boot    0
safety      0
class       0
dtype: int64
```

We can see that there are no missing values in the dataset.

# **10. Declare feature vector and target variable** <a class="anchor" id="10"></a>

[Table of Contents](#0.1)

```python
X = df.drop(['class'], axis=1)

y = df['class']
```

# **11. Split data into separate training and test set** <a class="anchor" id="11"></a>

[Table of Contents](#0.1)

```python
# split data into training and testing sets

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)
```

```python
# check the shape of X_train and X_test

X_train.shape, X_test.shape
```

**Output:**
```text
((1157, 6), (571, 6))
```

# **12. Feature Engineering** <a class="anchor" id="12"></a>

[Table of Contents](#0.1)


**Feature Engineering** is the process of transforming raw data into useful features that help us to understand our model better and increase its predictive power. I will carry out feature engineering on different types of variables.


First, I will check the data types of variables again.

```python
# check data types in X_train

X_train.dtypes
```

**Output:**
```text
buying      object
maint       object
doors       object
persons     object
lug_boot    object
safety      object
dtype: object
```

### Encode categorical variables


Now, I will encode the categorical variables.

```python
X_train.head()
```

**Output:**
```text
buying  maint  doors persons lug_boot safety
48    vhigh  vhigh      3    more      med    low
468    high  vhigh      3       4    small    low
155   vhigh   high      3    more    small   high
1721    low    low  5more    more    small   high
1208    med    low      2    more    small   high
```

We can see that all  the variables are ordinal categorical data type.

```python
# import category encoders

import category_encoders as ce
```

```python
# encode categorical variables with ordinal encoding

encoder = ce.OrdinalEncoder(cols=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety'])


X_train = encoder.fit_transform(X_train)

X_test = encoder.transform(X_test)
```

```python
X_train.head()
```

**Output:**
```text
buying  maint  doors  persons  lug_boot  safety
48         1      1      1        1         1       1
468        2      1      1        2         2       1
155        1      2      1        1         2       2
1721       3      3      2        1         2       2
1208       4      3      3        1         2       2
```

```python
X_test.head()
```

**Output:**
```text
buying  maint  doors  persons  lug_boot  safety
599        2      2      4        3         1       2
1201       4      3      3        2         1       3
628        2      2      2        3         3       3
1498       3      2      2        2         1       3
1263       4      3      4        1         1       1
```

We now have training and test set ready for model building.

# **13. Random Forest Classifier model with parameter n_estimators=10** <a class="anchor" id="13"></a>

[Table of Contents](#0.1)

```python
# import Random Forest classifier

from sklearn.ensemble import RandomForestClassifier



# instantiate the classifier 

rfc = RandomForestClassifier(random_state=0,n_estimators= 10)



# fit the model

rfc.fit(X_train, y_train)
```

**Output:**
```text
RandomForestClassifier(n_estimators=10, random_state=0)
```

```python
print(rfc.get_params())
```

**Output:**
```text
{'bootstrap': True, 'ccp_alpha': 0.0, 'class_weight': None, 'criterion': 'gini', 'max_depth': None, 'max_features': 'auto', 'max_leaf_nodes': None, 'max_samples': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 10, 'n_jobs': None, 'oob_score': False, 'random_state': 0, 'verbose': 0, 'warm_start': False}
```

```python
# Predict the Test set results

y_pred = rfc.predict(X_test)



# Check accuracy score 

from sklearn.metrics import accuracy_score

print('Model accuracy score with 10 decision-trees : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))
```

**Output:**
```text
Model accuracy score with 10 decision-trees : 0.9247
```

Here, **y_test** are the true class labels and **y_pred** are the predicted class labels in the test-set.

Here, I have build the Random Forest Classifier model with parameter of `n_estimators = 10`. So, I have used 10 decision-trees to build the model. Now, I will increase the number of decision-trees and see its effect on accuracy.

# **14. Random Forest Classifier model with parameter n_estimators=100** <a class="anchor" id="14"></a>

[Table of Contents](#0.1)

```python
# instantiate the classifier with n_estimators = 100

rfc_100 = RandomForestClassifier( random_state=0)



# fit the model to the training set

rfc_100.fit(X_train, y_train)



# Predict on the test set results

y_pred_100 = rfc_100.predict(X_test)



# Check accuracy score 

print('Model accuracy score with 100 decision-trees : {0:0.4f}'. format(accuracy_score(y_test, y_pred_100)))
```

**Output:**
```text
Model accuracy score with 100 decision-trees : 0.9457
```

The model accuracy score with 10 decision-trees is 0.9247 but the same with 100 decision-trees is 0.9457. So, as expected accuracy increases with number of decision-trees in the model.

# **15. Find important features with Random Forest model** <a class="anchor" id="15"></a>

[Table of Contents](#0.1)


Until now, I have used all the features given in the model. Now, I will select only the important features, build the model using these features and see its effect on accuracy. 


First, I will create the Random Forest model as follows:-

```python
# create the classifier with n_estimators = 100

clf = RandomForestClassifier(n_estimators=100, random_state=0)



# fit the model to the training set

clf.fit(X_train, y_train)
```

**Output:**
```text
RandomForestClassifier(random_state=0)
```

Now, I will use the feature importance variable to see feature importance scores.

```python
# view the feature scores

feature_scores = pd.Series(clf.feature_importances_, index=X_train.columns).sort_values(ascending=False)

feature_scores
```

**Output:**
```text
safety      0.295319
persons     0.233856
buying      0.151734
maint       0.146653
lug_boot    0.100048
doors       0.072389
dtype: float64
```

We can see that the most important feature is `safety` and least important feature is `doors`.

# **16. Visualize feature scores of the features** <a class="anchor" id="16"></a>

[Table of Contents](#0.1)


Now, I will visualize the feature scores with matplotlib and seaborn.

```python
# Creating a seaborn bar plot

sns.barplot(x=feature_scores, y=feature_scores.index)



# Add labels to the graph

plt.xlabel('Feature Importance Score')

plt.ylabel('Features')



# Add title to the graph

plt.title("Visualizing Important Features")



# Visualize the graph

plt.show()
```

# **17. Build Random Forest model on selected features** <a class="anchor" id="17"></a>

[Table of Contents](#0.1)


Now, I will drop the least important feature `doors` from the model, rebuild the model and check its effect on accuracy.

```python
# declare feature vector and target variable

X = df.drop(['class', 'doors'], axis=1)

y = df['class']
```

```python
# split data into training and testing sets

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)
```

Now, I will build the random forest model and check accuracy.

```python
# encode categorical variables with ordinal encoding

encoder = ce.OrdinalEncoder(cols=['buying', 'maint', 'persons', 'lug_boot', 'safety'])


X_train = encoder.fit_transform(X_train)

X_test = encoder.transform(X_test)
```

```python
# instantiate the classifier with n_estimators = 100

clf = RandomForestClassifier(random_state=0)



# fit the model to the training set

clf.fit(X_train, y_train)


# Predict on the test set results

y_pred = clf.predict(X_test)



# Check accuracy score 

print('Model accuracy score with doors variable removed : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))
```

**Output:**
```text
Model accuracy score with doors variable removed : 0.9264
```

`doors` variable was removed from the model, rebuild it and checked its accuracy. The accuracy of the model with `doors` variable removed is 0.9264. The accuracy of the model with all the variables taken into account is 0.9247. So, we can see that the model accuracy has been improved with `doors` variable removed from the model.

Furthermore, the second least important model is `lug_boot`. If we remove it from the model and rebuild the model, then the accuracy was found to be 0.8546. It is a significant drop in the accuracy. So,we will not drop it from the model.

Now, based on the above analysis we can conclude that our classification model accuracy is very good. Our model is doing a very good job in terms of predicting the class labels.


But, it does not give the underlying distribution of values. Also, it does not tell anything about the type of errors our classifer is making. 


We have another tool called `Confusion matrix` that comes to our rescue.

# **18. Confusion matrix** <a class="anchor" id="18"></a>

[Table of Contents](#0.1)



A confusion matrix is a tool for summarizing the performance of a classification algorithm. A confusion matrix will give us a clear picture of classification model performance and the types of errors produced by the model. It gives us a summary of correct and incorrect predictions broken down by each category. The summary is represented in a tabular form.


Four types of outcomes are possible while evaluating a classification model performance. These four outcomes are described below:-


**True Positives (TP)** – True Positives occur when we predict an observation belongs to a certain class and the observation actually belongs to that class.


**True Negatives (TN)** – True Negatives occur when we predict an observation does not belong to a certain class and the observation actually does not belong to that class.


**False Positives (FP)** – False Positives occur when we predict an observation belongs to a    certain class but the observation actually does not belong to that class. This type of error is called **Type I error.**



**False Negatives (FN)** – False Negatives occur when we predict an observation does not belong to a certain class but the observation actually belongs to that class. This is a very serious error and it is called **Type II error.**



These four outcomes are summarized in a confusion matrix given below.

```python
# Print the Confusion Matrix and slice it into four pieces

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print('Confusion matrix\n\n', cm)
```

**Output:**
```text
Confusion matrix

 [[104  12  10   3]
 [  0  18   0   2]
 [ 10   0 387   0]
 [  3   2   0  20]]
```

```python
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,7))
sns.heatmap(cm,annot=True,fmt='g')
plt.xlabel('Predicted')
plt.ylabel('Truth')
```

**Output:**
```text
Text(69.0, 0.5, 'Truth')
```

# **19. Classification Report** <a class="anchor" id="19"></a>

[Table of Contents](#0.1)


**Classification report** is another way to evaluate the classification model performance. It displays the  **precision**, **recall**, **f1** and **support** scores for the model. I have described these terms in later.

We can print a classification report as follows:-

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
```

**Output:**
```text
precision    recall  f1-score   support

         acc       0.89      0.81      0.85       129
        good       0.56      0.90      0.69        20
       unacc       0.97      0.97      0.97       397
       vgood       0.80      0.80      0.80        25

    accuracy                           0.93       571
   macro avg       0.81      0.87      0.83       571
weighted avg       0.93      0.93      0.93       571
```

# **20. Results and conclusion** <a class="anchor" id="20"></a>

[Table of Contents](#0.1)


1.	In this project, I build a Random Forest Classifier to predict the safety of the car. I build two models, one with 10 decision-trees and another one with 100 decision-trees. 
2.	The model accuracy score with 10 decision-trees is 0.9247 but the same with 100 decision-trees is 0.9457. So, as expected accuracy increases with number of decision-trees in the model.
3.	I have used the Random Forest model to find only the important features, build the model using these features and see its effect on accuracy. The most important feature is `safety` and least important feature is `doors`.
4.	I have removed the `doors` variable from the model, rebuild it and checked its accuracy. The accuracy of the model with `doors` variable removed is 0.9264. The accuracy of the model with all the variables taken into account is 0.9247. So, we can see that the model accuracy has been improved with `doors` variable removed from the model.
5.	The second least important model is `lug_boot`. If I remove it from the model and rebuild the model, then the accuracy was found to be 0.8546. It is a significant drop in the accuracy. So, I will not drop it from the model.
6.	Confusion matrix and classification report are another tool to visualize the model performance. They yield good performance.

# **21. References** <a class="anchor" id="21"></a>

[Table of Contents](#0.1)


The work done in this project is inspired from following books and websites:-

1. Hands on Machine Learning with Scikit-Learn and Tensorflow by Aurélién Géron

2. Introduction to Machine Learning with Python by Andreas C. Müller and Sarah Guido

3. https://en.wikipedia.org/wiki/Random_forest

4. https://www.datacamp.com/community/tutorials/random-forests-classifier-python

5. http://dataaspirant.com/2017/05/22/random-forest-algorithm-machine-learing/

6. https://stackabuse.com/random-forest-algorithm-with-python-and-scikit-learn/

7. https://youtu.be/J4Wdy0Wc_xQ & https://youtu.be/nyxTdL_4Q-Q

So, now we
come to the end of this kernel.

Thank you

# **22. Assignment** <a class="anchor" id="22"></a>

Use the dataset provided & do the following:

Dataset: https://www.kaggle.com/mlg-ulb/creditcardfraud

1. Measure prediction score using default n_estimators.
2. Fine tune the model using GridSearchCV(), and then build a model using the optimal value of n_estimators, max_features, max_depth etc.

[Table of Contents](#0.1)

[Go to Top](#0)