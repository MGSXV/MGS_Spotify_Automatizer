import json
from urllib.parse import urlencode
import requests

class Playlist(object):
    endpoint = "https://api.spotify.com/v1/me/playlists"
    def __init__(self, access_token):
        super().__init__()
        self.access_token = access_token
        
    def get_user_playlists(self):
        endpoint = self.endpoint
        access_token = self.access_token
        headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
        }
        params = urlencode({"limit": 50, "offset": 0})
        req_url = f"{endpoint}?{params}"
        response = requests.get(req_url, headers=headers)
        print(response.json())