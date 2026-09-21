#!/usr/bin/env python3
"""
Database Seed & Migration Script for the Learning Platform.
Idempotent script to create indexes and populate subjects, topics, and lessons.
"""
import sys
import os
from datetime import datetime, timezone

# Ensure backend root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dotenv import load_dotenv
load_dotenv()

from app.core.config import settings
from app.database.mongodb import db_manager


def seed_database():
    print(f"Connecting to MongoDB at: {settings.MONGODB_URI.split('@')[-1] if '@' in settings.MONGODB_URI else settings.MONGODB_URI}")
    db = db_manager.connect()
    db_manager.create_indexes()
    now = datetime.now(timezone.utc).isoformat()

    # =========================================================================
    # 1. SUBJECTS SEED DATA
    # =========================================================================
    subjects_data = [
        {
            "name": "Data Structures & Algorithms",
            "slug": "dsa",
            "description": "Master essential data structures and algorithms using Python with interactive visualizations.",
            "icon": "Binary",
            "order": 1,
            "difficulty": "Beginner to Advanced",
            "isPublished": True,
            "estimated_hours": "40+ hrs",
        },
        {
            "name": "Machine Learning",
            "slug": "machine-learning",
            "description": "Understand core statistical learning theory, regression, classification, and model evaluation.",
            "icon": "Brain",
            "order": 2,
            "difficulty": "Intermediate",
            "isPublished": True,
            "estimated_hours": "30+ hrs",
        },
        {
            "name": "Deep Learning",
            "slug": "deep-learning",
            "description": "Dive into deep neural networks, backpropagation, convolutional layers, and architectures.",
            "icon": "Cpu",
            "order": 3,
            "difficulty": "Intermediate to Advanced",
            "isPublished": True,
            "estimated_hours": "35+ hrs",
        },
        {
            "name": "SQL & Relational Databases",
            "slug": "sql",
            "description": "Master structured querying, schema design, complex joins, indexing, and query optimization.",
            "icon": "Database",
            "order": 4,
            "difficulty": "Beginner to Intermediate",
            "isPublished": True,
            "estimated_hours": "20+ hrs",
        },
        {
            "name": "MongoDB & NoSQL",
            "slug": "mongodb",
            "description": "Learn flexible JSON document modeling, indexing strategies, and high-performance aggregation pipelines.",
            "icon": "Layers",
            "order": 5,
            "difficulty": "Beginner to Intermediate",
            "isPublished": True,
            "estimated_hours": "20+ hrs",
        },
        {
            "name": "Large Language Models",
            "slug": "llm",
            "description": "Explore transformer foundations, tokenization, self-attention, and language model mechanics.",
            "icon": "Sparkles",
            "order": 6,
            "difficulty": "Intermediate to Advanced",
            "isPublished": True,
            "estimated_hours": "25+ hrs",
        },
        {
            "name": "Generative AI & RAG",
            "slug": "generative-ai",
            "description": "Build modern GenAI apps with prompt engineering, vector search, embeddings, and RAG architectures.",
            "icon": "Wand2",
            "order": 7,
            "difficulty": "Intermediate",
            "isPublished": True,
            "estimated_hours": "25+ hrs",
        },
        {
            "name": "Agentic AI",
            "slug": "agentic-ai",
            "description": "Design autonomous AI agents with reasoning loops, tool calling, memory systems, and multi-agent coordination.",
            "icon": "Bot",
            "order": 8,
            "difficulty": "Advanced",
            "isPublished": True,
            "estimated_hours": "30+ hrs",
        },
    ]

    print("\n--- Seeding Subjects ---")
    subject_id_map = {}
    for sub in subjects_data:
        res = db.subjects.find_one_and_update(
            {"slug": sub["slug"]},
            {
                "$set": {
                    **sub,
                    "updatedAt": now,
                },
                "$setOnInsert": {"createdAt": now}
            },
            upsert=True,
            return_document=True
        )
        subject_id_map[sub["slug"]] = res["_id"]
        print(f"  ✓ Subject: {sub['name']} ({sub['slug']})")

    # =========================================================================
    # 2. TOPICS SEED DATA
    # =========================================================================
    topics_data = [
        # DSA Topics
        {
            "subjectSlug": "dsa",
            "title": "Foundations of Algorithms",
            "slug": "foundations",
            "description": "Core computing concepts, Big-O asymptotic analysis, and memory trade-offs.",
            "order": 1,
            "isPublished": True,
        },
        {
            "subjectSlug": "dsa",
            "title": "Arrays & Two-Pointers",
            "slug": "arrays",
            "description": "Contiguous memory layout, dynamic arrays, sliding windows, and two-pointer patterns.",
            "order": 2,
            "isPublished": True,
        },
        {
            "subjectSlug": "dsa",
            "title": "Searching Algorithms",
            "slug": "searching",
            "description": "Linear search, binary search, and search-space reduction patterns.",
            "order": 3,
            "isPublished": True,
        },
        {
            "subjectSlug": "dsa",
            "title": "Sorting Algorithms",
            "slug": "sorting",
            "description": "Comparison vs non-comparison sorts, bubble sort, merge sort, and quicksort mechanics.",
            "order": 4,
            "isPublished": True,
        },
        # Machine Learning Topics
        {
            "subjectSlug": "machine-learning",
            "title": "ML Foundations",
            "slug": "ml-foundations",
            "description": "Core concepts, supervised vs unsupervised learning, and data pipelines.",
            "order": 1,
            "isPublished": True,
        },
        {
            "subjectSlug": "machine-learning",
            "title": "Regression & Evaluation",
            "slug": "regression",
            "description": "Linear regression, loss functions, gradient descent, and evaluation metrics.",
            "order": 2,
            "isPublished": True,
        },
        {
            "subjectSlug": "machine-learning",
            "title": "Classification Metrics",
            "slug": "classification",
            "description": "Binary and multi-class classification, confusion matrix, precision, and recall.",
            "order": 3,
            "isPublished": True,
        },
        # Deep Learning Topics
        {
            "subjectSlug": "deep-learning",
            "title": "Neural Network Fundamentals",
            "slug": "neural-networks",
            "description": "Perceptrons, activation functions, forward pass, and backpropagation.",
            "order": 1,
            "isPublished": True,
        },
        # SQL Topics
        {
            "subjectSlug": "sql",
            "title": "SQL Query Foundations",
            "slug": "sql-queries",
            "description": "SELECT statements, filtering with WHERE, sorting, and data aggregation.",
            "order": 1,
            "isPublished": True,
        },
        # MongoDB Topics
        {
            "subjectSlug": "mongodb",
            "title": "CRUD & Querying",
            "slug": "mongodb-crud",
            "description": "Document structures, query selectors, projections, and updates.",
            "order": 1,
            "isPublished": True,
        },
        # LLM Topics
        {
            "subjectSlug": "llm",
            "title": "LLM Architecture Pipeline",
            "slug": "llm-architecture",
            "description": "From input prompt to tokenization, embeddings, self-attention, and text generation.",
            "order": 1,
            "isPublished": True,
        },
        # Generative AI Topics
        {
            "subjectSlug": "generative-ai",
            "title": "Retrieval-Augmented Generation (RAG)",
            "slug": "rag-architecture",
            "description": "Vector indexing, similarity search, prompt grounding, and hallucination reduction.",
            "order": 1,
            "isPublished": True,
        },
        # Agentic AI Topics
        {
            "subjectSlug": "agentic-ai",
            "title": "Autonomous Agent Workflows",
            "slug": "agent-workflows",
            "description": "Perception, planning, tool selection, action execution, and environment feedback.",
            "order": 1,
            "isPublished": True,
        },
    ]

    print("\n--- Seeding Topics ---")
    topic_id_map = {}
    for top in topics_data:
        sub_id = subject_id_map.get(top["subjectSlug"])
        res = db.topics.find_one_and_update(
            {"slug": top["slug"]},
            {
                "$set": {
                    **top,
                    "subjectId": sub_id,
                    "updatedAt": now,
                },
                "$setOnInsert": {"createdAt": now}
            },
            upsert=True,
            return_document=True
        )
        topic_id_map[top["slug"]] = res["_id"]
        print(f"  ✓ Topic: {top['title']} ({top['slug']}) under [{top['subjectSlug']}]")

    # =========================================================================
    # 3. LESSONS SEED DATA (With Interactive Visualizer Configs)
    # =========================================================================
    lessons_data = [
        # --- DSA: Foundations ---
        {
            "topicSlug": "foundations",
            "subjectSlug": "dsa",
            "title": "What is DSA?",
            "slug": "what-is-dsa",
            "description": "Introduction to data structures, algorithms, and computational thinking.",
            "estimatedTime": "10 min",
            "difficulty": "Beginner",
            "order": 1,
            "isPublished": True,
            "interactiveType": None,
            "content": {
                "sections": [
                    {
                        "type": "explanation",
                        "title": "The Pillars of Software Engineering",
                        "content": "A **data structure** is a specialized format for organizing, processing, retrieving, and storing data in memory. An **algorithm** is a finite sequence of well-defined, unambiguous computer instructions to solve a class of problems or perform a computation.\n\nTogether, they determine the efficiency, scalability, and elegance of software applications."
                    },
                    {
                        "type": "callout",
                        "variant": "info",
                        "content": "Nicklaus Wirth famously stated: 'Algorithms + Data Structures = Programs'."
                    },
                    {
                        "type": "code",
                        "title": "Example: Linear Search vs Hash Lookup",
                        "language": "python",
                        "code": "# Linear scan: O(n) time\ndef find_linear(items, target):\n    for item in items:\n        if item == target:\n            return True\n    return False\n\n# Hash set lookup: O(1) average time\ndef find_hashed(item_set, target):\n    return target in item_set"
                    }
                ]
            }
        },
        {
            "topicSlug": "foundations",
            "subjectSlug": "dsa",
            "title": "Time and Space Complexity",
            "slug": "time-and-space-complexity",
            "description": "Master Big-O notation to evaluate algorithmic performance at scale.",
            "estimatedTime": "15 min",
            "difficulty": "Beginner",
            "order": 2,
            "isPublished": True,
            "interactiveType": None,
            "content": {
                "sections": [
                    {
                        "type": "explanation",
                        "title": "Asymptotic Analysis & Big-O",
                        "content": "Big-O notation describes the upper bound of execution time or memory space an algorithm requires as the input size `n` grows towards infinity.\n\n- **O(1)**: Constant time (e.g. array index lookup)\n- **O(log n)**: Logarithmic time (e.g. Binary Search)\n- **O(n)**: Linear time (e.g. iterating over an array)\n- **O(n log n)**: Linearithmic time (e.g. Merge Sort, Quick Sort)\n- **O(n²)**: Quadratic time (e.g. nested loops, Bubble Sort)"
                    },
                    {
                        "type": "callout",
                        "variant": "tip",
                        "content": "Always focus on the dominant term and ignore constant factors. For instance, 3n² + 5n + 100 simplifies to O(n²)."
                    }
                ]
            }
        },

        # --- DSA: Arrays (Interactive Array Visualizer) ---
        {
            "topicSlug": "arrays",
            "subjectSlug": "dsa",
            "title": "What is an Array?",
            "slug": "what-is-an-array",
            "description": "Understand contiguous memory representation and O(1) index access with an interactive visualizer.",
            "estimatedTime": "15 min",
            "difficulty": "Beginner",
            "order": 1,
            "isPublished": True,
            "interactiveType": "ArrayVisualizer",
            "content": {
                "sections": [
                    {
                        "type": "explanation",
                        "title": "Contiguous Memory Representation",
                        "content": "An array stores elements in contiguous memory blocks. Because every element occupies an identical number of bytes, the computer can instantly compute the physical memory address of any element in **O(1) constant time** using the formula:\n\n`Address(A[i]) = BaseAddress + (i * ElementSize)`"
                    },
                    {
                        "type": "visualization",
                        "component": "ArrayVisualizer",
                        "initialState": {
                            "items": [10, 25, 38, 42, 67, 89]
                        }
                    },
                    {
                        "type": "code",
                        "title": "Python List Operations",
                        "language": "python",
                        "code": "arr = [10, 25, 38, 42, 67, 89]\n\n# O(1) Index Access\nprint(arr[3])  # 42\n\n# O(1) Amortized Append\narr.append(99)\n\n# O(n) Insertion at index\narr.insert(1, 15)  # Shifts elements right"
                    },
                    {
                        "type": "callout",
                        "variant": "tip",
                        "content": "Interact with the Array Visualizer above to inspect indices, append values, delete elements, and observe memory index shifts in real time!"
                    }
                ]
            }
        },
        {
            "topicSlug": "arrays",
            "subjectSlug": "dsa",
            "title": "Two Pointer Technique",
            "slug": "two-pointer-technique",
            "description": "Solve array and string problems in O(n) time using converging and fast/slow pointer pairs.",
            "estimatedTime": "20 min",
            "difficulty": "Intermediate",
            "order": 2,
            "isPublished": True,
            "interactiveType": "ArrayVisualizer",
            "content": {
                "sections": [
                    {
                        "type": "explanation",
                        "title": "The Converging Pointers Pattern",
                        "content": "The Two Pointer pattern uses two reference points to traverse an array or list simultaneously. In a sorted array, placing one pointer at the left (`left = 0`) and one at the right (`right = len(arr) - 1`) enables finding pairs that sum to a target in **O(n) time** without nested O(n²) loops."
                    },
                    {
                        "type": "code",
                        "title": "Two Sum on Sorted Array",
                        "language": "python",
                        "code": "def two_sum_sorted(numbers: list[int], target: int):\n    left, right = 0, len(numbers) - 1\n    while left < right:\n        current_sum = numbers[left] + numbers[right]\n        if current_sum == target:\n            return (left, right)\n        elif current_sum < target:\n            left += 1\n        else:\n            right -= 1\n    return None"
                    }
                ]
            }
        },

        # --- DSA: Searching (Interactive Binary Search Visualizer) ---
        {
            "topicSlug": "searching",
            "subjectSlug": "dsa",
            "title": "Binary Search",
            "slug": "binary-search",
            "description": "Divide and conquer sorted data in logarithmic O(log n) time with interactive step-by-step pointers.",
            "estimatedTime": "20 min",
            "difficulty": "Beginner",
            "order": 1,
            "isPublished": True,
            "interactiveType": "BinarySearchVisualizer",
            "content": {
                "sections": [
                    {
                        "type": "explanation",
                        "title": "Divide and Conquer Search",
                        "content": "Binary Search operates on sorted sequences. By comparing the target value against the middle element, it eliminates half of the remaining elements in each step, guaranteeing search completion in at most **log₂(n)** comparisons."
                    },
                    {
                        "type": "visualization",
                        "component": "BinarySearchVisualizer",
                        "initialState": {
                            "items": [3, 8, 14, 21, 35, 47, 56, 68, 72, 85, 94]
                        }
                    },
                    {
                        "type": "code",
                        "title": "Standard Binary Search in Python",
                        "language": "python",
                        "code": "def binary_search(arr: list[int], target: int) -> int:\n    low, high = 0, len(arr) - 1\n    while low <= high:\n        mid = (low + high) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            low = mid + 1\n        else:\n            high = mid - 1\n    return -1"
                    }
                ]
            }
        },

        # --- DSA: Sorting (Interactive Sorting Visualizer) ---
        {
            "topicSlug": "sorting",
            "subjectSlug": "dsa",
            "title": "Sorting Visualizer",
            "slug": "sorting-visualizer",
            "description": "Watch sorting algorithms organize data bar-by-bar with interactive play, pause, and step controls.",
            "estimatedTime": "25 min",
            "difficulty": "Intermediate",
            "order": 1,
            "isPublished": True,
            "interactiveType": "SortingVisualizer",
            "content": {
                "sections": [
                    {
                        "type": "explanation",
                        "title": "Visualizing Comparison Sorts",
                        "content": "Sorting reorganizes elements into non-decreasing order. Compare the mechanics of Bubble Sort (repeated pairwise swaps) vs Selection Sort (finding the minimum element in each pass) directly in the interactive visualizer below."
                    },
                    {
                        "type": "visualization",
                        "component": "SortingVisualizer",
                        "initialState": {
                            "items": [45, 12, 85, 32, 89, 21, 67, 3, 58, 74]
                        }
                    }
                ]
            }
        },

        # --- Machine Learning: Linear Regression (Interactive ML Visualizer) ---
        {
            "topicSlug": "regression",
            "subjectSlug": "machine-learning",
            "title": "Linear Regression & Best-Fit Line",
            "slug": "linear-regression",
            "description": "Interactive best-fit line adjustment, slope/intercept tuning, and real-time Mean Squared Error (MSE) calculation.",
            "estimatedTime": "25 min",
            "difficulty": "Intermediate",
            "order": 1,
            "isPublished": True,
            "interactiveType": "LinearRegressionVisualizer",
            "content": {
                "sections": [
                    {
                        "type": "explanation",
                        "title": "Modeling Linear Relationships",
                        "content": "Linear regression fits a linear equation `y = mx + b` to observed data points. The optimal parameters `m` (slope) and `b` (intercept) minimize the **Mean Squared Error (MSE)** loss function across all training samples."
                    },
                    {
                        "type": "visualization",
                        "component": "LinearRegressionVisualizer",
                        "initialState": {
                            "slope": 1.2,
                            "intercept": 20
                        }
                    },
                    {
                        "type": "code",
                        "title": "Linear Regression with scikit-learn",
                        "language": "python",
                        "code": "from sklearn.linear_model import LinearRegression\nimport numpy as np\n\nX = np.array([[1], [2], [3], [4], [5]])\ny = np.array([2.1, 3.9, 6.2, 7.8, 10.1])\n\nmodel = LinearRegression()\nmodel.fit(X, y)\n\nprint(f'Slope (m): {model.coef_[0]:.2f}')\nprint(f'Intercept (b): {model.intercept_:.2f}')"
                    }
                ]
            }
        },

        # --- Machine Learning: Classification (Interactive Confusion Matrix) ---
        {
            "topicSlug": "classification",
            "subjectSlug": "machine-learning",
            "title": "The Confusion Matrix",
            "slug": "confusion-matrix",
            "description": "Interactive breakdown of True Positives, False Positives, Precision, Recall, and F1-Score.",
            "estimatedTime": "20 min",
            "difficulty": "Intermediate",
            "order": 1,
            "isPublished": True,
            "interactiveType": "ConfusionMatrixVisualizer",
            "content": {
                "sections": [
                    {
                        "type": "explanation",
                        "title": "Beyond Simple Accuracy",
                        "content": "When evaluating classification models on imbalanced datasets, overall accuracy can be misleading. A **Confusion Matrix** categorizes predictions into True Positives (TP), False Positives (FP), True Negatives (TN), and False Negatives (FN), enabling precise calculation of **Precision**, **Recall**, and **F1-Score**."
                    },
                    {
                        "type": "visualization",
                        "component": "ConfusionMatrixVisualizer",
                        "initialState": {
                            "tp": 85,
                            "fp": 12,
                            "fn": 8,
                            "tn": 145
                        }
                    }
                ]
            }
        },

        # --- SQL: Query Foundations (Interactive SQL Editor) ---
        {
            "topicSlug": "sql-queries",
            "subjectSlug": "sql",
            "title": "Interactive SQL Editor",
            "slug": "sql-editor-playground",
            "description": "Run structured SQL queries against sample relational tables and inspect formatted result sets in real time.",
            "estimatedTime": "25 min",
            "difficulty": "Beginner",
            "order": 1,
            "isPublished": True,
            "interactiveType": "SQLEditor",
            "content": {
                "sections": [
                    {
                        "type": "explanation",
                        "title": "Querying Relational Data with SQL",
                        "content": "SQL (Structured Query Language) is the standard declarative language for interacting with relational databases. Use the interactive editor below to write and execute SQL queries against sample tables such as `employees` and `departments`."
                    },
                    {
                        "type": "visualization",
                        "component": "SQLEditor",
                        "initialState": {
                            "defaultQuery": "SELECT name, department, salary, experience_years\nFROM employees\nWHERE salary > 65000\nORDER BY salary DESC;"
                        }
                    }
                ]
            }
        },

        # --- MongoDB: CRUD (Interactive Mongo Playground) ---
        {
            "topicSlug": "mongodb-crud",
            "subjectSlug": "mongodb",
            "title": "MongoDB Document Playground",
            "slug": "mongodb-playground",
            "description": "Query JSON collections with MongoDB query operators like $gt, $in, and $regex with live document inspection.",
            "estimatedTime": "20 min",
            "difficulty": "Beginner",
            "order": 1,
            "isPublished": True,
            "interactiveType": "MongoPlayground",
            "content": {
                "sections": [
                    {
                        "type": "explanation",
                        "title": "Document-Oriented Database Queries",
                        "content": "MongoDB stores data in flexible, JSON-like BSON documents. Instead of rigid tabular schemas, documents can hold nested arrays and sub-documents. Use the interactive playground below to test query expressions."
                    },
                    {
                        "type": "visualization",
                        "component": "MongoPlayground",
                        "initialState": {
                            "query": '{\n  "skills": { "$in": ["Python", "FastAPI"] },\n  "experience": { "$gte": 3 }\n}'
                        }
                    }
                ]
            }
        },

        # --- LLM: Architecture Pipeline (Interactive LLM Pipeline Visualizer) ---
        {
            "topicSlug": "llm-architecture",
            "subjectSlug": "llm",
            "title": "The LLM Pipeline",
            "slug": "llm-pipeline",
            "description": "Explore the end-to-end transformer workflow: Prompt → Tokenization → Embeddings → Attention → Transformer → Generation.",
            "estimatedTime": "30 min",
            "difficulty": "Intermediate",
            "order": 1,
            "isPublished": True,
            "interactiveType": "LLMPipelineVisualizer",
            "content": {
                "sections": [
                    {
                        "type": "explanation",
                        "title": "How Large Language Models Process Text",
                        "content": "LLMs do not read letters or words directly. Raw input prompts pass through a multistage neural pipeline: byte-pair encoding tokenization, vector embeddings, multi-head self-attention layers, feed-forward transformers, and softmax token generation."
                    },
                    {
                        "type": "visualization",
                        "component": "LLMPipelineVisualizer",
                        "initialState": {
                            "prompt": "Explain how transformers process language tokens."
                        }
                    }
                ]
            }
        },

        # --- Generative AI: RAG (Interactive RAG Visualizer) ---
        {
            "topicSlug": "rag-architecture",
            "subjectSlug": "generative-ai",
            "title": "RAG: Retrieval-Augmented Generation",
            "slug": "rag-pipeline",
            "description": "Interactive workflow demonstrating semantic vector search, knowledge retrieval, context injection, and answer grounding.",
            "estimatedTime": "25 min",
            "difficulty": "Intermediate",
            "order": 1,
            "isPublished": True,
            "interactiveType": "RAGVisualizer",
            "content": {
                "sections": [
                    {
                        "type": "explanation",
                        "title": "Grounding LLMs with External Knowledge",
                        "content": "Retrieval-Augmented Generation (RAG) combines dense vector retrieval with LLM generation to provide private, up-to-date, domain-specific answers while preventing hallucinations."
                    },
                    {
                        "type": "visualization",
                        "component": "RAGVisualizer",
                        "initialState": {
                            "sampleQuery": "What is the return policy for international orders?"
                        }
                    }
                ]
            }
        },

        # --- Agentic AI: Agent Workflows (Interactive Agent Visualizer) ---
        {
            "topicSlug": "agent-workflows",
            "subjectSlug": "agentic-ai",
            "title": "Autonomous Agent Loop",
            "slug": "agent-workflow-loop",
            "description": "Step through Goal Formulation, Reasoning & Planning, Tool Calling, Environment Observation, and Final Answer.",
            "estimatedTime": "30 min",
            "difficulty": "Advanced",
            "order": 1,
            "isPublished": True,
            "interactiveType": "AgentWorkflowVisualizer",
            "content": {
                "sections": [
                    {
                        "type": "explanation",
                        "title": "The ReAct (Reason + Act) Paradigm",
                        "content": "Agentic AI systems move beyond single-turn responses by executing an iterative loop: formulating a hypothesis, selecting and invoking tools (APIs, search, calculators), observing outputs, and updating plans until the objective is reached."
                    },
                    {
                        "type": "visualization",
                        "component": "AgentWorkflowVisualizer",
                        "initialState": {
                            "userGoal": "Find the average stock price of AAPL over the last 30 days and calculate the volatility."
                        }
                    }
                ]
            }
        },
    ]

    print("\n--- Seeding Lessons ---")
    for les in lessons_data:
        t_id = topic_id_map.get(les["topicSlug"])
        res = db.lessons.find_one_and_update(
            {"slug": les["slug"]},
            {
                "$set": {
                    **les,
                    "topicId": t_id,
                    "updatedAt": now,
                },
                "$setOnInsert": {"createdAt": now}
            },
            upsert=True,
            return_document=True
        )
        print(f"  ✓ Lesson: {les['title']} ({les['slug']}) [Interactive: {les['interactiveType'] or 'None'}]")

    print("\n=======================================================")
    print("Database seeding completed successfully and idempotently!")
    print("=======================================================")


if __name__ == "__main__":
    seed_database()
