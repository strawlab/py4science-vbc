from sympy import *

a,b,c,d,e,f,g,h,i,x,y,z = var('a b c d e f g h i x y z')

f_1 = a*x + b*y + c*z - 1
f_2 = d*x + e*y + f*z - 1
f_3 = g*x + h*y + i*z - 1

s1 = solve([f_1,], x, y, z)

s2 = solve([f_1,f_2], x, y, z)

s3 = solve([f_1,f_2,f_3], x, y, z)

l = lambdify((y,z,a,b,c), s1[x], 'numpy')

print l(1,1,1,1,1)
