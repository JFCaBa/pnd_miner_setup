from docker_manager import DockerManager
from wifi_manager import WifiManager
from connection_manager import ConnectionManager
from notification_handler import NotificationHandler
from bluetooth_service import BluetoothService

if __name__ == "__main__":
    wallet_address = None  # Initialize or retrieve from some source

    docker_manager_instance = DockerManager(wallet_address)
    wifi_manager_instance = WifiManager()
    connection_manager_instance = ConnectionManager(wallet_address)
    notification_handler_instance = NotificationHandler(wallet_address)
    bluetooth_service_instance = BluetoothService()

    # Run your Bluetooth service
    bluetooth_service_instance.run()
