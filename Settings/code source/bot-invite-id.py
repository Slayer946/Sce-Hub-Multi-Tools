import webbrowser
from Config.Util import *

def get_bot_id():
    while True:
        try:
            IdBot = int(input(f"\n{red}{INPUT} ID bot -> {reset}"))
            return IdBot
        except ValueError:
            ErrorId()

def get_bot_invite_url(bot_id):
    return f'https://discord.com/oauth2/authorize?client_id={bot_id}&scope=bot&permissions=8'

def main():
    Title("Discord Invite Bot To Id")
    
    try:
        IdBot = get_bot_id()
        URLBot = get_bot_invite_url(IdBot)
        
        print(f"{INFO} URL bot: \"{color.WHITE}{URLBot}{color.RESET}\"")
        
        choice = input(f"{INPUT} Open the Internet ? (y/n) -> {color.RESET}")
        if choice.lower() in ['y', 'yes']:
            webbrowser.open_new_tab(URLBot)
        else:
            Continue()
            Reset()
    
    except Exception as e:
        Error(e)

if __name__ == "__main__":
    main()
