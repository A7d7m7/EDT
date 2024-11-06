from playwright.async_api import async_playwright
import discord
from discord.ext import commands

# Initialisation du bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Url de l'emploi du temps
url = "https://docs.google.com/spreadsheets/u/0/d/e/2PACX-1vRWbrMfK5FUlU4we-MLUyZIMMNBw3k9oCNFwDkrxxzfVptemgd4h4Tf66Et7yaQ94j9vPXiQvy3bvZG/pubhtml?pli=1#"

# Repond au bonjour
@bot.command()
async def bonjour(ctx):
    await ctx.send(f"Bonjour {ctx.author} !")

@bot.command()
async def edt_s1(ctx):
    img_name="edt_s1"
    await ctx.send("Je vais vous envoyer l'emploi du temps attendez quelque secondes.")
    try:
        async with async_playwright() as p:
            # Lance Firefox
            browser = await p.chromium.launch(headless=True)  # headless=True pour pas de fenêtre graphique
            page = await browser.new_page()
            
            # Va sur une URL
            url = "https://docs.google.com/spreadsheets/u/0/d/e/2PACX-1vRWbrMfK5FUlU4we-MLUyZIMMNBw3k9oCNFwDkrxxzfVptemgd4h4Tf66Et7yaQ94j9vPXiQvy3bvZG/pubhtml?pli=1#"
            await page.goto(url)
            
            await page.set_viewport_size({"width": 1500, "height": 1350})
            idL3_s1 = 686163362
            await page.evaluate(f'''try {{
                                    switchToSheet({idL3_s1});
                                }}
                                catch (e ) {{
                                
                                }}
                                ''')
            # Prendre une capture d'écran
            await page.screenshot(path=f'{img_name}.png')
            
            # Ferme le navigateur
            await browser.close() 
    except :
        await ctx.send("Une erreur est survenue veuillez contacter un developeur.")
    
    else:
        await ctx.send("Voici l'emploi du temps de la section 1:")
        await ctx.send(file=discord.File(f'{img_name}.png'))

@bot.command()
async def edt_s2(ctx):
    img_name="edt_s2"
    await ctx.send("Je vais vous envoyer l'emploi du temps attendez quelque secondes.")
    try:
        async with async_playwright() as p:
            # Lance Firefox
            browser = await p.chromium.launch(headless=True)  # headless=True pour pas de fenêtre graphique
            page = await browser.new_page()
            
            # Va sur une URL
            url = "https://docs.google.com/spreadsheets/u/0/d/e/2PACX-1vRWbrMfK5FUlU4we-MLUyZIMMNBw3k9oCNFwDkrxxzfVptemgd4h4Tf66Et7yaQ94j9vPXiQvy3bvZG/pubhtml?pli=1#"
            await page.goto(url)
            
            await page.set_viewport_size({"width": 1450, "height": 1350})
            idL3_s2 = 498225454
            await page.evaluate(f'''try {{
                                    switchToSheet({idL3_s2});
                                }}
                                catch (e ) {{
                                
                                }}
                                ''')
            # Prendre une capture d'écran
            await page.screenshot(path=f'{img_name}.png')
            
            # Ferme le navigateur
            await browser.close() 
    except :
        await ctx.send("Une erreur est survenue veuillez contacter un developeur.")
    
    else:
        await ctx.send("Voici l'emploi du temps de la section 2:")
        await ctx.send(file=discord.File(f'{img_name}.png'))

token = 'MTMwMzQ0NzMzODMyNDMzMjU3NA.GHLhzo.CUqz43llYkvDi7BgcYXwsczTEDb3lu5-tw9oKY'
bot.run(token)
