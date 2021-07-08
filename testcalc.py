import calc
my_sign = input("What's your zodiac sign? ")
partner_sign = input("What's your partner's zodiac sign? ")
my_name = input("What's your name? ")
partner_name = input("What's your partner's name? ")
total = 0
total+=calc.my_zodiac(my_sign, partner_sign)
total+=calc.my_name(my_name, partner_name)
print(total)