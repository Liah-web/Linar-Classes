Length=int(input("Enter value for length, l = "))
Width=int(input("Enter value for width, w = "))

#Calculate the area of the room in square feet
AreaOfTheRoomInSquareFeet = Length*Width
 
 #Convert the room in squarefeet to inches since the abestos was giving in inches
 #one foot is 12 inches
Onefoot=12
OneSquarefoot= Onefoot**2 #inches

AreaOfTheRoomInSquareInches= AreaOfTheRoomInSquareFeet*OneSquarefoot
AreaOfOneAbestosSheet=8 * 8 #8 inches by 8 inches
NumberOfAbestosNeeded=AreaOfTheRoomInSquareInches/AreaOfOneAbestosSheet  #Numbers of Abestos needed

print(NumberOfAbestosNeeded)


