from Config.Util import *
from Config.config import *
import requests
import subprocess
import sys
import webbrowser

try:
    def map_banner():
        print("""
         ____        _   _             
        |  _ \      | | | |            
        | |_) | ___ | |_| |_ ___ _ __  
        |  _ < / _ \| __| __/ _ \ '_ \ 
        | |_) | (_) | |_| ||  __/ | | |
        |____/ \___/ \__|\__\___|_| |_|

        Welcome to IP Info Tool!
        """)

    def BrowserPrivate(site, title, search_bar=True):
        # Ouvrir le navigateur avec l'URL spécifiée
        if search_bar:
            webbrowser.open_new(f"https://www.google.com/search?q={site}")
        else:
            webbrowser.open_new(site)

    Title("Ip Info")
    map_banner()
    
    ip = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Ip -> {reset}")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}")

    try:
        if sys.platform.startswith("win"):
            result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True, timeout=1)
        elif sys.platform.startswith("linux"):
            result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, text=True, timeout=1)
        if result.returncode == 0:
            ping = "Succeed"
        else:
            ping = "Fail"
    except Exception as e:
        ping = "Fail"
    
    try:
        response = requests.get(f"https://{website}/api/ip/ip={ip}")
        api = response.json()

        ip = api.get('ip', 'None')
        status = api.get('status', 'Invalid')
        country = api.get('country', 'None')
        country_code = api.get('country_code', 'None')
        region = api.get('region', 'None')
        region_code = api.get('region_code', 'None')
        zip_code = api.get('zip', 'None')
        city = api.get('city', 'None')
        latitude = api.get('latitude', 'None')
        longitude = api.get('longitude', 'None')
        timezone = api.get('timezone', 'None')
        isp = api.get('isp', 'None')
        org = api.get('org', 'None')
        as_host = api.get('as', 'None')
        loc_url = api.get('loc_url', f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}")
        credit = api.get('credit', 'None')
        copyright = api.get('copyright', 'None')

    except Exception as e:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        api = response.json()

        status = "Valid" if api.get('status') == "success" else "Invalid"
        country = api.get('country', 'None')
        country_code = api.get('countryCode', 'None')
        region = api.get('regionName', 'None')
        region_code = api.get('region', 'None')
        zip_code = api.get('zip', 'None')
        city = api.get('city', 'None')
        latitude = api.get('lat', 'None')
        longitude = api.get('lon', 'None')
        timezone = api.get('timezone', 'None')
        isp = api.get('isp', 'None')
        org = api.get('org', 'None')
        as_host = api.get('as', 'None')
        loc_url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

    print(f"""
    {INFO_ADD} Ip         : {white}{ip}{red}
    {INFO_ADD} Ping       : {white}{ping}{red}
    {INFO_ADD} Status     : {white}{status}{red}
    {INFO_ADD} Country    : {white}{country} ({country_code}){red}
    {INFO_ADD} Region     : {white}{region} ({region_code}){red}
    {INFO_ADD} Zip        : {white}{zip_code}{red}
    {INFO_ADD} City       : {white}{city}{red}
    {INFO_ADD} Latitude   : {white}{latitude}{red}
    {INFO_ADD} Longitude  : {white}{longitude}{red}
    {INFO_ADD} Timezone   : {white}{timezone}{red}
    {INFO_ADD} Isp        : {white}{isp}{red}
    {INFO_ADD} Org        : {white}{org}{red}
    {INFO_ADD} As         : {white}{as_host}{red}
    {reset}""")
    
    try:
        BrowserPrivate(site=loc_url, title=f"Ip Localisation ({latitude}, {longitude})", search_bar=False)
    except Exception as e:
        pass

    Continue()
    Reset()

except Exception as e:
    Error(e)
   