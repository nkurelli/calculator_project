import calc
my_name = input("Welcome to the Love Compatibility Calculator! \nWhat's your name? ")
partner_name = input("What's your partner's name? ")
my_age = input("How old are you? ")
partner_age = input(f"How old is {partner_name}? ")
my_sign = input("What's your zodiac sign? ")
partner_sign = input(f"What's {partner_name}'s zodiac sign? ")
print("LIST OF COLORS: {red, orange, yellow, green, blue, purple, pink, white, black, brown, grey")
my_color = input("Out of the above colors, what's your favorite? ")
partner_color = input(f"Out of the above colors, what's {partner_name}'s favorite? ")
print("LIST OF CANDY: {skittles, peanut butter cups, m&ms, starbursts, tootsie rolls, almond joy, hershey bar")
my_candy = input("Out of the above candies, what's your favorite? ")
partner_candy = input(f"Out of the above candies, what's {partner_name}'s favorite? ")
print("LIST OF FLAVORS: {vanilla, chocolate, cookies n' cream, mint chocolate chip, chocolate chip cookie dough, strawberry, rocky road")
my_ic = input("Out of the above flavors, what's your favorite? ")
partner_ic = input(f"Out of the above flavors, what's {partner_name}'s favorite? ")
total = 0
total+=calc.fav_color(my_color, partner_color)
total+=calc.my_zodiac(my_sign, partner_sign)
total+=calc.name(my_name, partner_name)
total+=calc.age(my_age, partner_age)
total+=calc.fav_icecream(my_ic, partner_ic)
total+=calc.fav_candy(my_candy, partner_candy)
var = "%"
print("You and "+partner_name+" are "+ str(total/6 * 100) + var + " compatible!")