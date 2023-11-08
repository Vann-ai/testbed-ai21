
import ai21
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()
ai21.api_key = os.getenv('API_KEY')

output = ai21.Summarize.execute(source="""Rob Roussel, senior project manager, said the bioremediation process was successfully breaking down the oil into carbon dioxide and water. He said the process was at the mercy of the weather, but would hopefully be complete by the end of next month. The oil was dumped in the quarry in the Vale after the tanker spill in 1967.
The 974ft (297m) Torrey Canyon was carrying 100,000 tons of crude oil when it hit the UK‘s south-west coast.
The shipwreck coated miles of Cornish beach in brown sludge with the pollution stretching from Hartland Point in North Devon to the Channel Islands and even the coast of Normandy.""", sourceType="TEXT")

print(output.summary)

# Second example
response = ai21.Segmentation.execute(
    source="https://en.wikipedia.org/wiki/Tom_Brady",
    sourceType='URL')

# print(response.segments[0].summary)
print(response.segments[0].values['segmentText'])
