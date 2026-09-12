# Azure PDF RAG Chatbot POC

A beginner-friendly FastAPI project that provides the starting point for a future PDF RAG chatbot with an MCP server, Docker, GitHub Actions, and Azure deployment.

## Current POC scope

- FastAPI application
- Root endpoint
- Health-check endpoint
- Unit tests with pytest
- Linting with Ruff
- GitHub Actions CI workflow
- Python 3.12 setup

The project intentionally does not include RAG, MCP, databases, authentication, Docker, or Azure deployment yet. Add those later through separate feature branches.

## Project structure

```text
azure-pdf-rag-chatbot-poc/
├── app/
│   ├── services/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── config.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_health.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── README.md
├── requirements.txt
└── requirements-dev.txt
```

## 1. Open the project

Extract the ZIP and open the extracted folder in Visual Studio Code.

```powershell
cd path\to\azure-pdf-rag-chatbot-poc
code .
```

## 2. Create a virtual environment

```powershell
py -3.12 -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If script execution is blocked, run this once in the current PowerShell window:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## 3. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

## 4. Run checks locally

Run linting:

```powershell
python -m ruff check .
```

Run tests:

```powershell
python -m pytest -v
```

Expected result: two tests pass.

## 5. Start the application

```powershell
python -m uvicorn app.main:app --reload
```

Open these URLs:

- API root: http://127.0.0.1:8000/
- Health endpoint: http://127.0.0.1:8000/health
- Swagger documentation: http://127.0.0.1:8000/docs

Stop the server with `Ctrl+C`.

## 6. Initialize Git

If you downloaded this project as a ZIP, initialize a new repository:

```powershell
git init
git branch -M main
git add .
git commit -m "chore: initialize FastAPI POC"
```

Create an empty GitHub repository named `azure-pdf-rag-chatbot-poc`. Do not initialize it with another README or `.gitignore`. Then connect and push:

```powershell
git remote add origin https://github.com/YOUR-USERNAME/azure-pdf-rag-chatbot-poc.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

## 7. Start feature-branch development

Always start a feature from the latest `main`:

```powershell
git switch main
git pull origin main
git switch -c feature/poc-chat-endpoint
```

After making and testing changes:

```powershell
python -m ruff check .
python -m pytest -v
git add .
git commit -m "feat: add POC chat endpoint"
git push -u origin feature/poc-chat-endpoint
```

Open a pull request from `feature/poc-chat-endpoint` into `main`. GitHub Actions will run Ruff and pytest automatically. Merge only after the CI check passes.

## Suggested feature order

1. `feature/poc-chat-endpoint`
2. `feature/pdf-rag`
3. `feature/mcp-server`
4. `feature/docker-support`
5. `feature/azure-deployment`
6. `feature/langgraph-orchestration`
7. `feature/sqlite-memory`
8. `feature/postgresql-memory`
9. `feature/authentication`
10. `feature/authorization`

Create one branch at a time, merge it through a pull request, then delete it before starting the next feature.
