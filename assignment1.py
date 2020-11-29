# Intro to Programming Using Python - Assignment #1
# Completed by: Rene Keller

# 1. Print out the following text:
# You've reached [your name].
# I'm not available right now, so leave a message and I'll call you back.
print ("\nExercise 1")
print ("You have reached Rene")
print ("I'm not available right now, so leave a message and I'll call you back.")

# 2. Create five variables for your first name, last name, shoe size, height, and age.
# And then print them out on one line.
print ("\nExercise 2")
my_first_name = "Rene"
my_last_name  = "Keller"
my_shoe_size  = 13
my_height     = "6 feet 4"
my_age        = 56

print(f"Here are my details: my name is {my_first_name} {my_last_name}, my shoe size is {my_shoe_size}, I am {my_height} tall and {my_age} old")

# 3. If subtotal = 10.58 and tip = 0.22 (22%) then calculate the total bill amount
# in a variable named total and print it out.
print ("\nExercise 3")
subtotal = 10.58
tip_percentage = 0.22
total = (subtotal * (tip_percentage+1))

print(f"The total amount including tip is ${total:.2f}")

# 4. Convert 158.8 into an integer.
# Convert 75 into a float.
# Convert "244.9" into a float and then an integer.
print ("\nExercise 4")
number1 = 158.8
number2 = 75
number3 = 244.9
float_number3 = float(number3)

print(f"conversion of {number1} into integer: {int(number1)}")
print(f"conversion of {number2} into float: {float(number2)}")
print(f"conversion of {number3} into float: {float_number3} and into back into integer {int(float_number3)}")

# 5. Use \t and \n in a string and then print it out so that it matches (approximately) the following:
# -in the woods
#               which
#                   stutter
#                           and
#
#                               sing
print ("\nExercise 5")
string_exercise = "-in the woods \n\t\twhich\n\t\t    stutter\n\t\t\t    and\n\n\n\t\t\t\tsing"
print(f"{string_exercise}")

# 6. Put your first name and total from above into an f-string (f"...") so that it reads:
# Mattan, your total is $12.91
# (remember to round the total to the nearest cent)
print ("\nExercise 6")
print(f"{my_first_name}, your total is ${total:.2f}")

# 7. Use input() to ask a user for the city they live in, and then print it back to them.
print ("\nExercise 7")
my_city = input("in which city do you live? ")
print(f"{my_city} is a beautiful place")

# 8. Build a future value calculator by using input() to get values from the user.
# (Make sure you convert them into integers or floats before doing any math on them.)
# Print out the result.
# Hint: Future Value = Present Value x (1 + rate of return) ^ number of periods
print ("\nExercise 8")
present_value = int(input("what is the present value? "))
rate_of_return = int(input("what is the rate of return in %? "))
no_of_periods = int(input("how many periods? "))

future_value = (present_value * (1.0 + (rate_of_return/100)) ** no_of_periods)

print(future_value)
