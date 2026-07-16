# Local AI DevOps Agent

## Stack
- Orchestrator: n8n (Local Community Edition)
- Execution: Python 3
- LLM Gateway: Ollama
- Model Core: Qwen 2.5 (14B)

## Workflow
1. Webhook catches repository update event.
2. n8n triggers local Python environment.
3. Script passes code contents to Ollama API.
4. Qwen 2.5 (14B) performs static analysis and outputs a markdown bug report.

## Architecture & Verification

### 1. n8n Integration Pipeline
![n8n Workflow Layout](./n8n%20workflow.png)

### 2. Local LLM Compute Core
![Ollama Active Models](./llm%20lists.png)

### 3. Automated Code Review Execution
![Agent Bug Report Output](./execution%20terminal.png)
## Setup & Run

Ensure Ollama has the model pulled:
```bash
ollama run qwen2.5:14b
```
Run the localized test execution pipeline:
```bash
python run_agent.py
