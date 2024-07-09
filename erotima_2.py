import sys
from datetime import datetime
import matplotlib.pyplot as plt
import my_re_functions as func

def getWeekDayNumber(s):
    datetime_object = datetime.strptime(s, '%d-%m-%Y')
    return int(datetime_object.strftime('%w'))


def main():
    

    data = func.readGames(sys.argv[1], t="file")

    allInfo = func.getInfoDicts(data)

    week = [0,0,0,0,0,0,0]
    days = ['ΚΥΡΙΑΚΗ','ΔΕΥΤΕΡΑ','ΤΡΙΤΗ','ΤΕΤΑΡΤΗ','ΠΕΜΠΤΗ','ΠΑΡΑΣΚΕΥΗ','ΣΑΒΒΑΤΟ']

    for a in allInfo:
        try:
            i = getWeekDayNumber(a['Date']);
            week[i]+=1
        except Exception as error:
            continue
    #dataset = []
    #for i in range(7):
        #dataset.append({days[i]:week[i]})
        

    plt.bar(days, week, color =['green','blue','orange','grey','black','yellow','purple'],  width = 0.9)
    plt.show()


if __name__ == '__main__':
    main()