import nest_asyncio
nest_asyncio.apply()
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('euh ja het werkt fz')

'''@client.event
async def on_message_delete(message): 
    if message.author == client.user:
        await message.channel.send(message.content)
        return
    
    await message.channel.send('Someone just deleted this message from ' + message.author.name +  ' : ' + '```' + message.content + '```')'''

@client.event
async def on_guild_channel_create(channel):
    await channel.send('Welcome, I was expecting you...')

@client.command(aliases = ['m'])
async def mute(context):
    vc = context.message.author.voice.channel
    for member in vc.members:
        if member.voice.self_mute == 0:
            await member.edit(mute = 1)
    await context.message.delete()

@client.command(aliases = ['um'])
async def unmute(context):
    vc = context.message.author.voice.channel
    for member in vc.members:
        await member.edit(mute = 0)
    await context.message.delete()

@client.command()
async def clear(context,*,number=1):
    messages = await context.channel.history(limit = number+1).flatten()
    await context.channel.delete_messages(messages)

lobbycode = None
@client.command(aliases = ['cd'])
async def code(context,*,new_lobbycode=''):
    global lobbycode 
    await context.message.delete()
    if len(new_lobbycode) == 0:
        if (lobbycode != None):
            await context.channel.send('```' + lobbycode + '```')
        else:
            await context.channel.send('No code yet')
    elif len(new_lobbycode) == 9 or len(new_lobbycode) == 6:
        lobbycode = new_lobbycode.upper()
        await context.channel.send('```' + lobbycode.upper() + '```')
    else:
        await context.channel.send(new_lobbycode.upper() + ' is not a valid code!')    
        
@client.command()
async def hotel(ctx):
    await ctx.send('Trivago!')
    
@client.command()
async def lekker_eten(ctx):
    await ctx.send('Wa een stom command is da!')
        
@client.command()
async def vliegt_de_blauwvoet(ctx):
    await ctx.send('``Storm op zee!``')

@client.command()
async def mock(ctx,*,to_mock):
    mocked_text = ''
    for i in range(0,len(to_mock)):
        if (i%2):
            mocked_text += to_mock[i].upper()
        else:
            mocked_text += to_mock[i].lower()
    await ctx.send(mocked_text)
    
@client.command()
async def python(ctx):
    await ctx.send('Nu blij Benjamin?')
    
@client.command()
async def stemopsimon(ctx):
    await ctx.send('Sinds wanneer heeft een SSL stemmen nodig?')

@client.event
async def on_member_join(member):
    for i in member.guild.channels:
        if i.name == 'general':
            ch = i
            await ch.send(f'Heyhey {member.display_name}!')
            for e in member.guild.roles:
                if e.name == 'Crewmates':
                    await member.add_roles(e,reason=None)
                    return 
        
@client.event
async def on_member_remove(member):
    for i in member.guild.channels:
        if i.name == 'general':
            ch = i
            await ch.send(f'Byebye {member.display_name}!')
            return 

@client.command()
async def crew(context, member : discord.Member):
    for e in context.guild.roles:
        if e.name == 'Crewmates':
            await member.add_roles(e)
            return 

@client.command()
async def commands(context):
    await context.send('```md\n' + '#!mute = Mutes the voice chat.\n'
                       '#!unmute = Unmutes the voice chat.\n'
                       '#!clear <#> = Clears the last number of messages (standard = 1)\n'
                       '#!code <******-**>= Formats 6-digit code.\n'
                       '#!code = Resends current code.\n'
                       '#!hotel = Just try it!' + '```')

client.run('NzU0MDIwODIxMzc4MjY5MzI0.X1uqnA.o9Ea3VuoJpC797mfx0jFhLEozu4')