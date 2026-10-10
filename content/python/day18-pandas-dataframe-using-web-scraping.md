# Day 18: Web Scraping to Pandas DataFrames with BeautifulSoup

Master extracting structured tabular data from raw HTML webpages into Pandas DataFrames: bypassing HTTP 403 Forbidden with custom `User-Agent` headers, DOM traversal with `BeautifulSoup`, container-based extraction, missing data handling, and large-scale multi-page crawling.

---

## 1. Complete Hands-on Guide: Web Scraping to DataFrame

# Pandas DataFrame using Web Scraping

This notebook shows how to scrape company data from a website, extract useful fields, and convert the collected information into a pandas DataFrame.

## 1. Import required libraries
Definition: We need `requests` to fetch the webpage, `BeautifulSoup` to parse HTML, `pandas` to create a DataFrame, and `numpy` for missing values.

```python
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
```

Example output:
```text
# No visible output, just libraries are imported.
```

## 2. Handle 403 forbidden response
Definition: Some websites block bots. A user-agent header helps mimic a browser request.

```python
headers = {'User-Agent': 'Mozilla/5.0'}
requests.get('url', headers=headers).text
```

Example output:
```text
<html> ... webpage content ... </html>
```

## 3. Load the webpage
Definition: Fetch the HTML content of the target page and parse it with BeautifulSoup.

```python
webpage = requests.get('https://www.ambitionbox.com/list-of-companies?page=1').text
soup = BeautifulSoup(webpage, 'lxml')
```

Example output:
```text
# HTML content is loaded and ready to parse.
```

## 4. Find page title
Definition: We can inspect the page’s HTML structure and fetch the first heading.

```python
soup.find_all('h1')[0].text
```

Example output:
```text
'List of companies'
```

## 5. Extract company names
Definition: Use HTML tags such as `h2` to identify company names in the page.

```python
for i in soup.find_all('h2'):
    print(i.text.strip())
```

Example output:
```text
TCS
Infosys
Wipro
Accenture
```

## 6. Extract ratings
Definition: Ratings are present in specific HTML tags and classes. We can count or extract them.

```python
len(soup.find_all('p', class_='rating'))
```

Example output:
```text
25
```

## 7. Extract review counts
Definition: Review count is often stored inside anchor tags with a specific class.

```python
len(soup.find_all('a', class_='review-count'))
```

Example output:
```text
25
```

## 8. Consider the whole container
Definition: Each company card is usually inside a `div` container. We can loop through each container to collect all attributes.

```python
company = soup.find_all('div', class_='company-content-wrapper')
```

Example output:
```text
[<div class="company-content-wrapper">...</div>, ...]
```

## 9. Build a DataFrame from one page
Definition: For each company card, extract name, rating, reviews, and company metadata, then store them in a dictionary and create a DataFrame.

```python
name=[]
rating=[]
reviews=[]
ctype=[]
hq=[]
how_old=[]
no_of_employee=[]

for i in company:
    name.append(i.find('h2').text.strip())
    rating.append(i.find('p', class_='rating').text.strip())
    reviews.append(i.find('a', class_='review-count').text.strip())
    ctype.append(i.find_all('p', class_='infoEntity')[0].text.strip())
    hq.append(i.find_all('p', class_='infoEntity')[1].text.strip())
    how_old.append(i.find_all('p', class_='infoEntity')[2].text.strip())
    no_of_employee.append(i.find_all('p', class_='infoEntity')[3].text.strip())


df = pd.DataFrame({
    'name': name,
    'rating': rating,
    'reviews': reviews,
    'company_type': ctype,
    'Head_Quarters': hq,
    'Company_Age': how_old,
    'No_of_Employee': no_of_employee,
})
```

Example output:
```text
           name  rating  reviews     company_type   Head_Quarters   Company_Age   No_of_Employee
0        TCS     3.8     14.3k+    IT Services     Mumbai          55 years      1 Lakh+
```

## 10. Scrape many pages
Definition: Loop through multiple pages and append each page’s extracted data into one final DataFrame.

```python
final = pd.DataFrame()
for j in range(1, 1001):
    webpage = requests.get('https://www.ambitionbox.com/list-of-companies?page={}'.format(j)).text
    soup = BeautifulSoup(webpage, 'lxml')
    company = soup.find_all('div', class_='company-content-wrapper')
    # extract data and append to final
```

Example output:
```text
# The final DataFrame grows as more pages are processed.
```

## 11. Save and inspect final data
Definition: After collecting all company records, check the shape and sample rows.

```python
final.shape
df.sample(5)
```

Example output:
```text
(10000, 7)

         name  rating   reviews  company_type  Head_Quarters  Company_Age  No_of_Employee
123   Infosys   3.9     12.8k+   IT Services    Bengaluru     42 years     1 Lakh+
```

---

### Summary
Web scraping helps extract useful information from webpages when the data is not available in CSV or API format. By parsing HTML with BeautifulSoup and organizing it into a pandas DataFrame, we can analyze the data efficiently.

```python
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
```

# if response code is 403
 - headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
 -requests.get('url',headers=headers).text

```python
webpage=requests.get('https://www.ambitionbox.com/list-of-companies?page=1').text
```

```python
soup=BeautifulSoup(webpage,'lxml')
```

```python
#print(soup.prettify())
```

```python
soup.find_all('h1')[0].text
```

**Execution Output:**
```text
'List of companies in India'
```

# TO FIND OUT NAMES OF THE COMPANIES

```python
for i in soup.find_all('h2'):
  print(i.text.strip())
```

**Execution Output:**
```text
TCS
Accenture
ICICI Bank
Cognizant
HDFC Bank
Capgemini
Tech Mahindra
HCL Technologies
L&T
Infosys
Tata Motors
IBM
Genpact
Reliance jio
Axis Bank
Wipro
Concentrix Corporation
HDB Financial Services
Vodafone
Bharti Airtel
Kotak Mahindra Bank
Amazon
Reliance
Bajaj Finserv
IndusInd Bank
Indian Army
Teleperformance
Hinduja Global Solutions
Samsung
Mahindra & Mahindra
```

```python
for i in soup.find_all('p'):
  print(i.text.strip())
```

**Execution Output:**
```text
Company Overview
477,887 unique
			companies found
Sort By:
Popular
3.9
Public
Mumbai + 164 more
52 years old
10000+ employees
Tata Consultancy Services is an IT services, consulting and business solutions organisation that has been partnering with the world’s largest businesses in their transformation journeys for the last 50 years. 

A part of the Tata group, India's largest multinational business group, TCS has over 436,000 of the world’s best-trained consultants in 46 countries. The company is listed on the BSE (formerly Bombay Stock Exchange) and the NSE (National Stock Exchange) in India. 

TCS'​ proactive stance on climate change and award winning work with communities across the world have earned it a place in leading sustainability indices such as the Dow Jones Sustainability Index (DJSI), MSCI Global Sustainability Index and the FTSE4Good Emerging Index.
4.0
Private
Dublin + 98 more
31 years old
10000+ employees
Accenture is a leading global professional services company, providing a broad range of services and solutions in strategy, consulting, digital, technology and operations. Combining unmatched experience and specialized skills across more than 40 industries and all business functions – underpinned by the world’s largest delivery network – Accenture works at the intersection of business and technology to help clients improve their performance and create sustainable value for their stakeholders. With 449,000 people serving clients in more than 120 countries, Ac
... [Output truncated for brevity]
```

```python
#for in soup.find_all('p'):
  #print(i.text.strip())
```

## TO FIND OUT THE RATINGS

```python
len(soup.find_all('p',class_='rating'))
```

**Execution Output:**
```text
30
```

## TO FIND OUT THE NUMBER OF REVIEWS

```python
len(soup.find_all('a' , class_='review-count'))
```

**Execution Output:**
```text
30
```

# CONSIDERING THE WHOLE CONTAINER

```python
company=soup.find_all('div',class_='company-content-wrapper')
```

```python
len(company)
```

**Execution Output:**
```text
30
```

```python
name=[]
rating=[]
reviews=[]
ctype=[]
hq=[]
how_old=[]
no_of_employee=[]

for i in company:

  name.append(i.find('h2').text.strip())
  rating.append(i.find('p',class_='rating').text.strip())
  reviews.append(i.find('a' , class_='review-count').text.strip())
  ctype.append(i.find_all('p',class_='infoEntity')[0].text.strip())
  hq.append(i.find_all('p',class_='infoEntity')[1].text.strip())
  how_old.append(i.find_all('p',class_='infoEntity')[2].text.strip())
  no_of_employee.append(i.find_all('p',class_='infoEntity')[3].text.strip())

df=pd.DataFrame({'name':name,
   'rating':rating,
   'reviews':reviews,
   'company_type':ctype,
   'Head_Quarters':hq,
   'Company_Age':how_old,
   'No_of_Employee':no_of_employee,
   })
```

```python
name
```

**Execution Output:**
```text
['TCS',
 'Accenture',
 'ICICI Bank',
 'Cognizant',
 'HDFC Bank',
 'Capgemini',
 'Tech Mahindra',
 'HCL Technologies',
 'L&T',
 'Infosys',
 'Tata Motors',
 'IBM',
 'Genpact',
 'Reliance jio',
 'Axis Bank',
 'Wipro',
 'Concentrix Corporation',
 'HDB Financial Services',
 'Vodafone',
 'Bharti Airtel',
 'Kotak Mahindra Bank',
 'Amazon',
 'Reliance',
 'Bajaj Finserv',
 'IndusInd Bank',
 'Indian Army',
 'Teleperformance',
 'Hinduja Global Solutions',
 'Samsung',
 'Mahindra & Mahindra']
```

```python
rating
```

**Execution Output:**
```text
['3.9',
 '4.0',
 '4.1',
 '3.9',
 '4.0',
 '3.4',
 '3.6',
 '3.7',
 '4.2',
 '3.9',
 '4.1',
 '4.1',
 '4.0',
 '4.0',
 '4.0',
 '3.8',
 '4.0',
 '4.0',
 '4.2',
 '4.2',
 '3.8',
 '4.1',
 '4.2',
 '4.1',
 '3.6',
 '4.7',
 '3.7',
 '3.8',
 '4.2',
 '4.2']
```

```python
reviews
```

**Execution Output:**
```text
['17.1k Reviews',
 '15k Reviews',
 '13.8k Reviews',
 '12.9k Reviews',
 '12k Reviews',
 '10k Reviews',
 '9.8k Reviews',
 '9.2k Reviews',
 '9.1k Reviews',
 '8.7k Reviews',
 '8.6k Reviews',
 '8.5k Reviews',
 '8.3k Reviews',
 '8.3k Reviews',
 '8.3k Reviews',
 '7.3k Reviews',
 '7.3k Reviews',
 '6.2k Reviews',
 '5.7k Reviews',
 '5.7k Reviews',
 '5.7k Reviews',
 '5.6k Reviews',
 '4.8k Reviews',
 '4.1k Reviews',
 '3.9k Reviews',
 '3.9k Reviews',
 '3.8k Reviews',
 '3.8k Reviews',
 '3.6k Reviews',
 '3.6k Reviews']
```

```python
ctype
```

**Execution Output:**
```text
['Public',
 'Private',
 'Public',
 'Private',
 'Public',
 'Private',
 'Public',
 'Public',
 'Public',
 'Public',
 'Public',
 'Private',
 'Private',
 'Public',
 'Public',
 'Public',
 'Public',
 'Private',
 'Public',
 'Public',
 'Public',
 'Private',
 'Public',
 'Public',
 'Public',
 'Govt agency',
 'Private',
 'Public',
 'Private',
 'Public']
```

```python
hq
```

**Execution Output:**
```text
['Mumbai + 164 more',
 'Dublin + 98 more',
 'Mumbai + 743 more',
 'Teaneck + 46 more',
 'Mumbai + 729 more',
 'Paris + 45 more',
 'Pune + 160 more',
 'Noida + 111 more',
 'Mumbai + 337 more',
 'Bangalore + 68 more',
 'Pune + 344 more',
 'New York + 73 more',
 'New York + 31 more',
 'Navi Mumbai + 606 more',
 'Mumbai + 670 more',
 'Bangalore + 123 more',
 'Fremont + 39 more',
 'Ahmedabad + 463 more',
 'Berkshire + 364 more',
 'New Delhi + 347 more',
 'Mumbai + 361 more',
 'Washington + 182 more',
 'Mumbai + 216 more',
 'Pune + 478 more',
 'Mumbai + 365 more',
 'New Delhi + 211 more',
 'Paris + 45 more',
 'Bangalore + 52 more',
 'Seoul + 292 more',
 'Mumbai + 268 more']
```

```python
how_old
```

**Execution Output:**
```text
['52 years old',
 '31 years old',
 '26 years old',
 '26 years old',
 '26 years old',
 '53 years old',
 '34 years old',
 '14 years old',
 '82 years old',
 '39 years old',
 '75 years old',
 '109 years old',
 '23 years old',
 '10 years old',
 '27 years old',
 '75 years old',
 '37 years old',
 '13 years old',
 '38 years old',
 '25 years old',
 '17 years old',
 '26 years old',
 '54 years old',
 '13 years old',
 '26 years old',
 '125 years old',
 '42 years old',
 '20 years old',
 '82 years old',
 '75 years old']
```

```python
no_of_employee
```

**Execution Output:**
```text
['10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees',
 '10000+ employees']
```

```python
df.shape
```

**Execution Output:**
```text
(30, 7)
```

# creating dataframe for all the pages

```python
final=pd.DataFrame()
for j in range(1,1001):
  webpage=requests.get('https://www.ambitionbox.com/list-of-companies?page={}'.format(j)).text
  soup=BeautifulSoup(webpage,'lxml')
  company=soup.find_all('div',class_='company-content-wrapper')
  name=[]
  rating=[]
  reviews=[]
  ctype=[]
  hq=[]
  how_old=[]
  no_of_employee=[]

  for i in company:

    try:
       name.append(i.find('h2').text.strip())
    except:
       name.append(np.nan)

    try:
       rating.append(i.find('p',class_='rating').text.strip())
    except:
       rating.append(np.nan)
   
    try:

      reviews.append(i.find('a' , class_='review-count').text.strip())
    except:
      reviews.append(np.nan)

    try:

      ctype.append(i.find_all('p',class_='infoEntity')[0].text.strip())
    except:
      ctype.append(np.nan)
    try:

      hq.append(i.find_all('p',class_='infoEntity')[1].text.strip())
    except:
      hq.append(np.nan)
    
    try:

      how_old.append(i.find_all('p',class_='infoEntity')[2].text.strip())
    except:
      how_old.append(np.nan)
    try:
      no_of_employee.append(i.find_all('p',class_='infoEntity')[3].text.strip())
    except:
      no_of_employee.append(np.nan)
    

  df=pd.DataFrame({'name':name,
    'rating':rating,
    'reviews':reviews,
    'company_type':ctype,
    'Head_Quarters':hq,
    'Company_Age':how_old,
    'No_of_Employee':no_of_employee,
    })
  
  final=final.append(df,ignore_index=True)
```

```python
df.sample(5)
```

**Execution Output:**
```text
name rating  ...    Company_Age    No_of_Employee
2               Bank of America    4.3  ...   22 years old  10000+ employees
22               R.R. Donnelley    4.1  ...  156 years old  10000+ employees
11  Mahindra Holidays & Reso...    3.9  ...   24 years old  10000+ employees
23  GVK Emergency Management...    3.9  ...   15 years old  10000+ employees
9            Itc Infotech India    3.4  ...   20 years old  10000+ employees

[5 rows x 7 columns]
```

```python
df.shape
```

**Execution Output:**
```text
(30, 7)
```

```python
final.shape
```

**Execution Output:**
```text
(30000, 7)
```
---

## Key Interview Concepts: Web Scraping & Data Extraction

### 1. Overcoming HTTP 403 Forbidden
Many web servers block requests without browser user-agent headers:
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
```

### 2. Container-Based Parsing Pattern
**Crucial Rule**: Never extract fields as separate parallel lists (e.g. `soup.find_all('h2')` and `soup.find_all('p', class_='rating')`) if some cards might be missing a rating! If card 3 lacks a rating, the lists will misalign and shift every subsequent record.

**The Container Pattern**:
Find each parent container element, and extract fields within that container scope:
```python
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

soup = BeautifulSoup(webpage_html, 'lxml')
containers = soup.find_all('div', class_='company-content-wrapper')

records = []
for card in containers:
    name_el = card.find('h2')
    rating_el = card.find('p', class_='rating')
    reviews_el = card.find('a', class_='review-count')
    
    records.append({
        'name': name_el.text.strip() if name_el else np.nan,
        'rating': float(rating_el.text.strip()) if rating_el else np.nan,
        'reviews': reviews_el.text.strip() if reviews_el else '0',
    })

df = pd.DataFrame(records)
```

### 3. Ethical Scraping & Rate Limiting
- Inspect `robots.txt` before scraping.
- Introduce `time.sleep(1)` between requests to avoid overwhelming target servers.
- Use session connection pooling: `session = requests.Session()`.
