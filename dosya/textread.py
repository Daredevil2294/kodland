import discord

f = open('dosya\text.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()

f = open('dosya\text.txt' , 'w', encoding='utf-8')
text = 'Yeni Yazı'
f.write(text)
f.close()

with open('dosya\images\meme2.jpg', 'rb') as f:
        picture = discord.File(f)

with open('dosya\images\meme1.jpg', 'rb') as f:
        picture = discord.File(f)