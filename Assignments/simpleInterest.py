#Create a script that calculates the simple interest on a loan or investment. Prompt the user to enter the principal, amount, interest, rate`1qs,` and time period(in years).\
#Use the formular: p*r*t/100

p=float(input("Enter the amount for principal:\n"))
r=float(input("Enter the rate given:\n"))
t=int(input("Enter the value for time:\n"))
SimpleInterest=((p*r)*float(t)/100.0)

print('If the principal is, '+str(p)+' the rate is, ' +str(r) +' and the time is, '+str(t)+' , then the simple interest  is ' + str(SimpleInterest) + ' on the loan or investment.')