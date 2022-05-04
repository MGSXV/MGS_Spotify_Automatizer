from auth.auth import SpotifyAuth
from app.test_playlist import Playlist

def	main():
	client_id = input("Enter your Client ID: ")
	client_secret = input("Enter your Client Secret: ")
	spotify = SpotifyAuth(client_id, client_secret)
	access_token = spotify.get_access_token()
	print(access_token)
	playlists = Playlist(access_token)
	print(playlists.get_user_playlists())

if __name__ == "__main__":
	main()