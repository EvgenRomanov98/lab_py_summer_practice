def func_accounting():
    selectiveAccountingDict = {"район1": {"кол-во избирателей": 5, "кол-во участков": 20, "площадь района": 3},
                           "район2": {"кол-во избирателей": 10, "кол-во участков": 25, "площадь района": 4},
                           "район4": {"кол-во избирателей": 20, "кол-во участков": 30, "площадь района": 7},
                           "район3": {"кол-во избирателей": 40, "кол-во участков": 35, "площадь района": 8},
                           "район5": {"кол-во избирателей": 80, "кол-во участков": 40, "площадь района": 10}}

    print(selectiveAccountingDict["район1"])
    print(selectiveAccountingDict["район1"]["кол-во избирателей"])
    
    print(selectiveAccountingDict.get("район6", 'No key'))
    
    for key in sorted(selectiveAccountingDict):
        print("selectiveAccountingDict['{0}']={1}".format(key, selectiveAccountingDict[key]))
        
func_accounting()
        
