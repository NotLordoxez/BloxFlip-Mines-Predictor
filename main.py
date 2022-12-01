import discord, random

bot = discord.Bot()

@bot.event
async def on_ready():
    print("We have logged in.")

@bot.slash_command()
async def mines(ctx, round_id):
    with open(f"roundid.txt","r") as f:
        x = f.read()

    if round_id in x:
        await ctx.respond("You cannot send the same Round-ID!")
        return
    else:
        with open(f"roundid.txt","a") as f:
            f.write(f"{round_id}\n")

    if len(round_id) != 36:
        await ctx.respond(f"Unable to predict {round_id}.")
        return

    for i in range(300):
        a = random.randint(0,7)
        b = random.randint(8,14)
        c = random.randint(15,25)

    idk = ":bomb:"
    
    #5x5 grid
    grid = [idk,idk,idk,idk,idk,idk,idk,idk,idk,idk,idk,idk,idk,idk,idk,idk,idk,idk,idk,idk,idk,idk,idk,idk,idk]

    grid[int(a)] = ":star:"
    grid[int(b)] = ":star:"
    grid[int(c)] = ":star:"

    #lazy to type just copy it from github lol

    msg = grid[0]+grid[1]+grid[2]+grid[3]+grid[4] + "\n" + grid[5]+grid[6]+grid[7]+grid[8]+grid[9] + "\n" + grid[10]+grid[11]+grid[12]+grid[13]+grid[14] + "\n" + grid[15]+grid[16]+grid[17]+grid[18]+grid[19] + "\n" + grid[20]+grid[21]+grid[22]+grid[23]+grid[24]

    em = discord.Embed(color=0x482957)
    em.add_field(
        name = "Prediction",
        value = msg
    )
    await ctx.respond(embed=em)
        
bot.run("bot token")
