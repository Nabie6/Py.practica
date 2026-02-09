test=float(input("your score in test: "))
hw=0
visit=0
if test>=90 and test<=100 :
    hw=str(input("did you do hw?:  "))
    if hw =="yes":
        print("Great! Grade: A+")
    elif hw =="no":
        print("Good job. But do your hw! Grade: A")
    else :
        print( "yes/no")
elif test>=80 and test<=89:
    visit=str(input("Ты посещал занятия больше 75%?: "))
    if visit=="yes":
        print("Good! Grade: B")
    elif visit=="no":
        print("You need to visit school better! Grade: C")
else:
    print ("Try harder!")
