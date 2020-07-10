## Motives and Background

I really want to make a bot since there are many bot on social media where the user are having so much fun with that. So, I made this project to grant that desire. Discord is the platform where people from around the world meet and communicate. So, maybe if I made this bot, it can help them communicate to each other if they haven't understand the languages or can help them to studying other languages without opening google translate in their browser.

I want to explain the second and third `@client.event` in `BOTranslate.py`. At the first time, I want to make the bot translating to destination languages right after the user react the message with flag emojis that they want to translate in to. But, after I code it, the API parameters doesn't work. So I decide to user typing normally with some command if they want to translate the word or sentences.

## Project Duration

I started made this bot at 23 June 2020. The features completed at 9 July 2020.

## Structure Code

```
BOTranslator
┣ .gitignore
┣ BOTranslator.py
┃ ┣ on_ready
┃ ┣ info
┃ ┣ langid
┃ ┣ translate
┃ ┣ ping
┣ languagesid.py
┣ requirements.txt
┣ tkn.py
```

## Class and Function
File: BOTranslator.py
Function | Access Level | Parameter | Return
-------- | ------------ | --------- | ------
on ready | public | None | None
info | public | ctx : discord.ctx | None
langid | public | ctx : discord.ctx | None
translate | public | ctx : discord.ctx, destination : str, sentences : Tuple | None
ping | public | ctx : discord.ctx | None

## Statistics
The line that i made in all these files are **215** lines
