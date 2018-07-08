#The purpose of this program is to calculate the area of triangle or a circle
print 'The Area Calculator have started'
print 'We will calculate the area of a circle or a triangle'
option = raw_input("Enter C for Circle or T for Triangle: ")
if option == 'C':
  radius = float(raw_input("Enter the radius: "))
  pi = 3.14159
  area = radius**2 * pi
  print 'The area of the circle is ' + str(area)
elif option == 'T':
  base = float(raw_input("Enter the base of the triangle: "))
  height = float(raw_input("Enter the height of the triangle: "))
  area = (base * height)/2
  print 'The are of the triangle is ' + str(area)
else:
  print 'Invalid input'
  
print "The program is ready to exit"
