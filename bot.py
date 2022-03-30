import lightbulb
import hikari
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = lightbulb.BotApp(
    token=TOKEN,
    default_enabled_guilds=(941897030765264938)
)


@bot.listen(hikari.GuildMessageCreateEvent)
async def print_msg(event):
    msgSender = event.get_member()
    print(event.content)
    print(msgSender.role_ids & msgSender.is_bot() == False)
    #msgSender != 'CCP Bot#6948' FIX
    #if(msgSender == 'Intx_PR#9657'):
      #  await event.get_channel().send(event.content)

@bot.command
@lightbulb.command('torture', 'Sets role or user to torture')
@lightbulb.implements(lightbulb.SlashCommand)
async def torture(ctx):
    guild = ctx.get_guild()
    members = guild.get_members()
    print(members)

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


bot.run()