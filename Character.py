import discord
import random 

class Character(discord.ui.View):
     def __init__(self, dm, p):
          self.dm = dm
          self.p = p