import os
from bs4 import BeautifulSoup
import urllib.request
import discord 
from discord.ext import commands
from keep_alive import keep_alive
from googletrans import Translator
import os

intents = discord.Intents.default()
intents.members = True

description = '''cu

comandos disponiveis: '''
bot = commands.Bot(command_prefix='p!', description=description, intents=intents)


my_secret = os.environ['token']
@bot.event
async def on_ready():
    print(f'logando {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def passiva(ctx, *, poke):
  site = "https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml"
  site = urllib.request.urlopen(site)
  soup = BeautifulSoup(site, 'html5lib')
  translator = Translator()
  if poke == "tsareena" or poke == "sylveon" or poke == "espeon" or poke == "glaceon":
    #ABA DOS POKE COM DUAS PASSIVA

    
    table = soup.find_all('table')[6]
    tr = table.find_all('tr')[0]
    msg = tr.text.strip()
    tr = table.find_all('tr')[1]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[2]
    msg2 = tr.text.strip()
    tr = table.find_all('tr')[3]
    msg3 = tr.text.strip()
    tr = table.find_all('tr')[4]
    msg4 = tr.text.strip()
    
    image = soup.find_all('img')[3]
    imagem = image['src']
    translated_text = translator.translate(msg2, dest="pt")
    translated_text2 =translator.translate(msg4, dest="pt")

    passiva = table.find_all('img')[1]
    passiva2 = passiva['src']
    print(msg, msg1, msg2, msg3)
    embed=discord.Embed(
      title=poke,
          url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml",
        description="Passiva",
        color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", icon_url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=True)
    embed.add_field(name=msg3, value=translated_text2.text, inline=False)
    embed.set_image(url="https://www.serebii.net/"+passiva2)
    embed.set_footer(text="Passivas de: " +poke)

  elif poke == "tyranitar":
    #ABA DO TYRANITAR

    
    table = soup.find_all('table')[6]
    tr = table.find_all('tr')[0]
    msg = tr.text.strip()
    tr = table.find_all('tr')[1]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[2]
    msg2 = tr.text.strip()
    tr = table.find_all('tr')[3]
    msg3 = tr.text.strip()
    tr = table.find_all('tr')[4]
    msg4 = tr.text.strip()
    tr = table.find_all('tr')[5]
    msg5 = tr.text.strip()
    tr = table.find_all('tr')[6]
    msg6 = tr.text.strip()
    
    image = soup.find_all('img')[3]
    imagem = image['src']
    passiva = table.find_all('img')[2]
    passiva2 = passiva['src']
    translated_text = translator.translate(msg2, dest='pt')
    translated_text2 = translator.translate(msg4, dest='pt')
    translated_text3 = translator.translate(msg6, dest='pt')
    print(msg, msg1, msg2, msg3, msg4, msg5, msg6)
    embed=discord.Embed(
      title=poke,
          url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml",
        description="Passiva",
        color=discord.Color.purple())
    embed.set_author(name=poke,   url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml",   icon_url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=True)
    embed.add_field(name=msg3, value=translated_text2.text, inline=False)
    embed.add_field(name=msg5, value=translated_text3.text, inline=False)
    embed.set_image(url="https://www.serebii.net/"+passiva2)
    embed.set_footer(text="Passivas de: " +poke)
    
  elif poke == "duraludon":
    #ABA DO DURALUDON

    
    table = soup.find_all('table')[4]
    tr = table.find_all('tr')[0]
    msg = tr.text.strip()
    tr = table.find_all('tr')[1]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[2]
    msg2 = tr.text.strip()
    
    image = soup.find_all('img')[3]
    imagem = image['src']
    passiva = table.find_all('img')[0]
    passiva2 = passiva['src']
    print(msg, msg1, msg2)
    translated_text = translator.translate(msg2, dest='pt')
    embed=discord.Embed(
      title=poke,
          url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml",
        description="Passiva",
        color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", icon_url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=True)
    embed.set_image(url="https://www.serebii.net/"+passiva2)
    embed.set_footer(text="Passivas de: " +poke)
   
  else:
    #ABA DOS POKEMON MACACO

    
    table = soup.find_all('table')[6]
    tr = table.find_all('tr')[0]
    msg = tr.text.strip()
    tr = table.find_all('tr')[1]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[2]
    msg2 = tr.text.strip()
    
    image = soup.find_all('img')[3]
    imagem = image['src']
    passiva = table.find_all('img')[0]
    passiva2 = passiva['src']
    print(msg, msg1, msg2)
    translated_text = translator.translate(msg2, dest='pt')
    embed=discord.Embed(
      title=poke,
          url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml",
        description="Passiva",
        color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", icon_url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=True)
    embed.set_image(url="https://www.serebii.net/"+passiva2)
    embed.set_footer(text="Passivas de: " +poke)
  
  await ctx.send(embed=embed)
















@bot.command()
async def basico(ctx, *, poke):
  site = "https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml"
  site = urllib.request.urlopen(site)
  soup = BeautifulSoup(site, 'html5lib')
  translator = Translator()
  if poke == "tsareena" or poke == "sylveon" or poke == "espeon" or poke == "glaceon":
    #ABA DOS POKE COM DUAS PASSIVA

    
    table = soup.find_all('table')[6]
    tr = table.find_all('tr')[7]
    msg = tr.text.strip()
    tr = table.find_all('tr')[8]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[9]
    msg2 = tr.text.strip()
      
    image = soup.find_all('img')[3]
    imagem = image['src']
    print(msg, msg1, msg2)
    translated_text = translator.translate(msg2, dest='pt')
    embed=discord.Embed(
        title=poke,
            url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml",
          color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", icon_url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=True)
    embed.set_image(url="https://www.serebii.net/pokemonunite/moves/basic.png")
    embed.set_footer(text="Basico de: " +poke)
  elif poke == "tyranitar":
    #ABA DO TYRANITAR


    
    table = soup.find_all('table')[6]
    tr = table.find_all('tr')[9]
    msg = tr.text.strip()
    tr = table.find_all('tr')[10]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[11]
    msg2 = tr.text.strip()
    translated_text = translator.translate(msg2, dest='pt') 
    image = soup.find_all('img')[3]
    imagem = image['src']
    print(msg, msg1, msg2)
    
    embed=discord.Embed(
        title=poke,
            url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml",
          color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", icon_url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=True)
    embed.set_image(url="https://www.serebii.net/pokemonunite/moves/basic.png")
    embed.set_footer(text="Basico de: " +poke)

    
  elif poke == "duraludon":
    #ABA DO DURALUDON
    table = soup.find_all('table')[4]
    tr = table.find_all('tr')[5]
    msg = tr.text.strip()
    tr = table.find_all('tr')[6]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[7]
    msg2 = tr.text.strip()
      
    image = soup.find_all('img')[3]
    imagem = image['src']
    print(msg, msg1, msg2)
    translated_text = translator.translate(msg2, dest='pt')
    embed=discord.Embed(
        title=poke,
            url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml",
          color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", icon_url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=True)
    embed.set_image(url="https://www.serebii.net/pokemonunite/moves/basic.png")
    embed.set_footer(text="Basico de: " +poke)

    
  else:
    #ABA DOS POKEMON MACACO


    table = soup.find_all('table')[6]
    tr = table.find_all('tr')[5]
    msg = tr.text.strip()
    tr = table.find_all('tr')[6]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[7]
    msg2 = tr.text.strip()
      
    image = soup.find_all('img')[3]
    imagem = image['src']
    translated_text = translator.translate(msg2, dest='pt')
    print(msg, msg1, msg2)
    embed=discord.Embed(
        title=poke,
            url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml",
          color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", icon_url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=True)
    embed.set_image(url="https://www.serebii.net/pokemonunite/moves/basic.png")
    embed.set_footer(text="Basico de: " +poke)
    
  await ctx.send(embed=embed)













@bot.command()
async def move1(ctx, *, poke):
  site = "https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml"
  site = urllib.request.urlopen(site)
  soup = BeautifulSoup(site, 'html5lib')
  translator= Translator()
  
  if poke == "tsareena" or poke == "sylveon" or poke == "espeon" or poke == "glaceon":
  
    table = soup.find_all('table')[6]
    tr = table.find_all('tr')[10]
    msg = tr.text.strip()
    tr = table.find_all('tr')[11]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[12]
    msg2 = tr.text.strip()
    tr = table.find_all('tr')[13]
    msg3 = tr.text.strip()
    tr = table.find_all('tr')[14]
    msg4 = tr.text.strip()
    tr = table.find_all('tr')[15]
    msg5 = tr.text.strip()
    tr = table.find_all('tr')[16]
    msg6 = tr.text.strip()
    
    image = soup.find_all('img')[3]
    imagem = image['src']
    translated_text = translator.translate(msg2, dest='pt')
    translated_text1 = translator.translate(msg4, dest='pt')
    translated_text2 = translator.translate(msg6, dest='pt')
    embed=discord.Embed(
        title=poke,
            url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", description=msg,
          color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml" )
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=True)
    embed.add_field(name=msg3, value=translated_text1.text, inline=False)
    embed.add_field(name=msg5, value=translated_text2.text, inline=True)
    embed.set_footer(text="move1 de: " +poke)
    await ctx.send(embed=embed)

  elif poke == "tyranitar":
  
    table = soup.find_all('table')[6]
    tr = table.find_all('tr')[12]
    msg = tr.text.strip()
    tr = table.find_all('tr')[13]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[14]
    msg2 = tr.text.strip()
    tr = table.find_all('tr')[15]
    msg3 = tr.text.strip()
    tr = table.find_all('tr')[16]
    msg4 = tr.text.strip()
    tr = table.find_all('tr')[17]
    msg5 = tr.text.strip()
    tr = table.find_all('tr')[18]
    msg6 = tr.text.strip()
    
    image = soup.find_all('img')[3]
    imagem = image['src']
    translated_text = translator.translate(msg2, dest='pt')
    translated_text1 = translator.translate(msg4, dest='pt')
    translated_text2 = translator.translate(msg6, dest='pt')
    embed=discord.Embed(
        title=poke,
            url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", description=msg,
          color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml" )
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=True)
    embed.add_field(name=msg3, value=translated_text1.text, inline=False)
    embed.add_field(name=msg5, value=translated_text2.text, inline=True)
    embed.set_footer(text="move1 de: " +poke)
    await ctx.send(embed=embed)
  elif poke == "duraludon":
  
    table = soup.find_all('table')[4]
    tr = table.find_all('tr')[8]
    msg = tr.text.strip()
    tr = table.find_all('tr')[9]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[10]
    msg2 = tr.text.strip()
    tr = table.find_all('tr')[11]
    msg3 = tr.text.strip()
    tr = table.find_all('tr')[12]
    msg4 = tr.text.strip()
    tr = table.find_all('tr')[13]
    msg5 = tr.text.strip()
    tr = table.find_all('tr')[14]
    msg6 = tr.text.strip()
    
    image = soup.find_all('img')[3]
    imagem = image['src']
    translated_text = translator.translate(msg2, dest='pt')
    translated_text1 = translator.translate(msg4, dest='pt')
    translated_text2 = translator.translate(msg6, dest='pt')
    embed=discord.Embed(
        title=poke,
            url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", description=msg,
          color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml" )
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=True)
    embed.add_field(name=msg3, value=translated_text1.text, inline=False)
    embed.add_field(name=msg5, value=translated_text2.text, inline=True)
    embed.set_footer(text="move1 de: " +poke)
    await ctx.send(embed=embed)
  else:
  
    table = soup.find_all('table')[6]
    tr = table.find_all('tr')[8]
    msg = tr.text.strip()
    tr = table.find_all('tr')[9]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[10]
    msg2 = tr.text.strip()
    tr = table.find_all('tr')[11]
    msg3 = tr.text.strip()
    tr = table.find_all('tr')[12]
    msg4 = tr.text.strip()
    tr = table.find_all('tr')[13]
    msg5 = tr.text.strip()
    tr = table.find_all('tr')[14]
    msg6 = tr.text.strip()
    
    image = soup.find_all('img')[3]
    imagem = image['src']
    translated_text = translator.translate(msg2, dest='pt')
    translated_text1 = translator.translate(msg4, dest='pt')
    translated_text2 = translator.translate(msg6, dest='pt')
    embed=discord.Embed(
        title=poke,
            url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", description=msg,
          color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml" )
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=True)
    embed.add_field(name=msg3, value=translated_text1.text, inline=False)
    embed.add_field(name=msg5, value=translated_text2.text, inline=True)
    embed.set_footer(text="move1 de: " +poke)
    await ctx.send(embed=embed)














@bot.command()
async def move2(ctx, *, poke):
  site = "https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml"
  site = urllib.request.urlopen(site)
  soup = BeautifulSoup(site, 'html5lib')
  translator= Translator()
  
  if poke == "tsareena" or poke == "sylveon" or poke == "espeon" or poke == "glaceon":
  
    table = soup.find_all('table')[6]
    tr = table.find_all('tr')[17]
    msg = tr.text.strip()
    tr = table.find_all('tr')[18]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[19]
    msg2 = tr.text.strip()
    tr = table.find_all('tr')[20]
    msg3 = tr.text.strip()
    tr = table.find_all('tr')[21]
    msg4 = tr.text.strip()
    tr = table.find_all('tr')[22]
    msg5 = tr.text.strip()
    tr = table.find_all('tr')[23]
    msg6 = tr.text.strip()
    
    image = soup.find_all('img')[3]
    imagem = image['src']
    translated_text = translator.translate(msg2, dest='pt')
    translated_text1 = translator.translate(msg4, dest='pt')
    translated_text2 = translator.translate(msg6, dest='pt')
    embed=discord.Embed(
        title=poke,
            url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", description=msg,
          color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml" )
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=True)
    embed.add_field(name=msg3, value=translated_text1.text, inline=False)
    embed.add_field(name=msg5, value=translated_text2.text, inline=True)
    embed.set_footer(text="move2 de: " +poke)
    await ctx.send(embed=embed)

  elif poke == "tyranitar":
  
    table = soup.find_all('table')[6]
    tr = table.find_all('tr')[19]
    msg = tr.text.strip()
    tr = table.find_all('tr')[20]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[21]
    msg2 = tr.text.strip()
    tr = table.find_all('tr')[22]
    msg3 = tr.text.strip()
    tr = table.find_all('tr')[23]
    msg4 = tr.text.strip()
    tr = table.find_all('tr')[24]
    msg5 = tr.text.strip()
    tr = table.find_all('tr')[25]
    msg6 = tr.text.strip()
    print(msg4, msg6)
    
    image = soup.find_all('img')[3]
    imagem = image['src']
    translated_text = translator.translate(msg2, dest='pt')
    translated_text3 = translator.translate(msg4, dest='pt')
    translated_text2 = translator.translate(msg6, dest='pt')
    embed=discord.Embed(
        title=poke,
            url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", description=msg,
          color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml" )
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=False)
    embed.add_field(name=msg3, value=msg4, inline=False)
    embed.add_field(name=msg5, value=translated_text2.text, inline=False)
    embed.set_footer(text="move2 de: " +poke)
    await ctx.send('```' +translated_text3.text +'```')
    await ctx.send(embed=embed)    


  elif poke == "duraludon":
  
    table = soup.find_all('table')[4]
    tr = table.find_all('tr')[15]
    msg = tr.text.strip()
    tr = table.find_all('tr')[16]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[17]
    msg2 = tr.text.strip()
    tr = table.find_all('tr')[18]
    msg3 = tr.text.strip()
    tr = table.find_all('tr')[19]
    msg4 = tr.text.strip()
    tr = table.find_all('tr')[20]
    msg5 = tr.text.strip()
    tr = table.find_all('tr')[21]
    msg6 = tr.text.strip()
    
    image = soup.find_all('img')[3]
    imagem = image['src']
    translated_text = translator.translate(msg2, dest='pt')
    translated_text1 = translator.translate(msg4, dest='pt')
    translated_text2 = translator.translate(msg6, dest='pt')
    embed=discord.Embed(
        title=poke,
            url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", description=msg,
          color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml" )
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=True)
    embed.add_field(name=msg3, value=translated_text1.text, inline=False)
    embed.add_field(name=msg5, value=translated_text2.text, inline=True)
    embed.set_footer(text="move2 de: " +poke)
    await ctx.send(embed=embed)
  else:
  
    table = soup.find_all('table')[6]
    tr = table.find_all('tr')[15]
    msg = tr.text.strip()
    tr = table.find_all('tr')[16]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[17]
    msg2 = tr.text.strip()
    tr = table.find_all('tr')[18]
    msg3 = tr.text.strip()
    tr = table.find_all('tr')[19]
    msg4 = tr.text.strip()
    tr = table.find_all('tr')[20]
    msg5 = tr.text.strip()
    tr = table.find_all('tr')[21]
    msg6 = tr.text.strip()
    
    image = soup.find_all('img')[3]
    imagem = image['src']
    translated_text = translator.translate(msg2, dest='pt')
    translated_text1 = translator.translate(msg4, dest='pt')
    translated_text2 = translator.translate(msg6, dest='pt')
    embed=discord.Embed(
        title=poke,
            url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", description=msg,
          color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml" )
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=True)
    embed.add_field(name=msg3, value=translated_text1.text, inline=False)
    embed.add_field(name=msg5, value=translated_text2.text, inline=True)
    embed.set_footer(text="move2 de: " +poke)
    await ctx.send(embed=embed)











@bot.command()
async def ult(ctx, *, poke):
  site = "https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml"
  site = urllib.request.urlopen(site)
  soup = BeautifulSoup(site, 'html5lib')
  translator= Translator()
  
  if poke == "tsareena" or poke == "sylveon" or poke == "espeon" or poke == "glaceon":
  
    table = soup.find_all('table')[6]
    tr = table.find_all('tr')[24]
    msg = tr.text.strip()
    tr = table.find_all('tr')[25]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[26]
    msg2 = tr.text.strip()
    image = soup.find_all('img')[3]
    imagem = image['src']
    translated_text = translator.translate(msg2, dest='pt')
    embed=discord.Embed(
        title=poke,
            url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", description=msg,
          color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml" )
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=True)
    embed.set_footer(text="Ult de: " +poke)
    await ctx.send(embed=embed)

  elif poke == "tyranitar":
  
    table = soup.find_all('table')[6]
    tr = table.find_all('tr')[26]
    msg = tr.text.strip()
    tr = table.find_all('tr')[27]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[28]
    msg2 = tr.text.strip()
  
    
    image = soup.find_all('img')[3]
    imagem = image['src']
    translated_text = translator.translate(msg2, dest='pt')
    embed=discord.Embed(
        title=poke,
            url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", description=msg,
          color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml" )
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=False)
    embed.set_footer(text="Ult de: " +poke)
    await ctx.send(embed=embed)    


  elif poke == "duraludon":
  
    table = soup.find_all('table')[4]
    tr = table.find_all('tr')[22]
    msg = tr.text.strip()
    tr = table.find_all('tr')[23]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[24]
    msg2 = tr.text.strip()

    image = soup.find_all('img')[3]
    imagem = image['src']
    translated_text = translator.translate(msg2, dest='pt')
    embed=discord.Embed(
        title=poke,
            url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", description=msg,
          color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml" )
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=True)
    embed.set_footer(text="Ult de: " +poke)
    await ctx.send(embed=embed)
  else:
  
    table = soup.find_all('table')[6]
    tr = table.find_all('tr')[22]
    msg = tr.text.strip()
    tr = table.find_all('tr')[23]
    msg1 = tr.text.strip()
    tr = table.find_all('tr')[24]
    msg2 = tr.text.strip()
    
    image = soup.find_all('img')[3]
    imagem = image['src']
    translated_text = translator.translate(msg2, dest='pt')
    embed=discord.Embed(
        title=poke,
            url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml", description=msg,
          color=discord.Color.purple())
    embed.set_author(name=poke, url="https://www.serebii.net/pokemonunite/pokemon/"+poke+".shtml" )
    embed.set_thumbnail(url="https://www.serebii.net/pokemonunite/pokemon/"+imagem)
    embed.add_field(name=msg1, value=translated_text.text, inline=True)
    embed.set_footer(text="Ult de: " +poke)
    await ctx.send(embed=embed)


keep_alive()
bot.run(my_secret)






