# Simulate First and Follow sets for a given grammar

terminals = []
nonTerminals = []
productions = []

def readInput(fileName):
    with open(fileName, "r") as file:
        data = file.readlines()
        for line in data:
            splittedList = line.strip().split("->")
            nonTerminals.append(splittedList[0].strip())
        for line in data:
            splittedList = line.strip().split("->")
            for symbol in splittedList[1].strip().split(" "):
                if symbol != "|" and symbol != " " and symbol not in nonTerminals and symbol not in terminals:
                    terminals.append(symbol)
        for line in data:
            splittedList = line.strip().split("->")
            productions.append({
                "nonTerminal": splittedList[0].strip(),
                "productions": splittedList[1].strip().split(" | ")
            })

def findFirst(symbol, first):
    for production in productions:
        if production["nonTerminal"] == symbol:
            for prod in production["productions"]:
                sym = prod.split(" ")
                for i in sym:
                  if i in terminals:
                    first.append(i)
                  else:
                    findFirst(i,first)
                  break
    return set(first)

readInput("input.txt")
print("Productions:")
for prod in productions:
   print(prod["nonTerminal"], "->", " | ".join(prod["productions"]))
print()
print("Terminals:", terminals)
print()
print("Non Terminals:",nonTerminals)
print()
firsts = []
for i in nonTerminals:
  first = findFirst(i,[])
  firsts.append({
      "nonTerminal": i,
      "first": first
  })
  print(f"First of {i} is", first)

def findFollow(initialSymbol, symbol, follow):
  if productions[0]["nonTerminal"] == symbol and follow == []:
    follow.append("$")
  for production in productions:
    for prod in production["productions"]:
      sym = prod.split(" ")
      for e in sym:
        if e == symbol:
          ind = sym.index(e)
          if(len(sym) > ind + 1):
            myElem = sym[sym.index(e)+1]
            if myElem in terminals:
              follow.append(myElem)
              break
            else:
              firsts = findFirst(myElem,[])
              for first in firsts:
                if first != "#" and first not in follow:
                  follow.append(first)
                elif first == "#":
                  elemFollow = findFollow(symbol, production["nonTerminal"], [])
                  for i in elemFollow:
                    if i not in follow:
                      follow.append(i)
          else:
            if production["nonTerminal"] != symbol and production["nonTerminal"] != initialSymbol:
              elemFollow = findFollow(symbol, production["nonTerminal"], [])
              for i in elemFollow:
                if i not in follow:
                  follow.append(i)
              break
  return set(follow)

follows = []
print()
for i in nonTerminals:
  follow = findFollow(i, i, [])
  follows.append(follow)
  print(f"Follow of {i} is", follow)