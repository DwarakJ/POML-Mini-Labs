import os
from poml import poml
from openai import AzureOpenAI

AZURE_OPENAI_API_KEY = os.environ.get("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT = os.environ.get("AZURE_OPENAI_DEPLOYMENT")  # e.g., 'gpt-35-turbo'

def summarize_report():
    prompt = poml(
        "summarize_report.poml",
        context={},
        format="openai_chat"
    )
    client = AzureOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        api_version="2023-05-15",
        azure_endpoint=AZURE_OPENAI_ENDPOINT
    )
    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=prompt["messages"],
        max_tokens=220,
        temperature=0.2
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("Generating executive summary from financial report...\n")
    summary = summarize_report()
    print("Executive Summary:\n", summary)