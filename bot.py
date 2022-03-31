from asyncio.windows_events import NULL
from fileinput import lineno
from glob import glob
from lib2to3.pgen2.token import NEWLINE
from msilib.schema import Environment
from pickle import FALSE
import lightbulb
import hikari
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

userTorture = []
roleTorture = []

bot = lightbulb.BotApp(
    token=TOKEN,
    default_enabled_guilds=(941897030765264938)
)

@bot.listen(hikari.StartedEvent)
async def _intializeBot(event):
    _initializeTortureTargets()


@bot.listen(hikari.GuildMessageCreateEvent)
async def copy_msg(event):
    msgSender = event.get_member()
    print(event.content)
    print(msgSender.id)
    print(msgSender.role_ids)
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
    print(canTorture)
    print(msgSender.is_bot)
    print(canTorture and not msgSender.is_bot)
    if(canTorture and not msgSender.is_bot):
        await event.get_channel().send(event.content)
        print('printed')

@bot.command
@lightbulb.command('torture', 'Torture either a user or role')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def group_torture(ctx):
    pass

@group_torture.child
@bot.command
@lightbulb.option('user_id', 'User to Torture')
@lightbulb.command('user', 'Choose user')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def tortureUser(ctx):
    #FIX: Rough apply by substring
    print(ctx.options.user_id)
    userId = ctx.options.user_id
    if(userId[0] == '<' and userId[len(userId)-1] == '>'):
        userId = userId[3:len(userId)-1]
        print(userId)
    with open('userTortureReg', 'a') as fileWrite:
        fileWrite.write('{newLine}'.format(newLine='\n' if len(userTorture) != 0 else str()) + userId)
    _initializeTortureTargets()


    

@group_torture.child
@bot.command
@lightbulb.command('role', 'Choose role')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def tortureRole(ctx):
    ctx.respond('Not finished yet')


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


bot.run()