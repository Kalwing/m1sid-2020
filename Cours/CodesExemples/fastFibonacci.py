def fib(n):
  if n<=1 :
    return 1
  else :
    f1=1
    f2=1
    for i in range(2,n+1):
       temp=f1+f2
       f1=f2
       f2=temp
    return f2
