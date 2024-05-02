import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatCompletionResponse, ChatMessage
from dotenv import load_dotenv

load_dotenv()

client = MistralClient(api_key=os.getenv("MISTRAL_API"))
model = os.getenv("MISTRAL_MODEL")


def call_model(system_prompt, user_prompt):
    response = __get_response(system_prompt, user_prompt)
    return response.choices[0].message.content


def __get_response(system_prompt, user_prompt):
    response = client.chat(
        model=model,
        response_format={"type": "json_object"},
        messages=[
            ChatMessage(role="system", content=system_prompt),
            ChatMessage(role="user", content=user_prompt),
        ],
    )
    return response
