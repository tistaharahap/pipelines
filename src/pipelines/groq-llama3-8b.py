from os import environ
from typing import List, Union, Generator, Iterator

from groq import Groq


class Pipeline:
    def __init__(self):
        self.client = Groq(api_key=environ.get("GROQ_API_KEY"))

    async def on_startup(self):
        pass

    async def on_shutdown(self):
        pass

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, Generator, Iterator]:
        response = self.client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages,
            temperature=0.8,
            max_tokens=8192,
            stream=True,
        )
        return response
