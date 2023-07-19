import discord
import responses
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
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.competing,name = 'life'))
        print(f'{client.user} has arived!')


    #testing non slash profile command
    @client.command(name = 'info')
    async def info(Interaction, member:discord.Member = None):
        try:
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


            for act in member.activities:
                if act.type == discord.ActivityType.listening:
                    listening = act.name
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
        except ValueError:
            raise commands.MemberNotFound(member)
            embed = discord.Embed(title='OOPS',description='Couldnt find the person you were looking for',colour= 0xf461ff)
            await Interaction.send(embed)
            



    #testing slash commands
    @client.tree.command(name = "test", description= "testing")
    async def test_command(interaction):
        await interaction.response.send_message("test working")
        print("Ready!")

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