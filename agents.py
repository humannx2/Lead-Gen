from crewai import Agent
from tools import map_data
from crewai import LLM
from dotenv import load_dotenv
import os

load_dotenv()

# Retrieve the API key
api_key = os.getenv("OPENAI_API_KEY")

llm = LLM(model="groq/gemma2-9b-it",api_key=api_key)

# Extract leads
lead_extractor=Agent(
    role="To extract the places that fall under the category of {category} from google maps",
    goal="Use the {category} category to provide the list of places with which fall under the same category using Google Maps",
    backstory="With over 10 years of experience in lead generation using google maps, you excel at finding companies and list of places under any category.",
    memory=True,
    verbose=True,
    allow_delegation=True,
    tools=[map_data,],
    max_iter=2,
    llm=llm
#     system_template="Uses the category given by the user to provide a list of places and companies under that category using google maps",
#     response_template="Give the detail of output in the format of Name, Address, Contact, Email."
)