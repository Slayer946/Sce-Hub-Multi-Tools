from Config.config import INFO_ADD, WHITE, RED
from Config.Util import Title, Continue, Error, ErrorModule

import requests
import json
import time

# Définition locale de RESET
RESET = "\033[0m"

# Fonction locale pour obtenir l'heure actuelle sous forme de chaîne
def current_time_hour():
    return time.strftime("%H:%M:%S")

try:
    Title("Roblox Cookie Info")

    cookie = input(f"\n{current_time_hour()} {INFO_ADD} Cookie -> {WHITE}")
    print(f"{current_time_hour()} Information Recovery..")

    try:
        info = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie})
        information = info.json()
        status = "Valid"
    except Exception as e:
        status = "Invalid"
        Error(f"Error retrieving information: {e}")

    try:
        username_roblox = information.get('UserName', 'None')
    except Exception as e:
        username_roblox = "None"
        Error(f"Error retrieving username: {e}")

    try:
        user_id_roblox = information.get("UserID", 'None')
    except Exception as e:
        user_id_roblox = "None"
        Error(f"Error retrieving user ID: {e}")

    try:
        robux_roblox = information.get("RobuxBalance", 'None')
    except Exception as e:
        robux_roblox = "None"
        Error(f"Error retrieving Robux balance: {e}")

    try:
        premium_roblox = information.get("IsPremium", 'None')
    except Exception as e:
        premium_roblox = "None"
        Error(f"Error retrieving premium status: {e}")

    try:
        avatar_roblox = information.get("ThumbnailUrl", 'None')
    except Exception as e:
        avatar_roblox = "None"
        Error(f"Error retrieving avatar URL: {e}")

    try:
        builders_club_roblox = information.get("IsAnyBuildersClubMember", 'None')
    except Exception as e:
        builders_club_roblox = "None"
        Error(f"Error retrieving Builders Club membership status: {e}")

    print(f"""
    {INFO_ADD} Status        : {WHITE}{status}{RESET}
    {INFO_ADD} Username      : {WHITE}{username_roblox}{RESET}
    {INFO_ADD} Id            : {WHITE}{user_id_roblox}{RESET}
    {INFO_ADD} Robux         : {WHITE}{robux_roblox}{RESET}
    {INFO_ADD} Premium       : {WHITE}{premium_roblox}{RESET}
    {INFO_ADD} Builders Club : {WHITE}{builders_club_roblox}{RESET}
    {INFO_ADD} Avatar        : {WHITE}{avatar_roblox}{RESET}
    """)

    Continue()
    RESET()

except Exception as e:
    Error(e)
