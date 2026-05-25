# README.md

````md id="8f9m2q"
# Interviewer

A multi-agent AI powered coding interviewer built using AutoGen.

The system:
- generates coding problems
- writes them into files
- lets candidates solve them locally
- evaluates the solution
- asks follow-up questions
- scores the candidate
- stores results in Excel

Basically your own AI technical interviewer.

---

# Features

- Multi-agent interview orchestration
- Real coding interview flow
- Topic-based DSA question generation
- MCP filesystem integration
- Code evaluation + scoring
- Excel result storage
- Prompt injection resistance
- Cross-platform support (Windows/Mac/Linux)

---

# Tech Stack

- Python 3.13+
- AutoGen
- MCP Filesystem Server
- OpenRouter / OpenAI / Groq compatible
- Rich CLI
- Questionary
- OpenPyXL

---

# Installation

## 1. Clone the repo

```bash
git clone <your-repo-url>
cd interviewer
````

---

## 2. Install uv

If you don't have uv installed...

Well, I got you covered, my friend 

### Windows

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Mac/Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Docs:
[https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

---

## 3. Sync dependencies

```bash
uv sync
```

---

## 4. Create `.env`

Copy everything from:

```bash
.env.example
```

into:

```bash
.env
```

---

# API Keys

## OpenRouter (Recommended)

Go here:

[https://openrouter.ai/](https://openrouter.ai/)

Create your own API key.

It's free up to a reasonable limit.

And secondly...

why would I give you mine? hehehe

---

# Running the Project

```bash
uv run python -m main
```

---

# Supported Models

You can swap models easily inside `interviewer.py`.

---

# Free Models

## DeepSeek Free

```python
client = OpenAIChatCompletionClient(
    model="deepseek/deepseek-chat:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model_info={
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "family": "unknown",
    },
)
```

---

## Llama 3.3 70B (Groq)

Very fast.

```python
client = OpenAIChatCompletionClient(
    model="llama-3.3-70b-versatile",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"),
    model_info={
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "family": "llama",
    },
)
```

---

## Gemini Flash

Cheap and good.

```python
client = OpenAIChatCompletionClient(
    model="google/gemini-2.0-flash-001",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model_info={
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "family": "gemini",
    },
)
```

---

# Paid Models

## GPT-4o

Best overall quality.

```python
client = OpenAIChatCompletionClient(
    model="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY"),
)
```

---

## GPT-4.1 Mini

Cheap + strong reasoning.

```python
client = OpenAIChatCompletionClient(
    model="gpt-4.1-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
)
```

---

## Claude Sonnet

Excellent interviewer behavior.

```python
client = OpenAIChatCompletionClient(
    model="anthropic/claude-3.7-sonnet",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model_info={
        "vision": False,
        "function_calling": True,
        "json_output": True,
        "structured_output": True,
        "family": "claude",
    },
)
```

---

# Project Structure

```txt
interviewer/
│
├── main.py
├── interviewer.py
├── problems/
├── interview_results.xlsx
├── .env.example
├── pyproject.toml
└── README.md
```

---

# How It Works

1. Candidate selects:

   * difficulty
   * DSA topics

2. AI interviewer:

   * generates a coding problem
   * writes it into `/problems`

3. Candidate solves problem locally

4. Evaluator agent reviews the code

5. Scorer agent:

   * assigns score
   * stores results in Excel

---

# Security Features

* Prompt injection resistance
* Topic-constrained generation
* Filesystem sandboxing
* Agent role enforcement
* Controlled evaluation flow

---

# Future Improvements

* Web UI
* Voice interviews
* Live collaborative coding
* Resume-based question generation
* Multi-round interviews
* System design rounds
* Docker support

---

# Disclaimer

If the AI rejects your solution brutally...

that's just realistic interview prep :)

# Additional Information/Advice

- I have noticed that using a paid model gives me a better result than free ones, as hallucinations are less
- I recommend using OpenAI or Google Gemini for this
- Avoid using laptops that you are not an admin of, as they may block calls to open-source LLM models 

```
```
