# Hypothesis Testing & Statistical Inference

Detailed theoretical foundations and hands-on Python implementations of statistical hypothesis testing: Null ($H_0$) and Alternative ($H_1$) hypotheses, Type I & Type II errors, significance level ($\alpha$), p-value interpretation, degrees of freedom, confidence intervals, One-Sample t-test, Two-Sample independent t-test, and Paired t-test using `scipy.stats`.

---

## 🔬 Theoretical Foundations of Hypothesis Testing

### Slide 1: Hypothesis Testing



---

### Slide 2: What is Hypothesis

• Hypothesis is a propositional statement to assume somethings or certain occurrences without the supporting empirical evidence yet.

• Example:

• Bankers assumed high income earners are more profitable than low-income earners.

• No changes in patient health after taking medicine

• Introduction of basic terms

• Population : The group of individuals under consideration.

• Sample : A finite subset of population.

• Population Parameter : A characteristic of population, e.g., population mean µ

• Sample Statistic : A function of sample observations which is calculated from the data in the sample, e.g., sample mean ()

---

### Slide 3: Null and Alternative hypothesis

• Null Hypothesis:

• Hypothesis to be tested which is usually a hypothesis of no difference, is called null hypothesis and is usually denoted by H0.

• Alternative Hypothesis:

• Any hypothesis which is complementary to the null hypothesis is called an alternative hypothesis, usually denoted by H1.

• Example:

• If we want to test the null hypothesis that the population has a specific mean 1000. Then the alternative hypothesis could be population mean ≠ µ0

• Null hypothesis,  H0 : µ=  1000

• Alternative hypothesis,  H1: µ≠  1000

---

### Slide 4: Errors in Hypothesis testing

• In practice, type I error is amount to reject a lot when it is good and type II error is accepting the lot when it is bad.

---

### Slide 5: P-value

• When we perform a hypothesis test in statistics, a p-value helps us to determine the significance of our results. All hypothesis tests ultimately use a p-value to weigh the strength of the evidence (what the data are telling you about the population). The p-value is a number between 0 and 1 and interpreted in the following way:

• A small p-value (typically ≤ 0.05) indicates strong evidence against the null hypothesis, so you reject the null hypothesis.

• A large p-value (> 0.05) indicates weak evidence against the null hypothesis, so you fail to reject the null hypothesis.

---

### Slide 6: Confidence level and Confidence Interval

• A Confidence Interval is an interval of numbers containing the most plausible values for our Population Parameter.

• The probability that this procedure produces an interval that contains the actual true parameter value is known as the Confidence Level and is generally chosen to be 0.90, 0.95 or 0.99.

• For example, if we found that the height of college boys lies between interval (4.5 to 6) then this will be our confidence interval and if we check the particular then 95% chance that a height of boy lie between this interval.

• The level of confidence determines the z critical value.

• 99%  2.58

• 95%  1.96

• 90%  1.645

---

### Slide 7: Example for confidence interval

• What is the average age of robbery victims in Chicago last year?

• Randomly sample 100 police reports of Chicago robberies last year. So, n = 100.Record the ages of the victims, add them all up, and divide by 100 to get the mean. Let's say the mean age in this case is 34.25 years.Utilizing a 95% CL, which has a standard z value of 1.96, calculate the standard deviation. With a mean of 34.25 and a standard deviation is 15.

• Now we can calculate CI by using above formula.

• Our CI is 34.25 ± 2.94, or   31.31 to 37.19.

• We can now say with 95% confidence, that if the true average age of all Chicago robbery victims last year was known, it would fall between 31.31 and 37.19 years of age.

---

### Slide 8: t-test for single mean

• Suppose we want to test:

• If a random sample xi (i = 1, 2, …, n) of size n has been drawn from a normal- population with a specified mean, say µo, or

• If the sample mean differs significantly from the, hypothetical µo  of the population mean.

• Under the null hypothesis Ho :

• (i)The sample has been drawn from the population with mean µ0

• Or (ii) there is no significance difference between sample mean ͞x and the population mean µ0 .

• The statistics

• Where

• Follows the student’s t-distribution with (n-1) degree of freedom.

---

### Slide 9: Example

• A random sample of 10 boys had the following I.Q.' s : 70, 120, 110, 101, 88, 83, 95, 98, 107, 100. Do these data support the assumption of a population mean I.Q. of 100 ? Find a reasonable range in which most of the mean I.Q. values of samples of 10 boys lie.

• Solution:

• Step(i): Set statistical hypothesis

• Null hypothesis, H0: The mean I.Q is 100, i.e., µ=100.

• Alternative hypothesis, H1: µ≠100.

• Step(ii): use appropriate test statistics.

• Under Ho. the test statistic is :

---

### Slide 10: Calculation for t-statistics and confidence interval:

• X

• (X-͞x)

• (X-͞x)2

• 70

• -27.2

• 739.84

• 120

• 22.8

• 519.84

• 110

• 12.8

• 163.84

• 101

• 3.8

• 14.44

• 88

• -9.2

• 84.64

• 83

• -14.2

• 201.64

• 95

• -2.2

• 4.84

• 98

• 0.8

• 0.64

• 107

• 9.8

• 96.04

• 100

• 2.8

• 7.84

• Total: 972

• 1833.60

• ͞x = 972/10 = 97.2

• S = (1833.60/9) 1/2 =14.27

• S/(n)½ = 14.27/(10) ½ = 4.51

• |t| = |97.2 -100|/ 4.51

• Calculated value of t = 0.62

• Confidence interval:

• = 97.2 ± 2.262 × 4.514

• (86.99 , 107.41)

• Tabulated value of t0.05 for degree of freedom 9 at 5% significance level (0.05) is 2.262.

• Since the calculated value is less than the tabulated value, we may conclude that the data is consistent with the assumption of mean I.Q. of 100 in the population.

---

### Slide 11: t-test using Python

• Python output:

• From above result we get p-value>0.05

• So here we conclude that we are unable to reject the null hypothesis. i.e., the mean I.Q. will be 100 in population.

---

### Slide 12: t-test for difference of means

• Suppose, we are having two independent samples and we want to check :

• The two samples come from the same population or different population.

• The null hypothesis in this case : H0 : µ1 = µ2

• Alternative hypothesis : H1 : µ1 ≠ µ2

• Where µ1 & µ2 are the corresponding means.

• For example, we want to test that which method of study

• is better from two methods available. We take two samples

• Of students studied from different methods i.e., online study

• And by tutor.

• Here H0 : there is no difference between two method of

• Studies.

• And H1 : there is difference between two method of studies.

---

### Slide 13: … Continued

• Test statistics,

• Where,

• S2 is an unbiased estimate of the common population variance σ2.

---

### Slide 14: Paired t-test

• Let us now consider the case when,

• (i) The sample size are equal. i.t .. n1 = n2 = n (say) and

• (ii) the two samples are dependent and the sample observations are paired together. i.e .

• The problem is to test if the sample means differ significantly or not.

• For example :To test the efficiency of particular drug

• For this we will take reading of patient before giving the drug and after giving the drug respectively.

• Let xi and yi (i= 1,2, …,n) be readings. here we apply the paired t-test given below.

• Here we consider the increments, di= xi – yi ,(i= 1,2, …,n)

• Under null hypothesis, H0 : drug is not responsible for these increments.

• and Alternative hypothesis, H1 : drug is responsible for these increments.

• the statistic,

• Follows student’s t-distribution with (n-1) degree of freedom.

---

### Slide 15: THANK YOU FOR YOURATTENTATION




---

## 🐍 Hands-on Hypothesis Testing in Python with SciPy


```python
from scipy.stats import ttest_ind,ttest_1samp,ttest_rel
import numpy as np
```

Q.1 Below are given the gain in weights (in lbs.) of dogs fed on two diets A and B. 
<br> Gain in weight <br>
Diet A	25	32	30	24	14	32	24	30	31	35	25 <br>
Diet B	44	34	22	10	47	31	40	30	32	35	18	21	35	29	22 <br>
Test, if the two diets differs significantly as regards their effect on increase in weight.

**H0 =  two diets are not differs significantly as regards their effect on increase in weight.** <br>
**Ha =  two diets differs significantly as regards their effect on increase in weight.**

```python
diet_a = [ 25,32 ,30 ,24 ,14 ,32 ,24 ,30 ,31, 35, 25]
diet_b = [44, 34, 22, 10, 47, 31, 40, 30, 32, 35, 18, 21, 35, 29, 22]
```

```python
if np.var(diet_a)!=np.var(diet_b):
    print("Variance of both sample are different")
else:
    print("Variance are same for both of the samples")
```

**Output:**
```text
Variance of both sample are different
```

```python
statistics,p_value = ttest_ind(diet_a, diet_b,equal_var=False,alternative='less')
```

```python
alpha = 0.01
```

```python
if p_value > alpha:
    print('p_value is greater than alpha value, so we accept the null hypothesis')
else:
    print('p_value is smaller than alpha value, so we reject the null hypothesis')
```

**Output:**
```text
p_value is greater than alpha value, so we accept the null hypothesis
```

# *----------

Q.2 A certain stimulus administered to each of the 12 patients resulted in the following increase of blood pressure: <br>
                  5,2,8,-1, 3,0, -2,1,5, 0, 4 and 6 <br>
Can it be concluded that the stimulus will, in general. be accompanied by an increase in blood pressure? <br>

**Ho : u = 0 i.e. assuming that the stimulus will not be accompanied by an increase in blood pressure.** <br>
**Ha : u != 0 i.e. assuming that the stimulus will accompanied by an increase in blood pressure.** <br>

```python
samp = [5,2,8,-1, 3,0, -2,1,5, 0, 4, 6]
```

```python
statistics,p_value = ttest_1samp(samp,0)
```

```python
alpha = 0.05
```

```python
if p_value > alpha:
    print('p_value is greater than alpha value, so we accept the null hypothesis')
else:
    print('p_value is smaller than alpha value, so we reject the null hypothesis')
```

**Output:**
```text
p_value is smaller than alpha value, so we reject the null hypothesis
```

Q.3 The scores of 10 candidates prior and after training are given below: <br>
Prior: 84 48 36 37 54 69 83 96 90 65 <br>
After: 90 58 56 49 62 81 84 86 84 75 <br>
Is the training effective? <br>

**H0: training is not effective** <br>
**Ha: training is effective**

```python
prior = [84, 48, 36, 37, 54, 69, 83, 96, 90, 65]
after = [90 ,58 ,56 ,49 ,62 ,81, 84, 86, 84, 75]
```

```python
np.var(prior),np.var(after)
```

**Output:**
```text
(430.75999999999993, 197.65)
```

```python
statistics,p_value = ttest_rel(prior,after,alternative='less')
```

```python
statistics
```

**Output:**
```text
-2.2149620448940843
```

```python
alpha = 0.05
```

```python
if p_value > alpha:
    print('p_value is greater than alpha value, so we accept the null hypothesis')
else:
    print('p_value is smaller than alpha value, so we reject the null hypothesis')
```

**Output:**
```text
p_value is smaller than alpha value, so we reject the null hypothesis
```

Q.4 Two independent samples of 8 and 7 items respectively had the following values <br>
**Sample I** :   9 11 13 11 15 9 12 14 <br>
**Sample II** : 19 12 10 14 9 8 10 <br>

**H0:  There is no significant difference between the means of samples.** <br>
**Ha: There is significant difference between the means of samples.**

```python
sample_1 = [9, 11, 13, 11, 15, 9 ,12, 14]
sample_2 = [19, 12, 10, 14, 9 ,8 ,10]
```

```python
statistics,p_value = ttest_ind(prior,after,equal_var=False)
```

```python
alpha = 0.01
```

```python
if p_value > alpha:
    print('p_value is greater than alpha value, so we accept the null hypothesis')
else:
    print('p_value is smaller than alpha value, so we reject the null hypothesis')
```

**Output:**
```text
p_value is greater than alpha value, so we accept the null hypothesis
```

```python
statistics
```

**Output:**
```text
-0.7539460330218664
```

```python
p_value
```

**Output:**
```text
0.46195497014332476
```


---

## 📋 Hypothesis Testing Exercises & Practice Problems


Exercise

Q.1 Below are given the gain in weights (in lbs.) of dogs fed on two diets A and B.

Gain in weight

Diet A

25

32

30

24

14

32

24

30

31

35

25

Diet B

44

34

22

10

47

31

40

30

32

35

18

21

35

29

22

Test, if the two diets differs significantly as regards their effect on increase in weight.

Explain which test will be using and why.

Q.2 A certain stimulus administered to each of the 12 patients resulted in the following increase of blood pressure:

5,2,8,-1, 3,0, -2,1,5, 0, 4 and 6

Can it be concluded that the stimulus will, in general. be accompanied by an increase in blood pressure? And explain which test should be use and why.

Q.3 The scores of 10 candidates prior and after training are given below:

Prior: 84 48 36 37 54 69 83 96 90 65

After: 90 58 56 49 62 81 84 86 84 75

Is the training effective? explain which test should be use and why.

Q.4 Two independent samples of 8 and 7 items respectively had the following values

Sample I :   9 11 13 11 15 9 12 14

Sample II : 19 12 10 14 9 8 10

explain which test should be use and why.

Q.5: Use Given dataset and perform ANOVA and Chi-Square test, Explain why and when we use this test.