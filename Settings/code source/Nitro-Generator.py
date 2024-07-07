import random
import string
import json
import requests
import threading

# Définition des couleurs pour l'affichage
RED = "\033[91m"
RESET = "\033[0m"
green = "\033[92m"
white = "\033[0;37m"

# Constantes pour les messages de statut
GEN_VALID = "Valid"
GEN_INVALID = "Invalid"
GEN_ERROR = "Error"

# Fonction pour vérifier le webhook
def CheckWebhook(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            print(f"Webhook {url} is valid and reachable.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to verify webhook {url}: {e}")

# Fonction pour vérifier et configurer le webhook
def setup_webhook():
    webhook_enabled = False
    webhook_url = ""
    try:
        webhook = input(f"{RED}\nWebhook ? (y/n) -> {RESET}")
        if webhook.lower() in ['y', 'yes']:
            webhook_enabled = True
            webhook_url = input(f"{RED}Webhook URL -> {RESET}")
            CheckWebhook(webhook_url)  # Assurez-vous que CheckWebhook est correctement défini
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

    return webhook_enabled, webhook_url

# Fonction pour envoyer le webhook
def send_webhook(embed_content, webhook_url):
    try:
        payload = {
            'embeds': [embed_content],
            'username': "username_webhook",  # Remplacez par le nom d'utilisateur du webhook
            'avatar_url': "avatar_webhook"  # Remplacez par l'URL de l'avatar du webhook
        }

        headers = {
            'Content-Type': 'application/json'
        }

        requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    except Exception as e:
        print(f"{RED}Failed to send webhook: {e}{RESET}")

# Fonction pour vérifier le nitro
def nitro_check(webhook_enabled, webhook_url):
    try:
        code_nitro = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        url_nitro = f'https://discord.gift/{code_nitro}'
        response = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code_nitro}?with_application=false&with_subscription_plan=true', timeout=1)
        
        if response.status_code == 200:
            if webhook_enabled:
                embed_content = {
                    'title': 'Nitro Valid !',
                    'description': f"**__Nitro:__**\n```{url_nitro}```",
                    'color': RED,  # Définir la couleur du webhook
                    'footer': {
                        "text": "username_webhook",  # Définir le nom d'utilisateur du webhook
                        "icon_url": "avatar_webhook",  # Définir l'URL de l'avatar du webhook
                    }
                }
                send_webhook(embed_content, webhook_url)
                print(f"{green}[{white}current_time_hour(){green}] {GEN_VALID} Status: {RESET}Valid{green}  | Nitro: {RESET}{url_nitro}{green}{RESET}")
            else:
                print(f"{green}[{white}current_time_hour(){green}] {GEN_VALID} Status: {RESET}Valid{green}  | Nitro: {RESET}{url_nitro}{green}{RESET}")
        else:
            print(f"{RED}[{white}current_time_hour(){RED}] {GEN_INVALID} Status: {RESET}Invalid{RED} | Nitro: {RESET}{url_nitro}{RED}{RESET}")

    except Exception as e:
        print(f"{RED}[{white}current_time_hour(){RED}] {GEN_ERROR} Status: {RESET}Error{RED} | Exception: {RESET}{e}{RED}{RESET}")

# Fonction principale pour gérer les threads
def main():
    try:
        webhook_enabled, webhook_url = setup_webhook()

        try:
            threads_number = int(input(f"Threads Number -> {RESET}"))
        except ValueError:
            print(f"{RED}Error: Invalid input for threads number.{RESET}")
            return

        threads = []
        for _ in range(threads_number):
            t = threading.Thread(target=nitro_check, args=(webhook_enabled, webhook_url))
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()

    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

# Point d'entrée du programme
if __name__ == "__main__":
    main()
