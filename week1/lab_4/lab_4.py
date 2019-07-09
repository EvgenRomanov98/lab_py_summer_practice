def get_int_vlan_map():
    portsAccess = {}
    portsTrunk = {}
    with open("config_sw.txt") as configFile:
        i = 0
        configFileList = configFile.readlines()
        while i < len(configFileList):
            if configFileList[i].find("interface") != -1:
                numInterface = configFileList[i].replace("interface", "").strip()
                infoVLAN = configFileList[i + 1]
                if infoVLAN.find("trunk") != -1:
                    numVLAN = infoVLAN.split(" ")[-1].strip().split(",")
                    portsTrunk.update({numInterface: numVLAN})
                    i += 1
                elif infoVLAN.find("access") != -1:
                    numVLAN = infoVLAN.split(" ")[-1].strip().split(",")
                    portsAccess.update({numInterface: numVLAN})
                    i += 1
                else:
                    i += 1
            else:
                i += 1

        print("portsAccess = \n", portsAccess)
        print("portsTrunk = \n", portsTrunk)

get_int_vlan_map()
