import trelloModule as trllo
import rbxModule as rbx
import discord
from discord.ext import commands
from discord.utils import get
import time
from ro_py import Client
import json

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = "?")
client.remove_command("help")

roblox = Client("53FA4D7611B6341DA7F2C97B2F51709C41EB5038FA4E0FB38F63E011741595D4D75041293018463150CA178EDAEFA84E50C7B1950BBF4F3B3604780610AE846218B0E2CC1DAE1C85332674DE574DF72F9B52DB4F58A9E36FF6407B6F10B8341B83F0E28BCE5D2609D62FD2082F78C2C5309827C23B5D0F8582365B6BF9BC56CA58818DF5CD74B01F3C4FB3D8EB6A64A78381B8C9506C4B60D0CA67F91496130AF1301CFB5041D0CDD153A79369694128034DED91154DCF4EDEF79A59E580D708C737E4DEC7B85D645864ECEDC5D2ADB0EDDA0976E6252E59EA174118A6594B5679E7906E00FDF718C7D2BA2C0E53ED6FF3E834FC4EBA860658333F5C274C16DEA0F7285E4FB9227B00D90AC57E5C738BCAACAB35827B53718785DD86BB722C7542ED1F80E71595C53A29ACDEF53D7D692993A00351153DD9ABDFDB30D405992E4E55DFE5")

@client.event
async def on_ready():
  print("[LOGS] Bot Online")

def get_user(userId):
  user = client.fetch_user(userId)
  return user

def get_guild(guildId):
  guild = client.fetch_guild(guildId)
  return guild

async def update_Roles(member, robloxName):
    rbxUserId = rbx.rbx_getId(robloxName)
    rbxRanking = rbx.rbx_getGroupRoles(rbxUserId)
    CustomerRole = get(guild.roles, id=915942545849208884)

    if rbxRanking == '1 | Customer':
      role = get(guild.roles, id=915942545849208884)
      await member.edit(roles=[role])

    elif rbxRanking == '2 | Premium Customer':
      role = get(guild.roles, id=915942490308223016)
      await member.edit(roles=[role, CustomerRole])

    elif rbxRanking == '3 | Awaiting Training':
      role = get(guild.roles, id=915942452530135054)
      await member.edit(roles=[role, CustomerRole])

    elif rbxRanking == '4 | Barista':
      role = get(guild.roles, id=915942405528768552)
      await member.edit(roles=[role, CustomerRole])
        
    elif rbxRanking == '5 | Waiter/Waitress':
      role = get(guild.roles, id=915942323320401960)
      await member.edit(roles=[role, CustomerRole])
        
    elif rbxRanking == '6 | Head Waiter':
      role = get(guild.roles, id=915942280806944778)
      await member.edit(roles=[role, CustomerRole])
        
    elif rbxRanking == '7 | Line Cook':
      role = get(guild.roles, id=915942257562124299)
      await member.edit(roles=[role, CustomerRole])
      
    elif rbxRanking == '8 | Chef':
      role = get(guild.roles, id=915942211806441483)
      await member.edit(roles=[role, CustomerRole])

    elif rbxRanking == '9 | Head Chef':
      role = get(guild.roles, id=915941914375753760)
      await member.edit(roles=[role, CustomerRole])

    elif rbxRanking == '10 | Executive Chef':
      role = get(guild.roles, id=915941874198523964)
      await member.edit(roles=[role, CustomerRole])
        
    elif rbxRanking == '11 | Trial Moderator':
      role = get(guild.roles, id=915941648477859890)
      await member.edit(roles=[role, CustomerRole])
        
    elif rbxRanking == '12 | Junior Moderator':
      role = get(guild.roles, id=915941608099303500)
      await member.edit(roles=[role, CustomerRole])
        
    elif rbxRanking == '13 | Experienced Moderator':
      role = get(guild.roles, id=915941580731461663)
      await member.edit(roles=[role, CustomerRole])

    elif rbxRanking == '14 | Senior Moderator':
      role = get(guild.roles, id=915941400225382431)
      await member.edit(roles=[role, CustomerRole])

@client.command()
async def verifyUser(ctx, id):
  if ctx.channel.id == 921765750228811876:
    userId = int(trllo.trello_cleanUp(id))
    channel = client.get_channel(917054840390172722)
    rbxUsername = trllo.getRbx_Username(id)
    user = await get_user(806826503013924875)
    rbxUserId = rbx.rbx_getId(rbxUsername)
    global guild
    guild = await get_guild(911988729990770708)
    rbxRanking = rbx.rbx_getGroupRoles(rbxUserId)
    member = await guild.fetch_member(user.id)
    role = get(guild.roles, id=915942545849208884)
    await member.add_roles(role)
    await update_Roles(member, rbxUsername)

    a_dictionary = {str(user.id) : rbxUsername}

    with open("data.json", "r+") as file:
      data = json.load(file)
      data.update(a_dictionary)
      file.seek(0)
      json.dump(data, file)
    
    sendEmbed = discord.Embed(title="**Moon's Restaurant Verification**", description=f"{user.mention} \n Welcome to the Moon's Restaurant!")
    sendEmbed.add_field(name="Roblox Username", value=rbxUsername, inline=True)
    sendEmbed.add_field(name="Discord Username", value=user.name, inline=True)
    sendEmbed.add_field(name="Roblox Group Rank", value=rbxRanking, inline=False)
    await channel.send(embed=sendEmbed)

@client.command()
async def verify(ctx):
  user = ctx.author

  sendEmbed = discord.Embed(title="**Moon's Restaurant Verification**", description="Discord Verify")
  sendEmbed.add_field(name="Step 1:", value='Please enter your Roblox Username:', inline=False)
  await user.send('Starting Verification')
  time.sleep(2)
  await user.send(embed=sendEmbed)
  time.sleep(2)
  rbxUsrname = await client.wait_for('message', timeout=30)
  time.sleep(0.5)
  trllo.trllo_SendCode(rbxUsrname.content, user.name+'#'+ctx.author.discriminator+'*'+str(user.id))


  sendEmbed = discord.Embed(title="Please join this game and complete the Verification.", description="https://www.roblox.com/games/8266167816/Moons-Restaurant-Verification")
  time.sleep(2)
  await user.send(embed=sendEmbed)

@client.event
async def on_message(message):
    # Manually get the invocation context from the message
    ctx = await client.get_context(message)

    # Verify that the context has a command and can be used
    if ctx.valid:
        # Invoke the command using the earlier defined bot/client/command
        await client.invoke(ctx)
  


@client.command()
async def update(ctx, member: discord.Member=None):
  global guild
  guild = ctx.guild
  json_file = open("data.json")
  datafile = json.load(json_file)
  channel = client.get_channel(913860900182695977)

  if member == None:
    user = ctx.author
    userid = user.id
    strUserId = str(userid)
    rbxUsername = datafile[strUserId]
    memberTemp = await guild.fetch_member(user.id)
    await update_Roles(memberTemp, rbxUsername)
    rbxUserId = rbx.rbx_getId(rbxUsername)
    rbxRanking = rbx.rbx_getGroupRoles(rbxUserId)
    sendEmbed = discord.Embed(title="**Moon's Restaurant Verification**", description=f"{user.mention} Roles Updated!")
    sendEmbed.add_field(name="Role(s) updated for: ", value=rbxUsername, inline=True)
    sendEmbed.add_field(name="Added role(s): ", value=rbxRanking, inline=False)
    await ctx.send(embed=sendEmbed)

  else:
    userid = member.id
    strUserId = str(userid)
    rbxUsername = datafile[strUserId]
    await update_Roles(member, rbxUsername)
    rbxUserId = rbx.rbx_getId(rbxUsername)
    rbxRanking = rbx.rbx_getGroupRoles(rbxUserId)
    sendEmbed = discord.Embed(title="**Moon's Restaurant Verification**", description=f"{member.mention} Roles Updated!")
    sendEmbed.add_field(name="Role(s) updated for: ", value=rbxUsername, inline=True)
    sendEmbed.add_field(name="Added role(s): ", value=rbxRanking, inline=False)
    await ctx.send(embed=sendEmbed)

@client.command()
async def shout(ctx, *, shout_text):
    group = await roblox.get_group(12982366)
    await group.shout(shout_text)
    await ctx.send("Your shout has been sent.")

@client.command()
async def setRole(ctx, rbxName, rankId):
  rbxUserId = rbx.rbx_getId(rbxName)
  rbx.set_role(rbxUserId, rankId)
  await ctx.send('User has been ranked!')
  

client.run('OTIwNzQ5ODc3Mjc5OTk4MDYy.Ybo5JQ.bzVyFVz5CuWROBnuICArLZMDXDg')
