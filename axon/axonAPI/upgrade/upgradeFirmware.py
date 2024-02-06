from shlex import split as s
from subprocess import run as r
from config import w1700k
from login import login

ip = w1700k["ip"]
username = w1700k["username"]
password = w1700k["password"]
firmware = w1700k["firmware"]


def upgrade(ip, firmware):
    upgrade_firmware = r(
        s(
            f"curl -k -v -b cookie -F 'firmware=@../firmware/{ firmware }' -H 'X-Requested-With: XMLHttpRequest' 'https://{ ip }/cgi/cgi_set?Object=Device.X_AXON_Upgrade.Upgrade.4.&Operation=Modify&State=UPG_REQ&FileType=FIRMWARE&FileName=firmware.bin'"
        )
    )

    return upgrade_firmware


if __name__ == "__main__":
    login(ip, username, password)
    upgrade(ip, firmware)
