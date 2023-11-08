# get AI21_API_KEY. Use https://studio.ai21.com/account/account
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import AI21
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

AI21_API_KEY = os.getenv('API_KEY')

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm = AI21(ai21_api_key=AI21_API_KEY)
llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"
output = llm_chain.run(question)

print(output)
