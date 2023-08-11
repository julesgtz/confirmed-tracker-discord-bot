import lightbulb
import hikari
from Class import Tracker

t = str(input("Enter bot's token : "))
bot = lightbulb.BotApp(token=t)
@bot.command
@lightbulb.option("infos", "email:ordernumber", type=str, required=True)
@lightbulb.command("confirmed", "Select Shop")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    if ctx.guild_id:
         await ctx.respond("Réponse en DM", flags=hikari.MessageFlag.EPHEMERAL)
    embed = hikari.Embed(title="Confirmed Tracker", description=f"Tracking en cours <a:load:1105948968107638805>",
                             color="#000000")
    embed.set_footer("ToolsBot",icon="https://steamuserimages-a.akamaihd.net/ugc/2008072820057289343/6C08F1DA549037DD94593C9CDA0500810D2A51C1/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false")
    if ctx.guild_id:
        msg = await ctx.author.send(embed=embed)
    else:
        msg = await ctx.respond(embed=embed)
    s = {}
    email = []
    ordernumber = []
    infos = ctx.options.infos.split()
    for i in range(len(infos)):
        try:
            e, o = infos[i].split(":")
            email.append(e)
            ordernumber.append(o)
        except:
            if not ctx.guild_id == None:
                await ctx.author.send(f"wrong infos format : {infos[i]}")
            else:
                await ctx.respond(f"wrong infos format : {infos[i]}")

    for index in range(len(email)):
        mail, order, img, link, status, sku = await Tracker(email[index], ordernumber[index]).get_data()
        if status == None and sku == None:
            if ctx.guild_id:
                await ctx.author.send(f"No order at email {mail}:{order}")
            else:
                await ctx.respond(f"No order at email {mail}:{order}")
        else:
            if not sku in s:
                s[sku] = {}
                s[sku]["img"] = img
                s[sku]["status"] = []
                s[sku]["status"].append(status)
                s[sku]["link"] = []
                s[sku]["link"].append(link)
                s[sku]["email"] = []
                s[sku]["email"].append(mail)
                s[sku]["order"] = []
                s[sku]["order"].append(order)
            else:
                s[sku]["status"].append(status)
                s[sku]["link"].append(link)
                s[sku]["email"].append(mail)
                s[sku]["order"].append(order)
    embed = hikari.Embed(title="Confirmed Tracker", description=f"Tracking fini :white_check_mark:",
                         color="#34ff01")
    embed.set_footer("ToolsBot",
                     icon="https://steamuserimages-a.akamaihd.net/ugc/2008072820057289343/6C08F1DA549037DD94593C9CDA0500810D2A51C1/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false")
    await msg.edit(embed=embed)
    for sku in s.items():
        sku = sku[0]
        l = []
        invoices = []
        for index, status in enumerate(s[sku]["status"]):
            if s[sku]["link"][index] != None:
                link = s[sku]["link"][index]
                l.append(f"[{status}]({link})")
            else:
                l.append(status)

        for index, order in enumerate(s[sku]["order"]):
            try:
                ord, invoice = s[sku]["order"][index].split(",")
                invoices.append(f"[{ord}]({invoice})")
            except:
                invoices.append(order)

        embed = hikari.Embed(title="Confirmed Tracker",
                             description=f"Voici ce que j'ai trouver pour le sku **{sku}**", color="#fdfdfd")
        embed.set_thumbnail(s[sku]["img"])
        all_email = "\n".join(s[sku]["email"])
        all_order = "\n".join(invoices)
        all_status = "\n".join(l)
        embed.add_field(name="EMAIL", value=all_email, inline=True)
        embed.add_field(name="ORDER NUMBER", value=all_order, inline=True)
        embed.add_field(name="STATUS", value=all_status, inline=True)
        embed.set_footer("ToolsBot",
                         icon="https://steamuserimages-a.akamaihd.net/ugc/2008072820057289343/6C08F1DA549037DD94593C9CDA0500810D2A51C1/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false")
        if ctx.guild_id:
            await ctx.author.send(embed=embed)
        else:
            await ctx.respond(embed=embed)


bot.run()