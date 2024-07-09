# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

temp_f = float(input ("What is the temperature in Fahrenheit? "))
temp_c = (temp_f-32) * 5/9
print (temp_f,"degrees Fahrenheit is equal to",temp_c,"degrees Celsius.")
