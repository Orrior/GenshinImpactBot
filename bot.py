# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'TOKEN_HERE'
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
                      "Бля, вводите данные так: \n!calc Attack,CritChance(коэффициент нужен, долбоёб)," \
                      "Critdamage(Тут тоже коэффициент бляхамуха, не ебёт)\n" \
                      "!calc атака,критшанс,критурон\n```"

        if str(message.author) == "Bog#7709":
            await message.channel.send(f"```\nДарова лёха меня в бота превратили ебать\n{mainmessage}\n```")
        if str(message.author) == "Zhryke#2981":
            await message.channel.send("ъеъ, што")
        else:
            await message.channel.send(f"```\n{mainmessage}\n```")

    if str(msg).lower() == "артём" or str(msg).lower() == "артем" or str(msg).lower() == "artem":
        if str(message.author) == "Ateyl#6089":
            await message.channel.send("Бузак")
        else:
            await message.channel.send("**Пидорас**")

    if msg.startswith('!calc'):
        print(f"{msg} OK MASTA LETS KILL DA HOE \n {str(parsetest(msg))}")
        answer = parsetest(msg)
        if answer == "Лээ, ты бля нормально вводи эжжи" and str(message.author) == "Ateyl#6089":
            await message.channel.send(f"Артём блять введи всё нормально заебал")
        elif str(message.author) == "ARBUZI#9361":
            await message.channel.send(f"Ким бля ди нахуй не лезь")
        elif answer == "Лээ, ты бля нормально вводи эжжи" and str(message.author) == "Романыч#3956":
            await message.channel.send(f"Романыч бля всё хуйня давай по новой переменную. Если не понятно пиши !halp")
        elif str(message.author) == "Bog#7709":
            await message.channel.send(f"```\nдарова лёха\n{parsetest(msg)}\n```")
        else:
            await message.channel.send(f"```\n{parsetest(msg)}\n```")
client.run(TOKEN)