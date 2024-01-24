import subprocess

class WifiManager:
    @staticmethod
    def update_wifi_settings(ssid, psk):
        config_lines = [
            '\nnetwork={',
            f'    ssid="{ssid}"',
            f'    psk="{psk}"',
            '    key_mgmt=WPA-PSK',
            '}'
        ]
        with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'a') as wifi_file:
            wifi_file.writelines('\n'.join(config_lines))
        subprocess.run(['wpa_cli', '-i', 'wlan0', 'reconfigure'])