import os
from poml import poml
from openai import AzureOpenAI

AZURE_OPENAI_API_KEY = os.environ.get("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT = os.environ.get("AZURE_OPENAI_DEPLOYMENT")  # e.g., 'gpt-35-turbo'

def ask_orderbot(user_question):
    rendered = poml(
        "chatbot.poml",
        context={"user_question": user_question},
        format="openai_chat"
    )
    client = AzureOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        api_version="2023-05-15",
        azure_endpoint=AZURE_OPENAI_ENDPOINT
    )
    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=rendered["messages"],
        max_tokens=150,
        temperature=0.2
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("OrderBot: Ask your order-related question (type 'exit' to quit):")
    while True:
        question = input("You: ")
        if question.strip().lower() == "exit":
            break
        answer = ask_orderbot(question)
        print("OrderBot:", answer)