import requests
import threading
from Config.Util import *
from Config.config import *

try:
    Title("Discord Token Delete Friends")

    with open('TokenDisc.txt', 'r') as f:
        token = f.read().strip()

    r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token})
    if r.status_code != 200:
        ErrorToken()

    def DeleteFriends(friends, token):
        for friend in friends:
            try:
                requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{friend["id"]}', headers={'Authorization': token})
                print(f"{red}[{white}{current_time_hour()}{red}] Delete | User: {RESET}{friend['user']['username']}#{friend['user']['discriminator']}")
            except Exception as e:
                print(f"{red}[{white}{current_time_hour()}{red}] Error: {e}")

    friend_id = requests.get("https://discord.com/api/v9/users/@me/relationships", headers={'Authorization': token}).json()
    
    if not friend_id:
        print(f"{INFO} No friends found.")

    processes = []
    for chunk in [friend_id[i:i+3] for i in range(0, len(friend_id), 3)]:
        t = threading.Thread(target=DeleteFriends, args=(chunk, token))
        t.start()
        processes.append(t)

    for process in processes:
        process.join()

    Continue()
    Reset()

except Exception as e:
    Error(e)
