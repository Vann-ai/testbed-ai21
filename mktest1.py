import ai21
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()
ai21.api_key = os.getenv('API_KEY')

prompt = "What is the capital of Germany?"
output = ai21.Completion.execute(
    model="j2-light",
    custom_model="mktest1",
    prompt=prompt,
    numResults=1,
    epoch=20,
    maxTokens=200,
    temperature=0.7,
    topKReturn=0
)

print(output.completions[0].data.text)
