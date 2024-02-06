from shlex import split as s
from subprocess import check_output, run as r
from config import w1700k

ip = w1700k["ip"]
username = w1700k["username"]
password = w1700k["password"]


def login(ip, username, password):
    print("[+] Logging in...")

    login = r(
        s(
            f"curl -k -v -c cookie 'https://{ ip }/cgi/cgi_action' --data 'username={ username }&password={ password }'"
        ),
        capture_output=True,
    )
    print("[+] Cookie created...")
    print(f"[+] Connection #0 to host { ip } left intact...")
    print("[!] Logged in...")

    return login


if __name__ == "__main__":
    login(ip, username, password)
