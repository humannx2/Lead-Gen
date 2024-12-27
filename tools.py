from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

tool = SerperDevTool(
    search_url="https://google.serper.dev/maps",
    country="In",
    # locale="In",
    location=["Bengaluru", "Bangalore"],
    n_results=2,
)

print(tool.run(search_query="Security services"))