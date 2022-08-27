observador = 1

print('********** MENU **********')
print('     0. SALIR')
print('     1. SALUDAR')
print('     2. DESPEDIR ')
print('**************************')

while( observador != 0 ):
    observador = int( input('Digite un opcion del menu: ') )
    if (observador == 0):
        break
    elif observador == 1:
        print( 'Bienvenido, como estas ?' )
    elif observador == 2:
        print( 'Adios' )
    else: 
        print( 'Digite un opcion valida' )
else:
    print( 'termine' )