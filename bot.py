from asyncio.windows_events import NULL
from fileinput import lineno
from glob import glob
from lib2to3.pgen2.token import NEWLINE
from msilib.schema import Environment
import random
from pickle import FALSE
import lightbulb
import hikari
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

userTorture = []
roleTorture = []
userCensor = []
roleCensor = []

bot = lightbulb.BotApp(
    token=TOKEN
)

@bot.listen(hikari.StartedEvent)
async def _intializeBot(event):
    _initializeTortureTargets()
    _initializeTortureTargets()

@bot.listen(hikari.EventManagerAware)

@bot.listen(hikari.GuildMessageCreateEvent)
async def copy_msg(event):
    await tortureMsg(event)
    if(not True):
        await exaltMsg(event)
    await censorMsg(event)
    await event.edit('gay')

@bot.command
@lightbulb.command('torture', 'Torture either a user or role')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def group_torture(ctx):
    pass

@bot.command
@lightbulb.command('untorture', 'Remove from torture list')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def group_untorture(ctx):
    pass

@bot.command
@lightbulb.command('exalt', 'Exalt the CCP')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def group_exalt(ctx):
    pass

@bot.command
@lightbulb.command('censor', 'Censors target')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def group_censor(ctx):
    pass

@group_torture.child
@bot.command
@lightbulb.option('user_id', 'User to Torture')
@lightbulb.command('user', 'Choose user')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def tortureUser(ctx):
    #FIX: Rough apply by substring
    userId = ctx.options.user_id
    if(userId[0] == '<' and userId[len(userId)-1] == '>'):
        userId = userId[3:len(userId)-1]
    with open('userTortureReg', 'a') as fileWrite:
        fileWrite.write('{newLine}'.format(newLine='\n' if len(userTorture) != 0 else '') + userId)
    _initializeTortureTargets()
    await ctx.respond(f'<@!{userId}> is now being TORTURED')

@group_torture.child
@bot.command
@lightbulb.option('role_id', 'enter role')
@lightbulb.command('role', 'Choose role')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def tortureRole(ctx):
    ctx.respond('Not finished yet')

@group_untorture.child
@bot.command
@lightbulb.option('user_id', 'User to free')
@lightbulb.command('user', 'Choose user')
@lightbulb.implements(lightbulb.SlashCommand)
async def untortureRole(ctx):
    pass

@group_untorture.child
@bot.command
@lightbulb.option('role_id', 'enter role')
@lightbulb.command('role', 'Choose role')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def untortureRole(ctx):
    pass

@group_exalt.child
@bot.command
@lightbulb.option('user_id', 'enter role')
@lightbulb.command('user', 'Choose user')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def exalt(ctx):
    pass

@group_censor.child
@bot.command
@lightbulb.option('user_id', 'Enter user')
@lightbulb.command('user', 'Choose user')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def censor(ctx):
    #FIX: Rough apply by substring
    userId = ctx.options.user_id
    if(userId[0] == '<' and userId[len(userId)-1] == '>'):
        userId = userId[3:len(userId)-1]
    with open('userCensoredReg', 'a') as fileWrite:
        fileWrite.write('{newLine}'.format(newLine='\n' if len(userTorture) != 0 else '') + userId)
    _initializeCensorTargets()
    await ctx.respond(f'<@!{userId}> is now being CENSORED')
    

@bot.command
@lightbulb.command('stored', 'Test storing info')
@lightbulb.implements(lightbulb.SlashCommand)
async def recall(ctx):
    fileRead = open('botStore', 'r')
    file = fileRead.read()
    print(file)
    print(file[0])
    for line in file:
        await ctx.respond(line)
    await ctx.respond('done') 

@bot.command
@lightbulb.command('yes', 'Says yes')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('yes')

@bot.command
@lightbulb.command('group', 'This is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass

@my_group.child
@lightbulb.command('subcommand', 'This is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('This is a subcommand')

@bot.command()
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.command('add', 'Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

def _initializeTortureTargets():
    userTorture
    roleTorture
    with open('userTortureReg', 'r') as fileRead:
        for user in fileRead:
            if (user.strip() not in userTorture):
                userTorture.append(user.strip())
    with open('roleTortureReg', 'r') as fileRead:
        for role in fileRead:
            if (role.strip() not in roleTorture):
                roleTorture.append(role.strip())
    print(userTorture)
    print(roleTorture)

def _initializeCensorTargets():
    userCensor
    roleCensor
    with open('userCensorReg', 'r') as fileRead:
        for user in fileRead:
            if (user.strip() not in userCensor):
                userCensor.append(user.strip())
    with open('roleCensorReg', 'r') as fileRead:
        for role in fileRead:
            if (role.strip() not in roleCensor):
                roleCensor.append(role.strip())
    print(userCensor)
    print(roleCensor)

async def tortureMsg(eventIn):
    msgSender = eventIn.get_member()
    msgSenderId = str(msgSender.id)
    canTorture = False
    print(userTorture)
    for user in userTorture:
        if(msgSenderId == user):
            canTorture = True
            break
    if(not canTorture):
        for role in roleTorture:
            if(role in msgSender.role_ids):
                canTorture = True
                break
    if(canTorture and not msgSender.is_bot):
        await eventIn.get_channel().send(eventIn.content)

async def exaltMsg(eventIn):
    partySlogansNow = []
    with open('partySlogans', 'r') as fileRead:
        for line in fileRead:
            partySlogansNow.append(line.strip())
    sloganPick = random.randrange(0, len(partySlogansNow)-1)
    await eventIn.get_channel().send(eventIn.content)

async def censorMsg(eventIn):
    msgSender = eventIn.get_member()
    msgSenderId = str(msgSender.id)
    canCensor = False
    for user in userCensor:
        if(msgSenderId == user):
            canCensor = True
    if(canCensor and not msgSender.is_bot):
        eventIn.content = 'gay'


bot.run()