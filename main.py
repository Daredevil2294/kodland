print('hello world')
import random
print('Güçlü bir şifre için şifre uzunluğu giriniz. Güçlü bir şifre için 12 karakter kullanmanızı öneririz')
a=int(input('Şİfre uzunluğu:'))
b = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
print('Kendi istediğiniz şifreyi seçmeniz için size 4 ayrı alternatif veriyoruz:')
for i in range (4):
    c= ''
    for i in range(0,a):
        d= random.choice(b)
        c=c+d
    print(c)