def createPolynom(coeficient):
     size = len(coeficient)
     expr = 0
     for i in range(size):
         expr += coeficient[i] * sp.exp(x * i)
     return expr
