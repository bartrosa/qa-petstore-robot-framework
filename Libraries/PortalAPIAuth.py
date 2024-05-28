import requests

class PortalAPIAuth:
    def __init__(self, base_url, client_id, client_secret):
        self.base_url = base_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None

    def authenticate(self):
        auth_url = f"{self.base_url}/auth/token"
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }
        response = requests.post(auth_url, data=payload)
        response.raise_for_status()
        self.token = response.json().get('access_token')

    def get_token(self):
        if not self.token:
            self.authenticate()
        return self.token
