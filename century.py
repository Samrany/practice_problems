def centuryFromYear(year):
    if year % 100 == 0:
       return year / 100

    else:
        return year // 100 + 1


def checkPalindrome(inputString):
    if inputString[::-1] == inputString:
        return True
    else:
        return False