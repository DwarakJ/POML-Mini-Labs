import os
from poml import poml
from openai import AzureOpenAI

AZURE_OPENAI_API_KEY = os.environ.get("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT = os.environ.get("AZURE_OPENAI_DEPLOYMENT")  # e.g., 'gpt-35-turbo'

def generate_research_plan(project_options):
    prompt = poml(
        "research_plan.poml",
        context={"project_options": project_options},
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
        max_tokens=800,
        temperature=0.3
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("Enter your project options (one per line). Type 'END' to finish:")
    options = []
    while True:
        opt = input("> ").strip()
        if opt.lower() == "end":
            break
        if opt:
            options.append(opt)
    print("\nGenerating research plans...\n")
    plan = generate_research_plan(options)
    print(plan)