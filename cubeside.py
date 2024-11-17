import math 

# A program to calculate the volume and surface area of ​​a cube.
cuboida = float(input("cube side a? "))
cuboidb = float(input("cube side b? "))
cuboidc = float(input("cube side c? "))
cuboidsurface = ((cuboida * cuboidb) * 2) + ((cuboidb * cuboidc) * 2) + ((cuboida * cuboidc) * 2)
cuboidvolume = (cuboida * cuboidb) * cuboidc
print ("cuboid surface: ", cuboidsurface)
print ("cuboid volume: ", cuboidvolume)








