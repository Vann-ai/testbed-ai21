import requests
import json
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()
api_key = os.getenv('API_KEY')

url = "https://api.ai21.com/studio/v1/summarize-by-segment"

payload = json.dumps({
    "sourceType": "URL",
    "source": "https://www.ai21.com/blog/ai21-bigquery"
})
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
response_text = response.text
response_json = json.loads(response_text)

# print(response_json)
# print(json.dumps(response_json, indent=4))

# Print all summaries
for summary in response_json["segments"]:
    print(summary["summary"])
    print("\n")
