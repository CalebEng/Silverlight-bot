import discord
import responses
from discord import app_commands



async def sendMSG(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
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
    client = discord.Client(intents=intents)

    tree = app_commands.CommandTree(client)

    @client.event
    async def on_ready():
        await tree.sync()
        print(f'{client.user} has arived!')

    @tree.command(name = "test", description= "testing")
    async def test_command(interaction):
        await interaction.response.send_message("test working")
        print("Ready!")

    @tree.command(name = "info", description= "Who are you")
    async def info(Interaction, member:discord.Member = None):
        
        if member == None:
            member = Interaction.user
        
    
        name = member.display_name
        ids = member.id
        pfp = member.display_avatar
        des = ''


        guild = client.get_guild(Interaction.guild.id)
        member2 = await guild.fetch_member(ids)

        stat = member2.status
        activity=member2.activities
        game=None
        streaming = None
        cusAct = None


        for role in member.roles:
            if role !="@everyone":
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

    client.run(TOKEN)