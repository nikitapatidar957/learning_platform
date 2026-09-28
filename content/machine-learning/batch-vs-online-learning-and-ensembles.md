## 🔹 Batch Learning vs Online Learning (Machine Learning)

Since you’re learning about pretrained models and ML basics, this is a **core foundational concept** you must understand clearly.

---

## 🟢 1. Batch Learning (Offline Learning)

![Image](https://www.researchgate.net/publication/316818527/figure/fig1/AS%3A551276161519616%401508445887645/Online-machine-learning-versus-batch-learning-a-Batch-machine-learning-workflow-b.png)

![Image](https://www.researchgate.net/publication/338885030/figure/fig3/AS%3A852581303713794%401580282631993/The-schematic-diagram-of-offline-model-training.ppm)

![Image](https://images.prismic.io/encord/Z1gokJbqstJ98QaX_Screenshot2024-12-10at11.37.02.png?auto=format%2Ccompress)

![Image](https://images.prismic.io/encord/Z1gpWJbqstJ98QbM_Screenshot2024-12-10at11.42.17.png?auto=format%2Ccompress)

### 📌 What it means:

The model is trained on the **entire dataset at once**.

* Data is collected.
* Model is trained.
* Model is deployed.
* If new data comes → retrain the whole model again.

### 🧠 Simple Example:

Suppose you're predicting house prices.
You collect **10,000 house records**, train once, and deploy.

If 2,000 new records come later → you retrain again from scratch.

---

### ✅ Characteristics:

* Training happens **periodically**
* Needs **more memory**
* Stable & less noisy
* Good for static datasets

---

### 📍 Real-world Examples:

* Spam detection (retrained weekly)
* Credit scoring models
* Traditional ML systems

---

### ❌ Disadvantages:

* Cannot adapt instantly
* Retraining can be expensive

---

---

## 🔵 2. Online Learning (Incremental Learning)

![Image](https://blogs.sas.com/content/subconsciousmusings/files/2017/10/DataInMotion.png)

![Image](https://blogs.mathworks.com/deep-learning/files/2024/03/incremental_learning_workflow-1.png)

![Image](https://s3.amazonaws.com/eckerson/assets/files/000/000/731/original/RackMultipart20211111-12599-147g9f.png?1636620576=)

![Image](https://hpe-developer-portal.s3.amazonaws.com/uploads/media/2020/9/image7-1603902952832.png)

### 📌 What it means:

Model learns **step-by-step from new data** as it arrives.

Instead of retraining from scratch, it updates itself continuously.

---

### 🧠 Simple Example:

Imagine a stock price prediction model.

Every new data point:

* Model updates weights
* Improves continuously

---

### ✅ Characteristics:

* Works with **streaming data**
* Requires less memory
* Adapts quickly
* Good for dynamic environments

---

### 📍 Real-world Examples:

* Recommendation systems (Amazon/Netflix)
* Fraud detection
* Real-time bidding ads
* Self-driving cars

---

### ❌ Disadvantages:

* Can be unstable
* Sensitive to noisy data
* Risk of “catastrophic forgetting”

---

# 🔥 Direct Comparison

| Feature             | Batch Learning   | Online Learning            |
| ------------------- | ---------------- | -------------------------- |
| Training style      | All data at once | One-by-one / small batches |
| Memory usage        | High             | Low                        |
| Speed of adaptation | Slow             | Fast                       |
| Best for            | Static data      | Streaming data             |
| Complexity          | Simpler          | More complex               |

---

# 🧩 Quick Interview Answer (If Asked)

> **Batch learning** trains the model on the entire dataset at once and retrains periodically.
> **Online learning** updates the model incrementally as new data arrives without retraining from scratch.

---

## 🔹 Instance-Based Learning vs Model-Based Learning

This is a **very important ML theory question** (often asked in interviews 👀). Since you're building strong ML foundations, let's make it crystal clear.

---

# 🟢 1️⃣ Instance-Based Learning (Memory-Based Learning)

![Image](https://kevinzakka.github.io/assets/knn/teaser.png)

![Image](https://miro.medium.com/1%2ArxBUhOROIAbmSQ7EkK7RSQ.png)

![Image](https://cdn.prod.website-files.com/5ef788f07804fb7d78a4127a/6229f7d4e27dd43a2133105a_Engati-Lazy-Learning-%20%281%29.jpg)

![Image](https://editor.analyticsvidhya.com/uploads/76050eagerf.jpg)

### 📌 What it means:

The model **memorizes training data** and makes predictions by comparing new data to stored examples.

It does NOT build an explicit mathematical model.

👉 It learns **by similarity**.

---

### 🧠 How it works:

1. Store all training data.
2. When new data comes:

   * Find similar examples
   * Predict based on nearest neighbors

---

### 🔍 Example:

The classic example is **K-Nearest Neighbors (KNN)**.

If you want to classify a fruit:

* Look at the 5 closest fruits in memory
* Majority vote decides the class

---

### ✅ Characteristics:

* Also called **Lazy Learning**
* No training time (almost zero)
* High prediction time
* Needs large memory
* Works well with small datasets

---

### ❌ Disadvantages:

* Slow during prediction
* Not scalable for very large datasets
* Sensitive to irrelevant features

---

---

# 🔵 2️⃣ Model-Based Learning

![Image](https://bookdown.org/a_shaker/STM1001_Topic_8/STM1001_Topic_8_files/figure-html/unnamed-chunk-14-1.svg)

![Image](https://images.openai.com/static-rsc-3/Bogabe2xi1-VtvCLRswyxN95Tuwdfp-xrME-ZirLjXHmLEAh8MQ7p1GJXUcoD98Wtl0-on7URjSayvCFOChEQ6InLd2qJfdBzDeniQX4Zs0?purpose=fullsize\&v=1)

![Image](https://www.researchgate.net/publication/340694475/figure/fig3/AS%3A938161513431040%401600686543311/Model-based-and-model-free-algorithm.ppm)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2AesVJb_A1pD8FL4Ol4N7nCw%402x.jpeg)

### 📌 What it means:

The model **learns a mathematical function** from data.

Instead of memorizing examples, it builds a generalized model.

👉 It learns a **pattern or formula**.

---

### 🧠 How it works:

1. Choose a model (linear, tree, neural network).
2. Train it to learn parameters.
3. Use learned function for prediction.

---

### 🔍 Examples:

* **Linear Regression**
* **Logistic Regression**
* Decision Trees
* Neural Networks

Example:
If predicting house prices:

* Model learns equation:
  [
  Price = w₁(Size) + w₂(Location) + b
  ]

---

### ✅ Characteristics:

* Training takes time
* Prediction is fast
* Good for large datasets
* Better generalization

---

### ❌ Disadvantages:

* Model assumptions may be wrong
* Requires training effort

---

# 🔥 Direct Comparison

| Feature         | Instance-Based | Model-Based       |
| --------------- | -------------- | ----------------- |
| Learning style  | Memorizes data | Learns function   |
| Training time   | Very low       | Higher            |
| Prediction time | High           | Low               |
| Memory usage    | High           | Low               |
| Example         | KNN            | Linear Regression |

---

# 🎯 Interview-Ready Answer

> Instance-based learning stores training examples and predicts based on similarity (e.g., KNN).
> Model-based learning builds a mathematical model from data and uses learned parameters for prediction (e.g., linear regression).

---
## 🚀 Applications of Machine Learning

Since you're building strong ML fundamentals (and working in data science), knowing **real-world applications** is very important for interviews and system design discussions.

---

# 1️⃣ Healthcare 🏥

![Image](https://images.openai.com/static-rsc-3/dxW8J5AwlBhHep9qE741D4nk_dIl1ppwkD64ea1WA9DCeW_a-OCqwhIL5lDvrDhj1yxnlt2Jf6dIJFhEvIav8tklZND6OA1UzrH5dpeYKL0?purpose=fullsize\&v=1)

![Image](https://blogs.imperial.ac.uk/imperial-medicine/files/2018/01/Medical_imaging_collage.jpg)

![Image](https://deephealth.com/app/uploads/2024/11/dx_OS-1200x534-1.jpg)

![Image](https://www.cancer.gov/sites/g/files/xnrzdm211/files/styles/cgov_article/public/cgov_image/media_image/2022-03/IDH1%20mutant%20glioblastoma.jpg?h=19b638d4\&itok=dt_WKbyD)

### 📌 Applications:

* Disease prediction
* Medical image analysis
* Drug discovery
* Personalized treatment

### 💡 Example:

Detecting tumors from X-ray or MRI scans.

---

# 2️⃣ Finance 💰

![Image](https://www.inetsoft.com/images/website/fraud-management-dashboard.png)

![Image](https://images.openai.com/static-rsc-3/nsi9akEQXjny7bEaM-gYcimzLVYIL2weD7FlwjMlHd2EA9lPZ7fZLfePyGj287g8vRikrrDpHSMCdxkDCm6ou3qQjBW0meqnARVD0uX9poM?purpose=fullsize\&v=1)

![Image](https://images.openai.com/static-rsc-3/XIYm2Lmx-WcpFx7QyC-v3sJp5sKKU2VmvA0RU1CATb6a83qTmlNJikGagz9ykgc2NVli4p4ZEsMxglS8_RSzBR0Sl1X-p4LREmpgwyhefes?purpose=fullsize\&v=1)

![Image](https://www.mdpi.com/engproc/engproc-56-00254/article_deploy/html/images/engproc-56-00254-g001.png)

### 📌 Applications:

* Fraud detection
* Credit scoring
* Algorithmic trading
* Risk analysis

### 💡 Example:

Banks use ML to detect fraudulent transactions in real-time.

---

# 3️⃣ E-commerce & Recommendation Systems 🛒

![Image](https://images.openai.com/static-rsc-3/upAn1MkD40xa1bvOTdq8h4WbcLjWrNhnwroPxjpI-9Wwb5Srzyw9bL2MgfVqbGMWNdKkX88FZVxUlUr2NRYRUepD_kGXcjM9pj4yobGW6l4?purpose=fullsize\&v=1)

![Image](https://cdn.prod.website-files.com/60bfd2b558c9eba77e06bf57/60f591cef9c2cb840d6d7d96_recommended-thomas.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1272/1%2AExSkgz1P8w0QPXG_rwG-Xw.png)

![Image](https://images.tristatetechnology.com/blog-images/uploads/2024/11/how-do-the-Netflix-recommendation-systems-work.jpg)

### 📌 Applications:

* Product recommendations
* Personalized ads
* Customer segmentation
* Demand forecasting

### 💡 Example:

Product recommendations on **Amazon**
Movie suggestions on **Netflix**

---

# 4️⃣ Self-Driving Cars 🚗

![Image](https://images.openai.com/static-rsc-3/V3WHVKt4So3lv-dx9suc1GE-jAAw1FBnUwViux1-8QHJZuyu-XwEFxVC1ksjw_umgIKHuvJsXO8fGOCwuAElPzMdjY3u8P6fyeAv85Xha1k?purpose=fullsize\&v=1)

![Image](https://cdn.prod.website-files.com/614c82ed388d53640613982e/63f4c6f0fd4b0a07b2f2cc43_cv%20in%20autonomous%20vehicles.jpg)

![Image](https://www.thinkautonomous.ai/blog/content/images/2023/10/embeddable_7ca2537d-48af-4fba-a00d-7f677da22bdf.png)

![Image](https://www.dripuploads.com/uploads/image_upload/image/3332574/embeddable_f995efef-98bd-4c8a-af68-bb4b9a43785d.png)

### 📌 Applications:

* Object detection
* Lane detection
* Traffic prediction
* Real-time decision making

---

# 5️⃣ Natural Language Processing (NLP) 💬

![Image](https://images.openai.com/static-rsc-3/PvDptBQ4pBlwTE8ImpvdEOs8DZcvjcbkG0iq7R4tyw3nvNMU4n3SN_ZK2RwjBcMBn9IB5kBfKiowboU1bab57K3nVXV0V0cAsdBy7E1_IKI?purpose=fullsize\&v=1)

![Image](https://www.slideteam.net/media/catalog/product/cache/1280x720/d/a/dashboard_to_track_sentiment_analysis_process_slide01.jpg)

![Image](https://www.transifex.com/hs-fs/hubfs/Imported_Blog_Media/AI_Translation_Ebook_pdf-4-2-2.png?height=1485\&name=AI_Translation_Ebook_pdf-4-2-2.png\&width=2640)

![Image](https://cdn.prod.website-files.com/67588292e9cff3b01f7e95a1/680d0f10d79e341aa54a0a37_67588c56cc463befd1899a64_64833e0eeb11341171ab8eb6_How%252520Do%252520AI%252520Technologies%252520Help%252520the%252520Translation%252520Process%25252C%252520Bridging%252520Language%252520Barriers.png)

### 📌 Applications:

* Chatbots
* Sentiment analysis
* Machine translation
* Speech recognition

---

# 6️⃣ Marketing & Business Analytics 📊

![Image](https://miro.medium.com/1%2ADRGr99HMhUQhFArlBTx5Qg.png)

![Image](https://preset.io/68bc7a2ce5201ec0ae090f83ff85da8e/image-005.png)

![Image](https://www.researchgate.net/publication/27826995/figure/fig15/AS%3A668233992503297%401536330807086/Graph-of-Actual-Sales-MA3Sales-Forecast-and-MA5-Sales-Forecast.png)

![Image](https://www.researchgate.net/publication/366577226/figure/fig4/AS%3A11431281109369063%401671934977733/Demand-Forecasting-Graph.ppm)

### 📌 Applications:

* Customer churn prediction
* Sales forecasting
* Lead scoring
* Campaign optimization

Since you work in analytics, churn prediction & behavioral targeting are especially relevant for you.

---

# 🎯 Interview-Ready Structured Answer

> Machine learning is applied in healthcare for disease detection, finance for fraud detection, e-commerce for recommendation systems, autonomous vehicles for real-time decision-making, NLP for chatbots and translation, and business analytics for forecasting and customer segmentation.

---
## 🔄 Machine Learning Development Cycle

Since you're working in data science and building systems, understanding the **end-to-end ML lifecycle** is very important — especially for interviews and production-level discussions.

---

# 🧭 Complete ML Development Cycle

![Image](https://i.postimg.cc/XNdgtgxd/machine-learning-life-cycle.png)

![Image](https://media.licdn.com/dms/image/v2/D4D12AQFTIdT5gkEzOQ/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1681481399600?e=2147483647\&t=00Ue3XX5Ak7gsfGbCoEUAf5txxH-7iT29QDkzKOoYAo\&v=beta)

![Image](https://www.researchgate.net/publication/261307514/figure/fig3/AS%3A667618470002700%401536184055743/CRISP-DM-process-model.png)

![Image](https://miro.medium.com/1%2AJYbymHifAk7aQ1pHm_IdMQ.png)

---

## 1️⃣ Problem Definition

### 📌 What happens here?

* Understand business objective
* Define target variable
* Decide success metric (Accuracy? F1? RMSE?)

👉 Example:
“Predict whether a user will churn in next 30 days.”

---

## 2️⃣ Data Collection

### 📌 Sources:

* Databases
* APIs
* Logs
* Surveys
* Third-party datasets

👉 Data must be relevant and representative.

---

## 3️⃣ Data Preprocessing

### 📌 Includes:

* Handling missing values
* Removing duplicates
* Encoding categorical variables
* Feature scaling
* Handling imbalance

⚠️ If preprocessing is wrong → model performance suffers badly.

---

## 4️⃣ Exploratory Data Analysis (EDA)

### 📌 Goals:

* Understand distributions
* Detect outliers
* Identify correlations
* Feature importance insights

Helps in selecting better features.

---

## 5️⃣ Feature Engineering

### 📌 Creating:

* New meaningful features
* Interaction terms
* Aggregated metrics
* Domain-based transformations

Good features = Better model performance.

---

## 6️⃣ Model Selection

Choose algorithm based on problem type:

* Regression → Linear Regression
* Classification → Logistic Regression, Random Forest
* Deep learning → Neural Networks

---

## 7️⃣ Model Training

* Split data (Train/Test or Train/Val/Test)
* Train model
* Tune hyperparameters

---

## 8️⃣ Model Evaluation

Use proper metrics:

* Classification → Accuracy, Precision, Recall, F1, ROC-AUC
* Regression → RMSE, MAE, R²

⚠️ Avoid data leakage.

---

## 9️⃣ Model Deployment

* Convert to API
* Integrate into application
* Ensure low latency

This is where many ML projects fail in real companies.

---

## 🔟 Monitoring & Maintenance

### 📌 Important:

* Monitor performance
* Detect data drift
* Retrain when needed
* Maintain version control

Production ML = Continuous cycle 🔁

---

# 🔥 Simple Interview Answer

> The machine learning development cycle includes problem definition, data collection, preprocessing, feature engineering, model training, evaluation, deployment, and continuous monitoring.

---

# 🧠 Pro-Level Insight (For Experienced Role)

Since you're working in analytics:

In real production systems:

* 70% time → Data cleaning & feature engineering
* 20% → Model training
* 10% → Deployment & monitoring

---

A **tensor** is a **mathematical object used to store numbers in multiple dimensions**. It is a **generalization of scalars, vectors, and matrices**.

In simple terms, a **tensor is just a container for numbers arranged in different dimensions**.

---

## 1️⃣ Scalar (0-D Tensor)

A **scalar** is a single number.

Example:

```
5
```

Dimension: **0D**

Example in Python:

```python
import torch
x = torch.tensor(5)
```

---

## 2️⃣ Vector (1-D Tensor)

A **vector** is a list of numbers.

Example:

```
[2, 4, 6, 8]
```

Dimension: **1D**

Shape:

```
(4)
```

Python example:

```python
x = torch.tensor([2,4,6,8])
```

---

## 3️⃣ Matrix (2-D Tensor)

A **matrix** is a table of numbers (rows and columns).

Example:

```
[ [1,2,3],
  [4,5,6] ]
```

Dimension: **2D**

Shape:

```
(2,3)
```

Python example:

```python
x = torch.tensor([[1,2,3],
                  [4,5,6]])
```

---

## 4️⃣ Higher-Dimensional Tensor (3D, 4D, …)

A tensor can have **more dimensions**.

Example of **3D tensor**:

```
[
  [[1,2],[3,4]],
  [[5,6],[7,8]]
]
```

Shape:

```
(2,2,2)
```

---

## 📊 Summary

| Type   | Dimension | Example         |
| ------ | --------- | --------------- |
| Scalar | 0D        | `5`             |
| Vector | 1D        | `[1,2,3]`       |
| Matrix | 2D        | `[[1,2],[3,4]]` |
| Tensor | 3D+       | `[[[...]]]`     |

---

## 🤖 Why Tensors Are Important in AI / Deep Learning

Frameworks like:

* PyTorch
* TensorFlow

use **tensors to represent data** such as:

* images
* text embeddings
* audio signals
* neural network weights

Example:
An **RGB image tensor**:

```
Height × Width × Channels
224 × 224 × 3
```

---

✅ **Simple definition:**

> A **tensor is a multi-dimensional array used to represent data in machine learning and mathematics.**

Short answer: **usually no**.
Arrays, matrices, and tensors are designed to store **elements of the same data type** (homogeneous data). But there are some exceptions depending on the programming language.

Let’s understand clearly.

---

# 1️⃣ Array

In most programming languages, an **array stores elements of the same data type**.

Example (valid):

```python
[1, 2, 3, 4]
```

Example (not typical in strict arrays):

```python
[1, "hello", 3.5]
```

🔹 In languages like **C / Java**

* Arrays **must contain the same type**.

Example:

```c
int arr[3] = {1,2,3};   // valid
```

❌ Invalid

```c
int arr[3] = {1,"hello",3}; 
```

🔹 In Python with NumPy arrays
All elements must be **same datatype**.

Example:

```python
import numpy as np
arr = np.array([1,2,3])
```

If you try:

```python
np.array([1,"hello",3])
```

It will convert everything to **string type**.

---

# 2️⃣ Matrix

A **matrix also stores the same data type**.

Example:

```text
[1 2 3
 4 5 6]
```

All elements must be:

* integers
* floats
* or same numeric type

Example in Python:

```python
import numpy as np
matrix = np.array([[1,2],
                   [3,4]])
```

❌ Not recommended:

```python
[[1,"hello"],
 [3,4]]
```

Because matrices are used for **mathematical operations**, which require numeric data.

---

# 3️⃣ Tensor

A **tensor also stores elements of the same datatype**.

In deep learning frameworks like:

* PyTorch
* TensorFlow

Tensor elements must be consistent types such as:

* float32
* int32
* float64

Example:

```python
import torch
tensor = torch.tensor([1,2,3])
```

❌ Invalid:

```python
torch.tensor([1,"hello",3])
```

This will throw an **error**.

---

# 📊 Summary

| Structure | Different Data Types Allowed? | Reason                                 |
| --------- | ----------------------------- | -------------------------------------- |
| Array     | ❌ Usually no                  | Fixed datatype                         |
| Matrix    | ❌ No                          | Mathematical operations                |
| Tensor    | ❌ No                          | GPU computation requires same datatype |

---

✅ **Important Interview Point**

Arrays, matrices, and tensors are **homogeneous data structures**, meaning:

> **All elements must have the same datatype.**

---

💡 **Extra concept (very useful for interviews)**

Python **lists** can store different types:

```python
[1, "hello", 3.5, True]
```

But **arrays, matrices, and tensors cannot**.

---
Great 👍 Let’s clearly understand the **difference between List, Array, Matrix, and Tensor** because this is a **very common ML / Python interview question**.

---

# 1️⃣ List

A **list** is a Python data structure that can store **different types of data**.

Example:

```python
my_list = [10, "hello", 3.5, True]
```

✔ Features

* Can store **different data types**
* **Dynamic size**
* Slower for numerical computation

Example:

```python
a = [1,2,3,4]
```

---

# 2️⃣ Array

An **array** stores **elements of the same data type**.

Usually implemented using
NumPy

Example:

```python
import numpy as np
arr = np.array([1,2,3,4])
```

✔ Features

* **Homogeneous data** (same type)
* Faster numerical computation
* Supports **vector operations**

Example operation:

```python
arr + 2
```

Output

```
[3 4 5 6]
```

---

# 3️⃣ Matrix

A **matrix** is a **2D array used in linear algebra**.

Example:

```python
import numpy as np

matrix = np.array([
    [1,2,3],
    [4,5,6]
])
```

Shape:

```
2 × 3
```

✔ Features

* Always **2-dimensional**
* Used in **linear algebra operations**
* Used in **machine learning calculations**

Example:

```
Matrix Multiplication
A × B
```

---

# 4️⃣ Tensor

A **tensor is a multi-dimensional array** used in **deep learning**.

It can be:

| Dimension | Name   |
| --------- | ------ |
| 0D        | Scalar |
| 1D        | Vector |
| 2D        | Matrix |
| 3D+       | Tensor |

Example using
PyTorch

```python
import torch

tensor = torch.tensor([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])
```

Shape:

```
2 × 2 × 2
```

✔ Features

* Supports **multiple dimensions**
* Used in **deep learning models**
* GPU optimized

Frameworks using tensors:

* TensorFlow
* PyTorch

---

# 📊 Final Comparison

| Feature   | List                    | Array               | Matrix         | Tensor          |
| --------- | ----------------------- | ------------------- | -------------- | --------------- |
| Data type | Different types allowed | Same type           | Same type      | Same type       |
| Dimension | Any                     | 1D / multi          | Only 2D        | Any dimension   |
| Speed     | Slow                    | Fast                | Fast           | Very fast (GPU) |
| Used in   | General Python          | Numerical computing | Linear algebra | Deep learning   |

---

✅ **Simple memory trick**

```
List → general storage
Array → numerical storage
Matrix → 2D mathematical array
Tensor → multi-dimensional data for AI
```

---
To understand **when to use List, Array, Matrix, or Tensor**, you should know **what operations we perform on each** and **in which situations they are used**.

---

# 1️⃣ List (Python List)

### Operations

Common operations on lists:

```python
a = [1,2,3]

a.append(4)     # add element
a.remove(2)     # remove element
a[0]            # access element
a[1:3]          # slicing
```

### When to Use

Use **lists** when:

* Data types are **different**
* You need **dynamic size**
* Data is **not mainly for mathematical computation**

Example:

```python
student = ["Nikita", 25, "Data Scientist"]
```

✔ Best for

* storing mixed data
* general programming

---

# 2️⃣ Array

Usually used with
NumPy.

### Operations

```python
import numpy as np

a = np.array([1,2,3])

a + 2
a * 5
np.mean(a)
np.sum(a)
np.max(a)
```

✔ Operations include:

* element-wise addition
* element-wise multiplication
* mean
* sum
* statistical calculations

Example:

```
[1,2,3] + 2
= [3,4,5]
```

### When to Use

Use **arrays** when:

* Data is **numerical**
* Need **fast computation**
* Working with **large datasets**

✔ Common in:

* data analysis
* statistics
* preprocessing

---

# 3️⃣ Matrix

A **matrix is a 2D structure used in linear algebra**.

### Operations

Matrix operations include:

**Matrix multiplication**

```
A × B
```

**Transpose**

```
Aᵀ
```

**Determinant**

```
|A|
```

Example:

```python
import numpy as np

A = np.array([[1,2],
              [3,4]])

B = np.array([[5,6],
              [7,8]])

np.dot(A,B)
```

### When to Use

Use **matrix** when:

* working with **linear algebra**
* solving **equations**
* **machine learning algorithms**

Example uses:

* regression
* neural network weights
* PCA

---

# 4️⃣ Tensor

Tensors are used in **deep learning frameworks** like:

* TensorFlow
* PyTorch

### Operations

Typical tensor operations:

```python
import torch

t = torch.tensor([[1,2],[3,4]])

t + 2
t * 3
torch.matmul(t,t)
t.mean()
```

✔ Tensor operations include:

* broadcasting
* GPU computation
* automatic differentiation
* tensor multiplication

### When to Use

Use **tensors** when working with:

* **deep learning**
* **image processing**
* **NLP**
* **large multidimensional data**

Example:

Image tensor shape

```
Batch × Height × Width × Channels
32 × 224 × 224 × 3
```

---

# 📊 Final Comparison

| Data Structure | Main Operations                       | When to Use         |
| -------------- | ------------------------------------- | ------------------- |
| List           | append, remove, slicing               | General programming |
| Array          | element-wise math, statistics         | Data analysis       |
| Matrix         | matrix multiplication, transpose      | Linear algebra / ML |
| Tensor         | multidimensional math, GPU operations | Deep learning       |

---

✅ **Simple way to remember**

```
List → general data
Array → numerical data
Matrix → linear algebra
Tensor → deep learning
```

---

💡 Since you are learning **ML and neural networks**, the **most important structures are:**

* **NumPy Arrays**
* **Tensors**

because almost all ML models internally operate on **arrays and tensors**.
Great 👍 Let’s see **how tensors are used inside neural networks step-by-step**. I’ll keep it simple and practical.

---

# 1️⃣ Input Data → Tensor

In deep learning, the **input data is first converted into a tensor**.

Example: Image input

```
Height × Width × Channels
224 × 224 × 3
```

If we process multiple images together (batch):

```
Batch × Height × Width × Channels
32 × 224 × 224 × 3
```

Deep learning frameworks like

* PyTorch
* TensorFlow

store this data as **tensors**.

Example:

```python
import torch
image_tensor = torch.randn(32,224,224,3)
```

---

# 2️⃣ Weights and Bias → Tensor

Neural networks learn using **weights and biases**, and these are also stored as tensors.

Example:

```
Input layer → Hidden layer
```

Weight matrix:

```
W = (input_features × neurons)
```

Example:

```
W = (784 × 128)
```

Bias:

```
b = (1 × 128)
```

Both are tensors.

Example:

```python
W = torch.randn(784,128)
b = torch.randn(128)
```

---

# 3️⃣ Forward Pass (Tensor Operations)

Neural networks compute output using **tensor operations**.

Formula:

```
Z = XW + b
```

Where

* **X** = input tensor
* **W** = weight tensor
* **b** = bias tensor

Example:

```python
Z = torch.matmul(X, W) + b
```

This operation is **vectorized tensor computation**, which makes deep learning fast.

---

# 4️⃣ Activation Function

After computing ( Z ), we apply an **activation function**.

Example:

```
A = ReLU(Z)
```

Example code:

```python
A = torch.relu(Z)
```

Now the tensor **flows to the next layer**.

---

# 5️⃣ Loss Calculation

The network compares prediction with the real answer.

Example loss:

```
Loss = (Prediction - True Value)²
```

Example:

```python
loss = torch.mean((prediction - target)**2)
```

Loss is also a **tensor value**.

---

# 6️⃣ Backpropagation

Now the model calculates **gradients of tensors**.

```
∂Loss / ∂W
```

Frameworks automatically compute gradients.

Example:

```python
loss.backward()
```

Now every tensor stores **gradient information**.

---

# 7️⃣ Weight Update

Optimizer updates weights.

Example:

```
W = W - learning_rate × gradient
```

Example:

```python
optimizer.step()
```

---

# 📊 Tensor Flow Inside Neural Network

```
Input Tensor
      ↓
Weight Tensor
      ↓
Matrix Multiplication
      ↓
Activation Function
      ↓
Output Tensor
      ↓
Loss Tensor
      ↓
Gradient Tensor
      ↓
Weight Update
```

---

# 📌 Real Example (MNIST Digits)

Input image:

```
28 × 28
```

Flattened tensor:

```
784
```

Network:

```
Input: 784
Hidden: 128
Output: 10
```

Tensor shapes:

```
X → (batch_size × 784)
W1 → (784 × 128)
W2 → (128 × 10)
```

---

✅ **Key Idea**

> Deep learning is basically **a series of tensor operations** (multiplication, addition, activation, gradients).

Understanding **how to decide tensor dimensions in deep learning** is very important. The key idea is:

> **Tensor dimensions depend on the type of data and the model architecture.**

There are a few **standard patterns** used in deep learning.

---

# 1️⃣ Basic Rule: Batch Dimension First

Almost every deep learning model uses **batch processing**.

Tensor format usually starts with:

```
Batch Size × Features
```

Example:

```
32 × 10
```

Meaning:

* 32 samples processed together
* 10 features per sample

Frameworks like PyTorch and TensorFlow follow this rule.

---

# 2️⃣ Tabular Data Tensor Shape

Used in **regression, classification, ML models**.

Example dataset:

| Age | Salary | Experience |
| --- | ------ | ---------- |
| 25  | 40000  | 2          |
| 30  | 60000  | 5          |

Tensor shape:

```
Batch × Features
```

Example:

```
32 × 3
```

Meaning:

* 32 rows
* 3 features

---

# 3️⃣ Image Data Tensor Shape (CNN)

Images have **height, width, and channels**.

Tensor format:

```
Batch × Channels × Height × Width
```

Example:

```
32 × 3 × 224 × 224
```

Meaning:

* 32 images
* 3 color channels (RGB)
* 224 × 224 pixels

Example code:

```python
import torch
image = torch.randn(32,3,224,224)
```

---

# 4️⃣ Text Data Tensor Shape (NLP)

Text models use **sequence length and embeddings**.

Tensor format:

```
Batch × Sequence Length × Embedding Dimension
```

Example:

```
32 × 50 × 300
```

Meaning:

* 32 sentences
* 50 words per sentence
* 300 embedding values per word

---

# 5️⃣ RNN / LSTM Tensor Shape

Sequence models use **time steps**.

Typical format:

```
Batch × Sequence Length × Features
```

Example:

```
32 × 100 × 64
```

Meaning:

* 32 sequences
* 100 time steps
* 64 features

Used in:

* speech recognition
* time series
* language modeling

---

# 6️⃣ Transformer Tensor Shape

Transformers also use:

```
Batch × Sequence Length × Embedding Dimension
```

Example:

```
32 × 128 × 768
```

Meaning:

* 32 inputs
* 128 tokens
* 768 embedding size

Models like BERT use this structure.

---

# 📊 Summary Table

| Data Type    | Tensor Shape                      |
| ------------ | --------------------------------- |
| Tabular data | Batch × Features                  |
| Images (CNN) | Batch × Channels × Height × Width |
| Text (NLP)   | Batch × Sequence × Embedding      |
| Time series  | Batch × Time Steps × Features     |
| Transformers | Batch × Sequence × Embedding      |

---

# 🧠 Simple Rule to Remember

```
First dimension → Batch
Next dimensions → Structure of the data
```

Examples:

```
Tabular → (batch, features)
Images → (batch, channels, height, width)
Text → (batch, sequence, embedding)
```

---

# 🎯 Practical Example

Suppose you train a **cat vs dog classifier**.

Image size:

```
128 × 128 RGB
```

Batch size:

```
16
```

Tensor shape:

```
16 × 3 × 128 × 128
```

---

✅ **Key idea**

> Tensor dimensions represent the **structure of the data flowing through the neural network**.

---
Here are the **pros and cons of the main data structures used in Python and deep learning**: **List, Array, Matrix, and Tensor**.

---

# 1️⃣ List (Python List)

### ✅ Pros

* Can store **different data types**
* **Dynamic size** (can grow or shrink easily)
* Very easy to use in **general programming**
* Built-in Python operations (append, remove, slicing)

Example:

```python
data = [10, "hello", 3.5, True]
```

### ❌ Cons

* **Slow for numerical computations**
* Not optimized for **large mathematical operations**
* No **vectorized operations**
* Not memory efficient for large datasets

### 📌 When to Use

Use **lists** when:

* data types are **different**
* working on **general programming logic**

---

# 2️⃣ Array (NumPy Array)

Typically used with
NumPy

### ✅ Pros

* **Fast numerical operations**
* **Vectorized computation**
* Memory efficient
* Supports **statistical and mathematical operations**

Example:

```python
import numpy as np
arr = np.array([1,2,3,4])
```

### ❌ Cons

* Stores **only one data type**
* Slightly harder for beginners
* Limited support for **very high dimensional deep learning operations**

### 📌 When to Use

Use **arrays** when:

* working with **data analysis**
* doing **numerical computations**
* preprocessing data for ML models

---

# 3️⃣ Matrix

Matrix is basically a **2D numerical structure** used in **linear algebra**.

### ✅ Pros

* Good for **linear algebra operations**
* Supports operations like:

  * matrix multiplication
  * transpose
  * determinant
* Fundamental for **machine learning algorithms**

Example:

```python
matrix = [[1,2],
          [3,4]]
```

### ❌ Cons

* Limited to **2 dimensions only**
* Not suitable for **complex deep learning data**
* Less flexible compared to tensors

### 📌 When to Use

Use **matrix** when:

* solving **linear algebra problems**
* implementing **ML algorithms**
* performing **matrix multiplication**

---

# 4️⃣ Tensor

Used in deep learning frameworks like

* PyTorch
* TensorFlow

### ✅ Pros

* Supports **multi-dimensional data**
* Optimized for **GPU computation**
* Enables **automatic differentiation**
* Core structure for **deep learning models**

Example:

```python
import torch
tensor = torch.tensor([[1,2],[3,4]])
```

### ❌ Cons

* More complex to understand for beginners
* Requires deep learning frameworks
* Higher memory usage for large models

### 📌 When to Use

Use **tensors** when:

* building **deep learning models**
* processing **images, text, audio**
* training **neural networks**

---

# 📊 Quick Comparison

| Data Structure | Pros                           | Cons                 | Best Use            |
| -------------- | ------------------------------ | -------------------- | ------------------- |
| List           | flexible, mixed data           | slow math operations | general programming |
| Array          | fast numerical operations      | same data type only  | data analysis       |
| Matrix         | good for linear algebra        | only 2D              | ML math operations  |
| Tensor         | multi-dimensional, GPU support | complex              | deep learning       |

---

✅ **Simple memory trick**

```
List → flexibility
Array → fast computation
Matrix → linear algebra
Tensor → deep learning
```

---

💡 Since you are learning **machine learning and neural networks**, the most important structures to master are:

* **NumPy Arrays**
* **Tensors (PyTorch / TensorFlow)**

because almost every ML or DL model internally uses them.
To answer this **from an interview point of view**, you should explain **what they are, how they work, their dimensions, examples, operations, and use in machine learning**.

---

# 1️⃣ Scalar

## What is a Scalar?

A **scalar** is a **single number** with **no direction and no dimensions**.

It represents **one value only**.

Example:

```
5
-10
3.14
```

Dimension:

```
0D (zero dimension)
```

---

## How Scalar Works

A scalar represents **magnitude only**.

Example:

* Temperature = **25°C**
* Weight = **60 kg**
* Age = **24**

These values have **size but no direction**.

---

## Operations on Scalars

Basic arithmetic operations:

```
Addition
Subtraction
Multiplication
Division
```

Example:

```
5 + 3 = 8
4 × 2 = 8
```

---

## Scalar in Machine Learning

In ML, scalar values represent:

* **loss value**
* **learning rate**
* **bias**
* **single feature value**

Example:

```python
learning_rate = 0.01
loss = 0.45
```

---

# 2️⃣ Vector

## What is a Vector?

A **vector** is an **ordered list of numbers**.

Example:

```
[2, 4, 6]
```

Dimension:

```
1D (one dimension)
```

It contains **multiple scalars arranged in order**.

---

## How Vector Works

Vectors represent **magnitude and direction**.

Example in physics:

```
velocity = [5, 3]
```

Meaning:

```
x direction = 5
y direction = 3
```

---

## Vector Representation

```
v = [v1, v2, v3]
```

Example:

```
v = [2,4,6]
```

---

## Vector Operations

### 1️⃣ Vector Addition

```
[1,2,3] + [4,5,6] = [5,7,9]
```

### 2️⃣ Scalar Multiplication

```
2 × [1,2,3] = [2,4,6]
```

### 3️⃣ Dot Product

```
[1,2,3] · [4,5,6]
= 1×4 + 2×5 + 3×6
= 32
```

---

## Vector in Machine Learning

Vectors represent:

* **feature vectors**
* **word embeddings**
* **model parameters**

Example:

```
House features vector:

[Area, Bedrooms, Age]
[1200, 3, 5]
```

---

# 3️⃣ Tensor

## What is a Tensor?

A **tensor is a multi-dimensional array of numbers**.

It is a **generalization of scalar, vector, and matrix**.

| Structure | Dimension  |
| --------- | ---------- |
| Scalar    | 0D         |
| Vector    | 1D         |
| Matrix    | 2D         |
| Tensor    | 3D or more |

---

## Tensor Example

### 0D Tensor (Scalar)

```
5
```

### 1D Tensor (Vector)

```
[1,2,3]
```

### 2D Tensor (Matrix)

```
[[1,2],
 [3,4]]
```

### 3D Tensor

```
[
 [[1,2],[3,4]],
 [[5,6],[7,8]]
]
```

---

## How Tensor Works

Tensors store **multi-dimensional data**.

Example: Image

```
Height × Width × Channels
224 × 224 × 3
```

Batch of images:

```
Batch × Channels × Height × Width
32 × 3 × 224 × 224
```

Frameworks like

* PyTorch
* TensorFlow

use tensors to perform **fast GPU computations**.

---

## Tensor Operations

### 1️⃣ Element-wise operations

```
Tensor + Tensor
Tensor × Tensor
```

Example:

```
[1,2] + [3,4] = [4,6]
```

---

### 2️⃣ Matrix multiplication

```
A × B
```

Used in neural networks.

---

### 3️⃣ Broadcasting

Allows operations between different shapes.

Example:

```
[1,2,3] + 2 = [3,4,5]
```

---

### 4️⃣ Reduction operations

```
mean()
sum()
max()
```

---

## Tensor in Deep Learning

Deep learning is basically **tensor computation**.

Example in neural network:

```
Z = XW + b
```

Where

```
X → input tensor
W → weight tensor
b → bias tensor
```

---

# 📊 Comparison

| Property   | Scalar              | Vector          | Tensor                  |
| ---------- | ------------------- | --------------- | ----------------------- |
| Definition | single number       | list of numbers | multi-dimensional array |
| Dimension  | 0D                  | 1D              | 2D, 3D, ...             |
| Example    | 5                   | [1,2,3]         | [[[...]]]               |
| ML Use     | loss, learning rate | feature vectors | images, sequences       |

---

# 🧠 Simple Way to Remember

```
Scalar → one number
Vector → list of numbers
Matrix → table of numbers
Tensor → multi-dimensional data
```

---

# 🎯 Interview Answer (Short Version)

If an interviewer asks:

**Difference between scalar, vector, and tensor**

You can say:

> A scalar is a single numeric value with zero dimensions. A vector is a one-dimensional array of numbers. A tensor is a generalization of scalars and vectors to multiple dimensions and is used to represent complex data structures in deep learning such as images, text, and batches of data.

Your question mixes a few concepts, so let’s clarify it carefully from a **machine learning / linear algebra interview perspective**.

You said:

* **100 students (samples)**
* **3 features per student**

Example dataset:

| Student | Feature1 | Feature2 | Feature3 |
| ------- | -------- | -------- | -------- |
| S1      | 10       | 5        | 2        |
| S2      | 8        | 6        | 3        |
| ...     | ...      | ...      | ...      |
| S100    | 7        | 4        | 1        |

---

# 1️⃣ What is the Correct Representation?

This dataset is represented as a **matrix or tensor** with shape:

```
(100, 3)
```

Meaning:

* **100 rows → students (samples)**
* **3 columns → features**

So the **tensor dimension is 2D**, not 100D.

---

# 2️⃣ Axis Explanation

For this tensor:

```
Shape = (100, 3)
```

Axes are:

```
Axis 0 → samples (students)
Axis 1 → features
```

Visualization:

```
Axis 0 ↓

[10 5 2]
[8  6 3]
[9  7 1]
...
```

Axis 1 →

```
Feature1 Feature2 Feature3
```

So there are **2 axes**, not 3.

---

# 3️⃣ Are There 100-Dimensional Vectors?

No.

Each **student is represented as a vector with 3 dimensions**, because there are **3 features**.

Example student vector:

```
[10, 5, 2]
```

Dimension of this vector:

```
3D vector
```

So we have:

```
100 vectors
each vector = 3 dimensions
```

---

# 4️⃣ Correct Mathematical Interpretation

Dataset structure:

```
100 × 3 matrix
```

Meaning:

* **100 vectors**
* Each vector lives in **3-dimensional feature space**

So the **space dimension = 3**, not 100.

---

# 5️⃣ Is Each Dimension a Tensor?

Not exactly.

More precisely:

* Each **feature value** → scalar (0D tensor)
* Each **student row** → vector (1D tensor)
* Entire dataset → matrix (2D tensor)

Hierarchy:

```
Scalar → single feature value
Vector → student features
Matrix → dataset
Tensor → general term for multi-dimensional data
```

---

# 6️⃣ Final Structure

```
Dataset Tensor
Shape = (100, 3)
```

Breakdown:

```
100 students → axis 0
3 features  → axis 1
```

Each row:

```
[Feature1, Feature2, Feature3]
```

Example:

```
[1200, 3, 5]
```

---

# 📊 Summary

| Concept          | Value     |
| ---------------- | --------- |
| Samples          | 100       |
| Features         | 3         |
| Tensor Shape     | (100, 3)  |
| Axes             | 2         |
| Vector dimension | 3         |
| Tensor type      | 2D tensor |

---

# 🎯 Interview Answer

You can say:

> If we have 100 students with 3 features each, the dataset can be represented as a 2-dimensional tensor with shape (100, 3). Each row represents a student and each column represents a feature. Therefore we have 100 vectors in a 3-dimensional feature space.

---

✅ If you want, I can also explain a **very common confusion in ML interviews**:

**Difference between feature space dimension vs tensor dimension vs vector dimension** (this is where many people get confused).
The **ternary operator** is a **short way to write an `if-else` condition in a single line**. It is called **ternary** because it uses **three parts (three operands)**.

### Basic Syntax

```python
value_if_true if condition else value_if_false
```

### Structure

```
condition ? true_value : false_value   (in languages like C, Java, JS)

Python style:
true_value if condition else false_value
```

### Example (Normal If-Else)

```python
age = 18

if age >= 18:
    status = "Adult"
else:
    status = "Minor"
```

### Same Example Using Ternary Operator

```python
age = 18
status = "Adult" if age >= 18 else "Minor"
```

So here:

| Part        | Meaning                     |
| ----------- | --------------------------- |
| `age >= 18` | condition                   |
| `"Adult"`   | value if condition is true  |
| `"Minor"`   | value if condition is false |

---

# Example 2

```python
a = 10
b = 20

max_value = a if a > b else b
print(max_value)
```

Output:

```
20
```

Meaning:

* If `a > b` → return `a`
* Otherwise → return `b`

---

# Example 3 (Even or Odd)

```python
num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(result)
```

Output:

```
Odd
```

---

# Why Use Ternary Operator?

### Advantages

✅ Shorter code
✅ Cleaner for simple conditions
✅ Easy to read for small logic

Example:

Normal:

```python
if score >= 50:
    result = "Pass"
else:
    result = "Fail"
```

Ternary:

```python
result = "Pass" if score >= 50 else "Fail"
```

---

# Nested Ternary Operator (Advanced)

```python
num = 0

result = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(result)
```

Output:

```
Zero
```

---

# Interview Definition

**Ternary Operator:**
A **conditional operator** that evaluates a condition and returns one value if the condition is true and another value if the condition is false, written in a single line.

---

# Simple Way to Remember

```
value_if_true if condition else value_if_false
```

Example:

```
"Pass" if marks >= 40 else "Fail"
```

--- 
I'll explain each concept clearly from a **Python / NumPy interview perspective**.

---

# 1. `np.ceil()`

### Definition

`np.ceil()` returns the **smallest integer greater than or equal to a number**.

It **rounds UP** to the nearest integer.

### Syntax

```python
np.ceil(x)
```

### Example

```python
import numpy as np

np.ceil(4.2)
```

Output

```
5.0
```

### More Examples

| Input           | Output |
| --------------- | ------ |
| `np.ceil(2.1)`  | `3.0`  |
| `np.ceil(5.9)`  | `6.0`  |
| `np.ceil(-2.3)` | `-2.0` |

Note: Output is **float**, not integer.

Example with array:

```python
arr = np.array([1.2, 3.7, 4.1])
np.ceil(arr)
```

Output

```
[2. 4. 5.]
```

### Use Case

* rounding up prices
* pagination calculations
* allocating resources

Example:

```python
pages = np.ceil(total_items / items_per_page)
```

---

# 2. Floating Point Error

### Definition

A **floating point error** occurs because **computers cannot represent some decimal numbers exactly in binary**.

Example:

```python
0.1 + 0.2
```

Output:

```
0.30000000000000004
```

Why?

Because internally:

```
0.1 ≈ 0.0001100110011... (binary infinite)
0.2 ≈ 0.001100110011... (binary infinite)
```

So Python approximates them.

### NumPy Example

```python
import numpy as np

np.array([0.1]) + np.array([0.2])
```

Output

```
array([0.3])
```

But internally small precision error may exist.

### Types of Floating Errors

| Type           | Meaning             |
| -------------- | ------------------- |
| Overflow       | number too large    |
| Underflow      | number too small    |
| Divide by zero | division by zero    |
| Invalid        | undefined operation |

Example:

```python
1/0
```

---

# 3. `timedelta64`

### Definition

`timedelta64` represents **time duration** in NumPy.

It stores **difference between two dates/times**.

### Example

```python
import numpy as np

np.timedelta64(5, 'D')
```

Output

```
numpy.timedelta64(5,'D')
```

Meaning:

```
5 Days
```

### Units Supported

| Unit | Meaning     |
| ---- | ----------- |
| Y    | Year        |
| M    | Month       |
| W    | Week        |
| D    | Day         |
| h    | Hour        |
| m    | Minute      |
| s    | Second      |
| ms   | Millisecond |
| us   | Microsecond |
| ns   | Nanosecond  |

### Example

```python
np.timedelta64(10, 'h')
```

Output

```
10 hours
```

### Date Difference Example

```python
d1 = np.datetime64('2026-03-01')
d2 = np.datetime64('2026-03-06')

d2 - d1
```

Output

```
5 days
```

---

# 4. `np.seterr()`

### Definition

`np.seterr()` controls **how NumPy handles floating point errors**.

Instead of crashing, you can control behavior.

### Syntax

```python
np.seterr(divide='warn')
```

### Parameters

| Option | Meaning         |
| ------ | --------------- |
| ignore | ignore error    |
| warn   | show warning    |
| raise  | raise exception |
| print  | print warning   |
| log    | log error       |

### Example

```python
import numpy as np

np.seterr(divide='warn')

np.array([1]) / 0
```

Output:

```
RuntimeWarning: divide by zero encountered
```

### Raise Exception Example

```python
np.seterr(divide='raise')

np.array([1]) / 0
```

Output:

```
FloatingPointError
```

---

# Summary Table

| Concept              | Meaning                                   |
| -------------------- | ----------------------------------------- |
| `np.ceil()`          | round number upward                       |
| Floating Point Error | precision issue in decimal representation |
| `timedelta64`        | represents time duration                  |
| `np.seterr()`        | controls floating-point error behavior    |

---

# Simple Interview Answer

* **np.ceil()** → returns smallest integer ≥ number
* **Floating point error** → precision issue in decimal numbers due to binary representation
* **timedelta64** → NumPy data type for time difference
* **np.seterr()** → function to control floating point error handling

---

If you want, I can also explain **10 very important NumPy interview functions** like:

* `np.floor()`
* `np.round()`
* `np.clip()`
* `np.where()`
* `np.arange()`
* `np.linspace()`

These are **very commonly asked in Data Scientist interviews**.
