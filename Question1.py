print("The Patient's Portal")

# Dentist options amount variables.
optionA = 250
optionB = 50
optionC = 100
optionD = 150
optionE = 75

# Total variable
total = 0
cO = ''

# advanced payment
advanced = False

while cO != 'a' and cO != 'b' and cO != 'c' and cO != 'd' and cO != 'e':
    # Menu choices
    print("Please select the service you would like to come in for.\n"
          "A)Root Canal Therapy\n"
          "B)Oral Hygiene Check\n"
          "C)Emergency Injury Treatment\n"
          "D)Post-Procedure Check-up\n"
          "E)Routine Check-ups and Consultation")
    chosenOption = str(input("Please choose one: "))
    cO = chosenOption.lower()

print('You chose ', cO)

if cO == 'a':
    total = optionA
elif cO == 'b':
    total = optionB
elif cO == 'c':
    total = optionC
elif cO == 'd':
    total = optionD
elif cO == 'e':
    total = optionE

print('Your total is $', total)
adv = ''
while adv != 'y' and adv != 'n':
    print("Did you know? Book in advance and get 50% off!")
    adv = str(input("Would you like to pay today? [y/n]: "))
    adv = adv.lower()

if adv == 'y':
    total = 0.5 * total
    print("Your total payable is $", total)
else:
    total = total
    print("Your total payable after the service is $", total)

print("Have a smiling day!")
