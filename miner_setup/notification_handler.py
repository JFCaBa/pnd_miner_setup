import json

class NotificationHandler:
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def handle_notification(self, cHandle, data):
        try:
            data_str = data.decode("utf-8")
            print(f"Received [{data_str}]")

            # Parse data as JSON
            payload = json.loads(data_str)
            hotspot = payload.get("hotspot")
            password = payload.get("password")
            wallet = payload.get("wallet")

            # Update WiFi settings
            if hotspot and password:
                self.update_wifi_settings(hotspot, password)
                print("WiFi settings updated.")

            # Cache wallet address
            if wallet:
                self.wallet_address = wallet
                print(f"Cached wallet address: {self.wallet_address}")

        except json.JSONDecodeError as e:
            print(f"An error occurred: {e.msg}")