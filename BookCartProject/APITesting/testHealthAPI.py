# GET method for a health check for the BookCart website. Should return 200 OK if it works

import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BASE_URL = os.getenv("BASE_URL")

def test_health():
    """Health check for BookCart API using the /Book endpoint."""
    url = BASE_URL
    
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            print("✅ BookCart API health check passed (200 OK).")
            try:
                data = response.json()
                if isinstance(data, list):
                    print(f"📚 Book list retrieved successfully. Found {len(data)} books.")
                else:
                    print("⚠️ Response was JSON but not a list:", data)
            except ValueError:
                print("⚠️ Response not valid JSON.")
        else:
            print(f"❌ Health check failed with status {response.status_code}")
            print("Response text:", response.text)
    
    except requests.exceptions.RequestException as e:
        print("❌ API health check error:", e)


if __name__ == "__main__":
    test_health()
