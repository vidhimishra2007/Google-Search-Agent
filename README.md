# 🔍 Google Search Agent

An AI-powered agent built with **Google Agent Development Kit (ADK)** that answers questions using real-time Google Search. Built with `gemini-2.5-flash` as the underlying model.

---

## 📋 Features

- Real-time Google Search integration
- Answers questions requiring current/live information
- Built on Google ADK framework
- Supports both terminal and web UI interaction

---

## 🛠️ Tech Stack

- **Python**
- **Google ADK** (`google-adk`)
- **Google GenAI** (`google-genai`)
- **Gemini 2.5 Flash** (LLM)
- **Google Search Tool** (built-in ADK tool)

---

## 📁 Project Structure

```
project/
├── agent.py        # Main agent definition and logic
├── .env            # API key (never commit this)
├── .gitignore      # Ignores .env
└── README.md       # This file
```

---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies
```bash
uv add google-adk google-genai python-dotenv
```

### 3. Set up your API key
- Get a free API key from [Google AI Studio](https://aistudio.google.com/apikey)
- Create a `.env` file in the project root:
```
GOOGLE_API_KEY=your_api_key_here
```

### 4. Add `.env` to `.gitignore`
```bash
echo ".env" >> .gitignore
```

---

## 🚀 Running the Agent

### Option 1: Web UI (recommended)
```bash
uv run adk web --port 8000
```
Then open: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Option 2: Terminal
```bash
uv run python agent.py
```

---

## 💬 Example Queries

- *"What is the current population of New York City?"*
- *"What happened in the news today?"*
- *"What is the latest version of Python?"*
- *"Who won the IPL 2025?"*

---

## ⚠️ Important Notes

- **Never commit your `.env` file** — it contains your private API key
- Gemini 2.5 Flash free tier allows **1,000 requests/day**
- Requires an **internet connection** (API calls go to Google servers)

---

## 📄 License

MIT License — free to use and modify.
