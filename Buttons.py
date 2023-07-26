import discord
import Games


class Buttons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="hit",style=discord.ButtonStyle.danger)
    async def hit(self, Interaction, Button: discord.ui.Button):
        name = Interaction.user.display_name
        await Games.testing(Interaction,name) 

    @discord.ui.button(label="me",style=discord.ButtonStyle.success,row=1)
    async def me(self, Interaction, Button:discord.ui.Button):
        name = Interaction.user.display_name
        await Games.testing(Interaction,name)
    
    @discord.ui.button(label="baby",style=discord.ButtonStyle.blurple,row=2)
    async def baby(self, Interaction, Button:discord.ui.Button):
        name = Interaction.user.display_name
        await Games.testing(Interaction,name)