import math
ang = int(input('Enter the angle you want: '))
cos = math.cos(math.radians(ang))
sin = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
print('The sine of {}° is {:.3f} \nThe cosine of {}° is {:.3f} \nThe tangent of {}° is {:.3f}'.format(ang, sin, ang, cos, ang, tan))
