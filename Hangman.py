import discord
import Games
import random 


class Hangman(discord.ui.View):
    def __init__(self,word,hidden):
            super().__init__(timeout=None)
            self.hidden = hidden
            self.word =word
            self.guesses=0

    @discord.ui.button(label="Q",style=discord.ButtonStyle.grey)
    async def letq(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"q")
    
    @discord.ui.button(label="W",style=discord.ButtonStyle.grey)
    async def letw(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"w")

    @discord.ui.button(label="E",style=discord.ButtonStyle.grey)
    async def lete(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"e")
    
    @discord.ui.button(label="R",style=discord.ButtonStyle.grey)
    async def letr(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"r")

    @discord.ui.button(label="T",style=discord.ButtonStyle.grey)
    async def lett(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"t")

    @discord.ui.button(label="Y",style=discord.ButtonStyle.grey,row=1)
    async def lety(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"y")

    @discord.ui.button(label="U",style=discord.ButtonStyle.grey,row=1)
    async def letu(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"u")

    @discord.ui.button(label="I",style=discord.ButtonStyle.grey,row=1)
    async def leti(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"i")

    @discord.ui.button(label="O",style=discord.ButtonStyle.grey,row=1)
    async def leto(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"o")

    @discord.ui.button(label="P",style=discord.ButtonStyle.grey,row=1)
    async def letp(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"p")

    @discord.ui.button(label="A",style=discord.ButtonStyle.grey,row=2)
    async def leta(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"a")
    
    @discord.ui.button(label="S",style=discord.ButtonStyle.grey,row=2)
    async def lets(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"s")

    @discord.ui.button(label="D",style=discord.ButtonStyle.grey,row=2)
    async def letd(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"d")

    @discord.ui.button(label="F",style=discord.ButtonStyle.grey,row=2)
    async def letf(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"f")
    
    @discord.ui.button(label="G",style=discord.ButtonStyle.grey,row=2)
    async def letg(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"g")

    @discord.ui.button(label="H",style=discord.ButtonStyle.grey,row=3)
    async def leth(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"h")

    @discord.ui.button(label="J",style=discord.ButtonStyle.grey,row=3)
    async def letj(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"j")

    @discord.ui.button(label="K",style=discord.ButtonStyle.grey,row=3)
    async def letk(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"k")

    @discord.ui.button(label="L",style=discord.ButtonStyle.grey,row=3)
    async def letl(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"l")

    @discord.ui.button(label="X",style=discord.ButtonStyle.grey,row=3)
    async def letx(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"x")

    @discord.ui.button(label="C",style=discord.ButtonStyle.grey,row=4)
    async def letc(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"c")

    @discord.ui.button(label="V",style=discord.ButtonStyle.grey,row=4)
    async def letv(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"v")

    @discord.ui.button(label="B",style=discord.ButtonStyle.grey,row=4)
    async def letb(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"q")

    @discord.ui.button(label="N",style=discord.ButtonStyle.grey,row=4)
    async def letn(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"n")

    @discord.ui.button(label="M",style=discord.ButtonStyle.grey,row=4)
    async def letm(self, Interaction, button):
          name = Interaction.user.display_name
          await Games.hangman(self,Interaction,name,button,"m")