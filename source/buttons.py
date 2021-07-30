# do your stuff here


    @commands.command(name='button-test')
    async def button_test(self, ctx):


        one = Button(style=ButtonStyle.blue, label="1", id="embed1") #create buttons
        two = Button(style=ButtonStyle.red, label="2", id="embed2")
        three = Button(style=ButtonStyle.green, label="3", id="embed3")
        four = Button(style=ButtonStyle.grey, label="4", id="embed4")
        invite = Button(style=ButtonStyle.URL, label="Invite here 🤖", url="https://discord.com/oauth2/authorize?client_id=834155102293721138&scope=bot&permissions=306048230") 


        embed1 = Embed(title="This is embed 1", description="for the blue button.", colour=discord.Colour.blue()) # create embeds
        embed2 = Embed(title="This is embed 2.", description="for the red button.", colour=discord.Colour.red())
        embed3 = Embed(title="this is embed 3.", description="For the green button.", colour=discord.Colour.green())
        embed4 = Embed(title="This is embed 4.", description="for the grey button.", colour=discord.Colour.greyple())



        await ctx.send(
            "This is an embed test!",
            components=[                    # attach the buttons
                [one,
                two],
                [three,
                four],
                [invite]
            ]       
        )

                
        buttons = {
                "embed1": embed1,       
                "embed2": embed2,
                "embed3": embed3,
                "embed4": embed4        #assign the buttons to the embeds
        }

        while True:
            event = await self.bot.wait_for("button_click")          
            if event.channel is not ctx.channel:                # wait for the button click, get the button id
                return
            if event.channel == ctx.channel:
                response = buttons.get(event.component.id)     
                if response is None:
                    await event.channel.send(
                        "Something went wrong. Please try it again."            # error
                    )
                if event.channel == ctx.channel:
                    await event.respond(    
                        type=InteractionType.ChannelMessageWithSource,      # send the message
                        embed=response
                    )
                    
  # do your stuff here
