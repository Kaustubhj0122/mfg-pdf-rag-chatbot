"""FastAPI entry point for the PDF RAG Chatbot POC."""

from fastapi import FastAPI

app = FastAPI(
    title="PDF RAG Chatbot",
    description="Beginner POC for a future PDF RAG and MCP chatbot.",
    version="0.1.0",
)


@app.get("/")
def root() -> dict[str, str]:
    """Return basic API information."""
    return {"message": "PDF RAG Chatbot API is running"}


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return the application health status."""
    return {"status": "healthy"}
