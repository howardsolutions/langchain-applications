import os 
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linked_in_profile_url: str, mock: bool = False):
    """ 
        scrape information from Linkedin profiles, 
        Manually scrape the information from the linked in profile
    """
    if mock:
        linked_in_profile_url = "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json"
        response = requests.get(
            linked_in_profile_url,
            timeout=10
        )
        
        data = response.json().get("person")
        return data
    
    
if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linked_in_profile_url="https://www.linkedin.com/in/eden-marco",
            mock=True
        )
    )