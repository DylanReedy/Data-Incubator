import requests, json
import os.path

url = "https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches"
endurl = ".json"
baseFilename = "RiotData_json_"
allDataFilename = "AllData.json"
listOfFileNames=[]
allDataFiles=[]

def FetchDataFromRiotS3():
    for x in range(1, 11):
        finalurl = url + str(x) + endurl
        outfilename = baseFilename + str(x) + '.txt'
        if(os.path.isfile(outfilename)) :
            print("already have json data from web")
            return
        else:
            print("need json data from web")
            r = requests.get(finalurl)
            content = r.json()
            with open(outfilename, 'w') as outfile:
                json.dump(content, outfile)

def CombineFileNamesIntoArray():
    for x in range(1,11):
        print("combine " + str(x))
        listOfFileNames.append(baseFilename + str(x) + '.txt')        
       
def WriteRiotDataToFile(fileName):
    if(os.path.isfile(fileName)):
        print("file already exists")
        return
    else:
        CombineFileNamesIntoArray()
        with open(fileName, "w") as outfile:
            for filename in listOfFileNames:
                print("read file " + filename)
                with open(filename, 'rb') as inputFile:
                    file_data = json.load(inputFile)
                    allDataFiles.append(file_data)
            json.dump(allDataFiles, outfile)
            
def GetRiotData(fileName):
    with open(fileName) as json_file:
        data = json.load(json_file)
        return data

#
#head = []
#with open("result.json", "w") as outfile:
#    for f in file_list:
#        with open(f, 'rb') as infile:
#            file_data = json.load(infile)
#            head += file_data
#    json.dump(head, outfile)



#def CombineFiles():
#    for x in range(1,11):
#        listOfFileNames[x] = baseFilename + str(x) + '.txt'
#    for fileName in listOfFileNames:
#        with open(fileName, 'rb') as inputFile:
#            allDataFiles += json.load(inputFile)
#
#
#def LoadRiotDataFromFile():
#
#    with open('json_data\json1.txt') as json_file:
#        data = json.load(json_file)
#
#
            

#with open("AllData.json", "w") as outfile:
#    for f in listOfFileNames:
#        with open(f, 'rb') as infile:
#            file_data = json.load(infile)
#            allDataFiles += file_data
#    json.dump(allDataFiles, outfile)