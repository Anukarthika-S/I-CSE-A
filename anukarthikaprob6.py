#program tofind the nth power is odd or even
num=int(input("enter the number:"))
power=int(input("enter the power of the number:"))
number=num**power
if(number%2==0):
  print("the nth powerof the number is even!!")
elif(number%!=0):
  print("the nth power of the number is odd!!")
else:
  print("invalid!!!")
