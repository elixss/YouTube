# this all is required to run the code. 

# in the video is shown how to work with it.

# i dont show how to create a reddit client.

# do your stuff here

reddit = asyncpraw.Reddit(client_id='client_id',
                        client_secret='client_secret',
                        username='username',             # put your data inside this 
                        password='password',
                        user_agent='agent')


all_subs = []

async def gen_memes():
    subreddit = await reddit.subreddit("memes")         # instead of generating 350 memes every time we use the command, we generate them when the bot starts and just pick one from there
    top = subreddit.top(limit=350)
    async for submission in top:
        all_subs.append(submission)
        
        
@bot.event
async def on_ready():                                       # if you haven't, make a "on_ready" event like this. you need to generate the memes there 
    bot.loop.create_task(status_task())
    print('i am online.')
    await gen_memes()


@bot.command(aliases=["memes"])                 # not we are making the command, which picks one of the pre- generated memes. 
async def meme(ctx):
    random_sub = random.choice(all_subs)
    all_subs.append(random_sub)
    name = random_sub.title                     # we pick some data about the subreddit post here, and the actual meme too. 
    url = random_sub.url 
    likes = random_sub.score 
    comments = random_sub.num_comments
    link = random_sub.permalink

    embed = Embed(title=f'__{name}__', colour=discord.Colour.random(), timestamp=ctx.message.created_at, url=f'https://reddit.com{link}')
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_image(url=url)
    embed.set_footer(text=f'👍{likes} 💬{comments}', icon_url='https://www.vectorico.com/download/social_media/Reddit-Icon.png')        # this is the embed of the meme 
    await ctx.send(embed=embed)


    if len(all_subs) <= 20:           #  if the preloaded memes are less than 20, the bot regenerates new ones.
        await gen_memes()


@bot.command(name='reload-meme')        # we also make a command which reloads the memes manually
async def reload_memes(ctx):
    msg = await ctx.send('Reloading memes ... ')
    await gen_memes()
    await msg.edit(content='Memes reloaded ✅!')
    
# do your stuff here


