import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import os
import json
import time

class spotifyAuth(object):
    client_id = None
    client_secret = None
    redirect = None
    user_name = None
    scope = 'playlist-read-collaborative playlist-modify-public playlist-read-private playlist-modify-private'
    def __init__(self, client_id, client_secret, redirect, user_name):
        super().__init__()
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect = redirect
        self.user_name = user_name

    def get_access_token(self):
        user_name = self.user_name
        scope = self.scope
        client_id = self.client_id
        client_secret = self.client_secret
        redirect = self.redirect
        oauth_obj = spotipy.SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect, scope=scope)
        token_dict = oauth_obj.get_access_token()
        return token_dict['access_token']

    def perform_oauth(self):
        token = self.get_access_token()
        spotify_obj = spotipy.Spotify(auth=token)
        return (spotify_obj)

    def get_playlists(self, spotify_obj: spotipy.Spotify):
        limit = 50
        offset = 0
        user_name = self.user_name
        playlists = spotify_obj.user_playlists(user_name, limit, offset)
        while len(playlists["items"]) != 0:
            for item in playlists["items"]:
                print(item["name"].encode('utf-8'))
            offset += limit
            playlists = spotify_obj.user_playlists(user_name, limit, offset)