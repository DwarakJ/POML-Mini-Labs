# Automated Financial Report Summarizer (POML + Azure OpenAI)

This mini-lab demonstrates using POML, Python, and Azure OpenAI to extract and summarize key insights from financial reports (PDF/DOCX).

## Features

- Structured prompt with `<Document>` ingesting a real PDF financial report
- Stepwise instructions and output format guide the LLM for concise, C-level summaries
- Modular and reusable—just swap in any financial report for a new summary!

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Set your Azure OpenAI credentials:
   ```sh
   export AZURE_OPENAI_API_KEY=...
   export AZURE_OPENAI_ENDPOINT=...
   export AZURE_OPENAI_DEPLOYMENT=...
   ```
3. Place your PDF report in `assets/sample_report.pdf`.
4. Run the summarizer:
   ```
   python main.py
   ```

## Example Output

```
Executive Summary:
In Q2 2025, Acme Corp reported revenues of $1.2B, up 8% YoY, with net profit margins holding steady at 14%. Revenue growth was driven by strong demand in the cloud segment, offsetting a 3% decline in hardware sales. The report highlighted operational efficiencies and cost controls as key margin drivers. Management noted elevated supply chain risks and foreign exchange volatility as ongoing concerns. The outlook remains cautiously optimistic, with investments planned in AI initiatives and expansion into APAC markets.
```

---

### How POML Helps

- **Componentized Inputs:** The `<Document>` tag brings in raw report data for accurate, context-rich summarization.
- **Reusable Logic:** Stepwise instructions and output format ensure every summary is consistent and high-quality.
- **Simple Templating:** Easily change instruction logic or output structure for different summary needs.

---

*Try extending with DOCX support, longer reports, or more detailed output schemas for further learning!*