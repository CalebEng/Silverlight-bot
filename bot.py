import discord
import responses
import TicTac
import Hangman
import random
from discord import app_commands
from discord.ext import commands



async def sendMSG(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        if(response != ''):
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_dis_bot():
    f=open(r'C:\Users\caleb\OneDrive\Documents\Programing\Personal\Python codes\info.txt')
    TOKEN = f.read()
    f.close()
    intents=discord.Intents.all()
    intents.presences = True
    intents.members = True
    client = commands.Bot(command_prefix='sl-',intents=intents)

    

    @client.event
    async def on_ready():
        await client.tree.sync()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name = 'you'))
        print(f'{client.user} has arived!')
    
    @client.event
    async def on_command_error(Interaction, error):
        if isinstance(error, commands.errors.MemberNotFound):
            return await Interaction.send("User not found!")


    #testing non slash profile command
    @client.command(name = 'info')
    async def info(Interaction, member:discord.Member = None):
        
        if member == None:
            member = Interaction.message.author 
    
        name = member.display_name
        pfp = member.display_avatar
        des = ''
        stat = member.status
        activity=None
        playing=None
        streaming = None
        cusAct = None
        listening = None
        watching = None
        badges = member.public_flags.all()

        print(badges)
        
        for act in member.activities:
            if act.type == discord.ActivityType.listening:
                if act.name == "Spotify":
                    listening = act.title
                    
                else: listening = act.name
            if act.type == discord.ActivityType.watching:
                watching = act.name
            if isinstance(act, discord.CustomActivity):
                cusAct = act
            if isinstance(act, discord.Game):
                playing = act
            if isinstance(act, discord.Streaming):
                streaming = act
            if act.type == discord.ActivityType.competing: 
                activity = act.name

        for role in member.roles[1:]:
            des+=f'{role.name}, '
        des=des[:-2]

                
        who = discord.Embed(title=f"{name}", description=stat,colour=discord.Colour.random())
        who.set_author(name="Created by Silverlight",url="https://github.com/CalebEng",icon_url="https://avatars.githubusercontent.com/u/121829627?v=4")
        who.set_thumbnail(url=f"{pfp}")
        
        who.add_field(name= "Custom Status: ", value = cusAct,inline = False)
        
        who.add_field(name = "Playing: ", value = playing, inline=True)
        who.add_field(name = "Streaming: ", value= streaming, inline= True)
        who.add_field(name= "Watching: ",value=watching,inline=True)
        who.add_field(name = "Competing in: ", value = activity, inline=True)
        who.add_field(name= "Listening to: ",value=listening,inline=True)
        
        
        who.add_field(name="Roles: ",value=des,inline= False)

        who.set_footer(text=f"{Interaction.message.author.display_name} wanted this information" )
    
        await Interaction.send(embed= who)

            


    #testing getting information about a song (Spotify)
    @client.command(name = "song")
    async def song(Interaction, member:discord.Member = None):
        if member == None:
            member = Interaction.message.author
        check =0
        
        activ = None
        for act in member.activities:
                if act.type == discord.ActivityType.listening:
                    check+=1
                    if act.name == "Spotify":
                        activ = act
                        songName = activ.title
                        artists = ""
                        pfp = activ.album_cover_url
                        album = activ.album
                        trackurl = activ.track_url

                        for art in activ.artists:
                            artists+=f"{art}, "
                        artists=artists[:-2]
                        emb = discord.Embed(title=f"{member.display_name} is listening to: ", description=songName,colour = discord.Colour.random())
                        emb.set_author(name="Click to listen along!",url=trackurl)
                        emb.set_thumbnail(url=pfp)
                        
                        emb.add_field(name = "Artist(s): ",value = artists,inline = True)
                        emb.add_field(name = "Album: ",value = album, inline = False)

                        emb.set_footer(text = f"{Interaction.message.author.display_name} wanted this information")

                        await Interaction.send(embed = emb)
                    else: 
                        await Interaction.send(f"Song: {act.name}")
        if check ==0:
            await Interaction.send("No song found")

    @client.tree.command(name="complement", description="complement plz")
    async def comp(Interaction, member:discord.Member = None):
        if member == None:
            member = Interaction.user
        emb = discord.Embed(title="Complement from Silverlight", description = f"Ur an idiot {member.display_name} :)")
        await Interaction.response.send_message(embed = emb)    
        
    #testing profile slash command
    @client.tree.command(name = "info", description= "Who are you")
    async def info(Interaction, member:discord.Member = None):
        
        if member == None:
            member = Interaction.user
        
    
        name = member.display_name
        pfp = member.display_avatar
        des = ''
        stat = member.status
        activity=member.activities
        game=None
        streaming = None
        cusAct = None


        for role in member.roles[1:]:
            des+=f'{role.name}, '
        des=des[:-2]

        who = discord.Embed(title=f"{name}", description=stat,colour=discord.Colour.random())
        who.set_author(name="Created by Silverlight",url="https://github.com/CalebEng",icon_url="https://avatars.githubusercontent.com/u/121829627?v=4")
        who.set_thumbnail(url=f"{pfp}")
        
        
        who.add_field(name="Activity: ",value=activity,inline=True)
        
        who.add_field(name = "Gaming: ", value = game, inline=True)
        
        who.add_field(name = "Stream: ", value= streaming, inline= True)
       
        who.add_field(name= "Custom Activity: ", value = cusAct,inline = True)
        
        who.add_field(name="Roles: ",value=des,inline= False)

        who.set_footer(text=f"{Interaction.user.display_name} wanted this information" )

        await Interaction.response.send_message(embed= who)

   
    '''
    Takes in a number representing distance in KM and converts it to CN towers
    '''
    @client.tree.command(name = "cntowerkm", description= "Converts distance in KM to CN Towers pssstt...(This is for u Eunice)")
    async def cnKM(Interaction, km: int):
        name = Interaction.user.display_name
        dis = (km*1000)/553
        who = discord.Embed(title="Distance from KM to CN-Towers",description=f"{km} KM is:\n {dis} CN-Towers",colour=discord.Colour.purple())
        who.set_thumbnail(url="https://w7.pngwing.com/pngs/197/465/png-transparent-cn-tower-coloring-book-drawing-line-art-cn-tower-silhouette-child-black-tower.png")
        who.set_footer(text=f"{name} wanted this information")

        await Interaction.response.send_message(embed = who)

    '''
    Takes in a number representing distance in M and converts it to CN towers
    '''
    @client.tree.command(name = "cntowerm", description="Converts distance in M to CN Towers pssstt...(This is for u Eunice)")
    async def cnM(Interaction, m:int):
        name = Interaction.user.display_name
        dis = (m)/553
        who = discord.Embed(title="Distance from M to CN-Towers",description=f"{m} M is:\n {dis} CN-Towers",colour=discord.Colour.purple())
        who.set_thumbnail(url="https://w7.pngwing.com/pngs/197/465/png-transparent-cn-tower-coloring-book-drawing-line-art-cn-tower-silhouette-child-black-tower.png")
        who.set_footer(text=f"{name} wanted this information")

        await Interaction.response.send_message(embed = who)

    @client.tree.command(name = "coinflip",description="flips a coin")
    async def coinFlip(Interaction):
        name = Interaction.user.display_name
        ans = random.randint(0,1)

        if ans == 0:
            await Interaction.response.send_message("Heads")
        else:
            await Interaction.response.send_message("Tails")

    @client.tree.command(name = "roll",description="rolls a dice of n sides")
    async def roll(Interaction,sides:int):
        ans = random.randint(1,sides)
        await Interaction.response.send_message(ans)

#games---------------------------------------------------------------------------------------------
    @client.tree.command(name="tic-tac-toe")
    async def tictactoe(Interaction,member:discord.Member):
        view = TicTac.TicTac(Interaction.user.display_name,member.display_name)
        emb = discord.Embed(title=f"{Interaction.user.display_name} has challenged {member.display_name} to tic tac toe!" )
        await Interaction.response.send_message(embed=emb,view = view)

    @client.tree.command(name= "hangman",description="There are no word containing z cuz discord wouldn't let me have more than 25 buttons deal wit it")
    async def hangman(Interaction):
        bank = []
        with open (r'C:\Users\caleb\OneDrive\Documents\Programing\Personal\Python codes\Silverlight bot\wordlist.txt', 'r') as f:
            for row in f:
                bank.append(row[:-1])
        temp = random.choice(bank)
        hidden = '#'*len(temp)
        view = Hangman.Hangman(temp,hidden)
        emb = discord.Embed(title = f"Word: {hidden}",description=f'Chances left: 7 | length: {len(hidden)}')
        await Interaction.response.send_message(embed=emb,view=view)
    
   
#--------------------------------------------------------------------------------------------------
    '''
    ON any message inputed in any discord channel
    '''
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 

        username = str(message.author)
        umsg = str(message.content)
        channel = str(message.channel)
        print(f"{username} said: '{umsg}' ({channel})")

        if umsg[0]=='?':
            umsg = umsg[1:]
            await sendMSG(message, umsg, is_private=True)
        else:
            await sendMSG(message, umsg, is_private=False)
            await client.process_commands(message)

        

    client.run(TOKEN)