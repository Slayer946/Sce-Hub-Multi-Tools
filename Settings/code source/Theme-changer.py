from Config.Util import *
from Config.config import *

try:
    import requests
    import time
    from itertools import cycle
except Exception as e:
    ErrorModule(e)

Title("Discord Token Theme Changer")

try:
    print()
    with open('TokenDisc.txt', 'r') as f:
        token = f.read().strip()

    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    
    if r.status_code == 200:
        try:
            amount = int(input(f"{color.RED}{INPUT} Enter the number of cycles -> {color.RESET}"))
        except ValueError:
            ErrorNumber()
                
        modes = cycle(["light", "dark"])
        for i in range(amount):
            theme = next(modes)
            try:
                print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Changed{color.RED} | Theme: {color.WHITE}{theme}{color.RED}")
                time.sleep(0.5)
                setting = {'theme': theme}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
            except Exception as e:
                print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error {e}{color.RED}  | Theme: {color.WHITE}{theme}{color.RED}")

        print(f"{color.RED}{INFO} Finish.")
        Continue()
        Reset()
    else:
        ErrorToken()

except Exception as e:
    Error(e)
