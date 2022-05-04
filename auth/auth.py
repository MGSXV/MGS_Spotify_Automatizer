import base64
import datetime
import requests

class SpotifyAuth(object):
	access_token = None
	expire_date = datetime.datetime.now()
	is_expired = True
	client_id = None
	client_secret = None
	token_url = "https://accounts.spotify.com/api/token"

	def __init__(self, client_id, client_secret):
		super().__init__()
		self.client_id = client_id
		self.client_secret = client_secret

	def get_client_credentials(self):
		"""
        Returns a base64 encoded string
        """
		client_id = self.client_id
		client_secret = self.client_secret
		if client_id == None or client_secret == None:
			raise Exception("Insert Client ID and Client Secret.")
		client_credentials = f"{client_id}:{client_secret}"
		client_credentials_base64 = base64.b64encode(client_credentials.encode())
		return client_credentials_base64.decode()

	def get_token_headers(self):
		client_credentials_base64 = self.get_client_credentials()
		return {
			"Authorization": f"Basic {client_credentials_base64}"
		}

	def get_token_data(self):
		return {
			"grant_type": "client_credentials"
		}

	def perform_auth(self):
		token_url = self.token_url
		token_data = self.get_token_data()
		token_headers = self.get_token_headers()
		request_auth = requests.post(token_url, token_data, headers=token_headers)
		if request_auth.status_code not in range(200, 299):
			raise Exception("Authentication Error!")
		data = request_auth.json()
		access_token = data["access_token"]
		expires_in = data["expires_in"]
		now = datetime.datetime.now()
		expires = now + expires_in
		self.access_token = access_token
		self.expire_date = expires
		self.is_expired = expires < now
		return True

	def get_access_token(self):
		token = self.access_token
		expires = self.expire_date
		now = datetime.datetime.now()
		if expires < now:
			self.perform_auth()
			return self.get_access_token
		elif token == None:
			self.perform_auth()
			return self.get_access_token
		return token
