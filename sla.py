@bot.command()
async def embed(ctx):
    embed=discord.Embed(
    title="Limp",
        url="https://twitter.com/Limpu__",
        description="vini macaco",
        color=discord.Color.blue())
    embed.set_author(name="Limp", url="https://twitter.com/Limpu__", icon_url="https://cdn.discordapp.com/avatars/231405874017599488/57e97f53bf790b50177649bd55578300.png?size=4096")

    embed.add_field(name="vini viado", value="vini macaco", inline=True)
    embed.add_field(name="teste", value="teste", inline=False)
    embed.set_footer(text="apo gay")
    await ctx.send(embed=embed)