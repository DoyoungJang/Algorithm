

count = int(input(""))
stringResult = []

for mainIterate in range(count):

    number = int(input(""))
    number2 = input("")

    if number >= 0:
        if number <= 1000:

            stringEven = ""
            stringOdd = ""
            arrayNumber = []
            arrayStringEven = []
            array = number2.split()
            resultTotal = 0

            for j in range(9):
                resultTotal = resultTotal + int(array[j])

            if resultTotal <= number:
                stringResult.append("YES")

            if resultTotal > number:
                stringResult.append("NO")

for iterate in range(len(stringResult)):
    print(stringResult[iterate])