import numpy as np
import matplotlib.pyplot as plt

nMax = 1000
stdDev = .2
t = 100
fValues = []

def f(x, y):
  return (x**2) * np.sin(4*np.pi*x) - y*np.sin(4*np.pi*y + np.pi) + 1
def P(i, j):
    fi = f(i[0], i[1])
    fj = f(j[0], j[1])
    return np.exp(-(fi - fj) / t)

def perturb(x, xl, xu, sig):
  x_cand = x + np.random.normal(loc=0, scale=sig)
  for i in range(x.shape[0]):
    if (x_cand[i] < xl[i]):
      x_cand[i] = xl[i]
    if (x_cand[i] > xu[i]):
      x_cand[i] = xu[i]
  return x_cand


def escalona(t):
  return t * 0.99
  
x_l = [-1, -1]
x_u = [2, 2]
xBest = np.random.uniform(low=x_l, high=x_u)
fBest = f(xBest[0], xBest[1])
i = 0

while i < nMax:
  n = np.random.normal(0, stdDev)
  xCand = perturb(xBest, x_l, x_u, stdDev)
  fCand = f(xCand[0], xCand[1])
  if (fCand < fBest):
    xBest = xCand
    fBest = fCand
  elif (P(xCand, xBest) >= np.random.uniform(0, 1)):
    xBest = xCand
    fBest = fCand
  fValues.append(fBest)
  i = i + 1
  t = escalona(t)


x_axis = np.linspace(-1, 2, 1000)
plt.plot(x_axis, fValues)
plt.show()

bp = 1