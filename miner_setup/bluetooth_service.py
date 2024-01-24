import bluetooth
import traceback
class BluetoothService:
    def __init__(self):
        self.server_sock = None
        self.client_sock = None

    def setup_service(self):
        self.server_sock = None
        self.client_sock = None
        self.wallet_address = None  # Initialize wallet_address as None
        print("Setting up Bluetooth server")
    
    def run(self):
        try:
            self.setup_service()
             # Create a new server socket using RFCOMM protocol
            self.server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

            # Bind to any port
            self.server_sock.bind(("", bluetooth.PORT_ANY))
            self.server_sock.listen(1)

            # Get the port the server socket is listening
            port = self.server_sock.getsockname()[1]

            # Provide a valid UUID for the service
            service_id = "00001101-0000-1000-8000-00805F9B34FB"
            service_name = "My Miner Service"
            service_classes = [service_id, bluetooth.SERIAL_PORT_CLASS]
            profiles = [bluetooth.SERIAL_PORT_PROFILE]
        
            bluetooth.advertise_service(
                self.server_sock, service_name,
                service_id=service_id,
                service_classes=service_classes,
                profiles=profiles
            )

            print(f"Waiting for connection on RFCOMM channel {port}")

            # Accept incoming connections
            self.client_sock, client_info = self.server_sock.accept()
            print(f"Accepted connection from {client_info}")

            # Now you can use self.client_sock to communicate with the connected device
            # Use self.client_sock.recv(size) to read data and self.client_sock.send(data) to send data

            # ... (handle notifications and other logic)
        except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc()
        finally:
            if self.client_sock:
                self.client_sock.close()
            if self.server_sock:
                self.server_sock.close()
            print("Disconnected.")

