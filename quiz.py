print('''
     ----------WELCOME TO SUMAN'S QUIZ HOUSE!!!!!!-----------------
    ''')

playing=input(''' 
    ---------DO U WANNA PLAY OR NOT -------------------------------
    ''')
score=0   #for score varaible
if  playing.lower()!= "yes": #this is lower() for making all the input in lowercase
    print("GOODBIE :)")
    quit()
print('''   
    OK LETS START THE GAME ARE YOU READY!!!!  
    : )
    ''')
answer=input('''
    Q.1 Who is the father of computer?
     a.Charls babbages  b.shyam    c.Hari   d.krishana
    ''')
if answer.lower() == 'a':
    print("Correct")
    score+=1
else:
    print("Incorrect answer Correct is 'a'")


answer=input('''
    Q.2 When was the first computer was brought in nepal?
     a.1999   b.2020    c.2028   d.2038
    ''')
if answer.lower() == 'c':
    print("Correct")
    score+=1
else:
    print("Incorrect answer Correct is 'c'")


answer=input('''
    Q.3 What is fullform of RAM?
     a.Roy and mouice   b.Random access memory    c.Run and mouk   d.Ram and Madan
    ''')
if answer.lower() == 'b':
    print("Correct")
    score+=1
else:
    print("Incorrect answer Correct is 'c'")


answer=input('''
    Q.4 What is shortcut key to undo?
     a.ctrl+q   b.ctrl+r    c.ctrl+d   d.ctrl+Z
    ''')
if answer.lower() == 'd':
    print("Correct")
    score+=1
else:
    print("Incorrect answer Correct is 'c'")

answer=input('''
    Q.5 What is liveware?
     a.robots   b.Humanbeing    c.Physical devices   d.softwares
    ''')
if answer.lower() == 'b':
    print("Correct")
    score+=1
else:
    print("Incorrect answer Correct is 'b'")

print("You answer "+str(score)+ " question ")
print("You answer "+str((score/5)*100)+"%.")

print('''____THANSK FOR PLAYING _______
     __________GODBIE________
               : )
        ''')