import discord
import random 




async def tictac(self,Interaction,name,button):
    win =0
    done = False
    v=self.board
    h=list(zip(*v))

    #checking columns for a win
    for i in v:
        win = sum(i)
        if win == 3:
            done = True
            x = discord.Embed(title=f"{self.pl2} has LOST!", description=f"{self.pl1} WINS!"  )
            await Interaction.response.edit_message(embed =x ,view = None)
        elif win == -3:
            done = True
            x = discord.Embed(title=f"{self.pl1} has LOST!", description=f"{self.pl2} WINS!"  )
            await Interaction.response.edit_message(embed =x ,view = None)

    #checking rows for a win
    for i in h:
        win = sum(i)
        if win == 3:
            done = True
            x = discord.Embed(title=f"{self.pl2} has LOST!", description=f"{self.pl1} WINS!"  )
            await Interaction.response.edit_message(embed =x ,view = None)
        elif win == -3:
            done = True
            x = discord.Embed(title=f"{self.pl1} has LOST!", description=f"{self.pl2} WINS!"  )
            await Interaction.response.edit_message(embed =x ,view = None)

    #checking diag for a win
    wd1 = self.board[0][0]+self.board[1][1]+self.board[2][2]
    wd2 = self.board[0][2]+self.board[1][1]+self.board[2][0]
    if wd1 ==3 or wd2 ==3:
        done = True
        x = discord.Embed(title=f"{self.pl2} has LOST!", description=f"{self.pl1} WINS!"  )
        await Interaction.response.edit_message(embed =x ,view = None)
    elif wd1 == -3 or wd2 == -3:
        done = True
        x = discord.Embed(title=f"{self.pl1} has LOST!", description=f"{self.pl2} WINS!"  )
        await Interaction.response.edit_message(embed =x ,view = None)

    #else cont game
    if not done:
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

#player surrenders
async def qu(self,Interaction,name,winner):
    x = discord.Embed(title=f"{name} has surrendered!", description=f"{winner} WINS!"  )
    await Interaction.response.edit_message(embed =x ,view = None)

#player(s) vote for tie
async def tie(self,Interaction,name):
    if self.p1T and self.p2T:
        x = discord.Embed(title=f"Both players voted for a TIE", description=f"NO WINNER")
        await Interaction.response.edit_message(embed = x, view = None)
    else:
        await Interaction.response.send_message(f"{name} has voted for a TIE!")
