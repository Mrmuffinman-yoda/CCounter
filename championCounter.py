class champion:
    #Lets first import the colours to make some text more expressive
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()
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
            print("Options : [Counter : 1] [Quit : 2 ]")
            userInput = input("What would you like to do ? : ")
            if (userInput == "1"):
                champion.counter()
            elif(userInput == "2"):
                exit()

    def counter():
        #Counter inputter into file directory
        myChampion =input("What champion did you play? : ")
        enemyChampion = input("What champion did you vs? :")
        boolWOL = input("Did you win or lose ? :" )
        f = open(f"champions/{myChampion}.txt","x")

    def patchChecker():
        #Open patch.txt and print patch version
        patch = open(".internal/patch.txt","r")
        print(f"Is the current version still => {champion.Fore.RED}{patch.readline()}{champion.Style.RESET_ALL}?")
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
            patch = open(".internal/patch.txt","w")
            patch.write(newVersion)
            patch.close()
        patch = open(".internal/patch.txt","r")
        print(f"Changing patch version to {champion.Fore.GREEN}{patch.readline()}{champion.Style.RESET_ALL} ")

champion.main()
    
