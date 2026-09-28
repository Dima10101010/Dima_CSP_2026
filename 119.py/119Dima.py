import turtle as trtl

builder = trtl.Turtle()


ShirtOptions = ["Shirt One", "Shirt Two", "Shirt Three"]

def ShirtOne():
    builder.forward(50)
def ShirtTwo():
    builder.forward(100)
def ShirtThree():
    builder.forward(200)

ShirtFunctions = [ShirtOne, ShirtTwo, ShirtThree]

Qustion1 = input("Shirt or Sweater")

if Qustion1 == "Shirt":
    print("Your choices are:", ShirtOptions)
    UserInputOne = input("Pick a shirt")


SweaterOptions = ()
ShortsOptions = ()
PantsOptions = ()

wn = trtl.Screen()
wn.mainloop()