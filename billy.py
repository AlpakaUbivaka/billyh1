import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import utils

import asyncio
import random
import os
from dotenv import load_dotenv

client = discord.Client()

bot = commands.Bot(command_prefix = '>')

load_dotenv()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to САМЫЙ МУЖЫЦКИЙ СЕРВЕР СЕЯ РУСИ!')

@bot.event 
async def on_member_join(ctx, member):
	await ctx.send(f'Wellcome to the club body') #реакция на нового пользователя


@bot.command()
async def sueta(ctx): #вывод фразочек по команде
	jiza = ['Суета...', 'fuck youuuu', 'Я покажу тебе, кто босс этой качалки!', 'Как глубоко ты готов зайти?', 'Сначала я порву свою майку, а потом твоё очко, как видишь, майка уже порвана.', 'ты ошибся дверью, дружочек-пирожочек.']
	await ctx.send(random.choice(jiza))
	
@bot.command()
asynk def trista(ctx):
	await ctx.send('отсоси у тракториста')

@bot.command()
async def fuck_you(ctx):
	embed = discord.Embed(
		title='Oh, fuck you, leather man!',
		url='https://youtu.be/17jixTfd81Y',
	)
	await ctx.send(embed=embed)


@bot.command()
async def secret(ctx):
	embed = discord.Embed(
		title="Великий секрет гачимучи",
		url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
	)
	await ctx.send(embed=embed)


@bot.command(pass_context = True)
async def meme(ctx):
	image = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg']
	await ctx.send(file=discord.File(random.choice(image)))

token = os.getenv('BOT_TOKEN')
token = os.environ.get('BOT_TOKEN')
bot.run(token)
