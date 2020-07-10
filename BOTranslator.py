import discord
import googletrans
#import random
import asyncio, datetime
import languagesid
import tkn
from tkn import token
from languagesid import LANGUAGES
from discord.ext import commands
from googletrans import Translator

client = commands.Bot(command_prefix = '--')
client.activity = discord.Activity(
    name="--info",
    detail="--info",
    type=discord.ActivityType.listening,
    start=datetime.datetime.now(),
)
translator = Translator()

@client.event
async def on_ready():
    print("I'm ready!")

# Don't mind these 2 client event below, see the documentation.md for the story
#@client.event
#async def on_raw_reaction_add(payload):
    #await payload.send(f'{payload.member} mereaksi {payload.emoji} di pesan {payload.message_id}')
    #print(f'{payload.member} mereaksi {payload.emoji.name} di pesan {payload.message_id}')
    #message_id = payload.message_id

#@client.event
#async def on_reaction_add(reaction, user):
    #channel = reaction.message.channel
    #msgs = reaction.message.content
    #emo = reaction.emoji
    #if reaction.emoji.name == 'flag_id':
    #    translations = translator.translate(msgs, dest='id')
    #    await channel.send(f'{msgs} to id is "{translations.text}"')
    #else:
    #    pass
    #await channel.send(f'{user.name} mereaksi {reaction.emoji} di pesan "{reaction.message.content}"')
    #await channel.send(f'{reaction.emoji.name} adalah emoji name dari emoji {emo}')
    #print(f'{payload.member} mereaksi {payload.emoji} di pesan {payload.message_id}')

@client.command()
async def info(ctx):
    embed = discord.Embed(title="Commands", colour=0x008cff)
    embed.add_field(
        name = "--translate (lang_id) (the sentences)",
        value = "Example '--translate ja i love you' -> translate from detection language to Japanese",
        inline= False,
    )
    embed.add_field(
        name = "--langid",
        value = "language id you can translate in to",
        inline = False,
    )
    embed.add_field(
        name = "--ping",
        value = "the bot's ping",
        inline = False,
    )
    await ctx.send(embed=embed)

@client.command()
async def langid(ctx):
    embed = discord.Embed(title="Supported Langueages", colour=0x008cff)
    embed.add_field(
        name = "ID : Languages",
        value = "'af': 'afrikaans'\n'sq': 'albanian'\n'am': 'amharic'\n'ar': 'arabic'\n'hy': 'armenian'\n'az': 'azerbaijani'\n'eu': 'basque'\n'be': 'belarusian'\n'bn': 'bengali'\n'bs': 'bosnian'\n'bg': 'bulgarian'\n'ca': 'catalan'\n'ceb': 'cebuano'\n'ny': 'chichewa'\n'zh-cn': 'chinese (simplified)'\n'zh-tw': 'chinese (traditional)'\n'co': 'corsican'\n'hr': 'croatian'\n'cs': 'czech'\n'da': 'danish'\n'nl': 'dutch'\n'en': 'english'\n'eo': 'esperanto'\n'et': 'estonian'\n'tl': 'filipino'\n'fi': 'finnish'\n'fr': 'french'\n'fy': 'frisian'\n'gl': 'galician'\n'ka': 'georgian'\n'de': 'german'\n'el': 'greek'\n'gu': 'gujarati'\n'ht': 'haitian creole'\n'ha': 'hausa'\n'haw': 'hawaiian'\n'iw': 'hebrew'\n'hi': 'hindi'\n'hmn': 'hmong'\n'hu': 'hungarian'\n'is': 'icelandic'\n'ig': 'igbo'\n'id': 'indonesian'\n'ga': 'irish'\n'it': 'italian'\n'ja': 'japanese'\n'jw': 'javanese'\n'kn': 'kannada'\n'kk': 'kazakh'\n'km': 'khmer'\n'ko': 'korean'\n'ku': 'kurdish (kurmanji)'\n'ky': 'kyrgyz'",
        inline= True,
    )
    embed.add_field(
        name="ID : Languages",
        value="'lo': 'lao'\n'la': 'latin'\n'lv': 'latvian'\n'lt': 'lithuanian'\n'lb': 'luxembourgish'\n'mk': 'macedonian'\n'mg': 'malagasy'\n'ms': 'malay'\n'ml': 'malayalam'\n'mt': 'maltese'\n'mi': 'maori'\n'mr': 'marathi'\n'mn': 'mongolian'\n'my': 'myanmar (burmese)'\n'ne': 'nepali'\n'no': 'norwegian'\n'ps': 'pashto'\n'fa': 'persian'\n'pl': 'polish'\n'pt': 'portuguese'\n'pa': 'punjabi'\n'ro': 'romanian'\n'ru': 'russian'\n'sm': 'samoan'\n'gd': 'scots gaelic'\n'sr': 'serbian'\n'st': 'sesotho'\n'sn': 'shona'\n'sd': 'sindhi'\n'si': 'sinhala'\n'sk': 'slovak'\n'sl': 'slovenian'\n'so': 'somali'\n'es': 'spanish'\n'su': 'sundanese'\n'sw': 'swahili'\n'sv': 'swedish'\n'tg': 'tajik'\n'ta': 'tamil'\n'te': 'telugu'\n'th': 'thai'\n'tr': 'turkish'\n'uk': 'ukrainian'\n'ur': 'urdu'\n'uz': 'uzbek'\n'vi': 'vietnamese'\n'cy': 'welsh'\n'xh': 'xhosa'\n'yi': 'yiddish'\n'yo': 'yoruba'\n'zu': 'zulu'\n'he': 'Hebrew'",
        inline=True
    )
    await ctx.send(embed=embed)

@client.command()
async def translate(ctx, destination, *, sentences):
    dest = destination
    langs = translator.detect(sentences)
    translations = translator.translate(sentences, dest)
    embed = discord.Embed(title="Translate", colour=0x008cff)
    embed.add_field(
        name = "Sentences from " + LANGUAGES.get(langs.lang),
        value = sentences,
        inline= False,
    )
    embed.add_field(
        name = "Translate to " + LANGUAGES.get(dest),
        value = translations.text + "\nPronounciation: " + translations.pronunciation,
        inline= False,
    )
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

client.run(token)