print(" ___     ___ _______ _______ _______ __   __ ___ ___     ______  _______ ______")
print("|   |   |   |       |       |  _    |  | |  |   |   |   |      ||       |    _ | ")
print("|   |   |   |  _____|_     _| |_|   |  | |  |   |   |   |  _    |    ___|   | || ")
print("|   |   |   | |_____  |   | |      ||  |_|  |   |   |   | | |   |   |___|   |_||_ ")
print("|   |___|   |_____  | |   | |  _   ||       |   |   |___| |_|   |    ___|    __  |")
print("|       |   |_____| | |   | | |_|   |       |   |       |       |   |___|   |  | |")
print("|_______|___|_______| |___| |_______|_______|___|_______|______||_______|___|  |_|")
print("==By Redte4m@gmail.com============================================================")
loop_condition = True
while loop_condition == True:
    print("Please choose from the options below.")
    print("Press 1 to create a basic list from a source document with words (ALWAYS run first!!).")
    print("Press 2 to change letter case a few times (hello -> hello, Hello, HELLO, hElLo, & HeLlO).")
    print("Press 3 to concatenate words from the same list into a new file.")
    print("Press 4 to concatenate words from two different lists into a new file.")
    print("Press 5 to change some letters to symbols.")
    print("Press 6 to change some letters to numbers.")
    print("Press 7 to add strings of numbers to the end of each word (hello -> hello1, hello2, etc.)")
    print("Press 8 to add strings of numbers to the start of each word (hello -> 1hello, 2hello, etc.)")
    print("Press 9 to add strings of character to the start and end of each word (hello -> hello!, !hello, etc.)")
    print("Press 0 to quit.")
    main_input = int(input("What would you like to do? "))
    loop_condition = False
    if main_input == 0:
        print("Very well.")
        print("Goodbye.")
        quit()
    elif main_input == 1:
        print("Option 1 selected.")
        print("This will take a document and break it into a plain, unique, all lower-case list.")
        file_in = input("What is the source document to build the list file from? ")
        file_out = input("What do you want to name the final list? ")
        min_len = input("What is minimum word length to save in the list? ")
        f2 = open('/tmp/lb1', "w+")
        with open (file_in) as f1:
          lines = f1.readlines()
          for line in lines:
              words = line.split()
              for word in words:
                  if len(word) >= int(min_len):
                      f2.write(word.strip(',;-:"!@#$%^&*(){}|[]?/><.'))
                      f2.write('\n')
        f1.close()
        f2.close()
        f3 = open('/tmp/lb1', "r")
        f4 = open('/tmp/lb2', "w+")
        templine = f3.readline()
        while templine:
            lower = (templine.lower())
            f4.write(lower)
            templine = f3.readline()
        f3.close()
        f4.close()
        f5 = open('/tmp/lb2', "r")
        f6 = open(file_out, 'w+')
        flag = False
        with open('/tmp/lb2') as f5:
        	for line in f5:
        		for temp in f6:
        			if temp == line:
        				flag = True
        				break
        		if flag == False:
        			f6.write(line)
        		elif flag == True:
        			flag = False
        		f6.seek(0)
        	f6.close()
        f5.close()
        num_lines = sum(1 for line in open(file_out))
        print("Job complete. Your new list has", num_lines, "total words.")
        print("Returning to main menu.")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        loop_condition = True
    elif main_input == 2:
            print("Option 2 selected.")
            print("This will take each word in a list and change the letter case five times.")
            file_in = input("What is the source list file? ")
            file_out = input("What do you want to name the final list? ")
            f1 = open(file_out, "w+")
            with open (file_in) as f2:
                templine1 = f2.readline()
                while templine1:
                    str1 = (templine1.strip('\n'))
                    f1.write(str1+'\n')
                    morph = ''.join([e.upper() if i%2==0 else e for i, e in enumerate(str1)])
                    f1.write(morph+'\n')
                    swap = (morph.swapcase())
                    f1.write(swap+'\n')
                    cap = (str1.capitalize())
                    f1.write(cap+'\n')
                    upper = (str1.upper())
                    f1.write(upper+'\n')
                    templine1 = f2.readline()
            f1.close()
            f2.close()
            num_lines = sum(1 for line in open(file_out))
            print("Job complete. Your new list has", num_lines, "total words.")
            print("Returning to main menu.")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
            loop_condition = True
    elif main_input == 3:
        print("Option 3 selected.")
        print("This will take a list and add each word in the list to the other once.")
        file_in = input("What is the source list file? ")
        file_out = input("What do you want to name the final list? ")
        f1 = open(file_out, "w+")
        with open (file_in) as f2:
            templine1 = f2.readline()
            while templine1:
                with open (file_in) as f3:
                    templine2 = f3.readline()
                    while templine2:
                        str1 = (templine1.strip('\n'))
                        str2 = (templine2.strip('\n'))
                        f1.write(str1+str2+'\n')
                        templine2 = f3.readline()
                templine1 = f2.readline()
        f1.close()
        f2.close()
        f3.close()
        num_lines = sum(1 for line in open(file_out))
        print("Job complete. Your new list has", num_lines, "total words.")
        print("Returning to main menu.")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        loop_condition = True
    elif main_input == 4:
        print("Option 4 selected.")
        print("This will take two lists and add each word in each list to the other once.")
        print("The total list will only be as long as the shortest list times two.")
        file_in1 = input("What is the first list? ")
        file_in2 = input("What is the second list? ")
        file_out = input("What do you want to name the final list? ")
        f1 = open(file_out, "w+")
        with open (file_in1) as f2:
            templine1 = f2.readline()
            while templine1:
                with open (file_in2) as f3:
                    templine2 = f3.readline()
                    while templine2:
                        str1 = (templine1.strip('\n'))
                        str2 = templine2
                        f1.write(str1+str2)
                        str2 = (templine2.strip('\n'))
                        str1 = templine1
                        f1.write(str2+str1)
                        templine2 = f3.readline()
                templine1 = f2.readline()
        f1.close()
        f2.close()
        f3.close()
        num_lines = sum(1 for line in open(file_out))
        print("Job complete. Your new list has", num_lines, "total words.")
        print("Returning to main menu.")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        loop_condition = True
    elif main_input == 5:
        print("Option 5 selected.")
        print("This will take a list and turn some letters to symbols and other changes.")
        print("It can be run more than once but may result in some duplicates.")
        file_in = input("What is the source list file? ")
        file_out = input("What do you want to name the final list? ")
        f3 = open(file_out, "w+")
        with open(file_in) as f4:
            templine2 = f4.readline()
            while templine2:
                f3.write(templine2)
                if 'a' in templine2:
                    var = templine2.count('a')
                    if var == 1:
                        f3.write(templine2.replace('a', '@', 1))
                    if var == 2:
                        f3.write(templine2.replace('a', '@', 1))
                        f3.write(templine2.replace('a', '@', 2))
                    if var == 3:
                        f3.write(templine2.replace('a', '@', 1))
                        f3.write(templine2.replace('a', '@', 2))
                        f3.write(templine2.replace('a', '@', 3))
                    if var == 4:
                        f3.write(templine2.replace('a', '@', 1))
                        f3.write(templine2.replace('a', '@', 2))
                        f3.write(templine2.replace('a', '@', 3))
                        f3.write(templine2.replace('a', '@', 4))
                if 'A' in templine2:
                    var = templine2.count('A')
                    if var == 1:
                        f3.write(templine2.replace('A', '@', 1))
                    if var == 2:
                        f3.write(templine2.replace('A', '@', 1))
                        f3.write(templine2.replace('A', '@', 2))
                    if var == 3:
                        f3.write(templine2.replace('A', '@', 1))
                        f3.write(templine2.replace('A', '@', 2))
                        f3.write(templine2.replace('A', '@', 3))
                    if var == 4:
                        f3.write(templine2.replace('A', '@', 1))
                        f3.write(templine2.replace('A', '@', 2))
                        f3.write(templine2.replace('A', '@', 3))
                        f3.write(templine2.replace('A', '@', 4))
                if 'h' in templine2:
                    var = templine2.count('h')
                    if var == 1:
                        f3.write(templine2.replace('h', '#', 1))
                    if var == 2:
                        f3.write(templine2.replace('h', '#', 1))
                        f3.write(templine2.replace('h', '#', 2))
                    if var == 3:
                        f3.write(templine2.replace('h', '#', 1))
                        f3.write(templine2.replace('h', '#', 2))
                        f3.write(templine2.replace('h', '#', 3))
                    if var == 4:
                        f3.write(templine2.replace('h', '#', 1))
                        f3.write(templine2.replace('h', '#', 2))
                        f3.write(templine2.replace('h', '#', 3))
                        f3.write(templine2.replace('h', '#', 4))
                if 'H' in templine2:
                    var = templine2.count('H')
                    if var == 1:
                        f3.write(templine2.replace('H', '#', 1))
                    if var == 2:
                        f3.write(templine2.replace('H', '#', 1))
                        f3.write(templine2.replace('H', '#', 2))
                    if var == 3:
                        f3.write(templine2.replace('H', '#', 1))
                        f3.write(templine2.replace('H', '#', 2))
                        f3.write(templine2.replace('H', '#', 3))
                    if var == 4:
                        f3.write(templine2.replace('H', '#', 1))
                        f3.write(templine2.replace('H', '#', 2))
                        f3.write(templine2.replace('H', '#', 3))
                        f3.write(templine2.replace('H', '#', 4))
                if 's' in templine2:
                    var = templine2.count('s')
                    if var == 1:
                        f3.write(templine2.replace('s', '$', 1))
                    if var == 2:
                        f3.write(templine2.replace('s', '$', 1))
                        f3.write(templine2.replace('s', '$', 2))
                    if var == 3:
                        f3.write(templine2.replace('s', '$', 1))
                        f3.write(templine2.replace('s', '$', 2))
                        f3.write(templine2.replace('s', '$', 3))
                    if var == 4:
                        f3.write(templine2.replace('s', '$', 1))
                        f3.write(templine2.replace('s', '$', 2))
                        f3.write(templine2.replace('s', '$', 3))
                        f3.write(templine2.replace('s', '$', 4))
                if 'S' in templine2:
                    var = templine2.count('S')
                    if var == 1:
                        f3.write(templine2.replace('S', '$', 1))
                    if var == 2:
                        f3.write(templine2.replace('S', '$', 1))
                        f3.write(templine2.replace('S', '$', 2))
                    if var == 3:
                        f3.write(templine2.replace('S', '$', 1))
                        f3.write(templine2.replace('S', '$', 2))
                        f3.write(templine2.replace('S', '$', 3))
                    if var == 4:
                        f3.write(templine2.replace('S', '$', 1))
                        f3.write(templine2.replace('S', '$', 2))
                        f3.write(templine2.replace('S', '$', 3))
                        f3.write(templine2.replace('S', '$', 4))
                if 'l' in templine2:
                    var = templine2.count('l')
                    if var == 1:
                        f3.write(templine2.replace('l', '!', 1))
                    if var == 2:
                        f3.write(templine2.replace('l', '!', 1))
                        f3.write(templine2.replace('l', '!', 2))
                    if var == 3:
                        f3.write(templine2.replace('l', '!', 1))
                        f3.write(templine2.replace('l', '!', 2))
                        f3.write(templine2.replace('l', '!', 3))
                    if var == 4:
                        f3.write(templine2.replace('l', '!', 1))
                        f3.write(templine2.replace('l', '!', 2))
                        f3.write(templine2.replace('l', '!', 3))
                        f3.write(templine2.replace('l', '!', 4))
                if 'L' in templine2:
                    var = templine2.count('L')
                    if var == 1:
                        f3.write(templine2.replace('L', '!', 1))
                    if var == 2:
                        f3.write(templine2.replace('L', '!', 1))
                        f3.write(templine2.replace('L', '!', 2))
                    if var == 3:
                        f3.write(templine2.replace('L', '!', 1))
                        f3.write(templine2.replace('L', '!', 2))
                        f3.write(templine2.replace('L', '!', 3))
                    if var == 4:
                        f3.write(templine2.replace('L', '!', 1))
                        f3.write(templine2.replace('L', '!', 2))
                        f3.write(templine2.replace('L', '!', 3))
                        f3.write(templine2.replace('L', '!', 4))
                if 'i' in templine2:
                    var = templine2.count('i')
                    if var == 1:
                        f3.write(templine2.replace('i', '1', 1))
                    if var == 2:
                        f3.write(templine2.replace('i', '1', 1))
                        f3.write(templine2.replace('i', '1', 2))
                    if var == 3:
                        f3.write(templine2.replace('i', '1', 1))
                        f3.write(templine2.replace('i', '1', 2))
                        f3.write(templine2.replace('i', '1', 3))
                    if var == 4:
                        f3.write(templine2.replace('i', '1', 1))
                        f3.write(templine2.replace('i', '1', 2))
                        f3.write(templine2.replace('i', '1', 3))
                        f3.write(templine2.replace('i', '1', 4))
                if 'I' in templine2:
                    var = templine2.count('I')
                    if var == 1:
                        f3.write(templine2.replace('I', '1', 1))
                    if var == 2:
                        f3.write(templine2.replace('I', '1', 1))
                        f3.write(templine2.replace('I', '1', 2))
                    if var == 3:
                        f3.write(templine2.replace('I', '1', 1))
                        f3.write(templine2.replace('I', '1', 2))
                        f3.write(templine2.replace('I', '1', 3))
                    if var == 4:
                        f3.write(templine2.replace('I', '1', 1))
                        f3.write(templine2.replace('I', '1', 2))
                        f3.write(templine2.replace('I', '1', 3))
                        f3.write(templine2.replace('I', '1', 4))
                if 'you' in templine2:
                    f3.write(templine2.replace('you', 'u', 1))
                if 'you' in templine2:
                    f3.write(templine2.replace('you', 'U', 1))
                if 'YOU' in templine2:
                    f3.write(templine2.replace('YOU', 'u', 1))
                if 'YOU' in templine2:
                    f3.write(templine2.replace('YOU', 'U', 1))
                if 'YoU' in templine2:
                    f3.write(templine2.replace('YoU', 'u', 1))
                if 'yOu' in templine2:
                    f3.write(templine2.replace('yOu', 'U', 1))
                if 'love' in templine2:
                    f3.write(templine2.replace('love', 'LUV', 1))
                if 'love' in templine2:
                    f3.write(templine2.replace('love', 'luv', 1))
                if 'LOVE' in templine2:
                    f3.write(templine2.replace('LOVE', 'luv', 1))
                if 'LOVE' in templine2:
                    f3.write(templine2.replace('LOVE', 'LUV', 1))
                if 'LoVe' in templine2:
                    f3.write(templine2.replace('LoVe', 'luv', 1))
                if 'lOvE' in templine2:
                    f3.write(templine2.replace('lOvE', 'LUV', 1))
                if 'too' in templine2:
                    f3.write(templine2.replace('too', '2', 1))
                if 'TOO' in templine2:
                    f3.write(templine2.replace('TOO', '2', 1))
                if 'ToO' in templine2:
                    f3.write(templine2.replace('ToO', '2', 1))
                if 'tOo' in templine2:
                    f3.write(templine2.replace('tOo', '2', 1))

                templine2 = f4.readline()
            f3.close()
            f4.close()
        num_lines = sum(1 for line in open(file_out))
        print("Job complete. Your new list has", num_lines, "total words.")
        print("Returning to main menu.")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        loop_condition = True
    elif main_input == 6:
        print("Option 6 selected.")
        print("This will take a list and turn letters to numbers.")
        print("It can be run more than once but may result in some duplicates.")
        file_in = input("What is the source list file? ")
        file_out = input("What do you want to name the final list? ")
        f3 = open(file_out, "w+")
        with open(file_in) as f4:
            templine2 = f4.readline()
            while templine2:
                f3.write(templine2)
                if 'a' in templine2:
                    var = templine2.count('a')
                    if var == 1:
                        f3.write(templine2.replace('a', '4', 1))
                    if var == 2:
                        f3.write(templine2.replace('a', '4', 1))
                        f3.write(templine2.replace('a', '4', 2))
                    if var == 3:
                        f3.write(templine2.replace('a', '4', 1))
                        f3.write(templine2.replace('a', '4', 2))
                        f3.write(templine2.replace('a', '4', 3))
                    if var == 4:
                        f3.write(templine2.replace('a', '4', 1))
                        f3.write(templine2.replace('a', '4', 2))
                        f3.write(templine2.replace('a', '4', 3))
                        f3.write(templine2.replace('a', '4', 4))
                if 'A' in templine2:
                    var = templine2.count('A')
                    if var == 1:
                        f3.write(templine2.replace('A', '4', 1))
                    if var == 2:
                        f3.write(templine2.replace('A', '4', 1))
                        f3.write(templine2.replace('A', '4', 2))
                    if var == 3:
                        f3.write(templine2.replace('A', '4', 1))
                        f3.write(templine2.replace('A', '4', 2))
                        f3.write(templine2.replace('A', '4', 3))
                    if var == 4:
                        f3.write(templine2.replace('A', '4', 1))
                        f3.write(templine2.replace('A', '4', 2))
                        f3.write(templine2.replace('A', '4', 3))
                        f3.write(templine2.replace('A', '4', 4))
                if 'b' in templine2:
                    var = templine2.count('b')
                    if var == 1:
                        f3.write(templine2.replace('b', '8', 1))
                    if var == 2:
                        f3.write(templine2.replace('b', '8', 1))
                        f3.write(templine2.replace('b', '8', 2))
                    if var == 3:
                        f3.write(templine2.replace('b', '8', 1))
                        f3.write(templine2.replace('b', '8', 2))
                        f3.write(templine2.replace('b', '8', 3))
                    if var == 4:
                        f3.write(templine2.replace('b', '8', 1))
                        f3.write(templine2.replace('b', '8', 2))
                        f3.write(templine2.replace('b', '8', 3))
                        f3.write(templine2.replace('b', '8', 4))
                if 'B' in templine2:
                    var = templine2.count('B')
                    if var == 1:
                        f3.write(templine2.replace('B', '8', 1))
                    if var == 2:
                        f3.write(templine2.replace('B', '8', 1))
                        f3.write(templine2.replace('B', '8', 2))
                    if var == 3:
                        f3.write(templine2.replace('B', '8', 1))
                        f3.write(templine2.replace('B', '8', 2))
                        f3.write(templine2.replace('B', '8', 3))
                    if var == 4:
                        f3.write(templine2.replace('B', '8', 1))
                        f3.write(templine2.replace('B', '8', 2))
                        f3.write(templine2.replace('B', '8', 3))
                        f3.write(templine2.replace('B', '8', 4))
                if 's' in templine2:
                    var = templine2.count('s')
                    if var == 1:
                        f3.write(templine2.replace('s', '5', 1))
                    if var == 2:
                        f3.write(templine2.replace('s', '5', 1))
                        f3.write(templine2.replace('s', '5', 2))
                    if var == 3:
                        f3.write(templine2.replace('s', '5', 1))
                        f3.write(templine2.replace('s', '5', 2))
                        f3.write(templine2.replace('s', '5', 3))
                    if var == 4:
                        f3.write(templine2.replace('s', '5', 1))
                        f3.write(templine2.replace('s', '5', 2))
                        f3.write(templine2.replace('s', '5', 3))
                        f3.write(templine2.replace('s', '5', 4))
                if 'S' in templine2:
                    var = templine2.count('S')
                    if var == 1:
                        f3.write(templine2.replace('S', '5', 1))
                    if var == 2:
                        f3.write(templine2.replace('S', '5', 1))
                        f3.write(templine2.replace('S', '5', 2))
                    if var == 3:
                        f3.write(templine2.replace('S', '5', 1))
                        f3.write(templine2.replace('S', '5', 2))
                        f3.write(templine2.replace('S', '5', 3))
                    if var == 4:
                        f3.write(templine2.replace('S', '5', 1))
                        f3.write(templine2.replace('S', '5', 2))
                        f3.write(templine2.replace('S', '5', 3))
                        f3.write(templine2.replace('S', '5', 4))
                if 'e' in templine2:
                    var = templine2.count('e')
                    if var == 1:
                        f3.write(templine2.replace('e', '3', 1))
                    if var == 2:
                        f3.write(templine2.replace('e', '3', 1))
                        f3.write(templine2.replace('e', '3', 2))
                    if var == 3:
                        f3.write(templine2.replace('e', '3', 1))
                        f3.write(templine2.replace('e', '3', 2))
                        f3.write(templine2.replace('e', '3', 3))
                    if var == 4:
                        f3.write(templine2.replace('e', '3', 1))
                        f3.write(templine2.replace('e', '3', 2))
                        f3.write(templine2.replace('e', '3', 3))
                        f3.write(templine2.replace('e', '3', 4))
                if 'E' in templine2:
                    var = templine2.count('E')
                    if var == 1:
                        f3.write(templine2.replace('E', '3', 1))
                    if var == 2:
                        f3.write(templine2.replace('E', '3', 1))
                        f3.write(templine2.replace('E', '3', 2))
                    if var == 3:
                        f3.write(templine2.replace('E', '3', 1))
                        f3.write(templine2.replace('E', '3', 2))
                        f3.write(templine2.replace('E', '3', 3))
                    if var == 4:
                        f3.write(templine2.replace('E', '3', 1))
                        f3.write(templine2.replace('E', '3', 2))
                        f3.write(templine2.replace('E', '3', 3))
                        f3.write(templine2.replace('E', '3', 4))
                if 'l' in templine2:
                    var = templine2.count('l')
                    if var == 1:
                        f3.write(templine2.replace('l', '1', 1))
                    if var == 2:
                        f3.write(templine2.replace('l', '1', 1))
                        f3.write(templine2.replace('l', '1', 2))
                    if var == 3:
                        f3.write(templine2.replace('l', '1', 1))
                        f3.write(templine2.replace('l', '1', 2))
                        f3.write(templine2.replace('l', '1', 3))
                    if var == 4:
                        f3.write(templine2.replace('l', '1', 1))
                        f3.write(templine2.replace('l', '1', 2))
                        f3.write(templine2.replace('l', '1', 3))
                        f3.write(templine2.replace('l', '1', 4))
                if 'L' in templine2:
                    var = templine2.count('L')
                    if var == 1:
                        f3.write(templine2.replace('L', '1', 1))
                    if var == 2:
                        f3.write(templine2.replace('L', '1', 1))
                        f3.write(templine2.replace('L', '1', 2))
                    if var == 3:
                        f3.write(templine2.replace('L', '1', 1))
                        f3.write(templine2.replace('L', '1', 2))
                        f3.write(templine2.replace('L', '1', 3))
                    if var == 4:
                        f3.write(templine2.replace('L', '1', 1))
                        f3.write(templine2.replace('L', '1', 2))
                        f3.write(templine2.replace('L', '1', 3))
                        f3.write(templine2.replace('L', '1', 4))
                if 't' in templine2:
                    var = templine2.count('t')
                    if var == 1:
                        f3.write(templine2.replace('t', '7', 1))
                    if var == 2:
                        f3.write(templine2.replace('t', '7', 1))
                        f3.write(templine2.replace('t', '7', 2))
                    if var == 3:
                        f3.write(templine2.replace('t', '7', 1))
                        f3.write(templine2.replace('t', '7', 2))
                        f3.write(templine2.replace('t', '7', 3))
                    if var == 4:
                        f3.write(templine2.replace('t', '7', 1))
                        f3.write(templine2.replace('t', '7', 2))
                        f3.write(templine2.replace('t', '7', 3))
                        f3.write(templine2.replace('t', '7', 4))
                if 'T' in templine2:
                    var = templine2.count('T')
                    if var == 1:
                        f3.write(templine2.replace('T', '7', 1))
                    if var == 2:
                        f3.write(templine2.replace('T', '7', 1))
                        f3.write(templine2.replace('T', '7', 2))
                    if var == 3:
                        f3.write(templine2.replace('T', '7', 1))
                        f3.write(templine2.replace('T', '7', 2))
                        f3.write(templine2.replace('T', '7', 3))
                    if var == 4:
                        f3.write(templine2.replace('T', '7', 1))
                        f3.write(templine2.replace('T', '7', 2))
                        f3.write(templine2.replace('T', '7', 3))
                        f3.write(templine2.replace('T', '7', 4))
                if 'o' in templine2:
                    var = templine2.count('o')
                    if var == 1:
                        f3.write(templine2.replace('o', '0', 1))
                    if var == 2:
                        f3.write(templine2.replace('o', '0', 1))
                        f3.write(templine2.replace('o', '0', 2))
                    if var == 3:
                        f3.write(templine2.replace('o', '0', 1))
                        f3.write(templine2.replace('o', '0', 2))
                        f3.write(templine2.replace('o', '0', 3))
                    if var == 4:
                        f3.write(templine2.replace('o', '0', 1))
                        f3.write(templine2.replace('o', '0', 2))
                        f3.write(templine2.replace('o', '0', 3))
                        f3.write(templine2.replace('o', '0', 4))
                if 'O' in templine2:
                    var = templine2.count('o')
                    if var == 1:
                        f3.write(templine2.replace('O', '0', 1))
                    if var == 2:
                        f3.write(templine2.replace('O', '0', 1))
                        f3.write(templine2.replace('O', '0', 2))
                    if var == 3:
                        f3.write(templine2.replace('O', '0', 1))
                        f3.write(templine2.replace('O', '0', 2))
                        f3.write(templine2.replace('O', '0', 3))
                    if var == 4:
                        f3.write(templine2.replace('O', '0', 1))
                        f3.write(templine2.replace('O', '0', 2))
                        f3.write(templine2.replace('O', '0', 3))
                        f3.write(templine2.replace('O', '0', 4))
                templine2 = f4.readline()
            f3.close()
            f4.close()
        num_lines = sum(1 for line in open(file_out))
        print("Job complete. Your new list has", num_lines, "total words.")
        print("Returning to main menu.")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        loop_condition = True
    elif main_input == 7:
        print("Option 7 selected.")
        print("This will take a list and add stings of numbers to the end of each word.")
        file_in = input("What is the source list file? ")
        file_out = input("What do you want to name the final list? ")
        f15 = open(file_out, "w+")
        with open(file_in) as f4:
            templine2 = f4.readline()
            while templine2:
                f15.write(templine2)
                str3 = (templine2.strip('\n'))
                numbers = list(range(0, 100))
                for num in numbers:
                    str3 = (templine2.strip('\n'))
                    f15.write(str3 + str(num)+'\r')
                numbers2 = list(range(1950, 2019))
                for num in numbers2:
                    str3 = (templine2.strip('\n'))
                    f15.write(str3 + str(num)+'\r')
                f15.write(str3+"007"'\n')
                f15.write(str3+"1234"'\n')
                f15.write(str3+"2345"'\n')
                f15.write(str3+"3456"'\n')
                f15.write(str3+"4567"'\n')
                f15.write(str3+"5678"'\n')
                f15.write(str3+"6789"'\n')
                f15.write(str3+"7890"'\n')
                f15.write(str3+"0987"'\n')
                f15.write(str3+"8765"'\n')
                f15.write(str3+"7654"'\n')
                f15.write(str3+"6543"'\n')
                f15.write(str3+"5432"'\n')
                f15.write(str3+"4321"'\n')
                f15.write(str3+"12345"'\n')
                f15.write(str3+"123456"'\n')
                f15.write(str3+"1234567"'\n')
                f15.write(str3+"12345678"'\n')
                f15.write(str3+"123456789"'\n')
                f15.write(str3+"1234567890"'\n')
                f15.write(str3+"0987654321"'\n')
                f15.write(str3+"987654321"'\n')
                f15.write(str3+"87654321"'\n')
                f15.write(str3+"7654321"'\n')
                f15.write(str3+"654321"'\n')
                f15.write(str3+"54321"'\n')
                f15.write(str3+"4321"'\n')
                f15.write(str3+"321"'\n')
                templine2 = f4.readline()
            f15.close()
            f4.close()
        num_lines = sum(1 for line in open(file_out))
        print("Job complete. Your new list has", num_lines, "total words.")
        print("Returning to main menu.")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        loop_condition = True
    elif main_input == 8:
        print("Option 8 selected.")
        print("This will take a list and add stings of numbers to the start of each word.")
        file_in = input("What is the source list file? ")
        file_out = input("What do you want to name the final list? ")
        f15 = open(file_out, "w+")
        with open(file_in) as f4:
            templine2 = f4.readline()
            while templine2:
                f15.write(templine2)
                str3 = (templine2.strip('\n'))
                numbers = list(range(0, 100))
                for num in numbers:
                    str3 = (templine2.strip('\n'))
                    f15.write(str(num)+str3+'\r')
                numbers2 = list(range(1950, 2019))
                for num in numbers2:
                    str3 = (templine2.strip('\n'))
                    f15.write(str(num)+str3+'\r')
                f15.write("007"+str3+'\n')
                f15.write("1234"+str3+'\n')
                f15.write("2345"+str3+'\n')
                f15.write("3456"+str3+'\n')
                f15.write("4567"+str3+'\n')
                f15.write("5678"+str3+'\n')
                f15.write("6789"+str3+'\n')
                f15.write("7890"+str3+'\n')
                f15.write("0987"+str3+'\n')
                f15.write("8765"+str3+'\n')
                f15.write("7654"+str3+'\n')
                f15.write("6543"+str3+'\n')
                f15.write("5432"+str3+'\n')
                f15.write("4321"+str3+'\n')
                f15.write("12345"+str3+'\n')
                f15.write("123456"+str3+'\n')
                f15.write("1234567"+str3+'\n')
                f15.write("12345678"+str3+'\n')
                f15.write("123456789"+str3+'\n')
                f15.write("1234567890"+str3+'\n')
                f15.write("0987654321"+str3+'\n')
                f15.write("987654321"+str3+'\n')
                f15.write("87654321"+str3+'\n')
                f15.write("7654321"+str3+'\n')
                f15.write("654321"+str3+'\n')
                f15.write("54321"+str3+'\n')
                f15.write("4321"+str3+'\n')
                f15.write("321"+str3+'\n')
                templine2 = f4.readline()
            f15.close()
            f4.close()
        num_lines = sum(1 for line in open(file_out))
        print("Job complete. Your new list has", num_lines, "total words.")
        print("Returning to main menu.")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        loop_condition = True
    elif main_input == 9:
        print("Option 8 selected.")
        print("This will take a list and add stings of numbers to the start of each word.")
        file_in = input("What is the source list file? ")
        file_out = input("What do you want to name the final list? ")
        f15 = open(file_out, "w+")
        with open(file_in) as f4:
            templine2 = f4.readline()
            while templine2:
                f15.write(templine2)
                str3 = (templine2.strip('\n'))
                f15.write("!"+str3+'\n')
                f15.write("@"+str3+'\n')
                f15.write("#"+str3+'\n')
                f15.write("$"+str3+'\n')
                f15.write("%"+str3+'\n')
                f15.write("!@"+str3+'\n')
                f15.write("@#"+str3+'\n')
                f15.write("#$"+str3+'\n')
                f15.write("$%"+str3+'\n')
                f15.write("!@#"+str3+'\n')
                f15.write("@#$"+str3+'\n')
                f15.write("#$%"+str3+'\n')
                f15.write("!#%"+str3+'\n')
                f15.write("@$"+str3+'\n')
                f15.write("!@$"+str3+'\n')
                f15.write("@$%"+str3+'\n')
                f15.write("!@#$"+str3+'\n')
                f15.write("@#$%"+str3+'\n')
                f15.write("!@$%"+str3+'\n')
                f15.write("!#$%"+str3+'\n')
                f15.write("#$%@"+str3+'\n')
                f15.write("@!#@"+str3+'\n')
                f15.write("$#!@"+str3+'\n')
                f15.write("%#$@"+str3+'\n')
                f15.write("#!@$"+str3+'\n')
                f15.write(str3+"!"'\n')
                f15.write(str3+"@"'\n')
                f15.write(str3+"#"'\n')
                f15.write(str3+"$"'\n')
                f15.write(str3+"%"'\n')
                f15.write(str3+"!@"'\n')
                f15.write(str3+"@#"'\n')
                f15.write(str3+"#$"'\n')
                f15.write(str3+"$%"'\n')
                f15.write(str3+"!@#"'\n')
                f15.write(str3+"@#$"'\n')
                f15.write(str3+"#$%"'\n')
                f15.write(str3+"!#%"'\n')
                f15.write(str3+"@$%"'\n')
                f15.write(str3+"!@#$"'\n')
                f15.write(str3+"!@$%"'\n')
                f15.write(str3+"@#$%"'\n')
                f15.write(str3+"!#$%"'\n')
                f15.write(str3+"#$%@"'\n')
                f15.write(str3+"@!#@"'\n')
                f15.write(str3+"$#!@"'\n')
                f15.write(str3+"%#$@"'\n')
                f15.write(str3+"%#$@"'\n')
                f15.write(str3+"#!@$"'\n')
                templine2 = f4.readline()
            f15.close()
            f4.close()
        num_lines = sum(1 for line in open(file_out))
        print("Job complete. Your new list has", num_lines, "total words.")
        print("Returning to main menu.")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        loop_condition = True
