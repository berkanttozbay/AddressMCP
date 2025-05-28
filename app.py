### app.py
import os
import requests
from dotenv import load_dotenv


API_KEY = ("7a8b4fb5-63d2-40be-ad09-ebc85ce91de7")
API_URL = "https://api.cloudmersive.com/validate/address/parse"


def parse_address(input_text: str) -> dict:
    """
    Parse unstructured address text into a structured format using Cloudmersive API.
    Only returns relevant address fields.
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
        data = response.json()

        # Örnek olarak sadece bazı önemli alanları döndürüyoruz:
        return {
            "Successful": data.get("Successful"),
            "Building": data.get("Building"),
            "StreetNumber": data.get("StreetNumber"),
            "Street": data.get("Street"),
            "City": data.get("City"),
            "StateOrProvince": data.get("StateOrProvince"),
            "PostalCode": data.get("PostalCode"),
            "CountryFullName": data.get("CountryFullName"),
            "ISOTwoLetterCode": data.get("ISOTwoLetterCode"),
        }

    else:
        return {"error": f"API request failed with status code {response.status_code}"}
