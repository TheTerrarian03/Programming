conversionList = {
    " ": "000",
    "s": "001",
    "e": "010",
    "n": "011",
    "k": "100",
    "o": "101",
    "a": "110",
    "!": "111"
}

strText = "senko san!"
strBinSpcs = "001 010 011 100 101 000 001 110 011 111"
strBinNorm = "001010011100101000001110011111"


def convText():
    end_product = []

    for i in strText:
        for e in conversionList:
            if i == e:
                end_product.append(conversionList.get(e))

    print()
    print(*end_product, sep="")
    print(*end_product, sep=" ")


def convBin(fromList, spcsVal):
    end_product = []

    def convert(list):
        new = ""
        for x in list:
            new += x
        return new

    i = 0
    while i <= len(fromList):
        try:
            temp_list = []
            for _ in range(3):
                temp_list.append(fromList[i])
                i += 1
            if spcsVal:
                i += 1

            for key, value in conversionList.items():
                if convert(temp_list) == value:
                    end_product.append(key)
        except IndexError:
            break

    print(fromList)
    print(*end_product, sep="")


uI1 = input("Text or Binary: ")
if uI1.lower() == "text":
    convText()
if uI1.lower() == "binary":
    uI2 = input("Spaces present? (y/n): ")
    if uI2.lower() == "y":
        convBin(strBinSpcs, True)
    else:
        convBin(strBinNorm, False)
