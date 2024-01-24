import subprocess


class DockerManager:
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def start_docker_container(self):
        # Stop the existing container if it's running
        subprocess.run(["docker", "stop", "worker"], stderr=subprocess.DEVNULL)
        subprocess.run(["docker", "rm", "worker"], stderr=subprocess.DEVNULL)

        # Start a new container with the wallet address as an environment variable
        subprocess.run([
            "docker", "run",
            "--name", "worker",
            "-e", f"WALLET_ADDRESS={self.wallet_address}",
            "-d",
            "jfca68/pnd_scanner_worker"
        ])