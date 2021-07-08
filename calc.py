def name(my_name, partner_name):
    count = 0 
    my_name = my_name.casefold()
    partner_name = partner_name.casefold()
    if(len(my_name)==len(partner_name)):
        count+=.5
    my_vowels = 0
    partner_vowels = 0
    for vowel in "aeiou":
        my_vowels+=my_name.count(vowel)
        partner_vowels+=partner_name.count(vowel)
    if(partner_vowels==my_vowels):
        count+=.5
    return count
def age(my_age, partner_age):
    count = 0
    my_age = int(my_age)
    partner_age = int(partner_age)
    gap = abs(my_age - partner_age)
    if gap == 0:
        count+=1
    elif gap == 1:
        count+=.75
    elif gap == 2:
        count+=.5
    elif gap == 3:
        count+=.25
    return count
def fav_color(my_color, partner_color):
    count = 0
    my_color = my_color.casefold()
    partner_color = partner_color.casefold()
    if my_color == partner_color:
        count+=1
    return count
def fav_candy(my_candy, partner_candy):
    count = 0
    my_candy = my_candy.casefold()
    partner_candy = partner_candy.casefold()
    if my_candy == partner_candy:
        count+=1
    return count
def fav_icecream(my_ic, partner_ic):
    count = 0
    my_ic = my_ic.casefold()
    partner_ic = partner_ic.casefold()
    if my_ic == partner_ic:
        count+=1
    return count
def my_zodiac(my_sign, partner_sign):
    aries = {"aries":1, "leo":1, "sagittarius":1, "taurus":0, "virgo":.75, "capricorn":0, "gemini":1, "libra":1, "aquarius":1, "cancer":0, "scorpio":0, "pisces":.75}
    leo = {"aries":1, "leo":1, "sagittarius":1, "taurus":.75, "virgo":0, "capricorn":0, "gemini":1, "libra":1, "aquarius":.75, "cancer":.75, "scorpio":.75, "pisces":.75}
    sagittarius = {"aries":1, "leo":1, "sagittarius":1, "taurus":0, "virgo":0, "capricorn":0, "gemini":1, "libra":1, "aquarius":1, "cancer":.75, "scorpio":.75, "pisces":.75}
    taurus = {"aries":0, "leo":.75, "sagittarius":0, "taurus":1, "virgo":1, "capricorn":1, "gemini":0, "libra":.75, "aquarius":0, "cancer":1, "scorpio":1, "pisces":1}
    virgo = {"aries":0, "leo":.75, "sagittarius":0, "taurus":1, "virgo":1, "capricorn":1, "gemini":0, "libra":0, "aquarius":.75, "cancer":1, "scorpio":1, "pisces":.75}
    capricorn = {"aries":0, "leo":.75, "sagittarius":0, "taurus":1, "virgo":1, "capricorn":1, "gemini":0, "libra":75, "aquarius":0, "cancer":1, "scorpio":1, "pisces":1}
    gemini = {"aries":1, "leo":1, "sagittarius":.75, "taurus": 0, "virgo": .75, "capricorn": .75, "gemini":1, "libra":1, "aquarius":1, "cancer":0, "scorpio":0, "pisces":0}
    libra = {"aries":.75, "leo":1, "sagittarius":1, "taurus": .75, "virgo": 0, "capricorn": 0, "gemini":1, "libra":1, "aquarius":1, "cancer":0, "scorpio":0, "pisces":.75}
    aquarius = {"aries":1, "leo":1, "sagittarius":1, "taurus": 0, "virgo": 0, "capricorn": 0, "gemini":1, "libra":1, "aquarius":1, "cancer":0, "scorpio":.75, "pisces":.75}
    cancer = {"aries":0, "leo":.75, "sagittarius":.75, "taurus": 1, "virgo": 1, "capricorn": 1, "gemini":0, "libra":0, "aquarius":0, "cancer":1, "scorpio":1, "pisces":1}
    scorpio = {"aries":.75, "leo":.75, "sagittarius":0, "taurus": 1, "virgo": 1, "capricorn": 1, "gemini":0, "libra":0, "aquarius":0, "cancer":1, "scorpio":1, "pisces":1}
    pisces = {"aries":.75, "leo":.75, "sagittarius":.75, "taurus": 1, "virgo": .75, "capricorn": 1, "gemini":0, "libra":0, "aquarius":0, "cancer":1, "scorpio":1, "pisces":1}
    my_sign = my_sign.casefold()
    partner_sign = partner_sign.casefold()
    if my_sign == "aries":
        return aries[partner_sign]
    elif my_sign == "leo":
        return leo[partner_sign]
    elif my_sign == "sagittarius":
        return sagittarius[partner_sign]
    elif my_sign == "taurus":
        return taurus[partner_sign]
    elif my_sign == "virgo":
        return virgo[partner_sign]
    elif my_sign == "capricorn":
        return capricorn[partner_sign]
    elif my_sign == "gemini":
        return gemini[partner_sign]
    elif my_sign == "libra":
        return libra[partner_sign]
    elif my_sign == "aquarius":
        return aquarius[partner_sign]
    elif my_sign == "cancer":
        return cancer[partner_sign]
    elif my_sign == "scorpio":
        return scorpio[partner_sign]
    elif my_sign == "pisces":
        return pisces[partner_sign]
    else:
        return "Error: the zodiac sign you entered does not exist!"