import requests
import  time, random
from utilities import XLUtils
import os
'''class person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def details(self):
        print(self.name, self.age)

class employee(person):
    def __init__(self,name, age,id ,salary):
        self.id = id
        self.salary = salary
        person.__init__(self,name, age)

    def empdata(self):
        print("The person has id",self.id)
        print("The person has salary",self.salary)

a=employee("Ram",23,1234,50000)
a.details()
a.empdata()'''

'''class identity:
    def __init__(self,driver):
        self.driver =driver

    def ID(self):
        self.driver.find_element_by_name("email").send_keys("HelloKartikey")
        assert True'''

'''rupee = 10
count=rupee
replace=0
while count>=3:
    count-=3
    replace+=1
count=replace+count
altr=0
while (replace>=3):
    replace-=3
    altr+=1
altr=altr+replace
print(rupee+count+replace)
start = time.time()
n=10000
for j in range(1,n+1):

    i = 1
    while(i*i<=j):
        if(i*i==j):
            print("Number:", j, "Root:", i)
        else:
            pass
        i+=1

end = time.time()
print(end-start)

n=4
m=4
a=n-1
while(a>=n/2):
    d= (a/m)*10
    #print(d)
    s=d%10
    #print(s)
    if(s==0):
        print("Number closest to",n,"divisible by 4 is:-",a)
        break
    else:
        pass
    a-=1'''

'''lst = [2,4,7,1,3,9,9,7]
a=list(set(lst))
print(a)
a.pop()
c=a.pop()
print(c)'''

'''def power(a,b):
    c=1
    if(a>1):
        while (c<=b):
            c=c*a
            if(c==b):
                return ("Yes ",b,"is in powers of ",a)
            else:
                pass
        if(c>b):
            return ("No ",b," is not in powers of ",a)
    else:
        return ("Please enter a number greater then 1")

d=power(4,16)
print(d)'''

'''def waveArray(l):                       ####wave arrey
    if(len(l)%2==0):
        arrange(l)
        return l
    else:
        b=lst.pop()
        arrange(l)
        l.append(b)
        return l

def arrange(l):
    i = 0
    while i < len(l):
        l[i], l[i + 1] = l[i + 1], l[i]
        i += 2

lst=[1,2,3,4,5,7,10]
a = waveArray(lst)
print(a)'''


'''stri = "geeksforgeeks"                  ###########duplicacy removal from string
a = {}
c=0
for i in stri:
    if(i in a):
        a[i] += 1
    else:
        a[i] = 1
d = max(a.values())
#d = max(a, key=a.get)

for j,k in a.items():
    if k==d:
        print("The most repeated character is-",j,", order of repetition is",d)'''

'''k = int(input("Enter character number to be removed"))
st = "abcdef"
st1 = list(st)
l=len(st1)
s = ""

if (k>=0 and k<len(st1)):
    st1.remove(st1[k])
else:
    print("Please enter number within range of word length")
for i in st1:
    s+=i
print(s)'''

'''s = "geeks for geeks"
j=""
a=[]
for i in s:
    if i!=" ":
        j+=i
    else:
        a.append(j)
        j=""
a.append(j)
print(a)'''

'''def string_to_list(string):
    j = ""
    a = []
    for i in string:
        if i != " ":
            j += i
        else:
            a.append(j)
            j = ""
    a.append(j)
    return a

a="geeks for geeks"
b="geeks for geeks is good"
x=string_to_list(a)
y=string_to_list(b)
k=0
if (len(x)<len(y)):
    for i in x:
        if(x[k]==y[])'''

'''a=[1,2,3,4,5]
print(a)
c=1
s=[]
for i in a:
    c=c*i
for i in a:
    d=int(c/i)
    s.append(d)
print(s)'''

'''s="dog"
vowels="aeiou"
if("a" in s):
    if("e" in s):
        if ("i" in s):
            if ("o" in s):
                if ("u" in s):
                    print("All vowels are present in the string")
                else:
                    print("All vowels are not present")
            else:
                print("All vowels are not present")
        else:
            print("All vowels are not present")
    else:
        print("All vowels are not present")
else:
    print("All vowels are not present")'''

'''def game(choice, players_no):
    c = {}
    if choice == "y":
        dict = {1: "STONE", 2: "PAPER", 3: "SCISSOR"}
        choice_dict = {}
        lst = []
        i = 0
        while players_no != 0:
            r = "Player" + str(i + 1)
            v = r + " Make Your Choice as 1 or 2 or 3 for STONE, PAPER, SCISSOR respectively:-"
            n = int(input(v))
            lst.append(r)
            choice_dict[lst[i]] = dict[n]
            players_no -= 1
            i += 1
        #print(choice_dict)
    else:
        print("The game ends, Thank You!!!!!")

    for k in choice_dict:
        if choice_dict[k] in c:
            c[choice_dict[k]] += 1
        else:
            c[choice_dict[k]] = 1

    if (len(c) == 3):
        print("Ooops!!! Its a draw, all three gestures are present...try again")

    return c,choice_dict

choice = input("Want to start the game?? Press y or n--")
players_no = int(input("Enter the numbers of players"))
z,choice_dict = game(choice,players_no)
print(z)
while len(choice_dict)!=1:
    a=[]
    b=[]
    t=0
    if (len(z)==2):
        for l in z:
            a.append(z[l])
            b.append(l)
        if (a[t]>a[t+1]):
            #print(b[t],"group is the winner")
            for i in choice_dict.copy():
                if(choice_dict[i]==b[t]):
                    print(i,"is the winner, chose",b[t])
                else:
                    choice_dict.pop(i)
            z,choice_dict = game("y",len(choice_dict))


        elif(a[t]<a[t+1]):
            #print(b[t+1],"group is the winner")
            for i in choice_dict:
                if(choice_dict[i]==b[t+1]):
                    print(i,"is the winner, chose", b[t+1])
                else:
                    choice_dict.pop(i)
            z, choice_dict = game("y", len(choice_dict))

        elif(a[t]==a[t+1] and a[t+1]>=2):
            print("Its a tie between",b[t],"and",b[t+1],"play again...")
            z, choice_dict = game("y", len(choice_dict))

        else:
            q = []
            p=0
            for h in choice_dict:
                q.append(h)
            if(choice_dict[q[p]]=="PAPER" and choice_dict[q[p+1]]=="STONE"):
                print(q[p],"wins and has got",choice_dict[q[p]],"...",q[p+1],"got",choice_dict[q[p+1]])
                choice_dict.pop(q[p + 1])
            elif (choice_dict[q[p]] == "SCISSOR" and choice_dict[q[p + 1]] == "PAPER"):
                print(q[p], "wins and has got", choice_dict[q[p]], "...", q[p + 1], "got", choice_dict[q[p + 1]])
                choice_dict.pop(q[p + 1])
            elif (choice_dict[q[p]] == "STONE" and choice_dict[q[p + 1]] == "SCISSOR"):
                print(q[p], "wins and has got", choice_dict[q[p]], "...", q[p + 1], "got", choice_dict[q[p + 1]])
                choice_dict.pop(q[p + 1])
            else:
                print(q[p],"got",choice_dict[q[p]],"and",q[p+1],"got",choice_dict[q[p+1]],"...",q[p],"lost from",q[p+1])
                choice_dict.pop(q[p])

    elif(len(z)==1):
        print("All Players made the same choice...play again")


if len(choice_dict)==1:
    for g in choice_dict:
        print(g,"CONGRATULATIONS!!!!!!")'''

'''a=["a","b","c","d"]
shift = int(input("Enter the no.-"))

for i in range(shift):
    c = a.pop()
    a.insert(0,c)

print(a)'''

'''def esti(num,wrep):
    choc=0
    c = int(num / wrep)
    d = wrep * c
    choc = choc + num + c
    e = num - d
    if(e>=3):
        esti(e,wrep)
    else:
        if(d!=c):
            esti(c,wrep)
        else:
            pass

    return choc,e


num = 18
wrep = 3
t,s = esti(num,wrep)
print(t,s)'''

'''def rotate(lst, n):
    print(lst)
    for i in range(n):
        a = lst.pop(0)
        lst.append(a)
    print(lst)


lis = [1,2,3,4,5,6]
n=int(input("Enter number"))
rotate(lis,n)'''

'''def combination(word_lst):
    str = ""
    lst = []
    for i in range(0,len(word_lst)):
        for j in (1,len(word_lst)):
            word_lst[i,j] = word_lst[j,i]
    for l in word_lst:
        str+=l
    if str not in lst:
        lst.append(str)
        combination(word_lst)

    return lst


word = "abcdef"
a=[]
for i in word:
   a.append(i)
d = combination(a)
print(d)'''

'''path = "/home/admin7/Documents/errors.xlsx"
row_count = XLUtils.getRowCount(path,"Sheet1")
for i in range(2,row_count+1):
    url = XLUtils.readData(path,"Sheet1",i,2)
    new_url = "https://www.tradeindia.com"+url
    x = requests.head(new_url)
    c = x.status_code
    d = i-1
    print(d,".",new_url,"--",c)
    XLUtils.writeData(path,"Sheet1",i,3,c)'''

directory = "Kartikey"

path = "/home/admin7/Documents"

new_path = os.path.join(path,directory)

os.mkdir(new_path)