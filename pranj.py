# import json
# print("wel come login  and signup page")
# usr=input("what u want to do login or sign up :-")
# if usr=="signup":
#     usr_name=input("enter the usr_name:-")
#     password=input("enter usr password:-")
#     password1=input("comform password")
#     if password==password1:
#         description=input("enter the description:-")
#         dob=input("enter ur dob:-")
#         hobbies=input("enter ur hobbies:-")
#         gender=input("enter ur gender f/m:-")
#         usr_details={"description":description,"DOB":dob,"hobbies":hobbies,"gender":gender}
#         with open("p.json","w")as f:
#             data=json.dump(usr_details,f,indent=4)

#     else:
#         print("not strong password")
# else:
#     if usr=="login":
#         usr_name=input("enter the usr_name:-")
#         password=input("enter usr password:-")
#         password1=input("comform password")
#         with open("p.json","r")as file:
#             data=json.load(file)
#         if password==data["password1"]:



# element=[23,14,56,12,19,9,15,25,31,42,43]
# count=0
# count1=0
# sum=0
# sum1=0
# i=0
# while i<len(element):
#     if element[i]%2==0:
#         count=count+1
#         sum=sum+element[i]
#     else:
#         count1=count1+1
#         sum1=sum1+element[i]
#     i=i+1
# print("count even:-",count)
# print("sum even:-",sum)
# avg=sum/count
# print("avg even:-",avg)
# print("count1 odd:-",count1)
# print("sum odd:-",sum1)
# avg=sum1/count1
# print("avg odd:-",avg)

m = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
v=15
while i<len(m):
    col=0
    sum=0
    s=len(m[i])
    while col<s:
        sum=sum+m[i][col]
        col=+1
    print(sum,"column")
    a=sum+sum+sum
    i+=1
print(a)
j=0
while j<len(m):
    row=0
    sum1=0
    while row<len(m[i]):
        sum1=sum1+m[row][row]
        row+=1
    print(sum1,"row")
    h=sum1+sum1+sum1
    j+=1  
print(h)
x=m[0][0]+m[1][1]+m[2][2]
z=m[0][2]+m[1][1]+m[2][0]
if x==v:
    if z==v:
        c=x+z
        print("diagonal:",c)
        if sum==sum1==v:
            print("it is magic square")
        else:
            print("it is not magic square")
    else:
        print("it is not magic square")
else:
    print("it is not magic square")