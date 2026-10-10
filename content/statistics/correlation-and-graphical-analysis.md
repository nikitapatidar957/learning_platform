# Correlation & Graphical Data Analysis

Mastering exploratory data analysis (EDA): Univariate, Bivariate, and Multivariate analysis, Pearson and Spearman correlation coefficients, covariance, scatter plot matrices, box plots for outlier detection, histograms with KDE density estimation, and real-world worker productivity dataset analysis.

---

## 📉 Correlation & Graphical Analysis Concepts

### Slide 1: Correlation and Graphical Analysis



---

### Slide 2: Correlation

• Correlation is a statistical measure that indicates the extent to which two or more variables fluctuate together. If the change in one variable affects a change in the other variable, the variables are said to be correlated.

• If the two variables deviate in the same direction, correlation is said to be positive. Example - income & expenditure, volume of a commodity & its price.

• If the two variables deviate in the opposite direction, correlation is said to be negative. Example – Demand & price, vaccination & illness from a particular disease.

• Coefficient of Correlation (Karl Pearson) :  Correlation coefficient measures the degree of linear relationship between two variables. It is defined as :

• r(X,Y)  =    =

• Covariance is a measure of the directional relationship between the two variables.

---

### Slide 3: Correlation

• Coefficient of Correlation (Spearman) : It is used to check the Rank correlation i.e. the statistical dependence between the rankings of two variables.

• Where di is the difference between Xi & Yi, n is the number of observations.

• Properties :

• -1 ≤ r(X,Y) ≤ 1 : The value of correlation coefficient lies between -1 to 1.

• If r = + 1, the correlation is perfect and positive and if r = -1, correlation is perfect and negative. r=0 represents no correlation.

• Correlation coefficient is independent of change of origin & scale.

• Two independent variables are uncorrelated, but converse it not true.

---

### Slide 4: Correlation : Representation

• Scatter diagram : Scatter diagram is a simplest way for graphically checking the correlation between two variables.

• Interpretation:  The value of correlation coefficient can be interpreted as:

• If  r is close to zero then correlation is said to be very low.

• If  r is close to -0.5 or 0.5 then correlation is said to be moderate.

• If  r is greater than 0.75 or less than -0.75 then correlation is said to be high.

---

### Slide 5: Correlation : Things to Remember

• Correlation is very simplest way to understand the relationship between two variables, but it has some drawbacks also. We have to be careful about following things while using correlation.

• Correlation does not imply causation : Correlation does not prove that one variable causes the other.

• A study founds that there is high negative correlation between Number of astronauts dying in spacecraft & Percentage of people wearing seatbelts in automobiles.

• Result : Use your seatbelt and save an astronaut’s life.

• It is called the spurious or nonsense correlation.

• Correlation only measures the linear relationship : If two variables are non linearly related to each other then Correlation may not measure the relationship between them.

---

### Slide 6: Correlation Plot

• corr() function in Python : To find the correlation between two variables in Python we can use the function corr().

• DataFrame.corr(method='pearson', min_periods=1)

• We can specify the method of correlation in cor() function. i.e. “pearson"," spearman” etc.

• cor() can be applied on the data frame also with multiple variables. It will give the correlation between each pair of variables.

---

### Slide 7: Data Visualization



---

### Slide 8: What is Data Visualization?

• Data visualization is defined as a graphical representation that contains the information and the data.

• By using visual elements like charts, graphs, and maps, data visualization techniques provide an accessible way to see and understand trends, outliers, and patterns in data.

• It is used in many areas such as:

• To model complex events.

• It is a powerful technique to explore the data with presentable and interpretable results.

• Visualize phenomenon's that cannot be observed directly, such as weather patterns, medical conditions, or mathematical relationships.

---

### Slide 9: Different Types of Analysis for Data Visualization

• Univariate Analysis: In the univariate analysis, we will be using a single feature to analyze almost all its properties.

• Distribution Plot is one of the best univariate plots to know about the distribution of data.

• This plot gives us a combination of both probability density functions(pdf) and histogram in a single plot.

• Box and Whisker plot can be used to obtain more statistical details about the data.

• The straight lines at the maximum and minimum are also called whiskers.

• Points that lie outside the whiskers will be considered as an outlier.

• The box plot also gives us a description of the 25th, 50th,75th quartiles.

• sns.FacetGrid(hb,hue='SurvStat',size=5).map(sns.distplot,'age').add_legend()

• sns.boxplot(x='SurvStat',y='axil_nodes',data=hb)

---

### Slide 10: Different Types of Analysis for Data Visualization

• Bivariate Analysis: When we compare the data between exactly 2 features then it is known as bivariate analysis.

• The line plots are nothing but the values on a series of data points will be connected with straight lines.

• The plot may seem very simple but it has more applications not only in machine learning but in many other areas.

• Bar Plot is one of the widely used plots for categorical data.

• Though it may seem simple it is powerful in analyzing data like sales figures every week, revenue from a product, Number of visitors to a site on each day of a week, etc.

• Scatter Plot describes us as a representation, where each point in the entire dataset is present with respect to any 2 to 3 features (Columns) and use to find the patterns, clusters, and separability of the data.

• Scatter plots are available in both 2-D as well as in 3-D.

• plt.plot(x,y)

• plt.bar(x,y)

• plt.scatter(x,y)

---

### Slide 11: Summarize



---

### Slide 12: Various Python Libraries used for visualization

• Matplotlib

• Matplotlib is very easy to set up and remember the code.

• Matplotlib supports all the popular charts (lots, histograms, power spectra, bar charts, error charts, scatterplots, etc.) right out of the box. There are also extensions that you can use to create advanced visualizations like 3-Dimensional plots, etc.

• However, the chart doesn’t look good. It will probably do the job for data analysis, but its result for a business meeting is not great.

---

### Slide 13: Various Python Libraries used for visualization

• Seaborn

• When using Seaborn, you will also notice that many of the default settings in the plots work quite well right out of the box, example : It automatically adds x and y-axis labels. The x ticks could look better, but for a basic chart, that's way better than Matplotlib.

• Seaborn is built on top of matplotlib and provides a very simple yet intuitive interface for building visualizations.

• Seaborn supports a plethora of advanced plots like categorical plotting (catplot), distribution plotting using kde (distplot), swarm plot, etc.

---

### Slide 14: Various Python Libraries used for visualization

• Plotly Express

• The first thing that comes to my mind when I think about plotly is interactivity! It is used to create visualizations that need to be highly interactive for the user.

• Plotly supports a gamut of plots like 3-D plots, Map-based visualizations, scientific plots, etc. The list is endless!

---

### Slide 15: Various Python Libraries used for visualization

• Altair

• Altair is a declarative library for data visualization.

• Its principle is that rather than focusing on the code part, one should focus on the visualization part and write as less code as possible and still be able to create beautiful and intuitive plots. That’s right down my alley!

---

### Slide 16: Assignment

• Please download the following datasets :

• 1. Time series data

• https://archive.ics.uci.edu/ml/machine-learning-databases/00597/

• 2. Categorical dataset (combine white wine and red wine datasets hence, making 2 categories)

• https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/

• Plot simple visuals like line chart, bar chart, histogram, scatterplot, correlation plots, pie chart, stacked chart, box plot, dist plot and other relevant plots based on the given data and information.

• Plot complex visuals by combining various simple visuals and add legends, axis and title to it.

• Use customization in plots and make them more presentable.

• Use different data visualization libraries in python like matplotlib, seaborn, plotly,…etc.

• Find 5 insights from each dataset using bivariate and multivariate data analysis graphs also include correlation inferences.

• Submit assignments in a combined Jupyter notebook and rename file as graphical_analysis_name (please replace name with your name)

---

### Slide 17: THANK YOU FOR YOURATTENTATION




---

## 🧪 Hands-on EDA & Graphical Analysis with Python


1. Plot simple visuals like line chart, bar chart, histogram, scatterplot, correlation plots, pie chart, stacked chart, box plot, dist plot and other relevant plots based on the given data and information.

2. Plot complex visuals by combining various simple visuals and add legends, axis and title to it. 
     Use customization in plots and make them more presentable.

3. Use different data visualization libraries in python like matplotlib, seaborn, plotly,…etc.

4. Find 5 insights from each dataset using bivariate and multivariate data analysis graphs also include correlation inferences.

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import plotly
```

```python
warnings.filterwarnings('ignore')
```

```python
garment_df = pd.read_csv('garments_worker_productivity.csv')
```

01. date : Date in MM-DD-YYYY
02. day : Day of the Week
03. quarter : A portion of the month. A month was divided into four quarters
04. department : Associated department with the instance
05. team : Associated team number with the instance
06. no_of_workers : Number of workers in each team
07. no_of_style_change : Number of changes in the style of a particular product
08. targeted_productivity : Targeted productivity set by the Authority for each team for each day.
09. smv : Standard Minute Value, it is the allocated time for a task
10. wip : Work in progress. Includes the number of unfinished items for products
11. over_time : Represents the amount of overtime by each team in minutes
12. incentive : Represents the amount of financial incentive (in BDT) that enables or motivates a particular course of action.
13. idle_time : The amount of time when the production was interrupted due to several reasons
14. idle_men : The number of workers who were idle due to production interruption
15. actual_productivity : The actual % of productivity that was delivered by the workers. It ranges from 0-1.

```python
garment_df.head()
```

**Output:**
```text
date   quarter  department       day  team  targeted_productivity  \
0  1/1/2015  Quarter1      sweing  Thursday     8                   0.80   
1  1/1/2015  Quarter1  finishing   Thursday     1                   0.75   
2  1/1/2015  Quarter1      sweing  Thursday    11                   0.80   
3  1/1/2015  Quarter1      sweing  Thursday    12                   0.80   
4  1/1/2015  Quarter1      sweing  Thursday     6                   0.80   

     smv     wip  over_time  incentive  idle_time  idle_men  \
0  26.16  1108.0       7080         98        0.0         0   
1   3.94     NaN        960          0        0.0         0   
2  11.41   968.0       3660         50        0.0         0   
3  11.41   968.0       3660         50        0.0         0   
4  25.90  1170.0       1920         50        0.0         0   

   no_of_style_change  no_of_workers  actual_productivity  
0                   0           59.0             0.940725  
1                   0            8.0             0.
... [Output truncated for brevity]
```

We have number of workers in decimal or in fraction which is not possible practically, will make it rounded employee.

```python
garment_df.date = pd.DatetimeIndex(garment_df.date)
```

```python
garment_df.quarter.replace("Quarter5","Quarter1",inplace=True)
```

```python
garment_df.no_of_workers = round(garment_df.no_of_workers)
```

```python
garment_df.info()
```

We have NA or null values in the wip feature we will replace all the null values with 0, perhaps if there is no WIP which means the work is completed or not started.

```python
plt.figure(figsize=(12,8))
sns.heatmap(garment_df.isna(),cbar=False)
plt.title("Null Values in HeatMap",fontsize=20)
plt.xlabel("Features",fontsize = 15)
plt.ylabel("Data Frequency",fontsize = 15)
```

**Output:**
```text
Text(87.0, 0.5, 'Data Frequency')
```

```python
garment_df.wip.fillna(0,inplace=True)
```

Here we have filled the NA values

```python
finishing_df = garment_df[(garment_df.department =='finishing')]
siwing_df = garment_df[(garment_df.department =='sweing')]
```

```python
temp_df =pd.DataFrame(finishing_df.groupby(['team'])['actual_productivity'].mean()).reset_index()

temp_df_2 =pd.DataFrame(siwing_df.groupby(['team'])['actual_productivity'].mean()).reset_index()
```

```python
f, axes = plt.subplots(2, 1,figsize=(18,9),sharex=True)
f.suptitle("Department wise Team Productivity",fontsize=30)
clr = ['green' if (x == temp_df.actual_productivity.max()) else ('red' if (x==temp_df.actual_productivity.min()) else 'grey') for x in temp_df.actual_productivity]
sns.barplot(  x="team", y= "actual_productivity", data=temp_df , ax=axes[0],palette=clr)
axes[0].set_title("Finishing Department",fontsize = 20)


f.show()

clr = ['green' if (x == temp_df_2.actual_productivity.max()) else ('red' if (x==temp_df_2.actual_productivity.min()) else 'grey') for x in temp_df_2.actual_productivity]
sns.barplot(  x="team", y= "actual_productivity", data=temp_df_2 , ax=axes[1],palette=clr)
axes[1].set_title("Siwing Department",fontsize = 20)


for ax in axes.flat:
    ax.set(xlabel='Teams', ylabel='Productivity (in %)')
for ax in axes:
    ax.label_outer()
    


f.tight_layout()
f.show()
```

- Team 3 is highly productive in finishing department where as team 6 has the least productivity in finishing department.
- Team 1 is high productive in Siwing Department where as team 5 is least productive.

```python
temp_df = garment_df[(garment_df.team ==2)&(garment_df.department =='finishing')]
temp_df_2 = garment_df[(garment_df.team ==2)&(garment_df.department =='sweing')]

f = plt.figure(figsize=(18,9))
plt.suptitle("Team 2 Actual Productivity",fontsize=20)
ax = f.add_subplot(211)
ax.plot(temp_df.date,temp_df.actual_productivity,"-g",ls='--')
plt.title("Finishing depart.",fontsize=15)
plt.xticks(temp_df.date,rotation=90)

ax2 = f.add_subplot(212)
ax2.plot(temp_df_2.date,temp_df_2.actual_productivity,"-r",ls='dashdot')
plt.title("Siwing depart.",fontsize=15)

plt.xticks(temp_df_2.date,rotation=90)

plt.tight_layout()
plt.show()
```

1. Firstly the dates are not available in the Finishing and Siwing depart.
2. Team 2 has highest productivity in siwing department from 26 jan 2015 to 12 feb 2015 then it falls.
3. Team 2 has highest productivty in Finishing department is on 15 feb 2015.
4. Team 2 has least productivity in siwing department is on 14-january 2015 and in Finishing department have least in 24 february 2015.

```python
garment_df['diff_productivity'] = garment_df.actual_productivity - garment_df.targeted_productivity
```

```python
plt.figure(figsize=(18,8))
plt.plot(garment_df.date,garment_df['diff_productivity'].cumsum(axis = 0),"-g")
plt.title("Actual - Target Productivity Cumulative trend",fontsize=20)
plt.xlabel("Date",fontsize=15)
plt.xticks(garment_df.date,rotation=90)
plt.show()
```

- Here the trend of productivity is increased from january 24 to feb 15 the it start declining.

```python
plt.figure(figsize=(18,8))
sns.barplot(garment_df.quarter,garment_df['diff_productivity'],color='darkcyan')
plt.title("Quarter wise Productivity Difference",fontsize=20)
plt.xlabel("Quarter",fontsize=15)
plt.ylabel("Productivity Difference",fontsize=15)
plt.show()
```

In the First Quarter we have higher positive change in productivity whereas Quarter 3 and Quarter 4 has least change in productivity

```python
sns.set(style="darkgrid")
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .95)},figsize=(18,9))
sns.boxplot( garment_df.over_time, ax=ax_box,color='darkcyan')
sns.histplot(x =garment_df.over_time,color='darkcyan', ax=ax_hist)
plt.suptitle("Over time Distribution").set_size(20)
ax_box.set(xlabel='')
ax_hist.set(xlabel='Over Time',ylabel='Count')
plt.show()
```

Most Frequent Overtime duration is less than the 2000 minutes where as 6000-7000 has the highest frequency of overtime.has outlier in the feature

```python
num_feature = [feature for feature in garment_df.columns if garment_df[feature].dtype!='O'][2:-1]
```

```python
sns.pairplot(garment_df[num_feature],size=3,dropna=True,diag_kind='kde',palette='darkcyan')
plt.title("Garments Numeric Features").set_size(20)
plt.show()
```

There is no any relation between the features.

```python
df1 = pd.read_csv("winequality-red.csv",sep=";")
df1['wine'] = 'Red_Wine'
```

```python
df2 = pd.read_csv("winequality-white.csv",sep=";")
df2['wine'] = 'White_Wine'
```

```python
df = pd.concat([df1,df2])
```

```python
df.columns
```

**Output:**
```text
Index(['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol', 'quality', 'wine'],
      dtype='object')
```

```python
df.head()
```

**Output:**
```text
fixed acidity  volatile acidity  citric acid  residual sugar  chlorides  \
0            7.4              0.70         0.00             1.9      0.076   
1            7.8              0.88         0.00             2.6      0.098   
2            7.8              0.76         0.04             2.3      0.092   
3           11.2              0.28         0.56             1.9      0.075   
4            7.4              0.70         0.00             1.9      0.076   

   free sulfur dioxide  total sulfur dioxide  density    pH  sulphates  \
0                 11.0                  34.0   0.9978  3.51       0.56   
1                 25.0                  67.0   0.9968  3.20       0.68   
2                 15.0                  54.0   0.9970  3.26       0.65   
3                 17.0                  60.0   0.9980  3.16       0.58   
4                 11.0                  34.0   0.9978  3.51       0.56   

   alcohol  quality      wine  
0      9.4        5  Red_Wine  
1      9.8        5  Red_
... [Output truncated for brevity]
```

```python
import plotly.express as px


# plotting the line chart
fig =px.bar(df, x="wine", y="alcohol",title="Wine Alcohol Based",color='wine',color_discrete_sequence=["red", "darkcyan"])

# showing the plot
fig.show()
```

```python
plt.figure(figsize=(20,16))


for i,col in enumerate(list(df.columns.values[:-1])):
    plt.subplot(4,3,i+1)
    sns.distplot(df1[col],color='r',kde=True,label='Red Wine')
    sns.distplot(df2[col],color='darkcyan',kde=True,label='White Wine')
    plt.grid()
    plt.legend(loc = 'upper right')
    plt.tight_layout()
```

- pH feature is approximately normally distributed.
- Remaining all independent features are positively skewed

```python
plt.figure(figsize=(15,15))
for i,col in enumerate(list(df.columns.values[:-1])):
    plt.subplot(4,3,i+1)
    sns.boxplot(x =df['wine'], y = df[col],color='darkcyan')
    plt.grid('darkgrid')
    plt.tight_layout()
```

Outliers are the points outside the 1.5×IQR or more above the third quartile or 1.5×IQR or more below the first quartile.
* Except for alcohol, all other features have outliers.

```python
plt.figure(figsize=(10,10))
mask = np.triu(np.ones_like(df.corr()))
sns.heatmap(df.corr(),mask=mask,annot=True,vmin=-1,vmax=1)
plt.title("Correlation Plot", fontsize=20)
```

**Output:**
```text
Text(0.5, 1.0, 'Correlation Plot')
```

* density has a strong positive correlation with residual sugar, whereas it has a strong negative correlation with alcohol.
* pH & fixed acidity has negative correlation.
* density & fixed acidity has positive correlation.
* citric acid & fixed acidity has positive correlation.
* citric acid & volatile acidity has negative correlation.
* free sulphur dioxide & total sulphur dioxide has positive correlation.

```python
plt.figure(figsize=[10,8])
sns.set_theme(style='darkgrid')
plt.subplot(2,1,1)
sns.barplot(df1['quality'],df1['alcohol'],color='r')
plt.xlabel('').set_size(15)
plt.ylabel('Alcohol').set_size(15)
plt.title("Red Wine").set_size(20)


plt.subplot(2,1,2)
sns.barplot(df2['quality'],df2['alcohol'],color='darkcyan')
plt.xlabel('Quality').set_size(15)
plt.ylabel('Alcohol').set_size(15)
plt.title("White Wine").set_size(20)
plt.tight_layout()


plt.show()
```

Quality has higher concentration of alcohol in Red wine where as quality 9 has highest in the White Wine.

```python
plt.figure(figsize=(10,8))
sns.scatterplot(df['fixed acidity'],df['pH'],hue=df['wine'])
plt.xlabel('Acidity').set_size(15)
plt.ylabel('pH').set_size(15)
plt.title("Acidity/pH").set_size(20)
```

However, there is no direct connection between total acidity and pH (it is possible to find wines with a high pH for wine and high acidity).

```python
plt.figure(figsize=(10,8))
sns.set_theme(style='darkgrid')
plt.subplot(2,1,1)
sns.countplot(df1['citric acid'] > 0)
plt.xlabel('Citric Acid Content').set_size(15)
plt.ylabel('Count').set_size(15)
plt.title("Red Wine Citric Acid").set_size(20)
plt.tight_layout()


plt.subplot(2,1,2)
sns.countplot(df2['citric acid'] > 0)
plt.xlabel('Citric Acid Content').set_size(15)
plt.ylabel('Count').set_size(15)
plt.title("White Wine Citric Acid").set_size(20)
plt.tight_layout()


plt.show()
```

In the European Union, use of citric acid for acidification is prohibited, but limited use of citric acid is permitted for removing excess iron and copper from the wine if potassium ferrocyanide is not available.
From the above graph, we can infer that approximately 180-200 red wines are European.

```python
plt.figure(figsize=(10,8))

plt.figure(figsize=(10,8))
sns.set_theme(style='darkgrid')
plt.subplot(2,1,1)
sns.pointplot(df1['pH'].round(1),df1['residual sugar'], color='r')
plt.xlabel('pH').set_size(15)
plt.ylabel('Red Wine Residual Sugar').set_size(15)
plt.tight_layout()


plt.subplot(2,1,2)
sns.pointplot(df2['pH'].round(1),df2['residual sugar'], color='green')
plt.xlabel('pH').set_size(15)
plt.ylabel('White Residual Sugar').set_size(15)
plt.tight_layout()


plt.show()
```

From the graph, we can see that low levels of pH(High Acidity) have high levels of Sugar in red wines. whereas in white wines there levels of sugar is low on lower PH as well.