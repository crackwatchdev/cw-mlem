import discord
import configparser
conf = configparser.ConfigParser()
conf.read('./config.ini')
bot = commands.Bot(command_prefix='mlem&')
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    
bot.run(conf.get('bot', 'token'))