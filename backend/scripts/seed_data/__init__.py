"""
Consolidated seed data package for the Learning Platform.
"""
from .subjects_data import SUBJECTS_DATA
from .dsa_data import DSA_TOPICS, DSA_LESSONS
from .ml_data import ML_TOPICS, ML_LESSONS
from .python_data import PYTHON_TOPICS, PYTHON_LESSONS
from .sql_data import SQL_TOPICS, SQL_LESSONS
from .genai_llm_agentic_data import ADVANCED_TOPICS, ADVANCED_LESSONS
from .git_data import GIT_TOPICS, GIT_LESSONS
from .aws_data import AWS_TOPICS, AWS_LESSONS

ALL_SUBJECTS = SUBJECTS_DATA
ALL_TOPICS = DSA_TOPICS + ML_TOPICS + PYTHON_TOPICS + SQL_TOPICS + ADVANCED_TOPICS + GIT_TOPICS + AWS_TOPICS
ALL_LESSONS = DSA_LESSONS + ML_LESSONS + PYTHON_LESSONS + SQL_LESSONS + ADVANCED_LESSONS + GIT_LESSONS + AWS_LESSONS

