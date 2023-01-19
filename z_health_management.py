from importlib.metadata import files
import datetime
from tabnanny import check
def getdate():
    return datetime.datetime.now()

def food():
    num=int(input("enter 1.adi 2.raj 3.shre. "))
    if num==1:
        food=input("Enter the food you ate ")
        f=open("adifood.txt","a")
        date=str(getdate())
        f.write(date+": ")
        f.write(food+"\n")
        f.close()
    elif num==2:
        food=input("enter the food you ate \n ")
        f=open("rajfood.txt","a")
        date=str(getdate())
        f.write(date+" "+food+"\n")
        f.close()
    elif num==3:
        food=input("enter the food you ate ")
        f=open("shrefood.txt","a")
        date=str(getdate())
        f.write(date+" : "+food+"\n")
        f.close()
        
def exercise():
    num=int(input("Enter 1.adi 2.raj 3.shre please : "))
    exer=input("enter the exercise you did today : ")
    date=str(getdate())
    if num==1:
        f=open("adiexer.txt","a")
        f.write(date+" : "+exer+"\n")
        f.close()
    elif num==2:
        f=open("rajexer.txt","a")
        f.write(date+" : "+exer+"\n")
        f.close()
    elif num==3:
        f=open("shreexer.txt","a")
        f.write(date+" : "+exer+"\n")
        f.close()
        
def Display():
    num=int(input("enter the 1.adi 2.raj 3.shre to display your record.."))
    if(num==1):
        check=int(input("enter which record you wanna see food or exercise..1.exercise 2.food "))
        if check==1:
            f=open("adiexer.txt")
            print(f.read())
            f.close()
        elif check==2:
            f=open("adifood.txt")
            print(f.read())
            f.close()
    elif num==2:
        check=int(input("enter which record you wanna see food or exercise..1.exercise 2.food "))
        if check==1:
            f=open("rajexer.txt")
            print(f.read())
            f.close()
        elif check==2:
            f=open("rajfood.txt")
            print(f.read())
            f.close()
    else:
        check=int(input("enter which record you wanna see food or exercise..1.exercise 2.food "))
        if check==1:
            f=open("shreexer.txt")
            print(f.read())
            f.close()
        elif check==2:
            f=open("shrefood.txt")
            print(f.read())
            f.close()
num=int(input("enter 1.display record 2.entry.."))
if(num==1):
    Display()
elif num==2:
    check=int(input("enter 1. to entry for food 2.entry for exercise.."))
    if(check==1):
        food()
    elif check==2:
        exercise()
print("Have a Good day.. ")
        
    
    
        
