import json
import requests

from pydantic import BaseModel
from fastapi import FastAPI, Depends


OPENROUTER_API_KEY = (
    "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"
)


class DataInput(BaseModel):
    promt: str


app = FastAPI()


def send_message(promt: str):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        },
        data=json.dumps(
            {
                "model": "google/learnlm-1.5-pro-experimental:free",
                "messages": [
                    {
                        "role": "user",
                        "content": promt,
                    }
                ],
            }
        ),
    )

    response_content = json.loads(response.content.decode())
    return response_content["choices"][0]["message"]["content"]


@app.post("/")
def ask_ai(data: DataInput = Depends()):
    message = send_message(data.promt)
    return {"message": message}
