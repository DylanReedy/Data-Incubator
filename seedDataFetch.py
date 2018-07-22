import requests, json, os.path

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
