### app.py
import os
import requests
from dotenv import load_dotenv


API_KEY = "7a8b4fb5-63d2-40be-ad09-ebc85ce91de7"
API_URL = "https://api.cloudmersive.com/validate/address/street-address"

def parse_input_address(input_text: str) -> dict:
    """
<<<<<<< HEAD
    Parse input text into address components.
    Basic parsing - in real world, you might want to use more sophisticated parsing.
=======
    Parse unstructured address text into a structured format using Cloudmersive API.
    Only returns relevant address fields.
>>>>>>> 8ce7638c06a4ae50adc4b47eb92714d830bbf476
    """
    parts = input_text.split(',')
    address_parts = {
        'street_address': parts[0].strip() if len(parts) > 0 else '',
        'city': parts[1].strip() if len(parts) > 1 else '',
        'state': parts[2].strip() if len(parts) > 2 else '',
        'postal_code': parts[3].strip() if len(parts) > 3 else '',
        'country': parts[4].strip() if len(parts) > 4 else 'Turkey'  # Varsayılan ülke
    }
    return address_parts

def validate_address(input_text: str) -> dict:
    """
    Validates if the given address is correct and exists.
    Returns a dictionary with validation result and details.
    """
    try:
        # Parse input address
        address_parts = parse_input_address(input_text)
        
        headers = {
            "Apikey": API_KEY,
            "Content-Type": "application/json"
        }
        
        # Use validate endpoint with our parsed components
        payload = {
            "StreetAddress": address_parts['street_address'],
            "City": address_parts['city'],
            "StateOrProvince": address_parts['state'],
            "PostalCode": address_parts['postal_code'],
            "CountryFullName": address_parts['country']
        }

        print(f"\nGönderilen istek:")
        print(f"URL: {API_URL}")
        print(f"Headers: {headers}")
        print(f"Payload: {payload}")

        response = requests.post(API_URL, json=payload, headers=headers)

        print(f"\nAPI Yanıtı:")
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Response Data: {data}")
            
            is_valid = data.get("ValidAddress", False)
            
            return {
                "is_valid": is_valid,
                "validation_status": "Geçerli bir adres" if is_valid else "Geçersiz adres",
                "coordinates": {
                    "latitude": data.get("Latitude"),
                    "longitude": data.get("Longitude")
                } if is_valid else None,
                "message": "Adres doğrulandı ve koordinatları bulundu." if is_valid else "Adres doğrulanamadı veya bulunamadı.",
                "input_address": address_parts,
                "raw_response": data
            }
        else:
            print(f"Error Response: {response.text}")
            return {
                "is_valid": False,
                "validation_status": "Hata",
                "message": f"API isteği başarısız oldu: HTTP {response.status_code}",
                "coordinates": None,
                "input_address": address_parts,
                "error_details": response.text
            }

    except Exception as e:
        print(f"Exception: {str(e)}")
        return {
            "is_valid": False,
            "validation_status": "Hata",
            "message": f"Sistem hatası: {str(e)}",
            "coordinates": None,
            "input_address": None,
            "error_details": str(e)
        }

# Test the function with a sample address
print(validate_address("Barbaros Bulvarı No:145, Beşiktaş, İstanbul, 34349, Turkey"))

<<<<<<< HEAD
=======
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
>>>>>>> 8ce7638c06a4ae50adc4b47eb92714d830bbf476
