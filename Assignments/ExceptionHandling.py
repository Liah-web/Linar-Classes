try:
    numerator=70
    denominator=0

    result=numerator/denominator
    print(result)

except:
    print("Error:cannot be divided by 0")


try:
        fav="My favorite colour is Blue. I love Blue because it is the sky. I love blue because it is a cool colour."
        find=fav.index("Nigeria")
        print(find)
except:
     print("Error:Not found")


try:
     Poem="Twinkle Twinkle little star, oh I wonder what you are, like a  in the sky"
     Boem=Poem.__reversed__("diamond")
     print(Boem)
except:
     print("Error:it is an exception")