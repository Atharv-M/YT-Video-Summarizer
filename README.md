# 🎥 YT-Video-Summarizer

A **Generative AI-powered YouTube Video Summarizer** built with **LangChain**, **Google Gemini**, and **Streamlit**.  
This tool allows users to **paste a YouTube video URL** and instantly generate an **AI-driven summary** of its transcript.  

---

## 📌 Table of Contents
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Architecture](#architecture)  
- [Workflow](#workflow)  
- [Screenshots](#screenshots)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Configuration](#configuration)  
  - [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)  

---

## 🚀 Features
- 🎬 **Summarize YouTube videos** using just the URL  
- 🧠 **LLM-powered** summarization via **LangChain** and **Google Gemini**  
- 📜 **Transcript extraction** and context-aware analysis  
- 🖥️ **Streamlit UI** for user-friendly interaction  
- ⚡ **Fast and scalable** with prompt optimization  

---

## 🛠️ Tech Stack
- **Language**: Python  
- **Frameworks**: LangChain, Streamlit  
- **LLM**: Google Gemini  
- **Libraries**: YouTube Transcript API, Transformers  
- **Deployment**: Streamlit App  

---

## 🏗️ Architecture
1. User enters a **YouTube video URL**.  
2. The app fetches the **transcript** of the video.  
3. LangChain + Gemini processes the transcript.  
4. An **AI-generated summary** is returned and displayed.  

---

## 🔄 Workflow

### Flowchart
```mermaid
flowchart TD
    A[User provides YouTube URL] --> B[Extract Transcript using YouTube API]
    B --> C[Process Transcript with LangChain + Gemini]
    C --> D[Generate Concise Summary]
    D --> E[Display Summary in Streamlit UI]

