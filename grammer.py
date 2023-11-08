import ai21
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()
ai21.api_key = os.getenv('API_KEY')

output = ai21.GEC.execute(
    text="At times, my job can be quite monogamous. I’m not aloud to do anything creative.")
print(output.corrections[0])
