# Ian Bullard
# UWYO COSC 1010
# Submission Date 11/04/24
# Lab 08
# Lab Section: 14
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def check_type(string_to_check):
    returnvalue = False
    try:
        returnvalue = float(string_to_check)
        returnvalue = int(string_to_check)
    except:
        pass
    return returnvalue


print(check_type("x"))



print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, a, an):
    y_array = []
    if (check_type(m) and check_type(b) and check_type(a) and check_type(an)) == int:
        for x in range(a, an + 1):
            y = (m * x) + (b)
            y_array.append(y)
    else:
        m = int(m)
        b = int(b)
        a = int(a)
        an = int(an)
        for x in range(a, an):
            y = (m * x) + (b)
            y_array.append(y)
    return y_array

while True:
    a = input("Give me a lower x bound or enter exit to exit\n") # Clean these up using in behind each of these and putting them in the right order
    an = input("Give me an upper x bound or enter exit to exit\n")
    m = input("Give me a slope value or enter exit to exit\n")
    b = input("Give me the Y Intercept/b value or enter exit to exit\n")
    
    a = a.lower()
    an = an.lower()
    m = m.lower()
    b = b.lower()

    if a == "exit" or an == "exit" or m == "exit" or b == "exit":
        break
    else:
        print(slope_intercept(m, b, a, an))
    


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def quadratic_formula(a_quad, b_quad, c_quad):
    if (check_type(a_quad) and check_type(b_quad) and check_type(c_quad)) == int:    
        quad_sqrt = ((b_quad**2)- (4*(a_quad)*(c_quad)))
        if quad_sqrt < 0:
            return "Null"
        else:
            positive_solution = ((-b_quad) + (quad_sqrt) ** 0.5)/ (2*a_quad)
            negative_solution = ((-b_quad) - (quad_sqrt) ** 0.5)/ (2*a_quad)
            return positive_solution, negative_solution
            
    else:
        a_quad = int(a_quad)
        b_quad = int(b_quad)
        c_quad = int(c_quad)
        quad_sqrt = ((b_quad**2)- (4*(a_quad)*(c_quad)))
        if quad_sqrt < 0:
            return "Null"
        else:
            positive_solution = ((-b_quad) + (quad_sqrt) ** 0.5)/ (2*a_quad)
            negative_solution = ((-b_quad) - (quad_sqrt) ** 0.5)/ (2*a_quad)
            return positive_solution, negative_solution
    
while True:
    a_quad = input("Input an a value or enter exit to exit\n")
    b_quad = input("Input an b value or enter exit to exit\n")
    c_quad = input("Input an c value or enter exit to exit\n")

    if a_quad == "exit" or b_quad == "exit" or c_quad == "exit":
        break
    else:
        print(quadratic_formula(a_quad, b_quad, c_quad))
