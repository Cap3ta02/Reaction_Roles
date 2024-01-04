import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} online') # il compilatore invia un messaggio online

@bot.event #funzione assegna ruolo
async def on_raw_reaction_add(payload):
    if payload.message_id == None:  # Sostituisci ~None con l'ID del messaggio da controllare
        if payload.emoji.name == '✅':  # Verifica se l'emoji reagita è ✅
            guild = bot.get_guild(payload.guild_id)
            member = await guild.fetch_member(payload.user_id)
            role = discord.utils.get(guild.roles, name='amici')  # Sostituisci con il nome del ruolo da assegnare
        
            if role is not None:  # Verifica se il ruolo esiste nel server
                await member.add_roles(role)
                print(f'Assegnato il ruolo {role.name} a {member.name}')

@bot.event #funzione che rimuove il ruolo in caso di eliminazione dell'emoji
async def on_raw_reaction_remove(payload):
    if payload.message_id == None:  # Sostituisci ~None con l'ID del messaggio da controllare
        if payload.emoji.name == '✅':  # Verifica se l'emoji reagita è ✅
            guild = bot.get_guild(payload.guild_id)
            member = await guild.fetch_member(payload.user_id)
            role = discord.utils.get(guild.roles, name='amici')  # Sostituisci con il nome del ruolo da assegnare
        
            if role is not None:  # Verifica se il ruolo esiste nel server
                await member.remove_roles(role)
                print(f'Rimosso il ruolo {role.name} da {member.name}')



@bot.event
async def on_ready():
    print(f'Bot avviato come {bot.user.name}')


bot.run('token')  # Sostituisci con il token del tuo bot Discord