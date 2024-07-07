from Config.Util import *
from Config.config import *
import requests
from datetime import datetime, timezone

try:
    Title("Discord Token Info")

    with open('TokenDisc.txt', 'r') as f:
        token = f.read().strip()

    print(f"{RED}{WAIT} Information Recovery..{RESET}")

    try:
        user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()

        r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})

        if r.status_code == 200:
            status = "Valid"
        else:
            status = "Invalid"

        try:
            username_discord = user['username'] + '#' + user['discriminator']
        except KeyError:
            username_discord = "None"

        try:
            display_name_discord = user.get('global_name', 'None')
        except KeyError:
            display_name_discord = "None"

        try:
            user_id_discord = user['id']
        except KeyError:
            user_id_discord = "None"

        try:
            email_discord = user.get('email', 'None')
        except KeyError:
            email_discord = "None"

        try:
            email_verified_discord = user.get('verified', 'None')
        except KeyError:
            email_verified_discord = "None"

        try:
            phone_discord = user.get('phone', 'None')
        except KeyError:
            phone_discord = "None"

        try:
            mfa_discord = user.get('mfa_enabled', 'None')
        except KeyError:
            mfa_discord = "None"

        try:
            country_discord = user.get('locale', 'None')
        except KeyError:
            country_discord = "None"

        try:
            created_at_discord = datetime.fromtimestamp(((int(user['id']) >> 22) + 1420070400000) / 1000, timezone.utc)
        except KeyError:
            created_at_discord = "None"

        try:
            if user.get('premium_type', 0) == 0:
                nitro_discord = 'False'
            elif user.get('premium_type', 0) == 1:
                nitro_discord = 'Nitro Classic'
            elif user.get('premium_type', 0) == 2:
                nitro_discord = 'Nitro Boosts'
            elif user.get('premium_type', 0) == 3:
                nitro_discord = 'Nitro Basic'
            else:
                nitro_discord = 'False'
        except KeyError:
            nitro_discord = "None"

        try:
            avatar_url_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user.get('avatar', '')}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user.get('avatar', '')}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user.get('avatar', '')}.png"
        except KeyError:
            avatar_url_discord = "None"

        try:
            avatar_discord = user.get('avatar', 'None')
        except KeyError:
            avatar_discord = "None"

        try:
            avatar_decoration_discord = user.get('avatar_decoration_data', 'None')
        except KeyError:
            avatar_decoration_discord = "None"

        try:
            public_flags_discord = user.get('public_flags', 'None')
        except KeyError:
            public_flags_discord = "None"

        try:
            flags_discord = user.get('flags', 'None')
        except KeyError:
            flags_discord = "None"

        try:
            banner_discord = user.get('banner', 'None')
        except KeyError:
            banner_discord = "None"

        try:
            banner_color_discord = user.get('banner_color', 'None')
        except KeyError:
            banner_color_discord = "None"

        try:
            accent_color_discord = user.get("accent_color", 'None')
        except KeyError:
            accent_color_discord = "None"

        try:
            nsfw_discord = user.get('nsfw_allowed', 'None')
        except KeyError:
            nsfw_discord = "None"

        try:
            linked_users_discord = user.get('linked_users', 'None')
            linked_users_discord = ' / '.join(linked_users_discord) if linked_users_discord else "None"
        except KeyError:
            linked_users_discord = "None"

        try:
            bio_discord = "\n" + user.get('bio', 'None') if user.get('bio', 'None') else "None"
        except KeyError:
            bio_discord = "None"

        try:
            authenticator_types_discord = ' / '.join(user.get('authenticator_types', 'None'))
        except KeyError:
            authenticator_types_discord = "None"

        try:
            guilds_response = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': token})
            if guilds_response.status_code == 200:
                guilds = guilds_response.json()
                guild_count = len(guilds)
                owner_guilds = [guild for guild in guilds if guild.get('owner', False)]
                owner_guild_count = f"({len(owner_guilds)})" if owner_guilds else "None"
                owner_guilds_names = "\n" + "\n".join([f"{guild['name']} ({guild['id']})" for guild in owner_guilds]) if owner_guilds else "None"
            else:
                owner_guild_count = "None"
                guild_count = "None"
                owner_guilds_names = "None"
        except Exception as e:
            owner_guild_count = "None"
            guild_count = "None"
            owner_guilds_names = "None"

        try:
            billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token})
            if billing_discord.status_code == 200:
                billing_data = billing_discord.json()
                payment_methods_discord = ' / '.join(['CB' if method.get('type', 0) == 1 else 'Paypal' if method.get('type', 0) == 2 else 'Other' for method in billing_data])
            else:
                payment_methods_discord = "None"
        except Exception as e:
            payment_methods_discord = "None"

        try:
            friends = requests.get('https://discord.com/api/v8/users/@me/relationships', headers={'Authorization': token})
            if friends.status_code == 200:
                friends_data = friends.json()
                friends_discord = '\n' + ' / '.join([f"{friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})" for friend in friends_data]) if friends_data else "None"
            else:
                friends_discord = "None"
        except Exception as e:
            friends_discord = "None"

        try:
            gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token})
            if gift_codes.status_code == 200:
                gift_codes_data = gift_codes.json()
                gift_codes_discord = '\n\n'.join([f"Gift: {gift['promotion']['outbound_title']}\nCode: {gift['code']}" for gift in gift_codes_data]) if gift_codes_data else "None"
            else:
                gift_codes_discord = "None"
        except Exception as e:
            gift_codes_discord = "None"

    except Exception as e:
        print(f"{ERROR} Error when retrieving information: {white}{e}")

    print(f"""
    {white}[{red}+{white}]{red} Status                 : {color.WHITE}{status}{color.RED}
    {white}[{red}+{white}]{red} Token                  : {color.WHITE}{token}{color.RED}
    {white}[{red}+{white}]{red} Username               : {color.WHITE}{username_discord}{color.RED}
    {white}[{red}+{white}]{red} Display Name           : {color.WHITE}{display_name_discord}{color.RED}
    {white}[{red}+{white}]{red} Id                     : {color.WHITE}{user_id_discord}{color.RED}
    {white}[{red}+{white}]{red} Created                : {color.WHITE}{created_at_discord}{color.RED}
    {white}[{red}+{white}]{red} Country                : {color.WHITE}{country_discord}{color.RED}
    {white}[{red}+{white}]{red} Email                  : {color.WHITE}{email_discord}{color.RED}
    {white}[{red}+{white}]{red} Verified               : {color.WHITE}{email_verified_discord}{color.RED}
    {white}[{red}+{white}]{red} Phone                  : {color.WHITE}{phone_discord}{color.RED}
    {white}[{red}+{white}]{red} Nitro                  : {color.WHITE}{nitro_discord}{color.RED}
    {white}[{red}+{white}]{red} Linked Users           : {color.WHITE}{linked_users_discord}{color.RED}
    {white}[{red}+{white}]{red} Avatar Decoration      : {color.WHITE}{avatar_decoration_discord}{color.RED}
    {white}[{red}+{white}]{red} Avatar                 : {color.WHITE}{avatar_discord}{color.RED}
    {white}[{red}+{white}]{red} Avatar URL             : {color.WHITE}{avatar_url_discord}{color.RED}
    {white}[{red}+{white}]{red} Accent Color           : {color.WHITE}{accent_color_discord}{color.RED}
    {white}[{red}+{white}]{red} Banner                 : {color.WHITE}{banner_discord}{color.RED}
    {white}[{red}+{white}]{red} Banner Color           : {color.WHITE}{banner_color_discord}{color.RED}
    {white}[{red}+{white}]{red} Flags                  : {color.WHITE}{flags_discord}{color.RED}
    {white}[{red}+{white}]{red} Public Flags           : {color.WHITE}{public_flags_discord}{color.RED}
    {white}[{red}+{white}]{red} NSFW Allowed           : {color.WHITE}{nsfw_discord}{color.RED}
    {white}[{red}+{white}]{red} Multi-Factor Auth      : {color.WHITE}{mfa_discord}{color.RED}
    {white}[{red}+{white}]{red} Authenticator Types    : {color.WHITE}{authenticator_types_discord}{color.RED}
    {white}[{red}+{white}]{red} Billing                : {color.WHITE}{payment_methods_discord}{color.RED}
    {white}[{red}+{white}]{red} Gift Codes             : {color.WHITE}{gift_codes_discord}{color.RED}
    {white}[{red}+{white}]{red} Guilds                 : {color.WHITE}{guild_count}{color.RED}
    {white}[{red}+{white}]{red} Owner Guilds           : {color.WHITE}{owner_guild_count}{owner_guilds_names}{color.RED}
    {white}[{red}+{white}]{red} Bio                    : {color.WHITE}{bio_discord}{color.RED}
    {white}[{red}+{white}]{red} Friends                : {color.WHITE}{friends_discord}{color.RED}
    """)

    Continue()
    Reset()

except Exception as e:
    Error(e)
