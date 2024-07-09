# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

temp_f = float(input ("¿Cuál es la temperatura en fahrenheit? "))
temp_c = (temp_f-32) * 5/9
print (temp_f,"grados fahrenheit es igual a",temp_c,"grados centígrados.")
