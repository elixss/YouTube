#do your stuff here



# today i will show how you can use the brandnew discord-select menus with python!

    # we need to import the requirements first


    @commands.command(name='select-test')
    async def select_test(self, ctx):
        await ctx.send("We are testing selects!",
        components=
        [Select(placeholder="Choose what you want to see!",
                            options=[
                                SelectOption(
                                    label="Option 1",
                                    value="option1",
                                    description="See option 1",
                                    emoji="😄" # you can use discord.Parti ... emoji to use a custom one (i dont know what its called)
                                ),
                                SelectOption(
                                    label="Option 2",
                                    value="option2",
                                    description="See option 2",
                                    emoji="😄" # you can use discord.Parti ... emoji to use a custom one (i dont know what its called)
                                ),
                                SelectOption(
                                    label="Option 3",
                                    value="option3",
                                    description="See option 3",
                                    emoji="😄" # you can use discord.Parti ... emoji to use a custom one (i dont know what its called)
                                ),
                            ])]
                            ) 
        e1 = Embed(title="embed1", description="a really exciting embed")
        e2 = Embed(title="embed2", description="a really exciting embed")
        e3 = Embed(title="embed3", description="a really exciting embed")

        while True:
            try: # try except is not required but i would recommend using it
                event = await self.bot.wait_for("select_option", check=None)

                label = event.component[0].label

                if label == "Option 1":
                    await event.respond(
                        type=InteractionType.ChannelMessageWithSource,
                        ephemeral=True, # we dont want to spam someone
                        embed=e1
                    )

                elif label == "Option 2":
                    await event.respond(
                        type=InteractionType.ChannelMessageWithSource,
                        ephemeral=True, # we dont want to spam someone
                        embed=e2
                    )
                elif label == "Option 3":
                    await event.respond(
                        type=InteractionType.ChannelMessageWithSource,
                        ephemeral=False, # we dont want to spam
                        embed=e3 
                    )


            except discord.NotFound:
                print("error.") # since this is bugged, we cant send an error. this error raises every time you use a select, but if this is fixed you can send what ever you want.




        # so thats basically it, lets test it :D
        # i will share this code on my github profile for lazy people who just want  to copy paste the datetime A combination of a date and a time. Attributes: ()
        # the link is https://github.com/elixss_
        # i hoped this video helped you, if it did please like and sub :D
        
        
        
# do your stuff here
