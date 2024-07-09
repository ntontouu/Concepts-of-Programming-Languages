import sys
import my_re_functions as func

def main():
    data = func.readGames(sys.argv[1], t="file",returnText=True)
    for d in data:
        d = "\n".join(d)
        print(func.gameWinnerFromText(d))
        print(func.gameDateFromText(d))
        print(func.gameMovesFromText(d))
        print(func.gameDifferenceFromText(d))
        print("-----")

if __name__ == '__main__':
    main()