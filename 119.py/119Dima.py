import turtle as trtl

builder = trtl.Turtle()

ShirtOptions = ["Shirt One", "Shirt Two", "Shirt Three"]
def ShirtOne():
    builder.fillcolor("Red")
    builder.begin_fill()

    builder.penup()
    builder.goto(-75, 0)
    builder.pendown()

    builder.left(90)
    builder.forward(150)
    builder.left(125)
    builder.forward(60)
    builder.right(125)
    builder.forward(60)
    builder.right(60)
    builder.forward(60)
    builder.right(30)
    builder.forward(150)
    builder.right(30)
    builder.forward(60)
    builder.right(60)
    builder.forward(60)
    builder.right(125)
    builder.forward(60)
    builder.left(125)
    builder.forward(150)
    builder.right(90)
    builder.goto(-75, 0)

    builder.end_fill()

def ShirtTwo():
    builder.fillcolor("Blue")
    builder.begin_fill()

    builder.penup()
    builder.goto(-75, 0)
    builder.pendown()

    builder.left(90)
    builder.forward(150)
    builder.left(125)
    builder.forward(60)
    builder.right(125)
    builder.forward(60)
    builder.right(60)
    builder.forward(60)
    builder.right(30)
    builder.forward(150)
    builder.right(30)
    builder.forward(60)
    builder.right(60)
    builder.forward(60)
    builder.right(125)
    builder.forward(60)
    builder.left(125)
    builder.forward(150)
    builder.right(90)
    builder.goto(-75, 0)

    builder.end_fill()

def ShirtThree():
    builder.fillcolor("Yellow")
    builder.begin_fill()

    builder.penup()
    builder.goto(-75, 0)
    builder.pendown()

    builder.left(90)
    builder.forward(150)
    builder.left(125)
    builder.forward(60)
    builder.right(125)
    builder.forward(60)
    builder.right(60)
    builder.forward(60)
    builder.right(30)
    builder.forward(150)
    builder.right(30)
    builder.forward(60)
    builder.right(60)
    builder.forward(60)
    builder.right(125)
    builder.forward(60)
    builder.left(125)
    builder.forward(150)
    builder.right(90)
    builder.goto(-75, 0)

    builder.end_fill()
ShirtFunctions = [ShirtOne, ShirtTwo, ShirtThree]

SweaterOptions = ["Sweater One", "Sweater Two", "Sweater Three"]
def SweaterOne():
    builder.fillcolor("Red")
    builder.begin_fill()

    builder.penup()
    builder.goto(-75, 0)
    builder.pendown()

    builder.goto(-75, 150)
    builder.goto(-150, 50)
    builder.goto(-175, 0)
    builder.goto(-210, 0)
    builder.goto(-165, 110)
    builder.goto(-115, 180)
    builder.goto(-75, 220)
    builder.goto(50, 220)
    builder.goto(75, 220)
    builder.goto(115, 180)
    builder.goto(165, 110)
    builder.goto(210, 0)
    builder.goto(175, 0)
    builder.goto(150, 50)
    builder.goto(75, 150)
    builder.goto(75, 0)
    builder.goto(-75, 0)
    builder.end_fill()

def SweaterTwo():
    builder.fillcolor("Blue")
    builder.begin_fill()

    builder.penup()
    builder.goto(-75, 0)
    builder.pendown()

    builder.goto(-75, 150)
    builder.goto(-150, 50)
    builder.goto(-175, 0)
    builder.goto(-210, 0)
    builder.goto(-165, 110)
    builder.goto(-115, 180)
    builder.goto(-75, 220)
    builder.goto(50, 220)
    builder.goto(75, 220)
    builder.goto(115, 180)
    builder.goto(165, 110)
    builder.goto(210, 0)
    builder.goto(175, 0)
    builder.goto(150, 50)
    builder.goto(75, 150)
    builder.goto(75, 0)
    builder.goto(-75, 0)
    builder.end_fill()

def SweaterThree():
    builder.fillcolor("Yellow")
    builder.begin_fill()

    builder.penup()
    builder.goto(-75, 0)
    builder.pendown()

    builder.goto(-75, 150)
    builder.goto(-150, 50)
    builder.goto(-175, 0)
    builder.goto(-210, 0)
    builder.goto(-165, 110)
    builder.goto(-115, 180)
    builder.goto(-75, 220)
    builder.goto(50, 220)
    builder.goto(75, 220)
    builder.goto(115, 180)
    builder.goto(165, 110)
    builder.goto(210, 0)
    builder.goto(175, 0)
    builder.goto(150, 50)
    builder.goto(75, 150)
    builder.goto(75, 0)
    builder.goto(-75, 0)
    builder.end_fill()
SweaterFunctions = [SweaterOne, SweaterTwo, SweaterThree]

ShortsOptions = ["Short One", "Short Two", "Short Three"]
def ShortOne():
    builder.penup()
    builder.goto(-75, 0)
    builder.pendown()
    builder.fillcolor("Red")
    builder.begin_fill()

    builder.left(260)
    builder.forward(120)
    builder.left(100)
    builder.forward(80)
    builder.left(85)
    builder.forward(89)
    builder.right(170)
    builder.forward(89)
    builder.left(85)
    builder.forward(90)
    builder.goto(75, 0)
    builder.goto(-75, 0)
    builder.end_fill()

def ShortTwo():
    builder.penup()
    builder.goto(-75, 0)
    builder.pendown()
    builder.fillcolor("Blue")
    builder.begin_fill()

    builder.left(260)
    builder.forward(120)
    builder.left(100)
    builder.forward(80)
    builder.left(85)
    builder.forward(89)
    builder.right(170)
    builder.forward(89)
    builder.left(85)
    builder.forward(90)
    builder.goto(75, 0)
    builder.goto(-75, 0)
    builder.end_fill()

def ShortThree():
    builder.penup()
    builder.goto(-75, 0)
    builder.pendown()
    builder.fillcolor("Yellow")
    builder.begin_fill()

    builder.left(260)
    builder.forward(120)
    builder.left(100)
    builder.forward(80)
    builder.left(85)
    builder.forward(89)
    builder.right(170)
    builder.forward(89)
    builder.left(85)
    builder.forward(90)
    builder.goto(75, 0)
    builder.goto(-75, 0)
    builder.end_fill()

ShortFunctions = [ShortOne, ShortTwo, ShortThree]

PantsOptions = ["Pants One", "Pants Two", "Pants Three"]
def PantsOne():
    builder.forward(70)
def PantsTwo():
    builder.forward(80)
def PantsThree():
    builder.forward(30)
PantsFunctions = [PantsOne, PantsTwo, PantsThree]

def shoes():
    builder.forward(20)

def Question1():
    Qustion1 = input("Shirt or Sweater? ")
    if Qustion1 == "Sweater":
        print("Your choices are:", SweaterOptions)
        UserInputOne = input("Pick a Sweater: ")

        if UserInputOne == "Sweater One":
            SweaterOne()
        elif UserInputOne == "Sweater Two":
            SweaterTwo()
        elif UserInputOne == "Sweater Three":
            SweaterThree()

    if Qustion1 == "Shirt":
        print("Your choices are:", ShirtOptions)
        UserInputOne = input("Pick a shirt: ")

        if UserInputOne == "Shirt One":
            ShirtOne()
        elif UserInputOne == "Shirt Two":
            ShirtTwo()
        elif UserInputOne == "Shirt Three":
            ShirtThree()

def Question2():
    Question2 = input("Shorts or Pants? ")
    if Question2 == "Shorts":
        print("Your choices are", ShortsOptions)
        UserInputTwo = input("Pick Shorts: ")

        if UserInputTwo == "Short One":
            ShortOne()
        elif UserInputTwo == "Short Two":
            ShortTwo()
        elif UserInputTwo == "Short Three":
            ShortThree()

    if Question2 == "Pants":
            print("Your choices are", PantsOptions)
            UserInputTwo = input("Pick Pants: ")
    
            if UserInputTwo == "Pants One":
                PantsOne()
            elif UserInputTwo == "Pants Two":
                PantsTwo()
            elif UserInputTwo == "Pants Three":
                PantsThree()

def Question3():
    Question3 = input("Shoes or no shoes? ")
    if Question3 == "Shoes":
        shoes()
    elif Question3 == "No":
        print("Here is your outfit")


Question1()
Question2()
Question3()

wn = trtl.Screen()
wn.mainloop()