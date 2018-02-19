number = int(input(""))
stringResult = []

if number > 0:
    if number <= 10:
        for i in range(number):
            textString = input("")
            stringEven = ""
            stringOdd = ""
            arrayNumber = []
            arrayStringOdd = []
            arrayStringEven = []

            if len(textString)<=100:
                for j in range(len(textString)):
                    if j % 2 == 0:
                        arrayStringEven.append(textString[j])
                        stringEven = stringEven + arrayStringEven[j // 2]

                    if j % 2 != 0:
                        arrayStringOdd.append(textString[j])
                        stringOdd = stringOdd + arrayStringOdd[j // 2]

                stringResult.append(stringEven + stringOdd)

        for iterate in range(len(stringResult)):
            print(stringResult[iterate])


test1 = []

test1.append(1)
test1.append("2")

print(test1)
