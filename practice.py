import random
import time

'''a= "abcDefGtHKJHui"
s=""
for i in a:
    if(i.isupper()):
        print("Capital Latter",i)
        s+=i.lower()
    else:
        print("Small Letter",i)
        s+=i.upper()

print(a)
print(s)

a=10011456
c=0
while(a!=0):
    d=a%10
    c=c*10 + d
    a=int(a/10)

print(c)

num=153                                      #####Armstrong
number_length=len(str(num))
t=0
r=num

while(r!=0):
    q=r%10
    r=int(r/10)
    t=t+pow(q,number_length)

if(t==num):
    print("Its Armstrong")

else:
    print("Its not Armstrong")

a=0                                   ###Fibonacci series
b=1
print(a,",",b,end="")
for i in range(0,10):
    c=a+b
    print(",",c,end="")
    a=b
    b=c'''
'''
a="after a long weekend i met a girl"                  #########replacing a letter with other
c=""
for i in a:
    if(i=="a"):
        c=c+"T"

    else:
        c=c+i

print(c)'''
'''x=a.replace("a","X")
print(x)'''

'''
a="after a long weekend i met a girl"                  #########count a repeated letter in given string
c=0
letter = input("enter letter:-")
for i in a:
    if(i==letter):
        c+=1
    else:
        pass
print("Given string:-",a)
print(letter,"letter comes",c,"times in the given string!!!!")'''

'''lst=[1,2,3,4,6,7,8,8,10]
for i in range(1,11):
    if(i in lst):
        pass
    else:
        print("missing no.",i)'''
#############Inheritnce
'''
class Person:
    def __init__(self,name, age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name)
        print(self.age)

class Employee(Person):
    def __init__(self,name,age,id,salary):
        self.id=id
        self.salary=salary
        Person.__init__(self,name,age)

    def details(self):
        print("Person has salary",self.salary)
        print("Person has ID",self.id)

a= Employee("Ram",25,1200,500000)
a.display()
a.details()

########Polymorphism
class Bird:
    def intro(self):
        print("Birds are the species which can fly in the sky")

    def flight(self):
        print("Some of the birds are not supposed to fly")

class Sparrow(Bird):
    def flight(self):
        print("Sparrow can fly")

class Osritch(Bird):
    def flight(self):
        print("Ostritch cannot fly but run on ground")

brd=Bird()
spr=Sparrow()
ost=Osritch()
brd.intro()
brd.flight()

spr.intro()
spr.flight()

ost.intro()
ost.flight()'''

'''def fact(n):
    if n<1:
        return 1
    else:
        return n*fact(n-1)


x=fact(5)
print(x)'''
'''num1=5
num2=2
result=0
while num1>0:
    num1=num1-num2
    result+=1


print(result,num1)1234->4123->'''
'''k=8
l=4
num=1234
while k>0:
    a=int(num/10)
    b=num%10
    c=b*1000+a
    print(c)
    num=c
    k-=1'''
'''business_list=["SwipeWire","SecureSmarter","Dwellsmith","SalePush","Formonix","Branding","Cloudrevel","Seekingon","Medicing","Crowdstage","Hiphonic","QuickSpace","MetConnect","Rentoor","Kiddily"]
client_list=["Aakav Kumar","Aakesh Maurya","Aarav Chand","Advik Kaushik","Chaitanya Seth","Hredhaan Mishra","Hemang Kumar","Inesh Pandey","Ishaan Kapoor","Jairaj Singh","Jihan Khan","Lekh Gaumat","Lohit Pal","Ramesh Gupta","Rituraj Upadhyay"]
i = random.randrange(0,14)
business = business_list[i]+" Pvt. Ltd."
client = client_list[i]
print(business,client)
mob = random.randrange(9000000000,9999999999)
email = str(mob) + "trade@gmail.com"
print(email)'''


'''class Pass:
    def __init__(self, driver):
        self.driver = driver

    def Passwrd(self):
        self.driver.find_element_by_name("pass").send_keys(123456789)
        self.driver.find_element_by_name("login").click()
        time.sleep(2)'''

'''def combination(height, lst):
    d=[]
    for i in lst:
        b = height-i
        if(b in lst):
            c=[]
            for k in lst:
                if(b==k):
                    c.append(i)
                    c.append(k)
        else:
            pass

        d.append(c)

        count=0
        e=[]
        m = height-i
        while m>=0:
            e.append(i)
            if m==0:
                d.append(e)
            else:
                pass
            m=m-i

        if (lst[i]==0):
            pass
        else:
            add = 0
            f = []
            while (add!=height):
                add+=lst[i]
                if(add <= height):
                    f.append(lst[i])
                else:
                    add+=lst[i-1]
                    if (add <= height):
                        f.append(lst[i])
        d.append(f)

    print(d)

height = int(input("Enter the desired height"))
lst = [1,2,3,4]
combination(height,lst)'''


