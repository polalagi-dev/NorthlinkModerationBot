import discord
import os
import termcolor
import datetime
import sys
import time
import requests
from dotenv import load_dotenv

intents=discord.Intents.default()
bot=discord.Client(intents=intents)
tree=discord.app_commands.CommandTree(bot)

load_dotenv()

TOKEN=os.getenv("TOKEN")
GUILD=int(os.getenv("GUILD"))
LOG=int(os.getenv("LOGCHANNEL"))

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

async def modLog(moderator,target,moderationType,reason,extra): # moderationType - 1 ban - 2 warn - 3 kick - 4 unban - 5 clearwarn - 6 mute - 7 unmute
    if moderationType==1:
        embed=discord.Embed(title="Moderator Action Log",description=f"Check details below for more information.",color=0X1FACE3,timestamp=datetime.datetime.now())
        embed=embed.add_field(name="User",value=f"<@{target.id}>")
        embed=embed.add_field(name="Moderator",value=f"<@{moderator.id}>")
        embed=embed.add_field(name="Moderation Type",value="Ban")
        embed=embed.add_field(name="Reason",value=reason)
        embed=embed.add_field(name="Delete Message Days",value=str(extra))
        await bot.get_channel(LOG).send(content="Moderation Action logged.",embed=embed)
    elif moderationType==2:
        embed=discord.Embed(title="Moderator Action Log",description=f"Check details below for more information.",color=0X1FACE3,timestamp=datetime.datetime.now())
        embed=embed.add_field(name="User",value=f"<@{target.id}>")
        embed=embed.add_field(name="Moderator",value=f"<@{moderator.id}>")
        embed=embed.add_field(name="Moderation Type",value="Warn")
        embed=embed.add_field(name="Reason",value=reason)
        await bot.get_channel(LOG).send(content="Moderation Action logged.",embed=embed)
    elif moderationType==3:
        embed=discord.Embed(title="Moderator Action Log",description=f"Check details below for more information.",color=0X1FACE3,timestamp=datetime.datetime.now())
        embed=embed.add_field(name="User",value=f"<@{target.id}>")
        embed=embed.add_field(name="Moderator",value=f"<@{moderator.id}>")
        embed=embed.add_field(name="Moderation Type",value="Kick")
        embed=embed.add_field(name="Reason",value=reason)
        await bot.get_channel(LOG).send(content="Moderation Action logged.",embed=embed)
    elif moderationType==4:
        embed=discord.Embed(title="Moderator Action Log",description=f"Check details below for more information.",color=0X1FACE3,timestamp=datetime.datetime.now())
        embed=embed.add_field(name="User",value=f"<@{target.id}>")
        embed=embed.add_field(name="Moderator",value=f"<@{moderator.id}>")
        embed=embed.add_field(name="Moderation Type",value="Unban")
        embed=embed.add_field(name="Reason",value=reason)
        await bot.get_channel(LOG).send(content="Moderation Action logged.",embed=embed)
    elif moderationType==5:
        embed=discord.Embed(title="Moderator Action Log",description=f"Check details below for more information.",color=0X1FACE3,timestamp=datetime.datetime.now())
        embed=embed.add_field(name="User",value=f"<@{target.id}>")
        embed=embed.add_field(name="Moderator",value=f"<@{moderator.id}>")
        embed=embed.add_field(name="Moderation Type",value="Clear all warns")
        embed=embed.add_field(name="Reason",value=reason)
        await bot.get_channel(LOG).send(content="Moderation Action logged.",embed=embed)
    elif moderationType==6:
        embed=discord.Embed(title="Moderator Action Log",description=f"Check details below for more information.",color=0X1FACE3,timestamp=datetime.datetime.now())
        embed=embed.add_field(name="User",value=f"<@{target.id}>")
        embed=embed.add_field(name="Moderator",value=f"<@{moderator.id}>")
        embed=embed.add_field(name="Moderation Type",value="Mute")
        embed=embed.add_field(name="Reason",value=reason)
        await bot.get_channel(LOG).send(content="Moderation Action logged.",embed=embed)
    elif moderationType==7:
        embed=discord.Embed(title="Moderator Action Log",description=f"Check details below for more information.",color=0X1FACE3,timestamp=datetime.datetime.now())
        embed=embed.add_field(name="User",value=f"<@{target.id}>")
        embed=embed.add_field(name="Moderator",value=f"<@{moderator.id}>")
        embed=embed.add_field(name="Moderation Type",value="Unmute")
        embed=embed.add_field(name="Reason",value=reason)
        await bot.get_channel(LOG).send(content="Moderation Action logged.",embed=embed)

def checkTwitchStatus(account: str):
    content=requests.get(f"https://twitch.tv/{account.lower()}")
    if "isLiveBroadcast" in content:
        return True
    else:
        return False

async def streamingStatus():
    while True:
        result=checkTwitchStatus("AviaPlays")
        if result:
            await bot.change_presence(activity=discord.Streaming(name="AviaPlays", url="https://twitch.tv/AviaPlays"))
        else:
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="commands."), status=discord.Status.idle)

@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD))
    log(f"{bot.user} Connected and synced slash commands.",1)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="commands."), status=discord.Status.idle)
    # TODO - add streamingStatus implementation

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
    await modLog(itr.user,user,3,reason,None)

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
    await modLog(itr.user,user,1,reason,None)

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
    await modLog(itr.user,user,4,reason,None)

@tree.command(name="mute",description="Mutes user",guild=discord.Object(id=GUILD))
async def muteCommandFunction(itr,user: discord.User, reason: str = "No reason given."):
    role=discord.utils.find(lambda g: g.name=="bro got muted", itr.guild.roles)
    ownerrole=discord.utils.find(lambda g: g.name=="Owner", itr.guild.roles)
    if not ownerrole in itr.user.roles:
        await itr.response.send_message(content="Not authorized.",ephemeral=True)
        return
    if role in user.roles:
        await itr.response.send_message(content="User is already muted.",ephemeral=True)
        return
    uid=user.id
    embed=discord.Embed(title="Action Successful",description=f"Action was sucessfully logged and completed.",color=0X1FACE3,timestamp=datetime.datetime.now())
    embed=embed.add_field(name="User",value=f"<@{user.id}>") #User: <@{str(user.id)}>\nModerator: <@{str(itr.user.id)}>\nType: Kick
    embed=embed.add_field(name="Moderator",value=f"<@{itr.user.id}>")
    embed=embed.add_field(name="Moderation Type",value="Mute")
    embed=embed.add_field(name="Reason",value=reason)
    await user.add_roles(role)
    await itr.response.send_message(content=f"Sucessfully muted <@{str(uid)}>.",embed=embed,ephemeral=False)
    await modLog(itr.user,user,6,reason,None)

@tree.command(name="about",description="About the bot",guild=discord.Object(id=GUILD))
async def aboutCommandFunction(itr):
    embed=discord.Embed(title="About",description=f"Here's some info about the bot.",color=0X1FACE3,timestamp=datetime.datetime.now())
    embed=embed.add_field(name="Repository",value=f"[Link](https://github.com/polalagi-dev/NorthlinkModerationBot)") #User: <@{str(user.id)}>\nModerator: <@{str(itr.user.id)}>\nType: Kick
    embed=embed.add_field(name="Developer",value=f"<@690228101208211539>")
    embed=embed.add_field(name="Language",value="Python")
    embed=embed.add_field(name="License",value="Apache 2.0 License - [Link](https://github.com/polalagi-dev/NorthlinkModerationBot/blob/master/LICENSE)")
    await itr.response.send_message(content="",embed=embed,ephemeral=False)

@tree.command(name="unmute",description="Unmutes user",guild=discord.Object(id=GUILD))
async def unmuteCommandFunction(itr,user: discord.User, reason: str = "No reason given."):
    role=discord.utils.find(lambda g: g.name=="bro got muted", itr.guild.roles)
    ownerrole=discord.utils.find(lambda g: g.name=="Owner", itr.guild.roles)
    if not ownerrole in itr.user.roles:
        await itr.response.send_message(content="Not authorized.",ephemeral=True)
        return
    if not role in user.roles:
        await itr.response.send_message(content="User is not muted.",ephemeral=True)
        return
    uid=user.id
    embed=discord.Embed(title="Action Successful",description=f"Action was sucessfully logged and completed.",color=0X1FACE3,timestamp=datetime.datetime.now())
    embed=embed.add_field(name="User",value=f"<@{user.id}>") #User: <@{str(user.id)}>\nModerator: <@{str(itr.user.id)}>\nType: Kick
    embed=embed.add_field(name="Moderator",value=f"<@{itr.user.id}>")
    embed=embed.add_field(name="Moderation Type",value="Unmute")
    embed=embed.add_field(name="Reason",value=reason)
    await user.remove_roles(role)
    await itr.response.send_message(content=f"Sucessfully unmuted <@{str(uid)}>.",embed=embed,ephemeral=False)
    await modLog(itr.user,user,7,reason,None)

# @tree.command(name="openticket",description="Opens a ticket",guild=discord.Object(id=GUILD))
# async def openticketCommandFunction(itr, reason: str = "No reason given."):
#     guild=bot.get_guild(GUILD)
#     if f"ticket-{itr.user}" in guild.channels:
#         await itr.response.send_message(content="You can only have one ticket opened at a time.",ephemeral=True)
#         return
#     guild.create_text_channel(name=f"ticket-{itr.user}",category=None) # TODO add valid category parameter
#     channelId=discord.utils.get(guild.channels, name=f"ticket-{itr.user}")
#     embed=discord.Embed(title="Ticket Created",description=f"Support is gonna respond soon.",color=0X1FACE3,timestamp=datetime.datetime.now())
#     embed=embed.add_field(name="Reason of Ticket Creation",value=reason) #User: <@{str(user.id)}>\nModerator: <@{str(itr.user.id)}>\nType: Kick
#     #await bot.get_guild(GUILD).unban(user=user,reason=reason)
#     await itr.response.send_message(content=f"Ticket created, <#{str(channelId)}>.",ephemeral=True)
#     await guild.get_channel(channel_id=channelId).send_message(content=f"<@{str(itr.user.id)}>",embeds=embed)
#     #await itr.response.send_message(content=f"Sucessfully unbanned <@{str(uid)}>.",embed=embed,ephemeral=False)

# @tree.command(name="closeticket",description="Closes a ticket",guild=discord.Object(id=GUILD))
# async def closeticketCommandFunction(itr, reason: str = "No reason given."):
#     guild=bot.get_guild(GUILD)
#     if f"ticket-{itr.user}" in itr.channel:
#         await itr.response.send_message(content="You can only have one ticket opened at a time.",ephemeral=True)
#         return
#     guild.create_text_channel(name=f"ticket-{itr.user}",category=None) # TODO add valid category parameter
#     channelId=discord.utils.get(guild.channels, name=f"ticket-{itr.user}")
#     embed=discord.Embed(title="Ticket Created",description=f"Support is gonna respond soon.",color=0X1FACE3,timestamp=datetime.datetime.now())
#     embed=embed.add_field(name="Reason of Ticket Creation",value=reason) #User: <@{str(user.id    
# )}>\nModerator: <@{str(itr.user.id)}>\nType: Kick
#     #await bot.get_guild(GUILD).unban(user=user,reason=reason)
#     await itr.response.send_message(content=f"Ticket created, <#{str(channelId)}>.",ephemeral=True)
#     await guild.get_channel(channel_id=channelId).send_message(content=f"<@{str(itr.user.id)}>",embeds=embed)
#     #await itr.response.send_message(content=f"Sucessfully unbanned <@{str(uid)}>.",embed=embed,ephemeral=False)

@bot.event
async def on_member_join(user):
    embed=discord.Embed(title="Welcome to Northlink Ferries!",description=f"Welcome! We hope you enjoy your stay at Northlink Ferries! Also, don't forget to read the rules so you can enjoy the crossings!\n- Ownership Team",color=0X1FACE3,timestamp=datetime.datetime.now())
    embed=embed.set_image("https://cdn.discordapp.com/avatars/1016379795631779890/1092b308fa22df9b456284c05d83be5c.webp")
    await user.send(content="Northlink Ferries",embeds=embed)

script=open("main.py","r")
initial=script.readlines()
script.close()

bot.run(TOKEN)