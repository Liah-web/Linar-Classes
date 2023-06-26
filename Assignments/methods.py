
#Method is a function that belong to a object

#Below are 5 methods for list

#1. Python list append(): Add a single element to the end of the list
Food= ["Yam", "Spaghetti", "Beans", "Indomie"]
#append "Potatoes" to the list
Food.append("Potatoes")
print("Tola's favorites are", Food)

#2. Python list count(): Returns  counts of the element in list
Ages_of_students_in_year_3=[17,16,18,18,19,19,13,15,17,17,19,18,18,18]

#chech how many of the students are 18 years of age
Age18=Ages_of_students_in_year_3.count(18)
print(Age18)

#3. Python List insert(): Insert an element to the list
#Even numbers from 1-20 
EvenNumbers=[2,4,6,8,9,10,14,16,18,20]
EvenNumbers.insert(6, 12)
print("The even numbers from 1-20 are", EvenNumbers)

#4. Python List sort(): sorts elements of a list in ascending order
#Arranging the scores of the students from lowest to the highest
scoreOfstudents=[40, 14,60,78,45,34,22,56,87,35,67,12,90]
scoreOfstudents.sort()
print(scoreOfstudents)

#5. Python list reverse(): reverse the elements of the list
studentscore=[40, 14,60,78,45,34,22,56,87,35,67,12,90]
studentscore.reverse()
print(studentscore)



#Tuples Method
#1. count(): Returns the number of times a specified value occurs in a tuple
StudentMark=(60,56,60,48,36,13,60,60)
Numbersofstudentsthatscored60=StudentMark.count(60)
print("The number of students that scored 60 are:", Numbersofstudentsthatscored60)

#2. index(): Searches the tuple for a specified value and returns the position of where it was found
thistuple=("yam", "pap", "rice")
x=thistuple.index("pap")
print(x)

