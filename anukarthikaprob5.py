#programto find if a triangle is possible or not
AB=int(input("enter the side1 of the triangle:"))
BC=int(input("enter the side2 of the triangle:"))
CA=int(input("enter the side3 of the triangle:"))
if(AB<BC+CA and BC<AB+CA and CA<AB+BC):
  print("triangle is possible!!")
else:
  print("triangle is not possible!!")
