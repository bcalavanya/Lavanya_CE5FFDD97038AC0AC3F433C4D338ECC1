# 1.1 implement a recursive function to calculate the factorial of a given number
1!=1*1
2!=2*1
3!=3*2*1
4!=4*3*2*1
5!=5*4*3*2*1
6!=6*5*4*3*2*1
7!=7*6*5*4*3*2*1
8!=8*7*6*5*4*3*2*1
9!=9*8*7*6*5*4*3*2*1
10!=10*9*8*7*6*5*4*3*2*1

def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)
    
number=int(input("Enter a value :"))
res = fact_rec(number)

print("The factorial of {} is {}.".format(number,res))