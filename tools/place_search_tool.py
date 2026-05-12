import os
from utils.place_info_search import GooglePlaceSearchTool, TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_doten

class PlaceSearchTool:
    def __init__(self):
        load_doten()
        self.google_api_key = os.environ.get("GPLACES_API_KEY")
        self.google_place_search = GooglePlaceSearchTool(self.google_api_key)
        self.tavily_Search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self._setup_tools

    def _setup_tools(self) -> List:
        """Setup all tools from the place search tool"""
        @tool
        def search_attractions(place:str) -> str:
            """Search attractions near the place"""
            try:
                attraction_result = self.google_place_search.google_search_attractions(place)
                if attraction_result:
                    return f"Following are the attractions of {place} as suggested by google {attraction_result}"
            except Exception as e:
                tavily_result = self.tavily_Search.tavily_search_attractions(place)
                return f"Google cannot find the details due to {e}. \nfollowing are the attractions of {place}"
            
        @tool
        def search_restaurants(place:str)-> str:
            """Search near by restaurants"""
            try:
                restaturant_result = self.google_place_search.google_search_restaurants(place)
                if restaturant_result:
                    return f"Following are the top restaurants near{place} as suggest by google {restaturant_result}"
            except Exception as e:
                tavily_result = self.tavily_Search.tavily_search_restaurants(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the restaurants of {place}"
            
        @tool
        def search_activities(place:str)->str:
            """Search activities near the place"""
            try:
                activities_result = self.google_place_search.google_search_activities(place)
                if activities_result:
                    return f"Following are the activities in and around {place}"
            except Exception as e:
                tavily_result = self.tavily_Search.tavily_search_activities(place)
                return f"Google cannot find the details due to {e}. \n Following are the activities of {place}"
            
            @tool
            def search_transportation(place:str)->str:
                """Search mode of transportation in the place"""
                try:
                    transportation_result = self.google_place_search.google_search_transportation(place)
                    if transportation_result:
                        return f"Following are the modes of transportation in and around {place}"
                except Exception as e:
                    tavily_result = self.tavily_Search.tavily_search_transportation(place)
                    return f"Google cannot find the details due to {e}. \nFollowing are the modes of transportations in {place}"
            return [search_activities, search_restaurants, search_attractions, search_transportation]