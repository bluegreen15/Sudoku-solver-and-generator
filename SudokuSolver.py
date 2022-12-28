from random import *
GanzSudoku = []

Reihe0 = []
Reihe1 = []
Reihe2 = []
Reihe3 = []
Reihe4 = []
Reihe5 = []
Reihe6 = []
Reihe7 = []
Reihe8 = []

Spalte0 = []
Spalte1 = []
Spalte2 = []
Spalte3 = []
Spalte4 = []
Spalte5 = []
Spalte6 = []
Spalte7 = []
Spalte8 = []

Kasten0 = []
Kasten1 = []
Kasten2 = []
Kasten3 = []
Kasten4 = []
Kasten5 = []
Kasten6 = []
Kasten7 = []
Kasten8 = []

advanced_debug_protocol = False
generator_mode = True

imptimer = 0
generating_timer = 0
#
#
def GanzzahligeDiv(zahl1, zahl2):
    return int((zahl1 - (zahl1 % zahl2)) / zahl2)


def printCurrentSudoku():
    r2 = ""
    for row1 in GanzSudoku[0:9]:
        r2 += str(row1.Zahl)
    print(r2)
    r2 = ""
    for row2 in GanzSudoku[9:18]:
        r2 += str(row2.Zahl)
    print(r2)
    r2 = ""
    for row3 in GanzSudoku[18:27]:
        r2 += str(row3.Zahl)
    print(r2)
    r2 = ""
    for row4 in GanzSudoku[27:36]:
        r2 += str(row4.Zahl)
    print(r2)
    r2 = ""
    for row5 in GanzSudoku[36:45]:
        r2 += str(row5.Zahl)
    print(r2)
    r2 = ""
    for row6 in GanzSudoku[45:54]:
        r2 += str(row6.Zahl)
    print(r2)
    r2 = ""
    for row7 in GanzSudoku[54:63]:
        r2 += str(row7.Zahl)
    print(r2)
    r2 = ""
    for row9 in GanzSudoku[63:72]:
        r2 += str(row9.Zahl)
    print(r2)
    r2 = ""
    for row9 in GanzSudoku[72:81]:
        r2 += str(row9.Zahl)
    print(r2)


def printStatusinfo(which):
    if which == 1:
        if generator_mode:
            print("=====###=====\nEnabling the generator mode...")
            print("=====###=====\nClear whole sudoku:")
        else:
            print("=====###=====\nLoading sudoku...")
            print("=====###=====\nOutputting start sudoku: ")
    elif which == 2:
        if generator_mode:
            print("=====###=====\nStarting the generation of a new sudoku...")
        else:
            print("=====###=====\nStarting solving of sudoku...")
        StartLoesenSudoku()
        printStatusinfo(3)
    elif which == 3:
        print("Sudoku successfully solved!")
    elif which == 4:
        print("=====###=====\nOutputting solved sudoku:")


def StartLoesenSudoku():
    if generator_mode:
        for i in range(0, 81):
            GanzSudoku[i].resetAll()
        generateSudoku()
    else:
        r = 0
        while not SudokuGeloest():
            r += 1
            before_sudoku = GanzSudoku
            Loesen()
            print("Solving...")
            if advanced_debug_protocol:
                print("\nSudoku after Round" + str(r) + ":")
                printCurrentSudoku()
                print("\n")
                for i in range(0, 81):
                    all_changes = ""
                    if before_sudoku[i].Zahl != GanzSudoku[i].Zahl:
                        all_changes += "x: " + str(GanzSudoku[i].Reihe) + "; y: " + str(GanzSudoku[i].Spalte) \
                                   + " changed from " + str(before_sudoku[i].Zahl) + " to " + str(GanzSudoku[i].Zahl) \
                                   + "; Reason: " + GanzSudoku[i].change_reason
                        print(all_changes)


#
def Loesen():
    global imptimer
    one_number_changed = False
    for sb in range(0, 81):
        temp_int_strg = GanzSudoku[sb].Zahl
        GanzSudoku[sb].SetThePossibles()
        GanzSudoku[sb].SetNumberIfPossible()
        if temp_int_strg != GanzSudoku[sb].Zahl:
            one_number_changed = True
    if not one_number_changed:
        imptimer += 1
        if imptimer >= 3:
            print("Sudoku is impossible. Stop the program.")
            exit()
    else:
        imptimer = 0


#

def SudokuGeloest():
    geloest = True
    for everyfield in GanzSudoku:
        if everyfield.Zahl == 0:
            geloest = False

    return geloest
#
#
#

def generateSudoku():
    global generating_timer
    generating_timer += 1
    if generating_timer >= 250:
        print("===#####===")
        print("Could not generate a sudoku!\nPlease start a new try.")
        print("\nNotice: The chance for a generated sudoku is about 2%.\nSo you probably have to do some attemps.")
        exit()
    imptimer2 = 0
    one_number_changed = False
    randindex = randint(0, 80)
    while GanzSudoku[randindex].Zahl != 0:
        randindex = randint(0, 80)

    randnum = randint(1, 9)

    global timer
    timer = 0
    while not numberPossibleAt(randindex, randnum):
        randnum = randint(1, 9)
        timer += 1
        if timer >= 10:
            timer = 0
            randnum = 0
            break
    GanzSudoku[randindex].Zahl = randnum
    printCurrentSudoku()
    print("Generating...")

    before_sudoku = []
    for j in range(0, 81):
        before_sudoku.append(GanzSudoku[j].Zahl)
    while not SudokuGeloest():
        for sb in range(0, 81):
            temp_int_strg = GanzSudoku[sb].Zahl
            GanzSudoku[sb].SetThePossibles()
            GanzSudoku[sb].SetNumberIfPossible()
            if temp_int_strg != GanzSudoku[sb].Zahl:
                one_number_changed = True
        if not one_number_changed:
            imptimer2 += 1
            if imptimer2 >= 3:
                break
        else:
            imptimer2 = 0
            one_number_changed = False

    if SudokuGeloest():
        print("Sudoku succesfully generated!")
        printCurrentSudoku()
        exit()
    for i in range(0, 81):
        if GanzSudoku[i].Zahl != before_sudoku[i]:
            GanzSudoku[i].Zahl = before_sudoku[i]
    generateSudoku()


def numberPossibleAt(ind, nu):   # Sagt ob eine Zahl an GanzSudoku[ind] möglich ist.
    if GanzSudoku[ind].Reihe == 0:
        for feldR0 in range(0, 9):
            GanzSudoku[feldR0].SetThePossibles()
            if len(GanzSudoku[feldR0].possible) <= 1:
                return False
            if GanzSudoku[feldR0].Zahl == nu:
                return False

    elif GanzSudoku[ind].Reihe == 1:
        for feldR1 in Reihe1:
            feldR1.SetThePossibles()
            if len(feldR1.possible) <= 1:
                return False
            if feldR1.Zahl == nu:
                return False

    elif GanzSudoku[ind].Reihe == 2:
        for feldR2 in Reihe2:
            feldR2.SetThePossibles()
            if len(feldR2.possible) <= 1:
               return False
            if feldR2.Zahl == nu:
                return False

    elif GanzSudoku[ind].Reihe == 3:
        for feldR3 in Reihe3:
            feldR3.SetThePossibles()
            if len(feldR3.possible) <= 1:
               return False
            if feldR3.Zahl == nu:
                return False

    elif GanzSudoku[ind].Reihe == 4:
        for feldR4 in Reihe4:
            feldR4.SetThePossibles()
            #if len(feldR4.possible) <= 1:
             #   return False
            if feldR4.Zahl == nu:
                return False

    elif GanzSudoku[ind].Reihe == 5:
        for feldR5 in Reihe5:
            feldR5.SetThePossibles()
            #if len(feldR5.possible) <= 1:
             #   return False
            if feldR5.Zahl == nu:
                return False

    elif GanzSudoku[ind].Reihe == 6:
        for feldR6 in Reihe6:
            feldR6.SetThePossibles()
            if len(feldR6.possible) <= 1:
               return False
            if feldR6.Zahl == nu:
                return False

    elif GanzSudoku[ind].Reihe == 7:
        for fieldR7 in Reihe7:
            fieldR7.SetThePossibles()
            if len(fieldR7.possible) <= 1:
               return False
            if fieldR7.Zahl == nu:
                return False

    else:
        for feldR8 in Reihe8:
            feldR8.SetThePossibles()
            if len(feldR8.possible) <= 1:
                return False
            if feldR8.Zahl == nu:
                return False

##############################################

    if GanzSudoku[ind].Spalte == 0:
        for feldR0 in Spalte0:
            feldR0.SetThePossibles()
            #if len(feldR0.possible) <= 1:
             #   return False
            if feldR0.Zahl == nu:
                return False

    elif GanzSudoku[ind].Spalte == 1:
        for feldR1 in Spalte1:
            feldR1.SetThePossibles()
            if len(feldR1.possible) <= 1:
                return False
            if feldR1.Zahl == nu:
                return False

    elif GanzSudoku[ind].Spalte == 2:
        for feldR2 in Spalte2:
            feldR2.SetThePossibles()
            if len(feldR2.possible) <= 1:
                return False
            if feldR2.Zahl == nu:
                return False

    elif GanzSudoku[ind].Spalte == 3:
        for feldR3 in Spalte3:
            feldR3.SetThePossibles()
            if len(feldR3.possible) <= 1:
                return False
            if feldR3.Zahl == nu:
                return False

    elif GanzSudoku[ind].Spalte == 4:
        for feldR4 in Spalte4:
            feldR4.SetThePossibles()
            if len(feldR4.possible) <= 1:
                return False
            if feldR4.Zahl == nu:
                return False

    elif GanzSudoku[ind].Spalte == 5:
        for feldR5 in Spalte5:
            feldR5.SetThePossibles()
            if len(feldR5.possible) <= 1:
                return False
            if feldR5.Zahl == nu:
                return False

    elif GanzSudoku[ind].Spalte == 6:
        for feldR6 in Spalte6:
            feldR6.SetThePossibles()
            if len(feldR6.possible) <= 1:
                return False
            if feldR6.Zahl == nu:
                return False

    elif GanzSudoku[ind].Spalte == 7:
        for fieldR7 in Spalte7:
            fieldR7.SetThePossibles()
           # if len(fieldR7.possible) <= 1:
            #    return False
            if fieldR7.Zahl == nu:
                return False

    else:
        for feldR8 in Spalte8:
            feldR8.SetThePossibles()
            if len(feldR8.possible) <= 1:
                return False
            if feldR8.Zahl == nu:
                return False

###########################################

    if GanzSudoku[ind].Kasten == 0:
        for feldR0 in Kasten0:
            if feldR0.Zahl == nu:
                return False

    elif GanzSudoku[ind].Kasten == 1:
        for feldR1 in Kasten1:
            if feldR1.Zahl == nu:
                return False

    elif GanzSudoku[ind].Kasten == 2:
        for feldR2 in Kasten2:
            if feldR2.Zahl == nu:
                return False

    elif GanzSudoku[ind].Kasten == 3:
        for feldR3 in Kasten3:
            if feldR3.Zahl == nu:
                return False

    elif GanzSudoku[ind].Kasten == 4:
        for feldR4 in Kasten4:
            if feldR4.Zahl == nu:
                return False

    elif GanzSudoku[ind].Kasten == 5:
        for feldR5 in Kasten5:
            if feldR5.Zahl == nu:
                return False

    elif GanzSudoku[ind].Kasten == 6:
        for feldR6 in Kasten6:
            if feldR6.Zahl == nu:
                return False

    elif GanzSudoku[ind].Kasten == 7:
        for fieldR7 in Kasten7:
            if fieldR7.Zahl == nu:
                return False

    else:
        for feldR8 in Kasten8:
            if feldR8.Zahl == nu:
                return False

    return True


class Feld:  # KLassendef
    Zahl = 0  # Zahl

    possible = []  # Moeglich?

    Kasten = 88

    Reihe = 0
    Spalte = 0

    change_reason = ""

    def __init__(self, xx, yy):
        self.Reihe = xx
        self.Spalte = yy
        self.possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        if self.Reihe < 3:

            if self.Spalte < 3:
                self.Kasten = 0

            elif self.Spalte > 5:
                self.Kasten = 2
            else:
                self.Kasten = 1

        #
        elif self.Reihe > 5:

            if self.Spalte < 3:
                self.Kasten = 6

            elif self.Spalte > 5:
                self.Kasten = 8
            else:
                self.Kasten = 7

                #
        else:

            if self.Spalte < 3:
                self.Kasten = 3

            elif self.Spalte > 5:
                self.Kasten = 5
            else:
                self.Kasten = 4

    def SetThePossibles(self):
        if self.Zahl == 0:
            # Reihen
            if self.Reihe == 0:
                for feldR0 in Reihe0:
                    if feldR0.Spalte != self.Spalte:
                        if feldR0.Zahl != 0:
                            if feldR0.Zahl in self.possible:
                                self.possible.remove(feldR0.Zahl)

            elif self.Reihe == 1:
                for feldR1 in Reihe1:
                    if feldR1.Spalte != self.Spalte:
                        if feldR1.Zahl != 0:
                            if feldR1.Zahl in self.possible:
                                if self.Reihe == 0 and self.Spalte == 0:
                                    print(self.possible)
                                self.possible.remove(feldR1.Zahl)
                                if self.Reihe == 0 and self.Spalte == 0:
                                    print(self.possible)

            elif self.Reihe == 2:
                for feldR2 in Reihe2:
                    if feldR2.Spalte != self.Spalte:
                        if feldR2.Zahl != 0:
                            if feldR2.Zahl in self.possible:
                                self.possible.remove(feldR2.Zahl)

            elif self.Reihe == 3:
                for feldR3 in Reihe3:
                    if feldR3.Spalte != self.Spalte:
                        if feldR3.Zahl != 0:
                            if feldR3.Zahl in self.possible:
                                self.possible.remove(feldR3.Zahl)

            elif self.Reihe == 4:
                for feldR4 in Reihe4:
                    if feldR4.Spalte != self.Spalte:
                        if feldR4.Zahl != 0:
                            if feldR4.Zahl in self.possible:
                                self.possible.remove(feldR4.Zahl)

            elif self.Reihe == 5:
                for feldR5 in Reihe5:
                    if feldR5.Spalte != self.Spalte:
                        if feldR5.Zahl != 0:
                            if feldR5.Zahl in self.possible:
                                self.possible.remove(feldR5.Zahl)

            elif self.Reihe == 6:
                for feldR6 in Reihe6:
                    if feldR6.Spalte != self.Spalte:
                        if feldR6.Zahl != 0:
                            if feldR6.Zahl in self.possible:
                                self.possible.remove(feldR6.Zahl)

            elif self.Reihe == 7:
                for fieldR7 in Reihe7:
                    if fieldR7.Spalte != self.Spalte:
                        if fieldR7.Zahl != 0:
                            if fieldR7.Zahl in self.possible:
                                self.possible.remove(fieldR7.Zahl)

            else:
                for feldR8 in Reihe8:
                    if feldR8.Spalte != self.Spalte:
                        if feldR8.Zahl != 0:
                            if feldR8.Zahl in self.possible:
                                self.possible.remove(feldR8.Zahl)

            # Spalten
            if self.Spalte == 0:
                for feldS0 in Spalte0:
                    if feldS0.Reihe != self.Reihe:
                        if feldS0.Zahl != 0:
                            if feldS0.Zahl in self.possible:
                                self.possible.remove(feldS0.Zahl)

            elif self.Spalte == 1:
                for feldS1 in Spalte1:
                    if feldS1.Reihe != self.Reihe:
                        if feldS1.Zahl != 0:
                            if feldS1.Zahl in self.possible:
                                self.possible.remove(feldS1.Zahl)

            elif self.Spalte == 2:
                for feldS2 in Spalte2:
                    if feldS2.Reihe != self.Reihe:
                        if feldS2.Zahl != 0:
                            if feldS2.Zahl in self.possible:
                                self.possible.remove(feldS2.Zahl)

            elif self.Spalte == 3:
                for feldS3 in Spalte3:
                    if feldS3.Reihe != self.Reihe:
                        if feldS3.Zahl != 0:
                            if feldS3.Zahl in self.possible:
                                self.possible.remove(feldS3.Zahl)

            elif self.Spalte == 4:
                for feldS4 in Spalte4:
                    if feldS4.Reihe != self.Reihe:
                        if feldS4.Zahl != 0:
                            if feldS4.Zahl in self.possible:
                                self.possible.remove(feldS4.Zahl)

            elif self.Spalte == 5:
                for feldS5 in Spalte5:
                    if feldS5.Reihe != self.Reihe:
                        if feldS5.Zahl != 0:
                            if feldS5.Zahl in self.possible:
                                self.possible.remove(feldS5.Zahl)

            elif self.Spalte == 6:
                for feldS6 in Spalte6:
                    if feldS6.Reihe != self.Reihe:
                        if feldS6.Zahl != 0:
                            if feldS6.Zahl in self.possible:
                                self.possible.remove(feldS6.Zahl)

            elif self.Spalte == 7:
                for fieldS7 in Spalte7:
                    if fieldS7.Reihe != self.Reihe:
                        if fieldS7.Zahl != 0:
                            if fieldS7.Zahl in self.possible:
                                self.possible.remove(fieldS7.Zahl)

            else:
                for feldS8 in Spalte8:
                    if feldS8.Reihe != self.Reihe:
                        if feldS8.Zahl != 0:
                            if feldS8.Zahl in self.possible:
                                self.possible.remove(feldS8.Zahl)

            # Kästen
            if self.Kasten == 0:
                for feldK0 in Kasten0:
                    if feldK0.Reihe != self.Reihe and feldK0.Spalte != self.Spalte:
                        if feldK0.Zahl != 0:
                            if feldK0.Zahl in self.possible:
                                self.possible.remove(feldK0.Zahl)

            elif self.Kasten == 1:
                for feldK1 in Kasten1:
                    if feldK1.Reihe != self.Reihe and feldK1.Spalte != self.Spalte:
                        if feldK1.Zahl != 0:
                            if feldK1.Zahl in self.possible:
                                self.possible.remove(feldK1.Zahl)

            elif self.Kasten == 2:
                for feldK2 in Kasten2:
                    if feldK2.Reihe != self.Reihe and feldK2.Spalte != self.Spalte:
                        if feldK2.Zahl != 0:
                            if feldK2.Zahl in self.possible:
                                self.possible.remove(feldK2.Zahl)

            elif self.Kasten == 3:
                for feldK3 in Kasten3:
                    if feldK3.Reihe != self.Reihe and feldK3.Spalte != self.Spalte:
                        if feldK3.Zahl != 0:
                            if feldK3.Zahl in self.possible:
                                self.possible.remove(feldK3.Zahl)

            elif self.Kasten == 4:
                for feldK4 in Kasten4:
                    if feldK4.Reihe != self.Reihe and feldK4.Spalte != self.Spalte:
                        if feldK4.Zahl != 0:
                            if feldK4.Zahl in self.possible:
                                self.possible.remove(feldK4.Zahl)

            elif self.Kasten == 5:
                for feldK5 in Kasten5:
                    if feldK5.Reihe != self.Reihe and feldK5.Spalte != self.Spalte:
                        if feldK5.Zahl != 0:
                            if feldK5.Zahl in self.possible:
                                self.possible.remove(feldK5.Zahl)

            elif self.Kasten == 6:
                for feldK6 in Kasten6:
                    if feldK6.Reihe != self.Reihe and feldK6.Spalte != self.Spalte:
                        if feldK6.Zahl != 0:
                            if feldK6.Zahl in self.possible:
                                self.possible.remove(feldK6.Zahl)

            elif self.Kasten == 7:
                for fieldK7 in Kasten7:
                    if fieldK7.Reihe != self.Reihe and fieldK7.Spalte != self.Spalte:
                        if fieldK7.Zahl != 0:
                            if fieldK7.Zahl in self.possible:
                                self.possible.remove(fieldK7.Zahl)

            elif self.Kasten == 8:
                for feldK8 in Kasten8:
                    if feldK8.Reihe != self.Reihe and feldK8.Spalte != self.Spalte:
                        if feldK8.Zahl != 0:
                            if feldK8.Zahl in self.possible:
                                self.possible.remove(feldK8.Zahl)

    #
    #
    #
    def SetNumberIfPossible(self):
        inReiheVertreten = []
        inSpalteVertreten = []
        inKastenVertreten = []
        if self.Zahl == 0:
            if len(self.possible) == 1:
                self.Zahl = self.possible[0]
                if advanced_debug_protocol:
                    self.change_reason = "possible-unique"
                    print("x: " + str(self.Reihe) + "; y: " + str(self.Spalte) + "; box: " + str(self.Kasten) +
                          "; --> " + str(self.Zahl) + "; reason: " + self.change_reason)
                return
            else:
                if self.Reihe == 0:
                    for feldR0 in Reihe0:
                        if feldR0.Spalte != self.Spalte:
                            if feldR0.Zahl == 0:
                                for pos in feldR0.possible:
                                    if pos not in inReiheVertreten:
                                        inReiheVertreten.append(pos)

                elif self.Reihe == 1:
                    for feldR1 in Reihe1:
                        if feldR1.Spalte != self.Spalte:
                            if feldR1.Zahl == 0:
                                for pos in feldR1.possible:
                                    if pos not in inReiheVertreten:
                                        inReiheVertreten.append(pos)

                elif self.Reihe == 2:
                    for feldR2 in Reihe2:
                        if feldR2.Spalte != self.Spalte:
                            if feldR2.Zahl == 0:
                                for pos in feldR2.possible:
                                    if pos not in inReiheVertreten:
                                        inReiheVertreten.append(pos)

                elif self.Reihe == 3:
                    for feldR3 in Reihe3:
                        if feldR3.Spalte != self.Spalte:
                            if feldR3.Zahl == 0:
                                for pos in feldR3.possible:
                                    if pos not in inReiheVertreten:
                                        inReiheVertreten.append(pos)

                elif self.Reihe == 4:
                    for feldR4 in Reihe4:
                        if feldR4.Spalte != self.Spalte:
                            if feldR4.Zahl == 0:
                                for pos in feldR4.possible:
                                    if pos not in inReiheVertreten:
                                        inReiheVertreten.append(pos)

                elif self.Reihe == 5:
                    for feldR5 in Reihe5:
                        if feldR5.Spalte != self.Spalte:
                            if feldR5.Zahl == 0:
                                for pos in feldR5.possible:
                                    if pos not in inReiheVertreten:
                                        inReiheVertreten.append(pos)

                elif self.Reihe == 6:
                    for feldR6 in Reihe6:
                        if feldR6.Spalte != self.Spalte:
                            if feldR6.Zahl == 0:
                                for pos in feldR6.possible:
                                    if pos not in inReiheVertreten:
                                        inReiheVertreten.append(pos)

                elif self.Reihe == 7:
                    for fieldR7 in Reihe7:
                        if fieldR7.Spalte != self.Spalte:
                            if fieldR7.Zahl == 0:
                                for pos in fieldR7.possible:
                                    if pos not in inReiheVertreten:
                                        inReiheVertreten.append(pos)

                else:
                    for feldR8 in Reihe8:
                        if feldR8.Spalte != self.Spalte:
                            if feldR8.Zahl == 0:
                                for pos in feldR8.possible:
                                    if pos not in inReiheVertreten:
                                        inReiheVertreten.append(pos)

                                        #

                #
                if self.Spalte == 0:
                    for feldR0 in Spalte0:
                        if feldR0.Reihe != self.Reihe:
                            if feldR0.Zahl == 0:
                                for pos in feldR0.possible:
                                    if pos not in inSpalteVertreten:
                                        inSpalteVertreten.append(pos)

                elif self.Spalte == 1:
                    for feldR0 in Spalte1:
                        if feldR0.Reihe != self.Reihe:
                            if feldR0.Zahl == 0:
                                for pos in feldR0.possible:
                                    if pos not in inSpalteVertreten:
                                        inSpalteVertreten.append(pos)

                elif self.Spalte == 2:
                    for feldR0 in Spalte2:
                        if feldR0.Reihe != self.Reihe:
                            if feldR0.Zahl == 0:
                                for pos in feldR0.possible:
                                    if pos not in inSpalteVertreten:
                                        inSpalteVertreten.append(pos)

                elif self.Spalte == 3:
                    for feldR0 in Spalte3:
                        if feldR0.Reihe != self.Reihe:
                            if feldR0.Zahl == 0:
                                for pos in feldR0.possible:
                                    if pos not in inSpalteVertreten:
                                        inSpalteVertreten.append(pos)
                    #

                elif self.Spalte == 4:
                    for feldR0 in Spalte4:
                        if feldR0.Reihe != self.Reihe:
                            if feldR0.Zahl == 0:
                                for pos in feldR0.possible:
                                    if pos not in inSpalteVertreten:
                                        inSpalteVertreten.append(pos)

                elif self.Spalte == 5:
                    for feldR5 in Spalte5:
                        if feldR5.Reihe != self.Reihe:
                            if feldR5.Zahl == 0:
                                for pos in feldR5.possible:
                                    if pos not in inSpalteVertreten:
                                        inSpalteVertreten.append(pos)

                elif self.Spalte == 6:
                    for feldR6 in Spalte6:
                        if feldR6.Reihe != self.Reihe:
                            if feldR6.Zahl == 0:
                                for pos in feldR6.possible:
                                    if pos not in inSpalteVertreten:
                                        inSpalteVertreten.append(pos)

                elif self.Spalte == 7:
                    for fieldR7 in Spalte7:
                        if fieldR7.Reihe != self.Reihe:
                            if fieldR7.Zahl == 0:
                                for pos in fieldR7.possible:
                                    if pos not in inSpalteVertreten:
                                        inSpalteVertreten.append(pos)

                else:
                    for feldR8 in Spalte8:
                        if feldR8.Reihe != self.Reihe:
                            if feldR8.Zahl == 0:
                                for pos in feldR8.possible:
                                    if pos not in inSpalteVertreten:
                                        inSpalteVertreten.append(pos)

                                        #
                    #
                #

                if self.Kasten == 0:
                    for fieldK0 in Kasten0:
                        if not (fieldK0.Reihe == self.Reihe and fieldK0.Spalte == self.Spalte):
                            if fieldK0.Zahl == 0:
                                for pos in fieldK0.possible:
                                    if pos not in inKastenVertreten:
                                        inKastenVertreten.append(pos)

                elif self.Kasten == 1:
                    for fieldK1 in Kasten1:
                        if not (fieldK1.Reihe == self.Reihe and fieldK1.Spalte == self.Spalte):
                            if fieldK1.Zahl == 0:
                                for pos in fieldK1.possible:
                                    if pos not in inKastenVertreten:
                                        inKastenVertreten.append(pos)

                elif self.Kasten == 2:
                    for fieldK2 in Kasten2:
                        if not (fieldK2.Reihe == self.Reihe and fieldK2.Spalte == self.Spalte):
                            if fieldK2.Zahl == 0:
                                for pos in fieldK2.possible:
                                    if pos not in inKastenVertreten:
                                        inKastenVertreten.append(pos)

                elif self.Kasten == 3:
                    for fieldK3 in Kasten3:
                        if not (fieldK3.Reihe == self.Reihe and fieldK3.Spalte == self.Spalte):
                            if fieldK3.Zahl == 0:
                                for pos in fieldK3.possible:
                                    if pos not in inKastenVertreten:
                                        inKastenVertreten.append(pos)

                elif self.Kasten == 4:
                    for fieldK4 in Kasten4:
                        if not (fieldK4.Reihe == self.Reihe and fieldK4.Spalte == self.Spalte):
                            if fieldK4.Zahl == 0:
                                for pos in fieldK4.possible:
                                    if pos not in inKastenVertreten:
                                        inKastenVertreten.append(pos)

                elif self.Kasten == 5:
                    for fieldK5 in Kasten5:
                        if not (fieldK5.Reihe == self.Reihe and fieldK5.Spalte == self.Spalte):
                            if fieldK5.Zahl == 0:
                                for pos in fieldK5.possible:
                                    if pos not in inKastenVertreten:
                                        inKastenVertreten.append(pos)

                elif self.Kasten == 6:
                    for fieldK6 in Kasten6:
                        if not (fieldK6.Reihe == self.Reihe and fieldK6.Spalte == self.Spalte):
                            if fieldK6.Zahl == 0:
                                for pos in fieldK6.possible:
                                    if pos not in inKastenVertreten:
                                        inKastenVertreten.append(pos)

                elif self.Kasten == 7:
                    for fieldK7 in Kasten7:
                        if not (fieldK7.Reihe == self.Reihe and fieldK7.Spalte == self.Spalte):
                            if fieldK7.Zahl == 0:
                                for pos in fieldK7.possible:
                                    if pos not in inKastenVertreten:
                                        inKastenVertreten.append(pos)

                else:
                    for fieldK8 in Kasten8:
                        if not (fieldK8.Reihe == self.Reihe and fieldK8.Spalte == self.Spalte):
                            if fieldK8.Zahl == 0:
                                for pos in fieldK8.possible:
                                    if pos not in inKastenVertreten:
                                        inKastenVertreten.append(pos)
                #

                for num in self.possible:
                    if num not in inReiheVertreten:
                        self.Zahl = num
                        if advanced_debug_protocol:
                            self.change_reason = "row-unique"
                            print("x: " + str(self.Reihe) + "; y: " + str(self.Spalte) + "; box: " + str(self.Kasten) +
                                  "; --> " + str(self.Zahl) + "; reason: " + self.change_reason)
                        return

                for numb in self.possible:
                    if numb not in inSpalteVertreten:
                        self.Zahl = numb
                        if advanced_debug_protocol:
                            self.change_reason = "column-unique"
                            print("x: " + str(self.Reihe) + "; y: " + str(self.Spalte) + "; box: " + str(self.Kasten) +
                                  "; --> " + str(self.Zahl) + "; reason: " + self.change_reason)
                        return

                for number in self.possible:
                    if number not in inKastenVertreten:
                        self.Zahl = number
                        if advanced_debug_protocol:
                            self.change_reason = "box-unique"
                            print("x: " + str(self.Reihe) + "; y: " + str(self.Spalte) + "; box: " + str(self.Kasten) +
                                  "; --> " + str(self.Zahl) + "; reason: " + self.change_reason)
                        return
        else:
            self.change_reason = "Was already solved"
        return

    def resetAll(self):
        self.Zahl = 0


#
#
#
for x in range(0, 81):
    GanzSudoku.append(Feld(GanzzahligeDiv(x, 9), x % 9))

# Bestimmen bestimmter Felder
if not generator_mode:
    GanzSudoku[0].Zahl = 0
    GanzSudoku[1].Zahl = 8
    GanzSudoku[2].Zahl = 9
    GanzSudoku[3].Zahl = 0
    GanzSudoku[4].Zahl = 0
    GanzSudoku[5].Zahl = 0
    GanzSudoku[6].Zahl = 3
    GanzSudoku[7].Zahl = 4
    GanzSudoku[8].Zahl = 0

    GanzSudoku[9].Zahl = 0
    GanzSudoku[10].Zahl = 0
    GanzSudoku[11].Zahl = 0
    GanzSudoku[12].Zahl = 2
    GanzSudoku[13].Zahl = 0
    GanzSudoku[14].Zahl = 0
    GanzSudoku[15].Zahl = 0
    GanzSudoku[16].Zahl = 0
    GanzSudoku[17].Zahl = 0

    GanzSudoku[18].Zahl = 0
    GanzSudoku[19].Zahl = 0
    GanzSudoku[20].Zahl = 2
    GanzSudoku[21].Zahl = 0
    GanzSudoku[22].Zahl = 0
    GanzSudoku[23].Zahl = 0
    GanzSudoku[24].Zahl = 7
    GanzSudoku[25].Zahl = 0
    GanzSudoku[26].Zahl = 0

    GanzSudoku[27].Zahl = 0
    GanzSudoku[28].Zahl = 0
    GanzSudoku[29].Zahl = 0
    GanzSudoku[30].Zahl = 5
    GanzSudoku[31].Zahl = 3
    GanzSudoku[32].Zahl = 0
    GanzSudoku[33].Zahl = 6
    GanzSudoku[34].Zahl = 0
    GanzSudoku[35].Zahl = 4

    GanzSudoku[36].Zahl = 0
    GanzSudoku[37].Zahl = 0
    GanzSudoku[38].Zahl = 0
    GanzSudoku[39].Zahl = 8
    GanzSudoku[40].Zahl = 6
    GanzSudoku[41].Zahl = 4
    GanzSudoku[42].Zahl = 0
    GanzSudoku[43].Zahl = 1
    GanzSudoku[44].Zahl = 0

    GanzSudoku[45].Zahl = 0
    GanzSudoku[46].Zahl = 0
    GanzSudoku[47].Zahl = 0
    GanzSudoku[48].Zahl = 7
    GanzSudoku[49].Zahl = 9
    GanzSudoku[50].Zahl = 0
    GanzSudoku[51].Zahl = 0
    GanzSudoku[52].Zahl = 0
    GanzSudoku[53].Zahl = 0

    GanzSudoku[54].Zahl = 8
    GanzSudoku[55].Zahl = 4
    GanzSudoku[56].Zahl = 0
    GanzSudoku[57].Zahl = 6
    GanzSudoku[58].Zahl = 0
    GanzSudoku[59].Zahl = 0
    GanzSudoku[60].Zahl = 0
    GanzSudoku[61].Zahl = 2
    GanzSudoku[62].Zahl = 9

    GanzSudoku[63].Zahl = 0
    GanzSudoku[64].Zahl = 0
    GanzSudoku[65].Zahl = 6
    GanzSudoku[66].Zahl = 0
    GanzSudoku[67].Zahl = 0
    GanzSudoku[68].Zahl = 0
    GanzSudoku[69].Zahl = 0
    GanzSudoku[70].Zahl = 0
    GanzSudoku[71].Zahl = 5

    GanzSudoku[72].Zahl = 2
    GanzSudoku[73].Zahl = 0
    GanzSudoku[74].Zahl = 0
    GanzSudoku[75].Zahl = 3
    GanzSudoku[76].Zahl = 0
    GanzSudoku[77].Zahl = 0
    GanzSudoku[78].Zahl = 0
    GanzSudoku[79].Zahl = 0
    GanzSudoku[80].Zahl = 0

for y in range(0, 81):
    if GanzSudoku[y].Kasten == 0:
        Kasten0.append(GanzSudoku[y])
    elif GanzSudoku[y].Kasten == 1:
        Kasten1.append(GanzSudoku[y])
    elif GanzSudoku[y].Kasten == 2:
        Kasten2.append(GanzSudoku[y])
    elif GanzSudoku[y].Kasten == 3:
        Kasten3.append(GanzSudoku[y])
    elif GanzSudoku[y].Kasten == 4:
        Kasten4.append(GanzSudoku[y])
    elif GanzSudoku[y].Kasten == 5:
        Kasten5.append(GanzSudoku[y])
    elif GanzSudoku[y].Kasten == 6:
        Kasten6.append(GanzSudoku[y])
    elif GanzSudoku[y].Kasten == 7:
        Kasten7.append(GanzSudoku[y])
    else:
        Kasten8.append(GanzSudoku[y])

    #
    #
for y2 in range(0, 81):
    if GanzSudoku[y2].Reihe == 0:
        Reihe0.append(GanzSudoku[y2])
    elif GanzSudoku[y2].Reihe == 1:
        Reihe1.append(GanzSudoku[y2])
    elif GanzSudoku[y2].Reihe == 2:
        Reihe2.append(GanzSudoku[y2])
    elif GanzSudoku[y2].Reihe == 3:
        Reihe3.append(GanzSudoku[y2])
    elif GanzSudoku[y2].Reihe == 4:
        Reihe4.append(GanzSudoku[y2])
    elif GanzSudoku[y2].Reihe == 5:
        Reihe5.append(GanzSudoku[y2])
    elif GanzSudoku[y2].Reihe == 6:
        Reihe6.append(GanzSudoku[y2])
    elif GanzSudoku[y2].Reihe == 7:
        Reihe7.append(GanzSudoku[y2])
    else:
        Reihe8.append(GanzSudoku[y2])
for y3 in range(0, 81):
    if GanzSudoku[y3].Spalte == 0:
        Spalte0.append(GanzSudoku[y3])
    elif GanzSudoku[y3].Spalte == 1:
        Spalte1.append(GanzSudoku[y3])
    elif GanzSudoku[y3].Spalte == 2:
        Spalte2.append(GanzSudoku[y3])
    elif GanzSudoku[y3].Spalte == 3:
        Spalte3.append(GanzSudoku[y3])
    elif GanzSudoku[y3].Spalte == 4:
        Spalte4.append(GanzSudoku[y3])
    elif GanzSudoku[y3].Spalte == 5:
        Spalte5.append(GanzSudoku[y3])
    elif GanzSudoku[y3].Spalte == 6:
        Spalte6.append(GanzSudoku[y3])
    elif GanzSudoku[y3].Spalte == 7:
        Spalte7.append(GanzSudoku[y3])
    else:
        Spalte8.append(GanzSudoku[y3])

printStatusinfo(1)
printCurrentSudoku()
printStatusinfo(2)

printStatusinfo(4)
printCurrentSudoku()
