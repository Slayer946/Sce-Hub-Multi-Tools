from Settings.Program.Config.Config import *
from Settings.Program.Config.Util import *
import webbrowser
import re
import colorama
import requests

version_tool = 1.0.0
url_config = ""


try:
    colorama.init()
except:
    ErrorModule()

try:
    url = url_config
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        match = re.search(r'version_tool\s*=\s*"([^"]+)"', content)
        if match:
            current_version = match.group(1)
            if current_version != version_tool:
                print(f"{INFO} Please download the new version of the tool! {white}{version_tool}{color.LIGHTYELLOW_EX} -> {white}{current_version}{red}")
                webbrowser.open(github_tool)
                input(f"{INFO} Press Enter to continue using this version -> {color.RESET}")
                popup_version = f"{color.LIGHTYELLOW_EX}Please update the tool: {white}{version_tool}{color.LIGHTYELLOW_EX} -> {white}{current_version}{red}"
            else:
                popup_version = ""
        else:
            popup_version = ""
    else:
        popup_version = ""
except Exception as e:
    popup_version = ""

option_01 = "Website-Tool.py"
option_02 = "Virus-Builder.py"
option_03 = "vulnerability-Sql.py"
option_04 = "Website-Scanner.py"
option_05 = "Illegal-Website.py"
option_06 = "database-recherche.py"
option_07 = "create-dox.py"
option_08 = "Tracker-Dox.py"
option_09 = "Tracker-Username.py"
option_10 = "Email-Info.py"
option_11 = "Info-Number.py"
option_12 = "Info-Ip.py"
option_13 = "Ip-Port-Scanner.py"
option_14 = "Ip-Pinger.py"
option_15 = "Ip-Generator.py"
option_16 = "Encrypted-Password.py"
option_17 = "Password-Decrypted.py"
option_18 = "Your-Ip.py"
option_19 = "Info-Token.py"
option_20 = "Nuke-Token.py"
option_21 = "Join-Server-Token.py"
option_22 = "Leaver-Token-Server.py"
option_23 = "Login-Discord-Token.py"
option_24 = "Id-To-Token-BruteForce.py"
option_25 = "Discord-Server-Raid.py"
option_26 = "Spammer-Discord.py"
option_27 = "Discord-Delete-Friends.py"
option_28 = "Discord-Block-Friends.py"
option_29 = "Mass-Dm.py"
option_30 = "Delete-Dm.py"
option_31 = "Status-Changer.py"
option_32 = "Langage-Changer.py"
option_33 = "House-Changer.py"
option_34 = "Theme-changer.py"
option_35 = "Token-Generator.py"
option_36 = "Bot-Server-Nuke.py"
option_37 = "bot-invite-id.py"
option_38 = "Server-Info.py"
option_39 = "Nitro-Generator.py"
option_40 = "Webhook-Info.py"
option_41 = "Webhook-Delete.py"
option_42 = "Webhook-Spammer.py"
option_43 = "Webhook-Generator.py"
option_44 = "Cookie-Roblox-Login.py"
option_45 = "Cookie-Roblox-Info.py"
option_46 = "User-Info-Roblox.py"
option_47 = "Id-Roblox-Info.py"
option_48 = ""
option_49 = ""
option_50 = ""
option_51 = ""
option_52 = ""
option_53 = ""
option_54 = ""
option_55 = ""
option_56 = ""
option_57 = ""
option_58 = ""
option_59 = ""
option_60 = ""
option_61 = ""
option_62 = ""
option_63 = ""
option_64 = ""

option_previous_txt = option_previous.ljust(30)[:30]
option_next_txt = option_next.ljust(30)[:30]

page1 = f"""{white}[{red}Page n°1{white}]
   {white}[{red}01{white}] {red}->{white} {option_01.ljust(30)[:30].replace("-", " ")} {white}[{red}11{white}] {red}->{white} {option_11.ljust(30)[:30].replace("-", " ")} {white}[{red}21{white}] {red}->{white} {option_21.ljust(30)[:30].replace("-", " ")}
   {white}[{red}02{white}] {red}->{white} {option_02.ljust(30)[:30].replace("-", " ")} {white}[{red}12{white}] {red}->{white} {option_12.ljust(30)[:30].replace("-", " ")} {white}[{red}22{white}] {red}->{white} {option_22.ljust(30)[:30].replace("-", " ")}
   {white}[{red}03{white}] {red}->{white} {option_03.ljust(30)[:30].replace("-", " ")} {white}[{red}13{white}] {red}->{white} {option_13.ljust(30)[:30].replace("-", " ")} {white}[{red}23{white}] {red}->{white} {option_23.ljust(30)[:30].replace("-", " ")}
   {white}[{red}04{white}] {red}->{white} {option_04.ljust(30)[:30].replace("-", " ")} {white}[{red}14{white}] {red}->{white} {option_14.ljust(30)[:30].replace("-", " ")} {white}[{red}24{white}] {red}->{white} {option_24.ljust(30)[:30].replace("-", " ")}
   {white}[{red}05{white}] {red}->{white} {option_05.ljust(30)[:30].replace("-", " ")} {white}[{red}15{white}] {red}->{white} {option_15.ljust(30)[:30].replace("-", " ")} {white}[{red}25{white}] {red}->{white} {option_25.ljust(30)[:30].replace("-", " ")}
   {white}[{red}06{white}] {red}->{white} {option_06.ljust(30)[:30].replace("-", " ")} {white}[{red}16{white}] {red}->{white} {option_16.ljust(30)[:30].replace("-", " ")} {white}[{red}26{white}] {red}->{white} {option_26.ljust(30)[:30].replace("-", " ")}
   {white}[{red}07{white}] {red}->{white} {option_07.ljust(30)[:30].replace("-", " ")} {white}[{red}17{white}] {red}->{white} {option_17.ljust(30)[:30].replace("-", " ")} {white}[{red}27{white}] {red}->{white} {option_27.ljust(30)[:30].replace("-", " ")}
   {white}[{red}08{white}] {red}->{white} {option_08.ljust(30)[:30].replace("-", " ")} {white}[{red}18{white}] {red}->{white} {option_18.ljust(30)[:30].replace("-", " ")} {white}[{red}28{white}] {red}->{white} {option_28.ljust(30)[:30].replace("-", " ")}
   {white}[{red}09{white}] {red}->{white} {option_09.ljust(30)[:30].replace("-", " ")} {white}[{red}19{white}] {red}->{white} {option_19.ljust(30)[:30].replace("-", " ")} {white}[{red}29{white}] {red}->{white} {option_29.ljust(30)[:30].replace("-", " ")}
   {white}[{red}10{white}] {red}->{white} {option_10.ljust(30)[:30].replace("-", " ")} {white}[{red}20{white}] {red}->{white} {option_20.ljust(30)[:30].replace("-", " ")} {white}[{red}30{white}] {red}-> {option_next.ljust(30)[:30]}

{red}┌───({white}{username_pc}@redtiger{red})─[{white}~/1{red}]"""

page2 = f"""{white}[{red}Page n°2{white}]
   {white}[{red}31{white}] {red}-> {option_previous.ljust(30)[:30]} {white}[{red}41{white}] {red}->{white} {option_41.ljust(30)[:30].replace("-", " ")} {white}[{red}61{white}] {red}->{white} {option_61.ljust(30)[:30].replace("-", " ")}
   {white}[{red}32{white}] {red}->{white} {option_32.ljust(30)[:30].replace("-", " ")} {white}[{red}42{white}] {red}->{white} {option_42.ljust(30)[:30].replace("-", " ")} {white}[{red}62{white}] {red}->{white} {option_62.ljust(30)[:30].replace("-", " ")}
   {white}[{red}33{white}] {red}->{white} {option_33.ljust(30)[:30].replace("-", " ")} {white}[{red}43{white}] {red}->{white} {option_43.ljust(30)[:30].replace("-", " ")} {white}[{red}63{white}] {red}->{white} {option_63.ljust(30)[:30].replace("-", " ")}
   {white}[{red}34{white}] {red}->{white} {option_34.ljust(30)[:30].replace("-", " ")} {white}[{red}44{white}] {red}->{white} {option_44.ljust(30)[:30].replace("-", " ")} {white}[{red}64{white}] {red}->{white} {option_64.ljust(30)[:30].replace("-", " ")}
   {white}[{red}35{white}] {red}->{white} {option_35.ljust(30)[:30].replace("-", " ")} {white}[{red}45{white}] {red}->{white} {option_45.ljust(30)[:30].replace("-", " ")} {white}[{red}65{white}] {red}->{white} {option_65.ljust(30)[:30].replace("-", " ")}
   {white}[{red}36{white}] {red}->{white} {option_36.ljust(30)[:30].replace("-", " ")} {white}[{red}46{white}] {red}->{white} {option_46.ljust(30)[:30].replace("-", " ")} {white}[{red}66{white}] {red}->{white} {option_66.ljust(30)[:30].replace("-", " ")}
   {white}[{red}37{white}] {red}->{white} {option_37.ljust(30)[:30].replace("-", " ")} {white}[{red}47{white}] {red}->{white} {option_47.ljust(30)[:30].replace("-", " ")} {white}[{red}67{white}] {red}->{white} {option_67.ljust(30)[:30].replace("-", " ")}
   {white}[{red}38{white}] {red}->{white} {option_38.ljust(30)[:30].replace("-", " ")} {white}[{red}48{white}] {red}->{white} {option_48.ljust(30)[:30].replace("-", " ")} {white}[{red}68{white}] {red}->{white} {option_68.ljust(30)[:30].replace("-", " ")}
   {white}[{red}39{white}] {red}->{white} {option_39.ljust(30)[:30].replace("-", " ")} {white}[{red}49{white}] {red}->{white} {option_49.ljust(30)[:30].replace("-", " ")} {white}[{red}69{white}] {red}->{white} {option_69.ljust(30)[:30].replace("-", " ")}
   {white}[{red}40{white}] {red}->{white} {option_40.ljust(30)[:30].replace("-", " ")} {white}[{red}50{white}] {red}->{white} {option_50.ljust(30)[:30].replace("-", " ")} {white}[{red}70{white}] {red}-> {option_next.ljust(30)[:30]}

{red}┌───({white}{username_pc}@redtiger{red})─[{white}~/2{red}]"""

try:
    try:
        clear()
    except:
        clear_terminal()
    print(f"{red}└─[{white}Menu Principal{red}]")
    if popup_version:
        print(popup_version)
    print(page1)
    option = input(f"{red}└─[{white}Select an option{red}] → {white}")

    if option == "01":
        exec(f"import {option_01}")
    elif option == "02":
        exec(f"import {option_02}")
    elif option == "03":
        exec(f"import {option_03}")
    elif option == "04":
        exec(f"import {option_04}")
    elif option == "05":
        exec(f"import {option_05}")
    elif option == "06":
        exec(f"import {option_06}")
    elif option == "07":
        exec(f"import {option_07}")
    elif option == "08":
        exec(f"import {option_08}")
    elif option == "09":
        exec(f"import {option_09}")
    elif option == "10":
        exec(f"import {option_10}")
    elif option == "11":
        exec(f"import {option_11}")
    elif option == "12":
        exec(f"import {option_12}")
    elif option == "13":
        exec(f"import {option_13}")
    elif option == "14":
        exec(f"import {option_14}")
    elif option == "15":
        exec(f"import {option_15}")
    elif option == "16":
        exec(f"import {option_16}")
    elif option == "17":
        exec(f"import {option_17}")
    elif option == "18":
        exec(f"import {option_18}")
    elif option == "19":
        exec(f"import {option_19}")
    elif option == "20":
        exec(f"import {option_20}")
    elif option == "21":
        exec(f"import {option_21}")
    elif option == "22":
        exec(f"import {option_22}")
    elif option == "23":
        exec(f"import {option_23}")
    elif option == "24":
        exec(f"import {option_24}")
    elif option == "25":
        exec(f"import {option_25}")
    elif option == "26":
        exec(f"import {option_26}")
    elif option == "27":
        exec(f"import {option_27}")
    elif option == "28":
        exec(f"import {option_28}")
    elif option == "29":
        exec(f"import {option_29}")
    elif option == "30":
        exec(f"import {option_30}")
    elif option == "31":
        print(page1)
    elif option == "32":
        exec(f"import {option_32}")
    elif option == "33":
        exec(f"import {option_33}")
    elif option == "34":
        exec(f"import {option_34}")
    elif option == "35":
        exec(f"import {option_35}")
    elif option == "36":
        exec(f"import {option_36}")
    elif option == "37":
        exec(f"import {option_37}")
    elif option == "38":
        exec(f"import {option_38}")
    elif option == "39":
        exec(f"import {option_39}")
    elif option == "40":
        exec(f"import {option_40}")
    elif option == "41":
        exec(f"import {option_41}")
    elif option == "42":
        exec(f"import {option_42}")
    elif option == "43":
        exec(f"import {option_43}")
    elif option == "44":
        exec(f"import {option_44}")
    elif option == "45":
        exec(f"import {option_45}")
    elif option == "46":
        exec(f"import {option_46}")
    elif option == "47":
        exec(f"import {option_47}")
    elif option == "48":
        exec(f"import {option_48}")
    elif option == "49":
        exec(f"import {option_49}")
    elif option == "50":
        exec(f"import {option_50}")
    elif option == "51":
        exec(f"import {option_51}")
    elif option == "52":
        exec(f"import {option_52}")
    elif option == "53":
        exec(f"import {option_53}")
    elif option == "54":
        exec(f"import {option_54}")
    elif option == "page2":
        try:
            clear()
        except:
            clear_terminal()
        print(page2)
        option = input(f"{red}└─[{white}Select an option{red}] → {white}")
        if option == "61":
            exec(f"import {option_61}")
        elif option == "62":
            exec(f"import {option_62}")
        elif option == "63":
            exec(f"import {option_63}")
        elif option == "64":
            exec(f"import {option_64}")
        elif option == "65":
            exec(f"import {option_65}")
        elif option == "66":
            exec(f"import {option_66}")
        elif option == "67":
            exec(f"import {option_67}")
        elif option == "68":
            exec(f"import {option_68}")
        elif option == "69":
            exec(f"import {option_69}")
        elif option == "70":
            print(page2)
        else:
            pass
    else:
        pass
except Exception as e:
    pass
