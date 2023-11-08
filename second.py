# get AI21_API_KEY. Use https://studio.ai21.com/account/account
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import AI21

from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

AI21_API_KEY = os.getenv('API_KEY')

template = "tell me a joke about {foo}"

prompt = PromptTemplate(template=template, input_variables=["foo"])
llm = AI21(ai21_api_key=AI21_API_KEY)
llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "dog"
output = llm_chain.run(question)

print(output)
