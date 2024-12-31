from crewai_tools import SerperDevTool
from dotenv import load_dotenv
from pprint import pprint


load_dotenv()

map_data = SerperDevTool(
    search_url="https://google.serper.dev/maps",
    country="In",
    locale="en",
    location="Bengaluru, Karnataka",
    n_results=2,
)


# print(map_data.run(search_query="Security services"))
Data=map_data.run(search_query="Security services in Karnataka")

print(type(Data))
print(type(Data['places']))
print(len(Data['places']))

fields_to_extract = ['title', 'address', 'type', 'website', 'phoneNumber']

# Filtered results
filtered_places = []
karnataka_filtered_places = []

for place in Data['places']:
    # print(place)  # Prints each dictionary in the list
    # Extract only the required fields
    filtered_place = {key: place.get(key, "N/A") for key in fields_to_extract}
    filtered_places.append(filtered_place)
    if 'Karnataka' in place.get('address', ''):
        karnataka_filtered_places.append(filtered_place)
    # Print the filtered place
    # print(filtered_place)
    pprint(karnataka_filtered_places)
