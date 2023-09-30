import turtle
a= turtle.Turtle()

def drtg():
  a.forward(100)
  a.left(90)
  a.forward(50)
  a.left(90)
  a.forward(100)
  a.left(90)
  a.forward(50)
  
def kare():
  a.forward(50)
  a.left(90)
  a.forward(50)
  a.left(90)
  a.forward(50)
  a.left(90)
  a.forward(50)

def yuvarlak():
  a.circle(50)
  
def tri():
  a.fd(50)
  a.left(120)
  a.fd(50)
  a.left(120)
  a.fd(50)
  a.left(120)
  
b=input("Üçgen/Daire/ Dikdörtgen/ Kare çizmek için birinizi seçiniz.")
if b == "Daire":
  yuvarlak()
elif b == "Dikdörtgen":
  drtg()
elif b == "Kare":
  kare()
elif b == "Üçgen":
  tri()
else:
  print("Lütfen soruda belirtildiği gibi yaznınız.")
