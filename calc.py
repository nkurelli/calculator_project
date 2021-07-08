def my_name(my_name, partner_name):
    count = 0   
    if(len(my_name)==len(partner_name)):
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