# tests whether /User/login endpoint is reachable and responding properly

import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials and base URL from .env
BASE_URL = os.getenv("BASE_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

def test_login():
    login_url = BASE_URL
    
    # Headers for the request
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",  # Mimic a browser
        "Accept": "application/json"
    }

    try: 
        # Make a GET request (Note: This is only for testing. Login typically uses POST)
        response = requests.get(login_url, headers=headers)

        # Raise an error if response code is not 2xx
        response.raise_for_status()

        print("✅ Login endpoint reachable.")
        print("📦 Response preview:", response.text[:200], "...")

        # Attempt to parse response as JSON
        try:
            data = response.json()
        except ValueError:
            print("⚠️ Response is not valid JSON.")
            return

        # Handle based on type
        if isinstance(data, dict):
            print("🔐 Token:", data.get("token", "No token found in response"))
        else:
            print("ℹ️ Server responded with non-JSON or unexpected structure:", data)

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
        print("Response text:", response.text)
    except Exception as err:
        print(f"❌ Other error occurred: {err}")

if __name__ == "__main__":
    test_login()

