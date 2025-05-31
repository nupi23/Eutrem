import discord
from bot_logic import gen_pass
from discord.ext import commands
import os #Archivos
import random

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def Hola(ctx):
    await ctx.send("Hola!")
@bot.command()
async def Adios(ctx):
    await ctx.send("\U0001f642")
@bot.command()
async def GG(ctx):
    await ctx.send("Bien jugado")
@bot.command()
async def XD(ctx):
    await ctx.send("X_X")
@bot.command()
async def GC(ctx):
    await ctx.send(gen_pass())
@bot.command()
async def MMA(ctx):
    memesa = os.listdir("Memesa")
    mas = random.choice(memesa)
    with open(f'Memesa/{mas}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)
@bot.command()
async def MMDC(ctx):
    memesd = os.listdir("Memesd")
    mds = random.choice(memesd)
    with open(f'Memesd/{mds}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)
    bot.run("MTM0MDY5ODY0NTc0MTMwNTkyNg.GNOpfP.cDVk1h_hfYe-Dtwwng8I1IEgGxc3Q1kbVeykEc")
