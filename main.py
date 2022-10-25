import discord
import os
import termcolor
import datetime
import sys
import time
from dotenv import load_dotenv

intents=discord.Intents.default()
bot=discord.Client(intents=intents)
tree=discord.app_commands.CommandTree(bot)

load_dotenv()

TOKEN=os.getenv("TOKEN")
GUILD=int(os.getenv("GUILD"))

# actionLog=open("action.log","r+w")
# actionLogPrevious=actionLog.readlines()
# actionLog.write(f"{actionLogPrevious}\n-- LOG {str(datetime.datetime.now())} --\n")
# actionLog.close()

def log(t,f):
    #actionLog=open("action.log","w")
    if f==1:
        r=termcolor.colored(str(datetime.datetime.now()),"grey",attrs=["bold"])+" "+termcolor.colored("[SUCCESS] > ","green",attrs=["bold"])+t
        #raw=str(datetime.datetime.now())+" [INFO] > "+t
        print(r)
        #actionLog.write("\n"+raw)
    elif f==2:
        r=termcolor.colored(datetime.datetime.now(),"grey",attrs=["bold"])+" "+termcolor.colored("[ERROR] > ","red",attrs=["bold"])+t
       #raw=str(datetime.datetime.now())+" [INFO] > "+t
        print(r)
        #actionLog.write("\n"+raw)
    elif f==3:
        r=termcolor.colored(datetime.datetime.now(),"grey",attrs=["bold"])+" "+termcolor.colored("[WARNING] > ","yellow",attrs=["bold"])+t
        #raw=str(datetime.datetime.now())+" [INFO] > "+t
        print(r)
        #actionLog.write("\n"+raw)
    elif f==4:
        r=termcolor.colored(str(datetime.datetime.now()),"grey",attrs=["bold"])+" "+termcolor.colored("[INFO] > ","magenta",attrs=["bold"])+t
        #raw=str(datetime.datetime.now())+" [INFO] > "+t
        print(r)
        #actionLog.write("\n"+raw)
    #actionLog.close()

@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD))
    log(f"{bot.user} Connected and synced slash commands.",1)

# @tree.command(name="slash",description="Testing slash commands.",guild=discord.Object(id=GUILD))
# async def slashCommandFunction(itr):
#     embed=discord.Embed(title="Embed",description="Body",color=0xFFF,timestamp=datetime.datetime.now())
#     await itr.response.send_message(embed=embed)
#     log(f"{bot.user} Responded to an interaction by {itr.user}",4) # TODO - check if works - TODO completed, does work

# @tree.command(name="kick",description="Kicks user",guild=discord.Object(id=GUILD))
# async def kickCommandFunction(itr,user: discord.User = None):
#     embed=discord.Embed(title="Embed",description=f"User: {user}",color=0xFFFFF,timestamp=datetime.datetime.now())
#     bot.kick
#     await itr.response.send_message(embed=embed)

@tree.command(name="kick",description="Kicks user",guild=discord.Object(id=GUILD))
async def kickCommandFunction(itr,user: discord.User, reason: str = "No reason given."):
    role=discord.utils.find(lambda g: g.name=="Owner", itr.guild.roles)
    if not role in itr.user.roles:
        await itr.response.send_message(content="Not authorized.",ephemeral=True)
        return
    uid=user.id
    embed=discord.Embed(title="Action Successful",description=f"Action was sucessfully logged and completed.",color=0X1FACE3,timestamp=datetime.datetime.now())
    embed=embed.add_field(name="User",value=f"<@{user.id}>") #User: <@{str(user.id)}>\nModerator: <@{str(itr.user.id)}>\nType: Kick
    embed=embed.add_field(name="Moderator",value=f"<@{itr.user.id}>")
    embed=embed.add_field(name="Moderation Type",value="Kick")
    embed=embed.add_field(name="Reason",value=reason)
    await bot.get_guild(GUILD).kick(user=user,reason=reason)
    await itr.response.send_message(content=f"Sucessfully kicked <@{str(uid)}>.",embed=embed,ephemeral=False)

@tree.command(name="ban",description="Bans user",guild=discord.Object(id=GUILD))
async def banCommandFunction(itr,user: discord.User, reason: str = "No reason given.", deletemessagedays: int = 0):
    role=discord.utils.find(lambda g: g.name=="Owner", itr.guild.roles)
    if not role in itr.user.roles:
        await itr.response.send_message(content="Not authorized.",ephemeral=True)
        return
    uid=user.id
    embed=discord.Embed(title="Action Successful",description=f"Action was sucessfully logged and completed.",color=0X1FACE3,timestamp=datetime.datetime.now())
    embed=embed.add_field(name="User",value=f"<@{user.id}>") #User: <@{str(user.id)}>\nModerator: <@{str(itr.user.id)}>\nType: Kick
    embed=embed.add_field(name="Moderator",value=f"<@{itr.user.id}>")
    embed=embed.add_field(name="Moderation Type",value="Ban")
    embed=embed.add_field(name="Reason",value=reason)
    embed=embed.add_field(name="Delete Message Days",value=str(deletemessagedays))
    await bot.get_guild(GUILD).ban(user=user,reason=reason,delete_message_days=deletemessagedays)
    await itr.response.send_message(content=f"Sucessfully banned <@{str(uid)}>.",embed=embed,ephemeral=False)

@tree.command(name="unban",description="Unbans user",guild=discord.Object(id=GUILD))
async def unbanCommandFunction(itr,user: discord.User, reason: str = "No reason given."):
    role=discord.utils.find(lambda g: g.name=="Owner", itr.guild.roles)
    if not role in itr.user.roles:
        await itr.response.send_message(content="Not authorized.",ephemeral=True)
        return
    uid=user.id
    embed=discord.Embed(title="Action Successful",description=f"Action was sucessfully logged and completed.",color=0X1FACE3,timestamp=datetime.datetime.now())
    embed=embed.add_field(name="User",value=f"<@{user.id}>") #User: <@{str(user.id)}>\nModerator: <@{str(itr.user.id)}>\nType: Kick
    embed=embed.add_field(name="Moderator",value=f"<@{itr.user.id}>")
    embed=embed.add_field(name="Moderation Type",value="Unban")
    embed=embed.add_field(name="Reason",value=reason)
    await bot.get_guild(GUILD).unban(user=user,reason=reason)
    await itr.response.send_message(content=f"Sucessfully unbanned <@{str(uid)}>.",embed=embed,ephemeral=False)

@bot.event
async def on_member_join(user):
    embed=discord.Embed(title="Welcome to Northlink Ferries!",description=f"Welcome! We hope you enjoy your stay at Northlink Ferries! Also, don't forget to read the rules so you\n- Ownership Team",color=0X1FACE3,timestamp=datetime.datetime.now())
    embed=embed.set_image("https://cdn.discordapp.com/avatars/1016379795631779890/1092b308fa22df9b456284c05d83be5c.webp")
    await user.send(content="Northlink Ferries",embeds=embed)

script=open("main.py","r")
initial=script.readlines()
script.close()

bot.run(TOKEN)