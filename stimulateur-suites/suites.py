import matplotlib.pyplot as plt

def suite_arithmetique(u0, r, n):
  u=[0]*n
  for i in range(n):
    u[i]= u0+i*r
  return u

def suite_geometrique(u0 ,q ,n):
  u=[0]*n
  for i in range(n):
    u[i]= u0*q**i
  return u

def suite_fibonacci(n):
  u=[0]*n
  u[0]=0
  u[1]=1
  for i in range(2,n):
    u[i]=u[i-1]+u[i-2]
  return u

def afficher_graphique(suite, titre):
  indices= list(range(len(suite)))
  plt.plot(indices, suite)
  plt.title(titre)
  plt.show()

