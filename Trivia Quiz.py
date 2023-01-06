print("Hi Welcome to Karl's Quiz Game!")
answer = str(input("Do you want to play? (yes/no) :"))
quiz_number = 0
correct = 0
chances = 3
if answer.lower() == "yes":
    while chances != 0 and quiz_number != 10:
        answer == ""
        print("Instructions: If its a multiple choice question type the corresponding letter, and if its a true or false question write 't' or 'f'\nIf you make 3 mistakes then its Game Over!")
        print("Let's Start!")
        print("Which of the following is NOT a programming language")
        print("a. Python\nb. Java\nc. PHP\nd. LAN")
        answer = input("Answer: ")
        if answer.lower() == "d":
            answer == ""
            correct +=1
            print(f"Correct! You have {correct} point! so far")
        else:
            answer == ""
            chances -= 1
            print(f"Wrong! You have {chances} chances left!")
            if chances == 0:
                break
            quiz_number += 1
        print("What number system are values expressed only in 1s and 0s")
        print("a. Hexadecimal\nb. Binary\nc. Octal\nd. Decimal")
        answer = input("Answer: ")
        if answer.lower() == "b":
            answer == ""
            correct +=1
            print(f"Correct! You have {correct} points so far!")
        else:
            answer == ""
            chances -= 1
            print(f"Wrong! You have {chances} chances left!")
            if chances == 0:
                break
            quiz_number += 1
        print("What does HTML stand for?")
        print("a. Hypertext Markup Language\nb. Holy Teachings of Mark and Luke\nc. Hypersonic Test Missles of Lithuania\nd. Hydrophobic Textile Machines against Liquid")
        answer = input("Answer: ")
        if answer.lower() == "a":
            answer == ""
            correct +=1
            print(f"Correct! You have {correct} points so far!")
        else:
            answer == ""
            chances -= 1
            print(f"Wrong! You have {chances} chances left!")
            if chances == 0:
                break
            quiz_number += 1
        print("Ada Lovelace was the first computer programmer")
        print("True or False")
        answer = input("Answer: ")
        if answer.lower() == "t":
            answer == ""
            correct +=1
            print(f"Correct! You have {correct} points so far!")
        else:
            answer == ""
            chances -= 1
            print(f"Wrong! You have {chances} chances left!")
            if chances == 0:
                break
            quiz_number += 1
        print("The first computer 'bug' was an actual real life bug")
        print("True or False")
        answer = input("Answer: ")
        if answer.lower() == "t":
            answer == ""
            correct +=1
            print(f"Correct! You have {correct} points so far!")
        else:
            answer == ""
            chances -= 1
            print(f"Wrong! You have {chances} chances left!")
            if chances == 0:
                break
            quiz_number += 1
        print("A widespread computer virus was created by a Filipino named Onel de Guzman. What was the name of this Computer virus?")
        print("a. I would die for you virus\nb. You belong with me virus\nc. Mahal kita virus\nd. I love you virus")
        answer = input("Answer: ")
        if answer.lower() == "d":
            answer == ""
            correct +=1
            print(f"Correct! You have {correct} points so far!")
        else:
            answer == ""
            chances -= 1
            print(f"Wrong! You have {chances} chances left!")
            if chances == 0:
                break
            quiz_number += 1
        print("What was the name of the first created computer virus?")
        print("a. Lurking Virus\nb. Crawling Virus\nc. Creeper Virus\nd. Stalking Virus")
        answer = input("Answer: ")
        if answer.lower() == "c":
            answer == ""
            correct +=1
            print(f"Correct! You have {correct} points so far!")
        else:
            answer == ""
            chances -= 1
            print(f"Wrong! You have {chances} chances left!")
            if chances == 0:
                break
            quiz_number += 1
        print("If RAM is short for random access memory. What does ROM mean?")
        print("a. Read-only memory\nb. Random over memory\nc. Real only memory\nd. Rolling over memory")
        answer = input("Answer: ")
        if answer.lower() == "a":
            answer == ""
            correct +=1
            print(f"Correct! You have {correct} points so far!")
        else:
            answer == ""
            chances -= 1
            print(f"Wrong! You have {chances} chances left!")
            if chances == 0:
                break
            quiz_number += 1
        print("In binary 1 Megabyte is equal to 1,000,000 Bytes")
        print("True or False?")
        answer = input("Answer: ")
        if answer.lower() == "f":
            answer == ""
            correct +=1
            print(f"Correct! You have {correct} points so far!")
        else:
            answer == ""
            chances -= 1
            print(f"Wrong! You have {chances} chances left!")
            if chances == 0:
                break
            quiz_number += 1
        print("What is CPU an acronym for?")
        print("a. Computer parts unity\nb. Central processing unit\nc. Computer play unit\nd. Central part unit")
        answer = input("Answer: ")
        if answer.lower() == "b":
            answer == ""
            correct +=1
            print(f"Correct! You have {correct} points so far!")
        else:
            answer == ""
            chances -= 1
            print(f"Wrong! You have {chances} chances left!")
            if chances == 0:
                break
            quiz_number += 1
elif answer.lower() == "no":
    print("Thanks for playing!")
if chances == 0:
    print("Awww! Too bad! You have no chances left!")
elif correct == 10:
    print("CONGRATUALTIONS YOU SCORED PERFECTLY!")
elif correct > 0:
    print(f"Congratualtions! You scored {correct} points!")