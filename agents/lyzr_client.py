import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("LYZR_API_KEY")
AGENT_ID = os.getenv("LYZR_AGENT_ID")

URL = "https://agent-prod.studio.lyzr.ai/v3/inference/chat/"

HEADERS = {"x-api-key": API_KEY, "Content-Type": "application/json"}


def ask_lyzr(prompt):
    payload = {
        "user_id": "engineering-user",
        "agent_id": AGENT_ID,
        "session_id": "engineering-session",
        "message": prompt,
    }

    response = requests.post(URL, headers=HEADERS, json=payload, timeout=30)

    if response.status_code != 200:
        print("LYZR ERROR:")
        print(response.text)
        raise Exception(f"Lyzr Error: {response.status_code}")

    return response.json()