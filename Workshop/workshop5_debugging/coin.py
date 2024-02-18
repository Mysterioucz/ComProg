# -*- coding: utf-8 -*-
import math

# find greatest common divisor
# of given inputs a and b
def gcd(a,b): 
  if(b==0): 
    return a
  elif a == 0:
    return b
  else:
    return gcd(b, a%b)


if __name__ == '__main__':
  # na : amount of coin_a
  # nb : amount of coin_b
  # find such a case that T = a*na + b*nb 
  # print na, nb if possible, else print IMPOSSIBLE

  print('Input: coin_a coin_b target_value')
  print('Input: ', end= '')
  a, b, T = [int(x) for x in input().split(' ')]

  # T cannot be composed by coin_a and coin_b 
  # if it cannot be divided by their greatest common divisor
  if(T % gcd(a, b) != 0):
    yes = False
  else:
    na = 0  
    yes = False
    while(not yes):
      try:
        if (T - a*na) % b == 0:
          nb = (T - a*na)/b
          yes = True
        else:
          na += 1
      except:
        nb = 0
        if (T - b*nb) % a == 0:
          na = (T - b*nb)/a
          yes = True
        else:
          nb += 1
    if na < 0 or nb<0:
      yes = False


  if(yes):
    print(f"na: {na}, nb: {nb}")
  else:
    print("IMPOSSIBLE")