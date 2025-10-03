import os
from ollama import Client
from dotenv import load_dotenv

load_dotenv()


class OllamaService:
    def __init__(
        self,
        host: str = "http://ollama:11434",
        model: str = os.getenv("OLLAMA_MODEL") or "gemma3:4b",
    ):
        self.client = Client(host=host)
        self.model = model

    def query(self, prompt: str, system_message: str, image) -> str:
        response = self.client.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt, "images": [image]},
            ],
        )
        return response["message"]["content"]
