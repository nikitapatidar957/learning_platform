# Production Deployment: Docker Containerization, Gunicorn & CI/CD Pipelines

Master productionizing machine learning systems: WSGI servers (Gunicorn), Docker containerization, cloud deployment configurations (Procfile), continuous integration & continuous deployment (GitHub Actions), and production logging.

---

## 1. Architecture Overview & Project Specification

# E-commerce-Customer-Churn-Prediction

##Overview

This is an end-to-end ML project, which aims at developing a classification model for predicting if a customer for an ecommerce business will churn or not in the following month

The classifier used for this project is DecisionTreeClassifier.

Deployed in Railway.app.

Link to the application : https://ecommerce-customer-churn.up.railway.app/ 

************************************************************************************************************

## Dataset Information

This dataset contains information on the customers personal details, spending habits etc

Link : https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction 

************************************************************************************************************

## App Interface

![image](https://user-images.githubusercontent.com/77207245/206840674-1cc63fa5-e92d-4c67-a9df-c603a7c50ea9.png)

************************************************************************************************************

## Directory Tree

![image](https://user-images.githubusercontent.com/77207245/206840435-48e20324-a79b-4601-b881-9687baa2521f.png)

************************************************************************************************************

## Technologies Used

![image](https://user-images.githubusercontent.com/77207245/206840274-30f095bf-eb95-4fda-9397-1ae7962a5e1b.png)



---

## 2. Docker Containerization (`Dockerfile`)

Below is the Docker configuration packaging the Python environment, dependencies, and WSGI entry point:

```dockerfile
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app 
```

### Dependency Manifest (`requirements.txt`)
```text
matplotlib>=3.2.2
scikit-learn>=1.0.2
seaborn>=0.11.2
pandas>=1.3.5
numpy>=1.21.6
imblearn>=0.0
bz2file>=0.98
Flask>=1.1.4
Jinja2>=2.11.3
gunicorn>=20.1.0
itsdangerous==1.1.0
MarkupSafe==2.0.1
Werkzeug==1.0.1
```

---

## 3. Production WSGI Configuration (`Procfile`)

```text
web: gunicorn app:app
```

**Why Gunicorn over Flask's built-in development server?**
- Flask's `app.run()` server is single-threaded and intended solely for local debugging. It blocks on concurrent requests.
- Gunicorn (Green Unicorn) is a pre-fork worker WSGI server. A master process handles incoming connections and delegates requests across multiple worker processes (`--workers=4`), enabling concurrent request handling and auto-recovery from worker crashes.

---

## 4. Continuous Integration & Deployment (CI/CD) with GitHub Actions

Below is the workflow definition in `.github/workflows/main.yaml` automating Docker image builds and cloud releases on every push to `main`:

```yaml
# Your workflow name.
name: Deploy to heroku.

# Run workflow on every push to main branch.
on:
  push:
    branches: [main]

# Your workflows jobs.
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # Check-out your repository.
      - name: Checkout
        uses: actions/checkout@v2


### ⬇ IMPORTANT PART ⬇ ###

      - name: Build, Push and Release a Docker container to Heroku. # Your custom step name
        uses: gonuit/heroku-docker-deploy@v1.3.3 # GitHub action name (leave it as it is).
        with:
          # Below you must provide variables for your Heroku app.

          # The email address associated with your Heroku account.
          # If you don't want to use repository secrets (which is recommended) you can do:
          # email: my.email@example.com
          email: ${{ secrets.HEROKU_EMAIL }}
          
          # Heroku API key associated with provided user's email.
          # Api Key is available under your Heroku account settings.
          heroku_api_key: ${{ secrets.HEROKU_API_KEY }}
          
          # Name of the heroku application to which the build is to be sent.
          heroku_app_name: ${{ secrets.HEROKU_APP_NAME }}

          # (Optional, default: "./")
          # Dockerfile directory.
          # For example, if you have a Dockerfile in the root of your project, leave it as follows:
          dockerfile_directory: ./

          # (Optional, default: "Dockerfile")
          # Dockerfile name.
          dockerfile_name: Dockerfile

          # (Optional, default: "")
          # Additional options of docker build command.
          docker_options: "--no-cache"

          # (Optional, default: "web")
          # Select the process type for which you want the docker container to be uploaded.
          # By default, this argument is set to "web".
          # For more information look at https://devcenter.heroku.com/articles/process-model
          process_type: web
          
   
          
### ⬆ IMPORTANT PART ⬆ ###

```

---

## 5. Production Logging Best Practices

Logs generated across the pipeline:
- `ecc_dc_log.log`: Tracks data cleaning execution and missing value imputations.
- `ecc_eda_log.log`: Records descriptive statistical summaries and distribution skewness.
- `ecc_fe_log.log`: Logs feature selection p-values and dropped columns.
- `ecc_model_log.log`: Records model evaluation metrics, hyperparameter tuning logs, and artifact export timestamps.

### Logging Implementation in Production
```python
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        RotatingFileHandler('production_model.log', maxBytes=10_000_000, backupCount=5),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
```

---

## Key Interview Questions: MLOps & Production Engineering

1. **What is MLOps and why is it necessary?**:
   - Machine Learning Operations (MLOps) is the discipline of unifying machine learning system development (Dev) and system operations (Ops). It standardizes testing, versioning, deployment, monitoring, and automated retraining of ML models in production.
2. **Containerization with Docker**:
   - Eliminates "works on my machine" issues by packaging application code, Python interpreter, system C/C++ libraries, and exact dependency versions into an isolated, reproducible container image.
3. **CI/CD for Machine Learning**:
   - Automated testing: Unit tests for data transformation functions, model inference sanity tests, latency benchmarks.
   - Automated deployment: Building Docker container, pushing to container registry (Docker Hub, AWS ECR, GCP GCR), and deploying to container orchestration services (Kubernetes, ECS) or cloud platforms.
4. **Data Drift vs Concept Drift**:
   - **Data Drift (Covariate Shift)**: The input feature distribution $P(X)$ changes over time (e.g., users switch to mobile devices), but the relationship $P(Y|X)$ remains constant.
   - **Concept Drift**: The statistical relationship between inputs and outputs $P(Y|X)$ changes (e.g., consumer behavior shifts dramatically during economic events), degrading model performance.
