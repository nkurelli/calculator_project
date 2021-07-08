import calc

my_name = input("What's your name? ")
partner_name = input("What's your partner's name? ")

my_sign = input("What's your zodiac sign? ")
partner_sign = input(f"What's {partner_name}'s zodiac sign? ")

print("LIST OF COLORS: {red, orange, yellow, green, blue, purple, pink, white, black, brown, grey")
my_color = input("Out of the above colors, what's your favorite? ")
partner_color = input("Out of the above colors, what's {partner_name}'s favorite? ")

total = 0
total+=calc.my_color(my_color, partner_color)
total+=calc.my_zodiac(my_sign, partner_sign)
total+=calc.my_name(my_name, partner_name)
print(total)