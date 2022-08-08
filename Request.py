import json
import requests
url=requests.get("https://api.merakilearn.org/courses")
re=url.json()
with open("courses.json","w") as file:
    json.dump(re,file,indent=7)
    

r=open("courses.json","r")
read=r.read()
data=json.loads(read)

print()
print("WELCOME TO NAVGURUKUL AND LEARN BASIC PROGRAMING LANGUAGE")
print()

k=1
for i in data:
    print(k,i["name"],i["id"])
    k+=1

option=int(input("enter programe number:-"))
print()

print(data[option-1]["name"],data[option-1]["id"])
print()

a=data[option-1]["name"]+".json"
s=requests.get("https://api.merakilearn.org/courses/"+data[option-1]["id"]+"/exercises")
ex=s.json()
with open(a,"w") as f:
    json.dump(ex,f,indent=4)

ret=open(a,"r")
read=ret.read()
deta=json.loads(read)
main_list=[]
b=1
b1=1
for i in deta["course"]["exercises"]:
    print(b,i["name"])
    print("   ",i["slug"])
    b+=1
    main_list.append(i)

with open("main_file.json","w") as write:
    json.dump(main_list,write,indent=4)

topic=int(input("enter topic number:-")) 
topic=topic-1
i=0
while i<len(deta["course"]["exercises"][topic]["content"]):
    print(deta["course"]["exercises"][topic]["content"][i]["value"])
    print()
    i+=1
while topic<= len(deta["course"]["exercises"]):
    l=input("previous or next (p&n)")
    if l=="p" and l!="n":
        topic-=1
        if l=="p" and topic>=1:
            print(deta["course"]["exercises"][topic]["name"],"\n")
            i=0
            while i<len(deta["course"]["exercises"][topic]["content"]):
                print(deta["course"]["exercises"][topic]["content"][i]["value"])
                i+=1
        else:
            i=0
            while i<len(deta) :
                print(str(i+1),deta["course"]["exercises"][i]["name"]) 
                i+=1
    elif l=="n" and l!="p":
        topic+=1
        if l=="n" and topic<len(deta["course"]["exercises"]):
            print(deta["course"]["exercises"][topic]["name"],"\n")
            i=0
            while i<len(deta["course"]["exercises"][topic]["content"]):
                print(deta["course"]["exercises"][topic]["content"][i]["value"])
                i+=1
        if topic+1== len(deta["course"]["exercises"]):
            print("topic is completed") 
            break
    else:
        print("wrong user_input")
        break


