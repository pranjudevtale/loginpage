import simplejson
def password():
    with open("Emp.json","r") as d:
        e=simplejson.load(d)
        f=dict(e)
    for x,y in f.items():
        m=list(y.items())
        l=len(m)-5
        for x in range(l):
            if x==1:
               b=list(m[x])
               for x in range(len(b)):
                   if x==1:
                       c=b[x]
                       return c
print(" 1. Singup \n 2. Login \n 3. Forget Password")
a=int(input(" Are you new user :- Enter 1 :-\n Already you have account :- Enter 2 :- \n Forget password :- Enter 3 :- "))
print()
if a==1:
    for x in range(3):
        flag=0
        print("your username you use gmail.com format")
        b=input("Enter your good username :-")
        if b.islower() and "1" in b or "2" in b or "3" in b or "4" in b or "5" in b or "6" in b or "7" in b or "8" in b or "9" in b or "0" in b :
            if "@" in b and "." in b:
                print("Successfuly username")
                break
            else:
                print("Invalid username")
                flag=1
        else:
            print("Invalid username")
            flag=1
            
    if flag==0:
        for x in range(2):
            flag=0
            print("You use strong password format")
            c=input("Enter your best password :- ")
            if len(c)>=8 and len(c)<=16:
                if c.capitalize():
                    if "@" in c:
                        print("Successfuly password")
                        break
                    else:
                        print("Invalid  password")
                        flag=1
                else:
                    print("Invalid")
                    flag=1
            else:
                print("Check your password length")
        if flag==0:
            print("Bio DATA")
            fname=input("Enter your first name:- ")
            lname=input("Enter your last name :- ")
            DOB=input("Enter your D.O.B :- ")
            age=input("Enter your age :- ")
            blood=input("Enter your Blood group :-")
            record=[b,c,fname,lname,DOB,age,blood]
            e=["User","Pass","First name","Last name ","D.O.B","Age","Blood Group"]
            old={}
            g="Candidate"
            for x in range(1):
                new={}
                for y in range(len(e)):
                    new[e[y]]=record[y]
                old[g]=new
            with open("./Emp.json","a") as a:
                simplejson.dump(old,a,indent=7)
            print("Your data successufly submited")
elif a==2:
    print("Check your Bio Data or not?")
    with open("Emp.json","r") as d:
        e=simplejson.load(d)
    for x in range(4):
        if x==3:
            print("You have Sign-up first before Log-in")
            break 
        user=input("Enter your Username :- ")
        for x in e:
            b=e[x]
            print(b)
            flag=0
            for y in b:
                if b[y]==user:
                    print("Success")
                    flag+=1
                    break
                else:
                    print("Your username does not exist please try again ")
                    break
        if flag==1:
            break     
else:
    print("Forget your Password")
    user=input("Enter your Username :- ")
    with open("Emp.json","r") as d:
        e=simplejson.load(d)
    for x in e:
        b=e[x]
        for y in b:
            if b[y]==user:
                print("Thist is your password :-", password(), "and Username is :-",b[y])
                print("""                         Success                           """)
        else:
            print("Your username is worng")