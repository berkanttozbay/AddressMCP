### app.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = ("7a8b4fb5-63d2-40be-ad09-ebc85ce91de7")
API_URL = "https://api.cloudmersive.com/validate/address/parse"


def parse_address(input_text: str) -> dict:
    """
    Parse unstructured address text into a structured format using Cloudmersive API.
    """
    headers = {
        "Apikey": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "InputString": input_text
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"API request failed with status code {response.status_code}"}
