import json
import base64
from colorama import Fore
import os


path = os.path.join(os.getenv("APPDATA"), "rays-client", "config.json")

try:
    with open(path, 'r') as f:
        alts = json.load(f)
except FileNotFoundError:
    print(f"{Fore.RED}[-] {Fore.RESET}Config file not found")
    exit()

with open('alts.txt', 'w') as outfile:

    for item in alts["alts"]:
        username = item["username"]
        password = base64.b64decode(item["password"]).decode("utf-8")

        outfile.write(f"Username: {username}\n")
        outfile.write(f"Password: {password}\n\n")

print(f"{Fore.BLUE}[+] {Fore.RESET}Done!")