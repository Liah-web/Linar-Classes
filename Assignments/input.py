
#At age ......, you are to save from your salary 80% equal to ......., and 20% equal to ......., from your miscellaneous. From the miscellaneous, you can only dash out ..... at once.
#The solution
age=str(input("Enter your age? \n"))
salary = float(input("Enter your salary? \n"))
expenses=float(input("Enter your expenses? \n"))
calculatebalance= salary - expenses
savings80=(0.8* calculatebalance)
mis20=(0.2*calculatebalance)
dashout=((float(age)*mis20)/1000.0)

print('At age '+str(age)+' you are to save from your balance (80%) equivalent to ' +str(savings80)+' and (20%) equivalent to '+str(mis20)+' for miscellaneous')
print('From the miscellaneous, you can only dashout '+str(dashout)+' at once')