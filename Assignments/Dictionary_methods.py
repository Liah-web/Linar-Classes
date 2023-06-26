#1. keys()
Food={
"carbohydrates":"Rice, Yam, Wheat",
"Proteins" : "Beans,Fish,Eggs",
"water":"water",
}
MyKeys=Food.keys()
print(MyKeys)

#2. Pop()
Animals={
"pets":"Dogs,Cats",
"security":"Dogs",
"beef":"cow,sheep,ram",
"dairy":"Cow,Goat",
}
MyAnimals=Animals.pop("dairy")
print(MyAnimals)

#3. clear()
StudentInfo={
"FirstName":"Mira",
"Surname": "Ayoade",
"Age":"20",
"Course":"Geophysics",
"Degree":"Bsc"
}
Submit=StudentInfo.clear()
print(Submit)

#4. copy()
studentscore={"Jambscore":"270"}
duplicate=studentscore.copy()
print(duplicate)

#5. fromkeys()
firstname=("Ayo","Ade")
surname="Mamood"
fam=dict.fromkeys(firstname,surname)
print(fam)

#6. items()
studentinformation={
"studentname": "Ayo",
"surname":"Mide",
"school":"Lasu",
"faculty":"Education",

}
rint=studentinformation.items()
print(rint)

#7. get()
selectedAnimals={
"pet":"dogs",
"sport":"horse",
"beef":"cow",
}
find=selectedAnimals.get("beef")
print(find)

#8. popitem()
lookalike={
"Dragon":"Dinosaurs",
"Tiger":":Leopard",
"Crocodile": "Alligator",
}
lookalike.popitem()
print(lookalike)

#9. values()
studentresults={
    "mide":"45",
    "Rasaq": "95",
    "Mimi":"80",
    "Ada":"80",
    "Donald":"60"
    }
studentresults.values()
print(studentresults)

#10. updates()
newrelease={
"mide":"45",
    "Rasaq": "95",
    "Mimi":"80",
    "Ada":"80",
    "Donald":"60",
}
newrelease.update({"Lawrence": "89"})
print(newrelease)