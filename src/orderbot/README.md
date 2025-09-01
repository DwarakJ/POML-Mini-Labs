# AI-powered Customer Support Chatbot for Order Inquiries (POML + Azure OpenAI)

This mini-lab demonstrates building a structured, reliable customer support chatbot for order inquiries using POML, Python, and Azure OpenAI.

## Features

- Combines CSV order data, tabular item details, and stepwise instructions in a structured POML prompt
- Enforces agent role, task, and constraints for accurate, safe chat behavior
- Easily extensible with more data and logic

## Setup

1. Install requirements:
   ```
   pip install -r requirements.txt
   ```
2. Set your Azure OpenAI credentials as environment variables:
   ```
   export AZURE_OPENAI_API_KEY=...
   export AZURE_OPENAI_ENDPOINT=...
   export AZURE_OPENAI_DEPLOYMENT=...
   ```
3. Run the chatbot:
   ```
   python main.py
   ```

## Example Usage

```
You: How much did I pay for my last order?
OrderBot: Your last order (OrderId: CC10182) totaled $120.00 and included items such as Shorts and Socks.

You: What is the delivery status of my T-Shirt?
OrderBot: Your order CC10183 included a T-Shirt, which was shipped and delivered on 2024-01-20.
```

---

### How POML Helps

- **Structured Data Integration:** CSVs are referenced as `<table>` in the prompt, so the LLM can answer with specifics.
- **Reusable Prompt:** Role, task, and instructions are modular and easy to update.
- **Safe LLM Use:** Guardrails prevent the bot from overstepping or hallucinating answers.

---

Feel free to extend the asset data, instructions, and enrich the POML as a team exercise!