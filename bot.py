import discord
import Character
import responses
import TicTac
import Hangman
import random
import Poet
import Player
from discord import app_commands
from discord.ext import commands

chars=[Player.player(0,0,0,0,0,0,0,0,0,0,0,0)]

async def sendMSG(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        if(response != ''):
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_dis_bot():
    f=open(r'C:\Users\caleb\Programing\Personal\Python codes\info.txt')
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
        badgeStr = ""

        for i in badges:
            badgeStr+=f"{str(i)[10:].replace('_',' ')}, "
            
        badgeStr=badgeStr[:-2]
        
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
        who.add_field(name= "Badges: ",value = badgeStr,inline = False)
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

    @client.tree.command(name= "hangman",description="There are no words containing z cuz discord wouldn't let me have more than 25 buttons, deal wit it")
    async def hangman(Interaction):
        bank = []
        with open (r'C:\Users\caleb\Programing\Personal\Python codes\Silverlight bot\wordlist.txt', 'r') as f:
            for row in f:
                bank.append(row[:-1])
        temp = random.choice(bank)
        hidden = '#'*len(temp)
        view = Hangman.Hangman(temp,hidden)
        emb = discord.Embed(title = f"Word: {hidden}",description=f'Chances left: 7 | length: {len(hidden)}')
        await Interaction.response.send_message(embed=emb,view=view)
    

    @client.tree.command(name ="dnd",description="Create characters")
    async def dnd(Interaction,players:int):
        with open(r'characters.txt','r') as f:
                stats =0
                num=0
                for row in f:
                    temp = row.split()
                    if stats==12:
                        chars.append(Player.player(0,0,0,0,0,0,0,0,0,0,0,0))
                        stats =0
                        num+=1
                    if(stats ==0):
                        chars[num].id=int(temp[1])
                        
                    if(stats ==1):
                        chars[num].name=temp[1]
                        
                    if(stats ==2):
                        chars[num].hp=int(temp[1])
                        
                    if(stats ==3):
                        chars[num].max=int(temp[1])
                        
                    if(stats ==4):
                        chars[num].agil=int(temp[1])
                        
                    if(stats ==5):
                        chars[num].str=int(temp[1])
                        
                    if(stats ==6):
                        chars[num].fine=int(temp[1])
                        
                    if(stats ==7):
                        chars[num].inst=int(temp[1])
                        
                    if(stats ==8):
                        chars[num].pres=int(temp[1])
                        
                    if(stats ==9):
                        chars[num].know=int(temp[1])
                        
                    if(stats ==10):
                        chars[num].evas =int(temp[1])
                    
                    if(stats==11):
                        chars[num].feat = temp[1]
                        
                    stats+=1
        await Interaction.response.send_message("Characters created!")
                    


   #display stats and give options
    @client.tree.command(name ="character")
    async def character(Interaction):
        pChar = None
        check  = False
        for i in chars:
            if Interaction.user.id == i.id:
                check =True
                pChar =i
        if check == True:
            #view = Character.Character(596818504154611741,Interaction.user.id)
            emb = discord.Embed(title =pChar.name,description="Feat: "+pChar.feat,colour=discord.Colour.random())
            emb.set_thumbnail(url=Interaction.user.display_avatar)
            emb.add_field(name ="HP", value =str(pChar.hp)+" / "+str(pChar.max),inline = False)
            emb.add_field(name ="Agility",value = pChar.agil, inline=True)
            emb.add_field(name="Strength", value = pChar.str,inline=True)
            emb.add_field(name="Finesse", value = pChar.fine,inline=True)
            emb.add_field(name="Instinct", value = pChar.inst,inline=True)
            emb.add_field(name="Presence", value = pChar.pres,inline=True)
            emb.add_field(name="Knowledge", value = pChar.know,inline=True)
            emb.add_field(name="Evasion", value = pChar.evas,inline=False)
            

            await Interaction.response.send_message(embed=emb)

        else:
            await Interaction.response.send_message("You have no character")

        
    @client.tree.command(name ="roll_dnd",description="Roll the dice")
    async def roll_dnd(Interaction):
        hope = random.randint(1,12)
        fear = random.randint(1,12)
        r1 = hope+fear
        r1c=""
        
        if hope==fear:
            r1c="CRITICAL: "

        hope2 = random.randint(1,12)
        fear2 = random.randint(1,12)
        r2 = hope2+fear2
        r2c=""

        if hope2==fear2:
            r2c="CRITICAL: "
        
        x="hope"
        y="hope"

        if hope<fear:
            x="fear"
        if hope2<fear2:
            y="fear"

        multi=[[r1,r2],[x,y],[r1c,r2c]]
        if r1>r2:
            multi[0][0]=r2 
            multi[0][1]=r1
            multi[1][0]= y
            multi[1][1]=x     
            multi[2][0]=r2c
            multi[2][1]=r1c            

        emb = discord.Embed(title="ROLLS:")
        emb.add_field(name ="Normal", value =r1c+ str(r1)+" with "+x)
        if(not multi[2][0]=="CRITICAL: "):
            emb.add_field(name = "Advantage",value=multi[2][1]+str(multi[0][1])+" with "+multi[1][1])
            emb.add_field(name = "Disadvantage",value=multi[2][0]+str(multi[0][0])+" with "+multi[1][0])
        else:
            emb.add_field(name = "Advantage",value=multi[2][0]+str(multi[0][0])+" with "+multi[1][0])
            emb.add_field(name = "Disadvantage",value=multi[2][1]+str(multi[0][1])+" with "+multi[1][1])
        
        

        await Interaction.response.send_message(embed=emb)

    @client.tree.command(name ="damage",description="hit damage")
    async def damage(Interaction,dmg:int,member:discord.Member):
        id=member.id
        temp ="There is no character registered for: "+member.display_name
        for i in chars:
            if int(id) == i.id:
                if(i.hp-dmg == -i.max and i.hp>=0):
                    i.hp=-3
                    temp =i.name+" has died!"
                elif(i.hp>0 and i.hp-dmg<=0):
                    i.hp=0 
                    temp =i.name+" has fallen!"
                elif(i.hp<=0 and i.hp>=-3):
                    i.hp-=2
                    temp =i.name+" fails 2 death saves!"          
                else:
                    i.hp-=dmg
                    temp =i.name+" has taken "+str(dmg)+" points of damage!"

        await Interaction.response.send_message(temp)
    
    @client.tree.command(name ="heal",description="heal damage")
    async def heal(Interaction,heal:int,member:discord.Member):
        id = member.id
        temp ="There is no character registered for: "+member.display_name
    

        for i in chars:
            if int(id) == i.id:
                if(i.hp<=0 and i.hp>-3):
                    i.hp=heal
                    temp=i.name+" has stabilized!"
                elif(i.hp<-3):
                    temp=i.name+" has already died"
                elif(i.hp+heal>=i.max):
                    i.hp=i.max
                    temp=i.name+" heals to max HP"
                else:
                    i.hp+=heal
                    temp = i.name+" heals: "+str(heal)+" points"

        await Interaction.response.send_message(temp)



        
#--------------------------------------------------------------------------------------------------
#poet
    @client.tree.command(name = "poet")
    async def poet(Interaction, start: str):
        opener = start
        
        await Poet.generatePoem(Interaction, opener)









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