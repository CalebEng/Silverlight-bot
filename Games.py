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


#hangman!
async def hangman(self,Interaction,name,button,guess):
    #if the letter is in the word
    if (guess in self.word):
        button.disabled = True
        button.style = discord.ButtonStyle.success
        for i in range(len(self.word)):
            if self.word[i] == guess:
                self.hidden= self.hidden[:i]+guess+self.hidden[i+1:]
        if self.hidden.count('+')==0:
            x = discord.Embed(title=f"Word guessed correctly!",description=f'Word: {self.word}')
            await Interaction.response.edit_message(embed=x,view = None)
        else:
            x = discord.Embed(title = f"Word: {self.hidden}",description=f'Chances left: {7-self.guesses} | length: {len(self.hidden)}')
            await Interaction.response.edit_message(embed=x,view =self)
    #letter not in the word
    else:
        button.disabled = True
        button.style = discord.ButtonStyle.danger
        self.guesses +=1
        if self.guesses ==7:
            x = discord.Embed(title=f"THE MAN HAS BEEN HUNG!")
            await Interaction.response.edit_message(embed = x,view = None)
        else:
            x = discord.Embed(title = f"Word: {self.hidden}",description=f'Chances left: {7-self.guesses} | length: {len(self.hidden)}')
            await Interaction.response.edit_message(embed = x,view = self)
    #if out of guesses
    





#getting the words for hangman
async def getList(self):
    bank = []
    with open (r'C:\Users\caleb\OneDrive\Documents\Programing\Personal\Python codes\Silverlight bot\wordlist.txt', 'r') as f:
        for row in f:
            bank.append(row[:-1])
    temp = random.choice(bank)
    return temp

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
