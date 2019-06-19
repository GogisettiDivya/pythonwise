
#project euler : 3
num = 600851475143
a = 0
b = 2
while b <= num:
  if num % b == 0:
    print(int(num),"is divisible,b")
    num = num / b
    a = b
  else:
    b = b + 1
print("The answer is the final :",a)

#projecteuler:4
#palindrome
palindrome = lambda num:str(num) == str(num)[::-1]
product = {i * j for i in range(100,1000) for j in range(100,1000)}
palindrome = filter(palindrome,product)
print(max(palindrome))

#project euler : 20
#factorial
import math
n = 100
fact = math.factorial(n)
res = [int(x) for x in str(fact)]
print(sum(res))

#project euler: 29
  print(sorted({a**b for a in range(2,101) for b in range(2,101)}))

#project euler:48
import math
n = int(input("enter the number"))
a = sum(list(pow(a,a) for a in range(1,11)))
print(str(a)[-10:])

#project euler: 16
import math
n = pow(2,1000)
l = [int(x) for x in str(n)]
print(sum(l))

#project euler : 2
def fibbo(max):
  s = [1,2]
  while sum(s[-2:]) < max:
      s.append(sum(s[-2:]))
  return sum([n for n in s if n%2 == 0])
print(fibbo(4000000))

#project euler : 1
limit = 1000
l = sum(filter(lambda x : x % 3 == 0 or x % 5 == 0,range(limit)))
print(l)

#project euler: 9
for a in range(1,1000):
  for b in range(1,1000):
    for c in range(1,1000):
      if((a < b < c) and (a + b + c == 1000) and (a*a + b*b == c*c )):
        print(a*b*c)

#project euler : 6
num = int(input("enter the number"))
l1 = sum([i*i for i in range(1,num + 1)])
s = sum([i for i in range(1,num + 1)])
l2 = s**2
print(l2-l1)

#project euler: 10
def is_prime(num):
    for i in range(2,round(num**0.5)+1):
        if num % i == 0:
            return False
    return True
prime_sum = 0
for i in range(2,2000000):
    if is_prime(i):
        prime_sum += i
print(prime_sum)

