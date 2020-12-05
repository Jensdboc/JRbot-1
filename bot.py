with open('ID.txt', 'r') as IDfile:
    for ID in IDfile.readlines():
        if ID == 'Jens':
            import nest_asyncio
            nest_asyncio.apply()   
            
import discord
from discord.ext import commands 

client = commands.Bot(command_prefix='!')

client.mute_message = None

@client.event
async def on_ready():
    print('euh ja het werkt fz')

#Command checks

@client.check
async def check_blacklist(ctx):
    with open('Blacklist.txt', 'r') as blacklist_file:
        for blacklisted_user in blacklist_file.readlines():
            if str(ctx.message.author.id) == str(blacklisted_user)[:-1]:
                return False
        return True

def admin_check(ctx):
    with open('Admin.txt', 'r') as admin_file:
        for admin in admin_file.readlines():
            if str(ctx.message.author.id) == str(admin)[:-1]:
                return True
        return False

#Admin commands

@client.command()
@commands.check(admin_check)
async def blacklist(ctx,*,user_id):
    with open('Blacklist.txt', 'a') as blacklist_file:
        blacklist_file.write(user_id + '\n')

@client.command()
@commands.check(admin_check)
async def admin(ctx):
    await ctx.channel.send('Yup')

@client.command()
@commands.check(admin_check)
async def start(ctx, dier):
    with open('Dieren.txt','a') as txt: 
        txt.truncate(0)
        txt.write(dier + '\n')
    with open('Last_user.txt', 'a') as user_file:
        user_file.truncate(0)
        user_file.write('placeholder')
    embed =  discord.Embed(title='Woordenketting', description='A new game has been started with ' + '`' + dier + '`' + ' as first word.', colour=0x11806a)
    await ctx.send(embed=embed)
    
#User commands

@client.command(aliases = ['m'], brief = "Mutes voicechannel")
async def mute(context):
    vc = context.message.author.voice.channel
    for member in vc.members:
        if member.id != 235088799074484224:
            await member.edit(mute = 1)
    await context.message.delete()

@client.command(aliases = ['um'], brief = "Unmutes voicechannel")
async def unmute(context):
    vc = context.message.author.voice.channel
    for member in vc.members:
        await member.edit(mute = 0)
    await context.message.delete()

@client.command()
async def clear(context,*,number=1):
    messages = await context.channel.history(limit = number+1).flatten()
    for mes in messages:
        if(client.mute_message):
            if (client.mute_message.id == mes.id):
                if (context.message.author.voice):
                    vc = context.message.author.voice.channel
                    for member in vc.members:
                        await member.edit(mute = 0)
                client.mute_message = None
    await context.channel.delete_messages(messages)

lobbycode = None
@client.command(aliases = ['cd'])
async def code(context,*,new_lobbycode=''):
    global lobbycode 
    await context.message.delete()
    if len(new_lobbycode) == 0:
        if (lobbycode != None):
            embed1 = discord.Embed(title=lobbycode, color=0x2ecc71)
        else:
            embed1 = discord.Embed(title='No code yet', color=0xff0000)
        await context.channel.send(embed=embed1)
    elif len(new_lobbycode) == 9 or len(new_lobbycode) == 6:
        for channel in context.guild.channels:
            if channel.name == 'mutechannel':
                lobbycode = new_lobbycode.upper()
                embed2 = discord.Embed(title=lobbycode.upper(), color=0x2ecc71)
                embed2.add_field(name='Mute', value='Press \N{Speaker with Cancellation Stroke}')
                embed2.add_field(name='Unmute', value='Press \N{Speaker with Three Sound Waves}')
                embed2.add_field(name='Cancel', value='Press \N{Cross Mark}')
                if (client.mute_message):
                    await client.mute_message.delete()
                client.mute_message = await channel.send(embed=embed2)
                await client.mute_message.add_reaction('\N{Speaker with Cancellation Stroke}')
                await client.mute_message.add_reaction('\N{Speaker with Three Sound Waves}')
                await client.mute_message.add_reaction('\N{Cross Mark}')
                return
    else:
        embed3 = discord.Embed(title=new_lobbycode.upper()+ ' is not a valid code!', color=0xff0000)
        await context.channel.send(embed=embed3)
    
autist_id = 383952659310444544
@client.command()
async def mock(ctx,*,to_mock):
    mocked_text = ''
    if(ctx.message.author.id == autist_id):
        c = 0
        for i in range(len(to_mock)):
            if (c%2):
                mocked_text += to_mock[i].lower()
            else:
                mocked_text += to_mock[i].upper()
            if(to_mock[i] != ' '):
                c += 1
    else:
        for i in range(len(to_mock)):
            if (i%2):
                mocked_text += to_mock[i].upper()
            else:
                mocked_text += to_mock[i].lower()
    embed = discord.Embed(title=mocked_text,color=0xe67e22)
    await ctx.send(embed=embed)
    
@client.command()
async def nick(ctx, member : discord.Member,*, nickname):
    await member.edit(nick=nickname)
    
@client.command()
async def hotel(ctx):
    embedVar = discord.Embed(title="Trivago!", color=0x992d22)
    await ctx.send(embed=embedVar)
        
@client.command()
async def vliegt_de_blauwvoet(ctx):
    await ctx.send('``Storm op zee!``') 
    
@client.command()
async def python(ctx):
    await ctx.send('Nu blij Benjamin?')

from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

@client.command()
async def stemopsimon(ctx):
    embed = discord.Embed(title='Sinds wanneer heeft een SSL stemmen nodig?', color=0xff0000) 
    link = 'https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTY2NjgyOTkyNTMyNTMwMjMx/gettyimages-2637237.jpg'
    embed.set_image(url=link)
    await ctx.send(embed=embed)
    channel = ctx.message.author.voice.channel
    await channel.connect()
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)
    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info('https://www.youtube.com/watch?v=AlJ8z86e8A8', download=False)
        URL = info['formats'][0]['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        
@client.command()
async def broederliefde(ctx):
    embed = discord.Embed(color=0x9b59b6)
    link = 'https://cdn.discordapp.com/attachments/770691436319342654/773576247254057000/unknown.png'
    embed.set_image(url=link)
    await ctx.send(embed=embed)
    
@client.command()
async def perfection(ctx):
    embed = discord.Embed(color=0x9b59b6)
    link = 'https://media.discordapp.net/attachments/770691436319342654/781997388394528768/unknown.png?width=962&height=300'
    embed.set_image(url=link)
    await ctx.send(embed=embed)    
    
import random
@client.command()
async def switch(ctx):
    l1 = []
    vc = ctx.message.author.voice.channel
    for member in vc.members:
        if member.id != 235088799074484224:
            print(member)
            l1.append(member.nick)
            #await ctx.message.author.send('Hallookes')
    l2 = l1.copy()
    random.shuffle(l1)
    embed = discord.Embed(title='Switch-game',description = 'Click on the spoiler message next to your name to reveal who you need to be!', color=0x9b59b6)
    for i in range(len(l1)):
        embed.add_field(name=f'{l2[i]}', value='||' + f'{l1[i]}' + '||' )
    await ctx.send(embed=embed)  

@client.command()
async def crew(context, member : discord.Member):
    for e in context.guild.roles:
        if e.name == 'Crewmates':
            await member.add_roles(e)
            return 
        
@client.command()
async def hug(context):
    embed = discord.Embed(title='You get a free hug!', color=0x1DDCF)
    link = 'https://media.discordapp.net/attachments/774593310844387358/783437572704567296/hug.png'
    embed.set_image(url=link)
    await context.message.author.send(embed=embed)
     
import urllib.request
@client.command(aliases = ['tm'])
async def thumbmail(ctx, url):
    urllib.request.urlretrieve(url, filename = 'secret.html')
    with open('secret.html', 'r', encoding = 'utf-8') as infile:
            start = '<meta property="og:image"'
            for line in infile:
                if start in str(line):
                    jpg = ''
                    for i in range(len(line)):
                        if line[i] == 'j' and line[i+1] == 'p' and line[i+2] == 'g':
                            jpg += 'jpg'
                            await ctx.send(jpg)
                            await ctx.message.delete()
                        if i > 38:
                            jpg += line[i]                       

@client.command()
async def commands(ctx):
    embed = discord.Embed(title='List of commands', color=0x7289da)
    embed.add_field(name='!Unmute [!um]', value='Unmutes the voicechat' )
    embed.add_field(name='!Mute [!m]', value='Mutes the voicechat' )
    embed.add_field(name='!clear <#>', value='Clears the last number of messages (standard = 1)' )
    embed.add_field(name='!code <*\*\*\*\*\*-**>  [!cd]', value='Formats 6-digit code, NA/EU is optional' )
    embed.add_field(name='!code', value='Resends current code, click on the emoji to mute, unmute or to remove the message' )
    embed.add_field(name='!hotel', value='Just try it!' )
    embed.add_field(name='!crew <@person>', value='Gives someone the crew-role' )
    embed.add_field(name='!broederliefde', value=':)' )
    embed.add_field(name='!stemopsimon', value='**ussr intensifies**' )
    embed.add_field(name='!mock <...>', value='Mock inserted text' )
    embed.add_field(name='!commands', value='Shows this message' )
    embed.add_field(name='!python', value='Alstublieft Benjamin' )
    embed.add_field(name='!nick <@person> <nick>', value='Changes the nickname of a certain person' )
    embed.add_field(name='!thumbmail <url> [!tm]', value='Provide a youtube link and recieve the thumbmail' )
    embed.add_field(name='!hug', value='Feeling lonely?' )
    embed.add_field(name='!switch', value='Starts a among-us switch game, click on the spoiler under your name' )
    embed.add_field(name='!perfection', value='Perfection!' )
    await ctx.send(embed=embed)

#User commands dierenketting

@client.command(aliases = ['d'])
async def dier(ctx,*, dier=None):
    list = []
    with open('Dieren.txt','r') as txt: 
        for word in txt.readlines():
            list.append(str(word[:-1]))
            woord = list[-1] 
            letter = list[-1][-1]
    if dier == None:
        embed =  discord.Embed(title='Woordenketting', description='You need to find an animal starting with ' + '`' + letter + '`' + ', final letter of ' + '`' + woord + '`', colour=0x11806a)
        await ctx.send(embed=embed)
        return
    if dier.lower() in list:
        embed =  discord.Embed(title='Woordenketting', description='`' + dier + '`' + ' already in list!', colour=0xff0000)
        await ctx.send(embed=embed)
        return 
    elif dier.lower() == 'linx' or dier.lower() == 'lynx':
        embed =  discord.Embed(title='Woordenketting', description='`' + dier + '`' + ' has NOT been added!', colour=0xff0000)
        embed.add_field(name='Note', value='Do you really have to be that guy?')
        await ctx.send(embed=embed)
        return 
    with open('Last_user.txt', 'r') as user_file:
        for user in user_file.readlines():
            with open('Dieren.txt','a') as txt:
                if str(ctx.message.author.id) != user and str(dier[0]).lower() == letter.lower():
                    with open('Last_user.txt', 'a') as user_file:
                        user_file.truncate(0)
                        user_file.write(str(ctx.message.author.id)) 
                        txt.write(dier.lower() + '\n')
                        embed =  discord.Embed(title='Woordenketting', description='`' + dier + '`' + ' has been added!', colour=0x11806a)
                        await ctx.send(embed=embed)
                elif str(dier[0]).lower() != letter.lower() and str(ctx.message.author.id) != user:
                    embed =  discord.Embed(title='Animal should start with ' + '`' + letter + '`' + ', final letter of ' + '`' + woord + '`', colour=0xff0000)
                    await ctx.send(embed=embed)
                else:
                    embed =  discord.Embed(title='Woordenketting', description='You need to wait for someone else to submit an animal!', colour=0xff0000)
                    await ctx.send(embed=embed)        
    
@client.command()
async def count(ctx):
    number = 0
    with open('Dieren.txt','r') as txt: 
        for word in txt.readlines():
            number += 1
    embed = discord.Embed(title='Woordenketting', description='The list contains ' + '`' + f'{number}' + '`' + ' animals so far.', colour=0x11806a)
    await ctx.send(embed=embed)

@client.command()
async def time_nick(ctx):
    l = ['appelflap', 'piemelgefriemel','kaiser Hans', 'Wedidntstartthefire', 'Kaboom', 'Potverdikke', 'DA imposter', '☺', '\N{Cross Mark}', 'VOTE KICK NORICK', 'Emma', 'Floefie', 'Meesje', 'Processing...', 'Norick03', 'ComradBenji']
    vc = ctx.message.author.voice.channel
    for member in vc.members:
        print(member)
        nickname = random.choice(l)
        await member.edit(nick=str(nickname))

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
   
@client.command(pass_context=True)
async def leave(ctx):
    client = ctx.message.guild.voice_client
    await client.disconnect()
    
#Bot events

@client.event
async def on_guild_channel_create(channel):
    embed =  discord.Embed(title='Welcome, I was expecting you...', colour=0xff0000)
    await channel.send(embed=embed)

@client.event
async def on_member_join(member):
    for i in member.guild.channels:
        if i.name == 'general':
            ch = i
            embed = discord.Embed(title=f'Heyhey {member.display_name}!', colour=0xff0000)
            await ch.send(embed=embed)
            for e in member.guild.roles:
                if e.name == 'Crewmates':
                    await member.add_roles(e,reason=None)
                    return 
        
@client.event
async def on_member_remove(member):
    for i in member.guild.channels:
        if i.name == 'general':
            ch = i
            embed = discord.Embed(title=f'Byebye {member.display_name}!', colour=0xff0000)
            await ch.send(embed=embed)
            return 


@client.event
async def on_reaction_add(reaction,user):
    if(user.id != client.user.id):
        if (reaction.message.id == client.mute_message.id):
            mute_emoji = '\N{Speaker with Cancellation Stroke}'
            unmute_emoji = '\N{Speaker with Three Sound Waves}'
            cancel_emoji = '\N{Cross Mark}'
            if (str(reaction.emoji) == unmute_emoji):
                await reaction.remove(user)
                if (user.voice):
                    vc = user.voice.channel
                    for member in vc.members:
                        await member.edit(mute = 0)
            if (str(reaction.emoji) == mute_emoji):
                await reaction.remove(user)
                if (user.voice):
                    vc = user.voice.channel
                    for member in vc.members:
                        if member.id != 235088799074484224:
                            await member.edit(mute = 1)
            if (str(reaction.emoji) == cancel_emoji and user.voice):
                await reaction.remove(user)
                await client.mute_message.delete()
                client.mute_message = None
                if (user.voice):
                    vc = user.voice.channel
                    for member in vc.members:
                        await member.edit(mute = 0)

client.run('NzU0MDIwODIxMzc4MjY5MzI0.X1uqnA.o9Ea3VuoJpC797mfx0jFhLEozu4')