'''THE CONTINUE KEYWORD STOPS THE CURRENT ITERATION AND RETURN CONTROL OF THE ITERATION TO THE BEGINNING OF THE 
OR WHILE LOOP'''
for i in range(15):
    if i ==6:
        continue
    print(i)

    food=["Yam", "Rice", "Spaghetti", "Noodles", "beans","Moimoi", "pap"]
for b in food:
   if b=="beans":
       continue
   print(b)
