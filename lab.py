
print("Rectangle Area Calculator")

# Taking input from the user for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculating the area
area = length * width

# Displaying the result
print("The area of the rectangle is:", area)

# Checking if the area is greater than 50
if area > 50:
    print("That's a large rectangle!")
else:
    print("That's a small rectangle!")

