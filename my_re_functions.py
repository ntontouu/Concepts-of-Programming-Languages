import re

#ΔΙΑΒΆΖΕΙ ΚΑΙ ΕΠΙΣΤΡΕΦΕΙ ΤΑ ΠΕΡΙΕΧΟΜΕΝΑ ΕΝΟΣ ΑΡΧΕΙΟΥ
def getFileContent(filename):
    f = open(filename, "r")
    s = f.read()
    return s

#ΕΠΙΣΤΡΕΦΕΙ ΤΑ ΔΕΔΟΜΕΝΑ ΠΟΥ ΚΑΘΟΡΙΖΕΙ ΤΟ PREFIX ΑΠΟ ΤΟ ΚΕΙΜΕΝΟ TEXT
def getElement(prefix, text):
    if prefix == "Moves":
        pattern = r'(\d+\.)'
        m = re.findall(pattern, text)
    else:
        pattern = r''+prefix+' "(\S|\s)*"'
        m = re.search(pattern, text)
    if m!=None:
        if prefix != "Moves": 
            txt = m.group()
            x = re.split("\s", txt)
        
        if prefix == "Result":
            y = re.split("\s",x[1])
            y = re.sub('"','',y[0])
            y = re.sub('1/2','0.5',y)
            y = re.split("-",y)
            return y
        elif prefix == "White":
            x = " ".join(x[1:])
            x = re.sub(","," ",x)
            return x
        elif prefix == "Black":
            x = " ".join(x[1:])
            x = re.sub(","," ",x)
            return x
        elif prefix == "BlackElo":
            return re.sub('"','',x[1])
        elif prefix == "WhiteElo":
            return re.sub('"','',x[1])
        elif prefix == "Date":
            x = re.sub('"','',x[1])
            d = re.split("\\.",x)
            return d[2]+"-"+d[1]+"-"+d[0]
        elif prefix == "Moves":
            return len(m)
    return ""

#ΕΠΙΣΤΡΕΦΕΙ ΕΝΑ DICTIONARY ME ΤΙΣ ΠΛΗΡΟΦΟΡΙΕΣ ΤΗΣ ΠΑΡTIΔΑΣ GAME
def gameInfo(game):
    info = dict()
    
    moves = getElement("Moves",game['data'])
    info['moves'] = moves;
    
    for m in game['metadata']:
        result = getElement("Result",m)
        playerWhite = getElement("White",m)
        whiteElo = getElement("WhiteElo", m)
        blackElo = getElement("BlackElo", m)
        playerBlack = getElement("Black",m)
        date = getElement("Date",m)
        if len(result)>0:
            info['result'] = result
        if len(playerWhite)>0:
            info["White"]=playerWhite
        if len(playerBlack)>0:
            info["Black"]=playerBlack
        if len(whiteElo)>0:
            info["WhiteELO"]=whiteElo
        if len(blackElo)>0:
            info["BlackELO"]=blackElo
        if len(date)>0:
            info["Date"]=date
    result = info['result']
    try:
        if float(result[0]) > float(result[1]):
            info['winner'] = "Black"
        elif float(result[0]) == float(result[1]):
            info['winner'] = "Draw"
        else:
            info['winner'] = "White"
    except:
        info['winner']="-"
    try:
        dif = float(info['WhiteELO']) - float(info['BlackELO'])
    except:
        dif=0
    if dif < 0:
        info['difference'] = "Black is "+str(abs(dif))+" better than White"
    elif dif > 0:
        info['difference'] = "White is "+str(abs(dif))+" better than Black"
    else:
        info['difference'] = "White and Black are equals"    
    return info    

def readGames(filename, t="file", returnText=False):
    #ΔΙΑΒΑΖΕΙ ΤΟ ΑΡΧΕΙΟ ΜΕ ΤΙΣ ΠΑΡΤΙΔΕΣ
    if t=="file":
        text = getFileContent(filename)
    else:
        text = filename
    #ΠΙΝΑΚΑΣ ΜΕ ΤΑ METADATA ΤΩΝ ΠΑΙΧΝΙΔΙΩΝ
    introduction = []
    #ΛΑΜΒΑΝΟΝΤΑΙ ΟΙ ΓΡΑΜΜΕΣ ΜΕ ΤΑ METADATA
    for line in text.split("\n"):
            introduction.append(line)
    #ΑΠΟ ΤΙΣ ΓΡΑΜΜΕΣ ΤΩΝ METADATA ΔΗΙΟΥΡΓΕΙΤΑΙ Η ΛΙΣΤΑ ΜΕ ΤΑ METADATA
    first = True
    n = []
    introductions = []
    for i in introduction:
        if re.match(r'(\[Event\s.*)',i):
            if len(n)>0 and first == False:
                introductions.append(n)
            if first == True:
                first = False
            n = []
            n.append(i)
        else:
            n.append(i)
    introductions.append(n)
    if returnText:
        return introductions
    #ΔΗΜΙΟΥΡΓΕΊΤΑΙ Ο ΠΙΝΑΚΑΣ ΜΕ ΤΙΣ ΚΙΝΗΣΕΙΣ
    partides = []
    for line in text.split("\n"):
        if not re.match(r'(\[\w+\s.*)', line):
            partides.append(line)

    _partides = []
    s = ""
    for p in partides:
        if len(p) ==  0:
            _partides.append(s)
            s = " "
        else:
            s+=p
    partides = []

    for p in _partides:
        if len(p) > 1:
            partides.append(p.strip())
    #ΔΗΜΙΟΥΡΓΕΊΤΑΙ ΚΑΙ ΕΠΙΣΤΡΦΕΙ Η ΛΙΣΤΑ ΜΕ ΤΑ DICTIONARIES ΠΟΥ ΠΕΡΙΛΑΜΒΆΝΟΥΝ
    #ΤΙΣ ΚΙΝΗΣΕΙΣ ΚΑΙ ΤΑ METADATA ΤΩΝ ΠΑΡΤΙΔΩΝ 
    data = []
    for i,p in zip(introductions,partides):
        data.append({"metadata":i,"data":p})
    return data

def getInfoDicts(data):
    allGamesInfo = []
    for d in data:
        info = gameInfo(d)
        allGamesInfo.append(info)
    return allGamesInfo




def gameWinner(info):
    return info['winner']

def gameDate(info):
    return info['Date']

def gameDifference(info):
    return info['difference']

def gameMoves(info):
    return info['moves']


def gameWinnerFromText(text):
    data = readGames(text, t="string")
    gameInfo = getInfoDicts(data)
    return gameInfo[0]['winner']

def gameDateFromText(text):
    data = readGames(text, t="string")
    gameInfo = getInfoDicts(data)
    return gameInfo[0]['Date']


def gameMovesFromText(text):
    data = readGames(text, t="string")
    gameInfo = getInfoDicts(data)
    return gameInfo[0]['moves']

def gameDifferenceFromText(text):
    data = readGames(text, t="string")
    gameInfo = getInfoDicts(data)
    return gameInfo[0]['difference']