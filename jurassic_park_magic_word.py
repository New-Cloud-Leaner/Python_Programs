terminal_input = input("""
                       Jurassic Park , System Security Interface
                       Version 4.0.5 , Alpha E
                       Ready...
                       > """)
count = 0
while count < 2:
    if terminal_input != "please":
        print("""                    access: PERMISSION DENIED.""")
        terminal_input = input("                       > ")
        count +=1
        if count == 2 and terminal_input != "please":
            while True:
                print("                   Ah ah ah, you didn't say the magic word!")
    elif terminal_input == "please":
        print("""                        Aha You said the magic word! """)
        print(" ")
        print("                       #: ")
        break
            

