print('--------------------------')
print('   CALCULA TU COMISION')
print('__________________________')
user= input('Hola, ingresa tu nombre: ')

ventas= input('Ingresa tus ventas: ')

comision= float(ventas)*13/100
comision=round(comision,2)
print(user)
print(f' {user}, generaste ${comision}  en comisiones')
