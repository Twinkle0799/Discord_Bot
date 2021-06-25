#importing discord library
import discord

#connetion to client
client  = discord.Client()

@client.event
async def on_ready():
  print("The bot is online")

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return
  if str(msg.author.id)=="657440181221195788": #only send hello when you send msg
    if str(msg.content).lower()=="hello":
      await msg.channel.send("Hello");

client.run('ODU3NjI0MzkyOTg4MDk4NjMy.YNSS9Q.miEiDGH9olb7_-GhwqtHkEw07CU')