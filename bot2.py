import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def gen():
    pytania = "+-"
    pytanie = random.choice(pytania)
    return pytanie
@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def pomoc(ctx):
    await ctx.send("Możesz użyć komend: $pytanie,aby sprawdzić się w quizie $odpM/P,aby odpowiedzieć na pytanie.")
    
@bot.command()
async def pytanie(ctx):
    
    pytanie = gen()
    if pytanie == "+":
        odp = "B"
        await ctx.send("Co wrzucamy do żółtego kosza na śmieci?")
        await ctx.send("A - bio odpady")
        await ctx.send("B - plastik")
        await ctx.send("C - zmieszane")
        await ctx.send("Udziel odpowiedzi używając odpowiedzi $odpP A/B/C")
            
    else:
        odp = "A"
        await ctx.send("Co wrzucamy do zielonego kosza na śmieci?")
        await ctx.send("A - szkło")
        await ctx.send("B - plastik")
        await ctx.send("C - zmieszane")
        await ctx.send("Udziel odpowiedzi używając odpowiedzi $odpM A/B/C")
@bot.command()
async def odpP(ctx, odp):
    
    if odp == "B":
        await ctx.send("Odpowiedziałeś poprawnie!")
    else:
        await ctx.send("Nie odpowiedziałeś poprawnie. Poprawna odpowiedź to B!")
    
@bot.command()
async def odpM(ctx, odp):
    
    if odp == "A":
        await ctx.send("Odpowiedziałeś poprawnie!")
    else:
        await ctx.send("Nie odpowiedziałeś poprawnie. Poprawna odpowiedź to A!")


#$help
#$pytanie
#$odpowiedz
bot.run("##############")
