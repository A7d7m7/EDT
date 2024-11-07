import discord
from discord.ext import commands
from urllib.parse import urlencode
from urllib.request import urlretrieve

# Initialisation du bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Url de l'emploi du temps
url = "https://docs.google.com/spreadsheets/u/0/d/e/2PACX-1vRWbrMfK5FUlU4we-MLUyZIMMNBw3k9oCNFwDkrxxzfVptemgd4h4Tf66Et7yaQ94j9vPXiQvy3bvZG/pubhtml?pli=1#"

# Fonction de l'emploi du temps
@bot.command()
async def edt_s1(ctx):
        await ctx.send("Je vais vous envoyer l'emploi du temps attendez quelque secondes.")
        l3 = dict( 
                width=1500,
                height=1350,
                code_onglet=686163362
            )            
        
        image_name="screenshot.jpg"

        params = urlencode(
                dict(
                            access_key="2b3c5f9a3730466fa222158a7e48576b",
                            url="https://docs.google.com/spreadsheets/u/0/d/e/2PACX-1vRWbrMfK5FUlU4we-MLUyZIMMNBw3k9oCNFwDkrxxzfVptemgd4h4Tf66Et7yaQ94j9vPXiQvy3bvZG/pubhtml?pli=1#",
                            width=l3['width'],
                            height=l3['height'],
                            js=f"switchToSheet({l3['code_onglet']})"
                        )
            )
        urlretrieve("https://api.apiflash.com/v1/urltoimage?wait_until=page_loaded&" + params, image_name)

        await ctx.send("Voici l'emploi du temps:")
        await ctx.send(file=discord.File(f'{image_name}'))

@bot.command()
async def edt_s2(ctx):
        await ctx.send("Je vais vous envoyer l'emploi du temps attendez quelque secondes.")
        l3 = dict( 
                width=1450,
                height=1350,
                code_onglet=498225454
            )
        
        image_name="screenshot.jpg"

        params = urlencode(
                dict(
                            access_key="2b3c5f9a3730466fa222158a7e48576b",
                            url="https://docs.google.com/spreadsheets/u/0/d/e/2PACX-1vRWbrMfK5FUlU4we-MLUyZIMMNBw3k9oCNFwDkrxxzfVptemgd4h4Tf66Et7yaQ94j9vPXiQvy3bvZG/pubhtml?pli=1#",
                            width=l3['width'],
                            height=l3['height'],
                            js=f"switchToSheet({l3['code_onglet']})"
                        )
            )
        urlretrieve("https://api.apiflash.com/v1/urltoimage?wait_until=page_loaded&" + params, image_name)

        await ctx.send("Voici l'emploi du temps:")
        await ctx.send(file=discord.File(f'{image_name}'))


token = 'MTMwMzQ0NzMzODMyNDMzMjU3NA.GHLhzo.CUqz43llYkvDi7BgcYXwsczTEDb3lu5-tw9oKY'
bot.run(token)