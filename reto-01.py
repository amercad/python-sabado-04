numero = 0
sum = 0

while numero >= 0:
    numero = int( input('Digite un numero: ') )
    if numero >= 0:
        sum += numero
else:
    print('termino')
    
    
print( f'La suma de los numero ingresados es: { sum }' )