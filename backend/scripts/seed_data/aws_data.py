"""
AWS & Cloud Computing Topics and Lessons Seed Data
Incorporating verbatim concepts and interview Q&As from:
- python_interview/IMAGES/aws_proper_notes.md
- python_interview/aws_notes.md
"""

AWS_TOPICS = [
    {
        "subjectSlug": "aws",
        "title": "Cloud Computing & Server Foundations",
        "slug": "aws-cloud-foundations",
        "description": "Hardware vs Software, Client-Server Architecture, Web vs App vs Database Servers, Virtualization, and Cloud Service Models (IaaS, PaaS, SaaS).",
        "order": 1,
        "isPublished": True,
    },
    {
        "subjectSlug": "aws",
        "title": "Core AWS Compute & Storage Services",
        "slug": "core-aws-services",
        "description": "AWS global infrastructure, Regions & AZs, Amazon EC2 virtual servers, Amazon S3 object storage tiers, and AWS IAM security.",
        "order": 2,
        "isPublished": True,
    },
    {
        "subjectSlug": "aws",
        "title": "AWS Networking & Cloud Architecture",
        "slug": "aws-networking-architecture",
        "description": "Amazon VPC, Public/Private Subnets, Internet Gateways, NAT Gateways, Security Groups vs NACLs, and Elastic Load Balancing.",
        "order": 3,
        "isPublished": True,
    },
]

AWS_LESSONS = [
    {
        "topicSlug": "aws-cloud-foundations",
        "subjectSlug": "aws",
        "title": "Client-Server Architecture, Web Servers & Cloud Models",
        "slug": "cloud-foundations-client-server",
        "description": "Foundational computer architecture, client vs server distinctions, web vs database servers, hypervisors, and IaaS vs PaaS vs SaaS.",
        "estimatedTime": "35 mins",
        "difficulty": "Beginner to Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Hardware vs Software in Server Architecture",
                    "content": (
                        "• Hardware: Physical computing components (CPU, RAM, Motherboard, NIC, SSD/HDD) that you can physically touch.\n"
                        "• Software: Sets of instructions and binary programs running on top of hardware.\n\n"
                        "A server is not magical hardware—it is simply a computer running dedicated server software that listens on network ports to provide services to client devices."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Web Server vs Application Server vs Database Server",
                    "content": (
                        "1. Web Server (e.g., Nginx, Apache): Handles HTTP/HTTPS requests, serves static assets (HTML, CSS, JS, images), performs SSL termination, and reverse-proxies requests.\n"
                        "2. Application Server (e.g., Uvicorn, Gunicorn, Tomcat): Executes dynamic business logic, interacts with frameworks (FastAPI, Django, Spring), processes tokens, and computes responses.\n"
                        "3. Database Server (e.g., PostgreSQL, MongoDB Atlas): Specifically optimized for persistent data storage, indexing, ACID transactions, and query processing."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Cloud Computing Service Models: IaaS vs PaaS vs SaaS",
                    "content": (
                        "• IaaS (Infrastructure as a Service): You manage OS, runtime, middleware, data, and applications. Cloud provider manages physical hardware, virtualization, and networking. (Example: AWS EC2, Google Compute Engine).\n\n"
                        "• PaaS (Platform as a Service): Provider manages OS, runtime, scaling, and patches. You only deploy code and data. (Example: AWS Elastic Beanstalk, Heroku, Vercel).\n\n"
                        "• SaaS (Software as a Service): Fully managed software delivered over the web. You only consume the service. (Example: Gmail, Salesforce, Dropbox)."
                    )
                },
                {
                    "type": "callout",
                    "variant": "info",
                    "content": "Interview Cross-Question: Can your laptop be a server? Yes! Any computer running software listening on a port (e.g., `uvicorn main:app --port 8000`) acts as a server accessible across the local network."
                }
            ]
        }
    },
    {
        "topicSlug": "core-aws-services",
        "subjectSlug": "aws",
        "title": "AWS Global Infrastructure, EC2, S3 & IAM",
        "slug": "core-aws-services-ec2-s3-iam",
        "description": "Regions, Availability Zones, Edge Locations, EC2 instance types, S3 object storage lifecycle policies, and IAM least-privilege policies.",
        "estimatedTime": "45 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "AWS Global Infrastructure: Regions vs Availability Zones",
                    "content": (
                        "• Region: A physical geographic cluster of data centers around the world (e.g., `us-east-1` in N. Virginia, `ap-south-1` in Mumbai). Each region is completely isolated from other regions.\n\n"
                        "• Availability Zone (AZ): One or more discrete data centers with redundant power, networking, and connectivity within an AWS Region. AZs are interconnected with ultra-low latency fiber-optic networking.\n\n"
                        "• Edge Locations: Endpoints for AWS CloudFront (CDN) to cache content closer to end users worldwide."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Amazon EC2 (Elastic Compute Cloud)",
                    "content": (
                        "Virtual servers in the cloud running on Xen or AWS Nitro hypervisors.\n\n"
                        "EC2 Instance Types:\n"
                        "• General Purpose (e.g., `t3`, `m5`): Balanced compute, memory, and networking.\n"
                        "• Compute Optimized (e.g., `c5`, `c6g`): High-performance CPUs for batch processing, gaming, scientific modeling.\n"
                        "• Memory Optimized (e.g., `r5`, `x1`): Fast performance for workloads processing massive datasets in memory (Redis, in-memory DBs).\n"
                        "• Accelerated Computing (e.g., `p3`, `g4`): Hardware accelerators / GPUs for machine learning and LLM training."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Amazon S3 (Simple Storage Service)",
                    "content": (
                        "Object storage built to store and retrieve any amount of data from anywhere.\n\n"
                        "Key Concepts:\n"
                        "• Buckets: Globally unique containers for objects.\n"
                        "• Objects: Files composed of data, a key (name), and metadata (up to 5 TB per object).\n"
                        "• 99.999999999% (11 9's) Durability: Data is redundantly stored across multiple physical AZs.\n"
                        "• Storage Tiers: S3 Standard, S3 Intelligent-Tiering, S3 Standard-IA, S3 Glacier, and S3 Glacier Deep Archive."
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "AWS IAM Golden Rule: Principle of Least Privilege. Never use root account credentials for daily tasks; always create IAM Users/Roles with granular policies granting only minimum necessary permissions."
                }
            ]
        }
    },
    {
        "topicSlug": "aws-networking-architecture",
        "subjectSlug": "aws",
        "title": "VPC, Subnets, Routing & Security Groups",
        "slug": "aws-vpc-networking-security",
        "description": "Design secure private cloud topologies: VPC CIDR blocks, Public vs Private subnets, IGW, NAT Gateways, and Stateful Security Groups vs Stateless NACLs.",
        "estimatedTime": "40 mins",
        "difficulty": "Intermediate to Advanced",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Amazon Virtual Private Cloud (VPC)",
                    "content": (
                        "A VPC is a logically isolated virtual network dedicated to your AWS account.\n\n"
                        "• CIDR Block: Defines the IP address range (e.g., `10.0.0.0/16` gives 65,536 private IP addresses).\n"
                        "• Public Subnet: Has a route in its Route Table directing `0.0.0.0/0` traffic to an Internet Gateway (IGW). Instances receive Public IPs.\n"
                        "• Private Subnet: No direct route to the Internet Gateway. Instances (like backend servers and DBs) cannot be reached directly from the public internet."
                    )
                },
                {
                    "type": "explanation",
                    "title": "NAT Gateway vs Internet Gateway",
                    "content": (
                        "• Internet Gateway (IGW): Horizontally scaled, redundant VPC component that enables communication between your VPC and the internet (bi-directional).\n\n"
                        "• NAT Gateway (Network Address Translation): Placed in a Public Subnet to allow outbound internet access for instances in Private Subnets (e.g., downloading OS security updates) while preventing inbound connections from initiating from outside."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Security Groups vs Network ACLs (NACLs)",
                    "content": (
                        "• Security Group: Virtual firewall for instances. Stateful (if you send a request, return traffic is automatically allowed). Evaluates all rules before deciding.\n\n"
                        "• Network ACL (NACL): Firewall for subnets. Stateless (inbound and outbound rules must be explicitly defined). Rules evaluated in numerical order."
                    )
                },
                {
                    "type": "code",
                    "title": "Production 3-Tier VPC Architecture Blueprint",
                    "language": "text",
                    "code": (
                        "Internet\n"
                        "   │\n"
                        "   ▼\n"
                        "Internet Gateway (IGW)\n"
                        "   │\n"
                        "   ▼\n"
                        "[Tier 1: Public Subnets] ──> Application Load Balancer (ALB) + NAT Gateway\n"
                        "   │\n"
                        "   ▼\n"
                        "[Tier 2: Private App Subnets] ──> EC2 Auto Scaling Group / ECS Containers\n"
                        "   │\n"
                        "   ▼\n"
                        "[Tier 3: Isolated DB Subnets] ──> Multi-AZ Amazon RDS (PostgreSQL/MySQL)"
                    )
                }
            ]
        }
    }
]
