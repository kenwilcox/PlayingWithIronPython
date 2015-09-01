import clr
clr.AddReferenceToFile("Mapack.dll")
from Mapack import *

#print Matrix.__new__.__doc__

m = Matrix(2,2,1.2)
n = Matrix(1,2)
n[0,0] = 4
print m
print n

#print m * n
#print n.Transpose() * m
print m * 3
print n + -n

