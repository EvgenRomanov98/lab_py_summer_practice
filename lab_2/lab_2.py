#работа со словарями

selectiveAccountingDict = {"район1": {"кол-во изберателей": 5, "кол-во участков": 20, "площадь района": 3},
                           "район2": {"кол-во изберателей": 10, "кол-во участков": 25, "площадь района": 4},
                           "район4": {"кол-во изберателей": 20, "кол-во участков": 30, "площадь района": 7},
                           "район3": {"кол-во изберателей": 40, "кол-во участков": 35, "площадь района": 8},
                           "район5": {"кол-во изберателей": 80, "кол-во участков": 40, "площадь района": 10}}

print(selectiveAccountingDict["район1"])
print(selectiveAccountingDict["район1"]["кол-во изберателей"])

print(selectiveAccountingDict.get("район6", 'No key'))

for key in sorted(selectiveAccountingDict):
    print("selectiveAccountingDict['{0}']={1}".format(key, selectiveAccountingDict[key]))

#работа с множествами

firstLostOf = {1, 2, 25, 667, 65441}
secondLostOf = {1, 2, 2888, 6121, 65441, 668, 54546}

print(secondLostOf - firstLostOf) # елементи, що входять до 2 але не входять до 1

