import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hi(ctx):
    await ctx.send(f'Привет, у меня есть информация по разложении того или иного придмета! Пропиши команду !help для доп.инфы {bot.user}!')


@bot.command()
async def answer(ctx):
    if ctx.message.content == '!help':
        ctx.send('!plastic = время разложения пластика \n !steklo = время разложения стекла \n !жвачка = время разложения жевачки \n !statya = статья по загрязнению окращающей среды. ')

@bot.command()
async def plastic(ctx):
     await ctx.send('Среднее время разложения пластмассовых изделий на Земле, созданных по разным технологиям, колеблется от 6 месяцев до 700 лет.')

@bot.command()
async def steklo(ctx):
    await ctx.send('Среднее время разложения стеклянных изделий на Земле, созданных по разным технологиям, колеблется от 800 до 1.000 лет.')

@bot.command()
async def жвачка(ctx):
    await ctx.send('Среднее время разложения жвачки на Земле, от 10 лет в странах жарким климатом , а в холодном она сможет пролежать на несколько десятилетий дольше. ')
    
@bot.command()
async def statya(ctx): 
    await ctx.send('https://indicator.ru/label/zagryaznenie-okruzhayushej-sredy = Ссылка от статьи по загрязнению окращающей среды ')


bot.run("ТОКЕН")
