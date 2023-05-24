#programtocalculate the surface areaand volume ofcylinder
radius=float(input("enter the radius of the cylinder:"))
pi=3.14
height=float(input("enter the heightof the cylinder:"))
volume=pi*radius*radius*height
area=(2*pi*radius*height)+(2*pi*radius*radius)
print("the volume of the cylinder is:",volume)
print("the surface areaof the cylinder is:",area)
