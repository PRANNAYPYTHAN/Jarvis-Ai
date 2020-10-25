import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import string
import pandas as Pj

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():

    hour = int(datetime.datetime.now().hour)


    #print(hour, minute, seconds,microseconds)
    if hour>=0 and hour<12:
        speak("Hello, Good Morning ")

    elif hour>=12 and hour<16:
        speak("Hello, Good Afternoon ")
    elif hour>=16 and hour<20:
        speak("Hello, Good Evening")


    else:
        speak("Hello, Good Night ")

    speak("I am invent by Prannay Jain")

    speak("I am jarvis sir.May I help You")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #r.energy_threshold = 1
        audio = r.listen(source)
    try:
        print("Recoginizing...")
        command = r.recognize_google(audio, language='en-in')
        print("User said:",command,"\n")
    except Exception as e:
        print("Say that again please")
        return "None"
    return command


if __name__ == "__main__":
    wishMe()
    while True:

        command = takeCommand().lower()
        if 'angel' in command:
            speak("Please Exit You Are Not Good People")
        if 'time table' in command:
            df = Pj.read_excel("TimeTable.xlsx")
            print(df)
        if 'password' in command:
            if __name__ == "__main__":
                s1 = string.ascii_lowercase
                # print(s1)
                s2 = string.ascii_uppercase
                # print(s2)
                s3 = string.digits
                # print(s3)
                s4 = string.punctuation
                # print(s4)

                plen = int(input("Enter password length\n"))
                s = []
                s.extend(list(s1))
                s.extend(list(s2))
                s.extend(list(s3))
                s.extend(list(s4))

                random.shuffle(s)
                print("".join(s[0:plen]))
                # print(s)

        if 'hello' in command:
            speak("Hello Sir")
            print("User said:", command)
            print(speak)

        if 'language' in command:
            speak("I am developed in python language")

        if 'I' in command:
            speak("I am Jarvis sir")
            print(speak)
            print("User said:", command)
        if 'Priyanka' in command:
            speak("Hello,Mom")
            print("User said:", command)
            print(speak)

        if 'Amit' in command:
            speak("Hello Papa")
            speak(f"User said:{command}")
            print(speak)
        if 'Hiral' in command:
            speak("Hello Hiru")
            speak(f"User said:{command}")
            print(speak)

        if 'Prannay' in command:
            speak("Hello my inventor")
            speak(f"User said{command}:")
            print(speak)

        if 'wikipedia' in command:
            print("Searching")
            speak("Searching wikipedia....")
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=10000000000000)
            # speak("Hello , sir")
            speak("According to wikipedia")
            print(results)
            speak(results)

        if 'shinchan' in command:
            webbrowser.open("https://www.youtube.com/results?search_query=shinchan+latest+episode+in+hindi")
            speak("shinchan")
        if 'stone' in command:
            import random

            player_choice_list = {"s": "Stone", "p": "Paper", "sc": "Scissors"}
            computer_choice_list = ["Stone", "Paper", "Scissors"]
            player_win_chance = [["Stone", "Scissors"], ["Paper", "Stone"], ["Scissors", "Paper"]]

            player_choice_input = []
            player_score_board = []
            computer_choice_input = []
            computer_score_board = []
            tie_count = 0
            moves = 1
            try:
                player_name = input("Enter your name:  ")
                while (moves <= 10):
                    print("\n", end="")
                    print(f"Round - {moves} : Please choose :")
                    for key, value in player_choice_list.items():
                        print("Press", key, "for", value, "\n", end="")
                    player_input = input()
                    player_choice = player_choice_list[player_input.lower()]
                    player_choice_input.append(player_choice)
                    computer_choice = random.choice(computer_choice_list)
                    computer_choice_input.append(computer_choice)

                    if player_choice == computer_choice:
                        player_score_board.append(0)
                        computer_score_board.append(0)
                        tie_count = tie_count + 1
                        print("Game Tie!")
                    elif [player_choice, computer_choice_input] in player_win_chance:
                        player_score_board.append(100)
                        computer_score_board.append(0)
                        print("You Win")
                    else:
                        player_score_board.append(0)
                        computer_score_board.append(100)
                        print("Computer Won")
                    moves = moves + 1
                    continue
                    computer_choice = random.choice(computer_choice_list)
                    computer_choice_input.append(computer_choice)

                player_total_score = 0
                for score in player_score_board:
                    player_total_score = player_total_score + score
                computer_total_score = 0
                for score in computer_score_board:
                    computer_total_score = computer_total_score + score

                print("\n")
                if player_total_score > computer_total_score:
                    print(f"Congratulations.... {player_name} are winner!!!!\n")
                elif player_total_score > computer_total_score:
                    print("Computer are winner")
                else:
                    print("Game Tie")

                print(f"{player_name} - Game Summary:\n", end="")
                print("Won :", player_score_board.count(100), "times.", "\n", end="")
                print("Choices :", player_choice_input, "\n", end="")
                print("Score Board :", player_score_board, "\n", end="")
                print("Total Score: ", player_total_score, "\n")

                print("Computer - Game Summary:\n", end="")
                print("Won :", computer_score_board.count(100), "times.", "\n", end="")
                print("Choices :", computer_choice_input, "\n", end="")
                print("Score Board :", computer_score_board, "\n", end="")
                print("Total Score: ", computer_total_score, "\n")

                print("Game Tie", tie_count, "times.\n")

            except Exception as h:
                print("Wrong Input.Try again!!!")

        if 'website' in command:
            webbrowser.open("http://localhost:63342/Jarvis%20ai/Veda%20Tex.html?_ijt=a1fer9hg95i6e38ivg247c3fvi")
        if 'quiz' in command:

            winning_number = random.randint(1, 100)
            print("This is a number guessing game")
            speak("This is a number guessing game")
            input_number = int(input("Guess number between 1 to 100\n"))
            speak("Guess number between 1 to 100")

            guess = 1
            game_over = False
            while not game_over:
                if (winning_number == input_number):
                    # print("You win and guess are taken", guess)
                    speak("Sir you win")
                    game_over = True
                elif guess == 9:
                    game_over = True
                    print("Sorry your guesses are finish and take guesses", guess)
                    speak(f"Sorry your guesses are finish and take {guess} guesses")
                else:
                    if (winning_number > input_number):
                        print("You guess too low")
                        speak("You guess too low")
                        guess += 1
                        game_over = False
                        input_number = int(input("Please guess again\n"))
                    else:
                        print("You guess too high!")
                        speak("You guess too high!")
                        guess += 1
                        game_over = False
                        input_number = int(input("Guess Again\n"))

                # print(f"You take total moves {guess} ")
                speak(f"You take total moves {guess} ")
            print("Winning number is", winning_number)
        if 'pattern of equal' in command:
            print("How many row you want to print")
            speak("How many row you want to print")
            one = int(input())
            print("Type 1 or 0")
            speak("Type 1 or 0")
            tw = int(input())
            new = bool(tw)
            if new == True:
                for i in range(1, one + 1):
                    for j in range(1, i + 1):
                        print("=", end="")

                    print()

            elif new == False:
                for i in range(one, 0, -1):
                    for j in range(1, i + 1):
                        print("=", end="")
                    print()
        if 'pattern of star' in command:
            print("How many row you want to print")
            speak("How many row you want to print")
            one = int(input())
            print("Type 1 or 0")
            speak("Type 1 or 0")
            tw = int(input())
            new = bool(tw)
            if new == True:
                for i in range(1, one + 1):
                    for j in range(1, i + 1):
                        print("*", end="")

                    print()

            elif new == False:
                for i in range(one, 0, -1):
                    for j in range(1, i + 1):
                        print("*", end="")
                    print()

        if 'youtube' in command:
            webbrowser.open("youtube.com")
            speak("yotube")

        if 'google' in command:
            webbrowser.open("google.com")
            speak("google")
        if 'health' in command:
            def gettime():
                return datetime.datetime.now()


            def take(k):
                if k == 1:
                    c = int(input("Press 1 for Exercise and Press 2 for Food\n"))
                    if c == 1:
                        value = input("Type here\n")
                        with open("Prannay-Exercise.txt", "a") as op:
                            op.write(str([str(gettime())]) + ": " + value + "\n")
                        print("Success Fully Written")
                    elif c == 2:
                        value = input("Type here\n")
                        with open("Prannay-Food.txt", "a") as op:
                            op.write(str([str(gettime())]) + ": " + value + "\n")
                        print("Success Fully Written")
                elif k == 2:
                    c = int(input("Press 1 for Exercise and Press 2 for Food\n"))
                    if c == 1:
                        value = input("Type here\n")
                        with open("Mumma-Exercise.txt", "a") as op:
                            op.write(str([str(gettime())]) + ": " + value + "\n")
                        print("Success Fully Written")
                    elif c == 2:
                        value = input("Type here\n")
                        with open("Mumma-Food.txt", "a") as op:
                            op.write(str([str(gettime())]) + ": " + value + "\n")
                        print("Success Fully Written")
                elif k == 3:
                    c = int(input("Press 1 for Exercise and Press 2 for Food\n"))
                    if c == 1:
                        value = input("Type here\n")
                        with open("Hiral-Exercise.txt", "a") as op:
                            op.write(str([str(gettime())]) + ": " + value + "\n")
                        print("Success Fully Written")
                    elif c == 2:
                        value = input("Type here\n")
                        with open("Hiral-Food.txt", "a") as op:
                            op.write(str([str(gettime())]) + ": " + value + "\n")
                        print("Success Fully Written")
                elif k == 4:
                    c = int(input("Press 1 for Exercise and Press 2 for Food\n"))
                    if c == 1:
                        value = input("Type here\n")
                        with open("Papa-Exercise.txt", "a") as op:
                            op.write(str([str(gettime())]) + ": " + value + "\n")
                        print("Success Fully Written")
                    elif c == 2:
                        value = input("Type here\n")
                        with open("Papa-Food.txt", "a") as op:
                            op.write(str([str(gettime())]) + ": " + value + "\n")
                        print("Success Fully Written")
                else:
                    print("You press invalid input please run again and try again")


            def retrieve(k):
                if k == 1:
                    c = int(input("Enter 1 For Exercise and 2 for food\n"))
                    if c == 1:
                        with open("Prannay-Exercise.txt") as op:
                            for i in op:
                                print(i, end="")
                    elif c == 2:
                        with open("Prannay-Food.txt") as op:
                            for i in op:
                                print(i, end="")
                elif k == 3:
                    c = int(input("Enter 1 For Exercise and 2 for food\n"))
                    if c == 1:
                        with open("Hiral-Exercise.txt") as op:
                            for i in op:
                                print(i, end="")
                    elif c == 2:
                        with open("Hiral-Food.txt") as op:
                            for i in op:
                                print(i, end="")
                elif k == 2:
                    c = int(input("Enter 1 For Exercise and 2 for food\n"))
                    if c == 1:
                        with open("Mumma-Exercise.txt") as op:
                            for i in op:
                                print(i, end="")
                    elif c == 2:
                        with open("Mumma-Food.txt") as op:
                            for i in op:
                                print(i, end="")
                elif k == 4:
                    c = int(input("Enter 1 For Exercise and 2 for food\n"))
                    if c == 1:
                        with open("Papa-Exercise.txt") as op:
                            for i in op:
                                print(i, end="")
                    elif c == 2:
                        with open("Papa-Food.txt") as op:
                            for i in op:
                                print(i, end="")
                else:
                    print("Please Press valid input")


            print("Health Management system")
            a = int(input("Press 1 for log and 2 for retrieve\n"))

            if a == 1:
                b = int(input("Press 1 for Prannay 2 for Mumma 3 for Hiral 4 for Papa\n"))
                take(b)
            if a == 2:
                b = int(input("Press 1 for Prannay 2 for Mumma  3 for Hiral 4 for Papa\n"))
                retrieve(b)
        if 'stack overflow' in command:
            webbrowser.open("stackoverflow.com")

        if 'doraemon' in command:
            webbrowser.open("https://www.youtube.com/results?search_query=doraemon+latest+episode+in+hindi")
            speak("doraemon")
        if 'code' in command:
            webbrowser.open("https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww")
            speak("code with harry")
        if 'fact' in command:
            webbrowser.open("https://www.youtube.com/channel/UCGdPm5Aq081vVD7ih9jZf6Q")
            speak("factechz")
        if 'harry' in command:
            webbrowser.open("www.CodeWithHarry.com")
            speak("code with harry.com")
        if 'bajrangi' in command:
            webbrowser.open("https://www.youtube.com/results?search_query=selfie+with+bajrangi")
            speak("bajrangi")
        if 'mahabharat' in command:
            webbrowser.open("https://www.youtube.com/results?search_query=mahabharat+2013")
            speak("mahabharat")
        if 'mahabharat song' in command:
            webbrowser.open("https://www.youtube.com/watch?v=OKVt7I7zscQ")
            speak("mahabharat songs")
        if 'cooking' in command:
            webbrowser.open("https://www.youtube.com/channel/UCTbNOCtAGaqOEnLMeo3JTeg")
            speak('cooking shooking hindi')
        if 'vedatex' in command:
            webbrowser.open(
                "https://www.google.com/maps/place/Veda+Texfab+pvt+ltd/@25.3438499,74.6271888,17z/data=!3m1!4b1!4m5!3m4!1s0x3968c34bb981e0bd:0x3047caee2a7aaf8c!8m2!3d25.3438499!4d74.6293775")
            speak("vedatex location")
        if 'the time' in command:
            strtime = datetime.datetime.now().strftime("%Y:%D:%H:%M:%S")
            print(strtime)
            speak(f"Sir the time is {strtime}")
        if 'inventor' in command:
            speak("My inventor is prannay")
        if ' your name' in command:
            speak("My name is jrvis")
        if 'live hindi' in command:
            webbrowser.open("https://www.youtube.com/channel/UCHs3bWyXIw_6J0ORvg97b2w")
        if 'taarak mehta' in command:
            webbrowser.open("https://www.youtube.com/results?search_query=taarak+mehta+ka+ooltah+chashmah+horror")
        if 'horror stories' in command:
            webbrowser.open("https://www.youtube.com/channel/UC6oLBoqx1mYOOqmu0Wsjf8w")
        if 'maddam sir' in command:
            webbrowser.open("https://www.youtube.com/results?search_query=maddam+sir")
        if 'antariksh' in command:
            webbrowser.open("https://www.youtube.com/channel/UCZ1OsbnPa1RX6rl9NWlRTOg")
        if 'Vivek Bindra' in command:
            webbrowser.open("https://www.youtube.com/user/MrVivekBindra")
        if 'Sonu Sharma' in command:
            webbrowser.open("https://www.youtube.com/user/dalipsinghbisht")
        if 'ujjwal patni' in command:
            webbrowser.open("https://www.youtube.com/user/personality2009")
        if 'sandeep maheshwari' in command:
            webbrowser.open("https://www.youtube.com/user/SandeepSeminars")
        if 'discovery' in command:
            webbrowser.open("https://www.youtube.com/user/DiscoveryNetworks")
        if 'nat' in command:
            webbrowser.open("https://www.youtube.com/user/NationalGeographic")
        if 'Falguni Pathak' in command:
            webbrowser.open("https://www.youtube.com/channel/UCBbXAKzXjpTFtUD0fwL5HoQ")
        if '90 ALbum' in command:
            webbrowser.open("https://www.youtube.com/channel/UCBbXAKzXjpTFtUD0fwL5HoQ")
        if '5 - minute crafts' in command:
            webbrowser.open("https://www.youtube.com/channel/UC295-Dw_tDNtZXFeAPAW6Aw")
        if 'ipl' in command:
            webbrowser.open("https://www.youtube.com/results?search_query=ipl")
        if 'cricket' in command:
            webbrowser.open("https://www.youtube.com/results?search_query=cricket&pbjreload=101")
        if 'football' in command:
            webbrowser.open("https://www.youtube.com/results?search_query=football")
        if 'free fire' in command:
            webbrowser.open("https://www.youtube.com/channel/UC5c9VlYTSvBSCaoMu_GI6gQ")
        if 'movie' in command:
            webbrowser.open("https://www.youtube.com/results?search_query=mahabharat+pen+movies+")
        # Google Maps
        if 'email to papa' in command:
            try:
                speak("What did I send?")
                content = takeCommand()
                to = "velcrotexfab@gmail.com"
                sendEmail(to,content)
                speak("Email has been send")
            except Exception as e:
                print(e)
                speak("Sorry I cannot send")
        if 'Scratch' in command:
            Prannay = "C:\\Users\hp\AppData\Local\\Programs\\Scratch Desktop\\Scratch Desktop.exe"
            os.startfile(Prannay)
        if 'amazon' in command:
            webbrowser.open("https://www.amazon.com/")
        if 'flipkart' in command:
            webbrowser.open("https://www.flipkart.com/")
        if 'Maps' in command:
            webbrowser.open("https://www.google.com/maps")
        if 'Alpha' in command:
            webbrowser.open("https://www.youtube.com/channel/UC5NU0gwu-18DG2Gs3eK3pMw")
        if 'home' in command:
            webbrowser.open("https://www.google.com/maps/@25.3288736,74.6251166,13.17z")
        else:
            print("Sorry Sir please try again")


