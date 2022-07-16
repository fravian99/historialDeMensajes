import discord


async def history(message,bot):
    numberString = message.content[10:]
    number:int = int(numberString)
    author =message.author
    channel = message.channel
    messages=list()
    counter=0
    messages = await channel.history(limit = 100).flatten()
    await channel.send(author.name)
    messages = messages[::-1]
    for actualMessage in messages:
        
        if(not 'historial' in actualMessage.content):
            if(counter == number):
                break
            if(actualMessage.author==author):
                counter=counter +1    
                await channel.send(actualMessage.content)