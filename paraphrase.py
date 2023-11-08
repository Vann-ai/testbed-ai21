import ai21
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

ai21.api_key = os.getenv('API_KEY')
output = ai21.Paraphrase.execute(
    text="Vikings were Norse seafarers who raided the coast of Europe for centuries.", style="general")
print(output.suggestions[0].text)
