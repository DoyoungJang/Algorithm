#variables
zero = "zero"
one = "one"
two = "two"
three = "three"
four = "four"
five = "five"
six = "six"
seven = "seven"
eight = "eight"
nine = "nine"


#fuction
def stringToNumber(text):
    if text == "zero":
        return 0
    if text == "one":
        return 1
    if text == "two":
        return 2
    if text == "three":
        return 3
    if text == "four":
        return 4
    if text == "five":
        return 5
    if text == "six":
        return 6
    if text == "seven":
        return 7
    if text == "eight":
        return 8
    if text == "nine":
        return 9
    if text == "ten":
        return 10

def randomNumberSelect(text):
    if len(text) == 3:#one,two,six
        if len("one") == len(text):
            oneText = text
            for i in range(len(oneText)):
                oneText = oneText.replace("o", "")
            for i in range(len(oneText)):
                oneText = oneText.replace("n", "")
            for i in range(len(oneText)):
                oneText = oneText.replace("e", "")
            if oneText == "":
                return 1

        if len("two") == len(text):
            twoText = text
            for i in range(len(twoText)):
                twoText = twoText.replace("t", "")
            for i in range(len(twoText)):
                twoText = twoText.replace("w", "")
            for i in range(len(twoText)):
                twoText = twoText.replace("o", "")
            if twoText == "":
                return 2

        if len("six") == len(text):
            sixText = text
            for i in range(len(sixText)):
                sixText = sixText.replace("s", "")
            for i in range(len(sixText)):
                sixText = sixText.replace("i", "")
            for i in range(len(sixText)):
                sixText = sixText.replace("x", "")
            if sixText == "":
                return 6

        if len("ten") == len(text):
            tenText = text
            for i in range(len(tenText)):
                tenText = tenText.replace("t", "")
            for i in range(len(tenText)):
                tenText = tenText.replace("e", "")
            for i in range(len(tenText)):
                tenText = tenText.replace("n", "")
            if tenText == "":
                return 10

    if len(text) == 4:#zero, four, five, nine
        if len("zero") == len(text):
            zeroText = text
            for j in range(len(zeroText)):
                zeroText = zeroText.replace("z", "")
            for j in range(len(zeroText)):
                zeroText = zeroText.replace("e", "")
            for i in range(len(zeroText)):
                zeroText = zeroText.replace("r", "")
            for i in range(len(zeroText)):
                zeroText = zeroText.replace("o", "")
            if zeroText == "":
                return 0


        if len("four") == len(text):
            fourText = text
            for i in range(len(fourText)):
                fourText = fourText.replace("f", "")
            for i in range(len(fourText)):
                fourText = fourText.replace("o", "")
            for i in range(len(fourText)):
                fourText = fourText.replace("u", "")
            for i in range(len(fourText)):
                fourText = fourText.replace("r", "")
            if fourText == "":
                return 4

        if len("five") == len(text):
            fiveText = text
            for i in range(len(fiveText)):
                fiveText = fiveText.replace("f", "")
            for i in range(len(fiveText)):
                fiveText = fiveText.replace("i", "")
            for i in range(len(fiveText)):
                fiveText = fiveText.replace("v", "")
            for i in range(len(fiveText)):
                fiveText = fiveText.replace("e", "")
            if fiveText == "":
                return 5

        if len("nine") == len(text):
            nineText = text
            for i in range(len(nineText)):
                nineText = nineText.replace("n", "")
            for i in range(len(nineText)):
                nineText = nineText.replace("i", "")
            for i in range(len(nineText)):
                nineText = nineText.replace("e", "")
            if nineText == "":
                return 9

    if len(text) == 5:  # three, seven, eight
        if len("three") == len(text):
            threeText = text
            for i in range(len(threeText)):
                threeText = threeText.replace("t", "")
            for i in range(len(threeText)):
                threeText = threeText.replace("h", "")
            for i in range(len(threeText)):
                threeText = threeText.replace("r", "")
            for i in range(len(threeText)):
                threeText = threeText.replace("e", "")
            if threeText == "":
                return 3

        if len("seven") == len(text):
            sevenText = text
            for i in range(len(sevenText)):
                sevenText = sevenText.replace("s", "")
            for i in range(len(sevenText)):
                sevenText = sevenText.replace("e", "")
            for i in range(len(sevenText)):
                sevenText = sevenText.replace("v", "")
            for i in range(len(sevenText)):
                sevenText = sevenText.replace("n", "")
            if sevenText == "":
                return 7

        if len("eight") == len(text):
            eightText = text
            for i in range(len(eightText)):
                eightText = eightText.replace("e", "")
            for i in range(len(eightText)):
                eightText = eightText.replace("i", "")
            for i in range(len(eightText)):
                eightText = eightText.replace("g", "")
            for i in range(len(eightText)):
                eightText = eightText.replace("h", "")
            for i in range(len(eightText)):
                eightText = eightText.replace("t", "")
            if eightText == "":
                return 8


def calculatorString(text, operand1, operand2):
    if text =="+":
        return operand1 + operand2
    if text =="-":
        return operand1 - operand2
    if text =="*":
        return operand1 * operand2
    if text =="/":
        return operand1 / operand2

#code
count = int(input(""))
operationResult = []

for mainIterate in range(count):
    operationStringArray = []
    operationIntArray = []

    operation = input("")

    operationStringArray = operation.split()
    operationIntArray.append(stringToNumber(operationStringArray[0]))
    operationIntArray.append(stringToNumber(operationStringArray[2]))
    operationIntResult = randomNumberSelect(operationStringArray[4])

    if operationIntResult == calculatorString(operationStringArray[1], operationIntArray[0],operationIntArray[1]):
        operationResult.append("Yes")
    else :
        operationResult.append("No")

for iterate in range(len(operationResult)):
    print(operationResult[iterate])

