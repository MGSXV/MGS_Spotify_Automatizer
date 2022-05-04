from auth.auth import SpotifyAuth

def	main():
	client_id = input("Enter your Client ID: ")
	client_secret = input("Enter your Client Secret: ")
	spotify = SpotifyAuth(client_id, client_secret)
	spotify.perform_auth()

if __name__ == "__main__":
	main()