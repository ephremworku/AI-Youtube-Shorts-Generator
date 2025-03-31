# from ollama import chat
# from ollama import ChatResponse
# from ollama import Client
# client = Client(
#   host='http://localhost:11434',
#   headers={'x-some-header': 'some-value'}
# )
# # response = client.chat(model='llama3.2', messages=[
# #   {
# #     'role': 'user',
# #     'content': 'Why is the sky blue?',
# #   },
# # ])
# response: ChatResponse = client.chat(model='llava:7b', messages=[
#   {
#     'role': 'user',
#     'content': 'Why is the sky blue?',
#   },
# ])
# print(response['message']['content'])
# # or access fields directly from the response object
# print(response.message.content)

import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# openai.api_key = os.getenv("OPENAI_API")

# if not openai.api_key:
#     raise ValueError("API key not found. Make sure it is defined in the .env file.")
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API"),
)
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "Talk like a pirate."},
        {
            "role": "user",
            "content": "How do I check if a Python object is an instance of a class?",
        },
    ],
)
print(completion)