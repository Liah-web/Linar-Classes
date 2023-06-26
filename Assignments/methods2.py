#center() method center align a string, using a specified character(space is default) as ffill character
food="Spaghetti"
yummy=food.center(30)
print(yummy)

#count() method: Returns the number of times an object appeared in a list or string
Colour="My favorite colour is Blue. I love Blue because it is the sky. I love blue because it is a cool colour. There isn't Blue in Nigeria's flag"
blueappeared=Colour.count('Blue')
print(blueappeared)

#expandtabs(): sets the tab-size to the specifed number of whitespaces
Composition="My\tname\tis\tAaliyah.\tI'm\ta\tstudent\tof\tUnilag. "
expand=Composition.expandtabs(15)
print(expand)

#find() method finds the first occurrence of the specified object
Quickfindforcolour="My favorite colour is Blue. I love Blue because it is the sky. I love blue because it is a cool colour. There isn't Blue in Nigeria's flag"
seen=Quickfindforcolour.find("colour")
print(seen)