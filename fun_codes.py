
# MAXIMUN OF 2 NUMBERS
print ('MAXIMUN OF 2 NUMBERS ==>')
def maximum(a,b):
    if a>b:
        print(a,'is the biggest number')
    else:
        print(b,'is the biggest number')


maximum(6,7)


# FIZZ BUZZ
# Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.
print ('FIZZ BUZZ PROGRAM ==>')
def fb(num):
    if num%3==0 and num%5==0:
      print('FizzBuzz')
    elif num%3==0:
      print('Fizz')
    elif num%5==0:
      print('Buzz')
    else:
      print(num)

fb(90)

# SPEED
# Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”
print ('SPEED PROGRAM ==>')

def speed(s):
    d = 0
    if s<=70:
        print ("SPEED OK")
    if s>70:
        d = ((s-70) // 5)
        print('Demrit points: ',d)
        if d >= 12:
          print('Licanse is suspended')

speed(160)

# ShOW ODD EVEN NUMBERS
# Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

print ('EVEN/ODD Numbers ==>')

def showNumbers(limit):
  for i in range(0,limit+1):
   if i%2==0:
     print('EVEN')
   else:
     print('ODD')

showNumbers(10)

#Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
# For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.

print ('returns the sum of multiples of 3 and 5 between ==>')
def num(limit):
    sum = 0
    for i in range(0,limit+1):
      if i%3==0 or i%5==0:
          sum=i+sum
    print(sum)

num(20)

