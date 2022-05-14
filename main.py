from os import access
from auth.auth import spotifyAuth

def	main():
	client_id = input("Enter your Client ID: ")
	client_secret = input("Enter your Client Secret: ")
	user_name = input("Enter your username: ")
	redirect = input("Enter your redirect URI: ")
	spotify = spotifyAuth(client_id, client_secret, redirect, user_name)
	spotify_obj = spotify.perform_oauth()
	spotify.get_playlists(spotify_obj)

if __name__ == "__main__":
	main()