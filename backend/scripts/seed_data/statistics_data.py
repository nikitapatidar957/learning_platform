"""
Statistics & Probability Topics and Lessons Seed Data
Incorporating concepts from:
- 3. Descriptive Statistics
- 4. Hypothesis_testing
- 5. Graphical_analysis
"""

STATISTICS_TOPICS = [
    {
        "subjectSlug": "statistics",
        "title": "Descriptive Statistics & Data Distributions",
        "slug": "descriptive-statistics-theory",
        "description": "Population vs sample, qualitative vs quantitative data, measures of central tendency, dispersion (variance, std dev, IQR), skewness, and kurtosis.",
        "order": 1,
        "isPublished": True,
    },
    {
        "subjectSlug": "statistics",
        "title": "Probability Theory & Mathematical Statistics",
        "slug": "probability-foundations",
        "description": "Random experiments, sample space, trial & events, mutually exclusive events, independent events, conditional probability, and Bayes Theorem.",
        "order": 2,
        "isPublished": True,
    },
    {
        "subjectSlug": "statistics",
        "title": "Hypothesis Testing & Statistical Inference",
        "slug": "hypothesis-testing-inference",
        "description": "Null (H0) vs Alternative (H1) hypotheses, Type I & Type II errors, p-values, significance level, One-Sample, Two-Sample, and Paired t-tests.",
        "order": 3,
        "isPublished": True,
    },
    {
        "subjectSlug": "statistics",
        "title": "Correlation & Graphical Data Analysis",
        "slug": "correlation-graphical-analysis",
        "description": "Univariate, bivariate, and multivariate analysis, Pearson & Spearman correlation coefficients, covariance, scatter plots, and boxplot outlier detection.",
        "order": 4,
        "isPublished": True,
    },
]

STATISTICS_LESSONS = [
    # -------------------------------------------------------------------------
    # Topic 1: Descriptive Statistics
    # -------------------------------------------------------------------------
    {
        "topicSlug": "descriptive-statistics-theory",
        "subjectSlug": "statistics",
        "title": "Data Types, Central Tendency & Dispersion",
        "slug": "data-types-central-tendency-dispersion",
        "description": "Qualitative vs quantitative data (discrete vs continuous), calculation of Mean, Median, Mode, Variance, Standard Deviation, and IQR.",
        "estimatedTime": "35 mins",
        "difficulty": "Beginner to Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Qualitative vs Quantitative Data",
                    "content": (
                        "• Qualitative (Categorical) Data: Cannot be measured or counted numerically. Sorted by categories (e.g., blood group, gender, nationality, hair color).\n\n"
                        "• Quantitative Data: Expressed in numerical values suitable for mathematical and statistical analysis.\n"
                        "  - Discrete Data: Distinct, separate integers/whole numbers (e.g., number of students in a class, number of cars, days in a week).\n"
                        "  - Continuous Data: Continuous scale measurements with infinite possible values within an interval (e.g., height, weight, temperature, salary)."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Measures of Central Tendency & Robustness to Outliers",
                    "content": (
                        "1. Mean (Average): $\\bar{X} = \\frac{\\sum X}{N}$. Highly sensitive to extreme outlier values.\n\n"
                        "2. Median: Middle value of a sorted dataset. If $N$ is odd: element at $\\frac{N+1}{2}$. If $N$ is even: average of $\\frac{N}{2}$ and $\\frac{N}{2}+1$. Robust to outliers.\n\n"
                        "3. Mode: The value that occurs most frequently. A distribution can be unimodal, bimodal, or multimodal."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Skewness & Distribution Shapes",
                    "content": (
                        "• Symmetrical (Normal Distribution): $\\text{Mean} = \\text{Median} = \\text{Mode}$. Skewness $\\approx 0$.\n\n"
                        "• Positively Skewed (Right-tailed): Tail stretches towards high values. Mass of data is on the left. $\\text{Mean} > \\text{Median} > \\text{Mode}$ (e.g., Household Income Distribution).\n\n"
                        "• Negatively Skewed (Left-tailed): Tail stretches towards low values. Mass of data is on the right. $\\text{Mean} < \\text{Median} < \\text{Mode}$."
                    )
                },
                {
                    "type": "code",
                    "title": "Computing Descriptive Metrics in Python",
                    "language": "python",
                    "code": (
                        "import numpy as np\n"
                        "from scipy import stats\n\n"
                        "data = [12, 15, 12, 10, 18, 20, 12, 14, 15, 100]  # Note outlier 100\n\n"
                        "print('Mean:', np.mean(data))                     # 21.8 (distorted by 100)\n"
                        "print('Median:', np.median(data))                 # 14.5 (resistant to outlier)\n"
                        "print('Mode:', stats.mode(data).mode)             # 12\n"
                        "print('Standard Deviation:', np.std(data))        # 26.25\n"
                        "print('IQR:', stats.iqr(data))                    # 4.5"
                    )
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic 2: Probability Foundations
    # -------------------------------------------------------------------------
    {
        "topicSlug": "probability-foundations",
        "subjectSlug": "statistics",
        "title": "Probability Rules, Conditional Probability & Bayes Theorem",
        "slug": "probability-rules-bayes-theorem",
        "description": "Sample spaces, mutually exclusive events, independent events, multiplication rule, conditional probability, and Bayes Rule applications.",
        "estimatedTime": "35 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Fundamental Probability Rules",
                    "content": (
                        "• Probability Bounds: For any event $A$, $0 \\le P(A) \\le 1$. Sum of all mutually exclusive events in sample space $\\sum P(S) = 1$.\n\n"
                        "• Addition Rule: $P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$. If mutually exclusive: $P(A \\cap B) = 0$.\n\n"
                        "• Multiplication Rule: $P(A \\cap B) = P(A) \\cdot P(B|A)$. If independent: $P(A \\cap B) = P(A) \\cdot P(B)$."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Bayes' Theorem & Prior/Posterior Probabilities",
                    "content": (
                        "Bayes' Theorem calculates the posterior probability of an event given prior knowledge of conditions related to the event:\n\n"
                        "$$P(A|B) = \\frac{P(B|A) \\cdot P(A)}{P(B)}$$\n\n"
                        "• $P(A)$: Prior probability of hypothesis $A$.\n"
                        "• $P(B|A)$: Likelihood of observing evidence $B$ given $A$ is true.\n"
                        "• $P(A|B)$: Posterior probability of $A$ after observing evidence $B$."
                    )
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic 3: Hypothesis Testing
    # -------------------------------------------------------------------------
    {
        "topicSlug": "hypothesis-testing-inference",
        "subjectSlug": "statistics",
        "title": "Hypothesis Testing, t-Tests & p-Value Interpretation",
        "slug": "hypothesis-testing-t-tests",
        "description": "Formulating H0 and H1, Type I/II errors, calculating t-statistics, degrees of freedom, and running scipy.stats t-tests.",
        "estimatedTime": "40 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Null ($H_0$) vs Alternative ($H_1$) Hypothesis",
                    "content": (
                        "• Null Hypothesis ($H_0$): Statement of NO effect, NO difference, or status quo (e.g., 'Drug A and Drug B have identical efficacy').\n\n"
                        "• Alternative Hypothesis ($H_1$ or $H_a$): The claim that there IS a significant effect or difference.\n\n"
                        "Decision Matrix:\n"
                        "- Type I Error ($\\alpha$): Rejecting $H_0$ when $H_0$ is actually true (False Positive).\n"
                        "- Type II Error ($\\beta$): Failing to reject $H_0$ when $H_0$ is false (False Negative)."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Interpreting the p-Value",
                    "content": (
                        "The p-value is the probability of obtaining test results at least as extreme as the observed results, assuming the null hypothesis is true.\n\n"
                        "• If $p \\le \\alpha$ (typically $0.05$): Reject $H_0$ (statistically significant difference).\n"
                        "• If $p > \\alpha$: Fail to reject $H_0$ (insufficient evidence to conclude a difference)."
                    )
                },
                {
                    "type": "code",
                    "title": "Running Two-Sample Independent t-Test in Python",
                    "language": "python",
                    "code": (
                        "from scipy.stats import ttest_ind\n"
                        "import numpy as np\n\n"
                        "# Weight gain under Diet A vs Diet B\n"
                        "diet_a = [25, 32, 30, 24, 14, 32, 24, 30, 31, 35, 25]\n"
                        "diet_b = [44, 34, 22, 10, 47, 31, 40, 30, 32, 35, 18, 21, 35, 29, 22]\n\n"
                        "# Test for equal means\n"
                        "t_stat, p_val = ttest_ind(diet_a, diet_b, equal_var=False)\n"
                        "print(f't-statistic: {t_stat:.4f}, p-value: {p_val:.4f}')\n\n"
                        "alpha = 0.05\n"
                        "if p_val < alpha:\n"
                        "    print('Reject H0: Diets differ significantly!')\n"
                        "else:\n"
                        "    print('Fail to reject H0: No statistically significant difference detected.')"
                    )
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic 4: Correlation & Graphical Analysis
    # -------------------------------------------------------------------------
    {
        "topicSlug": "correlation-graphical-analysis",
        "subjectSlug": "statistics",
        "title": "Bivariate Analysis, Correlation & Outlier Detection",
        "slug": "bivariate-correlation-outliers",
        "description": "Pearson r vs Spearman rank correlation, scatter plots, covariance matrices, and detecting outliers using boxplots & IQR.",
        "estimatedTime": "35 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Pearson vs Spearman Rank Correlation",
                    "content": (
                        "• Pearson Correlation Coefficient ($r$): Measures linear relationships between continuous variables. Ranges from $-1.0$ (perfect negative) to $+1.0$ (perfect positive). Sensitive to outliers.\n\n"
                        "• Spearman Rank Correlation ($\\rho$): Measures monotonic relationships based on ranked values. Ideal for non-linear monotonic data and ordinal categories."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Outlier Detection with Boxplots & The 1.5 * IQR Rule",
                    "content": (
                        "Boxplots visualize distribution percentiles:\n"
                        "• $Q_1$: 25th percentile\n"
                        "• $Q_2$: Median (50th percentile)\n"
                        "• $Q_3$: 75th percentile\n"
                        "• $\\text{IQR} = Q_3 - Q_1$\n\n"
                        "Outlier Bounds:\n"
                        "• Lower Bound: $Q_1 - 1.5 \\times \\text{IQR}$\n"
                        "• Upper Bound: $Q_3 + 1.5 \\times \\text{IQR}$\n"
                        "Any data points outside these whiskers are identified as potential outliers."
                    )
                },
                {
                    "type": "code",
                    "title": "Computing Correlation and Filtering Outliers in Python",
                    "language": "python",
                    "code": (
                        "import pandas as pd\n"
                        "import numpy as np\n\n"
                        "data = pd.DataFrame({\n"
                        "    'hours_studied': [2, 3, 5, 7, 9, 10, 12, 14],\n"
                        "    'exam_score':    [50, 55, 65, 72, 85, 88, 94, 98]\n"
                        "})\n\n"
                        "# Pearson correlation matrix\n"
                        "print('Pearson Correlation:\\n', data.corr(method='pearson'))\n\n"
                        "# Detecting outliers via IQR\n"
                        "q1 = data['exam_score'].quantile(0.25)\n"
                        "q3 = data['exam_score'].quantile(0.75)\n"
                        "iqr = q3 - q1\n"
                        "outliers = data[(data['exam_score'] < q1 - 1.5 * iqr) | (data['exam_score'] > q3 + 1.5 * iqr)]\n"
                        "print('Detected Outliers count:', len(outliers))"
                    )
                }
            ]
        }
    }
]
