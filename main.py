import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
list_advice = ['Чаще пользоваться общественным транспортом',
               'Экономить энергию',
               'Сократить потребление мяса',
               'Утилизировать отходы, использовать вторсырье, даже воду',
               'Информировать и обучать']
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

    

@bot.command()
async def eco(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture) 



@bot.command()
async def advice(ctx):
    random_advice = random.choice(list_advice)
    await ctx.send(random_advice)






    



bot.run("")


