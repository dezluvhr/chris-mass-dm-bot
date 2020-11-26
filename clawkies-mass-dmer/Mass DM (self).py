import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('') #put message in ''
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run('', bot=False) #put token in ''
