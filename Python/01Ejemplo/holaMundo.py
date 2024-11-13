#comentario
#definir una variable
#ejemplo if

x = 28

if x < 0:
    # cuando sea verdad
    print('Es menor a 0')
elif x > 0:
   print('Es mayor a 0')
else:
    print('Es 0')

print ("-----------------------------")
# bucles

numero = 0
print ("Tabla del dos")

while numero <= 10 :
    print ("Resultado :", 2*numero)
    numero += 1

print ("-----------------------------")

#for

numero = [3,7,5,8]

for n in numero:
    print(n)