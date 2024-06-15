from os import environ
from typing import List, Union, Generator, Iterator

from openai import OpenAI


class Pipeline:
    def __init__(self):
        self.client = OpenAI(api_key=environ.get("OPENAI_API_KEY"))

    async def on_startup(self):
        pass

    async def on_shutdown(self):
        pass

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, Generator, Iterator]:
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.8,
            max_tokens=4096,
            stream=True,
        )
        return response
