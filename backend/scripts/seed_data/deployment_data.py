"""
Model Deployment & MLOps seed data: Topics and Lessons.
Covers Flask web framework, REST APIs, End-to-end ML churn pipeline, Docker containerization, Gunicorn, and GitHub Actions CI/CD.
"""

DEPLOYMENT_TOPICS = [
    {
        "subjectSlug": "deployment",
        "title": "Flask Web Framework & REST APIs",
        "slug": "flask-web-framework",
        "description": "Flask WSGI architecture, routing, HTTP request handling, Jinja2 dynamic HTML rendering, and building JSON inference endpoints.",
        "order": 1,
        "isPublished": True,
    },
    {
        "subjectSlug": "deployment",
        "title": "End-to-End Machine Learning Pipelines",
        "slug": "end-to-end-ml-pipelines",
        "description": "Complete real-world customer churn prediction: data cleaning, exploratory data analysis, statistical feature selection, and model serialization.",
        "order": 2,
        "isPublished": True,
    },
    {
        "subjectSlug": "deployment",
        "title": "Production Containerization & CI/CD",
        "slug": "containerization-and-cicd",
        "description": "Production WSGI serving with Gunicorn, Docker containerization, Procfile configuration, and automated GitHub Actions CI/CD pipelines.",
        "order": 3,
        "isPublished": True,
    },
]

DEPLOYMENT_LESSONS = [
    {
        "topicSlug": "flask-web-framework",
        "subjectSlug": "deployment",
        "title": "Flask Web Framework & Machine Learning API Serving",
        "slug": "flask-web-framework-and-ml-apis",
        "description": "Deploy trained machine learning models as production REST APIs and web applications using Flask and pickle deserialization.",
        "estimatedTime": "35 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Flask for Machine Learning Serving Architecture",
                    "content": (
                        "Flask is a lightweight WSGI micro-framework ideal for ML inference serving:\n\n"
                        "• **Load Model at Startup**: Never deserialize (`pickle.load`) inside request routes! Load the model once globally at application launch.\n"
                        "• **Routing**: Map URL endpoints to Python handler functions using `@app.route('/predict', methods=['POST'])`.\n"
                        "• **Request Parsing**: Read HTML form submissions with `request.form` or JSON API payloads with `request.get_json()`.\n"
                        "• **Response Generation**: Render Jinja2 HTML templates with `render_template('index.html', result=...)` or return RESTful JSON with `jsonify()`."
                    )
                },
                {
                    "type": "code",
                    "title": "Production Flask Model Serving API",
                    "language": "python",
                    "code": (
                        "from flask import Flask, request, jsonify, render_template\n"
                        "import pickle\n"
                        "import numpy as np\n\n"
                        "app = Flask(__name__)\n\n"
                        "# Load serialized ML pipeline once at startup\n"
                        "with open('churn.pkl', 'rb') as f:\n"
                        "    model = pickle.load(f)\n\n"
                        "@app.route('/')\n"
                        "def home():\n"
                        "    return render_template('index.html')\n\n"
                        "@app.route('/predict', methods=['POST'])\n"
                        "def predict():\n"
                        "    if request.is_json:\n"
                        "        data = request.get_json()\n"
                        "        features = np.array(data['features']).reshape(1, -1)\n"
                        "        pred = model.predict(features)[0]\n"
                        "        prob = model.predict_proba(features)[0][1]\n"
                        "        return jsonify({'churn_prediction': int(pred), 'churn_probability': float(prob)})\n"
                        "    else:\n"
                        "        # Handle HTML Form Submission\n"
                        "        tenure = float(request.form['tenure'])\n"
                        "        # ... feature parsing ...\n"
                        "        return render_template('index.html', prediction='Customer Churn Risk')"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "end-to-end-ml-pipelines",
        "subjectSlug": "deployment",
        "title": "End-to-End ML Pipeline: Cleaning, EDA, Feature Selection & Modeling",
        "slug": "end-to-end-ml-pipeline-data-to-model",
        "description": "Production case study on Customer Churn Prediction: data cleaning, EDA, hypothesis testing feature selection, and class imbalance handling.",
        "estimatedTime": "45 mins",
        "difficulty": "Intermediate to Advanced",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Production ML Pipeline Workflow",
                    "content": (
                        "A production-grade machine learning lifecycle consists of 5 tightly integrated stages:\n\n"
                        "1. **Data Cleaning & Anomaly Detection**: Imputing missing values using median/mode and filtering corrupted entries.\n"
                        "2. **Exploratory Data Analysis (EDA)**: Visualizing distributions and quantifying skewness across churn cohorts.\n"
                        "3. **Statistical Feature Selection**: Using t-tests for numerical variables and Chi-Square tests for categorical variables ($p < 0.05$).\n"
                        "4. **Class Imbalance Mitigation**: Balancing skewed customer distributions using SMOTE or cost-sensitive class weights.\n"
                        "5. **Pipeline Serialization**: Exporting feature transformers and estimators bundled into a single `.pkl` artifact."
                    )
                },
                {
                    "type": "code",
                    "title": "Pipeline Assembly and Serialization with Scikit-Learn",
                    "language": "python",
                    "code": (
                        "from sklearn.pipeline import Pipeline\n"
                        "from sklearn.preprocessing import StandardScaler\n"
                        "from sklearn.ensemble import RandomForestClassifier\n"
                        "import pickle\n\n"
                        "pipeline = Pipeline([\n"
                        "    ('scaler', StandardScaler()),\n"
                        "    ('classifier', RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42))\n"
                        "])\n\n"
                        "pipeline.fit(X_train, y_train)\n\n"
                        "# Save production artifact\n"
                        "with open('churn.pkl', 'wb') as f:\n"
                        "    pickle.dump(pipeline, f)"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "containerization-and-cicd",
        "subjectSlug": "deployment",
        "title": "Production Deployment: Docker Containerization, Gunicorn & CI/CD Pipelines",
        "slug": "production-containerization-docker-and-cicd",
        "description": "Master productionizing machine learning systems: Gunicorn WSGI, Docker containers, Procfiles, and automated GitHub Actions CI/CD.",
        "estimatedTime": "40 mins",
        "difficulty": "Advanced",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Containerization & Continuous Integration Principles",
                    "content": (
                        "• **Gunicorn WSGI**: Multi-worker pre-fork server running multiple worker processes concurrently (`gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app`).\n\n"
                        "• **Docker Containerization**: Packages the application, dependencies, system libraries, and runtime environment into an immutable, portable image.\n\n"
                        "• **CI/CD with GitHub Actions**: Automates running tests, linting, building Docker images, and deploying to cloud infrastructure whenever code is pushed to `main`."
                    )
                },
                {
                    "type": "code",
                    "title": "Production Dockerfile for Machine Learning Applications",
                    "language": "dockerfile",
                    "code": (
                        "FROM python:3.9-slim\n\n"
                        "WORKDIR /app\n\n"
                        "# Layer caching: copy requirements first\n"
                        "COPY requirements.txt .\n"
                        "RUN pip install --no-cache-dir -r requirements.txt\n\n"
                        "# Copy application code and model artifacts\n"
                        "COPY . .\n\n"
                        "EXPOSE 5000\n\n"
                        "CMD [\"gunicorn\", \"--workers=4\", \"--bind\", \"0.0.0.0:5000\", \"app:app\"]"
                    )
                }
            ]
        }
    },
]
