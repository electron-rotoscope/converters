def ndframes_to_rt(ndframes):
    # SMPTE translation to realtime frames
    rtframes = ndframes + ((ndframes // (30 * 60)) * 2) - \
               ((ndframes // (30 * 60 * 10)) * 2)
    return rtframes


def ntscframes_from_2398frames(_2398frames):
    ntscframes = (_2398frames // 4) * 5
    if _2398frames % 4 == 1:
        ntscframes = ntscframes + 1
    elif _2398frames % 4 == 2:
        ntscframes = ntscframes + 2
    elif _2398frames % 4 == 3:
        ntscframes = ntscframes + 4
    return ntscframes


def ntscframes_to_2398frames(ntscframes):
    _2398frames = (ntscframes // 5) * 4
    if ntscframes % 5 == 1:
        _2398frames = _2398frames + 1
    elif ntscframes % 5 == 2:
        _2398frames = _2398frames + 2
    elif ntscframes % 5 == 3:
        _2398frames = _2398frames + 2
    elif ntscframes % 5 == 4:
        _2398frames = _2398frames + 3
    return _2398frames


def count2398(hh, mm, ss, ff):
    # check validity
#    if hh > 23 or hh < 0 or mm > 59 or mm < 0 or \
#       ss > 59 or ss < 0 or ff > 23 or ff < 0:
#        return print("Please input valid numbers, you!")
    # make integers?
#    int(hh)
#    int(mm)
#    int(ss)
#    int(ff)
    # actual counting
    frames = ff + ( ss * 24) + (mm * 24 * 60) + (hh * 24 * 60 * 60)
    # output
#    print("The number you have inputted is - ",
#          hh, ":", mm, ":", ss, ":", ff, sep="")
#    print("That is exactly", frames, "frames in 23.98.")
    return frames


def countpal(hh, mm, ss, ff):
    # check validity
#    if hh > 23 or hh < 0 or mm > 59 or mm < 0 or \
#       ss > 59 or ss < 0 or ff > 24 or ff < 0:
#        return print("Please input valid numbers, you!")
    # make integers?
#    int(hh)
#    int(mm)
#    int(ss)
#    int(ff)
    # actual counting
    frames = ff + (ss * 25) + (mm * 25 * 60) + (hh * 25 * 60 * 60)
    # output
#    print("The number you have inputted is - ",
#          hh, ":", mm, ":", ss, ":", ff, sep="")
#    print("That is exactly", frames, "frames in PAL.")
    return frames


def countndf(hh, mm, ss, ff):
    # check validity
#    if hh > 23 or hh < 0 or mm > 59 or mm < 0 or \
#       ss > 59 or ss < 0 or ff > 29 or ff < 0:
#        return print("Please input valid numbers, you!")
    # make integers?
#    int(hh)
#    int(mm)
#    int(ss)
#    int(ff)
    # actual counting
    frames = ff + (ss * 30) + (mm * 30 * 60) + (hh * 30 * 60 * 60)
    # output
#    print("The number you have inputted is - ",
#          hh, ":", mm, ":", ss, ":", ff, sep="")
#    print("That is exactly", frames, "frames in Non Drop Frame.")
    return frames


def countdf(hh, mm, ss, ff):
    # check validity
#    if hh > 23 or hh < 0 or mm > 59 or mm < 0 or \
#       ss > 59 or ss < 0 or ff > 29 or ff < 0:
#        return print("Please input valid numbers, you!")
    # make integers?
#    int(hh)
#    int(mm)
#    int(ss)
#    int(ff)
    # actual counting (now for the hard part)
    # 3rd line: takes off 2 every minute except the 10s
    # 4th line: takes off 2 for every minute in the hour except the 10s
    frames = ff + \
             (ss * 30) + \
             ((mm * 30 * 60) - mm * 2) + (2 * (mm // 10)) + \
             ((hh * 30 * 60 * 60) - (hh * 60) * 2) + (((hh * 60) // 10) *2)
    # output
#    print("The number you have inputted is - ",
#          hh, ":", mm, ";", ss, ";", ff, sep="")
#    print("That is exactly", frames, "frames in Drop Frame.")
    return frames


def decount2398(fr):
    # Validity check
#    if fr < 0:
#        return print("Error")
    # Actual work
    h = fr//(24*60*60)
    m = (fr%(24*60*60))//(24*60)
    s = (fr%(24*60))//24
    f = fr%24
#    print("The number you have inputted is:", fr, "frames.")
#    print("That's ", h, ":", m, ":", s, ":", f, " in 23.98.", sep="")
    return [h, m, s, f]


def decountpal(fr):
    # Validity check
#    if fr < 0:
#        return print("Error")
    # decounting
    h = fr//(25*60*60)
    m = (fr%(25*60*60))//(25*60)
    s = (fr%(25*60))//25
    f = fr%25
#    print("The number you have inputted is:", fr, "frames.")
#    print("That's ", h, ":", m, ":", s, ":", f, " in PAL.", sep="")
    return [h, m, s, f]


def decountndf(fr):
    # Validity Check
#    if fr < 0:
#        return print("Error")
    # decounting
    h = fr//(30*60*60)
    m = (fr%(30*60*60))//(30*60)
    s = (fr%(30*60))//30
    f = fr%30
#    print("The number you have inputted is:", fr, "frames.")
#    print("That's ", h, ":", m, ":", s, ":", f, " in Non Drop Frame.", sep="")
    return [h, m, s, f]


def decountdf(fr):
    # Validity Check
#    if fr < 0:
#        return print("Error")
    # SMPTE translation to realtime frames
    rtfr = ndframes_to_rt(fr)
    # ndfdecounting
    h = rtfr//(30*60*60)
    m = (rtfr%(30*60*60))//(30*60)
    s = (rtfr%(30*60))//30
    f = rtfr%30
#    print("The number you have inputted is:", fr, "frames.")
#    print("That's ", h, ":", m, ";", s, ";", f, " in Drop Frame.", sep="")
    return [h, m, s, f]


def dffrom2398(hh,mm,ss,ff):
    return decountdf(ntscframes_from_2398frames(count2398(hh,mm,ss,ff)))


def dfto2398(hh,mm,ss,ff):
    return decount2398(ntscframes_to_2398frames(countdf(hh,mm,ss,ff)))


def ndffrom2398(hh,mm,ss,ff):
    return decountndf(ntscframes_from_2398frames(count2398(hh,mm,ss,ff)))


def ndfto2398(hh,mm,ss,ff):
    return decount2398(ntscframes_to_2398frames(countndf(hh,mm,ss,ff)))


def ndftodf(hh,mm,ss,ff):
    return decountdf(countndf(hh,mm,ss,ff))


def dftondf(hh,mm,ss,ff):
    return decountndf(countdf(hh,mm,ss,ff))


def offspeed2398topal(hh,mm,ss,ff):
    return decountpal(count2398(hh,mm,ss,ff))


def offspeedpalto2398(hh,mm,ss,ff):
    return decount2398(countpal(hh,mm,ss,ff))


def offspeedpaltondf(hh,mm,ss,ff):
    return decountndf(ntscframes_from_2398frames(countpal(hh,mm,ss,ff)))


def offspeedndftopal(hh,mm,ss,ff):
    return decountpal(ntscframes_to_2398frames(countndf(hh,mm,ss,ff)))


def offspeedpaltodf(hh,mm,ss,ff):
    return decountdf(ntscframes_from_2398frames(countpal(hh,mm,ss,ff)))


def offspeeddftopal(hh,mm,ss,ff):
    return decountpal(ntscframes_to_2398frames(countdf(hh,mm,ss,ff)))

def get_input():
    stillneedit = True
    proper_input = ""
#    print('''
#Any input format is acceptable, use whatever separators you like (:;,. etc)
#Or you can use no seperators at all (10.00.00.00 or 10000000)
#It will properly interpret overlong values in the first spot (ie 87:25:00)
#However, for now you must use full zeros (ie 1:01:01:01 not 1:1:1:1)
#''')
    while stillneedit:
        typed_input = input(": ")
        # escape clause (HA HA HA COMEDY HOUR UP INS)
        if typed_input.lower() == "back":
            return "b"
        if typed_input.lower() == "b":
            return "b"
        if typed_input.lower() == "restart":
            return "r"
        if typed_input.lower() == "r":
            return "r"
        if typed_input.lower() == "exit":
            return "x"
        if typed_input.lower() == "x":
            return "x"
        # Remove all non-digits
        for char in typed_input:
            if char in "0123456789":
                proper_input += char
        # Check for min length
        if len(proper_input) < 2:
            print("I do what I can, but you need to enter at least 2 numbers")
            print("Retry", end="")
            proper_input = ""
        # Check hours
        elif len(proper_input) >= 8 and \
             int(proper_input[:-6]) > 24:
            print("The entered value of", \
                  int(proper_input[:-6]), \
                  "hours is over 24 hours, this is not valid")
            print("Retry", end="")
            proper_input = ""
        # Check minutes
        elif len(proper_input) > 6 and \
             int(proper_input[-min(len(proper_input), 6):-4]) > 60:
            print("The entered value of", \
                  proper_input[-6:-4], \
                  "minutes too high when Hrs entered")
            print("Retry", end="")
            proper_input = ""
        # Check seconds
        elif len(proper_input) > 4 and \
             int(proper_input[-min(len(proper_input), 4):-2]) > 60:
            print("The entered value of", \
                  proper_input[-4:-2], \
                  "seconds is too high when Min entered")
            print("Retry", end="")
            proper_input = ""
        # Check NDF frames [REDACTED, SEE BELOW]
#        elif int(proper_input[-2:len(proper_input)]) > 30:
#            print("The entered value of", proper_input[-2:len(proper_input)], \
#                  "frames is too high")
#            print("Retry", end="")
#            proper_input = ""
        # Congratulations!
        else:
            stillneedit = False

    if len(proper_input) == 2:
        # stupid idea: trying to put overflow frames into seconds
        # do not do this. be not tempted. it is dumb.
        h = 0
        m = 0
        s = 0
        f = int(proper_input[-2:])
        hr = 0

    if 4 >= len(proper_input) >= 3:
        h = 0
        # For values above 60
        m = int(proper_input[:-2]) // 60
        s = int(proper_input[:-2]) % 60
        f = int(proper_input[-2:])
        hr = 0

    if 6 >= len(proper_input) >= 5:
        # For values above 60
        h = int(proper_input[:-4]) // 60
        m = int(proper_input[:-4]) % 60
        s = int(proper_input[-4:-2])
        f = int(proper_input[-2:])
        hr = 0

    if len(proper_input) >= 7:
        h = int(proper_input[:-6])
        m = int(proper_input[-6:-4])
        s = int(proper_input[-4:-2])
        f = int(proper_input[-2:])
        if 1 <= h <=3:
            hr = 1
        elif h == 0 and 50 <= m <= 59:
            hr = 1
        elif 10 <= h <=13:
            hr = 10
        elif h == 9 and 50 <= m <= 59:
            hr = 10
        else:
            hr = 0

#    print("Interpreted timecode is", h, m, s, f, "timecode hour:", hr)

    return [h, m, s, f, hr]


def raw_input():
    stillneedit = True
    proper_input = ""
    while stillneedit:
        typed_input = input(": ")
        # escape clause (HA HA HA COMEDY HOUR UP INS)
        if typed_input.lower() == "back":
            return "b"
        if typed_input.lower() == "b":
            return "b"
        if typed_input.lower() == "restart":
            return "r"
        if typed_input.lower() == "r":
            return "r"
        if typed_input.lower() == "exit":
            return "x"
        if typed_input.lower() == "x":
            return "x"
        # Remove all non-digits
        for char in typed_input:
            if char in "0123456789":
                proper_input += char
        # Check for numbers
        if len(proper_input) < 2:
            print("I do what I can, but you need to enter at least 2 numbers")
            print("Retry", end="")
            proper_input = ""
        # Congratulations!
        else:
            stillneedit = False

#    print("You have entered", proper_input, "frames.")

    return int(proper_input)


def check_24f(h, m, s, f):
    if f >= 24:
        print(f, "frames is not a valid 24-frame timecode value")
        print("Retry", end="")
        return False
    else:
#        print(f, "is a valid 24-frame timecode value")
        return True

def check_pal(h, m, s, f):
    if f >= 25:
        print(f, "frames is not a valid PAL timecode value")
        print("Retry", end="")
        return False
    else:
#        print(f, "frames is a valid PAL timecode value")
        return True


def check_df(h, m, s, f):
    if 0 <= f <=1 and s == 0 and m % 10 != 0:
        print("{0:02}:{1:02}.{2:02}.{3:02} \
is not a valid drop-frame timecode".format(h, m, s, f))
        print("Retry", end="")
        return False
    else:
#        print(m, s, f, "is a valid drop-frame timecode")
        return True


# sort of a joke, needed for now for ui
def check_ndf(h, m, s, f):
    if f >= 30:
        print(f, "frames is not a valid timecode value")
        print("Retry", end="")
        return False
    else:
#        print(f, "is a valid timecode value")
        return True


# press any key to continue function
def anykey(prompt="Press any key to continue...", failChars=""):
    '''
    Displays a prompt to the user, then waits for the user to press a key.
    Accepts a string for prompt, and a string containing all characters for which it should return False.
    Returns False if the char pressed was in the failChars string, True otherwise.
    Raises KeyboardInterrupt on Ctrl + C'''
    from msvcrt import getch, kbhit
    print(prompt, end=' ')
    ch = getch()
    while kbhit():
        getch()
    if ch == '\x03':
        raise KeyboardInterrupt
    else:
        return (ch not in failChars)
# end anykey definition


restart = True

choice_1 = ""

# TODO: escape key
# TODO: seperation into : deliniated lists or tuples

print('''


      electron.rotoscope TIMECODE CONVERTER
Please address any problems or suggestions to him''')

while restart:

    if choice_1 == "":
        waiting = True

    while waiting:
        print('''
Choose one and press enter

A or 1: Off-speed conversions
B or 2: Normal (at-speed) timecode conversions
C or 3: Timecode to/from frame count conversions
''')
        choice_1 = input("Choice: ")
        if choice_1.lower() == "a" or choice_1.lower() == "1":
            choice_1 = "A"
            waiting = False
        elif choice_1.lower() == "b" or choice_1.lower() == "2":
            choice_1 = "B"
            waiting = False
        elif choice_1.lower() == "c" or choice_1.lower() == "3":
            choice_1 = "C"
            waiting = False
        else:
            print("Please pick a choice from the list")
            choice_1 = ""

    if choice_1 == "A":
        print('''
A or 1: 23.98PsF to PAL/25PsF/50i
B or 2: PAL/50i/25PsF to 23.98PsF
C or 3: DF-Equivalent to PAL
D or 4: PAL to DF-Equivalent

or restart/back
''')
        waiting = True
        while waiting:
            choice_2 = input("Choice: ")
            if choice_2.lower() == "a" or choice_2.lower() == "1":
                choice_2 = "AA"
                waiting = False
            elif choice_2.lower() == "b" or choice_2.lower() == "2":
                choice_2 = "AB"
                waiting = False
            elif choice_2.lower() == "c" or choice_2.lower() == "3":
                choice_2 = "AC"
                waiting = False
            elif choice_2.lower() == "d" or choice_2.lower() == "4":
                choice_2 = "AD"
                waiting = False
            elif choice_2.lower() == "restart" or choice_2.lower() == "back":
                choice_1 = ""
                choice_2 = ""
                waiting = False
            elif choice_2.lower() == "r":
                choice_1 = ""
                choice_2 = ""
                waiting = False
            else:
                print("Please pick a choice from the list")
                choice_2 = ""

    if choice_1 == "B":
        print('''
A or 1: NDF to DF
B or 2: DF to NDF
C or 3: 23.98 to DF
D or 4: DF to 23.98
E or 5: 23.98 to NDF
F or 6: NDF to 23.98

or restart/back
''')
        waiting = True
        while waiting:
            choice_2 = input("Choice: ")
            if choice_2.lower() == "a" or choice_2.lower() == "1":
                choice_2 = "BA"
                waiting = False
            elif choice_2.lower() == "b" or choice_2.lower() == "2":
                choice_2 = "BB"
                waiting = False
            elif choice_2.lower() == "c" or choice_2.lower() == "3":
                choice_2 = "BC"
                waiting = False
            elif choice_2.lower() == "d" or choice_2.lower() == "4":
                choice_2 = "BD"
                waiting = False
            elif choice_2.lower() == "e" or choice_2.lower() == "5":
                choice_2 = "BE"
                waiting = False
            elif choice_2.lower() == "f" or choice_2.lower() == "6":
                choice_2 = "BF"
                waiting = False
            elif choice_2.lower() == "restart" or choice_2.lower() == "back":
                choice_1 = ""
                choice_2 = ""
                waiting = False
            elif choice_2.lower() == "r":
                choice_1 = ""
                choice_2 = ""
                waiting = False
            else:
                print("Please pick a choice from the list")
                choice_2 = ""


    if choice_1 == "C":
        print('''
A or 1: 23.98 timecode to number of frames
B or 2: PAL timecode to number of frames
C or 3: NDF timecode to number of frames
D or 4: DF timecode to number of frames
E or 5: Number of frames to 23.98 timecode
F or 6: Number of frames to PAL timecode
G or 7: Number of frames to NDF timecode
H or 8: Number of frames to DF timecode

or restart/back
''')
        waiting = True
        while waiting:
            choice_2 = input("Choice: ")
            if choice_2.lower() == "a" or choice_2.lower() == "1":
                choice_2 = "CA"
                waiting = False
            elif choice_2.lower() == "b" or choice_2.lower() == "2":
                choice_2 = "CB"
                waiting = False
            elif choice_2.lower() == "c" or choice_2.lower() == "3":
                choice_2 = "CC"
                waiting = False
            elif choice_2.lower() == "d" or choice_2.lower() == "4":
                choice_2 = "CD"
                waiting = False
            elif choice_2.lower() == "e" or choice_2.lower() == "5":
                choice_2 = "CE"
                waiting = False
            elif choice_2.lower() == "f" or choice_2.lower() == "6":
                choice_2 = "CF"
                waiting = False
            elif choice_2.lower() == "g" or choice_2.lower() == "7":
                choice_2 = "CG"
                waiting = False
            elif choice_2.lower() == "h" or choice_2.lower() == "8":
                choice_2 = "CH"
                waiting = False
            elif choice_2.lower() == "restart" or choice_2.lower() == "back":
                choice_1 = ""
                choice_2 = ""
                waiting = False
            elif choice_2.lower() == "r":
                choice_1 = ""
                choice_2 = ""
                waiting = False
            else:
                print("Please pick a choice from the list")
                choice_2 = ""


    if choice_2 == "AA":
        print('''
    Conversion from 23.98 fps off-speed to 25 fps
    [Assuming 00 Hr or 01 Hr or 10 Hr start time if entered, 00 Hr if not]

Please enter 23.98 timecode''', end="")
        waiting = True
        while waiting:
#             s = starting values [HH, MM, SS, FF, HourCode]
#             e = ending values [HH, MM, SS, FF]
            s = get_input()
            if s == "b":
                print("Going back")
                choice_1 = "A"
                waiting = False
            elif s == "r":
                print("Restarting")
                choice_1 = ""
                waiting = False
            elif s == "x":
                print("Exiting")
                waiting = False
                restart = False
            elif check_24f(s[0], s[1], s[2], s[3]) == True:
#                print("Okay input")
                e = offspeed2398topal(s[0]-s[4], s[1], s[2], s[3])
                e[0] += s[4]
                print("\n{0[0]:02}:{0[1]:02}:{0[2]:02}:{0[3]:02} > \
{1[0]:02}:{1[1]:02}:{1[2]:02}:{1[3]:02}\n\
[23.98 offspeed to 25/PAL (assuming {0[4]:02} Hr start time)]\n".format(s, e))
                print("Enter new timecode, 'exit', 'restart' or 'back'", end="")
            else:
                pass


    if choice_2 == "AB":
        print('''
    Conversion from 25 fps off-speed to 23.98 fps
    [Assuming 00 Hr or 01 Hr or 10 Hr start time if entered, 00 Hr if not]

Please enter 25/PAL timecode''', end="")
        waiting = True
        while waiting:
            # s = starting values [HH, MM, SS, FF, HourCode]
            # e = ending values [HH, MM, SS, FF]
            s = get_input()
            if s == "b":
                print("Going back")
                choice_1 = "A"
                waiting = False
            elif s == "r":
                print("Restarting")
                choice_1 = ""
                waiting = False
            elif s == "x":
                print("Exiting")
                waiting = False
                restart = False
            elif check_pal(s[0], s[1], s[2], s[3]) == True:
#                print("Okay input")
                e = offspeedpalto2398(s[0]-s[4], s[1], s[2], s[3])
                e[0] += s[4]
                print("\n{0[0]:02}:{0[1]:02}:{0[2]:02}:{0[3]:02} > \
{1[0]:02}:{1[1]:02}:{1[2]:02}:{1[3]:02}\n\
[25/PAL offspeed to 23.98 (assuming {0[4]:02} Hr start time)]\n".format(s, e))
                print("Enter new timecode, 'exit', 'restart' or 'back'", end="")
            else:
                pass


    if choice_2 == "AC":
        print('''
    Conversion from drop-frame equivalent of 23.98 tape, off-speed to PAL
    [Assuming 00 Hr or 01 Hr or 10 Hr start time if entered, 00 Hr if not]

Please enter drop-frame timecode''', end="")
        waiting = True
        while waiting:
            # s = starting values [HH, MM, SS, FF, HourCode]
            # e = ending values [HH, MM, SS, FF]
            s = get_input()
            if s == "b":
                print("Going back")
                choice_1 = "A"
                waiting = False
            elif s == "r":
                print("Restarting")
                choice_1 = ""
                waiting = False
            elif s == "x":
                print("Exiting")
                waiting = False
                restart = False
            elif check_df(s[0], s[1], s[2], s[3]) == True:
#                print("Okay input")
                e = offspeeddftopal(s[0] - s[4], s[1], s[2], s[3])
                e[0] += s[4]
                print("\n{0[0]:02}:{0[1]:02}.{0[2]:02}.{0[3]:02} > \
{1[0]:02}:{1[1]:02}:{1[2]:02}:{1[3]:02}\n\
[DF (equivalent) offspeed to 25/PAL (assuming {0[4]:02} Hr start time)]\n".format(s, e))
                print("Enter new timecode, 'exit', 'restart' or 'back'", end="")
            else:
                pass


    if choice_2 == "AD":
        print('''
    Conversion from PAL/25 off-speed to drop-frame equivalent of 23.98 tape
    [Assuming 00 Hr or 01 Hr or 10 Hr start time if entered, 00 Hr if not]

Please enter 25/PAL timecode''', end="")
        waiting = True
        while waiting:
            # s = starting values [HH, MM, SS, FF, HourCode]
            # e = ending values [HH, MM, SS, FF]
            s = get_input()
            if s == "b":
                print("Going back")
                choice_1 = "A"
                waiting = False
            elif s == "r":
                print("Restarting")
                choice_1 = ""
                waiting = False
            elif s == "x":
                print("Exiting")
                waiting = False
                restart = False
            elif check_pal(s[0], s[1], s[2], s[3]) == True:
#                print("Okay input")
                e = offspeedpaltodf(s[0] - s[4], s[1], s[2], s[3])
                e[0] += s[4]
                print("\n{0[0]:02}:{0[1]:02}:{0[2]:02}:{0[3]:02} > \
{1[0]:02}:{1[1]:02}.{1[2]:02}.{1[3]:02}\n\
[25/PAL offspeed to DF (equivalent) (assuming {0[4]:02} Hr start time)]\n".format(s, e))
                print("Enter new timecode, 'exit', 'restart' or 'back'", end="")
            else:
                pass


    if choice_2 == "BA":
        print('''
    Conversion from Non-Drop-Frame to Drop-Frame timecode
    [Assuming 00 Hr or 01 Hr or 10 Hr start time if entered, 00 Hr if not]

Please enter NDF timecode''', end="")
        waiting = True
        while waiting:
            # s = starting values [HH, MM, SS, FF, HourCode]
            # e = ending values [HH, MM, SS, FF]
            s = get_input()
            if s == "b":
                print("Going back")
                choice_1 = "B"
                waiting = False
            elif s == "r":
                print("Restarting")
                choice_1 = ""
                waiting = False
            elif s == "x":
                print("Exiting")
                waiting = False
                restart = False
            elif check_ndf(s[0], s[1], s[2], s[3]) == True:
#                print("Okay input")
                e = ndftodf(s[0] - s[4], s[1], s[2], s[3])
                e[0] += s[4]
                print("\n{0[0]:02}:{0[1]:02}:{0[2]:02}:{0[3]:02} > \
{1[0]:02}:{1[1]:02}.{1[2]:02}.{1[3]:02}\n\
[NDF converted to DF (assuming {0[4]:02} Hr start time)]\n".format(s, e))
                print("Enter new timecode, 'exit', 'restart' or 'back'", end="")
            else:
                pass


    if choice_2 == "BB":
        print('''
    Conversion from Drop-Frame to Non-Drop-Frame timecode
    [Assuming 00 Hr or 01 Hr or 10 Hr start time if entered, 00 Hr if not]

Please enter DF timecode''', end="")
        waiting = True
        while waiting:
            # s = starting values [HH, MM, SS, FF, HourCode]
            # e = ending values [HH, MM, SS, FF]
            s = get_input()
            if s == "b":
                print("Going back")
                choice_1 = "B"
                waiting = False
            elif s == "r":
                print("Restarting")
                choice_1 = ""
                waiting = False
            elif s == "x":
                print("Exiting")
                waiting = False
                restart = False
            elif check_df(s[0], s[1], s[2], s[3]) == True:
#                print("Okay input")
                e = dftondf(s[0] - s[4], s[1], s[2], s[3])
                e[0] += s[4]
                print("\n{0[0]:02}:{0[1]:02}.{0[2]:02}.{0[3]:02} > \
{1[0]:02}:{1[1]:02}:{1[2]:02}:{1[3]:02}\n\
[DF converted to NDF (assuming {0[4]:02} Hr start time)]\n".format(s, e))
                print("Enter new timecode, 'exit', 'restart' or 'back'", end="")
            else:
                pass


    if choice_2 == "BC":
        print('''
    Conversion from 23.98 to Drop-Frame timecode
    [Assuming 00 Hr or 01 Hr or 10 Hr start time if entered, 00 Hr if not]

Please enter 23.98 timecode''', end="")
        waiting = True
        while waiting:
            # s = starting values [HH, MM, SS, FF, HourCode]
            # e = ending values [HH, MM, SS, FF]
            s = get_input()
            if s == "b":
                print("Going back")
                choice_1 = "B"
                waiting = False
            elif s == "r":
                print("Restarting")
                choice_1 = ""
                waiting = False
            elif s == "x":
                print("Exiting")
                waiting = False
                restart = False
            elif check_24f(s[0], s[1], s[2], s[3]) == True:
#                print("Okay input")
                e = dffrom2398(s[0] - s[4], s[1], s[2], s[3])
                e[0] += s[4]
                print("\n{0[0]:02}:{0[1]:02}:{0[2]:02}:{0[3]:02} > \
{1[0]:02}:{1[1]:02}.{1[2]:02}.{1[3]:02}\n\
[23.98 converted to DF (assuming {0[4]:02} Hr start time)]\n".format(s, e))
                print("Enter new timecode, 'exit', 'restart' or 'back'", end="")
            else:
                pass


    if choice_2 == "BD":
        print('''
    Conversion from Drop-Frame to 23.98 timecode
    [Assuming 00 Hr or 01 Hr or 10 Hr start time if entered, 00 Hr if not]

Please enter DF timecode''', end="")
        waiting = True
        while waiting:
            # s = starting values [HH, MM, SS, FF, HourCode]
            # e = ending values [HH, MM, SS, FF]
            s = get_input()
            if s == "b":
                print("Going back")
                choice_1 = "B"
                waiting = False
            elif s == "r":
                print("Restarting")
                choice_1 = ""
                waiting = False
            elif s == "x":
                print("Exiting")
                waiting = False
                restart = False
            elif check_df(s[0], s[1], s[2], s[3]) == True:
#                print("Okay input")
                e = dfto2398(s[0] - s[4], s[1], s[2], s[3])
                e[0] += s[4]
                print("\n{0[0]:02}:{0[1]:02}.{0[2]:02}.{0[3]:02} > \
{1[0]:02}:{1[1]:02}:{1[2]:02}:{1[3]:02}\n\
[DF converted to 23.98 (assuming {0[4]:02} Hr start time)]\n".format(s, e))
                print("Enter new timecode, 'exit', 'restart' or 'back'", end="")
            else:
                pass


    if choice_2 == "BE":
        print('''
    Conversion from 23.98 to NDF timecode

Please enter 23.98 timecode''', end="")
        waiting = True
        while waiting:
            # s = starting values [HH, MM, SS, FF, HourCode]
            # e = ending values [HH, MM, SS, FF]
            s = get_input()
            if s == "b":
                print("Going back")
                choice_1 = "B"
                waiting = False
            elif s == "r":
                print("Restarting")
                choice_1 = ""
                waiting = False
            elif s == "x":
                print("Exiting")
                waiting = False
                restart = False
            elif check_24f(s[0], s[1], s[2], s[3]) == True:
#                print("Okay input")
                e = ndffrom2398(s[0] - s[4], s[1], s[2], s[3])
                e[0] += s[4]
                print("\n{0[0]:02}:{0[1]:02}:{0[2]:02}:{0[3]:02} > \
{1[0]:02}:{1[1]:02}:{1[2]:02}:{1[3]:02}\n\
[23.98 converted to NDF (assuming {0[4]:02} Hr start time)]\n".format(s, e))
                print("Enter new timecode, 'exit', 'restart' or 'back'", end="")
            else:
                pass


    if choice_2 == "BF":
        print('''
    Conversion from Non-Drop-Frame to 23.98 timecode

Please enter NDF timecode''', end="")
        waiting = True
        while waiting:
            # s = starting values [HH, MM, SS, FF, HourCode]
            # e = ending values [HH, MM, SS, FF]
            s = get_input()
            if s == "b":
                print("Going back")
                choice_1 = "B"
                waiting = False
            elif s == "r":
                print("Restarting")
                choice_1 = ""
                waiting = False
            elif s == "x":
                print("Exiting")
                waiting = False
                restart = False
            elif check_ndf(s[0], s[1], s[2], s[3]) == True:
#                print("Okay input")
                e = ndfto2398(s[0] - s[4], s[1], s[2], s[3])
                e[0] += s[4]
                print("\n{0[0]:02}:{0[1]:02}:{0[2]:02}:{0[3]:02} > \
{1[0]:02}:{1[1]:02}:{1[2]:02}:{1[3]:02}\n\
[NDF converted to 23.98 (assuming {0[4]:02} Hr start time)]\n".format(s, e))
                print("Enter new timecode, 'exit', 'restart' or 'back'", end="")
            else:
                pass


    if choice_2 == "CA":
        print('''
    Conversion from 23.98 timecode to number of frames

Please enter 23.98 timecode''', end="")
        waiting = True
        while waiting:
            # s = starting values [HH, MM, SS, FF, HourCode]
            # e = ending value
            s = get_input()
            if s == "b":
                print("Going back")
                choice_1 = "C"
                waiting = False
            elif s == "r":
                print("Restarting")
                choice_1 = ""
                waiting = False
            elif s == "x":
                print("Exiting")
                waiting = False
                restart = False
            elif check_24f(s[0], s[1], s[2], s[3]) == True:
#                print("Okay input")
                e = count2398(s[0], s[1], s[2], s[3])
                print("\n{0[0]:02}:{0[1]:02}:{0[2]:02}:{0[3]:02} \
in 23.98 timecode is {1} frames.\n".format(s, e))
                print("Enter new timecode, 'exit', 'restart' or 'back'", end="")
            else:
                pass


    if choice_2 == "CB":
        print('''
    Conversion from 25/PAL timecode to number of frames

Please enter 25/PAL timecode''', end="")
        waiting = True
        while waiting:
            # s = starting values [HH, MM, SS, FF, HourCode]
            # e = ending value
            s = get_input()
            if s == "b":
                print("Going back")
                choice_1 = "C"
                waiting = False
            elif s == "r":
                print("Restarting")
                choice_1 = ""
                waiting = False
            elif s == "x":
                print("Exiting")
                waiting = False
                restart = False
            elif check_pal(s[0], s[1], s[2], s[3]) == True:
#                print("Okay input")
                e = countpal(s[0], s[1], s[2], s[3])
                print("\n{0[0]:02}:{0[1]:02}:{0[2]:02}:{0[3]:02} \
in PAL timecode is {1} frames.\n".format(s, e))
                print("Enter new timecode, 'exit', 'restart' or 'back'", end="")
            else:
                pass


    if choice_2 == "CC":
        print('''
    Conversion from Non-Drop-Frame timecode to number of frames

Please enter NDF timecode''', end="")
        waiting = True
        while waiting:
            # s = starting values [HH, MM, SS, FF, HourCode]
            # e = ending value
            s = get_input()
            if s == "b":
                print("Going back")
                choice_1 = "C"
                waiting = False
            elif s == "r":
                print("Restarting")
                choice_1 = ""
                waiting = False
            elif s == "x":
                print("Exiting")
                waiting = False
                restart = False
            elif check_ndf(s[0], s[1], s[2], s[3]) == True:
#                print("Okay input")
                e = countndf(s[0], s[1], s[2], s[3])
                print("\n{0[0]:02}:{0[1]:02}:{0[2]:02}:{0[3]:02} \
in NDF timecode is {1} frames.\n".format(s, e))
                print("Enter new timecode, 'exit', 'restart' or 'back'", end="")
            else:
                pass


    if choice_2 == "CD":
        print('''
    Conversion from Drop-Frame timecode to number of frames

Please enter DF timecode''', end="")
        waiting = True
        while waiting:
            # s = starting values [HH, MM, SS, FF, HourCode]
            # e = ending value
            s = get_input()
            if s == "b":
                print("Going back")
                choice_1 = "C"
                waiting = False
            elif s == "r":
                print("Restarting")
                choice_1 = ""
                waiting = False
            elif s == "x":
                print("Exiting")
                waiting = False
                restart = False
            elif check_df(s[0], s[1], s[2], s[3]) == True:
#                print("Okay input")
                e = countdf(s[0], s[1], s[2], s[3])
                print("\n{0[0]:02}:{0[1]:02}.{0[2]:02}.{0[3]:02} \
in DF timecode is {1} frames.\n".format(s, e))
                print("Enter new timecode, 'exit', 'restart' or 'back'", end="")
            else:
                pass


    if choice_2 == "CE":
        print('''
    Conversion from number of frames to 23.98 timecode

Please enter frame count''', end="")
        waiting = True
        while waiting:
            # s = starting values [HH, MM, SS, FF, HourCode]
            # e = ending value
            s = raw_input()
            if s == "b":
                print("Going back")
                choice_1 = "C"
                waiting = False
            elif s == "r":
                print("Restarting")
                choice_1 = ""
                waiting = False
            elif s == "x":
                print("Exiting")
                waiting = False
                restart = False
            else:
#                print("Okay input")
                e = decount2398(s)
                print("\n{0} frames is {1[0]:02}:{1[1]:02}:{1[2]:02}:{1[3]:02} \
in 23.98 timecode.\n".format(s, e))
                print("Enter new timecode, 'exit', 'restart' or 'back'", end="")


    if choice_2 == "CF":
        print('''
    Conversion from number of frames to PAL timecode

Please enter frame count''', end="")
        waiting = True
        while waiting:
            # s = starting values [HH, MM, SS, FF, HourCode]
            # e = ending value
            s = raw_input()
            if s == "b":
                print("Going back")
                choice_1 = "C"
                waiting = False
            elif s == "r":
                print("Restarting")
                choice_1 = ""
                waiting = False
            elif s == "x":
                print("Exiting")
                waiting = False
                restart = False
            else:
#                print("Okay input")
                e = decountpal(s)
                print("\n{0} frames is {1[0]:02}:{1[1]:02}:{1[2]:02}:{1[3]:02} \
in PAL timecode.\n".format(s, e))
                print("Enter new timecode, 'exit', 'restart' or 'back'", end="")


    if choice_2 == "CG":
        print('''
    Conversion from number of frames to NDF timecode

Please enter frame count''', end="")
        waiting = True
        while waiting:
            # s = starting values [HH, MM, SS, FF, HourCode]
            # e = ending value
            s = raw_input()
            if s == "b":
                print("Going back")
                choice_1 = "C"
                waiting = False
            elif s == "r":
                print("Restarting")
                choice_1 = ""
                waiting = False
            elif s == "x":
                print("Exiting")
                waiting = False
                restart = False
            else:
#                print("Okay input")
                e = decountndf(s)
                print("\n{0} frames is {1[0]:02}:{1[1]:02}:{1[2]:02}:{1[3]:02} \
in NDF timecode.\n".format(s, e))
                print("Enter new timecode, 'exit', 'restart' or 'back'", end="")


    if choice_2 == "CH":
        print('''
    Conversion from number of frames to DF timecode

Please enter frame count''', end="")
        waiting = True
        while waiting:
            # s = starting values [HH, MM, SS, FF, HourCode]
            # e = ending value
            s = raw_input()
            if s == "b":
                print("Going back")
                choice_1 = "C"
                waiting = False
            elif s == "r":
                print("Restarting")
                choice_1 = ""
                waiting = False
            elif s == "x":
                print("Exiting")
                waiting = False
                restart = False
            else:
#                print("Okay input")
                e = decountdf(s)
                print("\n{0} frames is {1[0]:02}:{1[1]:02}.{1[2]:02}.{1[3]:02} \
in DF timecode.\n".format(s, e))
                print("Enter new timecode, 'exit', 'restart' or 'back'", end="")
