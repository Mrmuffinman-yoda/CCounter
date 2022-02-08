import os
class champion:
    #Lets first import the colours to make some text more expressive
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()
    patchVersion = None
    def main():
        # Main method
        turner = True
        #Check if user wants to stay in the while loop
        print("Welcome to the champion counterpicker!")
        print("You will have to remind me of a new patch though...")
        #Intro text
        champion.patchChecker()
        #Check if we are up to date with patches
        while(turner):
            print("Options : [Counter Input : 1] [Counter finder : 2] [Change Patch Version : 3] [Quit : 4 ]")
            userInput = input("What would you like to do ? : ")
            if (userInput == "1"):
                champion.counter() # Needs to be complete
            elif(userInput == "2"):
                champion.counterFinder() # Not started
            elif(userInput == "3"):
                champion.patchChecker() # Done
            elif(userInput == "4"):
                exit() # Done

    def counterFinder():
        # Needs to be complete
        return None
    def counter():
        #Counter inputter into file directory
        myChampion =input("What champion did you play? : ")
        enemyChampion = input("What champion did you vs? :")
        boolWOL = input("Did you win or lose ? :" )
        os.mkdir(f"internal/patch/{champion.patchVersion}/{myChampion}")
        championCounter = open(f"internal/patch/{champion.patchVersion}/{myChampion}/counter.txt","x")

    def patchChecker():
        #Open patch.txt and print patch version
        patch = open("internal/patch.txt","r")
        champion.patchVersion = patch.readline()
        print(f"Is the current version still => {champion.Fore.RED}{champion.patchVersion}{champion.Style.RESET_ALL}?")
        patch.close()
        #Ask user if this is the correct patch or not
        val = input("yes or no ?: ")
        # match val:
        #     case "yes":
        #         print(f"Continuing with patch{patch}")
        #     case "no":
        #         newVersion = input("What version are we currently on ?")
        #         patch.open(".internal/patch.txt","w")
        #         patch.write(newVersion)
        #         patch.close()
        if(val == "yes"):
            print(f"Continuing with patch{patch}")
        elif(val == "no"):
            try: 
                newVersion = int(input("What version are we currently on ? : "))
            except:
                print("Invalid input")
                champion.patchChecker()
            newVersion = str(newVersion)
            patch = open("internal/patch.txt","w")
            patch.write(newVersion)
            champion.patchVersion = newVersion
            patch.close()
        patch = open("internal/patch.txt","r")
        print(f"Changing patch version to {champion.Fore.GREEN}{patch.readline()}{champion.Style.RESET_ALL} ")

champion.main()
    
