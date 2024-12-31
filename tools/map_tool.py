# from crewai_tools import SerperDevTool
# from dotenv import load_dotenv
# from pprint import pprint


# load_dotenv()

# map_data = SerperDevTool(
#     search_url="https://google.serper.dev/maps",
#     country="In",
#     locale="en",
#     location="Bengaluru, Karnataka",
#     n_results=2,
# )


# # print(map_data.run(search_query="Security services"))
# Data=map_data.run(search_query="Security services in Karnataka")

# print(type(Data))
# print(type(Data['places']))
# print(len(Data['places']))

# fields_to_extract = ['title', 'address', 'type', 'website', 'phoneNumber']

# # Filtered results
# filtered_places = []
# karnataka_filtered_places = []

# for place in Data['places']:
#     # print(place)  # Prints each dictionary in the list
#     # Extract only the required fields
#     filtered_place = {key: place.get(key, "N/A") for key in fields_to_extract}
#     filtered_places.append(filtered_place)
#     if 'Karnataka' in place.get('address', ''):
#         karnataka_filtered_places.append(filtered_place)
#     # Print the filtered place
#     # print(filtered_place)
#     pprint(karnataka_filtered_places)


from crewai_tools import SerperDevTool
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

class MapTool:
    def __init__(self, location="Bengaluru, Karnataka", n_results=10):
        self.map_data = SerperDevTool(
            search_url="https://google.serper.dev/maps",
            country="In",
            locale="en",
            location=location,
            n_results=n_results,
        )
        self.fields_to_extract = ['title', 'address', 'type', 'website', 'phoneNumber']

    def search(self, query):
        """
        Searches Google Maps for the provided query and returns raw results.
        """
        return self.map_data.run(search_query=query)

    def extract_fields(self, places):
        """
        Extracts specific fields from the raw place data.
        """
        return [
            {key: place.get(key, "N/A") for key in self.fields_to_extract}
            for place in places
        ]

    def filter_by_location(self, places, location_keyword="Karnataka"):
        """
        Filters the places by a specific keyword in the address.
        """
        return [
            place
            for place in self.extract_fields(places)
            if location_keyword in place.get('address', '')
        ]

    def search_and_filter(self, query, location_keyword="Karnataka"):
        """
        Combines searching, extracting, and filtering in one step.
        """
        data = self.search(query)
        return self.filter_by_location(data['places'], location_keyword)

# if __name__ == "__main__":
#     map_tool = MapTool(location="Bengaluru, Karnataka", n_results=2)

#     # Search and filter places
#     query = "Security services in Karnataka"
#     filtered_places = map_tool.search_and_filter(query)

#     # Print filtered results
#     print("Filtered Places:")
#     pprint(filtered_places)

