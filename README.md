# ✍️ Blog Forge AI
### Multi-Agent AI System for Automated Research and Blog Generation

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-green)
![LLM](https://img.shields.io/badge/LLM-Powered-orange)
![Generative AI](https://img.shields.io/badge/Generative-AI-purple)

---

## 📑 Table of Contents

- [🚀 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🧠 AI Concepts Demonstrated](#-ai-concepts-demonstrated)
- [📈 Engineering Highlights](#-engineering-highlights)
- [🚀 Running the Application](#-running-the-application)
- [📸 Demo](#-demo)
- [📄 License](#-license)
  
---

## 🚀 Overview

**Blog Forge AI** is an end-to-end **multi-agent content generation system** built using **LangGraph** that transforms a simple topic into a detailed, publication-ready blog post.

The application autonomously:

- Conducts real-time web research
- Plans the blog structure
- Generates content in parallel
- Creates and inserts relevant images
- Produces a downloadable Markdown blog

---

## 🎯 Problem Statement

Creating high-quality technical blogs requires:

- Researching the latest information
- Organizing content into sections
- Writing long-form content
- Creating visuals
- Formatting and publishing

These tasks are time-consuming and difficult to automate with a single LLM call.

**Blog Forge AI** addresses this challenge by orchestrating multiple specialized AI agents that collaborate to autonomously generate complete, image-enhanced blogs.

---

## ✨ Features

### 🔍 Real-Time Research
- Performs web research on the given topic.
- Retrieves the latest information from the internet.
- Breaks broad topics into focused research questions.

### 🧠 Intelligent Blog Planning
- Generates a structured blog outline.
- Determines:
  - Section hierarchy
  - Content flow
  - Approximate word allocation.

### ⚡ Parallel Content Generation
- Dynamically creates worker agents.
- Each worker writes one section of the blog.
- Multiple sections are generated simultaneously.

### 🖼️ AI-Powered Image Generation
- Identifies where visuals are required.
- Generates contextual images.
- Automatically embeds images into the blog.

### 📄 Downloadable Output
- Exports the final blog as:
  - Markdown document
  - Associated image assets
- Ready for publishing on GitHub, Medium, or personal websites.

### 📊 Execution Monitoring
- Displays:
  - Agent execution logs
  - Research evidence
  - Generated images
  - Markdown preview

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-------------|
| Programming Language | Python |
| Agent Orchestration | LangGraph |
| LLM Framework | LangChain |
| Web Research | Tavily API |
| Structured Outputs | Pydantic |
| Frontend | Streamlit |
| Export Format | Markdown |

---

## 🧠 AI Concepts Demonstrated

- Multi-Agent Systems
- Agentic Workflows
- LLM Orchestration
- Parallel Processing
- Prompt Engineering
- Graph-Based Execution
- Autonomous Planning
- Generative AI Applications

---

## 📈 Engineering Highlights

✅ Designed a **graph-based multi-agent system** using LangGraph.

✅ Implemented **dynamic worker creation and parallel execution** for long-form content generation.

✅ Integrated **real-time web research** to improve factual relevance and freshness.

✅ Built an **AI-driven image generation and placement pipeline**.

✅ Developed an end-to-end **autonomous content generation application** from research to final export.

✅ Implemented **structured outputs using Pydantic models** to improve reliability.

---

## 🚀 Running the Application

## Local Setup

### Prerequisites

* Python 3.11+
* Git

### Clone Repository

```bash
git clone git@github.com:jatintomer27/blogforge_ai.git
```

```bash
cd blogforge_ai
```

### Create Virtual Environment

```bash
python3 -m venv blogforge
```

Linux / Mac

```bash
source blogforge/bin/activate
```


Windows

```bash
chatbot\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

```bash
cp env_example.txt .env
```

Update the Keys required in env file.

### Start Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## Docker Setup

- If you don’t want to install dependencies locally, you can run the complete Blog Forge AI app directly using Docker.

- [DockerHub Image](https://hub.docker.com/r/jatintomer/blogforge_ai)

---

## 🎥 Demo

![Application Demo](static/assets/demo.gif)

---

## 📄 License

This project is intended for personal and educational use. Feel free to modify and extend it according to your requirements.

