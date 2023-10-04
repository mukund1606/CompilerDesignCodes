# Implement Symbol Table in Python


def getInput(filePath):
    with open(filePath) as f:
        content = f.read().replace("\n", "").split(";")
        return content


symbolTable = {}


def printTable(table):
    print("Symbol Table")
    print("Name\tType\t\tValue\t\tAddress")
    for key in table:
        print(key + "\t" + "\t\t".join(table[key]))


def main():
    myData = getInput("code.txt")
    for line in myData:
        lineData = line.replace("=", "").split(" ")

        if len(lineData) < 3:
            continue
        dType = lineData[0]
        varName = lineData[1]
        varValue = " ".join(lineData[2:])
        varAddress = hex(id(varValue))
        if symbolTable.get(varName) is None:
            symbolTable[varName] = [dType, varValue, varAddress]
        else:
            continue
    printTable(symbolTable)


if __name__ == "__main__":
    main()