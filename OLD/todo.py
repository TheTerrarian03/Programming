# my useless (almost) to-do list program

def main():
    date = input("What is the date of the calendar's to-do list?"
                 "The Format is: MMDDYYYY\n")
    if date == "04152020":
        todo_04152020()
    elif date == "04162020":
        todo_04162020()
    elif date == "04172020":
        todo_04172020()
    elif date == "04202020":
        todo_04202020()
    elif date == "04212020":
        todo_04212020()
    elif date == "04222020":
        todo_04222020()
    elif date == "04232020":
        todo_04232020()
    elif date.lower() == "mmddyyyy":
        print("Haha, nice try. You have to put actual numbers in. Sorry!")
        main()
    else:
        print("The dates are: 04152020 -> 04272020 and 04302020.")
        main()


def todo_04152020():
    print("1. Work on Spanish stuff until MATH MEETING AT 10:30AM")
    print("2. MATH MEETING AT 10:30AM")
    print("3. Continue Spanish stuff, hopefully finish")
    print("4. Fill our P.E. Journal for 2 days")
    print("5. Work on Science notes and lab (due Friday)")
    print("6. Make extra ELA video")
    print("7. Choir warm-up assignment")


def todo_04162020():
    print("ELA MEETING AT 9:00AM")
    print("2. Make sure Spanish stuff is done.")
    print("3. Make sure Math stuff is done.")
    print("4. Work on science lab(s), make sure science notes are done.")
    print("5. fill out both the P.E. and ELA Journal.")
    print("6. Work on Choir thing??? (It's due Monday (later))")
    print("7. Chapter11 revier questions, pg. 373-374.")


def todo_04172020():
    print("1. Make sure there are no meetings.")
    print("2. Work on Choir thing? IDK.")
    print("3. Fill out Journals.")
    print("4. Make sure everything else is done.")


def to_do04182020():
    print("Nothing")


def to_do04192020():
    print("Nothing")


def todo_04202020():
    print("1. MATH MEETING AT 10:30AM")
    print("2. Work on Spanish stuff.")
    print("3. Work on Math Stuff.")
    print("4. Make sure Science notes (C4S2) are done; turn in.")
    print("5. Fill out ELA Journal.")
    print("6. Research/make-rough-draft of Earthday for History - due 04262020")
    print("7. ELA optional quiz.")


def todo_04212020():
    print("1. ELA MEETING AT 9:00AM")
    print("2. Spanish stuff: Duolingo 75pts, others")
    print("3. Watch the stupid Math vids.")
    print("4. Choir practice.")
    print("5. Fill out P.E. jouranl for two days.")
    print("6. Fill out ELA journal for just the one day.")
    print("7. Science notes complete, turn in both C4S2 and C4S3.")
    print("8. Research Earthday for History - due 26")


def tofo_04222020():
    print("MATH MEETING AT 10:30AM")
    print("More Spanish stuff; Duolingo try for 100pts, others")
    print("Choir practice...")
    print("Watch the stupid Math vids")
    print("Continue History Essay(?)")
    print("Fill out both P.E. and ELA journals")
    print("Make a P.E. Tabata :\(")
    print("Check ELA classroom")
    print("Start ELA narrative")


def todo_04232020():
    print("1. ELA MEETING AT 9:00AM")
    print("2. Finish working on Spanish worksheets, Duolingo")
    print("3. Do P.E.'s Monday challenge :\(")
    print("4. Check History essay")
    print("5. Start ELA narrative")
    print("6. Listen to Astronomia.")
    print("7. Choir practice...")


def todo_04242020():
    print("1. Finish Spanish worksheets")
    print("2. ELA narrative outline")
    print("3. Journals")
    print("4. Leave idle breakout on for a longtime")
    print("5. Science stuff?")


def todo_04252020():
    print("1. Turn in Spanish worksheets")
    print("2. Journals")
    print("2. ELA narrative finish")
    

def to_do04262020():
    print("Nothing")
   

def todo_04272020():
    print("1. MATH MEETING AT 10:30AM")
    print("2. Do some Spanish Duolingo)"
    print("3. Math Khan Academy")
    print("4. Science notes (Simple Machines Report)")
    print("5. Journals (Journals mean P.E., ELA, and Choir)")


def todo_04302020():
    print("1. ELA MEETING AT 9:00AM")
    print("2. turn in ELA journal to \"Journal Check\" tab in  classroom")


def exit_quit():
    end_prgm = input("Would you like to go again?\n")
    if end_prgm.lower == "yes" or end_prgm.lower() == "y":
        sys.exit()
    elif end_prgm.lower() == "no" or end_prgm.lower() == "n":
        print("Okay, let's do it again: ")
        main()


main()