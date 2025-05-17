import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Gemini API from the .env file
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def my_first_agent():
    # ✅ Correct Gemini API endpoint for MakerSuite
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": "Say hello to the user!"
                    }
                ]
            }
        ]
    }

    print("Sending request to Gemini API...")
    print("Request Data:", data)

    response = requests.post(url, headers=headers, json=data)

    print("Response Status Code:", response.status_code)
    print("Response Content:", response.text)

    if response.status_code == 200:
        try:
            result = response.json()
            print("API Response:", result)
            reply = result['candidates'][0]['content']['parts'][0]['text']
            print("Gemini says:", reply)
        except Exception as e:
            print("Error while processing the response:", e)
    else:
        print("Error in API request:", response.status_code)
        print(response.text)

# Run the agent
if __name__ == "__main__":
    my_first_agent()
