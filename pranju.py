import json
import re
import os
file=os.path.exists("user.json")
print(file)
if file==False:
    dict2={}
    list1=[]
    dict1={}
    print("wel come login  and signup page")
    usr=input("what u want to do login or sign up :-")
    if usr=="signup":
        usr_name=input("enter the usr_name:-")
        password=input("enter usr password:-")
        if re.search("[A-Z]",password) and re.search("[a-z]",password) and re.search("[0-9]",password) and re.search("[@,#,$]",password):
            password1=input("comform your password:-")
            with open("p.json","w")as file:
                data=json.dump(file)

            if password==password1:
                print("congress",usr_name)
                description=input("enter the description:-")
                dob=input("enter ur dob:-")
                hobbies=input("enter ur hobbies:-")
                gender=input("enter ur gender f/m:-")
                l1=["name","password","description","DOB","hobbie","gender"]
                l2=[usr_name,password,description,dob,hobbies,gender]
                for i in range(0,len(l1)):
                    dict2.update({l1[i]:l2[i]})
                list1.append(dict2)
                dict1.update({password:list1})
                with open ("json","w") as injson:
                    json.dump(dict1,injson,indent=4)
            else:
                print("password didnt match.")
        else:
            print("weak password")
if file==True:
    list1=[]
    usr=input("what u want to do login or sign up :-")
    if usr=="signup":
        usr_name=input("enter the usr_name:-")
        password=input("enter usr password:-")
        with open("usr.json","r")as n:
            data=json.load(n)
        for i in data:
            if i==password:
                print("this account is already exists:-")
                print(data[i])
                break
            if re.search("[A-Z]",password) and re.search("[a-z]",password) and re.search("[0-9]",password) and re.search("[@,#,$]",password):
                password=input("comform your password:-")
                if password==password1:
                    print("congress",usr_name)
                    description=input("enter the description:-")
                    dob=input("enter ur dob:-")
                    hobbies=input("enter ur hobbies:-")
                    gender=input("enter ur gender f/m:-")
                    print("congress",usr_name,"u have successfully signup")
                    l1=["name","password","description","DOB","hobbie","gender"]
                    l2=[usr_name,password,description,dob,hobbies,gender]
                    dict2={}
                    for i in range(0,len(l1)):
                        dict2.update({l1[i]:l2[i]})
                    list1.append(dict2)
                    dict1.update({password:list1})
                    with open ("user.json","w") as injson:
                        json.dump(data,injson,indent=2)
                else:
                    print("password didnt match:-")
            else:
                print("strong password")
        else:
            print("weak password")
    elif usr=="login":
        name=input("enter the user")
        password=input("enter the password")
        with open("uder.json","r")as file:
            data=json.load(file)
        for i in data:
            if i==password1:
                print("this account is already exists")
                print(data[i])
                break
            else:
                print("ur password is not exists")
    else:
        print("is not login")
else:
    print("it is not sign up")



