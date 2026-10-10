# Machine Learning Foundations: Theory, Linear & Logistic Regression

End-to-end guide covering Machine Learning paradigms (Supervised, Unsupervised, Reinforcement Learning), the Bias-Variance tradeoff, cost functions, gradient descent optimization, Ordinary Least Squares (OLS) Linear Regression, and Logistic Regression binary classification with Sigmoid activations, Log-Loss, ROC-AUC, and Confusion Matrices.

---

## 🧠 Machine Learning Basics Theory

## Machine Learning Fundamentals

We are living in the age of the intelligent machines. In the last decade, machine learning powered systems went from beating the world class chess players to now influencing most of our daily decisions like what we watch on streaming services like Netlix and Youtube. What is machine learning? And why is it important to be studying it now?

We hear that machine learning is transforming many industries, but what exactly can we use it for? And what are the set of problems that this technology is or not suited for? 

This introduction will give you the basics of machine learning or these things that you will always need to know. More concretely, it will cover the high level foundational knouledge such as:

- What is machine learning?
- The difference between artificial intelligence, data science, machine learning and deep learning
- The difference between machine learning and ordinary programming
- Applications of machine learning
- When to use and when not to use machine learning
- Types of machine learning
- A typical machine learning project workflow
- Evaluation metrics
- The challenges of training machine learning systems

### What is Machine Learning?

Machine learning is a new programming paradigm in which instead of explicitly programming computers to perform some tasks, we let them learn from data in order to find the underlying patterns in the data. In few words, machine learning is the science of giving the machine the ability to reason about the data. 

The term [machine learning](https://en.wikipedia.org/wiki/Machine_learning) was coined by Arthur Samuel in 1959. At that time, Arthur defined machine learning as a:

> *Field of study that gives computers the ability to learn without being explicitly programmed.*

A more technical definition of machine learning was provided by Tom M. Mitchell in 1997. Here is how Tom defined machine learning: 

> *A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E.*


Wikipedia provides a much clear definition of machine learning: 

> *Machine learning (ML) is the study of computer algorithms that improve automatically through experience and by the use of data. It is seen as a part of artificial intelligence. Machine learning algorithms build a model based on sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to do so. - Wikipedia.*

What does that mean?

In simple words, machine learning algorithms are trained on data rather than being programmed explicitly.

### Artificial Intelligence, Data Science, Machine Learning, and Deep Learning

AI or Artificial intelligence, data science, machine learning, and deep learning are used interchangeably, but they are quite different.

AI is a branch of computer science concerned with building intelligent machines capable of performing tasks at the level of human. AI seeks to mimic human. AI is an interdisciplinary field that involves machine learning, programming, robotics, data science, etc...

Machine learning on the other hand is the branch of AI and as we saw, it is concerned with giving the machine the ability to learn from data. Machine learning algorithms consists of shallow or classical algorithms such as decision trees and deep learning algorithms such as convolutional neural networks. We will learn more about these algorithms in the next parts. 

Deep learning is a branch of machine learning that deals with the study of artificial neural networks and it was inspired by the human brain. Classical machine learning algorithms needs a lot of feature engineering, but deep learning algorithms can extract features in huge amount of data such as images themselves.  

![figure](https://github.com/Nyandwi/machine_learning_complete/raw/main/images/ai-ml-dl.png)
*Figure 1-1: The difference between AI, machine learning and deep learning*

Data science is also an interdisciplinary field that deals with using data to solve business problems with various techniques. A concise definition of data science was provided by Cassie Kozyrkov: *"Data Science is the science of making data useful"*. 

Below illustration clearly shows what's really is data science.

![fig1-2.png](https://github.com/Nyandwi/machine_learning_complete/raw/main/images/venn-diagram.png)
*Figure 1-2: A slight modification of Conway's orginal venn diagram describing the field of data science.*

### Ordinary Programming Vs Machine Learning

In ordinary programming, the job of the programmer is to clearly write every single rule that makes up the task he/she is trying to accomplish. In order to get the results, she/he must write all rules that acts up on the data. 

Machine learning flips that. Instead of having to write the rules that makes up a particular application, we can feed data and results(or labels) to the machine learning model, and its job can be to determine the set of rules that map the data and labels. 

Let's take a real world example. If you wanted to build an application that given a picture of person can determine if he/she is wearing or not wearing a facemask, you can just feed a bunch of images of people with and without facemasks to the machine learning model, and the model can learn the rules or patterns that map the images to whether they have a facemask or not. 

You can even extends that further and use those learned rules to recognize facemasks in the images that were never seen by the that model. 

![figure](https://github.com/Nyandwi/machine_learning_complete/raw/main/images/traditional-ml.png)
*Figure 1-3: Traditional Programming vs Deep Learning*

Approaching a facemask recognition problem with rule based programming would really be a hard problem. You would have to write lots of code that would later turn out to not work typically because your program will be tested on different kinds of facemasks and people in various scenarios and it's almost impossible to express that in rules. Whereas with machine learning, all you need is a bunch of images of people with and without facemasks, and there you are few steps away from getting an effective facemask recognizer. We will do this in practice in the later parts, specifically in the section of Deep Computer Vision.

### Applications of Machine Learning

Before we step into further machine learning foundations, let's look at some of its most exciting applications. 

Machine learning has transformed many industries, from banking, manufacturing, streaming, autonomous vehicles, agriculture, etc...In fact, most of the tech products and services we use daily possess some sorts of machine learning algorithms running in their backgrounds.  

Here are the most commomly machine learning use cases:

* **Fraud detection**: Banks and other financial organizations can use machine learning to detect frauds in real time. 

* **Loan repayment prediction**: Banks can also use the historical data of their clients to predict if they will be able to repay back the loans before granting it to them. 

* **Diagnozing diseases and predicting the survival rate**: Machine learning is increasingly finding its value in medicine. It can assist medical professionals in diagnozing diseases in handful of minutes. Medical professionals can also use machine learning to predict the likelihood or a course of disease or survival rate(prognosis).

* **Detecting defects in industry**: Some manufacturing companies use machine vision to inspect defects in the products which ultimately result in speeding up the production process, automating the inspection task, reducing the cost and human workload. You can learn more about visual inspection in [2020 State of AI-Based Machine Vision by Landing AI](https://landing.ai/wp-content/uploads/2020/11/MachineVisionSurvey.pdf). 

* **Churn prediction**:  Organizations that provides some kinds of services can use machine learning to predict if a given customer is likely to opt out from the service or cancel subscription. This can help the organization to improve the customer experiences in order to retain the customers. 

* **Spam detection**: Almost all email providers such as Gmail or Outlook possess the ability to detect spams from all incoming emails to protect the users from fake promotions and scams. 

* **Autonomous vehicles**: Todays autonomous vehicles such as self driving cars use machine learning and deep learning systems to navigate in the roads. Using computer vision, they can be able to detect the pedestrian and traffic lights and signs and other surrounding objects. 

There are many more applications of machine learning and the list could go on. For example, a given ads agency can use machine learning to learn the kinds of things that their visitors are interested in and they can use the results to place the relevant ads on the website. Same for streaming services like YouTube and Netflix. These services uses machine learning to suggest the best media to their clients based on their interests.

### When And When Not to Use Machine Learning

Machine learning is an incredible technology and it has shown a lot of successes in solving various real world problems. However, like any other technology, machine learning is not suitable for solving all kinds of problems. It is thus equally important to know when and when not to use machine learning.

When to use machine learning? Machine learning is preferred when approaching:

* Problems that are too complex to be solved by ordinary programming. For these kinds of problems, it's probably safe to try machine learning. There is no way one can write all rules that can be used for recognizing facemasks or detect spam emails accurately for example.

* Problems that involve visual reasoning and language understanding such as image recognition, speech recognition, machine translation, etc...As we will see later, large scale perception or visual and language problems are typically handled by deep learning systems. 

* Fast changing problems where the characteristics of the problems changes with time, and there is a need to keep the system functioning well. Machine learning is suitable for these sorts of problems because machine learning algorithms can be retrained on new data. 

* Problems that are clear and have simple goals such as yes/no question or predicting a single continous number such as the quantity of product likely to be consumed in a given time.  Andrew Ng., Founder of DeepLearning.AI and Adjunct Stanford Professor likes to say that machine learning (employed for automation purpose) is likely to succeed when solving a problem that takes a human a second or less to accomplish such as detecting defects in a product. Recognizing if there is a defect in a product is very simple yes/no question and take a second or less to complete. 

With that said, you may not use machine learning when:

* You want the predictions made by your model to be fully explainable. This is because most machine learning models are considered to be `blackbox`. 
* You do not have a reliable data for the problem you're trying to solve. A simple example here is trying to use machine learning for predicting stocks. Stock market data is unreliable and can change in a matter of seconds without any logical reasons, and so, it's pretty hard to for a model to learn some useful patterns from such unreliability. 
* You can solve your problem with ordinary programming or a simple heuristic methods. 
* You want a solution that will never need to be updated. The predictions made by machine learning models decay overtime, so if you are not ready to update data and retrain models frequently, you may have to consider non machine learning techniques. 

Machine learning keeps transforming things that people never thought and with its vibrant online community, we will will keep to be surprised but in the meantime, it's a safe belt to use it in problems in which the solution can be in your favor because machine learning systems are hard to maintain. 

We talked about when you should use machine learning and when you should not, but also, there are other areas where machine learning is being heavily used but with extra care and human in the loop. Example of such critical areas include medicine, self driving cars, etc...In some of those areas like self driving cars(or driver assistants), machine learning is surely a big factor but also because the cost of error made by the model can be very high, human assistance becomes important.

### Types of Machine Learning Systems

In broad, there are 3 main types of machine learning systems that are:

* Supervised learning
* Unsupervised learning
* Reinforcement learning

Let's review all of these types to get a high level understanding of what's they really mean.

#### Supervised Learning

Most machine learning tasks fall into supervised learning type. As the name implies, a supervised learning model is trained with input data along with some form of guidance that we can call labels. In other words, a supervised learning model maps the input data (or X in many textbooks) to output labels (y). Labels are also known as targets and they act as a description of the input data. 

The example of facemask recognition that we used in above sections is a good example of supervised learning. In broad, there are 2 main kinds of supervised learning problems that are:

* **Classification problems** where the task is to identify a given category from numerous categories or simply make choice between a number of categories. Another example of classification task is to identify if the incoming email is either spam or not based on the email contents.

* **Regression problems** where the goal is to predict a continuous value of something. A classical example for this category is to predict the price of the used car given its features such as brand, age, number of doors, number of sits, safety level, maintenance cost, etc...

![figure](https://github.com/Nyandwi/machine_learning_complete/raw/main/images/class-reg.png)
*Figure 1-4: Graphical representation of classification and regression problems*

Supervised learning algorithms includes shallow algorithms such as linear and logistic regression, decision trees, random forests, K-Nearest Neighbors(KNN), and support vector machines(SVM). Neural networks can be both supervised(like using them for image classification) and unsupervised. 

With that said, there are other advanced tasks that falls into supervised learning type such as:

* Image captioning where the goal is to predict the caption of a given image. 
* Object detection where the goal is to recognize the object in image and draw the bounding box around it. 
* Image segmentation where the goal is to group the pixels that make up particular objects in the image. 

![figure](https://github.com/Nyandwi/machine_learning_complete/raw/main/images/vision.png)
*Figure 1-5: Advanced Tasks: Object detection, image segmentation, image captioning. You can test these advanced algorithms on your images using [vision-explorer](https://vision-explorer.allenai.org)*. 

Some of those tasks can involve both classification and regression. Take an example for object detection, a task of recognizing and localizing an object in an image: it involves classification(recognizing the object among many other objects) and regression(predicting the coordinates of the objects in an image to make a bounding box).

If any of the things we are talking about sounds unfamiliar, do not worry. There is no way to explain all things at once, but as we progress, things will get clear.

#### Unsupervised Learning

Supervised learning algorithms are trained with data and labels. Conversely, unsupervised learning algorithms are trained on unlabelled data. 

Unsupervised learning algorithms are primarily used for:

* Clustering: K-Means
* Dimension reduction and data visualization: Principal Component Analysis(PCA), t-Distributed Stochastic Neighbor Embedding(t-SNE). 

There are many more algorithms that could also be used for those 2 tasks, but, we will cover K-Means, PCA, and t-SNE because they are commonly used.

#### Reinforcement Learning

Reinforcement learning is a special type of machine learning that is most applicable in robotics and games. 

In reinforcement learning, a learning system called *an agent* can perceives the environment, performs some actions, and gets *rewarded* or *penalized* depending on how it is performing. The main goal of the agent is to accumulate as much as rewards as possible.

The *agent* learns the best strategy(*policy*) necessary for getting the most reward itself. 

Let's summarize the types of machine learning systems. By far, supervised and unsupervised learning are the two commonly used types of machine learning. Semi-supervised and self-supervised learning are also getting attractions in deep learning community, but they are still in research. We will focus more those two practical types: supervised and unsupervised.

### The Typical Machine Learning Workflow

Although every machine learning problem is unique, they all follow a similar workflow. In this section, we will learn how to approach machine learning problems systematically.

Overall, a typical machine learning project workflow consists of: 
* Defining and formulating a problem
* Collecting data
* Establishing a baseline
* Exploratory data analysis(EDA)
* Preparing data
* Selecting and training a model
* Performing error analysis and improving a model
* Evaluating a model
* Deploying a model

Let's talk about each step in brief.

#### Defining a Problem

Everything starts here. Problem definition is the important and the initial step in any machine learning project. This is where you make sure you understand the problem really well. Understanding the problem will give you proper intuitions about the next steps to follow such as right learning algorithms, etc. But wait, what does it mean to understand the problem?

Understanding the problem is all about diving deep into the details of the problem at hand and asking the right questions. First, it's important to narrow down the problem until you can have a simple and a well defined goal. Here are examples of simple goals: To *classify* products into different categories, to *predict* the price of a used car given its features (such as brand, age, etc...), to *recognize* if a person is wearing a facemask, to *divide* customers into different groups that share similar behaviors, etc...As you can see, the goal can tell whether the problem is classification, regression, or clustering...

At this stage, avoid vague words. The simpler you can formulate the problem, the better things will be down the hall. It's also worth questioning if the project should be pursued. Most problems do not require machine learning. 

Problem definition also goes beyond determining the goal and objective of the project to thinking about the data that will be needed. Machine learning models relies on the data, and the better models comes from better data. Do you have data that contains the things you want to predict? Models are not magical things, they are mathematical functions that takes data along with labels, and determine the patterns that can be used to make predictions on unseen data. If the data does not contain meaningful information relevant to what you want to predict, you will get poor predictions. 

After you understand the problem and you have an idea of the data you want, the next step is to collect it.

#### Collecting Data

This is usually the next stage after formulating a problem. Before we talk about collecting data, let's even understand the meaning of data. According to wikipedia, "data are a set of values of qualitative or quantitative variables about one or more persons or objects."

There are 2 main types of data that are: 
* Structured data that are organized in tabular or spreadsheet format. Example of tabular data includes customer records, car sales, etc...

* Unstructure data such as images, texts, sounds, and videos. Unstructured data are not organized as the former. 

Nowdays, there are lots of open-source datasets on platforms like Kaggle, Google datasets, UCL, and government websites. So, if you are solving a problem that someone solved before, it's very likely that you will find it somewhere in those platforms, or other public sources like this [repository](https://github.com/awesomedata/awesome-public-datasets). Your job as machine learning engineer is to find the relevant data that you can use to solve the presented problem.

That said, there are times that you will have to collect your own data, especially if you are solving a problem that no one solved before. In this case, consider the time that you will have to spend collecting data and the cost. You also do not need to wait until you have your desired data points before you can start. Embrace ML development early on so that you can learn if you (really) need more data. This idea is inspired by Andrew Ng.

Also, when collecting the data, quality is better than quantity. There are times where small data but good data can outwork big poor data. The amount of data you need is going to depend on the problem you're solving and its scope, but whatever the problem is, aiming to collect good data is the way to go.

#### Establishing a Baseline

Without a benchmark, you won't know how to evaluate your results properly. A baseline is the simplest model that can solve your problem with minimal requirements. It does not have to be a model. It can be an existing open source application, a statistical analysis or intuitions you get from data at a quick glance.

The single most purpose of a baseline is to act as a reference point when comparing the actual model with the baseline. The ultimate goal is to beat a baseline, and sometime, if you can't beat it, it might mean the project is not worth pursuing, or the baseline can be all you need.

#### Exploratory data analysis(EDA)

Before manipulating the data, it is quite important to learn about the dataset. This can be overlooked, but doing it well will help you know the effective strategies to be applied while cleaning the data.

Go through some values, plot some features, and try to understand the correlation between them. If the work is vision-related, visualize some images, spot what’s missing in the images. Are they diverse enough? What types of image scenarios can you add? Or what are images that can mislead the model?

Here are other things that you would want to inspect in the data:

* Duplicate values and samples
* Corrupted or data with unsupported formats (ex: having an image of .txt and with 0 Kilobytes)
* Class imbalances
* Biases
  
Before performing EDA, split the data into the training set, validation and test sets to avoid data leakage. The training set is used for training the model, validation set is used for evaluating the model performance during training to suggest improvements, and test set is for evaluating the final and best model performance. Validation and test set should have the same statistical distribution. 

Also, to avoid data leakage, do not touch the test set in EDA or anywhere before the model training.

#### Data Preprocessing

Data processing is perhaps the biggest part of any machine learning project. There is a notion that Data Scientists and Machine Learning Engineers spend more than 80% of their time preparing the data and this makes sense because the real world data are messy.

In this step, it is where you convert the raw data to go in a format that can be accepted by the machine learning algorithms.

Data preprocessing is hard because there are different types of data and the way you process one is different to the other. For example, in structured data, the way you process numerical features is going to be different to categorical features. Also in unstructured data, the way you manipulate images is going to be different to how you manipulate texts or sounds.

As the next parts will cover the practical implementations of typical data preprocessing steps, let's be general about things you're likely going to deal with while manipulating the features:

* **Imputing missing values:** Missing values can either be filled, removed or left as they are. There are various strategies for missing values such as mean, median, frequent imputations, backward and forward fill, and iterative imputations. The right imputation technique depends on the problem and the dataset. With the exception of tree based models, most machine learning models do not accept missing values. 

* **Encoding categorical features:** Categorical features are all types of features that have categorical values. For example, A gender feature having the values male and female is a categorical feature. You will want to encode such types of features. The techniques for encoding them are label encoding where you can assign 0 to Male and 0 to Female, or one hot encoding where you can get the binary representations (0s and 1s) in one hot matrix. You will see this later in practice.

* **Scaling the numeric features:** Most ML models work well when the input values are scaled to small values because they can train and converge faster than they would otherwise. There are two main scaling techniques that are normalization and standardization. Normalization rescales the feautures to the values between 0 and 1 whereas standardization rescales the features to have mean of 0 and a unit standard deviation. If you are aware that your data has normal or gausian distribution, normalization can be a good choice. Otherwise, standardization will work well in many cases. 

In many textbooks and courses, data preprocessing is also referred to data cleaning or data preparation. Feature engineering is also a part of data preprocessing. Feature engineering is a creative task and it require some extra knowledge about the data and the problem as it involves creating new features from existing features.

#### Selecting and Training a Model

Selecting, creating, and training a machine learning model is the tiniest part in any typical machine learning workflow. There are different types of models but in broad, most of them falls into these categories: linear models such as linear and logistic regression, tree-based models such as decision trees, ensemble models such as random forests, and finally neural networks. 

Depending on your problem, you can choose any relevant model from these categories or tries many of them. But, it is worth mentioning that getting a model that can ultimately solve a given problem is no *free lunch scenario*. You have to experiment with different models to get one that works for your problem and dataset.

To reduce your modelling curve, here are a few things that you can consider while choosing a machine learning model:

* **The scope of the problem:** The scope or type of your problem can give a strong signal on what learning algorithm to use.  Take an example: If you are going to build an image classifier, neural networks (Convolutional Neural Networks specifically) might be your go to algorithm. 

* **The size of the dataset:** Linear models tend to work well in small data problems, whereas ensemble models and neural network can work well when given huge amount of data.
* **The level of interpretability:** If you want the predictions of your model to be explainable, neural networks may not help. Tree based models such as decision trees can be explainable compared to other models.
* **Training time:** Complex models (neural networks and ensemble models) will take too long to train and thus draining the computation resources. On the other hand, linear models can train faster.

As you can see, there is a trade-off during model selection. You want explainability, choose models that can provide that for you, most models don't. You have a small dataset or you care about the training time, same thing, a right model for you.

#### Performing Error Analysis

Performing error analysis will guide you throughout the process of improving the results of the model. The improvement can either be from the data or the model.

One of the best way to do error analysis is to plot the learning curve and to try noticing where the model is failing and what might be the reason, and the right actions that you can take to reduce the errors.

To improve the model part, you can try different model configuration values or hyperparameters. You can also try different models to see one that works well. But also, good model comes from good data, so it's important to spend time examining the results of the model with respect to the input data.

Here are questions that you can yourself iteratively in the process error analysis:

* Is the model doing poorly on all classes or is it one specific class?
* Is it because there are not enough data points for that particular class compared to other classes?
* There are trade-offs and limits on how much you can do to reduce the errors. Is there a room for improvement?

Often, the improvements will not come from tuning the model, but spending time to increase the number of training samples and data quality.

When improving the data, you can create artificial data (a.k.a data augmentation). This will work well most of the time. The whole error analysis is an iterative process, keep doing it and always aim to improve the data than the model.

#### Evaluating the Model

When you have done a great job of getting a working model, it's time to evaluate it on unseen or test data, not on training data. 

And when the model works well on the test set, here comes the last step.

#### Deploying a Model

Model deployment is the last part in this workflow. When all the previous steps has gone right, and you are happy about the results of the model on the test set, the next step will be to deploy the model so that the users can start to make requests and get predictions or enhanced services. I call this process as *machine learning in action* because it what actually bring the value of machine learning.

### Evaluation Metrics

Evaluation metrics are used to measure the performance of the machine learning models. Earlier in this introduction to machine learning, we saw that most problems are either regression and classification, and they are evaluated differently. Let us start with metrics that are used for evaluating regression problems.

#### Regression Metrics

In regression tasks, the goal is to predict the continuous value. The difference between the actual value and the predicted value is called the *error*.

*Error = Actual value - Predicted value*

The square of the error over all samples is called Mean Squarred Error(MSE).

*MSE = SQUARE(Actual value - Predicted value)/Number of Samples*

***MSE Actual Formula***: 

$$\frac 1n\sum_{i=1}^n(y_i-\hat{y}_i)^2$$


Taking the square root of the mean squared error will give the Root Mean Squared Error(RMSE). RMSE is the most used regression metric. 

***RMSE Actual Formula***: 

$$\sqrt{\frac 1n\sum_{i=1}^n(y_i-\hat{y}_i)^2}$$

There are times that you will work with the datasets containing outliers. A suitable metric for those kinds of datasets is Mean Absolute Error (MAE). As simple as calculating MSE, MAE is also the absolute of the error.

*MAE = ABSOLUTE (Actual value - Predicted Value)*

***MAE Actual Formula***

$$\frac 1n\sum_{i=1}^n|y_i-\hat{y}_i|$$

Like said, MAE is very sensitive to outliers. It is a suitable metric for all kinds of problems that are likely to have abnormal scenarios such as time series.

#### Classification Metrics

In classification problems, the goal is to predict the categories/class.

*Accuracy* is the most commonly used metric. The accuracy shows the ability of the model in making the correct predictions. Take an example, in a horse and human classifier. If you have 250 training images for horses and the same number for humans, and the model can confidently predict 400 images, then the accuracy is 400/500 = 0.8, so your model is 80% accurate. 

The accuracy is simply an indicator of how your model is in making correct predictions and it will only be useful if you have a balanced dataset (like we had 250 images for horses and 250 images for humans). 

When we have a skewed dataset or when there are imbalances, we need a different perspective on how we evaluate the model. Take an example, if we have 450 images for horses and 50 images for humans, there is a chance of 90% (450/500) that the horse will be correctly predicted because the dataset is dominated by the horses. But how about humans? Well, it's obvious that the model will struggle at predicting them correctly. 

This is where we introduce other metrics that can be far more useful than accuracy such as *precision*, *recall*, and *F1 score*. 

*Precision* shows the percentage of the positive predictions that are actually positive. To quote [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall), precision answer the following question: `What proportion of positive identifications was actually correct?`

The *recall* on the other hand shows the percentage of the actual positive samples that were classified correctly. It answers the question: `What proportion of actual positives was identified correctly?`

There is a tradeoff between precision and recall. Often, increasing precision will decrease recall and vice versa. To simplify things, we combine both of these two metrics into a single metric called the *F1 score*. 

F1 score is the harmonic mean of precision and recall, and it shows how good the model is at classifying all classes without having to balance between precision and recall. If either precision or recall is very low, the F1 score is going to be low too.

Both accuracy, precision, and recall can be calculated easily by using a **confusion matrix**. A confusion matrix shows the number of correct and incorrect predictions made by a classifier in all available classes. 

More intuitively, a confusion matrix is made of 4 main elements: True negatives, false negatives, true positives, and false positives.

* **True Positives(TP)**: Number of samples that are correctly classified as positive, and their actual label is positive.

* **False Positives (FP)**: Number of samples that are incorrectly classified as positive, when in fact their actual label is negative.

* **True Negatives (TN)**: Number of samples that are correctly classified as negative, and their actual label is negative.

* **False Negatives (FN)**: Number of samples that are incorrectly classified as negative, when in fact their actual label is positive.

The accuracy that we talked about is the number of correct examples over total examples. So, that is 

*Accuracy = (TP + TN) / (TP + TN + FP + FN)*

Precision is the model accuracy on predicting positive examples. 

*Precision = TP / (TP + FP)*

On the other hand, Recall is the model ability to predict the positive examples correctly. 

*Recall = TP / (TP+FN)*

The higher the recall and precision, the better the model is at making accurate predictions but there is a tradeoff between them. Increasing precision will reduce the recall and vice versa. 

A classifier that doesn't have false positives has a precision of 1, and a classifier that doesn't have false negatives has a recall of 1. Ideally, a perfect classifier will have the precision and recall of 1.

We can combine both precision and recall to get another metric called F1 Score. F1 Score is the harmonic mean of precision and recall. 

*F1 Score = 2 x(precision x recall) / (precision + recall)*

Take an example of the following confusion matrix. 

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1631962774907/yLNqC8pKw.png)

From the above confusion matrix:

* `Accuracy = (TP + TN) / (TP + TN + FP + FN) = (71 +36)/(71+36+7+0) = 0.93 or 93%`
* `Precision = TP / (TP + FP) = 71/(71+7) =0.91 or  91%`
* `Recall = TP / (TP + FN) = 71/(71+0) = 1, or 100%`
* `F1 score = 2PR / (P + R) = 2x0.91x1/(0.91+1) = 0.95, or 95%`

Both accuracy, confusion matrix, precision, recall, and F1 score are implemented easily in Scikit-Learn, a machine learning framework used to build classical ML algorithms. We will learn more about Scikit-Learn in the next part.

### The Challenges of Machine Learning Systems

Like any other technology, machine learning has challenges. What makes machine learning different to normal software development is that it involves data and codes(model). Either of those brings its own challenges, and there is usually no clear ways of handling them.

Data is the primary ingredient of machine learning, and better models are the results of better data. In real world, though, better data are rare. Most datasets are messy. They require extensive amount of time to prepare, and they can turn out to not be helpful. Also, you may have heard about data labeling. Data labeling is a challenging, time-consuming and expensive task and there are always chances of having mismatch in labels. 

Even if you may have good data, you can still get poor models because it is very easy to mess up during data cleaning process. We will see some practical scenarios latter about this. 

That said, models are also not perfect. Some models are computationaly expensive. Also, they tend to *underfit* and *overfit* the training data. Underfitting and overfitting deserves their own topic as they are things that we are likely to deal with.

#### Underfittind and Overfitting

Building a machine learning model that can fit the training data well is not a trivial task. Often, at the initial training, the model will either underfit or overfit the data. Some machine learning models take that to the extreme. Take an example, when training decision trees, it is very likely that they will overfit the data at first.

There is a trade off between underfitting/overfitting, and so it's important to understand the difference between them and how to handle each and each. Understanding and handling underfitting and overfitting is a critical task in diagonizing machine learning models.

##### Underfitting (Low Bias)

Underfitting happens when the model does poor on the training data. It can be caused by the fact that the model is simple for the training data or the data does not contains the things that you are trying to predict. Good data has *high predictive power*, and poor data has *low predictive power*.

Here are some of the techniques that can be used to deal with underfitting:

* Use complex models. If you are using linear models, try other complex models like Random forests or Support Vector Machines. Not to mention neural networks if you are dealing with unstructured data (images, texts, sounds)
* Add more training data and use good features. Good features have high predictive power.
* Reduce the regularization.
* If you're using neural networks, increase the number of epochs/training iterations. If the epochs are very few, the model may not be able to learn the underlying rules in data and so it will not perform well.

##### Overfitting (High Variance)

Overfitting is the reverse of underfitting. An overfitted model will do well on the training data but will be poor when supplied with new data (the data that the model never saw).

Overfitting is caused by using model which is too complex for the dataset and few training examples.

Here are techniques to handle overfitting:

* Try simple models or simplify the current model. Some machine learning algorithms can be simplified. Take an example: in neural networks, you can reduce the number of layers or neurons. Also in classical algorithms like Support Vector Machines, you can try different kernels, a linear kernel is simple than a polynomial kernel.
  
* Find more training data.
* Stop the training early (also know as early stopping)
* Use different regularization techniques like dropout(in neural networks).


To summarize this, it is very important to be able to understand why the model is not doing well. If the model is being poor on the data it was trained on, you know it is underfitting and you know what to do about it.

Also, beside improving and expanding the training data, you often have to tune hyperparameters to get a model that can generalize well. While there are techniques that simplified hyperparameter search(like [Grid search](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV), [Random search](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html), [Keras Tuner](https://keras.io/keras_tuner/)), it is important to understand the hyperparameters of the model you are using so that you can know their proper search space.

We are getting to the end of the introduction to machine learning. Perhaps you might have seen some unfamiliar terms or concepts. That's okay. As we go from basics to practices, things will be clear.

### Final Notes

This was about introduction to machine learning basics. Machine learning is a field of computer science and a subfield of AI that is concerned with giving computers the ability to perform some tasks without being programmed explicitly, but rather learning from the data. Machine learning is already transforming industries. It is being used in areas like medicine, banking and finance, consumer electronics, autonomous vehicles, agriculture, etc...

We have also learned about different types of machine learning that are supervised learning, unsupervised learning, semi-supervised learning, self-supervised learning, and reinforcement learning. Also, we saw a typical flow of machine learning projects and the challenges of training learning systems, and how to overcome them.


---

## 📈 Linear Regression Theory & Formulation


### Slide 1: Regression



---

### Slide 2: Regression

• Definition : A statistical technique for estimating the relationship between two or more variables.

• The estimated relationship is represented in the form of an equation. The general form of regression equation is as follows:

• Y = β0 + β1X + ε

• Where,

• X = Independent variable that used to predict the dependent variable (also called predictor variable)

• Y = Dependent variable being predicted by regression model (also called response variable)

• β0 & β1 are called regression parameters and interpreted as

• β0 = Intercept (The average value of dependent variable Y when independent variable X is zero)

• β1 = Slope (The change in dependent variable Y for the unit change in independent variable X)

• ε = Residual (error), the portion of the dependent variable that is not explained by the model.

---

### Slide 3: Regression : Explanation



---

### Slide 4: Linear Vs Nonlinear



---

### Slide 5: Regression : Model types

• 2 & more predictor variables

• Only1 predictor variable

• Model is a linear equation

• Model is a linear equation

• Model is a nonlinear equation

• Model is a nonlinear equation

---

### Slide 6: Regression : General Methodology

• General Steps for Regression analysis :

• Exploring the relationship by plotting the independent variable with dependent variable.

• Specify the Regression model. (Simple linear, multiple linear or Nonlinear)

• Estimate the regression parameters with minimum residual(error).

• Analyze the relationship & predict the dependent variable for future.

• Example:

---

### Slide 7: Regression : some common models

• Simple linear Regression: To predict the sales using the expenditure on advertisement.

• Multiple linear Regression: To predict the compressive strength of cement using the contents of cement.

• Logistic Regression: To predict that a customer will take loan or not based on the factors such as age, gender, income, marital status etc.

---

### Slide 8: Linear Regression



---

### Slide 9: Linear Regression - Univariate

• Data set

• pairs

• Expression for linear regression:

• Parameters

• Variable

• What is the “best” value of              that predicts the data?

• Let the difference/error between model and real value for  be

• We want the model to “predict” values closer to real values 

• Method

• y

• x

• Let us minimize average error w.r.t

• and

• Contd.

---

### Slide 10: Linear Regression - Univariate

• Leads to two simultaneous algebraic equations in

• Can be solved easily to get “best”

• Exercise 1: Show that

• Exercise 2: For the dataset, calculate parameters and show that

• Exercise 3: use Excel “trendline” method to validate that this is correct.

---

### Slide 11: Assumptions of linear regression

• There is a linear relation between dependence variable and target.

• There is no correlation between residuals.

• Residuals have constant variance (homoscedasticity).

• Residuals of the model are normally distributed  Sum of  should be close to zero.

• Exercise 4: verify this for the dataset

• If residuals are not normally distributed, one can use GLM (Generalized linear Model).

---

### Slide 12: Linear Regression - Multivariate

• Univariate regression can be generalized to models with multiple variables (say p)

• Define feature vector with p components:          

• Arranging different  as row of a matrix, construct data matrix       Size of :

• Construct target vector with N components:           be 									prediction from model

• Let the vector of coefficients/parameters be:

• Multivariate Linear Regression model becomes:

• The parameters that minimizes the square of residuals is given by the matrix equation:

• In practice, this is not used for large data set. Why? Matrix inverse takes long time for large matrix

---

### Slide 13: Linear Regression - Multivariate

• Gradient descent algorithm is used to minimize the residuals:

• Starting with random values for run a loop where in each step, the parameters are updated by following rule:

• After sufficient steps, the algorithm will find  that minimizes the residuals

• In practice, dataset is divided into 2: - train-set  used to train the model to get the “best”  (includes hyper-parameter optimization)- test-set   used to validate the

• 

• “Learning rate” – adjusted to get best performance from algorith

---

### Slide 14: Linear Regression – Model Quality

• How does one measure the quality of the model?

• Model Accuracy

• Calculate root mean square error (RMSE) on test data: Measures the model accuracy against new data / unseen data

• Calculate R2 score: Measures how much variation in target variable is predicted by dependent variable

• Model Robustness

• Measure of the sensitivity of the model to (outlier) data (and violation of regression assumption)

• M-statistics

• Ability to explain

• Model that is easily explainable is preferred over complicated modelsmodel with fewer parameters are more stable, less sensitive to data distribution, robust

---

### Slide 15: THANK YOU FOR YOURATTENTION




---

## 🧪 Hands-on Exercise: Linear Regression in Python


```python
import numpy as np
import pandas as pd
```

# <font color=red>Hands-on exercise - Linear Regression </font>

#### In this exercise, Boston housing dataset in Scikit-Learn will be used to perform linear regression. There are three basic steps:

#### (1) Load Dataset
#### (2) Exploratory Data Analysis (EDA)
#### (3) Machine Learning model

## <font color=red>1. Load Dataset</font>

##### First, load the dataset and get some "feel" of the data:  how many variables, size of the dataset, what are the variables, what does each variable mean, etc.

```python
# Load Boston housing dataset from Scikit-Learn 
from sklearn.datasets import load_boston
dataset = load_boston ()

# Convert it to Pandas Datafram & find number of records
boston_df=pd.DataFrame(dataset.data, columns=dataset.feature_names)

# Add target variable which is stored separately
boston_df['MEDV']=dataset.target

# Print number of records
print ("Number of records: ", len(boston_df))
```

**Output:**
```text
Number of records:  506
```

```python
# Explore the data
boston_df.head()
```

**Output:**
```text
CRIM    ZN  INDUS  CHAS    NOX     RM   AGE     DIS  RAD    TAX  \
0  0.00632  18.0   2.31   0.0  0.538  6.575  65.2  4.0900  1.0  296.0   
1  0.02731   0.0   7.07   0.0  0.469  6.421  78.9  4.9671  2.0  242.0   
2  0.02729   0.0   7.07   0.0  0.469  7.185  61.1  4.9671  2.0  242.0   
3  0.03237   0.0   2.18   0.0  0.458  6.998  45.8  6.0622  3.0  222.0   
4  0.06905   0.0   2.18   0.0  0.458  7.147  54.2  6.0622  3.0  222.0   

   PTRATIO       B  LSTAT  MEDV  
0     15.3  396.90   4.98  24.0  
1     17.8  396.90   9.14  21.6  
2     17.8  392.83   4.03  34.7  
3     18.7  394.63   2.94  33.4  
4     18.7  396.90   5.33  36.2
```

```python
# Get the list of column names
x_list=boston_df.columns.tolist()

# Remove the target column name
y_target=x_list.pop()

print ("Variables:", x_list, "Target:", y_target)
```

**Output:**
```text
Variables: ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'] Target: MEDV
```

```python
# Find what each column name means from the dataset
print (dataset.DESCR[300:1300])
```

**Output:**
```text
- CRIM     per capita crime rate by town
        - ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
        - INDUS    proportion of non-retail business acres per town
        - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
        - NOX      nitric oxides concentration (parts per 10 million)
        - RM       average number of rooms per dwelling
        - AGE      proportion of owner-occupied units built prior to 1940
        - DIS      weighted distances to five Boston employment centres
        - RAD      index of accessibility to radial highways
        - TAX      full-value property-tax rate per $10,000
        - PTRATIO  pupil-teacher ratio by town
        - B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
        - LSTAT    % lower status of the population
        - MEDV     Median value of owner-occupied homes in $1000's

    :Missing Attribute Values: None

    :Creator: Harrison, D. and Rubi
```

## <font color=red> 2. Simple EDA</font>

```python
import seaborn as sns

# Visualize the target dependency on the variables - Split them into two rows for better visualization
sns.pairplot (boston_df, x_vars=x_list[:6], y_vars=[y_target]);
```

```python
sns.pairplot (boston_df, x_vars=x_list[6:], y_vars=[y_target]);
```

##### <span style='background:yellow'><font color=blue> Remark: LSTAT and RM has strong impact on the target variable MEDV - can be used first to do regression</font></span>

```python
# Plot the distribution of the target 
sns.distplot(boston_df['MEDV']);
```

```python
# Get how the variables are correlated 
boston_corr = boston_df.corr(method="pearson")

sns.heatmap(data=boston_corr);
```

## <font color=red> 3. Machine Learning Model</font>

### (a) Use specific columns (by-hand feature engineering) 
This amounts to selecting columns which has strong correlation with target variables and using them for regression. Later, we use feature selection algorithm to automatically select features.

```python
# Selecting first LSTAT and RM
X = pd.DataFrame(boston_df, columns=['LSTAT', 'RM'])
Y = boston_df['MEDV']
```

```python
# Split the dataset into train and test - do a 80% for train and 20% for test
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=10)

print(X_train.shape, X_test.shape)
print(Y_train.shape, Y_test.shape)
```

**Output:**
```text
(404, 2) (102, 2)
(404,) (102,)
```

```python
# Train the model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

linear_model = LinearRegression()
linear_model.fit(X_train, Y_train)
```

**Output:**
```text
LinearRegression()
```

```python
# Now predict using the model on the training set first
y_train_predict = linear_model.predict(X_train)

#...and then for the test dataset
y_test_predict = linear_model.predict(X_test)
```

```python
# Plot the predicted versus actual in the training set
import matplotlib.pyplot as plt
color=sns.color_palette()

fig, axes=plt.subplots (1,2)
ax1=sns.regplot (x=Y_train, y=y_train_predict, ax=axes[0], color=color[0])
ax2=sns.regplot (x=Y_test, y=y_test_predict, ax=axes[1], color=color[1])

ax1.set_title('Train')
ax2.set_title('Test')
plt.tight_layout()
plt.show();
```

```python
# Get distribution of the residuals
residual_train = np.abs(np.subtract(np.array(Y_train), np.array(y_train_predict)))
residual_test = np.abs(np.subtract(np.array(Y_test), np.array(y_test_predict)))

fig, axes=plt.subplots (1, 2)
color=sns.color_palette()

ax1=sns.distplot (residual_train, ax=axes[0], color=color[0])
ax2=sns.distplot (residual_test, ax=axes[1], color=color[1])

ax1.set_title('Train')
ax2.set_title('Test')
plt.tight_layout()
plt.show();
```

```python
# Root-mean-square of the residuals for the train and test
rmse_train = (np.sqrt(mean_squared_error(Y_train, y_train_predict)))
r2_train = r2_score (Y_train, y_train_predict)

rmse_test = (np.sqrt(mean_squared_error(Y_test, y_test_predict)))
r2_test = r2_score (Y_test, y_test_predict)

print ("RMSE for train:", rmse_train, "R2 score for train:", r2_train)
print ("RMSE for test :", rmse_test, "R2 score for test :", r2_test)
```

**Output:**
```text
RMSE for train: 5.290363048551534 R2 score for train: 0.6363353379616083
RMSE for test : 6.434440411684905 R2 score for test : 0.6041142735229121
```

### (b) Use all variables available in the data set

```python
# Create the new List
Xf = pd.DataFrame(boston_df, columns=x_list)
Yf = boston_df['MEDV']

# Create training and testing dataset
Xf_train, Xf_test, Yf_train, Yf_test = train_test_split(Xf, Yf, test_size = 0.2, random_state=10)

# Train a new model
linear_model_full = LinearRegression()
linear_model_full.fit(Xf_train, Yf_train)

# Predict on the train and test dataset
yf_train_predict = linear_model_full.predict(Xf_train)
yf_test_predict = linear_model_full.predict(Xf_test)
```

```python
# Plot the target for train and test
fig, axes=plt.subplots (1,2)
ax1=sns.regplot (x=Yf_train, y=yf_train_predict, ax=axes[0], color=color[0])
ax2=sns.regplot (x=Yf_test, y=yf_test_predict, ax=axes[1], color=color[1])

ax1.set_title('Train')
ax2.set_title('Test')
plt.tight_layout()
plt.show();
```

```python
# Plot the distributions of the residuals
# Get distribution of the residuals
residual_train = np.abs(np.subtract(np.array(Yf_train), np.array(yf_train_predict)))
residual_test = np.abs(np.subtract(np.array(Yf_test), np.array(yf_test_predict)))

fig, axes=plt.subplots (1, 2)
color=sns.color_palette()

ax1=sns.distplot (residual_train, ax=axes[0], color=color[0])
ax2=sns.distplot (residual_test, ax=axes[1], color=color[1])

ax1.set_title('Train')
ax2.set_title('Test')
plt.tight_layout()
plt.show();
```

```python
# Root-mean-square of the residuals for the train and test
rmse_train = (np.sqrt(mean_squared_error(Yf_train, yf_train_predict)))
r2_train = r2_score (Yf_train, yf_train_predict)

rmse_test = (np.sqrt(mean_squared_error(Yf_test, yf_test_predict)))
r2_test = r2_score (Yf_test, yf_test_predict)

print ("RMSE for train:", rmse_train, "R2 score for train:", r2_train)
print ("RMSE for test :", rmse_test, "R2 score for test :", r2_test)
```

**Output:**
```text
RMSE for train: 4.385300318036732 R2 score for train: 0.750121534530608
RMSE for test : 5.866341999333023 R2 score for test : 0.6709339839115628
```

##### <font color=blue> <span style='background:yellow'>Remark: Better R2 score compared to using only 2 variables. Also the root-mean-square error improved.
</span></font>

### (c) Feature selection

##### First, let us understand concept of penalized linear regression. 
Use L2 penalty term (Exercise: understand mathematics behind this)

```python
# Create the new List
Xl2 = pd.DataFrame(boston_df, columns=x_list)
Yl2 = boston_df['MEDV']

# Create training and testing dataset
Xl2_train, Xl2_test, Yl2_train, Yl2_test = train_test_split(Xl2, Yl2, test_size = 0.2, random_state=10)
```

```python
from sklearn.linear_model import Ridge

# Train the model
rr_model = Ridge(alpha=1, fit_intercept=True)
rr_model.fit(Xl2_train, Yl2_train)

# Predict on the train and test dataset
yl2_train_predict = rr_model.predict(Xl2_train)
yl2_test_predict = rr_model.predict(Xl2_test)
```

```python
# Root-mean-square of the residuals for the train and test
rmse_train = (np.sqrt(mean_squared_error(Yl2_train, yl2_train_predict)))
r2_train = r2_score (Yl2_train, yl2_train_predict)

rmse_test = (np.sqrt(mean_squared_error(Yl2_test, yl2_test_predict)))
r2_test = r2_score (Yl2_test, yl2_test_predict)

print ("RMSE for train:", rmse_train, "R2 score for train:", r2_train)
print ("RMSE for test :", rmse_test, "R2 score for test :", r2_test)
```

**Output:**
```text
RMSE for train: 4.4037623578050304 R2 score for train: 0.7480131375144308
RMSE for test : 5.914025559798654 R2 score for test : 0.6655627286231776
```

```python
# Loop over alpha (hyper-parameter)
for a in range(0,20,1):
    rr_model = Ridge(alpha=a, fit_intercept=True)
    rr_model.fit(Xl2_train, Yl2_train)
    
    yl2_train_predict = rr_model.predict(Xl2_train)
    yl2_test_predict = rr_model.predict(Xl2_test)
    
    r2_train = r2_score (Yl2_train, yl2_train_predict)
    r2_test = r2_score (Yl2_test, yl2_test_predict)
    print ("Alpha: ", a, "R2 score for train: ", r2_train, "R2 score for train:", r2_test)
    
    #rmse_train = (np.sqrt(mean_squared_error(Yfs_train, yfs_train_predict)))
    #rmse_test = (np.sqrt(mean_squared_error(Yfs_test, yfs_test_predict)))
    #print ("Alpha: ", a, "RMSE for train: ", rmse_train, "RMSE for train:", rmse_test)
```

**Output:**
```text
Alpha:  0 R2 score for train:  0.750121534530608 R2 score for train: 0.6709339839115636
Alpha:  1 R2 score for train:  0.7480131375144308 R2 score for train: 0.6655627286231776
Alpha:  2 R2 score for train:  0.7460479437895559 R2 score for train: 0.6622292412268544
Alpha:  3 R2 score for train:  0.7447268254905919 R2 score for train: 0.659911365760797
Alpha:  4 R2 score for train:  0.7437967422515108 R2 score for train: 0.6581187601991185
Alpha:  5 R2 score for train:  0.7431032285719339 R2 score for train: 0.65663196673309
Alpha:  6 R2 score for train:  0.7425601943488435 R2 score for train: 0.655340638009081
Alpha:  7 R2 score for train:  0.7421175860240857 R2 score for train: 0.6541835131022498
Alpha:  8 R2 score for train:  0.7417447486126676 R2 score for train: 0.6531238354330902
Alpha:  9 R2 score for train:  0.7414220134753399 R2 score for train: 0.6521381509060348
Alpha:  10 R2 score for train:  0.7411362529191663 R2 score for train: 0.6512107290932625
Alpha:  11 R2 score for t
... [Output truncated for brevity]
```

##### <font color=blue> <span style='background:yellow'>Remark: R2 score decreases monotonically as alpha increases. L2 penalty does not lead to any improvement in the prediction.</span></font>

##### Next we use L1 penalty (also called LASSO) for feature selection

```python
# Create the new List
Xfs = pd.DataFrame(boston_df, columns=x_list)
Yfs = boston_df['MEDV']

# Create training and testing dataset
Xfs_train, Xfs_test, Yfs_train, Yfs_test = train_test_split(Xfs, Yfs, test_size = 0.2, random_state=10)
```

```python
from sklearn.linear_model import Lasso

# Train the model
lr_model = Lasso (alpha=1, fit_intercept=True)
lr_model.fit(Xfs_train, Yfs_train)

# Predict on the train and test dataset
yfs_train_predict = rr_model.predict(Xfs_train)
yfs_test_predict = rr_model.predict(Xfs_test)
```

```python
# Root-mean-square of the residuals for the train and test
rmse_train = (np.sqrt(mean_squared_error(Yfs_train, yfs_train_predict)))
r2_train = r2_score (Yfs_train, yfs_train_predict)

rmse_test = (np.sqrt(mean_squared_error(Yfs_test, yfs_test_predict)))
r2_test = r2_score (Yl2_test, yl2_test_predict)

print ("RMSE for train:", rmse_train, "R2 score for train:", r2_train)
print ("RMSE for test :", rmse_test, "R2 score for test :", r2_test)
```

**Output:**
```text
RMSE for train: 4.479144462830916 R2 score for train: 0.7393124510934346
RMSE for test : 6.098772977236354 R2 score for test : 0.6443414842276636
```


---

## 🎯 Logistic Regression Classifier Deep Dive


<a class="anchor" id="0"></a>
# **Logistic Regression Classifier Tutorial**

<a class="anchor" id="0.1"></a>
# **Table of Contents**


1.	[Introduction to Logistic Regression](#1)
2.	[Logistic Regression intuition](#2)
3.	[Assumptions of Logistic Regression](#3)
4.	[Types of Logistic Regression](#4)
5.	[Import libraries](#5)
6.	[Import dataset](#6)
7.	[Exploratory data analysis](#7)
8.	[Declare feature vector and target variable](#8)
9.	[Split data into separate training and test set](#9)
10.	[Feature engineering](#10)
11.	[Feature scaling](#11)
12.	[Model training](#12)
13.	[Predict results](#13)
14.	[Check accuracy score](#14)
15.	[Confusion matrix](#15)
16.	[Classification metrices](#16)
17.	[Adjusting the threshold level](#17)
18.	[ROC - AUC](#18)
19.	[k-Fold Cross Validation](#19)
20.	[Hyperparameter optimization using GridSearch CV](#20)
21.	[Results and conclusion](#21)

# **1. Introduction to Logistic Regression** <a class="anchor" id="1"></a>


[Table of Contents](#0.1)


When data scientists may come across a new classification problem, the first algorithm that may come across their mind is **Logistic Regression**. It is a supervised learning classification algorithm which is used to predict observations to a discrete set of classes. Practically, it is used to classify observations into different categories. Hence, its output is discrete in nature. **Logistic Regression** is also called **Logit Regression**. It is one of the most simple, straightforward and versatile classification algorithms which is used to solve classification problems.

# **2. Logistic Regression intuition** <a class="anchor" id="2"></a>


[Table of Contents](#0.1)


In statistics, the **Logistic Regression model** is a widely used statistical model which is primarily used for classification purposes. It means that given a set of observations, Logistic Regression algorithm helps us to classify these observations into two or more discrete classes. So, the target variable is discrete in nature.


The Logistic Regression algorithm works as follows -

## **Implementation of linear equation**


Logistic Regression algorithm works by implementing a linear equation with independent or explanatory variables to predict a response value. For example, we consider the example of number of hours studied and probability of passing the exam. Here, number of hours studied is the explanatory variable and it is denoted by x1. Probability of passing the exam is the response or target variable and it is denoted by z.


If we have one explanatory variable (x1) and one response variable (z), then the linear equation would be given mathematically with the following equation-

    z = β0 + β1x1    

Here, the coefficients β0 and β1 are the parameters of the model.

For example : 

    C = 5/9 x (F - 32)

If there are multiple explanatory variables such as prediction of House Prices across a country, then the above equation can be extended to

    z = β0 + β1x1+ β2x2+……..+ βnxn
    
Here, the coefficients β0, β1, β2 and βn are the parameters of the model.

So, the predicted response value is given by the above equations and is denoted by z.

## **Sigmoid Function**

This predicted response value, denoted by z is then converted into a probability value that lie between 0 and 1. We use the sigmoid function in order to map predicted values to probability values. This sigmoid function then maps any real value into a probability value between 0 and 1.

In machine learning, **sigmoid function is used to map predictions to probabilities**. The sigmoid function has an S shaped curve. It is also called sigmoid curve.

A Sigmoid function is a special case of the Logistic function. It is given by the following mathematical formula.

Graphically, we can represent sigmoid function with the following graph.

### Sigmoid Function

![Sigmoid Function](https://miro.medium.com/max/970/1*Xu7B5y9gp0iL5ooBj7LtWw.png)

## **Decision boundary**

The sigmoid function returns a probability value between 0 and 1. This probability value is then mapped to a discrete class which is either “0” or “1”. In order to map this probability value to a discrete class (pass/fail, yes/no, true/false), we select a threshold value. This threshold value is called Decision boundary. Above this threshold value, we will map the probability values into class 1 and below which we will map values into class 0.

Mathematically, it can be expressed as follows:-

p ≥ 0.5 => class = 1

p < 0.5 => class = 0 

Generally, the decision boundary is set to 0.5. So, if the probability value is 0.8 (> 0.5), we will map this observation to class 1. Similarly, if the probability value is 0.2 (< 0.5), we will map this observation to class 0. This is represented in the graph below-

![Decision boundary in sigmoid function](https://ml-cheatsheet.readthedocs.io/en/latest/_images/logistic_regression_sigmoid_w_threshold.png)

## **Making predictions**

Now, we know about sigmoid function and decision boundary in logistic regression. We can use our knowledge of sigmoid function and decision boundary to write a prediction function. A prediction function in logistic regression returns the probability of the observation being positive, Yes or True. We call this as class 1 and it is denoted by P(class = 1). If the probability inches closer to one, then we will be more confident about our model that the observation is in class 1, otherwise it is in class 0.

# **3. Assumptions of Logistic Regression** <a class="anchor" id="3"></a>


[Table of Contents](#0.1)


The Logistic Regression model requires several key assumptions. These are as follows:-

1. Logistic Regression model **requires the dependent variable to be binary, multinomial or ordinal in nature**.

2. It requires the observations to be independent of each other. So, the observations should not come from repeated measurements.

3. Logistic Regression algorithm **requires little or no multicollinearity among the independent variables**. It means that the independent variables should not be too highly correlated with each other.

4. Logistic Regression model assumes linearity of independent variables and log odds.

5. The success of Logistic Regression model depends on the sample sizes. Typically, it requires a large sample size to achieve the high accuracy.

# **4. Types of Logistic Regression** <a class="anchor" id="4"></a>


[Table of Contents](#0.1)


Logistic Regression model can be classified into three groups based on the target variable categories. These three groups are described below:-

### 1. Binary Logistic Regression

In Binary Logistic Regression, the target variable has two possible categories. The common examples of categories are yes or no, good or bad, true or false, spam or no spam and pass or fail.


### 2. Multinomial Logistic Regression

In Multinomial Logistic Regression, the target variable has three or more categories which are not in any particular order. So, there are three or more nominal categories. The examples include the type of categories of fruits - apple, mango, orange and banana.


### 3. Ordinal Logistic Regression

In Ordinal Logistic Regression, the target variable has three or more ordinal categories. So, there is intrinsic order involved with the categories. For example, the student performance can be categorized as poor, average, good and excellent.

# **5. Import libraries** <a class="anchor" id="5"></a>


[Table of Contents](#0.1)

```python
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
%matplotlib inline
import os
import warnings
warnings.filterwarnings('ignore')
```

# **6. Import dataset** <a class="anchor" id="6"></a>


[Table of Contents](#0.1)

```python
data = 'weatherAUS.csv'

df = pd.read_csv(data)
```

# **7. Exploratory data analysis** <a class="anchor" id="7"></a>


[Table of Contents](#0.1)

```python
# view dimensions of dataset

df.shape
```

**Output:**
```text
(142193, 24)
```

We can see that there are 142193 instances and 24 variables in the data set.

```python
# preview the dataset

df.head()
```

**Output:**
```text
Date Location  MinTemp  MaxTemp  Rainfall  Evaporation  Sunshine  \
0  2008-12-01   Albury     13.4     22.9       0.6          NaN       NaN   
1  2008-12-02   Albury      7.4     25.1       0.0          NaN       NaN   
2  2008-12-03   Albury     12.9     25.7       0.0          NaN       NaN   
3  2008-12-04   Albury      9.2     28.0       0.0          NaN       NaN   
4  2008-12-05   Albury     17.5     32.3       1.0          NaN       NaN   

  WindGustDir  WindGustSpeed WindDir9am  ... Humidity3pm  Pressure9am  \
0           W           44.0          W  ...        22.0       1007.7   
1         WNW           44.0        NNW  ...        25.0       1010.6   
2         WSW           46.0          W  ...        30.0       1007.6   
3          NE           24.0         SE  ...        16.0       1017.6   
4           W           41.0        ENE  ...        33.0       1010.8   

   Pressure3pm  Cloud9am  Cloud3pm  Temp9am  Temp3pm  RainToday  RISK_MM  \
0       1007.1       8.0       
... [Output truncated for brevity]
```

```python
col_names = df.columns

col_names
```

**Output:**
```text
Index(['Date', 'Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation',
       'Sunshine', 'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
       'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
       'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am',
       'Temp3pm', 'RainToday', 'RISK_MM', 'RainTomorrow'],
      dtype='object')
```

### Drop  RISK_MM variable

It is given in the dataset description, that we should drop the `RISK_MM` feature variable from the dataset description. So, we 
should drop it as follows-

```python
df.drop(['RISK_MM'], axis=1, inplace=True)
```

```python
# view summary of dataset

df.info()
```

### Types of variables


In this section, We segregate the dataset into categorical and numerical variables. There are a mixture of categorical and numerical variables in the dataset. Categorical variables have data type object. Numerical variables have data type float64.


First of all, We will find categorical variables.

```python
# find categorical variables

categorical = [var for var in df.columns if df[var].dtype=='O']

print('There are {} categorical variables\n'.format(len(categorical)))

print('The categorical variables are :', categorical)
```

**Output:**
```text
There are 7 categorical variables

The categorical variables are : ['Date', 'Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday', 'RainTomorrow']
```

```python
# view the categorical variables

df[categorical].head()
```

**Output:**
```text
Date Location WindGustDir WindDir9am WindDir3pm RainToday  \
0  2008-12-01   Albury           W          W        WNW        No   
1  2008-12-02   Albury         WNW        NNW        WSW        No   
2  2008-12-03   Albury         WSW          W        WSW        No   
3  2008-12-04   Albury          NE         SE          E        No   
4  2008-12-05   Albury           W        ENE         NW        No   

  RainTomorrow  
0           No  
1           No  
2           No  
3           No  
4           No
```

### Summary of categorical variables


- There is a date variable. It is denoted by `Date` column.


- There are 6 categorical variables. These are given by `Location`, `WindGustDir`, `WindDir9am`, `WindDir3pm`, `RainToday` and  `RainTomorrow`.


- There are two binary categorical variables - `RainToday` and  `RainTomorrow`.


- `RainTomorrow` is the target variable.

## Explore problems within categorical variables


First, I will explore the categorical variables.


### Missing values in categorical variables

```python
# check missing values in categorical variables

df[categorical].isnull().sum()
```

**Output:**
```text
Date                0
Location            0
WindGustDir      9330
WindDir9am      10013
WindDir3pm       3778
RainToday        1406
RainTomorrow        0
dtype: int64
```

```python
# print categorical variables containing missing values

cat1 = [var for var in categorical if df[var].isnull().sum()!=0]

print(df[cat1].isnull().sum())
```

**Output:**
```text
WindGustDir     9330
WindDir9am     10013
WindDir3pm      3778
RainToday       1406
dtype: int64
```

We can see that there are only 4 categorical variables in the dataset which contains missing values. These are `WindGustDir`, `WindDir9am`, `WindDir3pm` and `RainToday`.

### Frequency counts of categorical variables


Now, I will check the frequency counts of categorical variables.

```python
# view frequency of categorical variables

for var in categorical: 
    
    print(df[var].value_counts())
```

**Output:**
```text
2017-01-10    49
2017-06-21    49
2017-05-08    49
2013-11-25    49
2014-03-18    49
              ..
2007-11-08     1
2007-12-27     1
2008-01-02     1
2007-11-13     1
2008-01-27     1
Name: Date, Length: 3436, dtype: int64
Canberra            3418
Sydney              3337
Perth               3193
Darwin              3192
Hobart              3188
Brisbane            3161
Adelaide            3090
Bendigo             3034
Townsville          3033
AliceSprings        3031
MountGambier        3030
Ballarat            3028
Launceston          3028
Albany              3016
Albury              3011
PerthAirport        3009
MelbourneAirport    3009
Mildura             3007
SydneyAirport       3005
Nuriootpa           3002
Sale                3000
Watsonia            2999
Tuggeranong         2998
Portland            2996
Woomera             2990
Cobar               2988
Cairns              2988
Wollongong          2983
GoldCoast           2980
WaggaWagga          2976
Penrith             2964
... [Output truncated for brevity]
```

```python
# view frequency distribution of categorical variables

for var in categorical: 
    
    print(df[var].value_counts()/np.float(len(df)))
```

**Output:**
```text
2017-01-10    0.000345
2017-06-21    0.000345
2017-05-08    0.000345
2013-11-25    0.000345
2014-03-18    0.000345
                ...   
2007-11-08    0.000007
2007-12-27    0.000007
2008-01-02    0.000007
2007-11-13    0.000007
2008-01-27    0.000007
Name: Date, Length: 3436, dtype: float64
Canberra            0.024038
Sydney              0.023468
Perth               0.022455
Darwin              0.022448
Hobart              0.022420
Brisbane            0.022230
Adelaide            0.021731
Bendigo             0.021337
Townsville          0.021330
AliceSprings        0.021316
MountGambier        0.021309
Ballarat            0.021295
Launceston          0.021295
Albany              0.021211
Albury              0.021175
PerthAirport        0.021161
MelbourneAirport    0.021161
Mildura             0.021147
SydneyAirport       0.021133
Nuriootpa           0.021112
Sale                0.021098
Watsonia            0.021091
Tuggeranong         0.021084
Portland            0.021070
Woomera   
... [Output truncated for brevity]
```

### Number of labels: cardinality


The number of labels within a categorical variable is known as **cardinality**. A high number of labels within a variable is known as **high cardinality**. High cardinality may pose some serious problems in the machine learning model. So, I will check for high cardinality.

```python
# check for cardinality in categorical variables

for var in categorical:
    
    print(var, ' contains ', len(df[var].unique()), ' labels')
```

**Output:**
```text
Date  contains  3436  labels
Location  contains  49  labels
WindGustDir  contains  17  labels
WindDir9am  contains  17  labels
WindDir3pm  contains  17  labels
RainToday  contains  3  labels
RainTomorrow  contains  2  labels
```

We can see that there is a `Date` variable which needs to be preprocessed. I will do preprocessing in the following section.


All the other variables contain relatively smaller number of variables.

### Feature Engineering of Date Variable

```python
df['Date'].dtypes
```

**Output:**
```text
dtype('O')
```

We can see that the data type of `Date` variable is object. I will parse the date currently coded as object into datetime format.

```python
# parse the dates, currently coded as strings, into datetime format

df['Date'] = pd.to_datetime(df['Date'])
```

```python
# extract year from date

df['Year'] = df['Date'].dt.year

df['Year'].head()
```

**Output:**
```text
0    2008
1    2008
2    2008
3    2008
4    2008
Name: Year, dtype: int64
```

```python
# extract month from date

df['Month'] = df['Date'].dt.month

df['Month'].head()
```

**Output:**
```text
0    12
1    12
2    12
3    12
4    12
Name: Month, dtype: int64
```

```python
# extract day from date

df['Day'] = df['Date'].dt.day

df['Day'].head()
```

**Output:**
```text
0    1
1    2
2    3
3    4
4    5
Name: Day, dtype: int64
```

```python
# again view the summary of dataset

df.info()
```

We can see that there are three additional columns created from `Date` variable. Now, I will drop the original `Date` variable from the dataset.

```python
# drop the original Date variable

df.drop('Date', axis=1, inplace = True)
```

```python
# preview the dataset again

df.head()
```

**Output:**
```text
Location  MinTemp  MaxTemp  Rainfall  Evaporation  Sunshine WindGustDir  \
0   Albury     13.4     22.9       0.6          NaN       NaN           W   
1   Albury      7.4     25.1       0.0          NaN       NaN         WNW   
2   Albury     12.9     25.7       0.0          NaN       NaN         WSW   
3   Albury      9.2     28.0       0.0          NaN       NaN          NE   
4   Albury     17.5     32.3       1.0          NaN       NaN           W   

   WindGustSpeed WindDir9am WindDir3pm  ...  Pressure3pm  Cloud9am  Cloud3pm  \
0           44.0          W        WNW  ...       1007.1       8.0       NaN   
1           44.0        NNW        WSW  ...       1007.8       NaN       NaN   
2           46.0          W        WSW  ...       1008.7       NaN       2.0   
3           24.0         SE          E  ...       1012.8       NaN       NaN   
4           41.0        ENE         NW  ...       1006.0       7.0       8.0   

   Temp9am  Temp3pm  RainToday  RainTomorrow  Year  Month 
... [Output truncated for brevity]
```

Now, we can see that the `Date` variable has been removed from the dataset.

### Explore Categorical Variables


Now, I will explore the categorical variables one by one.

```python
# find categorical variables

categorical = [var for var in df.columns if df[var].dtype=='O']

print('There are {} categorical variables\n'.format(len(categorical)))

print('The categorical variables are :', categorical)
```

**Output:**
```text
There are 6 categorical variables

The categorical variables are : ['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday', 'RainTomorrow']
```

We can see that there are 6 categorical variables in the dataset. The `Date` variable has been removed. First, I will check missing values in categorical variables.

```python
# check for missing values in categorical variables 

df[categorical].isnull().sum()
```

**Output:**
```text
Location            0
WindGustDir      9330
WindDir9am      10013
WindDir3pm       3778
RainToday        1406
RainTomorrow        0
dtype: int64
```

We can see that `WindGustDir`, `WindDir9am`, `WindDir3pm`, `RainToday` variables contain missing values. I will explore these variables one by one.

### Explore `Location` variable

```python
# print number of labels in Location variable

print('Location contains', len(df.Location.unique()), 'labels')
```

**Output:**
```text
Location contains 49 labels
```

```python
# check labels in location variable

df.Location.unique()
```

**Output:**
```text
array(['Albury', 'BadgerysCreek', 'Cobar', 'CoffsHarbour', 'Moree',
       'Newcastle', 'NorahHead', 'NorfolkIsland', 'Penrith', 'Richmond',
       'Sydney', 'SydneyAirport', 'WaggaWagga', 'Williamtown',
       'Wollongong', 'Canberra', 'Tuggeranong', 'MountGinini', 'Ballarat',
       'Bendigo', 'Sale', 'MelbourneAirport', 'Melbourne', 'Mildura',
       'Nhil', 'Portland', 'Watsonia', 'Dartmoor', 'Brisbane', 'Cairns',
       'GoldCoast', 'Townsville', 'Adelaide', 'MountGambier', 'Nuriootpa',
       'Woomera', 'Albany', 'Witchcliffe', 'PearceRAAF', 'PerthAirport',
       'Perth', 'SalmonGums', 'Walpole', 'Hobart', 'Launceston',
       'AliceSprings', 'Darwin', 'Katherine', 'Uluru'], dtype=object)
```

```python
# check frequency distribution of values in Location variable

df.Location.value_counts()
```

**Output:**
```text
Canberra            3418
Sydney              3337
Perth               3193
Darwin              3192
Hobart              3188
Brisbane            3161
Adelaide            3090
Bendigo             3034
Townsville          3033
AliceSprings        3031
MountGambier        3030
Ballarat            3028
Launceston          3028
Albany              3016
Albury              3011
PerthAirport        3009
MelbourneAirport    3009
Mildura             3007
SydneyAirport       3005
Nuriootpa           3002
Sale                3000
Watsonia            2999
Tuggeranong         2998
Portland            2996
Woomera             2990
Cobar               2988
Cairns              2988
Wollongong          2983
GoldCoast           2980
WaggaWagga          2976
Penrith             2964
NorfolkIsland       2964
Newcastle           2955
SalmonGums          2955
CoffsHarbour        2953
Witchcliffe         2952
Richmond            2951
Dartmoor            2943
NorahHead           2929
BadgerysCreek       2928

... [Output truncated for brevity]
```

```python
# let's do One Hot Encoding of Location variable
# get k-1 dummy variables after One Hot Encoding 
# preview the dataset with head() method

pd.get_dummies(df.Location, drop_first=True).head()
```

**Output:**
```text
Albany  Albury  AliceSprings  BadgerysCreek  Ballarat  Bendigo  Brisbane  \
0       0       1             0              0         0        0         0   
1       0       1             0              0         0        0         0   
2       0       1             0              0         0        0         0   
3       0       1             0              0         0        0         0   
4       0       1             0              0         0        0         0   

   Cairns  Canberra  Cobar  ...  Townsville  Tuggeranong  Uluru  WaggaWagga  \
0       0         0      0  ...           0            0      0           0   
1       0         0      0  ...           0            0      0           0   
2       0         0      0  ...           0            0      0           0   
3       0         0      0  ...           0            0      0           0   
4       0         0      0  ...           0            0      0           0   

   Walpole  Watsonia  Williamtown  Witchcliffe  Wollo
... [Output truncated for brevity]
```

### Explore `WindGustDir` variable

```python
# print number of labels in WindGustDir variable

print('WindGustDir contains', len(df['WindGustDir'].unique()), 'labels')
```

**Output:**
```text
WindGustDir contains 17 labels
```

```python
# check labels in WindGustDir variable

df['WindGustDir'].unique()
```

**Output:**
```text
array(['W', 'WNW', 'WSW', 'NE', 'NNW', 'N', 'NNE', 'SW', 'ENE', 'SSE',
       'S', 'NW', 'SE', 'ESE', nan, 'E', 'SSW'], dtype=object)
```

```python
# check frequency distribution of values in WindGustDir variable

df.WindGustDir.value_counts()
```

**Output:**
```text
W      9780
SE     9309
E      9071
N      9033
SSE    8993
S      8949
WSW    8901
SW     8797
SSW    8610
WNW    8066
NW     8003
ENE    7992
ESE    7305
NE     7060
NNW    6561
NNE    6433
Name: WindGustDir, dtype: int64
```

```python
# let's do One Hot Encoding of WindGustDir variable
# get k-1 dummy variables after One Hot Encoding 
# also add an additional dummy variable to indicate there was missing data
# preview the dataset with head() method

pd.get_dummies(df.WindGustDir, drop_first=True, dummy_na=True).head()
```

**Output:**
```text
ENE  ESE  N  NE  NNE  NNW  NW  S  SE  SSE  SSW  SW  W  WNW  WSW  NaN
0    0    0  0   0    0    0   0  0   0    0    0   0  1    0    0    0
1    0    0  0   0    0    0   0  0   0    0    0   0  0    1    0    0
2    0    0  0   0    0    0   0  0   0    0    0   0  0    0    1    0
3    0    0  0   1    0    0   0  0   0    0    0   0  0    0    0    0
4    0    0  0   0    0    0   0  0   0    0    0   0  1    0    0    0
```

```python
# sum the number of 1s per boolean variable over the rows of the dataset
# it will tell us how many observations we have for each category

pd.get_dummies(df.WindGustDir, drop_first=True, dummy_na=True).sum(axis=0)
```

**Output:**
```text
ENE    7992
ESE    7305
N      9033
NE     7060
NNE    6433
NNW    6561
NW     8003
S      8949
SE     9309
SSE    8993
SSW    8610
SW     8797
W      9780
WNW    8066
WSW    8901
NaN    9330
dtype: int64
```

We can see that there are 9330 missing values in WindGustDir variable.

### Explore `WindDir9am` variable

```python
# print number of labels in WindDir9am variable

print('WindDir9am contains', len(df['WindDir9am'].unique()), 'labels')
```

**Output:**
```text
WindDir9am contains 17 labels
```

```python
# check labels in WindDir9am variable

df['WindDir9am'].unique()
```

**Output:**
```text
array(['W', 'NNW', 'SE', 'ENE', 'SW', 'SSE', 'S', 'NE', nan, 'SSW', 'N',
       'WSW', 'ESE', 'E', 'NW', 'WNW', 'NNE'], dtype=object)
```

```python
# check frequency distribution of values in WindDir9am variable

df['WindDir9am'].value_counts()
```

**Output:**
```text
N      11393
SE      9162
E       9024
SSE     8966
NW      8552
S       8493
W       8260
SW      8237
NNE     7948
NNW     7840
ENE     7735
ESE     7558
NE      7527
SSW     7448
WNW     7194
WSW     6843
Name: WindDir9am, dtype: int64
```

```python
# let's do One Hot Encoding of WindDir9am variable
# get k-1 dummy variables after One Hot Encoding 
# also add an additional dummy variable to indicate there was missing data
# preview the dataset with head() method

pd.get_dummies(df.WindDir9am, drop_first=True, dummy_na=True).head()
```

**Output:**
```text
ENE  ESE  N  NE  NNE  NNW  NW  S  SE  SSE  SSW  SW  W  WNW  WSW  NaN
0    0    0  0   0    0    0   0  0   0    0    0   0  1    0    0    0
1    0    0  0   0    0    1   0  0   0    0    0   0  0    0    0    0
2    0    0  0   0    0    0   0  0   0    0    0   0  1    0    0    0
3    0    0  0   0    0    0   0  0   1    0    0   0  0    0    0    0
4    1    0  0   0    0    0   0  0   0    0    0   0  0    0    0    0
```

```python
# sum the number of 1s per boolean variable over the rows of the dataset
# it will tell us how many observations we have for each category

pd.get_dummies(df.WindDir9am, drop_first=True, dummy_na=True).sum(axis=0)
```

**Output:**
```text
ENE     7735
ESE     7558
N      11393
NE      7527
NNE     7948
NNW     7840
NW      8552
S       8493
SE      9162
SSE     8966
SSW     7448
SW      8237
W       8260
WNW     7194
WSW     6843
NaN    10013
dtype: int64
```

We can see that there are 10013 missing values in the `WindDir9am` variable.

### Explore `WindDir3pm` variable

```python
# print number of labels in WindDir3pm variable

print('WindDir3pm contains', len(df['WindDir3pm'].unique()), 'labels')
```

**Output:**
```text
WindDir3pm contains 17 labels
```

```python
# check labels in WindDir3pm variable

df['WindDir3pm'].unique()
```

**Output:**
```text
array(['WNW', 'WSW', 'E', 'NW', 'W', 'SSE', 'ESE', 'ENE', 'NNW', 'SSW',
       'SW', 'SE', 'N', 'S', 'NNE', nan, 'NE'], dtype=object)
```

```python
# check frequency distribution of values in WindDir3pm variable

df['WindDir3pm'].value_counts()
```

**Output:**
```text
SE     10663
W       9911
S       9598
WSW     9329
SW      9182
SSE     9142
N       8667
WNW     8656
NW      8468
ESE     8382
E       8342
NE      8164
SSW     8010
NNW     7733
ENE     7724
NNE     6444
Name: WindDir3pm, dtype: int64
```

```python
# let's do One Hot Encoding of WindDir3pm variable
# get k-1 dummy variables after One Hot Encoding 
# also add an additional dummy variable to indicate there was missing data
# preview the dataset with head() method

pd.get_dummies(df.WindDir3pm, drop_first=True, dummy_na=True).head()
```

**Output:**
```text
ENE  ESE  N  NE  NNE  NNW  NW  S  SE  SSE  SSW  SW  W  WNW  WSW  NaN
0    0    0  0   0    0    0   0  0   0    0    0   0  0    1    0    0
1    0    0  0   0    0    0   0  0   0    0    0   0  0    0    1    0
2    0    0  0   0    0    0   0  0   0    0    0   0  0    0    1    0
3    0    0  0   0    0    0   0  0   0    0    0   0  0    0    0    0
4    0    0  0   0    0    0   1  0   0    0    0   0  0    0    0    0
```

```python
# sum the number of 1s per boolean variable over the rows of the dataset
# it will tell us how many observations we have for each category

pd.get_dummies(df.WindDir3pm, drop_first=True, dummy_na=True).sum(axis=0)
```

**Output:**
```text
ENE     7724
ESE     8382
N       8667
NE      8164
NNE     6444
NNW     7733
NW      8468
S       9598
SE     10663
SSE     9142
SSW     8010
SW      9182
W       9911
WNW     8656
WSW     9329
NaN     3778
dtype: int64
```

There are 3778 missing values in the `WindDir3pm` variable.

### Explore `RainToday` variable

```python
# print number of labels in RainToday variable

print('RainToday contains', len(df['RainToday'].unique()), 'labels')
```

**Output:**
```text
RainToday contains 3 labels
```

```python
# check labels in WindGustDir variable

df['RainToday'].unique()
```

**Output:**
```text
array(['No', 'Yes', nan], dtype=object)
```

```python
# check frequency distribution of values in RainToday variable

df.RainToday.value_counts()
```

**Output:**
```text
No     109332
Yes     31455
Name: RainToday, dtype: int64
```

```python
# let's do One Hot Encoding of RainToday variable
# get k-1 dummy variables after One Hot Encoding 
# also add an additional dummy variable to indicate there was missing data
# preview the dataset with head() method

pd.get_dummies(df.RainToday, drop_first=True, dummy_na=True).head()
```

**Output:**
```text
Yes  NaN
0    0    0
1    0    0
2    0    0
3    0    0
4    0    0
```

```python
# sum the number of 1s per boolean variable over the rows of the dataset
# it will tell us how many observations we have for each category

pd.get_dummies(df.RainToday, drop_first=True, dummy_na=True).sum(axis=0)
```

**Output:**
```text
Yes    31455
NaN     1406
dtype: int64
```

There are 1406 missing values in the `RainToday` variable.

### Explore Numerical Variables

```python
# find numerical variables

numerical = [var for var in df.columns if df[var].dtype!='O']

print('There are {} numerical variables\n'.format(len(numerical)))

print('The numerical variables are :', numerical)
```

**Output:**
```text
There are 19 numerical variables

The numerical variables are : ['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine', 'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am', 'Temp3pm', 'Year', 'Month', 'Day']
```

```python
# view the numerical variables

df[numerical].head()
```

**Output:**
```text
MinTemp  MaxTemp  Rainfall  Evaporation  Sunshine  WindGustSpeed  \
0     13.4     22.9       0.6          NaN       NaN           44.0   
1      7.4     25.1       0.0          NaN       NaN           44.0   
2     12.9     25.7       0.0          NaN       NaN           46.0   
3      9.2     28.0       0.0          NaN       NaN           24.0   
4     17.5     32.3       1.0          NaN       NaN           41.0   

   WindSpeed9am  WindSpeed3pm  Humidity9am  Humidity3pm  Pressure9am  \
0          20.0          24.0         71.0         22.0       1007.7   
1           4.0          22.0         44.0         25.0       1010.6   
2          19.0          26.0         38.0         30.0       1007.6   
3          11.0           9.0         45.0         16.0       1017.6   
4           7.0          20.0         82.0         33.0       1010.8   

   Pressure3pm  Cloud9am  Cloud3pm  Temp9am  Temp3pm  Year  Month  Day  
0       1007.1       8.0       NaN     16.9     21.8  2008     12    1
... [Output truncated for brevity]
```

### Summary of numerical variables


- There are 16 numerical variables. 


- These are given by `MinTemp`, `MaxTemp`, `Rainfall`, `Evaporation`, `Sunshine`, `WindGustSpeed`, `WindSpeed9am`, `WindSpeed3pm`, `Humidity9am`, `Humidity3pm`, `Pressure9am`, `Pressure3pm`, `Cloud9am`, `Cloud3pm`, `Temp9am` and `Temp3pm`.


- All of the numerical variables are of continuous type.

## Explore problems within numerical variables


Now, I will explore the numerical variables.


### Missing values in numerical variables

```python
# check missing values in numerical variables

df[numerical].isnull().sum()
```

**Output:**
```text
MinTemp            637
MaxTemp            322
Rainfall          1406
Evaporation      60843
Sunshine         67816
WindGustSpeed     9270
WindSpeed9am      1348
WindSpeed3pm      2630
Humidity9am       1774
Humidity3pm       3610
Pressure9am      14014
Pressure3pm      13981
Cloud9am         53657
Cloud3pm         57094
Temp9am            904
Temp3pm           2726
Year                 0
Month                0
Day                  0
dtype: int64
```

We can see that all the 16 numerical variables contain missing values.

### Outliers in numerical variables

```python
# view summary statistics in numerical variables

print(round(df[numerical].describe()),2)
```

**Output:**
```text
MinTemp   MaxTemp  Rainfall  Evaporation  Sunshine  WindGustSpeed  \
count  141556.0  141871.0  140787.0      81350.0   74377.0       132923.0   
mean       12.0      23.0       2.0          5.0       8.0           40.0   
std         6.0       7.0       8.0          4.0       4.0           14.0   
min        -8.0      -5.0       0.0          0.0       0.0            6.0   
25%         8.0      18.0       0.0          3.0       5.0           31.0   
50%        12.0      23.0       0.0          5.0       8.0           39.0   
75%        17.0      28.0       1.0          7.0      11.0           48.0   
max        34.0      48.0     371.0        145.0      14.0          135.0   

       WindSpeed9am  WindSpeed3pm  Humidity9am  Humidity3pm  Pressure9am  \
count      140845.0      139563.0     140419.0     138583.0     128179.0   
mean           14.0          19.0         69.0         51.0       1018.0   
std             9.0           9.0         19.0         21.0          7.0   
min       
... [Output truncated for brevity]
```

On closer inspection, we can see that the `Rainfall`, `Evaporation`, `WindSpeed9am` and `WindSpeed3pm` columns may contain outliers.


We will draw boxplots to visualise outliers in the above variables.

```python
# draw boxplots to visualize outliers

plt.figure(figsize=(15,10))


plt.subplot(2, 2, 1)
fig = df.boxplot(column='Rainfall')
fig.set_title('')
fig.set_ylabel('Rainfall')


plt.subplot(2, 2, 2)
fig = df.boxplot(column='Evaporation')
fig.set_title('')
fig.set_ylabel('Evaporation')


plt.subplot(2, 2, 3)
fig = df.boxplot(column='WindSpeed9am')
fig.set_title('')
fig.set_ylabel('WindSpeed9am')


plt.subplot(2, 2, 4)
fig = df.boxplot(column='WindSpeed3pm')
fig.set_title('')
fig.set_ylabel('WindSpeed3pm')
```

**Output:**
```text
Text(0, 0.5, 'WindSpeed3pm')
```

The above boxplots confirm that there are lot of outliers in these variables.

### Check the distribution of variables


Now, We will plot the histograms to check distributions to find out if they are normal or skewed. If the variable follows normal distribution, then We will do `Extreme Value Analysis` otherwise if they are skewed, I will find IQR (Interquantile range).

```python
# plot histogram to check distribution

plt.figure(figsize=(15,10))


plt.subplot(2, 2, 1)
fig = df.Rainfall.hist(bins=10)
fig.set_xlabel('Rainfall')
fig.set_ylabel('RainTomorrow')


plt.subplot(2, 2, 2)
fig = df.Evaporation.hist(bins=10)
fig.set_xlabel('Evaporation')
fig.set_ylabel('RainTomorrow')


plt.subplot(2, 2, 3)
fig = df.WindSpeed9am.hist(bins=10)
fig.set_xlabel('WindSpeed9am')
fig.set_ylabel('RainTomorrow')


plt.subplot(2, 2, 4)
fig = df.WindSpeed3pm.hist(bins=10)
fig.set_xlabel('WindSpeed3pm')
fig.set_ylabel('RainTomorrow')
```

**Output:**
```text
Text(0, 0.5, 'RainTomorrow')
```

We can see that all the four variables are skewed. So,We will use interquantile range to find outliers.

```python
# find outliers for Rainfall variable

IQR = df.Rainfall.quantile(0.75) - df.Rainfall.quantile(0.25)
Lower_fence = df.Rainfall.quantile(0.25) - (IQR * 3)
Upper_fence = df.Rainfall.quantile(0.75) + (IQR * 3)
print('Rainfall outliers are values < {lowerboundary} or > {upperboundary}'.format(lowerboundary=Lower_fence, upperboundary=Upper_fence))
```

**Output:**
```text
Rainfall outliers are values < -2.4000000000000004 or > 3.2
```

For `Rainfall`, the minimum and maximum values are 0.0 and 371.0. So, the outliers are values > 3.2.

```python
# find outliers for Evaporation variable

IQR = df.Evaporation.quantile(0.75) - df.Evaporation.quantile(0.25)
Lower_fence = df.Evaporation.quantile(0.25) - (IQR * 3)
Upper_fence = df.Evaporation.quantile(0.75) + (IQR * 3)
print('Evaporation outliers are values < {lowerboundary} or > {upperboundary}'.format(lowerboundary=Lower_fence, upperboundary=Upper_fence))
```

**Output:**
```text
Evaporation outliers are values < -11.800000000000002 or > 21.800000000000004
```

For `Evaporation`, the minimum and maximum values are 0.0 and 145.0. So, the outliers are values > 21.8.

```python
# find outliers for WindSpeed9am variable

IQR = df.WindSpeed9am.quantile(0.75) - df.WindSpeed9am.quantile(0.25)
Lower_fence = df.WindSpeed9am.quantile(0.25) - (IQR * 3)
Upper_fence = df.WindSpeed9am.quantile(0.75) + (IQR * 3)
print('WindSpeed9am outliers are values < {lowerboundary} or > {upperboundary}'.format(lowerboundary=Lower_fence, upperboundary=Upper_fence))
```

**Output:**
```text
WindSpeed9am outliers are values < -29.0 or > 55.0
```

For `WindSpeed9am`, the minimum and maximum values are 0.0 and 130.0. So, the outliers are values > 55.0.

```python
# find outliers for WindSpeed3pm variable

IQR = df.WindSpeed3pm.quantile(0.75) - df.WindSpeed3pm.quantile(0.25)
Lower_fence = df.WindSpeed3pm.quantile(0.25) - (IQR * 3)
Upper_fence = df.WindSpeed3pm.quantile(0.75) + (IQR * 3)
print('WindSpeed3pm outliers are values < {lowerboundary} or > {upperboundary}'.format(lowerboundary=Lower_fence, upperboundary=Upper_fence))
```

**Output:**
```text
WindSpeed3pm outliers are values < -20.0 or > 57.0
```

For `WindSpeed3pm`, the minimum and maximum values are 0.0 and 87.0. So, the outliers are values > 57.0.

# **8. Declare feature vector and target variable** <a class="anchor" id="8"></a>


[Table of Contents](#0.1)

```python
X = df.drop(['RainTomorrow'], axis=1)

y = df['RainTomorrow']
```

# **9. Split data into separate training and test set** <a class="anchor" id="9"></a>


[Table of Contents](#0.1)

```python
# split X and y into training and testing sets

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
```

```python
# check the shape of X_train and X_test

X_train.shape, X_test.shape
```

**Output:**
```text
((113754, 24), (28439, 24))
```

# **10. Feature Engineering** <a class="anchor" id="10"></a>


[Table of Contents](#0.1)


**Feature Engineering** is the process of transforming raw data into useful features that help us to understand our model better and increase its predictive power. I will carry out feature engineering on different types of variables.


First, I will display the categorical and numerical variables again separately.

```python
# check data types in X_train

X_train.dtypes
```

**Output:**
```text
Location          object
MinTemp          float64
MaxTemp          float64
Rainfall         float64
Evaporation      float64
Sunshine         float64
WindGustDir       object
WindGustSpeed    float64
WindDir9am        object
WindDir3pm        object
WindSpeed9am     float64
WindSpeed3pm     float64
Humidity9am      float64
Humidity3pm      float64
Pressure9am      float64
Pressure3pm      float64
Cloud9am         float64
Cloud3pm         float64
Temp9am          float64
Temp3pm          float64
RainToday         object
Year               int64
Month              int64
Day                int64
dtype: object
```

```python
# display categorical variables

categorical = [col for col in X_train.columns if X_train[col].dtypes == 'O']

categorical
```

**Output:**
```text
['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday']
```

```python
# display numerical variables

numerical = [col for col in X_train.columns if X_train[col].dtypes != 'O']

numerical
```

**Output:**
```text
['MinTemp',
 'MaxTemp',
 'Rainfall',
 'Evaporation',
 'Sunshine',
 'WindGustSpeed',
 'WindSpeed9am',
 'WindSpeed3pm',
 'Humidity9am',
 'Humidity3pm',
 'Pressure9am',
 'Pressure3pm',
 'Cloud9am',
 'Cloud3pm',
 'Temp9am',
 'Temp3pm',
 'Year',
 'Month',
 'Day']
```

### Engineering missing values in numerical variables

```python
# check missing values in numerical variables in X_train

X_train[numerical].isnull().sum()
```

**Output:**
```text
MinTemp            495
MaxTemp            264
Rainfall          1139
Evaporation      48718
Sunshine         54314
WindGustSpeed     7367
WindSpeed9am      1086
WindSpeed3pm      2094
Humidity9am       1449
Humidity3pm       2890
Pressure9am      11212
Pressure3pm      11186
Cloud9am         43137
Cloud3pm         45768
Temp9am            740
Temp3pm           2171
Year                 0
Month                0
Day                  0
dtype: int64
```

```python
# check missing values in numerical variables in X_test

X_test[numerical].isnull().sum()
```

**Output:**
```text
MinTemp            142
MaxTemp             58
Rainfall           267
Evaporation      12125
Sunshine         13502
WindGustSpeed     1903
WindSpeed9am       262
WindSpeed3pm       536
Humidity9am        325
Humidity3pm        720
Pressure9am       2802
Pressure3pm       2795
Cloud9am         10520
Cloud3pm         11326
Temp9am            164
Temp3pm            555
Year                 0
Month                0
Day                  0
dtype: int64
```

```python
# print percentage of missing values in the numerical variables in training set

for col in numerical:
    if X_train[col].isnull().mean()>0:
        print(col, round(X_train[col].isnull().mean(),4))
```

**Output:**
```text
MinTemp 0.0044
MaxTemp 0.0023
Rainfall 0.01
Evaporation 0.4283
Sunshine 0.4775
WindGustSpeed 0.0648
WindSpeed9am 0.0095
WindSpeed3pm 0.0184
Humidity9am 0.0127
Humidity3pm 0.0254
Pressure9am 0.0986
Pressure3pm 0.0983
Cloud9am 0.3792
Cloud3pm 0.4023
Temp9am 0.0065
Temp3pm 0.0191
```

### Assumption


We assume that the data are missing completely at random (MCAR). There are two methods which can be used to impute missing values. One is mean or median imputation and other one is random sample imputation. When there are outliers in the dataset, we should use median imputation. So, We will use median imputation because median imputation is robust to outliers.


We will impute missing values with the appropriate statistical measures of the data, in this case median. Imputation should be done over the training set, and then propagated to the test set. It means that the statistical measures to be used to fill missing values both in train and test set, should be extracted from the train set only. This is to avoid overfitting.

```python
# impute missing values in X_train and X_test with respective column median in X_train

for df1 in [X_train, X_test]:
    for col in numerical:
        col_median=X_train[col].median()
        df1[col].fillna(col_median, inplace=True)
```

```python
# check again missing values in numerical variables in X_train

X_train[numerical].isnull().sum()
```

**Output:**
```text
MinTemp          0
MaxTemp          0
Rainfall         0
Evaporation      0
Sunshine         0
WindGustSpeed    0
WindSpeed9am     0
WindSpeed3pm     0
Humidity9am      0
Humidity3pm      0
Pressure9am      0
Pressure3pm      0
Cloud9am         0
Cloud3pm         0
Temp9am          0
Temp3pm          0
Year             0
Month            0
Day              0
dtype: int64
```

```python
# check missing values in numerical variables in X_test

X_test[numerical].isnull().sum()
```

**Output:**
```text
MinTemp          0
MaxTemp          0
Rainfall         0
Evaporation      0
Sunshine         0
WindGustSpeed    0
WindSpeed9am     0
WindSpeed3pm     0
Humidity9am      0
Humidity3pm      0
Pressure9am      0
Pressure3pm      0
Cloud9am         0
Cloud3pm         0
Temp9am          0
Temp3pm          0
Year             0
Month            0
Day              0
dtype: int64
```

Now, we can see that there are no missing values in the numerical columns of training and test set.

### Engineering missing values in categorical variables

```python
# print percentage of missing values in the categorical variables in training set

X_train[categorical].isnull().mean()
```

**Output:**
```text
Location       0.000000
WindGustDir    0.065114
WindDir9am     0.070134
WindDir3pm     0.026443
RainToday      0.010013
dtype: float64
```

```python
# print categorical variables with missing data

for col in categorical:
    if X_train[col].isnull().mean()>0:
        print(col, (X_train[col].isnull().mean()))
```

**Output:**
```text
WindGustDir 0.06511419378659213
WindDir9am 0.07013379749283542
WindDir3pm 0.026443026179299188
RainToday 0.01001283471350458
```

```python
# impute missing categorical variables with most frequent value

for df2 in [X_train, X_test]:
    df2['WindGustDir'].fillna(X_train['WindGustDir'].mode()[0], inplace=True)
    df2['WindDir9am'].fillna(X_train['WindDir9am'].mode()[0], inplace=True)
    df2['WindDir3pm'].fillna(X_train['WindDir3pm'].mode()[0], inplace=True)
    df2['RainToday'].fillna(X_train['RainToday'].mode()[0], inplace=True)
```

```python
# check missing values in categorical variables in X_train

X_train[categorical].isnull().sum()
```

**Output:**
```text
Location       0
WindGustDir    0
WindDir9am     0
WindDir3pm     0
RainToday      0
dtype: int64
```

```python
# check missing values in categorical variables in X_test

X_test[categorical].isnull().sum()
```

**Output:**
```text
Location       0
WindGustDir    0
WindDir9am     0
WindDir3pm     0
RainToday      0
dtype: int64
```

As a final check, I will check for missing values in X_train and X_test.

```python
# check missing values in X_train

X_train.isnull().sum()
```

**Output:**
```text
Location         0
MinTemp          0
MaxTemp          0
Rainfall         0
Evaporation      0
Sunshine         0
WindGustDir      0
WindGustSpeed    0
WindDir9am       0
WindDir3pm       0
WindSpeed9am     0
WindSpeed3pm     0
Humidity9am      0
Humidity3pm      0
Pressure9am      0
Pressure3pm      0
Cloud9am         0
Cloud3pm         0
Temp9am          0
Temp3pm          0
RainToday        0
Year             0
Month            0
Day              0
dtype: int64
```

```python
# check missing values in X_test

X_test.isnull().sum()
```

**Output:**
```text
Location         0
MinTemp          0
MaxTemp          0
Rainfall         0
Evaporation      0
Sunshine         0
WindGustDir      0
WindGustSpeed    0
WindDir9am       0
WindDir3pm       0
WindSpeed9am     0
WindSpeed3pm     0
Humidity9am      0
Humidity3pm      0
Pressure9am      0
Pressure3pm      0
Cloud9am         0
Cloud3pm         0
Temp9am          0
Temp3pm          0
RainToday        0
Year             0
Month            0
Day              0
dtype: int64
```

We can see that there are no missing values in X_train and X_test.

### Engineering outliers in numerical variables


We have seen that the `Rainfall`, `Evaporation`, `WindSpeed9am` and `WindSpeed3pm` columns contain outliers. I will use top-coding approach to cap maximum values and remove outliers from the above variables.

```python
def max_value(df3, variable, top):
    return np.where(df3[variable]>top, top, df3[variable])

for df3 in [X_train, X_test]:
    df3['Rainfall'] = max_value(df3, 'Rainfall', 3.2)
    df3['Evaporation'] = max_value(df3, 'Evaporation', 21.8)
    df3['WindSpeed9am'] = max_value(df3, 'WindSpeed9am', 55)
    df3['WindSpeed3pm'] = max_value(df3, 'WindSpeed3pm', 57)
```

```python
X_train.Rainfall.max(), X_test.Rainfall.max()
```

**Output:**
```text
(3.2, 3.2)
```

```python
X_train.Evaporation.max(), X_test.Evaporation.max()
```

**Output:**
```text
(21.8, 21.8)
```

```python
X_train.WindSpeed9am.max(), X_test.WindSpeed9am.max()
```

**Output:**
```text
(55.0, 55.0)
```

```python
X_train.WindSpeed3pm.max(), X_test.WindSpeed3pm.max()
```

**Output:**
```text
(57.0, 57.0)
```

```python
X_train[numerical].describe()
```

**Output:**
```text
MinTemp        MaxTemp       Rainfall    Evaporation  \
count  113754.000000  113754.000000  113754.000000  113754.000000   
mean       12.193497      23.237216       0.675080       5.151606   
std         6.388279       7.094149       1.183837       2.823707   
min        -8.200000      -4.800000       0.000000       0.000000   
25%         7.600000      18.000000       0.000000       4.000000   
50%        12.000000      22.600000       0.000000       4.800000   
75%        16.800000      28.200000       0.600000       5.400000   
max        33.900000      48.100000       3.200000      21.800000   

            Sunshine  WindGustSpeed   WindSpeed9am   WindSpeed3pm  \
count  113754.000000  113754.000000  113754.000000  113754.000000   
mean        8.041154      39.884074      13.978155      18.614756   
std         2.769480      13.116959       8.806558       8.685862   
min         0.000000       6.000000       0.000000       0.000000   
25%         8.200000      31.000000       7.00
... [Output truncated for brevity]
```

We can now see that the outliers in `Rainfall`, `Evaporation`, `WindSpeed9am` and `WindSpeed3pm` columns are capped.

### Encode categorical variables

```python
categorical
```

**Output:**
```text
['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday']
```

```python
X_train[categorical].head()
```

**Output:**
```text
Location WindGustDir WindDir9am WindDir3pm RainToday
110803   Witchcliffe           S        SSE          S        No
87289         Cairns         ENE        SSE         SE       Yes
134949  AliceSprings           E         NE          N        No
85553         Cairns         ESE        SSE          E        No
16110      Newcastle           W          N         SE        No
```

```python
# # encode RainToday variable

# # import category_encoders as ce

# encoder = ce.BinaryEncoder(cols=['RainToday'])

# X_train = encoder.fit_transform(X_train)

# X_test = encoder.transform(X_test)
```

```python
# # pd.get_dummies(X_train.RainToday)
# from sklearn.preprocessing import LabelEncoder

# lb_make = LabelEncoder()
# X_train["make_code"] = lb_make.fit_transform(X_train["RainToday"])
# X_train[["RainToday", "make_code"]].head(11)
```

```python
X_train.head()
```

**Output:**
```text
Location  MinTemp  MaxTemp  Rainfall  Evaporation  Sunshine  \
110803   Witchcliffe     13.9     22.6       0.2          4.8       8.5   
87289         Cairns     22.4     29.4       2.0          6.0       6.3   
134949  AliceSprings      9.7     36.2       0.0         11.4      12.3   
85553         Cairns     20.5     30.1       0.0          8.8      11.1   
16110      Newcastle     16.8     29.2       0.0          4.8       8.5   

       WindGustDir  WindGustSpeed WindDir9am WindDir3pm  ...  Pressure9am  \
110803           S           41.0        SSE          S  ...       1013.9   
87289          ENE           33.0        SSE         SE  ...       1016.9   
134949           E           31.0         NE          N  ...       1018.1   
85553          ESE           37.0        SSE          E  ...       1014.1   
16110            W           39.0          N         SE  ...       1017.6   

        Pressure3pm  Cloud9am  Cloud3pm  Temp9am  Temp3pm  RainToday  Year  \
110803       1013.4 
... [Output truncated for brevity]
```

We can see that two additional variables `RainToday_0` and `RainToday_1` are created from `RainToday` variable.

Now, I will create the `X_train` training set.

```python
X_train = pd.concat([X_train[numerical],
                     pd.get_dummies(X_train.RainToday),
                     pd.get_dummies(X_train.Location), 
                     pd.get_dummies(X_train.WindGustDir),
                     pd.get_dummies(X_train.WindDir9am),
                     pd.get_dummies(X_train.WindDir3pm)], axis=1)
X_train = X_train.rename(columns = {'No': 'RainToday_0', 'Yes': 'RainToday_1'}, inplace = False)
```

```python
list(X_train.columns)
```

**Output:**
```text
['MinTemp',
 'MaxTemp',
 'Rainfall',
 'Evaporation',
 'Sunshine',
 'WindGustSpeed',
 'WindSpeed9am',
 'WindSpeed3pm',
 'Humidity9am',
 'Humidity3pm',
 'Pressure9am',
 'Pressure3pm',
 'Cloud9am',
 'Cloud3pm',
 'Temp9am',
 'Temp3pm',
 'Year',
 'Month',
 'Day',
 'RainToday_0',
 'RainToday_1',
 'Adelaide',
 'Albany',
 'Albury',
 'AliceSprings',
 'BadgerysCreek',
 'Ballarat',
 'Bendigo',
 'Brisbane',
 'Cairns',
 'Canberra',
 'Cobar',
 'CoffsHarbour',
 'Dartmoor',
 'Darwin',
 'GoldCoast',
 'Hobart',
 'Katherine',
 'Launceston',
 'Melbourne',
 'MelbourneAirport',
 'Mildura',
 'Moree',
 'MountGambier',
 'MountGinini',
 'Newcastle',
 'Nhil',
 'NorahHead',
 'NorfolkIsland',
 'Nuriootpa',
 'PearceRAAF',
 'Penrith',
 'Perth',
 'PerthAirport',
 'Portland',
 'Richmond',
 'Sale',
 'SalmonGums',
 'Sydney',
 'SydneyAirport',
 'Townsville',
 'Tuggeranong',
 'Uluru',
 'WaggaWagga',
 'Walpole',
 'Watsonia',
 'Williamtown',
 'Witchcliffe',
 'Wollongong',
 'Woomera',
 'E',
 'ENE',
 'ESE',
 'N',
 'NE',
 'NNE
... [Output truncated for brevity]
```

Similarly, I will create the `X_test` testing set.

```python
X_test = pd.concat([X_test[numerical],
                    pd.get_dummies(X_test.RainToday),
                     pd.get_dummies(X_test.Location), 
                     pd.get_dummies(X_test.WindGustDir),
                     pd.get_dummies(X_test.WindDir9am),
                     pd.get_dummies(X_test.WindDir3pm)], axis=1)
X_test = X_test.rename(columns = {'No': 'RainToday_0', 'Yes': 'RainToday_1'}, inplace = False)
```

```python
X_test.head()
```

**Output:**
```text
MinTemp  MaxTemp  Rainfall  Evaporation  Sunshine  WindGustSpeed  \
86232      17.4     29.0       0.0          3.6      11.1           33.0   
57576       6.8     14.4       0.8          0.8       8.5           46.0   
124071     10.1     15.4       3.2          4.8       8.5           31.0   
117955     14.4     33.4       0.0          8.0      11.6           41.0   
133468      6.8     14.3       3.2          0.2       7.3           28.0   

        WindSpeed9am  WindSpeed3pm  Humidity9am  Humidity3pm  ...  NNW  NW  S  \
86232           11.0          19.0         63.0         61.0  ...    0   0  0   
57576           17.0          22.0         80.0         55.0  ...    0   0  1   
124071          13.0           9.0         70.0         61.0  ...    0   0  0   
117955           9.0          17.0         40.0         23.0  ...    0   0  0   
133468          15.0          13.0         92.0         47.0  ...    0   0  0   

        SE  SSE  SSW  SW  W  WNW  WSW  
86232    0    0    0   0
... [Output truncated for brevity]
```

We now have training and testing set ready for model building. Before that, we should map all the feature variables onto the same scale. It is called `feature scaling`. I will do it as follows.

# **11. Feature Scaling** <a class="anchor" id="11"></a>


[Table of Contents](#0.1)

```python
X_train.describe()
```

**Output:**
```text
MinTemp        MaxTemp       Rainfall    Evaporation  \
count  113754.000000  113754.000000  113754.000000  113754.000000   
mean       12.193497      23.237216       0.675080       5.151606   
std         6.388279       7.094149       1.183837       2.823707   
min        -8.200000      -4.800000       0.000000       0.000000   
25%         7.600000      18.000000       0.000000       4.000000   
50%        12.000000      22.600000       0.000000       4.800000   
75%        16.800000      28.200000       0.600000       5.400000   
max        33.900000      48.100000       3.200000      21.800000   

            Sunshine  WindGustSpeed   WindSpeed9am   WindSpeed3pm  \
count  113754.000000  113754.000000  113754.000000  113754.000000   
mean        8.041154      39.884074      13.978155      18.614756   
std         2.769480      13.116959       8.806558       8.685862   
min         0.000000       6.000000       0.000000       0.000000   
25%         8.200000      31.000000       7.00
... [Output truncated for brevity]
```

```python
cols = X_train.columns
```

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)
```

```python
X_train = pd.DataFrame(X_train, columns=[cols])
```

```python
X_test = pd.DataFrame(X_test, columns=[cols])
```

```python
X_train.describe()
```

**Output:**
```text
MinTemp        MaxTemp       Rainfall    Evaporation  \
count  113754.000000  113754.000000  113754.000000  113754.000000   
mean        0.484406       0.530004       0.210962       0.236312   
std         0.151741       0.134105       0.369949       0.129528   
min         0.000000       0.000000       0.000000       0.000000   
25%         0.375297       0.431002       0.000000       0.183486   
50%         0.479810       0.517958       0.000000       0.220183   
75%         0.593824       0.623819       0.187500       0.247706   
max         1.000000       1.000000       1.000000       1.000000   

            Sunshine  WindGustSpeed   WindSpeed9am   WindSpeed3pm  \
count  113754.000000  113754.000000  113754.000000  113754.000000   
mean        0.554562       0.262667       0.254148       0.326575   
std         0.190999       0.101682       0.160119       0.152384   
min         0.000000       0.000000       0.000000       0.000000   
25%         0.565517       0.193798       0.12
... [Output truncated for brevity]
```

We now have `X_train` dataset ready to be fed into the Logistic Regression classifier. I will do it as follows.

# **12. Model training** <a class="anchor" id="12"></a>


[Table of Contents](#0.1)

```python
# train a logistic regression model on the training set
from sklearn.linear_model import LogisticRegression


# instantiate the model
logreg = LogisticRegression(solver='liblinear', random_state=0)


# fit the model
logreg.fit(X_train, y_train)
```

**Output:**
```text
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                   intercept_scaling=1, l1_ratio=None, max_iter=100,
                   multi_class='warn', n_jobs=None, penalty='l2',
                   random_state=0, solver='liblinear', tol=0.0001, verbose=0,
                   warm_start=False)
```

# **13. Predict results** <a class="anchor" id="13"></a>


[Table of Contents](#0.1)

```python
y_pred_test = logreg.predict(X_test)

y_pred_test
```

**Output:**
```text
array(['No', 'No', 'No', ..., 'No', 'No', 'Yes'], dtype=object)
```

### predict_proba method


**predict_proba** method gives the probabilities for the target variable(0 and 1) in this case, in array form.

`0 is for probability of no rain` and `1 is for probability of rain.`

```python
# probability of getting output as 0 - no rain

logreg.predict_proba(X_test)[:,0]
```

**Output:**
```text
array([0.91383035, 0.83548538, 0.82033027, ..., 0.97675116, 0.79850517,
       0.30741737])
```

```python
# probability of getting output as 1 - rain

logreg.predict_proba(X_test)[:,1]
```

**Output:**
```text
array([0.08616965, 0.16451462, 0.17966973, ..., 0.02324884, 0.20149483,
       0.69258263])
```

# **14. Check accuracy score** <a class="anchor" id="14"></a>


[Table of Contents](#0.1)

```python
from sklearn.metrics import accuracy_score

print('Model accuracy score: {0:0.4f}'. format(accuracy_score(y_test, y_pred_test)))
```

**Output:**
```text
Model accuracy score: 0.8501
```

Here, **y_test** are the true class labels and **y_pred_test** are the predicted class labels in the test-set.

### Compare the train-set and test-set accuracy


Now, I will compare the train-set and test-set accuracy to check for overfitting.

```python
y_pred_train = logreg.predict(X_train)

y_pred_train
```

**Output:**
```text
array(['No', 'No', 'No', ..., 'No', 'No', 'No'], dtype=object)
```

```python
print('Training-set accuracy score: {0:0.4f}'. format(accuracy_score(y_train, y_pred_train)))
```

**Output:**
```text
Training-set accuracy score: 0.8477
```

### Check for overfitting and underfitting

```python
# print the scores on training and test set

print('Training set score: {:.4f}'.format(logreg.score(X_train, y_train)))

print('Test set score: {:.4f}'.format(logreg.score(X_test, y_test)))
```

**Output:**
```text
Training set score: 0.8477
Test set score: 0.8501
```

The training-set accuracy score is 0.8476 while the test-set accuracy to be 0.8501. These two values are quite comparable. So, there is no question of overfitting.

In Logistic Regression, we use default value of C = 1. It provides good performance with approximately 85% accuracy on both the training and the test set. But the model performance on both the training and test set are very comparable. It is likely the case of underfitting. 

I will increase C and fit a more flexible model.

```python
# fit the Logsitic Regression model with C=100

# instantiate the model
logreg100 = LogisticRegression(C=100, solver='liblinear', random_state=0)


# fit the model
logreg100.fit(X_train, y_train)
```

**Output:**
```text
LogisticRegression(C=100, class_weight=None, dual=False, fit_intercept=True,
                   intercept_scaling=1, l1_ratio=None, max_iter=100,
                   multi_class='warn', n_jobs=None, penalty='l2',
                   random_state=0, solver='liblinear', tol=0.0001, verbose=0,
                   warm_start=False)
```

```python
# print the scores on training and test set

print('Training set score: {:.4f}'.format(logreg100.score(X_train, y_train)))

print('Test set score: {:.4f}'.format(logreg100.score(X_test, y_test)))
```

**Output:**
```text
Training set score: 0.8478
Test set score: 0.8506
```

We can see that, C=100 results in higher test set accuracy and also a slightly increased training set accuracy. So, we can conclude that a more complex model should perform better.

Now, I will investigate, what happens if we use more regularized model than the default value of C=1, by setting C=0.01.

```python
# fit the Logsitic Regression model with C=001

# instantiate the model
logreg001 = LogisticRegression(C=0.01, solver='liblinear', random_state=0)


# fit the model
logreg001.fit(X_train, y_train)
```

**Output:**
```text
LogisticRegression(C=0.01, class_weight=None, dual=False, fit_intercept=True,
                   intercept_scaling=1, l1_ratio=None, max_iter=100,
                   multi_class='warn', n_jobs=None, penalty='l2',
                   random_state=0, solver='liblinear', tol=0.0001, verbose=0,
                   warm_start=False)
```

```python
# print the scores on training and test set

print('Training set score: {:.4f}'.format(logreg001.score(X_train, y_train)))

print('Test set score: {:.4f}'.format(logreg001.score(X_test, y_test)))
```

**Output:**
```text
Training set score: 0.8409
Test set score: 0.8448
```

So, if we use more regularized model by setting C=0.01, then both the training and test set accuracy decrease relatiev to the default parameters.

### Compare model accuracy with null accuracy


So, the model accuracy is 0.8501. But, we cannot say that our model is very good based on the above accuracy. We must compare it with the **null accuracy**. Null accuracy is the accuracy that could be achieved by always predicting the most frequent class.

So, we should first check the class distribution in the test set.

```python
# check class distribution in test set

y_test.value_counts()
```

**Output:**
```text
No     22067
Yes     6372
Name: RainTomorrow, dtype: int64
```

We can see that the occurences of most frequent class is 22067. So, we can calculate null accuracy by dividing 22067 by total number of occurences.

```python
# check null accuracy score

null_accuracy = (22067/(22067+6372))

print('Null accuracy score: {0:0.4f}'. format(null_accuracy))
```

**Output:**
```text
Null accuracy score: 0.7759
```

We can see that our model accuracy score is 0.8501 but null accuracy score is 0.7759. So, we can conclude that our Logistic Regression model is doing a good job in predicting the class labels.

Now, based on the above analysis we can conclude that our classification model accuracy is very good. Our model is doing a very good job in terms of predicting the class labels.


But, it does not give the underlying distribution of values. Also, it does not tell anything about the type of errors our classifer is making. 


We have another tool called `Confusion matrix` that comes to our rescue.

# **15. Confusion matrix** <a class="anchor" id="15"></a>


[Table of Contents](#0.1)


A confusion matrix is a tool for summarizing the performance of a classification algorithm. A confusion matrix will give us a clear picture of classification model performance and the types of errors produced by the model. It gives us a summary of correct and incorrect predictions broken down by each category. The summary is represented in a tabular form.


Four types of outcomes are possible while evaluating a classification model performance. These four outcomes are described below:-


**True Positives (TP)** – True Positives occur when we predict an observation belongs to a certain class and the observation actually belongs to that class.


**True Negatives (TN)** – True Negatives occur when we predict an observation does not belong to a certain class and the observation actually does not belong to that class.


**False Positives (FP)** – False Positives occur when we predict an observation belongs to a    certain class but the observation actually does not belong to that class. This type of error is called **Type I error.** Eg. You could not have Corona and still be tested positive



**False Negatives (FN)** – False Negatives occur when we predict an observation does not belong to a certain class but the observation actually belongs to that class. This is a very serious error and it is called **Type II error.**



These four outcomes are summarized in a confusion matrix given below.

```python
# Print the Confusion Matrix and slice it into four pieces

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred_test)

print('Confusion matrix\n\n', cm)

print('\nTrue Positives(TP) = ', cm[0,0])

print('\nTrue Negatives(TN) = ', cm[1,1])

print('\nFalse Positives(FP) = ', cm[0,1])

print('\nFalse Negatives(FN) = ', cm[1,0])
```

**Output:**
```text
Confusion matrix

 [[20892  1175]
 [ 3088  3284]]

True Positives(TP) =  20892

True Negatives(TN) =  3284

False Positives(FP) =  1175

False Negatives(FN) =  3088
```

The confusion matrix shows `20892 + 3285 = 24177 correct predictions` and `3087 + 1175 = 4262 incorrect predictions`.


In this case, we have


- `True Positives` (Actual Positive:1 and Predict Positive:1) - 20892


- `True Negatives` (Actual Negative:0 and Predict Negative:0) - 3285


- `False Positives` (Actual Negative:0 but Predict Positive:1) - 1175 `(Type I error)`


- `False Negatives` (Actual Positive:1 but Predict Negative:0) - 3087 `(Type II error)`

```python
# visualize confusion matrix with seaborn heatmap

cm_matrix = pd.DataFrame(data=cm, columns=['Actual Positive:1', 'Actual Negative:0'], 
                                 index=['Predict Positive:1', 'Predict Negative:0'])

sns.heatmap(cm_matrix, annot=True, fmt='d', cmap='YlGnBu')
```

# **16. Classification metrices** <a class="anchor" id="16"></a>


[Table of Contents](#0.1)

## Classification Report


**Classification report** is another way to evaluate the classification model performance. It displays the  **precision**, **recall**, **f1** and **support** scores for the model. I have described these terms in later.

We can print a classification report as follows:-

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred_test))
```

**Output:**
```text
precision    recall  f1-score   support

          No       0.87      0.95      0.91     22067
         Yes       0.74      0.52      0.61      6372

    accuracy                           0.85     28439
   macro avg       0.80      0.73      0.76     28439
weighted avg       0.84      0.85      0.84     28439
```

## Classification accuracy

```python
TP = cm[0,0]
TN = cm[1,1]
FP = cm[0,1]
FN = cm[1,0]
```

```python
# print classification accuracy

classification_accuracy = (TP + TN) / float(TP + TN + FP + FN)

print('Classification accuracy : {0:0.4f}'.format(classification_accuracy))
```

**Output:**
```text
Classification accuracy : 0.8501
```

## Classification error

```python
# print classification error

classification_error = (FP + FN) / float(TP + TN + FP + FN)

print('Classification error : {0:0.4f}'.format(classification_error))
```

**Output:**
```text
Classification error : 0.1499
```

## Precision


**Precision** can be defined as the percentage of correctly predicted positive outcomes out of all the predicted positive outcomes. It can be given as the ratio of true positives (TP) to the sum of true and false positives (TP + FP). 


So, **Precision** identifies the proportion of correctly predicted positive outcome. It is more concerned with the positive class than the negative class.



Mathematically, precision can be defined as the ratio of `TP to (TP + FP).`

```python
# print precision score

precision = TP / float(TP + FP)


print('Precision : {0:0.4f}'.format(precision))
```

**Output:**
```text
Precision : 0.9468
```

## Recall


Recall can be defined as the percentage of correctly predicted positive outcomes out of all the actual positive outcomes.
It can be given as the ratio of true positives (TP) to the sum of true positives and false negatives (TP + FN). **Recall** is also called **Sensitivity**.


**Recall** identifies the proportion of correctly predicted actual positives.


Mathematically, recall can be given as the ratio of `TP to (TP + FN).`

```python
recall = TP / float(TP + FN)

print('Recall or Sensitivity : {0:0.4f}'.format(recall))
```

**Output:**
```text
Recall or Sensitivity : 0.8712
```

## True Positive Rate


**True Positive Rate** is synonymous with **Recall**.

```python
true_positive_rate = TP / float(TP + FN)


print('True Positive Rate : {0:0.4f}'.format(true_positive_rate))
```

**Output:**
```text
True Positive Rate : 0.8712
```

## False Positive Rate

```python
false_positive_rate = FP / float(FP + TN)


print('False Positive Rate : {0:0.4f}'.format(false_positive_rate))
```

**Output:**
```text
False Positive Rate : 0.2635
```

## Specificity

```python
specificity = TN / (TN + FP)

print('Specificity : {0:0.4f}'.format(specificity))
```

**Output:**
```text
Specificity : 0.7365
```

## f1-score


**f1-score** is the weighted harmonic mean of precision and recall. The best possible **f1-score** would be 1.0 and the worst 
would be 0.0.  **f1-score** is the harmonic mean of precision and recall. So, **f1-score** is always lower than accuracy measures as they embed precision and recall into their computation. The weighted average of `f1-score` should be used to 
compare classifier models, not global accuracy.

## Support


**Support** is the actual number of occurrences of the class in our dataset.

# **17. Adjusting the threshold level** <a class="anchor" id="17"></a>


[Table of Contents](#0.1)

```python
# print the first 10 predicted probabilities of two classes- 0 and 1

y_pred_prob = logreg.predict_proba(X_test)[0:10]

y_pred_prob
```

**Output:**
```text
array([[0.91383035, 0.08616965],
       [0.83548538, 0.16451462],
       [0.82033027, 0.17966973],
       [0.99025943, 0.00974057],
       [0.95727308, 0.04272692],
       [0.97993822, 0.02006178],
       [0.17832113, 0.82167887],
       [0.23464123, 0.76535877],
       [0.90047563, 0.09952437],
       [0.85491359, 0.14508641]])
```

### Observations


- In each row, the numbers sum to 1.


- There are 2 columns which correspond to 2 classes - 0 and 1.

    - Class 0 - predicted probability that there is no rain tomorrow.    
    
    - Class 1 - predicted probability that there is rain tomorrow.
        
    
- Importance of predicted probabilities

    - We can rank the observations by probability of rain or no rain.


- predict_proba process

    - Predicts the probabilities    
    
    - Choose the class with the highest probability    
    
    
- Classification threshold level

    - There is a classification threshold level of 0.5.    
    
    - Class 1 - probability of rain is predicted if probability > 0.5.    
    
    - Class 0 - probability of no rain is predicted if probability < 0.5.

```python
# store the probabilities in dataframe

y_pred_prob_df = pd.DataFrame(data=y_pred_prob, columns=['Prob of - No rain tomorrow (0)', 'Prob of - Rain tomorrow (1)'])

y_pred_prob_df
```

**Output:**
```text
Prob of - No rain tomorrow (0)  Prob of - Rain tomorrow (1)
0                        0.913830                     0.086170
1                        0.835485                     0.164515
2                        0.820330                     0.179670
3                        0.990259                     0.009741
4                        0.957273                     0.042727
5                        0.979938                     0.020062
6                        0.178321                     0.821679
7                        0.234641                     0.765359
8                        0.900476                     0.099524
9                        0.854914                     0.145086
```

```python
# print the first 10 predicted probabilities for class 1 - Probability of rain

logreg.predict_proba(X_test)[0:10, 1]
```

**Output:**
```text
array([0.08616965, 0.16451462, 0.17966973, 0.00974057, 0.04272692,
       0.02006178, 0.82167887, 0.76535877, 0.09952437, 0.14508641])
```

```python
# store the predicted probabilities for class 1 - Probability of rain

y_pred1 = logreg.predict_proba(X_test)[:, 1]
```

```python
# plot histogram of predicted probabilities


# adjust the font size 
plt.rcParams['font.size'] = 12


# plot histogram with 10 bins
plt.hist(y_pred1, bins = 10)


# set the title of predicted probabilities
plt.title('Histogram of predicted probabilities of rain')


# set the x-axis limit
plt.xlim(0,1)


# set the title
plt.xlabel('Predicted probabilities of rain')
plt.ylabel('Frequency')
```

**Output:**
```text
Text(0, 0.5, 'Frequency')
```

### Observations


- We can see that the above histogram is highly positive skewed.


- The first column tell us that there are approximately 15000 observations with probability between 0.0 and 0.1.


- There are small number of observations with probability > 0.5.


- So, these small number of observations predict that there will be rain tomorrow.


- Majority of observations predict that there will be no rain tomorrow.

### Lower the threshold

```python
from sklearn.preprocessing import binarize

for i in range(1,5):
    
    cm1=0
    
    y_pred1 = logreg.predict_proba(X_test)[:,1]
    
    y_pred1 = y_pred1.reshape(-1,1)
    
    y_pred2 = binarize(y_pred1, i/10)
    
    y_pred2 = np.where(y_pred2 == 1, 'Yes', 'No')
    
    cm1 = confusion_matrix(y_test, y_pred2)
        
    print ('With',i/10,'threshold the Confusion Matrix is ','\n\n',cm1,'\n\n',
           
            'with',cm1[0,0]+cm1[1,1],'correct predictions, ', '\n\n', 
           
            cm1[0,1],'Type I errors( False Positives), ','\n\n',
           
            cm1[1,0],'Type II errors( False Negatives), ','\n\n',
           
           'Accuracy score: ', (accuracy_score(y_test, y_pred2)), '\n\n',
           
           'Sensitivity: ',cm1[1,1]/(float(cm1[1,1]+cm1[1,0])), '\n\n',
           
           'Specificity: ',cm1[0,0]/(float(cm1[0,0]+cm1[0,1])),'\n\n',
          
            '====================================================', '\n\n')
```

**Output:**
```text
With 0.1 threshold the Confusion Matrix is  

 [[12726  9341]
 [  547  5825]] 

 with 18551 correct predictions,  

 9341 Type I errors( False Positives),  

 547 Type II errors( False Negatives),  

 Accuracy score:  0.6523084496641935 

 Sensitivity:  0.9141556811048337 

 Specificity:  0.5766982371867494 

 ==================================================== 


With 0.2 threshold the Confusion Matrix is  

 [[17067  5000]
 [ 1233  5139]] 

 with 22206 correct predictions,  

 5000 Type I errors( False Positives),  

 1233 Type II errors( False Negatives),  

 Accuracy score:  0.7808291430781673 

 Sensitivity:  0.806497175141243 

 Specificity:  0.7734173199800607 

 ==================================================== 


With 0.3 threshold the Confusion Matrix is  

 [[19081  2986]
 [ 1873  4499]] 

 with 23580 correct predictions,  

 2986 Type I errors( False Positives),  

 1873 Type II errors( False Negatives),  

 Accuracy score:  0.8291430781673055 

 Sensitivity:  0.7060577
... [Output truncated for brevity]
```

### Comments


- In binary problems, the threshold of 0.5 is used by default to convert predicted probabilities into class predictions.


- Threshold can be adjusted to increase sensitivity or specificity. 


- Sensitivity and specificity have an inverse relationship. Increasing one would always decrease the other and vice versa.


- We can see that increasing the threshold level results in increased accuracy.


- Adjusting the threshold level should be one of the last step you do in the model-building process.

# **18. ROC - AUC** <a class="anchor" id="18"></a>


[Table of Contents](#0.1)



## ROC Curve


Another tool to measure the classification model performance visually is **ROC Curve**. ROC Curve stands for **Receiver Operating Characteristic Curve**. An **ROC Curve** is a plot which shows the performance of a classification model at various 
classification threshold levels. 



The **ROC Curve** plots the **True Positive Rate (TPR)** against the **False Positive Rate (FPR)** at various threshold levels.



**True Positive Rate (TPR)** is also called **Recall**. It is defined as the ratio of `TP to (TP + FN).`



**False Positive Rate (FPR)** is defined as the ratio of `FP to (FP + TN).`




In the ROC Curve, we will focus on the TPR (True Positive Rate) and FPR (False Positive Rate) of a single point. This will give us the general performance of the ROC curve which consists of the TPR and FPR at various threshold levels. So, an ROC Curve plots TPR vs FPR at different classification threshold levels. If we lower the threshold levels, it may result in more items being classified as positve. It will increase both True Positives (TP) and False Positives (FP).

```python
# plot ROC Curve

from sklearn.metrics import roc_curve

fpr, tpr, thresholds = roc_curve(y_test, y_pred1, pos_label = 'Yes')

plt.figure(figsize=(6,4))

plt.plot(fpr, tpr, linewidth=2)

plt.plot([0,1], [0,1], 'k--' )

plt.rcParams['font.size'] = 12

plt.title('ROC curve for RainTomorrow classifier')

plt.xlabel('False Positive Rate (1 - Specificity)')

plt.ylabel('True Positive Rate (Sensitivity)')

plt.show()
```

ROC curve help us to choose a threshold level that balances sensitivity and specificity for a particular context.

## ROC-AUC


**ROC AUC** stands for **Receiver Operating Characteristic - Area Under Curve**. It is a technique to compare classifier performance. In this technique, we measure the `area under the curve (AUC)`. A perfect classifier will have a ROC AUC equal to 1, whereas a purely random classifier will have a ROC AUC equal to 0.5. 


So, **ROC AUC** is the percentage of the ROC plot that is underneath the curve.

```python
# compute ROC AUC

from sklearn.metrics import roc_auc_score

ROC_AUC = roc_auc_score(y_test, y_pred1)

print('ROC AUC : {:.4f}'.format(ROC_AUC))
```

**Output:**
```text
ROC AUC : 0.8729
```

### Comments


- ROC AUC is a single number summary of classifier performance. The higher the value, the better the classifier.

- ROC AUC of our model approaches towards 1. So, we can conclude that our classifier does a good job in predicting whether it will rain tomorrow or not.

```python
# calculate cross-validated ROC AUC 

from sklearn.model_selection import cross_val_score

Cross_validated_ROC_AUC = cross_val_score(logreg, X_train, y_train, cv=5, scoring='roc_auc').mean()

print('Cross validated ROC AUC : {:.4f}'.format(Cross_validated_ROC_AUC))
```

**Output:**
```text
Cross validated ROC AUC : 0.8695
```

# **19. k-Fold Cross Validation** <a class="anchor" id="19"></a>


[Table of Contents](#0.1)

```python
# Applying 5-Fold Cross Validation

from sklearn.model_selection import cross_val_score

scores = cross_val_score(logreg, X_train, y_train, cv = 5, scoring='accuracy')

print('Cross-validation scores:{}'.format(scores))
```

**Output:**
```text
Cross-validation scores:[0.84690783 0.84624852 0.84633642 0.84963298 0.84773626]
```

We can summarize the cross-validation accuracy by calculating its mean.

```python
# compute Average cross-validation score

print('Average cross-validation score: {:.4f}'.format(scores.mean()))
```

**Output:**
```text
Average cross-validation score: 0.8474
```

Our, original model score is found to be 0.8476. The average cross-validation score is 0.8474. So, we can conclude that cross-validation does not result in performance improvement.

# **20. Hyperparameter Optimization using GridSearch CV** <a class="anchor" id="20"></a>


[Table of Contents](#0.1)

```python
from sklearn.model_selection import GridSearchCV


parameters = [{'penalty':['l1','l2']}, 
              {'C':[1, 10, 100, 1000]}]



grid_search = GridSearchCV(estimator = logreg,  
                           param_grid = parameters,
                           scoring = 'accuracy',
                           cv = 5,
                           verbose=0)


grid_search.fit(X_train, y_train)
```

**Output:**
```text
GridSearchCV(cv=5, error_score='raise-deprecating',
             estimator=LogisticRegression(C=1.0, class_weight=None, dual=False,
                                          fit_intercept=True,
                                          intercept_scaling=1, l1_ratio=None,
                                          max_iter=100, multi_class='warn',
                                          n_jobs=None, penalty='l2',
                                          random_state=0, solver='liblinear',
                                          tol=0.0001, verbose=0,
                                          warm_start=False),
             iid='warn', n_jobs=None,
             param_grid=[{'penalty': ['l1', 'l2']}, {'C': [1, 10, 100, 1000]}],
             pre_dispatch='2*n_jobs', refit=True, return_train_score=False,
             scoring='accuracy', verbose=0)
```

```python
# examine the best model

# best score achieved during the GridSearchCV
print('GridSearch CV best score : {:.4f}\n\n'.format(grid_search.best_score_))

# print parameters that give the best results
print('Parameters that give the best results :','\n\n', (grid_search.best_params_))

# print estimator that was chosen by the GridSearch
print('\n\nEstimator that was chosen by the search :','\n\n', (grid_search.best_estimator_))
```

**Output:**
```text
GridSearch CV best score : 0.8474


Parameters that give the best results : 

 {'penalty': 'l1'}


Estimator that was chosen by the search : 

 LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                   intercept_scaling=1, l1_ratio=None, max_iter=100,
                   multi_class='warn', n_jobs=None, penalty='l1',
                   random_state=0, solver='liblinear', tol=0.0001, verbose=0,
                   warm_start=False)
```

```python
# calculate GridSearch CV score on test set

print('GridSearch CV score on test set: {0:0.4f}'.format(grid_search.score(X_test, y_test)))
```

**Output:**
```text
GridSearch CV score on test set: 0.8507
```

### Comments


- Our original model test accuracy is 0.8501 while GridSearch CV accuracy is 0.8507.


- We can see that GridSearch CV improve the performance for this particular model.

# **21. Results and conclusion** <a class="anchor" id="21"></a>


[Table of Contents](#0.1)

1.	The logistic regression model accuracy score is 0.8501. So, the model does a very good job in predicting whether or not it will rain tomorrow.

2.	Small number of observations predict that there will be rain tomorrow. Majority of observations predict that there will be no rain tomorrow.

3.	The model shows no signs of overfitting.

4.	Increasing the value of C results in higher test set accuracy and also a slightly increased training set accuracy. So, we can conclude that a more complex model should perform better.

5.	Increasing the threshold level results in increased accuracy.

6.	ROC AUC of our model approaches towards 1. So, we can conclude that our classifier does a good job in predicting whether it will rain tomorrow or not.

7.	Our original model accuracy score is 0.8501 whereas accuracy score after RFECV is 0.8500. So, we can obtain approximately similar accuracy but with reduced set of features.

8.	In the original model, we have FP = 1175 whereas FP1 = 1174. So, we get approximately same number of false positives. Also, FN = 3087 whereas FN1 = 3091. So, we get slighly higher false negatives.

9.	Our, original model score is found to be 0.8476. The average cross-validation score is 0.8474. So, we can conclude that cross-validation does not result in performance improvement.

10.	Our original model test accuracy is 0.8501 while GridSearch CV accuracy is 0.8507. We can see that GridSearch CV improve the performance for this particular model.

[Go to Top](#0)