import os
from playsound import playsound
class champion:
    #Lets first import the colours to make some text more expressive
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()
    patchVersion = None
    def main():
        # Main method
        print("Welcome to the champion counter picker!")
        playsound('audio/neverUnderestimate.mp3')
        print("You will have to remind me of a new patch though...")
        #Intro text
        champion.patchChecker()
        #Check if we are up to date with patches
        while(True):
            print("Options : [Counter Input : 1] [Counter finder : 2] [Change Patch Version : 3] [Quit : 4 ]")
            userInput = input("What would you like to do ? : ")
            if (userInput == "1"):
                champion.counter() # Needs to be complete
            elif(userInput == "2"):
                champion.counterFinder() # Not started
            elif(userInput == "3"):
                champion.patchChecker() # Done
            elif(userInput == "4"):
                playsound('audio/hut234.mp3')
                exit() # Done

    def counterFinder():
        findChampion = input("Who do you need to find a counter for ?")
        try:
            counterFinder = open(f"internal/patch/{champion.patchVersion}/{findChampion}/counter.txt","r")
            lineReader = counterFinder.readlines()
            lineReader = champion.endChopper(lineReader)
            os.system("cls")
            print(lineReader)

        except:
            print(f"There is no information on {findChampion}"
        )
    
    def endChopper(counterArray):
        for i in range(len(counterArray)):
            counterArray[i] = counterArray[i][:-1]
        return counterArray


    def counter():
        #Counter inputter into file directory
        myChampion =input("What champion did you play ? : ").lower()
        enemyChampion = input("What champion did you vs ? :").lower()
        boolWOL = input("Did you win or lose ? :" ).lower()
        if(boolWOL != "win" or boolWOL != "lose"):
            print(f"{boolWOL} is an invalid input")
            champion.counter()
        if(boolWOL == "lose"):  
            playsound('audio/DatsGottaSting.mp3')
        if(os.path.exists(f"internal/patch/{champion.patchVersion}/{myChampion}/counter.txt")):
            championCounter = open(f"internal/patch/{champion.patchVersion}/{myChampion}/counter.txt","a")
            print("Opening file")
            print("File has been written!")
        else:
            os.mkdir(f"internal/patch/{champion.patchVersion}/{myChampion}")
            championCounter = open(f"internal/patch/{champion.patchVersion}/{myChampion}/counter.txt","x")
            print("Creating a new file")
        championCounter.write(f"{myChampion}-{enemyChampion}-{boolWOL}")
        championCounter.write("\n")
        championCounter.close()
    def patchChecker():
        #Open patch.txt and print patch version
        patch = open("internal/patch.txt","r")
        champion.patchVersion = patch.readline()
        print(f"Is the current version still => {champion.Fore.RED}{champion.patchVersion}{champion.Style.RESET_ALL}?")
        patch.close()
        #Ask user if this is the correct patch or not
        val = input("yes or no ?: ")
        if(val == "yes"):
            print(f"Continuing with patch {champion.patchVersion}")
            playsound('audio/reportingIn.mp3')
        elif(val == "no"):
            try: 
                newVersion = float(input("What version are we currently on ? : "))
                playsound('audio/YesSir.mp3')
            except:
                print("Invalid input")
                champion.patchChecker()
            newVersion = str(newVersion)
            patch = open("internal/patch.txt","w")
            patch.write(newVersion)
            champion.patchVersion = newVersion
            patch.close()
        patch = open("internal/patch.txt","r")
        print(f"PATCH VERSION : {champion.Fore.GREEN}{patch.readline()}{champion.Style.RESET_ALL} ")

champion.main()
    
