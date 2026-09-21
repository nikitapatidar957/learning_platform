# NexusLearn — Modern Interactive Developer Learning Platform

A production-ready, highly interactive, and scalable educational platform built from scratch. Features hands-on visualizers, code runners, database playgrounds, and modular course architectures covering core computer science and modern AI.

---

## 1. Project Overview

NexusLearn is designed to deliver a modern SaaS-quality learning experience for software engineers, machine learning practitioners, and AI researchers.

Key features:
- **8 Core Technical Disciplines**: Data Structures & Algorithms, Machine Learning, Deep Learning, SQL, MongoDB, Large Language Models, Generative AI & RAG, and Agentic AI.
- **Interactive Visualizers**: Dedicated step-by-step algorithms, live mathematical loss graphs, SQL execution sandbox, MongoDB document queries, transformer pipeline inspectors, and autonomous agent execution loops.
- **100% Data-Driven Architecture**: Course modules, topics, and lessons are completely driven by the FastAPI backend and MongoDB database. No courses or lessons are hardcoded in frontend pages.
- **Progress Tracking**: Real-time progress synchronization per lesson and subject with personalized learner dashboards.
- **Pluggable Authentication Abstraction**: Powered by Clerk for Version 1, with a modular FastAPI backend dependency layer allowing seamless migration to custom auth in the future.
- **Dark & Light Mode**: Curated high-contrast technical theme with smooth transitions and system preference auto-detection.
- **Global Search**: Instant multi-collection fuzzy search (`Cmd+K`) across subjects, topics, and lesson contents.
- **100% Free Access**: All learning material is unrestricted in Version 1 with zero paywalls or subscriptions.

---

## 2. Architecture

```text
                 ┌──────────────────────────────────────┐
                 │       Web and Mobile Browsers        │
                 └──────────────────┬───────────────────┘
                                    │
                                    ▼
                 ┌──────────────────────────────────────┐
                 │    Next.js 14+ Frontend (App Router) │
                 │    React 18 + TypeScript + Tailwind  │
                 │   shadcn/ui + Lucide + next-themes   │
                 └──────────────────┬───────────────────┘
                                    │
                       Clerk Auth   │  REST API
                      (Bearer JWT)  │ (JSON / HTTP)
                                    ▼
                 ┌──────────────────────────────────────┐
                 │        FastAPI Python Backend        │
                 │     Python 3.12 + Pydantic v2        │
                 │     Core Auth & Service Layer        │
                 └──────────────────┬───────────────────┘
                                    │
                                    ▼
                 ┌──────────────────────────────────────┐
                 │           MongoDB Database           │
                 │  (Atlas Cluster or Local Instance)   │
                 └──────────────────────────────────────┘
```

The frontend **never** accesses MongoDB directly. All operations are mediated through FastAPI services and Pydantic schemas.

---

## 3. Technology Stack

### Frontend
- **Framework**: Next.js 14 (App Router)
- **Library**: React 18 & TypeScript
- **Styling**: Vanilla Tailwind CSS with curated HSL design tokens
- **Icons**: Lucide React
- **Theme**: `next-themes` (Dark, Light, System)
- **Authentication**: Clerk Next.js SDK (`@clerk/nextjs`)

### Backend
- **Language**: Python 3.12+ (in isolated Conda environment)
- **API Framework**: FastAPI & Starlette
- **Server**: Uvicorn with ASGI standard workers
- **Data Validation**: Pydantic v2 (`BaseModel`, `ConfigDict`)
- **Database Driver**: PyMongo (with singleton connection pooling)
- **Testing**: pytest & pytest-asyncio

---

## 4. Python Environment Setup

Always use an isolated Conda environment:

```bash
# Create the environment
conda create -n learning-platform-env python=3.12 -y

# Activate the environment
conda activate learning-platform-env

# Verify Python version
python --version
# Expected: Python 3.12.x
```

---

## 5. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install dependencies into the activated Conda environment
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env

# Run database migrations and seed sample curriculum
python scripts/seed.py

# Start the development API server
uvicorn app.main:app --reload --port 8000
```

FastAPI server runs at: `http://localhost:8000`

---

## 6. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install Node dependencies
npm install

# Configure environment variables
cp .env.example .env.local

# Run Next.js development server
npm run dev
```

Next.js frontend runs at: `http://localhost:3000`

---

## 7. MongoDB Setup

NexusLearn supports both **MongoDB Atlas** and **Local MongoDB**:

1. **MongoDB Atlas**:
   Set `MONGODB_URI` in `backend/.env`:
   ```env
   MONGODB_URI="mongodb+srv://username:password@cluster.mongodb.net"
   MONGODB_DB_NAME="learning_platform"
   ```
   *Note: Ensure your IP is added to the MongoDB Atlas Network Access whitelist (`0.0.0.0/0` for development).*

2. **Local MongoDB**:
   Start the local MongoDB daemon:
   ```bash
   brew services start mongodb/brew/mongodb-community
   ```
   If the remote Atlas cluster is unreachable, the backend automatically detects and falls back to `mongodb://localhost:27017`.

---

## 8. Clerk Setup

1. Create a free account at [clerk.com](https://clerk.com) and create an application.
2. In the Clerk Dashboard under **API Keys**, copy your **Publishable Key** and **Secret Key**.
3. Add the Publishable Key to `frontend/.env.local`:
   ```env
   NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_...
   ```
4. Add the Secret Key to `backend/.env`:
   ```env
   CLERK_SECRET_KEY=sk_test_...
   ```
5. Google and Email logins work out of the box through Clerk.

---

## 9. Environment Variables

### Backend (`backend/.env`)
```env
# MongoDB Connection URI
MONGODB_URI="mongodb://localhost:27017"
MONGODB_DB_NAME="learning_platform"

# Clerk Secret Key (Optional in local development)
CLERK_SECRET_KEY=""

# Allowed CORS Origin
FRONTEND_URL="http://localhost:3000"
ENVIRONMENT="development"
PORT=8000
```

### Frontend (`frontend/.env.local`)
```env
# Clerk Public Key
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY="pk_test_Y2xlcmsuaGVsbG8uZGV2JA"

# Backend FastAPI URL
NEXT_PUBLIC_API_URL="http://localhost:8000"

# Clerk Route Paths
NEXT_PUBLIC_CLERK_SIGN_IN_URL="/sign-in"
NEXT_PUBLIC_CLERK_SIGN_UP_URL="/sign-up"
NEXT_PUBLIC_CLERK_AFTER_SIGN_IN_URL="/dashboard"
NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL="/dashboard"
```

---

## 10. Database Seed / Migration

The migration system is completely idempotent. Running it multiple times updates existing documents without creating duplicates:

```bash
# In learning-platform-env
python backend/scripts/seed.py
```

What the script does:
1. Connects to MongoDB and builds indexes (`slug`, `order`, compound unique index on `(user_id, lesson_id)`, text search indexes).
2. Upserts 8 core subjects.
3. Upserts modules/topics for each subject.
4. Upserts interactive lessons with explanation sections, code blocks, and visualizer configurations.

---

## 11. API Documentation

FastAPI provides automatic interactive Swagger documentation:
- **Interactive Swagger UI**: `http://localhost:8000/docs`
- **ReDoc Documentation**: `http://localhost:8000/redoc`
- **Health Check**: `http://localhost:8000/api/health`

### REST Endpoints Summary

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| `GET` | `/api/subjects` | List all available subjects | Public |
| `GET` | `/api/subjects/{slug}` | Get subject details and topics | Public |
| `GET` | `/api/subjects/{slug}/topics` | Get topics under a subject | Public |
| `GET` | `/api/topics/{slug}` | Get topic details and lessons | Public |
| `GET` | `/api/topics/{slug}/lessons` | List lessons under a topic | Public |
| `GET` | `/api/lessons/{slug}` | Get full lesson content & sections | Public |
| `GET` | `/api/progress` | Get user learning stats | Bearer Token |
| `GET` | `/api/progress/{lesson_id}` | Get progress for a lesson | Bearer Token |
| `POST` | `/api/progress/{lesson_id}` | Start / update lesson progress | Bearer Token |
| `PATCH` | `/api/progress/{lesson_id}` | Mark lesson as completed | Bearer Token |
| `GET` | `/api/search?q={query}` | Multi-collection search | Public |
| `GET` | `/api/auth/me` | Current user profile sync | Bearer Token |

---

## 12. Running Tests

Run the complete backend test suite using `pytest`:

```bash
cd backend
PYTHONPATH=. pytest tests/ -v
```

Tests cover:
- Subjects list and slug detail endpoints
- Topics and lessons hierarchy
- Progress tracking and completion toggles
- Multi-collection fuzzy search
- User upsert and duplicate prevention
- Unauthorized access enforcement (401 status)

---

## 13. Adding a New Subject

To add a new subject (e.g. `Rust Programming`), insert or seed a document into the `subjects` collection:

```python
db.subjects.update_one(
    {"slug": "rust"},
    {
        "$set": {
            "name": "Rust Systems Programming",
            "slug": "rust",
            "description": "Master memory safety, ownership, and concurrency in Rust.",
            "icon": "Cpu",
            "order": 9,
            "difficulty": "Intermediate to Advanced",
            "isPublished": True,
            "estimated_hours": "30+ hrs"
        }
    },
    upsert=True
)
```

The frontend will automatically render the new subject card and routing paths without requiring any code changes.

---

## 14. Adding a Topic

To attach a topic to a subject:

```python
db.topics.update_one(
    {"slug": "ownership-borrowing"},
    {
        "$set": {
            "subjectSlug": "rust",
            "title": "Ownership & Borrowing",
            "slug": "ownership-borrowing",
            "description": "Understand move semantics, references, and borrow checker rules.",
            "order": 1,
            "isPublished": True
        }
    },
    upsert=True
)
```

---

## 15. Adding a Lesson

To add a lesson under a topic:

```python
db.lessons.update_one(
    {"slug": "move-semantics"},
    {
        "$set": {
            "topicSlug": "ownership-borrowing",
            "subjectSlug": "rust",
            "title": "Understanding Move Semantics",
            "slug": "move-semantics",
            "description": "How Rust manages heap memory without a garbage collector.",
            "estimatedTime": "15 min",
            "difficulty": "Beginner",
            "order": 1,
            "isPublished": True,
            "interactiveType": None,
            "content": {
                "sections": [
                    {
                        "type": "explanation",
                        "title": "Stack vs Heap Ownership",
                        "content": "When a variable goes out of scope, Rust automatically calls drop()..."
                    },
                    {
                        "type": "code",
                        "language": "rust",
                        "title": "Move Example",
                        "code": "let s1 = String::from(\"hello\");\nlet s2 = s1; // s1 moved to s2"
                    }
                ]
            }
        }
    },
    upsert=True
)
```

---

## 16. Project Folder Structure

```text
learning_platform/
├── .env                          # Root environment file with MongoDB credentials
├── .gitignore                    # Git rules for Python, Node, Next.js, and secrets
├── README.md                     # Comprehensive documentation
│
├── backend/
│   ├── app/
│   │   ├── main.py               # FastAPI entrypoint, CORS, lifespan, router inclusion
│   │   ├── core/
│   │   │   ├── config.py         # Pydantic BaseSettings
│   │   │   ├── auth.py           # Clerk JWT verification & user upsert abstraction
│   │   │   └── dependencies.py   # FastAPI dependency injection
│   │   ├── database/
│   │   │   └── mongodb.py        # PyMongo singleton with auto-fallback & index manager
│   │   ├── schemas/              # Pydantic request/response models
│   │   │   ├── user.py
│   │   │   ├── subject.py
│   │   │   ├── topic.py
│   │   │   ├── lesson.py
│   │   │   ├── progress.py
│   │   │   └── search.py
│   │   ├── services/             # Pure business logic layer
│   │   │   ├── subject_service.py
│   │   │   ├── topic_service.py
│   │   │   ├── lesson_service.py
│   │   │   ├── progress_service.py
│   │   │   └── search_service.py
│   │   └── routes/               # API endpoint routers
│   │       ├── auth.py
│   │       ├── subjects.py
│   │       ├── topics.py
│   │       ├── lessons.py
│   │       ├── progress.py
│   │       └── search.py
│   ├── scripts/
│   │   └── seed.py               # Idempotent seed script
│   ├── tests/                    # pytest test suite
│   ├── requirements.txt
│   ├── .env.example
│   └── .env
│
└── frontend/
    ├── app/                      # Next.js App Router
    │   ├── layout.tsx            # Global providers, Navbar, Footer
    │   ├── page.tsx              # Landing page with interactive tech graph
    │   ├── globals.css           # Curated HSL tokens and glassmorphism
    │   ├── not-found.tsx         # Custom 404 page
    │   ├── error.tsx             # Error boundary
    │   ├── (auth)/               # Clerk Sign-In and Sign-Up pages
    │   ├── dashboard/            # Personalized learner dashboard
    │   └── courses/              # Subject, topic, and interactive lesson workspace
    ├── components/
    │   ├── layout/               # Navbar, Footer, ThemeToggle, ThemeProvider
    │   ├── navigation/           # CourseSidebar, Breadcrumb
    │   ├── courses/              # SubjectCard, TopicAccordion
    │   ├── dashboard/            # DashboardStats, ContinueLearningCard
    │   ├── lessons/              # LessonHeader, LessonContent, CompleteButton, LessonNavigation
    │   ├── code/                 # CodeBlock with syntax styling and copy button
    │   ├── search/               # SearchDialog (Cmd+K global search modal)
    │   ├── ui/                   # Button, Badge, ProgressBar, Skeleton
    │   └── visualizations/       # Interactive learning components
    │       ├── VisualizerHost.tsx
    │       ├── dsa/              # ArrayVisualizer, SortingVisualizer, BinarySearchVisualizer
    │       ├── ml/               # LinearRegressionVisualizer, ConfusionMatrixVisualizer
    │       ├── sql/              # SQLEditor playground
    │       ├── mongodb/          # MongoPlayground
    │       ├── llm/              # LLMPipelineVisualizer
    │       ├── genai/            # RAGVisualizer
    │       └── agentic/          # AgentWorkflowVisualizer
    ├── lib/
    │   ├── api.ts                # Typed client API functions
    │   ├── types.ts              # TypeScript domain types
    │   └── utils.ts              # Class merging utilities
    ├── package.json
    ├── tsconfig.json
    ├── tailwind.config.ts
    └── .env.local
```