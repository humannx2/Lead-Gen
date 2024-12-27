from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

map_data = SerperDevTool(
    search_url="https://google.serper.dev/maps",
    country="In",
    locale="en",
    location="Bengaluru, Karnataka, India",
    n_results=2,
)

# print(tool.run(search_query="Security services"))