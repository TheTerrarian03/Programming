import pandas
import numpy


subredditsDict = {
    # "subreddit here": count of appearance
}
    
genresDict = {
    # "genre here": count of appearance
}
    
followedDict = {
    # "subreddit here": true/false for whether followed
}

infoDict = {
    "followed": 0,
    "ads": 0,
    "suggested": 0
}

### STEP 1 - READ DATA FILE LINES INTO LIST
dataFile = open("data.txt", "r")
fileLines = dataFile.readlines()
dataFile.close()

### STEP 2 - SETUP SMA CSV FILE
smaCSV = open("smaCSV.csv", "w")
# write header
smaCSV.write("Accounts I follow (don't actually know the person),Actual Friends & Family,Advertisements/Sponsored Content,Suggested Content/Accounts,Type of Content\n")

# MAX_ENTRIES = 30  # I collected more data than the 30, so this will cap info logged at 30 points
MAX_ENTRIES = -1

### STEP 3 - PARSE DATA - COLLECT TOTALS & WRITE TO SMA
for line in fileLines[:MAX_ENTRIES]:
    smaToWrite = ""

    # remove newline
    if line.endswith("\n"):
        line = line[:-1]
    
    # split by spaces
    lineSplit = line.split(" ")

    # get subreddit
    subreddit = lineSplit[0].lower()

    # look for subreddit vs ad
    if subreddit == "ad":
        infoDict["ads"] += 1
        smaToWrite = ",,✅,,N/A\n"
        smaCSV.write(smaToWrite)
        continue  # break because there are no more actions for ads
    else:
        genre = lineSplit[1].lower()
        if not subreddit in subredditsDict:
            subredditsDict[subreddit] = 0
        subredditsDict[subreddit] += 1
        if not genre in genresDict:
            genresDict[genre] = 0
        genresDict[genre] += 1

    # check for sub not registered in followed
    if not subreddit in followedDict:
        isFollowed = input(f"Is the subreddit: \"{subreddit}\" a followed subreddit? (y/N)\n$ ")
        if "y" in isFollowed.lower():
            followedDict[subreddit] = True
        else:
            followedDict[subreddit] = False
    
    # log followed/suggested
    if followedDict[subreddit]:
        infoDict["followed"] += 1
        smaToWrite = f"✅,,,,{genre}\n"
    else:
        infoDict["suggested"] += 1
        smaToWrite = f",,,✅,{genre}\n"
    
    smaCSV.write(smaToWrite)

# close sma file
smaCSV.close()

### STEP 4 - TOTALS FILE
# open
totalsTXT = open("Totals.txt", "w")

# writing
# txt 'accounts' header
totalsTXT.write("ACCOUNTS:\n")
# accounts
totalsTXT.write(f"Followed: {infoDict['followed']}\nSuggested: {infoDict['suggested']}\nAds: {infoDict['ads']}\n\n")
# genres
totalsTXT.write("GENRES:\n" + '\n'.join([f"{genre}: {count}" for genre, count in genresDict.items()]))

# close
totalsTXT.close()

### STEP 6 - CHAR CSV
# open
chartCSV = open("chartCSV.csv", "w")
GRAPH_SPACING = 19

# writing
# accounts
chartCSV.write(",".join(infoDict.keys()) + "\n")
chartCSV.write(",".join(str(num) for num in infoDict.values()) + "\n")
# spacing
chartCSV.write(",\n"*GRAPH_SPACING)
# genres
chartCSV.write(",".join(genresDict.keys()) + "\n")
chartCSV.write(",".join(str(num) for num in genresDict.values()) + "\n")
# spacing
chartCSV.write(",\n"*GRAPH_SPACING)
# subreddits
chartCSV.write(",".join(subredditsDict.keys()) + "\n")
chartCSV.write(",".join(str(num) for num in subredditsDict.values()) + "\n")

# close
chartCSV.close()
