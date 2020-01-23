import json
import operator
from collections import defaultdict 
import itertools

# Function to load file source_file_2.json from disk
def loadJsonFile(pathFile):
    with open (pathFile) as f:
        data = json.load(f)
        #sort data from key 'priority'
        data.sort(key=operator.itemgetter('priority'))

    return data

# Function to write json file to disk
def writeJsonFileManagers(dictionaryTasks, pathJsonFile):
    with open(pathJsonFile, 'w') as jsonFile:
        # Formating structure of json file
        json.dump(dictionaryTasks, jsonFile, indent = 4)
    jsonFile.close()

    return

# Function to get dics from each key
def getValues(data):
    listNames = list()
    listManagers = list()
    listWatchers = list()
    listPriority = list()
    # Iterate into data to search keys
    for i in range(len(data)):
        for key, value in data[i].items():
            if key == 'name':
                listNames.append(value)
            elif key == 'managers':
                listManagers.append(value)
            elif key == 'watchers':
                listWatchers.append(value)
            elif key == 'priority':
                listPriority.append(value)

    return listNames, listManagers, listWatchers, listPriority

# Function to organize each task according to their managers or watchers
def organizeTasksManagers(listNames, listManagers):
    listDictManagers = list()

    for managers, names in zip(listManagers, listNames):
        dictManagers = dict.fromkeys(managers, names)
        #If one manager or watchers per task
        if len(dictManagers.items()) == 1:
            listDictManagers.append(dictManagers)
        else :
            for key, value in dictManagers.items():
                dictManager = {key : value}
                listDictManagers.append(dictManager)

    return listDictManagers

# Function to group the keys (managers or watchers)
# according to their respective priority tasks
def groupingDictionaryTasks(listDictManagers):
    dictionaryTasks = defaultdict(list)

    for managers in listDictManagers:
        for key, value in managers.items():
            dictionaryTasks[key].append(value)

    return dictionaryTasks

# Function Main
def main():
    # Path to input json file
    pathFile = './source_file_2.json' 
    
    # Function call
    data = loadJsonFile(pathFile)

    # Function call
    listNames, listManagers, listWatchers, listPriority = getValues(data)
    
    # Function call
    listDictManagers = organizeTasksManagers(listNames, listManagers)
    
    # Function call
    dictionaryTasks = groupingDictionaryTasks(listDictManagers)
    
    # Name to write managers.json file into disk
    pathJsonFile = './managers.json'
    
    # Function call
    writeJsonFileManagers(dictionaryTasks, pathJsonFile)
    
    # Function call
    listDictWatchers = organizeTasksManagers(listNames, listWatchers)
    
    # Function call
    dictionaryTasks = groupingDictionaryTasks(listDictWatchers)
    
    # Name to write watchers.json file into disk
    pathJsonFile = './watchers.json'
    
    # Function call
    writeJsonFileManagers(dictionaryTasks, pathJsonFile)

if __name__ == '__main__':
    main()
