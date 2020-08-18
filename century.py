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

def adjacentElementsProduct(inputArray):
    output_array = []
    for idx in range(len(inputArray)-1):
        output_array.append(inputArray[idx]*inputArray[idx+1])
    
    return max(output_array)