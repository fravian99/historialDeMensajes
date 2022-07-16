

from discord.ext import commands
import historial

bot=commands.Bot(command_prefix='>')


@bot.listen()
async def on_message(message):
    number = int()

    if 'historial' in message.content:
        
        await historial.history(message,bot)
        await message.delete()

bot.run('token del bot')