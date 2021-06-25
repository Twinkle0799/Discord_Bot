import os

#this is token you will get from discord developer portal, i just hide it from you so that u don't access my token
my_secret = os.environ['TOKEN']

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
      await msg.channel.send("Hello")
  if str(msg.content).lower() == "hi mr.bot":
      await msg.add_reaction("\U0001F91D")


@client.event
async def on_reaction_add(reaction,user):
  await reaction.message.channel.send(str(user)+" reacted with "+reaction.emoji)



client.run(my_secret)

