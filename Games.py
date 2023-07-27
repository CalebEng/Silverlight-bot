import discord
import random 




async def tictac(self,Interaction,name,button):
    if name == self.pl1 and self.turn:
        button.label = "X" 
        button.disabled = True
        button.style = discord.ButtonStyle.blurple
        self.turn = False
        await Interaction.response.edit_message(view = self)
    elif name == self.pl2 and not self.turn:
        button.label = "O"
        button.disabled = True
        button.style = discord.ButtonStyle.blurple
        self.turn = True
        await Interaction.response.edit_message(view = self)
    else:
        await Interaction.response.send_message(f"{name} that is not allowed!")