import random
import discord
import math
import asyncio
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def emoji_olusturucu():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)

def yazi_tura():
    para = random.randint(0, 2)
    if para == 0:
        return "YAZI"
    else:
        return "TURA"
    
import turtle
a= turtle.Turtle()

def turtledraw_dikdörtgen():
  a.forward(100)
  a.left(90)
  a.forward(50)
  a.left(90)
  a.forward(100)
  a.left(90)
  a.forward(50)
  
def turtledraw_kare():
  a.forward(50)
  a.left(90)
  a.forward(50)
  a.left(90)
  a.forward(50)
  a.left(90)
  a.forward(50)

def turtledraw_yuvarlak():
  a.circle(50)
  
def turtledraw_üçgen():
  a.fd(50)
  a.left(120)
  a.fd(50)
  a.left(120)
  a.fd(50)
  a.left(120)

   