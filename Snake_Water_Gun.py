import random
l=['s','w','g']
h=0
c=0
i=0
while(1):
    a=random.choice(l)
    b=input("Enter your choice(s for snake and w for water and g for gun): ")
    if a==b:
        print("Case #:",i+1,"Tie")
    elif a=='w':
        if b=='s':
            h=h+1
            print("Case #:",i+1,"You Won this game")
        else:
            c=c+1
            print("Case #:",i+1,"You loss this game")
    elif a=='s':
        if b=='w':
            h=h+1
            print("Case #:",i+1,"You Won this game")
        else:
            c=c+1
            print("Case #:",i+1,"You loss this game")
    else:
        if b=='w':
            h=h+1
            print("Case #:",i+1,"You Won this game")
        else:
            c=c+1
            print("Case #:",i+1,"You loss this game")
    i=i+1
    if i>9:
        break
if h>c:
    print("Congratulation You Won the game")
    print("You Won the game",h,"times and computer won game",c,"times")
else:
    print("Better luck next time You losses the game")
    print("Computer Won the game",c,"times and You won game",h,"times")
