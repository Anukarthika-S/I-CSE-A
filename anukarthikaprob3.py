#program to calculate the wind chill index
temperature=float(input("enterthe temperature in degrees"))
velocity=float(input("enter the windspeed in kms per hour"))
chillIndex=13.12+(0.6215*temperature)-(11.37*(v**0.16))+(0.3965*t*(v**0.16))
chillIndex1=chillIndex//1
print("the wind chill index for the given data is:",chillIndex1)
