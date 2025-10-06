import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class OpenrouterService:
    def __init__(
        self,
        base_url: str = "https://openrouter.ai/api/v1",
        api_key: str = os.getenv("OPENROUTER_API_KEY") or "",
        model: str = os.getenv("OPENROUTER_MODEL")
        or "qwen/qwen2.5-vl-32b-instruct:free",
    ):
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.model = model

    def query(self, prompt: str, image_hash) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {"url": image_hash},
                        },
                    ],
                }
            ],
        )
        # Return first choice content safely
        try:
            return completion.choices[0].message.content or ""
        except Exception:
            return ""
