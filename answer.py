import ai21
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()
ai21.api_key = os.getenv('API_KEY')

output = ai21.Answer.execute(context="In 2020 and 2021, enormous QE — approximately $4.4 trillion, or 18%, of 2021 gross domestic product (GDP) — and enormous fiscal stimulus (which has been and always will be inflationary) — approximately $5 trillion, or 21%, of 2021 GDP — stabilized markets and allowed companies to raise enormous amounts of capital. In addition, this infusion of capital saved many small businesses and put more than $2.5 trillion in the hands of consumers and almost $1 trillion into state and local coffers. These actions led to a rapid decline in unemployment, dropping from 15% to under 4% in 20 months — the magnitude and speed of which were both unprecedented. Additionally, the economy grew 7% in 2021 despite the arrival of the Delta and Omicron variants and the global supply chain shortages, which were largely fueled by the dramatic upswing in consumer spending and the shift in that spend from services to goods.",
                             question="Did the economy shrink after the Omicron variant arrived?")
print(output.answer)
print("\n")

output = ai21.Answer.execute(context="In 2020 and 2021, enormous QE — approximately $4.4 trillion, or 18%, of 2021 gross domestic product (GDP) — and enormous fiscal stimulus (which has been and always will be inflationary) — approximately $5 trillion, or 21%, of 2021 GDP — stabilized markets and allowed companies to raise enormous amounts of capital. In addition, this infusion of capital saved many small businesses and put more than $2.5 trillion in the hands of consumers and almost $1 trillion into state and local coffers. These actions led to a rapid decline in unemployment, dropping from 15% to under 4% in 20 months — the magnitude and speed of which were both unprecedented. Additionally, the economy grew 7% in 2021 despite the arrival of the Delta and Omicron variants and the global supply chain shortages, which were largely fueled by the dramatic upswing in consumer spending and the shift in that spend from services to goods.",
                             question="Did COVID-19 eventually help the economy?")
print(output.answer)
print("\n")

output = ai21.Answer.execute(context="In 2020 and 2021, enormous QE — approximately $4.4 trillion, or 18%, of 2021 gross domestic product (GDP) — and enormous fiscal stimulus (which has been and always will be inflationary) — approximately $5 trillion, or 21%, of 2021 GDP — stabilized markets and allowed companies to raise enormous amounts of capital. In addition, this infusion of capital saved many small businesses and put more than $2.5 trillion in the hands of consumers and almost $1 trillion into state and local coffers. These actions led to a rapid decline in unemployment, dropping from 15% to under 4% in 20 months — the magnitude and speed of which were both unprecedented. Additionally, the economy grew 7% in 2021 despite the arrival of the Delta and Omicron variants and the global supply chain shortages, which were largely fueled by the dramatic upswing in consumer spending and the shift in that spend from services to goods.",
                             question="How did COVID-19 affect the financial crisis of 2008?")
print(output.answer)
print("\n")
