from crewai import Task
from agents import lead_extractor

lead_gen_task=Task(
    description="""Conduct a through check on the maps to find the potential companies and startups under the given cateory.
    Make sure all the shortlisted companies/startups/organisations are based out on Karnataka, India""",
    expected_output="""A list with the Name, Contact Detals, Email, and Location of the shortlisted companies. 
    Leave the fields blank if any information from any comapny is missing""",
    agent=lead_extractor,
    output_file="Leads.csv"

)