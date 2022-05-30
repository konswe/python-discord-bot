import discord

TOKEN = 'BOT-TOKEN-HERE'

client = discord.Client()

@client.event
async def on_ready():
    print('logged as {0.user}'.format(client))

@client.event
async def on_message(message):  #sends message to user what he wrote
    if message.author != client.user:
        await message.author.send(f'you sent: {message.content}')

client.run(TOKEN)

