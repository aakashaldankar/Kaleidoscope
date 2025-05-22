
# 📚 KaleidoscopeQA – Intelligent QA Assistant for NCERT Class 12 English

**KaleidoscopeQA** is an AI-powered question-answering assistant named **Zero**, tailored specifically for students studying the *Kaleidoscope* English textbook (Class 12 NCERT). This tool is designed to support learners by answering questions, providing summaries, and interpreting poetry and literature in the book.

Whether it's prose, drama, or poetry – **Zero** helps enhance your understanding of each chapter by delivering insights in real-time.

---

## ✨ Why This Project Matters

In educational institutions or e-learning platforms, answering students' textual doubts requires significant manual effort. **KaleidoscopeQA** automates this process using cutting-edge AI technology, ensuring that students have a consistent, scalable, and insightful assistant available 24/7.

This project can be used in schools, tutoring apps, or self-learning platforms to assist learners without needing continuous human intervention.

---

## 🧠 Features

- 💬 Ask any question from the *Kaleidoscope* textbook and get a precise, contextual answer.
- 🧾 Summarize long chapters or poems.
- 🎭 Interpret the literary meaning of poems, metaphors, and phrases.
- 🗂️ Understand the story or poem in a specific chapter context.
- 🪵 Tree Indexing for deeper contextual awareness.

---

## 🏗️ Tech Stack

| Component            | Technology Used                |
|----------------------|--------------------------------|
| Embeddings           | all-mpnet-base-v2 (via HuggingFace) |
| Vector DB            | Qdrant                        |
| Indexing             | LlamaIndex (Vector + TreeIndex) |
| LLM                  | Gemma-9b-it (via Groq API)     |
| Interface            | Gradio                         |
| Programming Language | Python                         |

---

## 🗂️ Project Structure

```
├── Qdrant_db/              # Vector DB for the entire book
├── app.py                  # Main script to run the project via Gradio
├── chapter_index.pkl       # Chapter name mapping
├── model.py                # Embedding + Indexing setup
├── requirements.txt        # Python dependencies
├── tree_index.pkl          # TreeIndex for each chapter
```

---

## 🚀 Run the Project Locally

### ✅ Prerequisites

- Python 3.10+
- Valid Groq API key (Sign up at [Groq Console](https://console.groq.com/))
- Git (for cloning repo)

### 🔧 Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/aakashaldankar/Kaleidoscope.git
cd Kaleidoscope
```

2. **Create and Activate Virtual Environment (optional)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Set Up Environment Variable**

Create a `.env` file and add:

```
GROQ_API_KEY=your_groq_api_key_here
```

5. **Run the App**

```bash
python app.py
```

---

## 📌 Notes

- Ensure the folders `Qdrant_db/`, `tree_index.pkl`, and `chapter_index.pkl` are present in the correct locations.
- Gemma-9b-it is hosted via Groq API, so ensure you have network access.
- Use `.env` file or OS environment variables for storing sensitive keys.

---

## 🎯 Use Cases and Benefits

- 📚 **Educational Institutions**: Use as a virtual TA for English literature courses.
- 🧠 **E-learning Platforms**: Boost user engagement with intelligent textbook assistants.
- 💡 **Literature Enthusiasts**: Deepen understanding of complex poems and literary devices.

---

## 📮 Contact

Have questions or want to contribute?

📧 Email: aakashaldankar@gmail.com 
🧠 Project by: Aakash

---

> “Books speak when read. Zero listens and responds when questioned.” 📖✨
