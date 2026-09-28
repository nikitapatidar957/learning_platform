"""
Machine Learning Topics and Lessons Seed Data
Incorporating concepts from:
- python_interview/machine_learning.md
- python_interview/online_notes_ml.md
- python_interview/linear_regression.md
"""

ML_TOPICS = [
    {
        "subjectSlug": "machine-learning",
        "title": "ML Foundations & Lifecycle",
        "slug": "ml-foundations-workflow",
        "description": "Core concepts, traditional programming vs ML, supervised, unsupervised, reinforcement learning, and end-to-end workflows.",
        "order": 1,
        "isPublished": True,
    },
    {
        "subjectSlug": "machine-learning",
        "title": "Generalization & Feature Engineering",
        "slug": "generalization-feature-engineering",
        "description": "Overfitting, underfitting, bias-variance tradeoff, regularization, and feature scaling (Normalization vs Standardization).",
        "order": 2,
        "isPublished": True,
    },
    {
        "subjectSlug": "machine-learning",
        "title": "Linear Models & Optimization",
        "slug": "linear-models-regression",
        "description": "Simple and multiple linear regression, the 5 core statistical assumptions, and gradient descent optimization.",
        "order": 3,
        "isPublished": True,
    },
    {
        "subjectSlug": "machine-learning",
        "title": "Model Evaluation Metrics",
        "slug": "model-evaluation-metrics",
        "description": "Confusion matrix, accuracy paradox, precision, recall, F1 score, ROC-AUC, MAE, MSE, RMSE, and R-squared.",
        "order": 4,
        "isPublished": True,
    },
    {
        "subjectSlug": "machine-learning",
        "title": "Learning Strategies & Ensembles",
        "slug": "learning-strategies-ensembles",
        "description": "Batch learning vs online incremental learning, concept drift, and ensemble methods (Bagging vs Boosting).",
        "order": 5,
        "isPublished": True,
    },
]

ML_LESSONS = [
    # -------------------------------------------------------------------------
    # Topic 1: ML Foundations & Lifecycle
    # -------------------------------------------------------------------------
    {
        "topicSlug": "ml-foundations-workflow",
        "subjectSlug": "machine-learning",
        "title": "What is Machine Learning? Core Paradigms",
        "slug": "what-is-machine-learning",
        "description": "Understand what machine learning is, how it differs from traditional code, the 3 learning paradigms, and the ML lifecycle.",
        "estimatedTime": "25 mins",
        "difficulty": "Beginner",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "What is Machine Learning?",
                    "content": (
                        "Arthur Samuel (1959) famously defined Machine Learning as:\n"
                        "\"The field of study that gives computers the ability to learn without being explicitly programmed.\"\n\n"
                        "Tom Mitchell (1997) formalized this with an engineering definition:\n"
                        "\"A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, "
                        "if its performance at tasks in T, as measured by P, improves with experience E.\""
                    )
                },
                {
                    "type": "explanation",
                    "title": "Traditional Programming vs Machine Learning",
                    "content": (
                        "• Traditional Programming:\n"
                        "  Data + Rules (Logic written by human developer) ➔ Answers / Output\n\n"
                        "• Machine Learning:\n"
                        "  Data + Answers (Historical labels) ➔ Machine Learns the Rules (Statistical Model)\n\n"
                        "Example: To detect spam emails with traditional rules, you'd write endless `if 'win money' in email:` statements. Spammers easily bypass this. "
                        "With ML, the model analyzes 100,000 spam and non-spam emails, detects subtle word frequency distributions automatically, and adapts over time."
                    )
                },
                {
                    "type": "explanation",
                    "title": "The Three Core Paradigms of Machine Learning",
                    "content": (
                        "1. Supervised Learning:\n"
                        "   Data comes with ground-truth target labels. The model learns a mapping function from input features X to target y.\n"
                        "   • Classification: Target is discrete/categorical (e.g., Spam vs Not Spam, Cat vs Dog).\n"
                        "   • Regression: Target is continuous/numeric (e.g., House price, temperature, stock valuation).\n\n"
                        "2. Unsupervised Learning:\n"
                        "   Data has no target labels (only features X). The algorithm discovers hidden structure, clusters, or patterns.\n"
                        "   • Clustering: Grouping similar customers (k-Means, Hierarchical).\n"
                        "   • Dimensionality Reduction: Compressing features while retaining variance (PCA, t-SNE).\n\n"
                        "3. Reinforcement Learning:\n"
                        "   An autonomous agent interacts with an environment, takes actions, and receives scalar rewards or penalties. "
                        "   The goal is to discover an optimal policy to maximize cumulative reward over time (e.g., AlphaGo, self-driving cars, game playing)."
                    )
                },
                {
                    "type": "callout",
                    "variant": "info",
                    "content": "End-to-End ML Pipeline: Problem Formulation ➔ Data Collection ➔ Exploratory Data Analysis (EDA) ➔ Data Preprocessing & Cleaning ➔ Feature Engineering ➔ Model Training ➔ Hyperparameter Tuning ➔ Model Evaluation ➔ Deployment ➔ Continuous Monitoring."
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic 2: Generalization & Feature Engineering
    # -------------------------------------------------------------------------
    {
        "topicSlug": "generalization-feature-engineering",
        "subjectSlug": "machine-learning",
        "title": "Overfitting, Underfitting & The Bias-Variance Tradeoff",
        "slug": "bias-variance-tradeoff",
        "description": "Understand high bias vs high variance, how to diagnose generalization errors, and strategies to balance model complexity.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The Generalization Dilemma",
                    "content": (
                        "The primary goal of machine learning is NOT to achieve 100% accuracy on training data—it is to GENERALIZE accurately to unseen real-world data.\n\n"
                        "• Underfitting (High Bias): The model is too simple to capture the underlying pattern. It performs poorly on BOTH training data and test data. "
                        "Analogy: A student who didn't study at all and guesses randomly on both practice exams and final tests.\n\n"
                        "• Overfitting (High Variance): The model is overly complex and memorizes noise, outliers, and quirks of the training data. "
                        "It gets 99% on training data, but fails miserably on new test data. "
                        "Analogy: A student who memorized the exact questions on practice exam 1, but cannot solve the actual test because the numbers changed."
                    )
                },
                {
                    "type": "explanation",
                    "title": "The Mathematical Bias-Variance Decomposition",
                    "content": (
                        "For any supervised model, the total expected prediction error decomposes into:\n\n"
                        "Total Error = Bias² + Variance + Irreducible Error\n\n"
                        "• Bias: Error introduced by approximating a real-world complex problem with an overly simple model.\n"
                        "• Variance: Sensitivity to small fluctuations in the training dataset.\n"
                        "• Irreducible Error: Noise inherent in the problem (measurement error, missing variables) that no algorithm can eliminate."
                    )
                },
                {
                    "type": "code",
                    "title": "How to Fix Underfitting vs Overfitting",
                    "language": "python",
                    "code": (
                        "# How to Fix Underfitting (High Bias):\n"
                        "# 1. Increase model complexity (e.g., use polynomial features or deeper trees)\n"
                        "# 2. Add more relevant features / feature engineering\n"
                        "# 3. Decrease regularization strength (reduce alpha / lambda)\n\n"
                        "# How to Fix Overfitting (High Variance):\n"
                        "# 1. Collect more training data\n"
                        "# 2. Apply Regularization (L1 Lasso or L2 Ridge to penalize large weights)\n"
                        "# 3. Feature selection: remove noisy/irrelevant features\n"
                        "# 4. For trees: prune depth (max_depth), use Random Forest / Dropout\n"
                        "# 5. Use K-Fold Cross-Validation"
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "Interview Gold Rule: The sweet spot is a model that minimizes total error by balancing bias and variance—complex enough to learn true patterns, but regularized enough to ignore random noise."
                }
            ]
        }
    },
    {
        "topicSlug": "generalization-feature-engineering",
        "subjectSlug": "machine-learning",
        "title": "Feature Scaling: Normalization vs Standardization",
        "slug": "feature-scaling-mastery",
        "description": "Learn why distance and gradient algorithms fail without scaling, and when to choose Min-Max Normalization vs Z-Score Standardization.",
        "estimatedTime": "25 mins",
        "difficulty": "Intermediate",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Why is Feature Scaling Essential?",
                    "content": (
                        "Suppose you have two features: `Age` (ranging from 18 to 65) and `Salary` (ranging from 20,000 to 200,000). "
                        "When computing distance in kNN or calculating gradients in gradient descent, the massive numbers in `Salary` will completely dominate the math, "
                        "making `Age` mathematically invisible!\n\n"
                        "Feature scaling ensures all input features contribute proportionately on an equal footing."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Which Algorithms Require Scaling?",
                    "content": (
                        "• MUST SCALE:\n"
                        "  - Distance-based models: k-Nearest Neighbors (kNN), k-Means Clustering, Support Vector Machines (SVM).\n"
                        "  - Gradient-based models: Linear Regression, Logistic Regression, Neural Networks (prevents gradient oscillation and speeds up convergence).\n"
                        "  - Principal Component Analysis (PCA): Direction of maximum variance is otherwise dominated by large scales.\n\n"
                        "• DO NOT REQUIRE SCALING:\n"
                        "  - Tree-based models: Decision Trees, Random Forest, Gradient Boosting, XGBoost. "
                        "Trees only split on relative rank order (`if feature > threshold`), so multiplying a feature by 1,000,000 changes nothing about where the split occurs!"
                    )
                },
                {
                    "type": "code",
                    "title": "Normalization (Min-Max) vs Standardization (StandardScaler)",
                    "language": "python",
                    "code": (
                        "import numpy as np\n"
                        "from sklearn.preprocessing import MinMaxScaler, StandardScaler\n\n"
                        "data = np.array([[25, 50000], [35, 75000], [50, 120000]])\n\n"
                        "# 1. Normalization (Min-Max Scaling): Scales values to fixed range [0, 1]\n"
                        "# Formula: x_norm = (x - x_min) / (x_max - x_min)\n"
                        "# Use when: You know the distribution is not Gaussian or algorithm requires bounded ranges (e.g., Neural Net images)\n"
                        "min_max = MinMaxScaler()\n"
                        "norm_data = min_max.fit_transform(data)\n\n"
                        "# 2. Standardization (Z-score): Rescales to mean = 0, standard deviation = 1\n"
                        "# Formula: z = (x - mu) / sigma\n"
                        "# Use when: Data has outliers or follows normal distribution. Much less sensitive to outliers than Min-Max!\n"
                        "std_scaler = StandardScaler()\n"
                        "std_data = std_scaler.fit_transform(data)"
                    )
                },
                {
                    "type": "callout",
                    "variant": "warning",
                    "content": "Data Leakage Trap: ALWAYS fit scalers on training data only (`scaler.fit_transform(X_train)`), and then simply transform the test data (`scaler.transform(X_test)`). Never fit on the whole dataset before splitting!"
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic 3: Linear Models & Optimization
    # -------------------------------------------------------------------------
    {
        "topicSlug": "linear-models-regression",
        "subjectSlug": "machine-learning",
        "title": "Simple & Multiple Linear Regression",
        "slug": "linear-regression-deep-dive",
        "description": "Understand linear modeling, the best-fit line formula, cost functions, and residual error minimization.",
        "estimatedTime": "30 mins",
        "difficulty": "Beginner to Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": "LinearRegressionVisualizer",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "What is Linear Regression?",
                    "content": (
                        "Linear Regression models the relationship between a dependent target variable (y) and one or more independent explanatory features (X) "
                        "by fitting a linear equation to observed data.\n\n"
                        "• Simple Linear Regression (1 feature): y = m*x + c\n"
                        "  (where m is the slope/weight and c is the y-intercept/bias)\n\n"
                        "• Multiple Linear Regression (n features): y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε\n"
                        "  (where β coefficients represent the change in target for a unit change in each feature, keeping other features fixed)."
                    )
                },
                {
                    "type": "visualization",
                    "component": "LinearRegressionVisualizer",
                    "initialState": {}
                },
                {
                    "type": "explanation",
                    "title": "The Cost Function: Ordinary Least Squares (OLS) / MSE",
                    "content": (
                        "How does the model find the 'best-fit' line? By finding the line that minimizes the sum of squared differences between "
                        "the actual values (y) and predicted values (ŷ):\n\n"
                        "Cost Function: J(β) = (1 / 2n) * Σ (yᵢ - ŷᵢ)²\n\n"
                        "Why square the errors? Squaring ensures that positive and negative errors don't cancel each other out, and it penalizes large errors much more severely."
                    )
                },
                {
                    "type": "code",
                    "title": "Implementing Linear Regression in Python",
                    "language": "python",
                    "code": (
                        "from sklearn.linear_model import LinearRegression\n"
                        "import numpy as np\n\n"
                        "# Feature: Years of Experience; Target: Salary ($)\n"
                        "X = np.array([[1], [2], [3], [4], [5], [6]])\n"
                        "y = np.array([45000, 52000, 60000, 68000, 75000, 83000])\n\n"
                        "model = LinearRegression()\n"
                        "model.fit(X, y)\n\n"
                        "slope = model.coef_[0]         # Weight m: ~$7,500/year\n"
                        "intercept = model.intercept_   # Base salary c: ~$37,000\n"
                        "print(f'Formula: Salary = {slope:.2f} * Experience + {intercept:.2f}')\n\n"
                        "# Predict for 8 years experience\n"
                        "predicted_salary = model.predict([[8]])\n"
                        "print(f'Predicted Salary for 8 yrs: ${predicted_salary[0]:,.2f}')"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "linear-models-regression",
        "subjectSlug": "machine-learning",
        "title": "5 Core Assumptions of Linear Regression",
        "slug": "assumptions-linear-regression",
        "description": "Master the 5 essential statistical assumptions required for linear regression to produce valid, unbiased estimates.",
        "estimatedTime": "25 mins",
        "difficulty": "Intermediate",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The 5 Mandatory Assumptions for Linear Models",
                    "content": (
                        "In data science and machine learning interviews, this is one of the most frequently asked questions. "
                        "If these assumptions are violated, your p-values, coefficients, and predictions are statistically invalid:\n\n"
                        "1. Linearity: The relationship between the independent features X and dependent target y must be linear. "
                        "Check: Scatter plot of residuals vs predicted values (should show no curved pattern).\n\n"
                        "2. Independence of Errors (No Autocorrelation): Residuals (errors) must be independent of one another. "
                        "Critical in time-series data. Check: Durbin-Watson statistic (values between 1.5 and 2.5 indicate no autocorrelation).\n\n"
                        "3. Homoscedasticity (Constant Variance): The spread of residuals must remain constant across all levels of predictions. "
                        "If residuals fan out like a funnel, you have Heteroscedasticity. Fix: Log-transform the target variable.\n\n"
                        "4. Normality of Residuals: The error residuals should be normally distributed with mean 0. "
                        "Check: Q-Q Plot (points should follow the diagonal line) or Shapiro-Wilk test.\n\n"
                        "5. No Multicollinearity: Independent features should NOT be highly correlated with each other. "
                        "Check: Variance Inflation Factor (VIF). A VIF > 5 or 10 indicates severe multicollinearity. Fix: Drop one of the redundant features or apply Ridge regression."
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "Interview Memory Acronym: L-I-H-N-M: Linearity, Independence, Homoscedasticity, Normality, Multicollinearity."
                }
            ]
        }
    },
    {
        "topicSlug": "linear-models-regression",
        "subjectSlug": "machine-learning",
        "title": "Gradient Descent Optimization",
        "slug": "gradient-descent-optimization",
        "description": "Discover how algorithms learn weights by walking down error surfaces, learning rates, and Batch vs Stochastic vs Mini-batch GD.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 3,
        "isPublished": True,
        "interactiveType": "LinearRegressionVisualizer",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The Intuition: Walking Down a Mountain in the Fog",
                    "content": (
                        "Imagine you are standing on a foggy mountain peak (high error) and you want to reach the lowest valley (minimum error). "
                        "You cannot see the valley directly, but you can feel the slope of the ground under your feet. "
                        "At each step, you feel which way is steepest downhill, and take a step in that direction!\n\n"
                        "That is Gradient Descent: It calculates the partial derivative (slope) of the loss function with respect to each model weight, "
                        "and takes a step proportional to the negative gradient."
                    )
                },
                {
                    "type": "code",
                    "title": "The Weight Update Equation",
                    "language": "python",
                    "code": (
                        "# Weight update formula:\n"
                        "# w_new = w_old - (learning_rate * dLoss/dw)\n\n"
                        "def gradient_descent_step(w, b, X, y, lr=0.01):\n"
                        "    n = len(X)\n"
                        "    y_pred = w * X + b\n"
                        "    # Partial derivatives of MSE loss\n"
                        "    dw = (-2 / n) * sum(X * (y - y_pred))\n"
                        "    db = (-2 / n) * sum(y - y_pred)\n"
                        "    \n"
                        "    # Update weights\n"
                        "    w = w - lr * dw\n"
                        "    b = b - lr * db\n"
                        "    return w, b"
                    )
                },
                {
                    "type": "explanation",
                    "title": "The 3 Variants of Gradient Descent",
                    "content": (
                        "• Batch Gradient Descent: Computes the gradient over the ENTIRE dataset before making 1 weight update. "
                        "Smooth convergence, but very slow on massive datasets that don't fit in RAM.\n\n"
                        "• Stochastic Gradient Descent (SGD): Updates weights after EVERY SINGLE training sample. "
                        "Fast and can jump out of local minima, but updates are noisy and fluctuate wildly.\n\n"
                        "• Mini-Batch Gradient Descent: The sweet spot used in modern deep learning. Updates weights on small batches (e.g., 32, 64, 128 samples). "
                        "Leverages GPU vector parallelization while maintaining fast, stable convergence."
                    )
                },
                {
                    "type": "callout",
                    "variant": "warning",
                    "content": "Learning Rate Trap: If α is too small, convergence takes forever. If α is too large, the algorithm overshoots the minimum and diverges (exploding gradient)!"
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic 4: Model Evaluation Metrics
    # -------------------------------------------------------------------------
    {
        "topicSlug": "model-evaluation-metrics",
        "subjectSlug": "machine-learning",
        "title": "Classification Metrics & The Confusion Matrix",
        "slug": "classification-metrics-confusion-matrix",
        "description": "Master True/False Positives/Negatives, the accuracy paradox on imbalanced data, Precision, Recall, and the F1-Score.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": "ConfusionMatrixVisualizer",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The Confusion Matrix",
                    "content": (
                        "A Confusion Matrix is a 2x2 table that tabulates predicted classifications against actual outcomes:\n\n"
                        "• True Positive (TP): Model correctly predicted Positive (e.g., predicted Patient has disease, and they do).\n"
                        "• True Negative (TN): Model correctly predicted Negative (e.g., predicted Patient is healthy, and they are).\n"
                        "• False Positive (FP) - Type I Error: Model predicted Positive, but it was Negative (e.g., False Alarm, innocent flagged as fraud).\n"
                        "• False Negative (FN) - Type II Error: Model predicted Negative, but it was Positive (e.g., Dangerous Miss, cancer patient told they are healthy)."
                    )
                },
                {
                    "type": "visualization",
                    "component": "ConfusionMatrixVisualizer",
                    "initialState": {}
                },
                {
                    "type": "explanation",
                    "title": "The Accuracy Paradox",
                    "content": (
                        "Why can't we just use Accuracy (Total Correct / Total Predictions)?\n\n"
                        "Suppose you have a fraud detection dataset with 99,000 legitimate transactions and 1,000 fraudulent transactions (1% fraud). "
                        "A dumb model that blindly predicts 'LEGITIMATE' for 100% of transactions will achieve a 99.0% Accuracy score! "
                        "Yet it caught 0 fraudulent transactions and is completely useless in production.\n\n"
                        "This is why Precision, Recall, and F1-Score are vital for real-world engineering."
                    )
                },
                {
                    "type": "code",
                    "title": "Precision, Recall and F1-Score Formulas",
                    "language": "python",
                    "code": (
                        "# Precision = TP / (TP + FP)\n"
                        "# Question: Out of all instances the model labeled Positive, how many were actually Positive?\n"
                        "# Optimize when: False Positives are expensive (e.g., Spam filter placing boss email in junk)\n\n"
                        "# Recall (Sensitivity) = TP / (TP + FN)\n"
                        "# Question: Out of all actual Positive cases in reality, how many did the model catch?\n"
                        "# Optimize when: False Negatives are dangerous (e.g., Medical cancer screening, bank fraud)\n\n"
                        "# F1-Score = 2 * (Precision * Recall) / (Precision + Recall)\n"
                        "# Harmonic mean: Punishes extreme values, ensuring both Precision and Recall are balanced."
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "Why Harmonic Mean for F1? An arithmetic mean of Precision=1.0 and Recall=0.0 would give 0.50 (misleading). The harmonic mean yields 0.00, accurately signaling that the model is broken."
                }
            ]
        }
    },
    {
        "topicSlug": "model-evaluation-metrics",
        "subjectSlug": "machine-learning",
        "title": "Regression Evaluation Metrics: MAE, MSE, RMSE & R²",
        "slug": "regression-evaluation-metrics",
        "description": "Understand how to quantify continuous errors, when to use MAE vs RMSE, and how to interpret the R-squared score.",
        "estimatedTime": "25 mins",
        "difficulty": "Intermediate",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The 4 Core Regression Metrics",
                    "content": (
                        "When evaluating a continuous model (like predicting house prices or temperature), we quantify how far our predictions deviate from reality:\n\n"
                        "1. Mean Absolute Error (MAE): Average absolute difference: (1/n) * Σ |y - ŷ|.\n"
                        "   • Intuitive and easy to explain to non-technical business stakeholders.\n"
                        "   • Robust to outliers because errors are not squared.\n\n"
                        "2. Mean Squared Error (MSE): Average squared difference: (1/n) * Σ (y - ŷ)².\n"
                        "   • Heavily penalizes large outlier errors (an error of 10 adds 100 to the loss, whereas an error of 1 adds only 1).\n"
                        "   • Units are squared (e.g., dollars²), making direct business interpretation difficult.\n\n"
                        "3. Root Mean Squared Error (RMSE): Square root of MSE: √MSE.\n"
                        "   • Back in original units of the target variable (e.g., dollars).\n"
                        "   • Standard metric in Kaggle and production benchmarking.\n\n"
                        "4. R² Score (Coefficient of Determination): 1 - (SS_res / SS_tot).\n"
                        "   • Represents the proportion of variance in target y that is explained by the features X.\n"
                        "   • R² = 1.0: Perfect model.\n"
                        "   • R² = 0.0: Model performs no better than predicting the mean of y.\n"
                        "   • R² < 0.0: Model is worse than predicting the horizontal mean line!"
                    )
                },
                {
                    "type": "code",
                    "title": "Calculating Regression Metrics in Python",
                    "language": "python",
                    "code": (
                        "from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score\n"
                        "import numpy as np\n\n"
                        "y_true = np.array([100, 150, 200, 250, 300])\n"
                        "y_pred = np.array([105, 148, 190, 260, 315])\n\n"
                        "mae = mean_absolute_error(y_true, y_pred)\n"
                        "mse = mean_squared_error(y_true, y_pred)\n"
                        "rmse = np.sqrt(mse)\n"
                        "r2 = r2_score(y_true, y_pred)\n\n"
                        "print(f'MAE:  {mae:.2f}')   # Average dollar error\n"
                        "print(f'RMSE: {rmse:.2f}')  # Outlier-sensitive error\n"
                        "print(f'R^2:  {r2:.4f}')   # % variance explained (~0.98)"
                    )
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Topic 5: Learning Strategies & Ensembles
    # -------------------------------------------------------------------------
    {
        "topicSlug": "learning-strategies-ensembles",
        "subjectSlug": "machine-learning",
        "title": "Batch Learning vs Online / Incremental Learning",
        "slug": "batch-vs-online-learning",
        "description": "Understand offline batch training vs streaming online updates, out-of-core learning, and managing concept drift in production.",
        "estimatedTime": "25 mins",
        "difficulty": "Intermediate to Advanced",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Batch Learning (Offline Learning)",
                    "content": (
                        "In Batch Learning, the system is trained on all available historical data in one big chunk offline. "
                        "Once trained, the model weights are frozen and deployed into production to serve predictions.\n\n"
                        "• Key Limitation: When new data arrives, the model CANNOT learn incrementally. You must retrain the entire model from scratch on the old + new data, which is computationally expensive."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Online Learning (Incremental / Streaming Learning)",
                    "content": (
                        "In Online Learning, the model updates its parameters continuously as new data instances arrive, either individually or in small mini-batches.\n\n"
                        "• When to use Online Learning:\n"
                        "  1. Continuous real-time streaming data (e.g., real-time stock trades, Twitter sentiment, live clickstreams).\n"
                        "  2. Out-of-Core Learning: When your dataset is 500 GB but your server only has 32 GB of RAM! The system loads chunks from disk, trains the model incrementally, and discards the chunk from memory."
                    )
                },
                {
                    "type": "code",
                    "title": "Out-of-Core Incremental Learning with SGDClassifier",
                    "language": "python",
                    "code": (
                        "from sklearn.linear_model import SGDClassifier\n"
                        "import numpy as np\n\n"
                        "# SGDClassifier supports partial_fit for incremental streaming\n"
                        "model = SGDClassifier(loss='log_loss')\n\n"
                        "# Stream 1: First batch of incoming user clicks\n"
                        "X_batch_1 = np.array([[0.5, 1.2], [1.5, 0.8]])\n"
                        "y_batch_1 = np.array([0, 1])\n"
                        "model.partial_fit(X_batch_1, y_batch_1, classes=[0, 1])\n\n"
                        "# Stream 2: Next batch 1 hour later\n"
                        "X_batch_2 = np.array([[2.1, 0.4], [0.1, 1.9]])\n"
                        "y_batch_2 = np.array([1, 0])\n"
                        "model.partial_fit(X_batch_2, y_batch_2)  # Updates weights in real-time"
                    )
                },
                {
                    "type": "explanation",
                    "title": "Concept Drift: Why Models Decay Over Time",
                    "content": (
                        "In real production systems, consumer behavior and external factors change over time:\n"
                        "• Covariate Shift: The distribution of inputs P(X) changes (e.g., fashion trends shift from winter coats to summer shorts).\n"
                        "• Concept Shift: The statistical relationship between features and target P(y|X) changes (e.g., historical airline bookings before COVID vs during COVID).\n\n"
                        "Production Solution: Monitor model prediction distribution and rolling accuracy. Trigger automated retraining pipelines when performance dips below a threshold."
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "learning-strategies-ensembles",
        "subjectSlug": "machine-learning",
        "title": "Ensemble Learning: Bagging vs Boosting",
        "slug": "ensemble-bagging-boosting",
        "description": "Understand ensemble methods, combining weak learners, Random Forests (Bagging), and Gradient Boosting / XGBoost (Boosting).",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate to Advanced",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The Philosophy of Ensemble Learning",
                    "content": (
                        "Ensemble learning is based on the 'Wisdom of the Crowds': A group of diverse weak learners (models that perform slightly better than random guessing) "
                        "combined together will consistently outperform any single complex model."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Bagging vs Boosting: The Core Differences",
                    "content": (
                        "• Bagging (Bootstrap Aggregating - e.g., Random Forest):\n"
                        "  - Models are trained in PARALLEL and independently.\n"
                        "  - Each model trains on a random bootstrap sample (sampling with replacement) of the data.\n"
                        "  - Primary Goal: REDUCE VARIANCE (fixes overfitting).\n"
                        "  - Final decision: Majority vote (classification) or average (regression).\n\n"
                        "• Boosting (e.g., AdaBoost, Gradient Boosting, XGBoost, LightGBM, CatBoost):\n"
                        "  - Models are trained SEQUENTIALLY, not in parallel.\n"
                        "  - Each subsequent model focuses specifically on the errors and misclassifications made by the previous models.\n"
                        "  - Primary Goal: REDUCE BIAS (builds high-capacity accurate predictors).\n"
                        "  - Final decision: Weighted combination of all sequential learners."
                    )
                },
                {
                    "type": "code",
                    "title": "Random Forest vs Gradient Boosting in Python",
                    "language": "python",
                    "code": (
                        "from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier\n\n"
                        "# Bagging: Random Forest trains 100 trees in parallel with feature subsampling\n"
                        "rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)\n"
                        "# rf.fit(X_train, y_train)\n\n"
                        "# Boosting: Gradient Boosting trains trees sequentially to minimize residuals\n"
                        "gb = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3)\n"
                        "# gb.fit(X_train, y_train)"
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "Interview Summary: Bagging reduces Variance by training independent trees on random subsets in parallel. Boosting reduces Bias by training trees sequentially to correct prior errors."
                }
            ]
        }
    }
]
