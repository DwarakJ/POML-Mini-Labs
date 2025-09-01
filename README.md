# POML Mini Labs: Real-World Prompt Engineering with Prompt Orchestration Markup Language

Welcome to the **POML Mini Labs** repository—a hands-on collection of real-world example projects for mastering Prompt Orchestration Markup Language (POML) in advanced LLM applications. These labs are designed to go beyond basic prompting and build robust, maintainable, and data-driven AI workflows.

---

## What Is POML?

[POML](https://github.com/microsoft/poml) (Prompt Orchestration Markup Language) is a component-based markup and templating system for building structured, modular prompts for Large Language Models (LLMs). It enables:

- **Semantic prompt structure** (`<role>`, `<task>`, `<output-format>`, etc.)
- **Data integration** (CSV, Excel, PDF, images, JSON, tables)
- **Templating** (variables, loops, conditionals, file includes)
- **Output control** (schemas, token/char limits, stylesheets)
- **Multimodal workflows** (vision, tabular, document, and more)
- **First-class engineering practices** (version control, testability, IDE tooling)

---

## Labs Included

### 1. AI-powered Customer Support Chatbot for Order Inquiries

- **Goal:** Automate customer order Q&A using LLMs with tabular (CSV) data integration, stepwise constraints, and safe output formatting.
- **Key POML Features:** `<role>`, `<task>`, `<cp>`, `<table>`, `<let>`, `<for>`, `<HumanMessage>`, `<stylesheet>`

### 2. Automated Financial Report Summarizer

- **Goal:** Summarize long PDF financial reports into concise executive summaries using POML’s `<document>` integration and length constraints.
- **Key Features:** `<document>`, `<output-format>`, token/char limits, presentation control

### 3. Smart Research Plan Generator from Project Options

- **Goal:** Convert a list of project ideas into structured, repeatable research plans using POML stepwise instructions and templating.
- **Key Features:** `<task>`, `<stepwise-instructions>`, `<list>`, `<for>`, templating

---

## How to Run the Labs

### Prerequisites

- Python 3.8+ (for Python SDK labs)
- Node.js (for JS/TS SDK labs, optional)
- Access to an LLM provider (e.g., OpenAI, Azure OpenAI) and relevant API keys
- [poml](https://pypi.org/project/poml/) Python package (`pip install poml`)
- [openai](https://pypi.org/project/openai/) Python package as needed
- (Optional) [POML VS Code Extension](https://github.com/microsoft/poml/blob/main/docs/vscode/index.md) for syntax highlighting, preview, and testing