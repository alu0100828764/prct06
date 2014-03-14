#! usr/bin/python 

def aproximacion(n): 
 
  suma = 0.0 
  for i in range ( 1, n+1): 
     
      a = float (i-1)/n
      b = float (i)/n
      xi = float (i-0.5)/n 
      fxi = 4.0/(1.0+xi*xi)
      suma = suma + fxi
       
  r = suma/float (n) 
  return r
 
n = int(raw_input(' Introducir el numero de intervalos  : '))
m = int (raw_input( ' Introducir el numero de repeticiones : ' )) 

l = []
for i in range ( 1, m+1):
  pi = aproximacion(n*i) 
  l = l + [pi]

print l 