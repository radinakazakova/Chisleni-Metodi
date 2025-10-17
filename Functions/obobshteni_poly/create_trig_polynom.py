def createTrigPolynom(coeficient):
     size = len(coeficient)
     expr = 0
     counter = 1
     for i in range(size):
         if i == 0:
             expr += coeficient[i]
         elif i % 2 != 0: 
             expr += coeficient[i] * sp.cos(counter * x)
         else:
             expr += coeficient[i] * sp.sin(counter * x)
             counter += 1
     return expr
