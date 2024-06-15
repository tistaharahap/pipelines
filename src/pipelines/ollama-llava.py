from os import environ
from typing import List, Union, Generator, Iterator

from ollama import Client


class Pipeline:
    def __init__(self):
        headers = {"authorization": f"Bearer {environ.get('OLLAMA_API_KEY')}"}
        self.client = Client(api_key=environ.get("GROQ_API_KEY"), headers=headers)

    async def on_startup(self):
        pass

    async def on_shutdown(self):
        pass

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, Generator, Iterator]:
        response = self.client.chat(
            model="llava",
            messages=messages,
            stream=True,
        )
        return response