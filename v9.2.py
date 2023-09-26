distance = float(input('введите дальность выстрела - '))
if distance >28 and distance <30:

    print ('попал ')

elif distance >=30:

    print ('перелет')

elif distance >0 and distance <=28:

    print ('недолёт')

elif distance >=0:

    print ('не стреляй по своим ')