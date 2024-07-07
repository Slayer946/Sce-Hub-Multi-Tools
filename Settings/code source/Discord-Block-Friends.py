import requests
import threading
from Config.Util import *
from Config.config import *

RED = "\033[91m"
WHITE = "\033[97m"
RESET = "\033[0m"

try:
    Title("Discord Token Block Friends")

    with open('TokenDisc.txt', 'r') as f:
        token = f.read().strip()

    r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token})
    r.raise_for_status()
    if r.status_code != 200:
        ErrorToken()

    def block_friend(token, friend):
        try:
            response = requests.put(f'https://discord.com/api/v9/users/@me/relationships/{friend["id"]}', headers={'Authorization': token}, json={"type": 2})
            response.raise_for_status()
            print(f"{RED}[{WHITE}{current_time_hour()}{RED}] Blocked | User: {RESET}{friend['user']['username']}#{friend['user']['discriminator']}")
        except requests.exceptions.RequestException as e:
            print(f"{RED}[{WHITE}{current_time_hour()}{RED}] Error: {e}")

    friend_ids = requests.get("https://discord.com/api/v9/users/@me/relationships", headers={'Authorization': token}).json()
    
    if not friend_ids:
        print(f"{INFO} No friends found.")
        Continue()
        Reset()
    
    threads = []
    for chunk in [friend_ids[i:i+3] for i in range(0, len(friend_ids), 3)]:
        for friend in chunk:
            t = threading.Thread(target=block_friend, args=(token, friend))
            t.start()
            threads.append(t)
    
    for thread in threads:
        thread.join()

    Continue()
    Reset()

except Exception as e:
    Error(e)
