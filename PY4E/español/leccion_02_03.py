# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.

# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25

horas = input("¿Cuantas horas?: ")
tasa_de_pago =input("¿Cuál es la tasa de pago?: ")
pago = float(horas) * float(tasa_de_pago)
print("Pago: ",pago)
