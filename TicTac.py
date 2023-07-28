import discord
import Games


class TicTac(discord.ui.View):
    def __init__(self,p1,p2):
        super().__init__(timeout=None)
        self.pl1=p1
        self.pl2=p2
        self.p1T=False
        self.p2T=False
        self.turn = True
        self.board = [[0,0,0],[0,0,0,],[0,0,0]]
        

#tic tac toe grid buttons
#------------------------------------------------------------------------------------    
    @discord.ui.button(label="_",style=discord.ButtonStyle.grey)
    async def ul(self, Interaction, button):
        name = Interaction.user.display_name
        
        if name == self.pl1 and self.turn:
            self.board[0][0]+=1
        elif name == self.pl2 and not self.turn:
            self.board[0][0]-=1

        await Games.tictac(self, Interaction, name, button)

    @discord.ui.button(label="_",style=discord.ButtonStyle.grey)
    async def um(self, Interaction, button):
        name = Interaction.user.display_name

        if name == self.pl1 and self.turn:
            self.board[0][1]+=1
        elif name == self.pl2 and not self.turn:
            self.board[0][1]-=1

        await Games.tictac(self,Interaction,name)

    @discord.ui.button(label="_",style=discord.ButtonStyle.grey)
    async def ur(self, Interaction, button):
        name = Interaction.user.display_name

        if name == self.pl1 and self.turn:
            self.board[0][2]+=1
        elif name == self.pl2 and not self.turn:
            self.board[0][2]-=1

        await Games.tictac(self,Interaction,name)
  
    @discord.ui.button(label="_",style=discord.ButtonStyle.grey,row = 1)
    async def ml(self, Interaction, button):
        name = Interaction.user.display_name

        if name == self.pl1 and self.turn:
            self.board[1][0]+=1
        elif name == self.pl2 and not self.turn:
            self.board[1][0]-=1

        await Games.tictac(self,Interaction,name)

    @discord.ui.button(label="_",style=discord.ButtonStyle.grey,row = 1)
    async def mm(self, Interaction, button):
        name = Interaction.user.display_name

        if name == self.pl1 and self.turn:
            self.board[1][1]+=1
        elif name == self.pl2 and not self.turn:
            self.board[1][1]-=1

        await Games.tictac(self,Interaction,name)
   
    @discord.ui.button(label="_",style=discord.ButtonStyle.grey,row=1)
    async def mr(self, Interaction, button):
        name = Interaction.user.display_name

        if name == self.pl1 and self.turn:
            self.board[1][2]+=1
        elif name == self.pl2 and not self.turn:
            self.board[1][2]-=1

        await Games.tictac(self,Interaction,name)
    
    @discord.ui.button(label="_",style=discord.ButtonStyle.grey,row=2)
    async def ll(self, Interaction, button):
        name = Interaction.user.display_name

        if name == self.pl1 and self.turn:
            self.board[2][0]+=1
        elif name == self.pl2 and not self.turn:
            self.board[2][0]-=1

        await Games.tictac(self,Interaction,name)

    @discord.ui.button(label="_",style=discord.ButtonStyle.grey,row = 2)
    async def lm(self, Interaction, button):
        name = Interaction.user.display_name

        if name == self.pl1 and self.turn:
            self.board[2][1]+=1
        elif name == self.pl2 and not self.turn:
            self.board[2][1]-=1

        await Games.tictac(self,Interaction,name)
   
    @discord.ui.button(label="_",style=discord.ButtonStyle.grey,row=2)
    async def lr(self, Interaction, button):
        name = Interaction.user.display_name

        if name == self.pl1 and self.turn:
            self.board[2][2]+=1
        elif name == self.pl2 and not self.turn:
            self.board[2][2]-=1

        await Games.tictac(self,Interaction,name)
#------------------------------------------------------------------------------------  

    #Surrender button
    @discord.ui.button(label="Surrender",style=discord.ButtonStyle.danger,row =3)
    async def qu(self,Interaction, button):
        name = Interaction.user.display_name

        if name == self.pl1:
            await Games.qu(self,Interaction,name,self.pl2)
        elif name == self.pl2:
            await Games.qu(self, Interaction,name,self.pl1)
        else:
            await Interaction.response.send_message(f"{name} that is not allowed!")
    #tie button
    @discord.ui.button(label="TIE", style= discord.ButtonStyle.danger,row = 3)
    async def ti(self,Interaction,button):
        name = Interaction.user.display_name

        if name == self.pl1:
            self.p1T = True
            await Games.tie(self,Interaction,name)
        elif name == self.pl2:
            self.p2T = True
            await Games.tie(self, Interaction,name)
        else:
            await Interaction.response.send_message(f"{name} that is not allowed!")