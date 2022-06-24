larg = float(input('Wall Width:'))
alt = float(input('Wall Height:'))
area = larg * alt
ink = area / 2
print('The wall area is {}m² \nAmount of ink needed to paint the wall:{:.1f}l'.format(area, ink))
