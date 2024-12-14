import discord
from discord.ext import commands #for commands
from discord import app_commands #for slash commands
import asyncio

GUILD_ID = discord.Object(id="") 
class Client(commands.Bot):
    async def on_ready(self): #async function
        print(f'Logged on as {self.user}.')

        try:
            guild = discord.Object(id=)
            synced = await self.tree.sync(guild= guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')

        except Exception as e:
            print(f'Failed to sync commands: {e}')
   
   
    async def on_message(self, message):
        if message.author == self.user: #we dont want infinite loops
            return
        
        if message.content.startswith('hello'): #bot will reply if the message starts with hello
             await message.channel.send(f'Yo man {message.author.mention}') #pauses the execution of the on_message coroutine until the message is sent.

        if message.content == 'shasin':
            # Loop to mention the user repeatedly
          while True:
             await message.channel.send("<@{}>".format(774512861950640131) + ' muji khai')#mention specfic user with id
             await asyncio.sleep(1)

intents = discord.Intents.default()
intents.message_content = True
Client = Client(command_prefix ="!",intents=intents)


@Client.tree.command(name="pinggaud", description="Ping Gaud", guild= GUILD_ID)

async def ping(interaction: discord.Interaction):
     await interaction.response.send_message("<@{}>".format(530675632741285898))

@Client.tree.command(name="pingshasin", description="Ping Shasin", guild= GUILD_ID)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("<@{}>".format(774512861950640131))

@Client.tree.command(name="pingozaru", description="Ping Ozaru", guild= GUILD_ID)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("<@{}>".format(704346583143153797))


Client.run('') #insert your token here