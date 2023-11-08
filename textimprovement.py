import ai21
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()
ai21.api_key = os.getenv('API_KEY')

# First example
output = ai21.Improvements.execute(text="I ate a good and awesome pizza last night.", types=[
                                   'fluency', 'vocabulary/specificity', 'vocabulary/variety', 'clarity/short-sentences', 'clarity/conciseness'])

print(output.improvements[0])


# Second example
text = "Affiliated with the profession of project management, I have ameliorated myself with a different set of hard skills as well as soft skills."
response = ai21.Improvements.execute(text=text,
                                     types=["fluency"]
                                     )
improved_text = text
improvements = response["improvements"]
for curr_improvement in reversed(improvements):
    improved_text = improved_text[:curr_improvement["startIndex"]] + \
        curr_improvement['suggestions'][0] + \
        improved_text[curr_improvement["endIndex"]:]

print(improved_text)
