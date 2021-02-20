# bot.py
import os
import bdo_price_check
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'Nope'
GUILD = 'Замес'

client = discord.Client()


def parsetest(string):
    """
    Ну кароче у нас тут метод хуё-моё.
    Аттака, критшанс, критмножитель
    """
    test_message = (str(string))[5:]  # чтобы убрать чёртов !calc
    if test_message.startswith(" "):  # если стоит пробел, его сносим, а если не стоит, то и сносить нехуй
        test_message = test_message[1:]
    gstat = test_message.split(",")  # превращаем стринг в массив нахуй эээ
    try:
        gstat = list(map(float, gstat))  # у нас массив стрингов, а для матеши нужен массив чисел бляхамуха
    except ValueError:
        return "Лээ, ты бля нормально вводи эжжи"
    critdamage = gstat[0] * (gstat[2]+1)
    finalmessage = f"Урон = {gstat[0]}\nШанс крита = {round(gstat[1]*100)}%\n" \
                   f"Крит. множитель = {round(gstat[2]*100+ 100)}%\nУрон с критом = {round(critdamage)}\n" \
                   f"Средний урон за удар = {round(gstat[0]*(1-gstat[1])+critdamage*gstat[1],2)}"  # украшаем блять
    return finalmessage


@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    print(msg)

    if msg == '!halp':
        mainmessage = "Готов стать калькулятором вашей хуйни\n" \
                      "!calc атака,критшанс,критурон\n!market - цена на хуйню из бдо\nАртём - пидорас"

        await message.channel.send(f"```\n{mainmessage}\n```")

    if str(msg).lower() == "артём" or str(msg).lower() == "артем" or str(msg).lower() == "artem":
        if str(message.author) == "Ateyl#6089":
            await message.channel.send("Бузак")
        else:
            await message.channel.send("**Пидорас**")

    if msg == "!market":
        await message.channel.send(f"```\n{bdo_price_check.BdoProfit.formatted()}\n```")

    if msg.startswith('!calc'):
        print(f"{msg} OK MASTA LETS KILL DA HOE \n {str(parsetest(msg))}")
        answer = parsetest(msg)
        if answer == "Лээ, ты бля нормально вводи эжжи" and str(message.author) == "Ateyl#6089":
            await message.channel.send(f"Артём блять введи всё нормально заебал")
        else:
            await message.channel.send(f"```\n{parsetest(msg)}\n```")

client.run(TOKEN)