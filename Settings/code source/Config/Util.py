from config import *
try:
    import colorama
    import ctypes
    import subprocess
    import os
    import time
    import sys
    import datetime
    import requests
    import webbrowser
except Exception as e:
    import os
    print(f"[x] | Error Module (Restart Setup.bat): {e}")
    os.system("pause")

color_webhook = 0xa80505
username_webhook = name_tool  # Assuming name_tool is defined in Config
avatar_webhook = "https://cdn.discordapp.com/avatars/1128008782727893082/47da442ba728f4c4233a0586defa3ff9.png?size=512"

color = colorama.Fore
colorama.init()
red = color.RED
white = color.WHITE
green = color.GREEN
reset = color.RESET
blue = color.BLUE
yellow = color.YELLOW

try:
    username_pc = os.getlogin()
except OSError:
    username_pc = "username"

censored = "slayer946"

def current_time_day_hour():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def current_time_hour():
    return datetime.datetime.now().strftime('%H:%M:%S')

BEFORE = f'{red}[{white}'
AFTER = f'{red}]'

BEFORE_GREEN = f'{green}[{white}'
AFTER_GREEN = f'{green}]'

INPUT = f'{BEFORE}>{AFTER} |'
INFO = f'{BEFORE}!{AFTER} |'
ERROR = f'{BEFORE}x{AFTER} |'
ADD = f'{BEFORE}+{AFTER} |'
WAIT = f'{BEFORE}~{AFTER} |'

GEN_VALID = f'{BEFORE_GREEN}+{AFTER_GREEN} |'
GEN_INVALID = f'{BEFORE}x{AFTER} |'

INFO_ADD = f'{white}[{red}+{white}]{red}'

def ModuleInstall(module):
    subprocess.check_call(['pip', 'install', module])

def ModuleUninstall(module):
    subprocess.check_call(['pip', 'uninstall', module])

def Title(title):
    if sys.platform.startswith("win"):
        ctypes.windll.kernel32.SetConsoleTitleW(f"{name_tool} {version_tool} | {title}")
    elif sys.platform.startswith("linux"):
        sys.stdout.write(f"\x1b]2;{name_tool} {version_tool} | {title}\x07")
        
def Clear():
    if sys.platform.startswith("win"):
        os.system("cls")
    elif sys.platform.startswith("linux"):
        os.system("clear")

def Reset():
    if sys.platform.startswith("win"):
        file = 'python RedTiger.py'
    elif sys.platform.startswith("linux"):
        file = 'python3 RedTiger.py'
    subprocess.run(file, shell=True)

def StartProgram(program):
    if sys.platform.startswith("win"):
        file = f'python Settings/Program/{program}'
    elif sys.platform.startswith("linux"):
        file = f'python3 Settings/Program/{program}'
    subprocess.run(file, shell=True)

def Slow(text):
    delay = 0.03
    lines = text.split('\n')
    for line in lines:
        print(line)
        time.sleep(delay)

def Continue():
    input(f"{BEFORE + current_time_hour() + AFTER} {INFO} Press to continue -> " + reset)

def Error(e):
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error: {white}{e}", reset)
    Continue()
    Reset()

def ErrorChoiceStart():
    print(f"\n{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Choice !", reset)
    time.sleep(1)

def ErrorChoice():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Choice !", reset)
    time.sleep(3)
    Reset()

def ErrorId():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid ID !", reset)
    time.sleep(3)
    Reset()

def ErrorUrl():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid URL !", reset)
    time.sleep(3)
    Reset()

def ErrorEdge():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Edge not installed or driver not up to date !", reset)
    time.sleep(3)
    Reset()

def ErrorToken():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Token !", reset)
    time.sleep(3)
    Reset()
    
def ErrorNumber():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Number !", reset)
    time.sleep(3)
    Reset()

def ErrorWebhook():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Webhook !", reset)
    time.sleep(3)
    Reset()

def ErrorCookie():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Cookie !", reset)
    time.sleep(3)
    Reset()

def ErrorUsername():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Username !", reset)
    time.sleep(3)
    Reset()

def ErrorModule(e):
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error Module (Restart Setup.bat): {white}{e}", reset)
    Continue()
    Reset()

def OnlyWindows():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} This function is only available on Windows 10/11 !", reset)
    Continue()
    Reset()

def OnlyLinux():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} This function is only available on Linux !", reset)
    Continue()
    Reset()

def CheckWebhook(webhook):
    if not (webhook.lower().startswith(("https://discord.com/api/webhooks", "http://discord.com/api/webhooks",
                                        "https://canary.discord.com/api/webhooks", "http://canary.discord.com/api/webhooks",
                                        "https://discordapp.com/api/webhooks", "http://discordapp.com/api/webhooks"))):
        ErrorWebhook()

def ChoiceMultiChannelDiscord():
    try:
        num_channels = int(input(f"{INPUT} How many spam channels -> {reset}"))
    except ValueError:
        ErrorNumber()
    
    selected_channels = [] 
    number = 0
    for _ in range(num_channels):
        try:
            number += 1
            selected_channel_number = input(f"{red}{INPUT} Channel Id {number}/{num_channels} -> {reset}")
            selected_channels.append(selected_channel_number)
        except:
            ErrorId()

    return selected_channels

def ChoiceMultiTokenDisord():
    if sys.platform.startswith("linux"):
        return

    def CheckToken(token_number, token):
        r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
        if r.status_code == 200:
            status = f"Valid"
            user = requests.get(
                'https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
            username_discord = user['username']
            token_censored = token[:-25] + '.' * 3
            print(f"{white}[{red}{token_number}{white}]{red} -> {red}Status: {white}{status}{red} | User: {white}{username_discord}{red} | Token: {white}{token_censored}")
        else:
            status = f"Invalid"
            print(f"{white}[{red}{token_number}{white}]{red} -> {red}Status: {white}{status}{red} | {red}Token: {white}{token}")

    file_token_discord = "./TokenDisc.txt"
    tokens = {}
    token_discord_number = 0

    with open(file_token_discord, 'r') as file_token:
        for line in file_token:
            if not line.strip() or line.isspace():
                continue
            token_discord_number += 1
        
        if token_discord_number == 0:
            print(f"{INFO} No Token Discord in file: {white}{file_token_discord}{red} Please add tokens to the file.")
            Continue()
            Reset()
        else:
            print(f"{INFO} {white}{token_discord_number}{red} Token Discord found ({white}{file_token_discord}{red})")
    
    try:
        num_tokens = int(input(f"{INPUT} How many token (max {token_discord_number}) -> {reset}"))
        if num_tokens > token_discord_number:
            ErrorNumber()
    except ValueError:
        ErrorNumber()

    token_discord_number = 0
    with open(file_token_discord, 'r') as file_token:
        print()
        print(f"{red}Token Discord ({white}{file_token_discord}{red}):")
        for line in file_token:
            if not line.strip() or line.isspace():
                continue
            
            token_discord_number += 1
            modified_token = line.strip()
            tokens[token_discord_number] = modified_token
            CheckToken(token_discord_number, modified_token)

    number = 0
    selected_tokens = []
    print()
    for _ in range(num_tokens):
        try:
            number += 1
            selected_token_number = int(input(f"{color.RED}{INPUT} Token Number {number}/{num_tokens} -> {reset}"))
            selected_token = tokens[selected_token_number]
            selected_tokens.append(selected_token)
        except:
            ErrorNumber()

    return selected_tokens

def ChoiceMultiCookieDiscord():
    def CheckCookie(cookie_number, cookie):
        try:
            r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': f'{"YmFzaC5ydDovL3d3dy5wb3N0YWxpcy5jb20vc2Vzc2lvbgo="}'}, cookies={'__cfduid': cookie})
            if r.status_code == 200:
                status = f"Valid"
                user = requests.get(
                    'https://discord.com/api/v8/users/@me', headers={'Authorization': cookie}).json()
                username_discord = user['username']
                cookie_censored = cookie[:-35] + '.' * 3
                print(f"{white}[{red}{cookie_number}{white}]{red} -> {red}Status: {white}{status}{red} | User: {white}{username_discord}{red} | Cookie: {white}{cookie_censored}")
            else:
                status = f"Invalid"
                print(f"{white}[{red}{cookie_number}{white}]{red} -> {red}Status: {white}{status}{red} | {red}Cookie: {white}{cookie}")
        except:
            print(f"{white}[{red}{cookie_number}{white}]{red} -> {red}Error")

    file_cookie_discord = "./CookieDisc.txt"
    cookies = {}
    cookie_discord_number = 0

    with open(file_cookie_discord, 'r') as file_cookie:
        for line in file_cookie:
            if not line.strip() or line.isspace():
                continue
            cookie_discord_number += 1
        
        if cookie_discord_number == 0:
            print(f"{INFO} No Cookie Discord in file: {white}{file_cookie_discord}{red} Please add cookies to the file.")
            Continue()
            Reset()
        else:
            print(f"{INFO} {white}{cookie_discord_number}{red} Cookie Discord found ({white}{file_cookie_discord}{red})")
    
    try:
        num_cookies = int(input(f"{INPUT} How many cookie (max {cookie_discord_number}) -> {reset}"))
        if num_cookies > cookie_discord_number:
            ErrorNumber()
    except ValueError:
        ErrorNumber()

    cookie_discord_number = 0
    with open(file_cookie_discord, 'r') as file_cookie:
        print()
        print(f"{red}Cookie Discord ({white}{file_cookie_discord}{red}):")
        for line in file_cookie:
            if not line.strip() or line.isspace():
                continue
            
            cookie_discord_number += 1
            modified_cookie = line.strip()
            cookies[cookie_discord_number] = modified_cookie
            CheckCookie(cookie_discord_number, modified_cookie)

    number = 0
    selected_cookies = []
    print()
    for _ in range(num_cookies):
        try:
            number += 1
            selected_cookie_number = int(input(f"{color.RED}{INPUT} Cookie Number {number}/{num_cookies} -> {reset}"))
            selected_cookie = cookies[selected_cookie_number]
            selected_cookies.append(selected_cookie)
        except:
            ErrorNumber()

    return selected_cookies

def ChoiceMultiIdChannelDiscord():
    file_id_channel_discord = "./IdChannelDisc.txt"
    id_channels = {}
    id_channel_discord_number = 0

    with open(file_id_channel_discord, 'r') as file_id_channel:
        for line in file_id_channel:
            if not line.strip() or line.isspace():
                continue
            id_channel_discord_number += 1
        
        if id_channel_discord_number == 0:
            print(f"{INFO} No Id Channel Discord in file: {white}{file_id_channel_discord}{red} Please add ids channel to the file.")
            Continue()
            Reset()
        else:
            print(f"{INFO} {white}{id_channel_discord_number}{red} Id Channel Discord found ({white}{file_id_channel_discord}{red})")
    
    try:
        num_id_channels = int(input(f"{INPUT} How many id channel (max {id_channel_discord_number}) -> {reset}"))
        if num_id_channels > id_channel_discord_number:
            ErrorNumber()
    except ValueError:
        ErrorNumber()

    id_channel_discord_number = 0
    with open(file_id_channel_discord, 'r') as file_id_channel:
        print()
        print(f"{red}Id Channel Discord ({white}{file_id_channel_discord}{red}):")
        for line in file_id_channel:
            if not line.strip() or line.isspace():
                continue
            
            id_channel_discord_number += 1
            modified_id_channel = line.strip()
            id_channels[id_channel_discord_number] = modified_id_channel

    number = 0
    selected_id_channels = []
    print()
    for _ in range(num_id_channels):
        try:
            number += 1
            selected_id_channel_number = int(input(f"{color.RED}{INPUT} Id Channel Number {number}/{num_id_channels} -> {reset}"))
            selected_id_channel = id_channels[selected_id_channel_number]
            selected_id_channels.append(selected_id_channel)
        except:
            ErrorNumber()

    return selected_id_channels

def ChoiceMultUrlMessageDiscord():
    file_message_discord = "./MessageDisc.txt"
    message_discord = []
    message_discord_number = 0

    with open(file_message_discord, 'r') as file_message:
        for line in file_message:
            if not line.strip() or line.isspace():
                continue
            message_discord_number += 1
        
        if message_discord_number == 0:
            print(f"{INFO} No Message Discord in file: {white}{file_message_discord}{red} Please add messages to the file.")
            Continue()
            Reset()
        else:
            print(f"{INFO} {white}{message_discord_number}{red} Message Discord found ({white}{file_message_discord}{red})")
    
    try:
        num_messages = int(input(f"{INPUT} How many messages (max {message_discord_number}) -> {reset}"))
        if num_messages > message_discord_number:
            ErrorNumber()
    except ValueError:
        ErrorNumber()

    message_discord_number = 0
    with open(file_message_discord, 'r') as file_message:
        print()
        print(f"{red}Message Discord ({white}{file_message_discord}{red}):")
        for line in file_message:
            if not line.strip() or line.isspace():
                continue
            
            message_discord_number += 1
            modified_message = line.strip()
            message_discord.append(modified_message)

    number = 0
    selected_messages = []
    print()
    for _ in range(num_messages):
        try:
            number += 1
            selected_message = input(f"{color.RED}{INPUT} Message Number {number}/{num_messages} -> {reset}")
            selected_messages.append(selected_message)
        except:
            ErrorNumber()

    return selected_messages

def ChoiceMultiUrlMessageDiscord():
    file_url_discord = "./UrlDisc.txt"
    url_discord = {}
    url_discord_number = 0

    with open(file_url_discord, 'r') as file_url:
        for line in file_url:
            if not line.strip() or line.isspace():
                continue
            url_discord_number += 1
        
        if url_discord_number == 0:
            print(f"{INFO} No Url Discord in file: {white}{file_url_discord}{red} Please add urls to the file.")
            Continue()
            Reset()
        else:
            print(f"{INFO} {white}{url_discord_number}{red} Url Discord found ({white}{file_url_discord}{red})")
    
    try:
        num_urls = int(input(f"{INPUT} How many url (max {url_discord_number}) -> {reset}"))
        if num_urls > url_discord_number:
            ErrorNumber()
    except ValueError:
        ErrorNumber()

    url_discord_number = 0
    with open(file_url_discord, 'r') as file_url:
        print()
        print(f"{red}Url Discord ({white}{file_url_discord}{red}):")
        for line in file_url:
            if not line.strip() or line.isspace():
                continue
            
            url_discord_number += 1
            modified_url = line.strip()
            url_discord[url_discord_number] = modified_url

    number = 0
    selected_urls = []
    print()
    for _ in range(num_urls):
        try:
            number += 1
            selected_url_number = int(input(f"{color.RED}{INPUT} Url Number {number}/{num_urls} -> {reset}"))
            selected_url = url_discord[selected_url_number]
            selected_urls.append(selected_url)
        except:
            ErrorNumber()

    return selected_urls

def ChoiceMultiUsernameDiscord():
    file_username_discord = "./UsernameDisc.txt"
    username_discord = {}
    username_discord_number = 0

    with open(file_username_discord, 'r') as file_username:
        for line in file_username:
            if not line.strip() or line.isspace():
                continue
            username_discord_number += 1
        
        if username_discord_number == 0:
            print(f"{INFO} No Username Discord in file: {white}{file_username_discord}{red} Please add usernames to the file.")
            Continue()
            Reset()
        else:
            print(f"{INFO} {white}{username_discord_number}{red} Username Discord found ({white}{file_username_discord}{red})")
    
    try:
        num_usernames = int(input(f"{INPUT} How many username (max {username_discord_number}) -> {reset}"))
        if num_usernames > username_discord_number:
            ErrorNumber()
    except ValueError:
        ErrorNumber()

    username_discord_number = 0
    with open(file_username_discord, 'r') as file_username:
        print()
        print(f"{red}Username Discord ({white}{file_username_discord}{red}):")
        for line in file_username:
            if not line.strip() or line.isspace():
                continue
            
            username_discord_number += 1
            modified_username = line.strip()
            username_discord[username_discord_number] = modified_username

    number = 0
    selected_usernames = []
    print()
    for _ in range(num_usernames):
        try:
            number += 1
            selected_username_number = int(input(f"{color.RED}{INPUT} Username Number {number}/{num_usernames} -> {reset}"))
            selected_username = username_discord[selected_username_number]
            selected_usernames.append(selected_username)
        except:
            ErrorNumber()

    return selected_usernames

def ChoiceTime():
    def CheckTime(time_number, time):
        try:
            time += ".0"
            time = float(time)
            print(f"{white}[{red}{time_number}{white}]{red} -> {red}Time: {white}{time}{red}")
        except:
            print(f"{white}[{red}{time_number}{white}]{red} -> {red}Error")

    time = input(f"{color.RED}{INPUT} Input the time (second) -> {reset}")
    time_number = 0

    try:
        time = int(time)
        time = str(time)
    except ValueError:
        pass

    try:
        time = float(time)
    except ValueError:
        ErrorNumber()
    
    time_number += 1
    CheckTime(time_number, time)

    return time

def ChoiceWebhookDiscord():
    file_webhook_discord = "./WebhookDisc.txt"
    webhooks_discord = {}
    webhook_discord_number = 0

    with open(file_webhook_discord, 'r') as file_webhook:
        for line in file_webhook:
            if not line.strip() or line.isspace():
                continue
            webhook_discord_number += 1
        
        if webhook_discord_number == 0:
            print(f"{INFO} No Webhook Discord in file: {white}{file_webhook_discord}{red} Please add webhooks to the file.")
            Continue()
            Reset()
        else:
            print(f"{INFO} {white}{webhook_discord_number}{red} Webhook Discord found ({white}{file_webhook_discord}{red})")
    
    try:
        num_webhooks = int(input(f"{INPUT} How many webhook (max {webhook_discord_number}) -> {reset}"))
        if num_webhooks > webhook_discord_number:
            ErrorNumber()
    except ValueError:
        ErrorNumber()

    webhook_discord_number = 0
    with open(file_webhook_discord, 'r') as file_webhook:
        print()
        print(f"{red}Webhook Discord ({white}{file_webhook_discord}{red}):")
        for line in file_webhook:
            if not line.strip() or line.isspace():
                continue
            
            webhook_discord_number += 1
            modified_webhook = line.strip()
            webhooks_discord[webhook_discord_number] = modified_webhook

    number = 0
    selected_webhooks = []
    print()
    for _ in range(num_webhooks):
        try:
            number += 1
            selected_webhook_number = int(input(f"{color.RED}{INPUT} Webhook Number {number}/{num_webhooks} -> {reset}"))
            selected_webhook = webhooks_discord[selected_webhook_number]
            selected_webhooks.append(selected_webhook)
        except:
            ErrorNumber()

    return selected_webhooks

def ConfirmInput(data):
    confirm = input(f"{color.RED}{INPUT} You want to confirm {data} ({green}yes{white}/{red}no{white}) -> {reset}").lower()
    if confirm == "yes":
        pass
    elif confirm == "no":
        Reset()

def Continue():
    input(f"{color.RED}{INPUT} Press enter to continue...{reset}")

def ErrorNumber():
    print(f"{ERROR} {red}Error! {white}Only number is possible.")
    Continue()
    Reset()

def Reset():
    os.execl(sys.executable, sys.executable, *sys.argv)
