# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

#hrs = input("Enter Hours:")
#h = float(hrs)

horas = float(input("¿Cuantas horas?: "))
tasa_de_pago = float(input("¿Cuál es la tasa de pago?: "))
if horas > 40.0:
    con_el_tiempo = float(horas) - 40.0;
else:
    con_el_tiempo = float(0)
if horas > 40.0:
    pago = (40.0 * tasa_de_pago) + (con_el_tiempo * tasa_de_pago * 1.5)
else:
    pago = (horas * tasa_de_pago)
print(pago)
