from  matplotlib import pyplot as plt

data=[23,45,56,78,213]
plt.bar([1,2,3,4,5],data)
plt.show()
'''
data={
"Adults":40,
"Youths":45,
"Teens":10,
"children":5
}
 y
Thepeople=list(data.keys())
NumberOfPeoplePresent=list(data.values())

fig=plt.figures(figsize=(10,5))

plt.bar(Thepeople,NumberOfPeoplePresent, color="maroon", width=0.4)
plt.xlabel("The age groups present")
plt.ylabel("The percentage of each")
plt.title("Attendance in a church")
plt.show()



print(data)
print(Thepeople)
print(NumberOfPeoplePresent) '''