from crewai import Crew, Process
from tools import map_data
from agents import lead_extractor
from tasks import lead_gen_task
from dotenv import load_dotenv
import re

load_dotenv()

crew1 = Crew(
    agents=[lead_extractor],
    tasks=[lead_gen_task],
    process=Process.sequential,
    memory=True,
    cache=False,
    max_rpm=100,
    share_crew=True
)

result=crew1.kickoff({"category":"Security Services"})