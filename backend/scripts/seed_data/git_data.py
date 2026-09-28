"""
Git & Version Control Topics and Lessons Seed Data
Incorporating verbatim concepts from:
- python_interview/github.md
"""

GIT_TOPICS = [
    {
        "subjectSlug": "git",
        "title": "Git Architecture & The Object Model",
        "slug": "git-architecture-internals",
        "description": "Distributed VCS motivation, data integrity (SHA-1), Blobs, Trees, Commits DAG, and the 4 Git environments.",
        "order": 1,
        "isPublished": True,
    },
    {
        "subjectSlug": "git",
        "title": "Branching, Merging & Collaboration",
        "slug": "git-branching-merging-workflow",
        "description": "Pointer-based branches, fast-forward vs 3-way recursive merges, conflict resolution, and git rebase vs merge.",
        "order": 2,
        "isPublished": True,
    },
]

GIT_LESSONS = [
    {
        "topicSlug": "git-architecture-internals",
        "subjectSlug": "git",
        "title": "Git Architecture, Motivation & The Object Database",
        "slug": "git-architecture-and-workflows",
        "description": "Why Linus Torvalds built Git in 2005, centralized vs distributed VCS, content-addressable storage, and DAG commit graphs.",
        "estimatedTime": "30 mins",
        "difficulty": "Beginner to Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "History & Motivation Behind Git",
                    "content": (
                        "Created by Linus Torvalds in 2005 for the Linux kernel development community, Git replaced BitKeeper. "
                        "Earlier tools (like CVS and SVN) were Centralized Version Control Systems (CVCS) with major architectural flaws:\n\n"
                        "• Single Point of Failure: If the central server went down, developers couldn't commit, branch, or view history.\n"
                        "• Heavyweight Branching: Creating a branch in SVN duplicated the entire directory on the server.\n"
                        "• Slow Performance: Every diff and commit required a round-trip network call.\n\n"
                        "Git's Distributed Architecture (DVCS): Every developer has a complete, local clone of the entire repository history. "
                        "Branching, committing, viewing logs, and diffing happen locally on disk in milliseconds without internet access."
                    )
                },
                {
                    "type": "explanation",
                    "title": "The 4 Areas of Git",
                    "content": (
                        "1. Working Directory: The actual files on your local filesystem that you edit in VS Code.\n"
                        "2. Staging Area (Index): A binary file (`.git/index`) that tracks exactly what changes will go into the next commit.\n"
                        "3. Local Repository: Permanent compressed snapshots stored in `.git/objects`.\n"
                        "4. Remote Repository: The shared central hub (GitHub, GitLab) where commits are pushed and pulled."
                    )
                },
                {
                    "type": "explanation",
                    "title": "The Git Object Model: Blobs, Trees, and Commits",
                    "content": (
                        "Git is fundamentally a content-addressable key-value store:\n\n"
                        "• Blob (Binary Large Object): Stores raw file content compressed with zlib. Identifiers are the SHA-1 hash of the file content.\n"
                        "• Tree: A directory listing containing mode, type, SHA-1 hash, and filename for blobs or sub-trees.\n"
                        "• Commit: Metadata snapshot pointing to the root Tree object, author, committer, timestamp, message, and parent commit SHA(s).\n"
                        "• Annotated Tag: Permanent named pointer to a specific commit object with a cryptographic signature."
                    )
                },
                {
                    "type": "code",
                    "title": "Inspecting Git Objects with low-level Plumbing Commands",
                    "language": "bash",
                    "code": (
                        "# View the type of any Git SHA object\n"
                        "git cat-file -t <hash>\n\n"
                        "# View the raw content of any Git SHA object\n"
                        "git cat-file -p <hash>\n\n"
                        "# Example Tree output:\n"
                        "# 100644 blob a1b2c3d...    main.py\n"
                        "# 040000 tree e5f6a7b...    components\n\n"
                        "# View visual commit graph\n"
                        "git log --graph --oneline --decorate --all"
                    )
                },
                {
                    "type": "callout",
                    "variant": "info",
                    "content": "Data Integrity: Git uses SHA-1/SHA-256 cryptographic hashes. It is physically impossible to change a file or commit without changing its hash and all downstream commit hashes."
                }
            ]
        }
    },
    {
        "topicSlug": "git-branching-merging-workflow",
        "subjectSlug": "git",
        "title": "Branching, Merging, Conflict Resolution & Rebasing",
        "slug": "git-branching-merging",
        "description": "Understand lightweight pointer branching, fast-forward vs 3-way merges, resolving merge conflicts, and rebase tradeoffs.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Why Git Branching is Cost-Free",
                    "content": (
                        "In Git, a branch is NOT a copy of your files. A branch is simply a 41-byte text file in `.git/refs/heads/` "
                        "containing a 40-character commit hash! Creating a branch takes 1 write operation and zero disk overhead.\n\n"
                        "The special pointer `HEAD` tracks which branch/commit you are currently looking at."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Fast-Forward vs 3-Way Recursive Merges",
                    "content": (
                        "• Fast-Forward Merge: Occurs when no new commits exist on the target branch (e.g., `main`). "
                        "Git simply moves the `main` pointer forward to your feature branch's latest commit. No merge commit is generated.\n\n"
                        "• 3-Way Merge: Occurs when both branches have diverged with independent commits. "
                        "Git finds the Best Common Ancestor (Base), combines the two diffs, and creates a new synthetic Merge Commit with two parents."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Resolving Merge Conflicts Step-by-Step",
                    "content": (
                        "A conflict happens when two branches edit the exact same lines in a file. Git pauses and writes conflict markers:\n\n"
                        "```\n"
                        "<<<<<<< HEAD (Current branch)\n"
                        "const API_URL = 'https://api.v2.nexuslearn.com';\n"
                        "=======\n"
                        "const API_URL = 'https://api.prod.nexuslearn.com';\n"
                        ">>>>>>> feature-env (Incoming branch)\n"
                        "```\n\n"
                        "Resolution Steps:\n"
                        "1. Open file and decide on the correct code.\n"
                        "2. Delete all markers (`<<<<<<<`, `=======`, `>>>>>>>`).\n"
                        "3. Save the file.\n"
                        "4. Run `git add <file>` to mark conflict as resolved.\n"
                        "5. Run `git commit` to finalize the merge!"
                    )
                },
                {
                    "type": "code",
                    "title": "Git Rebase vs Git Merge",
                    "language": "bash",
                    "code": (
                        "# Merge: Preserves complete historical context with merge commits\n"
                        "git checkout main\n"
                        "git merge feature-auth\n\n"
                        "# Rebase: Rewrites commits on top of main for a clean linear history\n"
                        "git checkout feature-auth\n"
                        "git rebase main\n"
                        "# Golden Rule: NEVER rebase commits that have been pushed to a shared public branch!"
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "Interview Question: What is a detached HEAD state? It occurs when `HEAD` points directly to a specific commit hash rather than a named branch reference. Commits made in this state will be lost if not attached to a branch!"
                }
            ]
        }
    }
]
