import requests
import time

class ConnectionManager:
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    @staticmethod
    def has_internet_connection(self):
        try:
            requests.get("http://www.google.com", timeout=5)
            return True
        except (requests.ConnectionError, requests.Timeout):
            return False

    def wait_for_conditions(self):
        while True:
            if self.wallet_address and self.has_internet_connection():
                print("Internet connection available and wallet address received. Starting Docker container.")
                self.start_docker_container()
                break
            elif not self.wallet_address:
                print("\rWaiting for wallet address...     ",end='')
            elif not self.has_internet_connection():
                print("\rWaiting for internet connection...", end='')
            time.sleep(5)  # Check every 5 seconds