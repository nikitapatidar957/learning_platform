# End-to-End ML Pipeline: Cleaning, EDA, Feature Selection & Modeling

Step-by-step production case study on E-Commerce Customer Churn Prediction: comprehensive data cleaning, statistical exploratory analysis, outlier handling, hypothesis test feature selection, class imbalance mitigation, and model training.

---

## 1. Data Cleaning & Integrity Verification

# **Import Libraries and dataset**

```python
import os
os.environ['KAGGLE_CONFIG_DIR'] = "/content"
%cd /content
!kaggle datasets download -d ankitverma2010/ecommerce-customer-churn-analysis-and-prediction
!unzip \*.zip  && rm *.zip
```

**Execution Output:**
```text
/content
Warning: Your Kaggle API key is readable by other users on this system! To fix this, you can run 'chmod 600 /content/kaggle.json'
Downloading ecommerce-customer-churn-analysis-and-prediction.zip to /content
  0% 0.00/532k [00:00<?, ?B/s]
100% 532k/532k [00:00<00:00, 28.8MB/s]
Archive:  ecommerce-customer-churn-analysis-and-prediction.zip
  inflating: E Commerce Dataset.xlsx
```

```python
import logging

logger = logging.getLogger()

file_handler = logging.FileHandler(filename='ecc_dc_log.log', mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)
logger.info('FILE STARTS RUNNING!')
```

```python
import pandas as pd
import numpy as np
```

```python
logger.info('Libraries imported.')
```

```python
# Reading dataset to a dataframe
df = pd.read_excel('/content/E Commerce Dataset.xlsx', sheet_name='E Comm')
df.head()
```

**Execution Output:**
```text
CustomerID  Churn  Tenure PreferredLoginDevice  CityTier  WarehouseToHome  \
0       50001      1     4.0         Mobile Phone         3              6.0   
1       50002      1     NaN                Phone         1              8.0   
2       50003      1     NaN                Phone         1             30.0   
3       50004      1     0.0                Phone         3             15.0   
4       50005      1     0.0                Phone         1             12.0   

  PreferredPaymentMode  Gender  HourSpendOnApp  NumberOfDeviceRegistered  \
0           Debit Card  Female             3.0                         3   
1                  UPI    Male             3.0                         4   
2           Debit Card    Male             2.0                         4   
3           Debit Card    Male             2.0                         4   
4                   CC    Male             NaN                         3   

     PreferedOrderCat  SatisfactionScore MaritalStatus  NumberOfAddress  \
0  Laptop & Accessory                  2        Single                9   
1              Mobile                  3        Single                7   
2              Mobile                  3
... [Output truncated for brevity]
```

```python
logger.info('Data loaded.')
```

```python
# Reading data information/dictionary to a dataframe
data_info = pd.read_excel('/content/E Commerce Dataset.xlsx', sheet_name=0)
data_info.drop(['Unnamed: 0', 'Unnamed: 1'], axis=1, inplace=True)
data_info
```

**Execution Output:**
```text
Unnamed: 2  \
0                      Variable   
1                    CustomerID   
2                         Churn   
3                        Tenure   
4          PreferredLoginDevice   
5                      CityTier   
6               WarehouseToHome   
7          PreferredPaymentMode   
8                        Gender   
9                HourSpendOnApp   
10     NumberOfDeviceRegistered   
11             PreferedOrderCat   
12            SatisfactionScore   
13                MaritalStatus   
14              NumberOfAddress   
15                     Complain   
16  OrderAmountHikeFromlastYear   
17                   CouponUsed   
18                   OrderCount   
19            DaySinceLastOrder   
20               CashbackAmount   

                                           Unnamed: 3  
0                                         Discerption  
1                                  Unique customer ID  
2                                          Churn Flag  
3                  Tenure of customer in organization  
4                  Preferred login device of customer  
5                                           City tier  
6   Distance in between warehouse to home of customer  
7 
... [Output truncated for brevity]
```

```python
# Saving it to a txt for easy reference
np.savetxt(r'data_info.txt', data_info.values, fmt='%s')
```

# **Data Cleaning**

```python
logger.info('Data cleaning starts')
```

## **Basic Info**

```python
# Basic information on the dataset
df.info()
```

**Execution Output:**
```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5630 entries, 0 to 5629
Data columns (total 20 columns):
 #   Column                       Non-Null Count  Dtype  
---  ------                       --------------  -----  
 0   CustomerID                   5630 non-null   int64  
 1   Churn                        5630 non-null   int64  
 2   Tenure                       5366 non-null   float64
 3   PreferredLoginDevice         5630 non-null   object 
 4   CityTier                     5630 non-null   int64  
 5   WarehouseToHome              5379 non-null   float64
 6   PreferredPaymentMode         5630 non-null   object 
 7   Gender                       5630 non-null   object 
 8   HourSpendOnApp               5375 non-null   float64
 9   NumberOfDeviceRegistered     5630 non-null   int64  
 10  PreferedOrderCat             5630 non-null   object 
 11  SatisfactionScore            5630 non-null   int64  
 12  MaritalStatus                5630 non-null   object 
 13  NumberOfAddress              5630 non-null   int64  
 14  Complain                     5630 non-null   int64  
 15  OrderAmountHikeFromlastYear  5365 non-null   float64
 16  CouponUsed                   5374 non-null  
... [Output truncated for brevity]
```

**OBSERVATIONS**
- 5630 entries and 20 columns
- **Churn** is our target variable
- 8 floating point variables, 7 integer variables and 5 string variables
- There are some missing values.

**Check for duplicate rows** -

```python
df.duplicated().sum()
```

**Execution Output:**
```text
0
```

No duplicates

## **Check for Inconsistancies and corruptness**

```python
# Find the unique number of values for each variable
df.nunique()
```

**Execution Output:**
```text
CustomerID                     5630
Churn                             2
Tenure                           36
PreferredLoginDevice              3
CityTier                          3
WarehouseToHome                  34
PreferredPaymentMode              7
Gender                            2
HourSpendOnApp                    6
NumberOfDeviceRegistered          6
PreferedOrderCat                  6
SatisfactionScore                 5
MaritalStatus                     3
NumberOfAddress                  15
Complain                          2
OrderAmountHikeFromlastYear      16
CouponUsed                       17
OrderCount                       16
DaySinceLastOrder                22
CashbackAmount                 2586
dtype: int64
```

Except for Customer ID and CashbackAmount, lets find the unique values for the other columns

```python
# Unique values for columns
for col in df.drop(['CustomerID', 'CashbackAmount'], axis=1).columns:
  print('Column Name :', col)
  print(df[col].unique())
  print('-------------------------------------------------------------')
```

**Execution Output:**
```text
Column Name : Churn
[1 0]
-------------------------------------------------------------
Column Name : Tenure
[ 4. nan  0. 13. 11.  9. 19. 20. 14.  8. 18.  5.  2. 30.  1. 23.  3. 29.
  6. 26. 28.  7. 24. 25. 10. 15. 22. 27. 16. 12. 21. 17. 50. 60. 31. 51.
 61.]
-------------------------------------------------------------
Column Name : PreferredLoginDevice
['Mobile Phone' 'Phone' 'Computer']
-------------------------------------------------------------
Column Name : CityTier
[3 1 2]
-------------------------------------------------------------
Column Name : WarehouseToHome
[  6.   8.  30.  15.  12.  22.  11.   9.  31.  18.  13.  20.  29.  28.
  26.  14.  nan  10.  27.  17.  23.  33.  19.  35.  24.  16.  25.  32.
  34.   5.  21. 126.   7.  36. 127.]
-------------------------------------------------------------
Column Name : PreferredPaymentMode
['Debit Card' 'UPI' 'CC' 'Cash on Delivery' 'E wallet' 'COD' 'Credit Card']
-------------------------------------------------------------
Column Name : Gender
['Female' 'Male']
-------------------------------------------------------------
Column Name : HourSpendOnApp
[ 3.  2. nan  1.  0.  4.  5.]
-----------------------------------------------
... [Output truncated for brevity]
```

**OBSERVATIONS :** We can observe the following inconsistancies:
- **PreferredLoginDevice** : 'Mobile Phone' and 'Mobile' probably indicates mobile phone, since you cannot login with a land phone -> change it to a common 'Mobile'
- **WarehouseToHome** : Has extremely large values like 126 and 127, which is highly unlikely since people don't usually travel that long distance to buy goods. The values might be mistakenly entered -> change 126->26 and 127->27
- **PreferredPaymentMode** : 
  - 'CC' and 'Credit Card' indicate credit card -> change it to 'CC'
  - 'Cash on Delivery' and 'COD' indicate cash on delivery -> change it to 'COD'
  - In addition, change Debit Card to DC for convenience.
- **PreferedOrderCat**:
  - 'Mobile' and 'Mobile Phone' -> change it to 'Mobile'
  - 'Laptop & Accessory' -> change it to 'Laptop' for convenience.
- **NumberOfAddress** : Has large numbers above 10, which seems very unlikely. Need to look into it.

```python
# Correct values of column PreferredLoginDevice, WarehouseToHome, PreferredPaymentMode and PreferedOrderCat
df['PreferredLoginDevice'].replace({'Mobile Phone':'Mobile', 'Phone':'Mobile'}, inplace=True)
df['WarehouseToHome'].replace({126:26, 127:27}, inplace=True)
df['PreferredPaymentMode'].replace({'Credit Card':'CC', 'Cash on Delivery':'COD', 'Debit Card':'DC' }, inplace=True)
df['PreferedOrderCat'].replace({'Mobile Phone':'Mobile', 'Laptop & Accessory':'Laptop'}, inplace=True)
```

Now lets delve into the problem with the inconsistant values of NumberOfAddress.

```python
# Number of rows with NumberOfAddress greater than 5
df[df.NumberOfAddress>5].shape[0]
```

**Execution Output:**
```text
1453
```

There seems to be 1453 customers with more than 5 addresses registered in the ecommerce platform, in their name. This seems very unlikely. But we cannot rule out the following possibilities:
- The customer might have multiple properties(houses) in their name.
- Slight change in the address text.
- Addresses of workplace/workplaces if the customer works shifts.
- Ordering for someone else
- Someone else must be ordering in the customer's name name(either other family member with the customer's knowledge or in the rare case fraud transactions by outsiders).

In the above mention cases, multiple addresses might be added. 

If we have some other information like the actual list of addresses registered or the locations where the orders were made, number of family members, number of children, occupation related information, annual income etc., we might get a little bit insight into the possibility of customers have multiple addresses.

However, since we do not have them, we need to explore with the available information and reach a conclusion. We shall analyse more in the EDA process and come to a conclusion.

## **Dealing with missing values**

```python
# Find columns with missing values
missing_cols = [col for col in df.columns if df[col].isnull().any()]
missing_cols
```

**Execution Output:**
```text
['Tenure',
 'WarehouseToHome',
 'HourSpendOnApp',
 'OrderAmountHikeFromlastYear',
 'CouponUsed',
 'OrderCount',
 'DaySinceLastOrder']
```

```python
# Find the % of missing value in the above list of columns
percent = df[missing_cols].isnull().sum() * 100/len(df)
missing_df = pd.DataFrame({'column':missing_cols,
                           'no. of missing values' : df[missing_cols].isnull().sum().values,
                           'percentage' : percent.values})
missing_df
```

**Execution Output:**
```text
column  no. of missing values  percentage
0                       Tenure                    264    4.689165
1              WarehouseToHome                    251    4.458259
2               HourSpendOnApp                    255    4.529307
3  OrderAmountHikeFromlastYear                    265    4.706927
4                   CouponUsed                    256    4.547069
5                   OrderCount                    258    4.582593
6            DaySinceLastOrder                    307    5.452931
```

We see that the percent of missing values for any column is below 6%. We can either drop them (columnwise/rowwise) or impute them using any suitable method or a combination of both.

Dropping the column is not recommended, since each column has a max of only 6% missing values.

Lets look at the number of missing values in each row. If any rows has 4 or more than 4 missing values, we shall drop those rows.

```python
# Calculate the number of missing values in each row and finding the count
df.isnull().sum(axis=1).value_counts()
```

**Execution Output:**
```text
0    3774
1    1856
dtype: int64
```

The maximum number of missing value in any given row is 1. So, its difficult to drop rows with losing substantial information from the data. Therefore we shall impute them.

In our case, all our missing data are numeric type. Therefore, we shall fill the missing values with mean or median of the variable, depending in the skewness value.

```python
# Calculate skewness of missing value columns
df[missing_cols].skew(axis=0, skipna=True, numeric_only=True)
```

**Execution Output:**
```text
Tenure                         0.736513
WarehouseToHome                0.898406
HourSpendOnApp                -0.027213
OrderAmountHikeFromlastYear    0.790785
CouponUsed                     2.545653
OrderCount                     2.196414
DaySinceLastOrder              1.191000
dtype: float64
```

We can see that 
- **HourSpendOnApp** is normally distributed -> Fill missing values with mean
- **Tenure and OrderAmountHikeFromlastYear** are moderately skewed -> Fill missing values with mean
- **WarehouseToHome, CouponUsed, OrderCount and DaySinceLastOrder** are highly skewed -> Fill missing values with median

```python
round(df.HourSpendOnApp.mean()), round(df.Tenure.mean()), round(df.OrderAmountHikeFromlastYear.mean()), round(df.WarehouseToHome.mean())
```

**Execution Output:**
```text
(3, 10, 16, 16)
```

```python
df.CouponUsed.median(), df.OrderCount.median(), df.DaySinceLastOrder.median()
```

**Execution Output:**
```text
(1.0, 2.0, 3.0)
```

```python
# Fill missing values ith mean and median
df.fillna({'HourSpendOnApp':round(df.HourSpendOnApp.mean()), 
           'Tenure':round(df.Tenure.mean()), 
           'OrderAmountHikeFromlastYear':round(df.OrderAmountHikeFromlastYear.mean()),
           'WarehouseToHome':round(df.WarehouseToHome.mean()), 
           'CouponUsed':df.CouponUsed.median(), 
           'OrderCount':df.OrderCount.median(), 
           'DaySinceLastOrder':df.DaySinceLastOrder.median()}, inplace=True)
```

```python
df.head()
```

**Execution Output:**
```text
CustomerID  Churn  Tenure PreferredLoginDevice  CityTier  WarehouseToHome  \
0       50001      1     4.0               Mobile         3              6.0   
1       50002      1    10.0               Mobile         1              8.0   
2       50003      1    10.0               Mobile         1             30.0   
3       50004      1     0.0               Mobile         3             15.0   
4       50005      1     0.0               Mobile         1             12.0   

  PreferredPaymentMode  Gender  HourSpendOnApp  NumberOfDeviceRegistered  \
0                   DC  Female             3.0                         3   
1                  UPI    Male             3.0                         4   
2                   DC    Male             2.0                         4   
3                   DC    Male             2.0                         4   
4                   CC    Male             3.0                         3   

  PreferedOrderCat  SatisfactionScore MaritalStatus  NumberOfAddress  \
0           Laptop                  2        Single                9   
1           Mobile                  3        Single                7   
2           Mobile                  3        Sing
... [Output truncated for brevity]
```

```python
df.isnull().sum()
```

**Execution Output:**
```text
CustomerID                     0
Churn                          0
Tenure                         0
PreferredLoginDevice           0
CityTier                       0
WarehouseToHome                0
PreferredPaymentMode           0
Gender                         0
HourSpendOnApp                 0
NumberOfDeviceRegistered       0
PreferedOrderCat               0
SatisfactionScore              0
MaritalStatus                  0
NumberOfAddress                0
Complain                       0
OrderAmountHikeFromlastYear    0
CouponUsed                     0
OrderCount                     0
DaySinceLastOrder              0
CashbackAmount                 0
dtype: int64
```

```python
logger.info('Data cleaning ends!')
```

# **Save the data to Database**

```python
from pymongo import MongoClient
```

```python
# Connect to Mongodb cluster
client = MongoClient("mongodb+srv://<username>:<password>@mycluster.g3bp8fr.mongodb.net/?retryWrites=true&w=majority")

# List of databases
db_list = client.list_database_names()
```

```python
db_list
```

**Execution Output:**
```text
['CHURN', 'loan_db', 'admin', 'local']
```

```python
if 'CHURN' in db_list:
  # Drop database and create new database CHURN
  client.drop_database('CHURN')
  print(client.list_database_names())
  mydb = client.CHURN
else:
  pass
```

**Execution Output:**
```text
['loan_db', 'admin', 'local']
```

```python
# Creating collection/table 'ecomm_churn' in CHURN database
mytb = mydb.ecomm_churn
```

```python
# Convert dataframe o dictionary
data = df.to_dict(orient='records') 

# Insert 'data' to ecomm_churn
mytb.insert_many(data)
```

**Execution Output:**
```text
<pymongo.results.InsertManyResult at 0x7fc851a3e610>
```

```python
# Now check if CHURN added
client.list_database_names()
```

**Execution Output:**
```text
['CHURN', 'loan_db', 'admin', 'local']
```

```python
logger.info('Data saved in database!')
```

---

## 2. Statistical Exploratory Data Analysis (EDA)

# **Import necessary libraries and Load data from database**

```python
import logging

logger = logging.getLogger()

file_handler = logging.FileHandler(filename='ecc_eda_log.log', mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)
logger.info('FILE STARTS RUNNING!')
```

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

from pymongo import MongoClient

import warnings
warnings.filterwarnings('ignore')
```

```python
logger.info('Libraries imported!')
logger.info('Connecting to database...')
```

```python
# Connect to Mongodb cluster
client = MongoClient("mongodb+srv://<username>:<password>@mycluster.g3bp8fr.mongodb.net/?retryWrites=true&w=majority")

logger.info('Connected to database!')

# List of databases
db_list = client.list_database_names()
db_list
```

**Execution Output:**
```text
['CHURN', 'loan_db', 'admin', 'local']
```

```python
db = client.CHURN
```

```python
cursor = db.ecomm_churn.find()

df = pd.DataFrame(list(cursor)).drop('_id', axis=1)
df.head()
```

**Execution Output:**
```text
CustomerID  Churn  Tenure PreferredLoginDevice  CityTier  WarehouseToHome  \
0       50001      1     4.0               Mobile         3              6.0   
1       50002      1    10.0               Mobile         1              8.0   
2       50003      1    10.0               Mobile         1             30.0   
3       50004      1     0.0               Mobile         3             15.0   
4       50005      1     0.0               Mobile         1             12.0   

  PreferredPaymentMode  Gender  HourSpendOnApp  NumberOfDeviceRegistered  \
0                   DC  Female             3.0                         3   
1                  UPI    Male             3.0                         4   
2                   DC    Male             2.0                         4   
3                   DC    Male             2.0                         4   
4                   CC    Male             3.0                         3   

  PreferedOrderCat  SatisfactionScore MaritalStatus  NumberOfAddress  \
0           Laptop                  2        Single                9   
1           Mobile                  3        Single                7   
2           Mobile                  3        Sing
... [Output truncated for brevity]
```

```python
logger.info('Loaded data from database!')
```

```python
df.shape
```

**Execution Output:**
```text
(5630, 20)
```

# **Exploratory Data Analysis**

```python
logger.info('Data exploration starts!')
```

## **Basic Analysis**

```python
df.describe()
```

**Execution Output:**
```text
CustomerID        Churn       Tenure     CityTier  WarehouseToHome  \
count   5630.000000  5630.000000  5630.000000  5630.000000      5630.000000   
mean   52815.500000     0.168384    10.180995     1.654707        15.620426   
std     1625.385339     0.374240     8.354261     0.915389         8.075961   
min    50001.000000     0.000000     0.000000     1.000000         5.000000   
25%    51408.250000     0.000000     3.000000     1.000000         9.000000   
50%    52815.500000     0.000000     9.000000     1.000000        14.000000   
75%    54222.750000     0.000000    15.000000     3.000000        20.000000   
max    55630.000000     1.000000    61.000000     3.000000        36.000000   

       HourSpendOnApp  NumberOfDeviceRegistered  SatisfactionScore  \
count     5630.000000               5630.000000        5630.000000   
mean         2.934636                  3.688988           3.066785   
std          0.705528                  1.023999           1.380194   
min          0.000000                  1.000000           1.000000   
25%          2.000000                  3.000000           2.000000   
50%          3.000000                  4.000000           3.000000   
75%    
... [Output truncated for brevity]
```

```python
def unique_list():
  unique = []
  for col in df.columns:
    if col in ['CustomerID', 'CashbackAmount']:
      unique.append('Number of values too long for dataframe!')
    else:
      unique.append(df[col].unique())
  return unique
```

```python
basic_info = pd.DataFrame({'Columns' : df.columns,
                           'Data Type' : df.dtypes.values,
                           'No. of unique values' : df.nunique().values,
                           'Unique values' : unique_list()})
basic_info
```

**Execution Output:**
```text
Columns Data Type  No. of unique values  \
0                    CustomerID     int64                  5630   
1                         Churn     int64                     2   
2                        Tenure   float64                    36   
3          PreferredLoginDevice    object                     2   
4                      CityTier     int64                     3   
5               WarehouseToHome   float64                    32   
6          PreferredPaymentMode    object                     5   
7                        Gender    object                     2   
8                HourSpendOnApp   float64                     6   
9      NumberOfDeviceRegistered     int64                     6   
10             PreferedOrderCat    object                     5   
11            SatisfactionScore     int64                     5   
12                MaritalStatus    object                     3   
13              NumberOfAddress     int64                    15   
14                     Complain     int64                     2   
15  OrderAmountHikeFromlastYear   float64                    16   
16                   CouponUsed   float64                    17   
17                
... [Output truncated for brevity]
```

**OBSERVATION** :
- We have a total of 5630 customers information
- Numeric features : 13 (exclusing CustomerID and Churn), out of which 3 of them are categorical data
- String type features : 5

So we might have a total of 10 numeric and 8 categorical input features.
Lets explore them one by one.

## **Distribution of dependent variable : 'Churn'**

```python
df['Churn'].value_counts()
```

**Execution Output:**
```text
0    4682
1     948
Name: Churn, dtype: int64
```

```python
x_labels= ['No', 'Yes']

fig,ax = plt.subplots(figsize=(5,5))
ax=sns.countplot(x='Churn', data=df)
ax.set_xticklabels(x_labels)
plt.title('Figure 1 : Distribution of target variable')
plt.show()
```

We can see that this is a highly imbalanced dataset

## **Numeric Features**

### **Functions**

```python
# Function to plot the distribution of numerical variable
def plot_num_var(var_name, var_label, bin_num, fig_num):
  plt.figure(figsize = (25,5))
  plt.suptitle('Figure {} : Distribution of {}'.format(fig_num,var_name))

  plt.subplot(1,2,1)
  sns.histplot(data=df, x=var_name, bins=bin_num)
  plt.title('Fig {}(a)'.format(fig_num))
  plt.xlabel(var_name)
  plt.ylabel('Count')

  plt.subplot(1,2,2)
  sns.boxplot(data=df, x=var_name)
  plt.title('Fig {}(b)'.format(fig_num))
  plt.xlabel(var_name)
  
  plt.show()
```

```python
# Function to plot the distribution of numerical variable by Churn value
def plot_numvar_creditrisk(var_name, var_label, bin_num, fig_num):
  plt.figure(figsize = (25,5))
  plt.suptitle('Figure {} : Distribution of {} by Churn value'.format(fig_num,var_label))

  plt.subplot(1,2,1)
  sns.histplot(data=df, x=var_name, hue='Churn', bins=bin_num)
  plt.title('Fig {}(a)'.format(fig_num))
  plt.xlabel(var_label)
  plt.ylabel('Count')
  
  plt.subplot(1,2,2)
  sns.boxplot(data=df, x='Churn', y=var_name)
  plt.title('Fig {}(b)'.format(fig_num))
  plt.xlabel('Churn value')
  
  plt.show()
```

### **Tenure of customer in organization : 'Tenure'**

```python
# Distribution of Tenure of the customers with the ecommerce platform
plot_num_var('Tenure', 'Churn', 30, 2)
```

```python
percentiles = [0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 0.99]

pd.DataFrame(df['Tenure'].describe(percentiles=percentiles)).T
```

**Execution Output:**
```text
count       mean       std  min  10%  20%  25%  30%  40%  50%   60%  \
Tenure  5630.0  10.180995  8.354261  0.0  1.0  1.0  3.0  4.0  7.0  9.0  11.0   

         70%   75%   80%   90%   99%   max  
Tenure  14.0  15.0  17.0  23.0  30.0  61.0
```

```python
# Distribution of Tenure of customers by Churn value
plot_numvar_creditrisk('Tenure', 'Churn', 30, 3)
```

```python
df.groupby('Churn')['Tenure'].describe(percentiles=percentiles)
```

**Execution Output:**
```text
count       mean       std  min  10%  20%  25%  30%  40%   50%   60%  \
Churn                                                                          
0      4682.0  11.443614  8.258140  0.0  1.0  4.0  5.0  6.0  8.0  10.0  12.0   
1       948.0   3.945148  5.563415  0.0  0.0  0.0  0.0  1.0  1.0   1.0   1.0   

        70%   75%   80%   90%    99%   max  
Churn                                       
0      15.0  17.0  19.0  24.0  31.00  61.0  
1       4.0   7.0  10.0  12.3  20.53  21.0
```

**OBSERVATION**:
- Most of the customers have a Tenure between 0 to 20 months.
- Is right skewed.
- The probability to churn is found to be higher for customers whose tenure is within 2 or 3 months (Fig 3(a)). Although this might not be the actual picture, as its not fair to come to a conclusion within just 2 months.
- Similarly, Fig 3(a) shows that as the tenure increases, the possibility of churning also decreases.
- A few outliers are observed after 50 months of Tenure (Fig 2(b))
- Fig 3(b) and the description table shows that 50 t0 60 % of customers who churned have tenure of 1 month
- Max tenure for churned customer is 21. Which means any customer whose tenure is greater than that (till 61 months) have not churned.

We might have to assume that Tenure is a good input feature for our model.

### **Distance in between warehouse to home of customer : 'WarehouseToHome'**

```python
# Distribution of distance of the warehouse from the customers' houses
plot_num_var('WarehouseToHome', 'Churn', 60, 4)
```

```python
percentiles = [0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 0.99]

pd.DataFrame(df['WarehouseToHome'].describe(percentiles=percentiles)).T
```

**Execution Output:**
```text
count       mean       std  min  10%  20%  25%  30%   40%  \
WarehouseToHome  5630.0  15.620426  8.075961  5.0  7.0  8.0  9.0  9.0  12.0   

                  50%   60%   70%   75%   80%   90%   99%   max  
WarehouseToHome  14.0  16.0  17.0  20.0  23.0  29.1  35.0  36.0
```

```python
# Distribution of the distance of the warehouse from the customers' houses by Churn value
plot_numvar_creditrisk('WarehouseToHome', 'Churn', 60, 5)
```

```python
df.groupby('Churn')['WarehouseToHome'].describe(percentiles=percentiles)
```

**Execution Output:**
```text
count       mean       std  min  10%  20%   25%   30%   40%   50%  \
Churn                                                                       
0      4682.0  15.334259  8.011739  5.0  7.0  8.0   9.0   9.0  11.0  14.0   
1       948.0  17.033755  8.245758  5.0  8.0  9.0  10.0  11.0  14.0  16.0   

        60%   70%   75%   80%   90%    99%   max  
Churn                                             
0      15.6  17.0  19.0  22.0  29.0  35.00  36.0  
1      16.0  20.0  22.0  25.6  31.0  35.53  36.0
```

**OBSERVATION**:
- Most of the customers have a distance between 5 to 20 kms to the warehouse from their home
- Right skewed.
- The ratio of customers who have churned to have not churned seems to be almost consistent with increasing distance
- The mean distance for customers have churned and not-churned do not show any significant difference

Therefore, we might have to assume that WarehouseToHome does not contribute much value for our model.

### **Percentage increases in order from last year : 'OrderAmountHikeFromlastYear'**

```python
# Distribution of the percentage increase in order from last year
plot_num_var('OrderAmountHikeFromlastYear', 'Churn', 15, 6)
```

```python
percentiles = [0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 0.99]

pd.DataFrame(df['OrderAmountHikeFromlastYear'].describe(percentiles=percentiles)).T
```

**Execution Output:**
```text
count      mean       std   min   10%   20%  \
OrderAmountHikeFromlastYear  5630.0  15.72167  3.588459  11.0  12.0  13.0   

                              25%   30%   40%   50%   60%   70%   75%   80%  \
OrderAmountHikeFromlastYear  13.0  13.0  14.0  15.0  16.0  17.0  18.0  19.0   

                              90%   99%   max  
OrderAmountHikeFromlastYear  21.0  25.0  26.0
```

```python
# Distribution of the percentage increase in order from last year by Churn value
plot_numvar_creditrisk('OrderAmountHikeFromlastYear', 'Churn', 30, 7)
```

```python
df.groupby('Churn')['OrderAmountHikeFromlastYear'].describe(percentiles=percentiles)
```

**Execution Output:**
```text
count       mean       std   min   10%   20%   25%   30%   40%   50%  \
Churn                                                                          
0      4682.0  15.739641  3.547692  11.0  12.0  13.0  13.0  13.0  14.0  15.0   
1       948.0  15.632911  3.784068  11.0  12.0  12.0  13.0  13.0  14.0  15.0   

        60%   70%   75%   80%   90%   99%   max  
Churn                                            
0      16.0  17.0  18.0  19.0  21.0  25.0  26.0  
1      16.0  17.0  18.0  19.0  22.0  25.0  26.0
```

**OBSERVATION**:
- For most of the customers the % of increase in orders from last year has been between 12 to 17 %
- Is right skewed.
- The mean distance for customers have churned and not-churned do not show any significant difference

Therefore, we might have to assume that WarehouseToHome does not contribute much value for our model.

### **Total number of coupon has been used in last month : 'CouponUsed'**

```python
# Distribution of no. of cupons used by the customers in last month
plot_num_var('CouponUsed', 'Churn', 8, 8)
```

```python
percentiles = [0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 0.99]

pd.DataFrame(df['CouponUsed'].describe(percentiles=percentiles)).T
```

**Execution Output:**
```text
count      mean      std  min  10%  20%  25%  30%  40%  50%  60%  \
CouponUsed  5630.0  1.716874  1.85764  0.0  0.0  1.0  1.0  1.0  1.0  1.0  1.0   

            70%  75%  80%  90%  99%   max  
CouponUsed  2.0  2.0  2.0  4.0  9.0  16.0
```

```python
# Distribution of no. of cupons used by the customers in last month by Churn value
plot_numvar_creditrisk('CouponUsed', 'Churn', 8, 9)
```

```python
df.groupby('Churn')['CouponUsed'].describe(percentiles=percentiles)
```

**Execution Output:**
```text
count      mean       std  min  10%  20%  25%  30%  40%  50%  60%  \
Churn                                                                       
0      4682.0  1.718069  1.850065  0.0  0.0  1.0  1.0  1.0  1.0  1.0  1.0   
1       948.0  1.710970  1.895586  0.0  0.0  1.0  1.0  1.0  1.0  1.0  1.0   

       70%  75%  80%  90%   99%   max  
Churn                                  
0      2.0  2.0  2.0  4.0  9.00  16.0  
1      2.0  2.0  2.0  4.0  8.53  16.0
```

**OBSERVATION**:
- For most of the customers have used 0 to 2 coupons in the last month.
- Is right skewed.
- The mean number of coupons used for customers have churned and not-churned do not show any significant difference

Therefore, we might have to assume that CouponUsed does not contribute much value for our model.

### **Total number of orders has been places in last month : 'OrderCount'**

```python
# Distribution of the number of orders made by the customers in last month
plot_num_var('OrderCount', 'Churn', 8, 10)
```

```python
percentiles = [0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 0.99]

pd.DataFrame(df['OrderCount'].describe(percentiles=percentiles)).T
```

**Execution Output:**
```text
count      mean       std  min  10%  20%  25%  30%  40%  50%  \
OrderCount  5630.0  2.961812  2.879248  1.0  1.0  1.0  1.0  1.0  2.0  2.0   

            60%  70%  75%  80%  90%   99%   max  
OrderCount  2.0  2.0  3.0  4.0  7.0  14.0  16.0
```

```python
# Distribution of the number of orders made by the customers in last month by Churn value
plot_numvar_creditrisk('OrderCount', 'Churn', 8, 11)
```

```python
df.groupby('Churn')['OrderCount'].describe(percentiles=percentiles)
```

**Execution Output:**
```text
count      mean       std  min  10%  20%  25%  30%  40%  50%  60%  \
Churn                                                                       
0      4682.0  2.992952  2.897183  1.0  1.0  1.0  1.0  1.0  2.0  2.0  2.0   
1       948.0  2.808017  2.785363  1.0  1.0  1.0  1.0  1.0  2.0  2.0  2.0   

       70%  75%  80%  90%   99%   max  
Churn                                  
0      2.0  3.0  4.0  7.0  14.0  16.0  
1      2.0  3.0  3.0  7.0  15.0  16.0
```

**OBSERVATION**:
- For most of the customers have ordered upto 3 times in the last month.
- Is right skewed.
- The mean number of orders made by customers who have churned and not-churned do not show any significant difference

Therefore, we might have to assume that OrderCount does not contribute much value for our model.

### **Day Since last order by customer : 'DaySinceLastOrder'**

```python
# Distribution of the number of days since last order 
plot_num_var('DaySinceLastOrder', 'Churn', 23, 12)
```

```python
percentiles = [0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 0.99]

pd.DataFrame(df['DaySinceLastOrder'].describe(percentiles=percentiles)).T
```

**Execution Output:**
```text
count      mean       std  min  10%  20%  25%  30%  40%  \
DaySinceLastOrder  5630.0  4.459325  3.570626  0.0  1.0  2.0  2.0  2.0  3.0   

                   50%  60%  70%  75%  80%  90%   99%   max  
DaySinceLastOrder  3.0  4.0  7.0  7.0  8.0  9.0  15.0  46.0
```

```python
# Distribution of the number of days since last order by churn value
plot_numvar_creditrisk('DaySinceLastOrder', 'Churn', 23, 13)
```

```python
df.groupby('Churn')['DaySinceLastOrder'].describe(percentiles=percentiles)
```

**Execution Output:**
```text
count      mean       std  min  10%  20%  25%  30%  40%  50%  60%  \
Churn                                                                       
0      4682.0  4.709739  3.568374  0.0  1.0  2.0  2.0  2.0  3.0  3.0  4.0   
1       948.0  3.222574  3.316790  0.0  0.0  1.0  1.0  1.0  2.0  2.5  3.0   

       70%  75%  80%  90%   99%   max  
Churn                                  
0      7.0  8.0  8.0  9.0  15.0  31.0  
1      4.0  4.0  6.0  8.0  12.0  46.0
```

**OBSERVATION**:
- The number of days passed since last order for most of the customers have been mostly upto 7 days.
- Is right skewed.
- The mean number of orders made by customers who have churned and not-churned do shows a significant difference

Therefore, we might have to assume that DaySinceLastOrder does contributes some value for our model.

### **Average cashback in last month : 'CashbackAmount'**

```python
# Distribution of avg cashback amount in last month
plot_num_var('CashbackAmount', 'Churn', 23, 14)
```

```python
percentiles = [0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 0.99]

pd.DataFrame(df['CashbackAmount'].describe(percentiles=percentiles)).T
```

**Execution Output:**
```text
count       mean        std  min     10%      20%     25%  \
CashbackAmount  5630.0  177.22303  49.207036  0.0  126.86  140.804  145.77   

                    30%      40%     50%      60%     70%       75%      80%  \
CashbackAmount  148.334  153.654  163.28  173.066  187.09  196.3925  208.814   

                   90%       99%     max  
CashbackAmount  259.72  318.7431  324.99
```

```python
# Distribution of avg cashback amount in last month by churn value
plot_numvar_creditrisk('CashbackAmount', 'Churn', 23, 15)
```

```python
df.groupby('Churn')['CashbackAmount'].describe(percentiles=percentiles)
```

**Execution Output:**
```text
count        mean        std     min      10%      20%     25%  \
Churn                                                                    
0      4682.0  180.635203  50.434791    0.00  128.371  143.778  147.24   
1       948.0  160.370928  38.436055  110.09  123.210  127.414  132.02   

           30%     40%      50%     60%      70%     75%      80%     90%  \
Churn                                                                       
0      150.039  156.31  166.115  176.35  190.151  201.25  215.666  265.91   
1      139.040  146.80  149.660  154.73  167.350  174.69  185.356  212.22   

            99%     max  
Churn                    
0      319.0847  324.99  
1      306.3545  323.59
```

**OBSERVATION**:
- The average cashback in the last month mostly between 10 and 140 dollars.
- Outliers observed
- The mean cashback in the last month, made by customers who have churned and not-churned do show a significant difference.

Therefore, we might have to assume that CashbackAmount does contributes some value for our model.

### **Number of hours spent on mobile application : 'HourSpendOnApp'**

```python
# Distribution of the number of hours spent by the customers on the ecommerce app
plot_num_var('HourSpendOnApp', 'Churn', 23, 16)
```

```python
percentiles = [0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 0.99]

pd.DataFrame(df['HourSpendOnApp'].describe(percentiles=percentiles)).T
```

**Execution Output:**
```text
count      mean       std  min  10%  20%  25%  30%  40%  50%  \
HourSpendOnApp  5630.0  2.934636  0.705528  0.0  2.0  2.0  2.0  3.0  3.0  3.0   

                60%  70%  75%  80%  90%  99%  max  
HourSpendOnApp  3.0  3.0  3.0  4.0  4.0  4.0  5.0
```

```python
# Distribution of the number of hours spent by the customers on the ecommerce app by churn value
plot_numvar_creditrisk('HourSpendOnApp', 'Churn', 23, 17)
```

```python
df.groupby('Churn')['CashbackAmount'].describe(percentiles=percentiles)
```

**Execution Output:**
```text
count        mean        std     min      10%      20%     25%  \
Churn                                                                    
0      4682.0  180.635203  50.434791    0.00  128.371  143.778  147.24   
1       948.0  160.370928  38.436055  110.09  123.210  127.414  132.02   

           30%     40%      50%     60%      70%     75%      80%     90%  \
Churn                                                                       
0      150.039  156.31  166.115  176.35  190.151  201.25  215.666  265.91   
1      139.040  146.80  149.660  154.73  167.350  174.69  185.356  212.22   

            99%     max  
Churn                    
0      319.0847  324.99  
1      306.3545  323.59
```

**OBSERVATION**:
- The average cashback in the last month mostly between 10 and 140 dollars.
- Outliers observed
- The mean cashback in the last month, made by customers who have churned and not-churned do show a significant difference.

Therefore, we might have to assume that CashbackAmount does contributes some value for our model.

### **Total number of deceives is registered on particular customer : 'NumberOfDeviceRegistered'**

```python
# Distribution of the number of devices registered on the ecommerce app
plot_num_var('NumberOfDeviceRegistered', 'Churn', 23, 18)
```

```python
percentiles = [0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 0.99]

pd.DataFrame(df['NumberOfDeviceRegistered'].describe(percentiles=percentiles)).T
```

**Execution Output:**
```text
count      mean       std  min  10%  20%  25%  30%  \
NumberOfDeviceRegistered  5630.0  3.688988  1.023999  1.0  3.0  3.0  3.0  3.0   

                          40%  50%  60%  70%  75%  80%  90%  99%  max  
NumberOfDeviceRegistered  4.0  4.0  4.0  4.0  4.0  4.0  5.0  6.0  6.0
```

```python
# Distribution of the number of devices registered on the ecommerce app by churn value
plot_numvar_creditrisk('NumberOfDeviceRegistered', 'Churn', 23, 19)
```

```python
df.groupby('Churn')['NumberOfDeviceRegistered'].describe(percentiles=percentiles)
```

**Execution Output:**
```text
count      mean       std  min  10%  20%  25%  30%  40%  50%  60%  \
Churn                                                                       
0      4682.0  3.639257  1.018910  1.0  3.0  3.0  3.0  3.0  3.0  4.0  4.0   
1       948.0  3.934599  1.014127  1.0  3.0  3.0  3.0  3.0  4.0  4.0  4.0   

       70%  75%  80%  90%  99%  max  
Churn                                
0      4.0  4.0  4.0  5.0  6.0  6.0  
1      4.0  5.0  5.0  5.0  6.0  6.0
```

**OBSERVATION**:
- Maority of the customers have 3 to 4 devices registered with the app.

### **Total number of addresses added on particular customer : 'NumberOfAddress'**

```python
# Distribution of the number of addresses added by the customers on the ecommerce app
plot_num_var('NumberOfAddress', 'Churn', 23, 20)
```

```python
percentiles = [0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 0.99]

pd.DataFrame(df['NumberOfAddress'].describe(percentiles=percentiles)).T
```

**Execution Output:**
```text
count      mean       std  min  10%  20%  25%  30%  40%  \
NumberOfAddress  5630.0  4.214032  2.583586  1.0  2.0  2.0  2.0  2.0  3.0   

                 50%  60%  70%  75%  80%  90%   99%   max  
NumberOfAddress  3.0  4.0  5.0  6.0  6.0  8.0  11.0  22.0
```

```python
# Distribution of the number of addresses of the customers added on the ecommerce app by churn value
plot_numvar_creditrisk('NumberOfAddress', 'Churn', 23, 21)
```

```python
df.groupby('Churn')['NumberOfAddress'].describe(percentiles=percentiles)
```

**Execution Output:**
```text
count      mean       std  min  10%  20%  25%  30%  40%  50%  60%  \
Churn                                                                       
0      4682.0  4.162965  2.537001  1.0  2.0  2.0  2.0  2.0  3.0  3.0  4.0   
1       948.0  4.466245  2.790071  1.0  2.0  2.0  2.0  2.0  3.0  3.0  4.0   

       70%  75%  80%  90%   99%   max  
Churn                                  
0      5.0  5.0  6.0  8.0  11.0  22.0  
1      6.0  6.0  7.0  9.0  11.0  20.0
```

**OBSERVATION**:
- Majority of the customers have  or 3 addresses added with the app
- Outliers observed.
- The mean number of addresses for the customers who have churned and not-churned do not show a significant difference.

Therefore, we might have to assume that NumberOfAddress does not contributes much value for our model.

## **Categorical features**

### **Functions**

```python
def plotting_percentages(df, col, target, fig_num, x_labels):
    x, y = col, target
    
    # Temporary dataframe with percentage values
    temp_df = df.groupby(x)[y].value_counts(normalize=True)
    temp_df = temp_df.mul(100).rename('percent').reset_index()

    # Sort the column values for plotting    
    #order_list = list(df[col].unique())
    #order_list.sort()

    # Plot the figure
    sns.set(font_scale=1.5)
    g = sns.catplot(x=x, y='percent', hue=y,kind='bar', data=temp_df, height=6, aspect=3)
    g.ax.set_xticklabels(x_labels)
    g.ax.set_ylim(0,100)

    # Loop through each bar in the graph and add the percentage value    
    for p in g.ax.patches:
        txt = str(p.get_height().round(1)) + '%'
        txt_x = p.get_x() 
        txt_y = p.get_height()
        g.ax.text(txt_x,txt_y,txt)
        
    # Set labels and title
    plt.title(f'Figure {fig_num}(b) : {col.title()} By Percent {target.title()}')
    plt.xlabel(f'{col.title()}')
               
    plt.ylabel(f'{target.title()} Percentage', 
               fontdict={'fontsize': 20})
    return g
```

```python
def chisq_test(df, cat_var):
    # Creating an empty list of final selected predictors
    #SelectedPredictors=[]

    CrossTabResult=pd.crosstab(index=df['credit_risk'], columns=df[cat_var])
    ChiSqResult = chi2_contingency(CrossTabResult)
        
    # If the ChiSq P-Value is <0.05, that means we reject H0
    if (ChiSqResult[1] < 0.05):
        print('P-Value :', ChiSqResult[1])
        print('\'',cat_var,'\' IS CORRELATED with \'credit_risk\'')
    else:
        print('P-Value :', ChiSqResult[1])
        print(f'\'{cat_var}\' IS NOT CORRELATED with credit_risk')
```

### **Preferred login device of customer : 'PreferredLoginDevice'**

```python
df['PreferredLoginDevice'].unique()
```

**Execution Output:**
```text
array(['Mobile', 'Computer'], dtype=object)
```

```python
fig,ax = plt.subplots(figsize=(15,5))
ax=sns.countplot(x='PreferredLoginDevice', data=df)
plt.title('Figure 22 : Distribution of the number of customers preferring different login devices')
plt.show()
```

```python
fig,ax = plt.subplots(figsize=(15,5))
ax=sns.countplot(x='PreferredLoginDevice', hue='Churn', data=df)
plt.title('Figure 23(a) : Distribution of the number of customers preferring different login devices by Churn value')
plt.show()

plotting_percentages(df, 'PreferredLoginDevice', 'Churn', 23, df.PreferredLoginDevice.unique())
```

**Execution Output:**
```text
<seaborn.axisgrid.FacetGrid at 0x7fc4e8ee5a30>
```

**OBSERVATIONS :**
- Majority of the customers prefer mobile phones for logging into the ecommerce app.
- When categorized based on Churn value, while observing the percentage plot, the proportion of customers who have churned and not churned is almost similar for all categories under Preferredlogindevice.

It might be safe to assume that Preferredlogindevice might NOT be a good predictor variable for our model.

### **Tier type of the city the customer is living in : 'CityTier'**

```python
df['CityTier'].unique()
```

**Execution Output:**
```text
array([3, 1, 2])
```

```python
fig,ax = plt.subplots(figsize=(15,5))
ax=sns.countplot(x='CityTier', data=df)
plt.title('Figure 24 : Distribution of the number of customers based on the tier of the city they live in')
plt.show()
```

```python
fig,ax = plt.subplots(figsize=(15,5))
ax=sns.countplot(x='CityTier', hue='Churn', data=df)
plt.title('Figure 25(a) : Distribution of the number of customers based on the tier of the city they live in by Churn value')
plt.show()

plotting_percentages(df, 'CityTier', 'Churn', 25, df.CityTier.unique())
```

**Execution Output:**
```text
<seaborn.axisgrid.FacetGrid at 0x7fc4e93c8dc0>
```

**OBSERVATIONS :**
- Majority of the customers live in Tier 1 city, the least in Tier 2.
- When categorized based on Churn value, while observing the percentage plot, we see that the percentage of customers who churned were lesser in Tier 3 cities than others.

We shall assume that CityTier might prove be a good predictor variable for our model.

### **Preferred payment method of customer : 'PreferredPaymentMode'**

```python
df['PreferredPaymentMode'].unique()
```

**Execution Output:**
```text
array(['DC', 'UPI', 'CC', 'COD', 'E wallet'], dtype=object)
```

```python
fig,ax = plt.subplots(figsize=(15,5))
ax=sns.countplot(x='PreferredPaymentMode', data=df)
plt.title('Figure 26 : Distribution of the number of customers based on their preferred payment method')
plt.show()
```

```python
fig,ax = plt.subplots(figsize=(15,5))
ax=sns.countplot(x='PreferredPaymentMode', hue='Churn', data=df)
plt.title('Figure 27(a) : Distribution of the number of customers based on their preferred payment method by Churn value')
plt.show()

plotting_percentages(df, 'PreferredPaymentMode', 'Churn', 27, df.PreferredPaymentMode.unique())
```

**Execution Output:**
```text
<seaborn.axisgrid.FacetGrid at 0x7fc4e9415c70>
```

**OBSERVATIONS :**
- Majority of the customers prefer debit cards or credit cards for their payment.
- When categorized based on Churn value, while observing the percentage plot, we see that the percentage of customers who churned were lesser in customers who used debit and credit cards compared to other modes.

We shall assume that Preferredpaymentmode might prove be a good predictor variable for our model.

### **Gender of customer : 'Gender'**

```python
df['Gender'].unique()
```

**Execution Output:**
```text
array(['Female', 'Male'], dtype=object)
```

```python
df['Gender'].value_counts()
```

**Execution Output:**
```text
Male      3384
Female    2246
Name: Gender, dtype: int64
```

```python
fig,ax = plt.subplots(figsize=(15,5))
ax=sns.countplot(x='Gender', data=df)
plt.title('Figure 28 : Distribution of the number of customers based on their gender')
plt.show()
```

```python
fig,ax = plt.subplots(figsize=(15,5))
ax=sns.countplot(x='Gender', hue='Churn', data=df)
plt.title('Figure 29(a) : Distribution of the number of customers based on their gender by Churn value')
plt.show()

plotting_percentages(df, 'Gender', 'Churn', 29, df.Gender.unique())
```

**Execution Output:**
```text
<seaborn.axisgrid.FacetGrid at 0x7fc4e8e6ae50>
```

**OBSERVATIONS :**
- There are more male customers than females.
- When categorized based on Churn value, while observing the percentage plot, we see that the percentage of customers who churned were almost at similar levels among both males and females.

We shall assume that Gender might not be a good predictor variable for our model.

### **Preferred order category of customer in last month : 'PreferedOrderCat'**

```python
df['PreferedOrderCat'].unique()
```

**Execution Output:**
```text
array(['Laptop', 'Mobile', 'Others', 'Fashion', 'Grocery'], dtype=object)
```

```python
df.PreferedOrderCat.value_counts()
```

**Execution Output:**
```text
Mobile     2080
Laptop     2050
Fashion     826
Grocery     410
Others      264
Name: PreferedOrderCat, dtype: int64
```

```python
fig,ax = plt.subplots(figsize=(15,5))
ax=sns.countplot(x='PreferedOrderCat', data=df)
plt.title('Figure 30 : Distribution of the number of customers based on the categories they prefer to order most from')
plt.show()
```

```python
fig,ax = plt.subplots(figsize=(15,5))
ax=sns.countplot(x='PreferedOrderCat', hue='Churn', data=df)
plt.title('Figure 31(a) : Distribution of the number of customers based on the categories they prefer to order most from by Churn value')
plt.show()

plotting_percentages(df, 'PreferedOrderCat', 'Churn', 31, df.PreferedOrderCat.unique())
```

**Execution Output:**
```text
<seaborn.axisgrid.FacetGrid at 0x7fc4e84ebbe0>
```

**OBSERVATIONS :**
- Majority of the customers have made most of their orders either in the laptop or mobile categories.
- When categorized based on Churn value, while observing the percentage plot, we see that the customers who have ordered the most from the fashion category have churned the most, while the least churned ordered under Mobile followed closely by Grocery.
There is definitely a difference in the churn percentages across the different categories.

Therefore,we shall assume that Preferredordercat might prove be a good predictor variable for our model.

### **Satisfactory score of customer on service : 'SatisfactionScore'**

```python
df['SatisfactionScore'].unique()
```

**Execution Output:**
```text
array([2, 3, 5, 4, 1])
```

```python
df.SatisfactionScore.value_counts()
```

**Execution Output:**
```text
3    1698
1    1164
5    1108
4    1074
2     586
Name: SatisfactionScore, dtype: int64
```

```python
fig,ax = plt.subplots(figsize=(15,5))
ax=sns.countplot(x='SatisfactionScore', data=df)
plt.title('Figure 32 : Distribution of the number of customers based on the satisfaction scores they gave')
plt.show()
```

```python
fig,ax = plt.subplots(figsize=(15,5))
ax=sns.countplot(x='SatisfactionScore', hue='Churn', data=df)
plt.title('Figure 33(a) : Distribution of the number of customers based on the satisfaction score by Churn value')
plt.show()

plotting_percentages(df, 'SatisfactionScore', 'Churn', 33, df.SatisfactionScore.unique())
```

**Execution Output:**
```text
<seaborn.axisgrid.FacetGrid at 0x7fc4e911ec70>
```

**OBSERVATIONS :**
- Most of the customers have awarded an average satisfaction score(3), followed by good scores(4,5 combined) and then bad scores(1,2 combined)
- The least given score is 2
- When categorized based on Churn value, while observing the percentage plot, we see that customers that have given a score of 1 have highest churn % (which is understandable), while it it interesting to note that customers who have given good scores(4,,5) also have churned(nect to 1) out considerably more than what we would expect. 
- It is again interesting to note that while the least number of customers have awarded a score of 2 the chhurn % is also the lowest of the five scores

There is definitely a difference in the churn percentages across the different categories.

Therefore,we shall assume that SatisfactionScore might prove be a good predictor variable for our model.

### **Marital status of customer : 'MaritalStatus'**

```python
df['MaritalStatus'].unique()
```

**Execution Output:**
```text
array(['Single', 'Divorced', 'Married'], dtype=object)
```

```python
df.MaritalStatus.value_counts()
```

**Execution Output:**
```text
Married     2986
Single      1796
Divorced     848
Name: MaritalStatus, dtype: int64
```

```python
fig,ax = plt.subplots(figsize=(15,5))
ax=sns.countplot(x='MaritalStatus', data=df)
plt.title('Figure 34 : Distribution of the number of customers based on their marital status')
plt.show()
```

```python
fig,ax = plt.subplots(figsize=(15,5))
ax=sns.countplot(x='MaritalStatus', hue='Churn', data=df)
plt.title('Figure 35(a) : Distribution of the number of customers based on the marital status by Churn value')
plt.show()

plotting_percentages(df, 'MaritalStatus', 'Churn', 35, df.MaritalStatus.unique())
```

**Execution Output:**
```text
<seaborn.axisgrid.FacetGrid at 0x7fc4e8c00df0>
```

**OBSERVATIONS :**
- Maority of the customers are married
- When categorized based on Churn value, while observing the percentage plot, we see that married customers churn out the most.

There is definitely a difference in the churn percentages across the different categories.

Therefore,we shall assume that MaritalStatus might prove be a good predictor variable for our model.

### **Any complaint has been raised in last month : 'Complain'**

```python
df['Complain'].unique()
```

**Execution Output:**
```text
array([1, 0])
```

```python
df.Complain.value_counts()
```

**Execution Output:**
```text
0    4026
1    1604
Name: Complain, dtype: int64
```

```python
fig,ax = plt.subplots(figsize=(15,5))
ax=sns.countplot(x='Complain', data=df)
plt.title('Figure 36 : Distribution of the number of customers based on whehether they raised a complaint in the last month')
plt.show()
```

```python
fig,ax = plt.subplots(figsize=(15,5))
ax=sns.countplot(x='Complain', hue='Churn', data=df)
plt.title('Figure 37(a) : Distribution of the number of customers based on they raised a complaint in the last month by Churn value')
plt.show()

plotting_percentages(df, 'Complain', 'Churn', 37, df.Complain.unique())
```

**Execution Output:**
```text
<seaborn.axisgrid.FacetGrid at 0x7fc4e92422b0>
```

**OBSERVATIONS :**
- No. of cutomers who raised a complaint in the last month are lesser than those who have not.
- When categorized based on Churn value, while observing the percentage plot, we see that customers who have complained in the last month have churned out lesser compared to those who did not.

There is definitely a difference in the churn percentages across the different categories.

Therefore,we shall assume that Complain might prove be a good predictor variable for our model.

```python
logger.info('Data exploration ends!')
```

```python
logger.info('FILE ENDS RUNNING!')
```

---

## 3. Feature Engineering & Statistical Feature Selection

# **Import necessary libraries and Load data from database**

```python
import logging

logger = logging.getLogger()

file_handler = logging.FileHandler(filename='ecc_fe_log.log', mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)
logger.info('FILE STARTS RUNNING!')
```

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

import scipy.stats as stats
from scipy.stats import chi2_contingency

from pymongo import MongoClient

import warnings
warnings.filterwarnings('ignore')
```

```python
logger.info('Libraries imported!')
```

```python
# Connect to Mongodb cluster
client = MongoClient("mongodb+srv://<username>:<password>@mycluster.g3bp8fr.mongodb.net/?retryWrites=true&w=majority")

logger.info('Database connected!')

# List of databases
db_list = client.list_database_names()
db_list
```

**Execution Output:**
```text
['CHURN', 'loan_db', 'admin', 'local']
```

```python
db = client.CHURN
```

```python
cursor = db.ecomm_churn.find()

df = pd.DataFrame(list(cursor)).drop('_id', axis=1)
df.head()
```

**Execution Output:**
```text
CustomerID  Churn  Tenure PreferredLoginDevice  CityTier  WarehouseToHome  \
0       50001      1     4.0               Mobile         3              6.0   
1       50002      1    10.0               Mobile         1              8.0   
2       50003      1    10.0               Mobile         1             30.0   
3       50004      1     0.0               Mobile         3             15.0   
4       50005      1     0.0               Mobile         1             12.0   

  PreferredPaymentMode  Gender  HourSpendOnApp  NumberOfDeviceRegistered  \
0                   DC  Female             3.0                         3   
1                  UPI    Male             3.0                         4   
2                   DC    Male             2.0                         4   
3                   DC    Male             2.0                         4   
4                   CC    Male             3.0                         3   

  PreferedOrderCat  SatisfactionScore MaritalStatus  NumberOfAddress  \
0           Laptop                  2        Single                9   
1           Mobile                  3        Single                7   
2           Mobile                  3        Sing
... [Output truncated for brevity]
```

```python
logger.info('Data loaded from database!')
```

```python
df.shape
```

**Execution Output:**
```text
(5630, 20)
```

# **Feature Engineering**

```python
logger.info('Feature engineering starts!')
```

## **Outlier Handling**

Most of the outliers we observed during exploration of the data seems to represent the natural variation in the population(of the respective variable). Therefore, we leave them except for a few variables like Tenure, DaySinceLastOrder, CashbackAmount and NumberOfAddress.

 We handle them one by one.

**Tenure**

According to the percentile distribution of 'Tenure', we observe that customers with Tenure > 21, have not churned and the 99th percentile value is 31 which means the extreme values lies after that. So lets cap at the value 31, ie, all values above 31 will be considered as 31.

```python
percentile = df.Tenure.quantile([0.99]).values
df['Tenure'] = df['Tenure'].apply(lambda x : percentile[0] if x > percentile[0] else x)
```

**DaySinceLastOrder**

Similarly for DaySinceLastOrder, according to the percentile distribution, we see that values after DaySinceLastOrder=18 are extreme values [30,31,46]. The 99th percentile values is 15. So we shall cap at this position.

```python
percentile = df.DaySinceLastOrder.quantile([0.99]).values
df['DaySinceLastOrder'] = df['DaySinceLastOrder'].apply(lambda x : percentile[0] if x > percentile[0] else x)
```

**CashbackAmount**
Here we see that there are outliers after the upper bound and below the lower bound. We cap the values at the 1st and 99th percentile.

```python
percentile = df.CashbackAmount.quantile([0.01, 0.99]).values
df['CashbackAmount'] = df['CashbackAmount'].apply(lambda x : percentile[0] if x < percentile[0] else percentile[1] if x > percentile[1] else x)
```

## **Feature selection using Statistical Test**

We perform the following tests to select features that would contribute the best for our model.

```python
# Function to perform statistical test on numerical variables to determine whether to reject or accept H0
def num_stats(num_col):
  group_0 = df[df['Churn']==0][num_col]
  group_1 = df[df['Churn']==1][num_col]

  _, p_value = stats.ttest_ind(group_0,group_1,equal_var=False)

  print('P-value : ', p_value)
  if(p_value<0.05):
    print('Reject null hypothesis')
  else:
    print('Do not reject null hypotheis')
```

```python
def chisq_test(cat_col, df):
    CrossTabResult=pd.crosstab(index=df['Churn'], columns=df[cat_col])
    ChiSqResult = chi2_contingency(CrossTabResult)
        
    # If the ChiSq P-Value is <0.05, that means we reject H0
    if (ChiSqResult[1] < 0.05):
        print('P-Value :', ChiSqResult[1])
        print('Reject null hypothesis')
    else:
        print('P-Value :', ChiSqResult[1])
        print('Do not reject null hypotheis')
```

```python
num_col_list = ['Tenure', 'WarehouseToHome', 'OrderAmountHikeFromlastYear', 'CouponUsed', 'OrderCount',
                'DaySinceLastOrder', 'CashbackAmount', 'HourSpendOnApp', 'NumberOfDeviceRegistered', 'NumberOfAddress']
```

```python
for col in num_col_list:
  print('Column Name : ', col)
  num_stats(col)
  print('---------------------------------------------')
```

**Execution Output:**
```text
Column Name :  Tenure
P-value :  2.008277595367716e-202
Reject null hypothesis
---------------------------------------------
Column Name :  WarehouseToHome
P-value :  7.60206018025374e-09
Reject null hypothesis
---------------------------------------------
Column Name :  OrderAmountHikeFromlastYear
P-value :  0.4237779148876236
Do not reject null hypotheis
---------------------------------------------
Column Name :  CouponUsed
P-value :  0.9159384616337447
Do not reject null hypotheis
---------------------------------------------
Column Name :  OrderCount
P-value :  0.06430615371620459
Do not reject null hypotheis
---------------------------------------------
Column Name :  DaySinceLastOrder
P-value :  3.1021436368382634e-39
Reject null hypothesis
---------------------------------------------
Column Name :  CashbackAmount
P-value :  3.03484589898161e-43
Reject null hypothesis
---------------------------------------------
Column Name :  HourSpendOnApp
P-value :  0.14300103213870466
Do not reject null hypotheis
---------------------------------------------
Column Name :  NumberOfDeviceRegistered
P-value :  6.939036502330302e-16
Reject null hypothesis
---------------------------------
... [Output truncated for brevity]
```

```python
cat_col_list = ['PreferredLoginDevice', 'CityTier', 'PreferredPaymentMode',
                'PreferedOrderCat', 'SatisfactionScore', 'MaritalStatus', 'Gender', 'Complain']
```

```python
for col in cat_col_list:
  print('Column Name : ', col)
  chisq_test(col, df)
  print('---------------------------------------------')
```

**Execution Output:**
```text
Column Name :  PreferredLoginDevice
P-Value : 0.0001477040239947965
Reject null hypothesis
---------------------------------------------
Column Name :  CityTier
P-Value : 1.2612000812079956e-09
Reject null hypothesis
---------------------------------------------
Column Name :  PreferredPaymentMode
P-Value : 1.4978570960706217e-10
Reject null hypothesis
---------------------------------------------
Column Name :  PreferedOrderCat
P-Value : 3.11924340428766e-61
Reject null hypothesis
---------------------------------------------
Column Name :  SatisfactionScore
P-Value : 2.4233349782737515e-14
Reject null hypothesis
---------------------------------------------
Column Name :  MaritalStatus
P-Value : 1.073011277910542e-41
Reject null hypothesis
---------------------------------------------
Column Name :  Gender
P-Value : 0.030820940334890086
Reject null hypothesis
---------------------------------------------
Column Name :  Complain
P-Value : 2.6644609654641377e-78
Reject null hypothesis
---------------------------------------------
```

### **Drop unwanted columns based on the test results**

```python
df.drop(columns=['CustomerID', 'HourSpendOnApp', 'OrderAmountHikeFromlastYear', 'CouponUsed', 'OrderCount'], axis=1, inplace=True)
```

## **Encoding Categorical Variables**

```python
df_encoded = pd.get_dummies(df,columns=cat_col_list)
df_encoded.head()
```

**Execution Output:**
```text
Churn  Tenure  WarehouseToHome  NumberOfDeviceRegistered  NumberOfAddress  \
0      1     4.0              6.0                         3                9   
1      1    10.0              8.0                         4                7   
2      1    10.0             30.0                         4                6   
3      1     0.0             15.0                         4                8   
4      1     0.0             12.0                         3                3   

   DaySinceLastOrder  CashbackAmount  PreferredLoginDevice_Computer  \
0                5.0          159.93                              0   
1                0.0          120.90                              0   
2                3.0          120.28                              0   
3                3.0          134.07                              0   
4                3.0          129.60                              0   

   PreferredLoginDevice_Mobile  CityTier_1  ...  SatisfactionScore_3  \
0                            1           0  ...                    0   
1                            1           1  ...                    1   
2                            1           1  ...                    1   
3      
... [Output truncated for brevity]
```

```python
logger.info('Feature Engineering ends!')
```

# **Save the data in database**

```python
mydb = client.CHURN
```

```python
# Creating collection/table 'ecomm_churn_encoded' in CHURN database
mytb1 = mydb.ecomm_churn_encoded

# Convert df_encoded to dictionary
data = df_encoded.to_dict(orient='records') 

# Insert 'data' to ecomm_churn
mytb1.insert_many(data)
```

**Execution Output:**
```text
<pymongo.results.InsertManyResult at 0x7f68ac9a94f0>
```

```python
logger.info('Modified data saved in database!')
logger.info('FILE ENDS RUNNING!')
```

---

## 4. Model Training, Class Imbalance Handling & Serialization

# **Importing libraries and loading data from database**

```python
import logging

logger = logging.getLogger()

file_handler = logging.FileHandler(filename='ecc_model_log.log', mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)
logger.info('FILE STARTS RUNNING!')
```

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

from pymongo import MongoClient

from imblearn.over_sampling import SMOTE

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler
from sklearn import metrics

import warnings
warnings.filterwarnings('ignore')
```

```python
logger.info('Libraries imported!')
```

```python
# Connect to Mongodb cluster
client = MongoClient("mongodb+srv://<username>:<password>@mycluster.g3bp8fr.mongodb.net/?retryWrites=true&w=majority")

logger.info('Connected to database!')

# List of databases
db_list = client.list_database_names()
db_list
```

**Execution Output:**
```text
['CHURN', 'loan_db', 'admin', 'local']
```

```python
# List of collections/tables in 'CHURN'
mydb = client.CHURN
mydb.list_collection_names()
```

**Execution Output:**
```text
['ecomm_churn', 'ecomm_churn_bin_encoded', 'ecomm_churn_encoded', 'bank_churn']
```

```python
# Load 'ecomm_churn_encoded'
cursor = mydb.ecomm_churn_encoded.find()
df_e = pd.DataFrame(list(cursor)).drop('_id', axis=1)
```

```python
df_e.head()
```

**Execution Output:**
```text
Churn  Tenure  WarehouseToHome  NumberOfDeviceRegistered  NumberOfAddress  \
0      1   10.00            12.00                         3                5   
1      1    0.00            22.00                         5                2   
2      1   13.00             9.00                         4                2   
3      0    5.00            14.00                         3                2   
4      0    0.00            13.00                         4                3   

   DaySinceLastOrder  CashbackAmount  PreferredLoginDevice_Computer  \
0               2.00          120.73                              0   
1               7.00          139.19                              1   
2               2.00          126.83                              0   
3               7.00          189.98                              1   
4               0.00          161.32                              0   

   PreferredLoginDevice_Mobile  CityTier_1  ...  SatisfactionScore_3  \
0                            1           0  ...                    0   
1                            0           1  ...                    0   
2                            1           0  ...                    1   
3      
... [Output truncated for brevity]
```

```python
logger.info('Data loaded from database!')
```

# **Modeling**

```python
logger.info('Modeling starts!')
```

## **Handling imbalance**

```python
# Initialise SMOTE object
smote = SMOTE()
```

```python
# Separate independent and dependent variables
X = df_e.drop('Churn', axis=1)
y = df_e['Churn']
```

```python
# fit predictor and target variable
x_smote, y_smote = smote.fit_resample(X, y)
```

```python
# Combine balanced X and y
df_e = pd.DataFrame(x_smote, columns=df_e.drop('Churn', axis=1).columns)
df_e['Churn'] = y_smote

df_e.head()
```

**Execution Output:**
```text
Tenure  WarehouseToHome  NumberOfDeviceRegistered  NumberOfAddress  \
0    4.00             6.00                         3                9   
1   10.00             8.00                         4                7   
2   10.00            30.00                         4                6   
3    0.00            15.00                         4                8   
4    0.00            12.00                         3                3   

   DaySinceLastOrder  CashbackAmount  PreferredLoginDevice_Computer  \
0               5.00          159.93                              0   
1               0.00          120.90                              0   
2               3.00          120.28                              0   
3               3.00          134.07                              0   
4               3.00          129.60                              0   

   PreferredLoginDevice_Mobile  CityTier_1  CityTier_2  ...  \
0                            1           0           0  ...   
1                            1           1           0  ...   
2                            1           1           0  ...   
3                            1           0           0  ...   
4                     
... [Output truncated for brevity]
```

```python
df_e.Churn.value_counts()
```

**Execution Output:**
```text
1    4682
0    4682
Name: Churn, dtype: int64
```

## **Modeling using df_e**

### **Split train-test sets**

```python
# Separate dependent and independent variables
X = df_e.drop('Churn', axis=1)
y= df_e.Churn
```

```python
#standardise the x value by using standardscaler
scaler = StandardScaler()
X = scaler.fit_transform(X)
```

```python
# Split train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=.30,random_state =100)
```

```python
# Checking the target rate in the population, train sample and test sample
print("Population risk rate :", 
      round(sum(df_e.Churn)*100/len(df_e), 2),"%")
print("Train set risk rate :", 
      round(sum(y_train)*100/len(y_train), 2),"%")
print("Test set risk rate :", 
      round(sum(y_test)*100/len(y_test), 2),"%")
```

**Execution Output:**
```text
Population risk rate : 16.84 %
Train set risk rate : 17.25 %
Test set risk rate : 15.87 %
```

### **DecisionTreeClassifier**

```python
from sklearn.tree import DecisionTreeClassifier

# Training the model
dt_clf = DecisionTreeClassifier()
dt_clf.fit(X_train, y_train)
```

**Execution Output:**
```text
DecisionTreeClassifier()
```

```python
# Predictions on test data
y_pred = dt_clf.predict(X_test)
```

```python
# Evaluation metrics
print(metrics.classification_report(y_test, y_pred))
print(metrics.confusion_matrix(y_test, y_pred))
print('Accuracy :', metrics.accuracy_score(y_test, y_pred))
print('F1-score : ', metrics.f1_score(y_test, y_pred))
print('R2-score : ', metrics.r2_score(y_test, y_pred))
print('ROC-AUC Score :', metrics.roc_auc_score(y_test, y_pred))
```

**Execution Output:**
```text
precision    recall  f1-score   support

           0       0.98      0.97      0.98      1421
           1       0.86      0.89      0.87       268

    accuracy                           0.96      1689
   macro avg       0.92      0.93      0.92      1689
weighted avg       0.96      0.96      0.96      1689

[[1382   39]
 [  30  238]]
Accuracy : 0.9591474245115453
F1-score :  0.873394495412844
R2-score :  0.6939799594567626
ROC-AUC Score : 0.9303071202747697
```

```python
logger.info('Modeling ends!')
```

# **Save the model**

```python
import pickle

pickle.dump(dt_clf, open('churn.pkl', 'wb'))
```

```python
logger.info('Saved the model!')
logger.info('FILE ENDS RUNNING!')
```

---

## Production Pipeline Key Takeaways

1. **Handling Class Imbalance**:
   - In churn prediction, churners are often a small minority (e.g. 10-15%).
   - Using accuracy alone is misleading (predicting all 0s gives 85-90% accuracy).
   - Use techniques like **SMOTE (Synthetic Minority Over-sampling Technique)** or class-weighted loss functions (`class_weight='balanced'`), and evaluate using **ROC-AUC, Precision, Recall, and F1-Score**.
2. **Statistical Feature Selection**:
   - Continuous features vs Binary Churn target: Two-sample t-test or Mann-Whitney U test.
   - Categorical features vs Binary Churn target: Chi-Square ($\chi^2$) test of independence.
   - Discard features that show no statistically significant relationship ($p > 0.05$).
3. **Artifact Serialization**:
   - Serialize the final pipeline using `pickle` or `joblib`. Ensure all preprocessing transformers (scalers, encoders) are bundled into the pipeline to prevent data leakage during serving.
