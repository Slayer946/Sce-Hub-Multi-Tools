import requests
import threading
from Config.Util import *
from Config.config import *


RED = "\033[91m"
WHITE = "\033[97m"
RESET = "\033[0m"


try:
    Title("Discord Token Delete Dm")

    with open('TokenDisc.txt', 'r') as f:
        token = f.read().strip()
        
    r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token})
    if r.status_code != 200:
        ErrorToken()

    def DmDeleter(token, channels):
        for channel in channels:
            try:
                requests.delete(f'https://discord.com/api/v7/channels/{channel["id"]}', headers={'Authorization': token})
                print(f"{RED}[{WHITE}{current_time_hour()}{RED}] Delete | Channel: {RESET}{channel['id']}")
            except Exception as e:
                print(f"{RED}[{WHITE}{current_time_hour()}{RED}] Error: {e}")

    channel_id = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token}).json()
    if not channel_id:
        print(f"{INFO} No Dm found.")
        Continue()
        Reset()

    processes = []
    for chunk in [channel_id[i:i+3] for i in range(0, len(channel_id), 3)]:
        t = threading.Thread(target=DmDeleter, args=(token, chunk))
        t.start()
        processes.append(t)

    for process in processes:
        process.join()

    Continue()
    Reset()

except Exception as e:
    Error(e)
