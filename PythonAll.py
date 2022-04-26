# --------- Conditional Statements-------------
# --------- if-else with OR operator -------------
"""
gen=input("Are you Male(y/n):")
if gen == 'y' or gen == 'Y':
    print("Gender:Male")
else:
    print("Gender:Female")
    

# ---------- if-else with AND operator (voting age example) ---------

age=int(input("Enter your Age:"))
    #consider 120 upper limit
if age >= 18 and age <= 120:
    print("you are eligible for voting...")
else:
    print("you are NOT eligible for voting...")

# ---------- if-elif -------------
#casting input into integer
marks = int(input("Enter your Marks:"))
if marks < 35:
    print("Grade 'F':Fail")
elif marks >= 35 and marks <= 40:
    print("Grade 'D'")
elif marks >= 41 and marks <= 50:
    print("Grade 'C'")
elif marks >= 51 and marks <= 60:
    print("Grade 'B'")
elif marks >= 61 and marks <= 70:
    print("Grade 'B+'")
elif marks >= 71 and marks <= 80:
    print("Grade 'A'")
else:  #marks>80
    print("Grade 'A+'")

# ------------ Nested if ------------
n=int(input("Enter a number:"))
if n > 10:
    print("Number is greater than 10")
    if n % 2 == 0:
        print("Number is Even....")
    else:
        print("Number is Odd....")
else:
    print("Number is smaller than 10 or equal 10")

# ------------ Switch case alternative using Dictionary -------------
# Switch alternative - using dictionary to Return value

myswitch = {
    1:"ONE",
    2:"TWO",
    3:"THREE",
    4:"FOUR",
    5:"FIVE",
}
#TAKE USER INPUT AS INTEGER
num = int(input("Enter any no.(1 to 5)"))
print('you enter:',myswitch.get(num,"invalid number"))
#'INVALID NUMBER' IS THE DEFAULT VALUE IF NO CASES MATCHES THE INPUT

# ----------- Python Loops for & while ------------ #
# ----------- For loop - Accessing Elements
os = ["windows","MacOS","unix","linux"]
for x in os:
    print(x)

# ------------ for loop sequence of chars in string  --- Accessing chars of string one by one --------------
for x in "Python":
    print(x)

# ----------- for loop print square of numbers using range function -------
for x in range(1,11):
    print("Square of",x," is ",x*x)

# -------for loop print MULTIPLICATIVE table--------
n = int(input("Enter a number:"))
for i in range(1,11):
    print(n*i)

# ------- for-else -- else with for loop, else portion runs at the end od the loop ----------
for x in range(6):
    print(x)
else:
    print("End of Loop")


# --------- range function demo ----------- #
#the range() function returns a sequence of n numbers(from 0 to n-1),starting from 0 by default and increments by 1 by default
for x in range(6):
    print(x)
#print 0 to 5

# ------ demo 2 -----
for x in range(5,10):
    print(x)
#print 5 to 9

# ------ demo 3 -----
for x in range(0,10,+2):
    print(x)
#print 0 to 9 incremented by 2

# ------ demo 3 -----
for x in range(10,1,-2):
    print(x)
#print 10 to 2 decremented by 2


# ---------- While loop --------- #
n = 0
while n != 1:
    print("you are inside the while loop")
    print("press 1 to exit from the loop:")
    n = int(input())
print("you are out of the while loop")

# ------ while loop print no. example --------
n = 1
while n <= 10:
    print(n)
    n += 1

# ------ while loop print square of no. --------
n = 1
while n != 0:
    n = int(input("Enter no:"))
    print("square of no. is:",n*n)
print("end of program..")

# ---- while-else -- else with while loop, else portion runs at the end of the loop ------
num = 1
while num <= 5:
    print(num,"is less than 5")
    num += 1
else:
    print("we reached to 5")


# ----------- Nested loop -- MULTIPLICATIVE table from 1 to 10 ----------- #
for x in range(1,11):
    for y in range(1,11):
        print("{0:02d} ".format(x*y),end="")
    print();


# ---------Loop Controlling Statements------------- #
# ----- break demo ---- #
for x in range(5):
    if(x == 3):
        break
    print("number is ",x)


# ------ continue demo ------ #
for x in range(5):
    if(x == 3):
        continue
    print("number is ",x)


# -------- break and continue demo -------- #
while(1):
    print("\n Enter no.(<=100)to find Square.")
    print("press 0 to exit:")
    num = int(input())
    if num == 0:
        print("programs end . Thank you")
        break
    elif num > 100:
        print("number is greqater than 100 . Try again")
        continue
    print("\n Square of ",num,"is ",num*num)


# -------- pass demo 1-------- #
# in python, we cannot declare an empty loop,function,class,etc....
    # But if we want to create a loop(or function etc..) with no content,then we may use the "pass" statement to avoid getting error.
    # it just pass the control without executing any code.
    # if we want to bypass any code then "pass" statement can be used.

for x in range(5):
    pass

# ------- pass demo 2 -----
for x in range(5):
    if(x == 3):
        pass #if has no effect
    print("numer is :",x)

# ----- pass demo 3 -----
    # Empty loop #
for x in range(5):
    pass
    # Empty function #
def func():
    pass
    # Empty class #
class myClass:
    pass


####----------Pyton Standard Datatypes - List, Tuple, Dictionary, Set ---------####
# ---*****--- List ---*****--- #

# ------ create - define a list -------#
myList = ["iphone","oneplus","mi","oppo","google"]
print("list content:",myList)

# ------- list with different items --------
myList = [1,50,25,"apple","carrot",'A','Z','n',"Lion"]
print("list content:")
print(myList)

# -------- traverse list using loop -------
myList = ["iphone","oneplus","mi","oppo","google"]
print("All items of the list:")
for item in myList:
    print(item)

# ---------- access items using index ---------
myList = [1,50,25,"apple","carrot",'A','Z','n',"Lion"]
print("list content:",myList)
print("item at index 3 is :",myList[3])

# --------- access items using negative index ---------
# Negative indexing > beginning from the end
# -1 refers to the last item
myList = [1,50,25,"apple","carrot",'A','Z','n',"Lion"]
print("list content:",myList)
print("item at index -1 is :",myList[-1])

# ------- access item - index range ----------
# specifying a range,the return value will be a new list with the specified items
# [2:5] >> index 2 to 4(5 not included)
myList = ["c","c++","c#","java","Python","Ruby","Kotlin"]
print("list content:",myList)
print("item in range [2:5] is :",myList[2:5])
#with use of enumerate function
myList = ["c","c++","c#","java","Python","Ruby","Kotlin"]
for ix,val in enumerate(myList): #enumerate extract 2 values at time like in this it extract index & value
    print(f"At index {ix} value is {val}")

# ------ modify item ------
cities = ["ahbd","hlvd","morbi","jaipur","indor"]
print("cities name (before 2018):")
print(cities)
cities[2] = "bhuj"
print("\n cities name(after 2018):")
print(cities)

# --------- length -------
myList = ["iphone","oneplus","mi","oppo","google"]
print("list content:",myList)
print("length of list : ",len(myList))

# ----------- Add item-append() ---------
os = ["windows","unix","linux"]
print("os list:",os)
os.append("MacOS")
print("\n os list after append:")
print(os)

# ----------- Add item-insert() ---------
os = ["windows","unix","linux"]
print("os list:",os)
os.insert(1,"MacOS")
print("\n os list after insert:")
print(os)

# ------- Remove item - remove() --------
myList = ["iphone","oneplus","mi","oppo","google"]
print("list content:",myList)
myList.remove("oppo")
print("list content after remove:",myList)

# ------- Remove item - pop() --------
# pop() >> removes the specified index
# or remove the last item if index is not specified
myList = ["iphone","oneplus","mi","oppo","google"]
print("list content:",myList)
myList.pop(0)
print("list content after pop(0):",myList)
myList.pop()
print("list after pop():",myList)

# --------- Remove item - using del --------
# del() >> removes the specified index
myList = ["iphone","oneplus","mi","oppo","google"]
print("list content:",myList)
del myList[1]
print("list after deleting item at index 1:")
print(myList)

# --------- Remove All(empty list) - using clear() --------
# clear() >> remove all items
myList = ["iphone","oneplus","mi","oppo","google"]
print("list content:",myList)
myList.clear()
print("list after clear():",myList)

# ---------- Delete list (del keyword) ---------
# del >> delete list
myList = ["iphone","oneplus","mi","oppo","google"]
print("list content:",myList)
del myList
print("list is deleted")

# -------- search item ---------
fruits = ["apple", "banana","cherry","dragon fruit"]
search = input("enter item to be searched:")
if search in fruits:
    print("YES",search," is in list")
else:
    print("NO",search," not in list")

# --------- copy list - copy() ---------
listA=["c","c++","java","python","c#"]
listB=listA.copy()
print("list B:",listB)

# --------- copy list - list() ---------
listA=["c","c++","java","python","c#"]
listB=list(listA)
print("list B:",listB)

# ---------- Add (concatenate) two list ---------
listA=['A','B','C','D','E']
listB=[1,2,3,4,5]
listC=listA+listB
print("list A:",listA)
print("list B:",listB)
print("list C:",listC)

# ---------- Reverse list --------------
myList = ["one","two","three"]
print("list :",myList)
myList.reverse()
print("reverse list:",myList)

# ---------- count occurrence of item - count() ------------
# count() >> number of times the item appears in the list
myList = [4,1,5,6,4,8,9,4,3,2,4,7]
print("list:",myList)
n = myList.count(4)
print("no of 4 in the items:",n)

# --------- sort list ---------
# sort() >> sorts the list in ascending order by default
# sort(reverse=true) >> sorts the list in descending order
myList = ["iphone","oneplus","mi","oppo","google"]
print("unsorted list:",myList)
myList.sort()
print("\n sorted list(increasing order):")
print(myList)
myList.sort(reverse=True)
print("\n sorted list(decreasing order):")
print(myList)


# ----*-*-*-*-*---- Multi-Dimention List ----*-*-*-*---- #

# ---------- create & access -----------
mList = [[1,2,3,4],[5,6,8,7],[3,2,6,9,4,1]]
print("all items in multidimentional list:")
print(mList)

# -------- access via loop -------
ml = [
    [1,2,3,4],
    [5,6,7,8],
    [9,6,3,1,4,7]
]
for i in range(len(ml)):
    for j in range(len(ml[i])):
        print(ml[i][j],end=" ")
    print()

#-------- create list with zero field ----------
r = 4
c = 3
ml = [[0 for x in range(r)]for x in range(c)]
print("all items in ml list:")
print(ml)

# ----------- add sublist - append() -------
# append() >> add element sublist at the end
ml = [[1,2,3],[4,5,6],[7,8,9]]
print("ml list:")
print(ml)
ml.append([1,5,9])
print("\n ml list after append:")
print(ml)

# --------- add more items in sublist - extend() ----------
ml = [[1,2,3],[4,5,6],[7,8,9]]
print("ml list:")
print(ml)
ml[0].extend([1,5,9])
print("\n ml list after extend:")
print(ml)

# --------- Reverse m.list - reverse() -----------
ml = [[1,2,3],[4,5,6],[7,8,9]]
print("ml list:")
print(ml)
ml.reverse()
print("\n ml list after reverse:")
print(ml)

# --------- Reverse sublist - reverse() -----------
ml = [[1,2,3],[4,5,6],[7,8,9]]
print("ml list:")
print(ml)
ml[1].reverse()  #index 1's sublist
print("\n ml list after reverse:")
print(ml)

# -------- sort M.list - sort() -------------
# sort() >> sort the sublists
ml = [[11,2,23],[2,14,9],[1,8,7]]
print(" ml list:")
print(ml)
ml.sort()
print("\n ml list after sort:")
print(ml)

# -------- sort sublist - sort() -------------
# sort() >> sort the elements of the sublists
ml = [[11,2,23],[2,14,9],[1,8,7]]
print(" ml list:")
print(ml)
ml[1].sort() #index 1's sublist
print("\n ml list after sort:")
print(ml)


# ----*-*-*-*-*- Tuple -*-*-*-*-*---- #

# --------- create & define tuple ---------
myTuple = ("c","c++","c#","java","python")
print("Tuple content:",myTuple)

# --------- Tuple with single item ----------
# in order to define a tuple with a single item,
# we have to add a comma after the item,so that python will recognize it as a tuple.
tuple = ("hello",)
print("tuple:",tuple)

# --------- traverse tuple using loop -------
myTuple = ("iphone","mi","vivo","oneplus","oppo")
print("all items in tuple:")
for item in myTuple:
    print(item)

# --------- Tuple length ---------
myTuple = ("iphone","mi","vivo","oneplus","oppo")
print("all items in tuple:",myTuple)
print("length of tuple:",len(myTuple))

# --------- search item's 1st occurrence - index() -----------
myTuple = (1,3,5,4,1,2,4,1,2,5,1,2,4,2,8,4)
num = int(input("enter number to be searched:"))
x = myTuple.index(num)
print("first occurrence of the ",num,"is at index:",x)

# ---------- Add(concatenate) two tuple ---------
tupleA = ('A','B','C','D','E')
tupleB = (1,2,3,4,5)
tupleC = tupleA + tupleB
print("tuple C:",tupleC)

# ---------------- delete tuple (del keyword) ---------
# del >> delete tuple
myTuple = ("iphone","mi","vivo","oneplus","oppo")
print("all items in tuple:",myTuple)
del myTuple
print("Tuple is deleted...")

# --------------- count occurrence of item - count() --------------
# count() >> number of times the item appears in the tuple
myTuple = (4,1,2,5,4,1,8,4,6,7,3,4,2,9,1)
print("Tuple:",myTuple)
n = myTuple.count(4)
print("total no. of a in the tuple is:",n)


# ----*-*-*-*-*- Set -*-*-*-*-*---- #

# ------ create & define set --------
mySet = {"c","c++","c#","java","python"}
print("set content:",mySet)

# --------- length of set -----------
mySet = {"c","c++","c#","java","python"}
print("set content:",mySet)
print("length of set:",len(mySet))

# --------- search item -------
fruits = {"mango","cherry","apple","pinaple"}
search = input("enter item to be searched:")
if search in fruits:
    print("yes,",search," is in set")
else:
    print("no,",search," is not in set")

# ------ add item - add() -------------
# add() >> add item,one at a time
os = {"windows","unix","linux"}
print("os:",os)
os.add("MacOS")
print("\n os list after add:")
print(os)

# -------- Add multiple items - update() ----------
os = {"windows","unix","linux"}
print("os:",os)
os.update(["MacOS","solaris"])
print("\n os after update:")
print(os)

# --------- remove item - discard --------
# discard() >> removes the specific item
mySet = {"c","c++","c#","java","python"}
print("set content:",mySet)
mySet.discard("c")
print("set after discard:",mySet)

# ---------- remove item randomly - pop() ----------
# pop() >> removes the last item,but as the set is unordered so any random item will be deleted
mySet = {"c","c++","c#","java","python"}
print("set content:",mySet)
x = mySet.pop()
print("item removed from set:",x)
print("set content after pop():",mySet)

# --------- Add (join) two sets - union() --------------
# union() >> returns a new set with all items from both sets(including duplicate items)
setA = {1,3,'A','B','c'}
setB = {1,'A','D',3,4,5}
setC = setA.union(setB)
print("set C:",setC)

# -------- join two sets - update() ---------
#update() >> insert set2 in set1 (including duplicate value)
setA = {1,3,'A','B','c'}
setB = {1,'A','D',3,4,5}
print("set A before update:",setA)
print("set B before update:",setB)
setA.update(setB)
print("set A after update:",setA)

# --------- intersection sets - intersection() --------
# intersection() >> returns a new set containing the item exists in both set
laptop = {"apple","dell","lenovo","acer"}
mobile = {"oneplus","apple","mi"}
both = laptop.intersection(mobile)
print("intersection of set is:",both)

# ---------- difference between sets - difference() -----------
#difference() >> returns a sets that contains , the items that only exists in one set
laptop = {"apple","dell","lenovo","acer"}
mobile = {"oneplus","apple","mi"}
onlyLaptop = laptop.difference(mobile)
print("laptop company in both of set is:",onlyLaptop)


# ----*-*-*-*-*- Dictionaries -*-*-*-*-*---- #

# -------- create & show dictionary -------
bike = {
    "brand":"Bajaj",
    "model":"Avenger",
    "year":2019,
    "engine":"220cc"
}
print("dictionary data:")
print(bike)

# -------- Traverse dictionary items - values() ----------------
bike = {
    "brand":"Bajaj",
    "model":"Avenger",
    "year":2019,
    "engine":"220cc"
}
print("dictionary data:")
for x in bike.values():
    print(x)

# ------- Traverse dictionary items key-value - items() ----------------
bike = {
     "brand":"Bajaj",
     "model":"Avenger",
     "year":2019,
     "engine":"220cc"
 }
print("dictionary data:")
for x in bike.items():
     print(x)

# ---------- change value of key --------
bike = {
     "brand":"Bajaj",
     "model":"Avenger",
     "year":2019,
     "engine":"220cc"
 }
print("bike items:")
for x in bike.items():
     print(x)
bike["model"] = "pulsar"
print("\n bike details after modify:")
for x in bike.items():
    print(x)

# --------- add items ---------
bike = {
     "brand":"Bajaj",
     "model":"Avenger",
     "year":2019,
     "engine":"220cc"
 }
print("bike items:")
for x in bike.items():
     print(x)
bike["color"] = "jet black"
print("\n bike details after adding:")
for x in bike.items():
    print(x)

# --------- add item - update() --------
bike = {
     "brand":"Bajaj",
     "model":"Avenger",
     "year":2019,
     "engine":"220cc"
 }
print("bike items:")
for x in bike.items():
     print(x)
bike.update({"color":"jet black"})
print("\n bike details after adding:")
for x in bike.items():
    print(x)

# --------- length of dictionary ---------
bike = {
     "brand":"Bajaj",
     "model":"Avenger",
     "year":2019,
     "engine":"220cc"
 }
print("bike items:")
for x in bike.items():
     print(x)
print("\n length of bike dictionary:",len(bike))

# ---------- check if key exists ---------
bike = {
     "brand":"Bajaj",
     "model":"Avenger",
     "year":2019,
     "engine":"220cc"
 }
search = input("enter key to be  searched:")
if search in bike:
    print("YES")
else:
    print("NO")

# --------- removinng item - del ---------
bike = {
     "brand":"Bajaj",
     "model":"Avenger",
     "year":2019,
     "engine":"220cc"
 }
print("bike items:")
for x in bike.items():
     print(x)
del bike["engine"]
print("\n after removing item:")
for x in bike.items():
    print(x)

# ------- removing all - clear() ----------
bike = {
     "brand":"Bajaj",
     "model":"Avenger",
     "year":2019,
     "engine":"220cc"
 }
print("bike items:")
for x in bike.items():
     print(x)
bike.clear()
print("\n bike details after clear:")
print(bike)

# --------- delete dictionary - del keyword ---------
bike = {
     "brand":"Bajaj",
     "model":"Avenger",
     "year":2019,
     "engine":"220cc"
 }
print("bike items:")
print(bike)
del bike
print("dictionary deleted..")

# -------- copy dictionary - copy() -----------
x = {
     "brand":"Bajaj",
     "model":"Avenger",
     "year":2019,
     "engine":"220cc"
 }
y = x.copy()
print("dictionary data y:")
print(y)

# ------- copy dictionary - dict() ------
x = {
     "brand":"Bajaj",
     "model":"Avenger",
     "year":2019,
     "engine":"220cc"
 }
y = dict(x)
print("dictionary data y:")
print(y)

# --------- nested dictionary --------
laptop = {
    "brand":"MacBook",
    "os":"MacOS"
}
mobile = {
    "brand":"iphone",
    "os":"ios"
}
Apple = {
    "laptop":laptop,
    "mobile":mobile
}
print("Apple products:")
for x in Apple.items():
    print(x)


# ----*-*-*-*-*- Array -*-*-*-*-*---- #

# -------- Array demo -------
import array
# integer array
arrInt = array.array('i',[1,2,3,4,5])
# float array
arrFloat = array.array('f',[1.1,2.2,3.3,4.4,5.5])
# char array
arrChar = array.array('u',['A','B','C','D','E'])
print("integer array:")
for x in range(len(arrInt)):
    print(arrInt[x])
print("float array:")
for x in range(len(arrFloat)):
    print("{0:.2f}".format(arrFloat[x]))
print("character array:")
for x in range(len(arrChar)):
    print(arrChar[x])

# -------- Access item using index ---------
import array as arr
numArr = arr.array('i',[10,20,30,40,50])
print("array item at index 2 : ")
print(numArr[2])  # print 30
# negative indexing
print("Array index at index 3 : ")
print(numArr[-2])  # print 40

# -------- Access items in range (slice arrays) --------------
import array as arr
numArr = arr.array('i',[10,20,30,40,50,60,70,80])
print(numArr[3:6])  # 4th to 6th
print(numArr[:-3])  # beginning to 5th
print(numArr[3:])  # 4th to end
print(numArr[:])  # beginning to end

# ------- Modifying items -----
import array as arr
numArr = arr.array('i',[10,20,30,40,50,60,70,80])
print("Array items:")
print(numArr)
# changing index 3 value
numArr[3] = 44
print("\n array items after changing or modifying:")
print(numArr)
# changing 1st to 5th index values
numArr[1:5] = arr.array('i',[-8,-5,-6,-7])
print("\ array items after modify in -range:")
print(numArr)

# --------- add items - append() ---------
import array as arr
numArr = arr.array('i',[10,20,30])
print("Array items:")
print(numArr)
# add item at the end
numArr.append(40)
print("\n array items after add:")
print(numArr)

# -------- add items - insert() --------
import array as arr
numArr = arr.array('i',[10,20,30])
print("Array items:")
print(numArr)
# add 25 at index 2
numArr.insert(2,25)
print("\n array items after add:")
print(numArr)

# --------- remove items (del keyword) ---------
import array as arr
numArr = arr.array('i',[10,20,30,40,50])
print("Array items:")
print(numArr)
# remove item at the index 2
del numArr[2]
print("\n array items after remove index 2:")
print(numArr)
# whole array delete
del numArr
print("\n array is deleted...")

# --------- remove items - remove() --------
import array as arr
numArr = arr.array('i',[10,20,30,40,50])
print("Array items:")
print(numArr)
numArr.remove(30)
print("\n array items after remove 30:")
print(numArr)

# -------- remove items - pop() ----------
import array as arr
numArr = arr.array('i',[10,20,30,40,50])
print("Array items:")
print(numArr)
# delete item at index 1
numArr.pop(1)
print("\n array items after pop:")
print(numArr)

# --------- Array reverse - reverse() --------
import array as arr
numArr = arr.array('i',[10,20,30,40,50])
print("Array items:")
print(numArr)
# reverse the array
numArr.reverse()
print("\n array items after reverse:")
print(numArr)

# -------- add 2 arrays - extend() --------
import array as arr
numA = arr.array('i',[10,20,30])
numB = arr.array('i',[40,50,60])
print("Array A:")
print(numA)
numA.extend(numB)
print("\n array A after extend:")
print(numA)

# ---------- add 2 array using '+' ------
import array as arr
numA = arr.array('i',[10,20,30])
numB = arr.array('i',[40,50,60])
numC = numA + numB
print("Array C:",numC)

# ------- count occurrence of item - count() -------------
# count() >> number of times the item appears in the list
import array as arr
numA = arr.array('i',[1,2,4,6,3,4,8,9,4,7,5,4,3,2,1,4])
print("Array:",numA)
n = numA.count(4)
print("total count of 4 in array:",n)


# -----*-*-*-*-*- Function(def) -*-*-*-*-*----- #

# -------- define and calling function ---------
def my_fun():
    print("hello from function ")
my_fun()

# ------- function with parameters -----------
def capitals(country,capital):
    print("Country:",country,">>Capital:",capital)
capitals("India","New Delhi")
capitals("England","London")

# --------- function with default parameters ----------
def func(hobby="coding"):
    print("I Love ",hobby)
func("singing")
func("dancing")
func()
func("travelling")

# --------- keyword argument (kwargs) ---------
def func(firstname,lastname):
    print("your surname is:",lastname)
func("Vipul","Patel")  #normal
func(firstname="Nita",lastname="Vadodariya")  #kwargs

# -------- variable Argument -------
def func(*proglang):
    print("Programming Language Known:")
    for x in proglang:
        print(x)
print("1st function call")
func("C#","Python")
print("\n 2nd function call")
func("AI","Ruby","ML")

# ---------- Passing list to a function --------
def func(sport):
    print("Sports:")
    for x in sport:
        print(x)
games = ["Cricket","Hockey","Football","Polo"]
func(games)

# -------- Pass function -----
# Function definition cannot be empty.
# But if we want an empty function for some reason, put in the pass statement to avoid getting an error.
def func():
    pass

# -------- Recursion --------
# Factorial of a number is the product of the number and all numbers below it.
# for ex., 4! = 4*3*2*1    --->> NOTE : Factorial of 0 is 1
# defining a function
def fact(n):
    if n <= 1:
        return 1
    else:
        n = n * fact(n-1)
        return n
n = int(input("Enter Number:"))
print("Factorial:",fact(n))

# ------ Function inside function ----------
def outer():
    print("Outer or Main function...")

    def inner():
        print("inner function...")
    inner()
outer()

# ------- Global variable ---------
x = 100
def func():
    global x
    x = 50
print("variable of x:",x)
func()
print("value of x after call function:",x)

# --------- Function demo add 2 nums ---------
def add(a,b):
    return a+b
n1 = int(input("enter 1st num:"))
n2 = int(input("enter 2nd num:"))
ans = add(n1,n2)
print("Addition : ",ans)

# --------- Function demo (sq,cube) -----------
def square(a):
    print("square:",(a*a))
def cube(a):
    print("cube:",(a*a*a))
n = int(input("enter number:"))
square(n)
cube(n)


# -----*-*-*-*-*- Lambda Functions -*-*-*-*-*----- #

# ------- lambda function demo 1 - sum --------
# lambda function to add two numbers
x = lambda a,b:a+b
print("sum:",x(10,20))

# -------- lambda function demo 2 - larger --------
# lambda function to find greater number
x = (lambda n,m:(n>m and 'First' or 'Second'))
print(x(50,20),"number is greater")

# --------- lambda function demo 3 - even odd -----------
# lambda function to find even odd num
x = (lambda x:(x % 2 and 'odd' or 'even'))
print("number is",x(5))

# ---------- lambda inside function -------
def double(n):
    return  lambda a:a*n
cal = double(2)
print("result:",cal(6))

# --------- lambda with filter() --------
numbers = [1,3,6,2,7,5,8,4,9,0]
result = filter(lambda x:x<5,numbers)
print("number list:",numbers)
print("numbers smaller than 5 in list :")
print(list(result))

# ---------- lambda with map() ---------
# map() perform square function for all item of the list
def square(n):
    return n*n
result = map(square,[1,2,3,4])
print("Square of num in the list:")
print(list(result))

# --------- lambda with reduce() ---------
# reduce() operates on each item of the list,in the following manner:
# r1=1+2
# r2=r1+3
# r3=r2+4
# r4=....
from functools import reduce
numbers = [1,2,3,4,5]
prod = reduce(lambda x,y:x*y,numbers)
print("product of all numbers in list:",prod)


# -----*-*-*-*-*- Class Object -*-*-*-*-*----- #

#--------- class object demo 1 ---------
class MyClass:
    x = 10
obj = MyClass()
print("value of class attribute x : ",obj.x)

# ---------- class object demo 2 --------
class MyClass:
    def func(self):
        print("Hello i m a class function")
obj = MyClass()
obj.func()

# -------- init() & self (constructor) --------
class MyClass:
    def __init__(self):
        print("hello from init() function[constructor]")
    def func(self):
        print("hello from func() function")
obj = MyClass()
obj.func()

# -------- init() & self (parameterized constructor) -----------
class VotingAge:
    def __init__(self,eligibleAge):
        self.eligibleAge = eligibleAge
    def isEligible(self,user_age):
        if user_age >= self.eligibleAge:
            print("you are eligible for voting")
        else:
            print("you are not....")
v1 = VotingAge(18)  # for india
v1.isEligible(25)  # print eligible
v2 = VotingAge(16)  # for Argentina
v2.isEligible(14)  # not eligible

# --------- Modifying object properties ---------
class Student:
    def __init__(self,name,course):
        self.name = name
        self.course = course
    def show(self):
        print("Student details...")
        print("name:",self.name)
        print("course:",self.course)
s = Student("Niki","BCA")
s.show()
# change course
s.course = "MCA"
print("after change")
s.show()

# ----------- Delete object properties - del ----------
class Student:
    def __init__(self,name,course,age):
        self.name = name
        self.course = course
        self.age = age
s = Student("Niki","BCA",19)
print("Name:",s.name)
print("course",s.course)
print("age:",s.age)
# deleting age
del s.age
print("after  deleting age")
print("Name:",s.name)
print("course",s.course)

# --------- Delete Object (del keyword) --------
class Student:
    def __init__(self,name,course):
        self.name = name
        self.course = course
    def show(self):
        print("name:",self.name)
        print("course:",self.course)
s1 = Student("Niki","BCA")
s2 = Student("Mansi","BCA")
s1.show()
s2.show()
# delete s2
del s2
s1.show()


# -----*-*-*-*-*- Inheritance -*-*-*-*-*----- #

# ------- Single Inheritance ---------
class Base:
    def sum(self,a,b):
        return a+b
class Derived(Base):
    def multi(self,a,b):
        return a*b
n1 = int(input("Enter a:"))
n2 = int(input("Enter b:"))
d = Derived()
print("from base class sum :",d.sum(n1,n2))
print("from derived class multiply :",d.multi(n1,n2))

# ---------- Hierarchical Inheritance --------
class Base:
    a = 10
    b = 20
class Derived1(Base):
    def sum(self):
        add = self.a + self.b
        print("Addition:",add)
class Derived2(Base):
    def multi(self):
        mul = self.a * self.b
        print("Multiply:",mul)
d1 = Derived1()
d2 = Derived2()
d1.sum()
d2.multi()

# -------- Multiple Inheritance -------
class Student:
    def getName(self,name):
        print("Name:",name)
class Mark:
    def getMark(self,python,ai):
        print("Python:",python)
        print("AI:",ai)
class Info(Student,Mark):
    def getInfo(self):
        self.getName("niki")
        self.getMark(95,90)
i = Info()
i.getInfo()

# ------- Multilevel Inheritance --------
class University:
    def getUniDtl(self):
        self.uname = input("Enter University name:")
        self.rno = input("Registration No:")
    def showUniDtl(self):
        print("University name:",self.uname)
        print("uni registration no:",self.rno)
class College(University):
    def getClgDtl(self):
        self.cname = input("Enter College Name:")
        self.cno = input("Enter College No:")
        self.getUniDtl()
    def showClgDtl(self):
        print("College name:",self.cname)
        print("college no:",self.cno)
        self.showUniDtl()
class Student(College):
    def getStudDtl(self):
        self.sname = input("Student name:")
        self.eno = input("Enrollment No:")
        self.scourse = input("Course Name:")
        self.getClgDtl()
    def showStudDtl(self):
        print("\n Student Information:")
        print("student name:",self.sname)
        print("student eno:",self.eno)
        print("student course:",self.scourse)
        self.showClgDtl()
s = Student()
s.getStudDtl()
s.showStudDtl()

# -------- Hybrid Inheritance ---------
class Student:
    def getStudDtl(self):
        self.sname = input("Enter student name:")
        self.rno = input("Enter RollNo:")
    def showSD(self):
        print("Student Name:",self.sname)
        print("Student RNo:",self.rno)
class Marks(Student):
    total = 0
    def getMark(self):
        for x in range(4):
            print("Subject ",(x+1),":",end="")
            self.mark = int(input())
            self.total = self.total + self.mark
    def getTotal(self):
        self.showSD()
        return self.total
class Sports:
    spname = ""
    grade = 0
    def getSport(self):
        self.spname = input("Enter Sport name:")
    def getSmarks(self):
        return self.grade
    def showSport(self):
        print("Sport Name:",self.spname)
class Result(Marks,Sports):
    def getResult(self):
        self.getStudDtl()
        self.getMark()
        self.getSport()
    def showResult(self):
        mTotal = int(self.getTotal())
        sTotal = int(self.getSmarks())
        per = (mTotal+sTotal)/4
        print("Percentage :{:.2f}".format(per))
        self.showSport()
r = Result()
r.getResult()
r.showResult()

# ------- Super keyword --------
class Parent:
    def func1(self):
        print("this is parent class")
class Child(Parent):
    def func1(self):
        print("this is child class function 1")
    def func2(self):
        super().func1()  # calling parent class
        self.func1()  # calling child func1
        print("this is child 2nd function")
ch = Child()
ch.func2()


# -----*-*-*-*-*- Exception Handling -*-*-*-*-*----- #

# ------ Try except --------
try:
    print(num)
except:
    print("error.....")

# -------- Handle Multiple Exception --------
print("Name Error 1:")
print("Ttpe Error 2:")
print("ZeroDivisionError Error 3:")
ch = int(input("Enter your Choice:"))
try:
    if ch == 1:
        print(num)
    elif ch == 2:
        x = 'ABC'+10
    else:
        x = 10/0
except NameError:
    print("Name Error....")
except TypeError:
    print("Type mismatch Error....")
except ZeroDivisionError:
    print("Divide by Zero Error....")

# ------- Else Clause ------
print("Press 1 generate exception")
print("Press 2 safe execution")
ch = int(input("Enter your choice:"))
try:
    if ch == 1:
        x = 10/0
except:
    print("Exception generated....")
else:
    print("Safe execution....")

# -------- Finally -------
print("press 1 generate exception.")
print("press 2 safe execution..")
ch = int(input("Enter your Choice:"))
try:
    print("\n try execute.")
    if ch == 1:
        x = 10/0
except:
    print("Exception occured...")
finally:
    print("Finally Block are Executed....")

# ------- Raise an Exception -------
num = -1
if num < 0:
    raise Exception("exception no. is smaller than 0.....")
"""
"""
# Python Intro:
    -->> Python is a widely used general purpose,interpreted,high level Programming language.
    -->> Developed by:  "Guido van Rossum in 1991 at the National Research Institute for 
                         Mathematics and Computer Science in Netherlands".
    -->> Python is named after the comedy television show Monty Python's Flying Circus.
    
# important feature of Python:
    -->> Easy to learn
    -->> cross platform
    -->> open sourse
    -->> huge library support
    -->> efficient memory management

# use of Python:
    -->> server-side web development
    -->> software development
    -->> Machine Learning
    -->> data analysis
    -->> system scripting
    -->> AI implementation
    
# List of Python Keywords :
    -->> and - Logical AND operator
    -->> as  - To create and alias
    -->> asert - for debugging
    -->> break - Breaking a Loop
    -->> class - To define a class
    -->> continue - To continue to the next iteration of a loop
    -->> def - To define a function
    -->> del - To delete an object
    -->> elif - Used to conditional statements(else if)
    -->> else - used in conditional statement
    -->> except - used with exception,performs when exception occurs
    -->> False - boolean value
    -->> finally - used with exception , a block of code that will be execute always
    -->> for - For Loop
    -->> from - import specific parts of a module
    -->> global - To declare a global variable
    -->> if - A conditional statement
    -->> import - Import a module
    -->> in - To check if a value whether it is present in list,tuple,etc...
    -->> is - To test if two variables are equal
    -->> lambda - To create an anonymous function
    -->> None - Represent a Null Value
    -->> nonlocal - To declare a non-local variable
    -->> not - Logical NOT operater
    -->> or - Logical OR operator
    -->> pass - Null or do nothing variable
    -->> raise - To raise an exception
    -->> return - To exit a function and return a value
    -->> true - boolean value
    -->> try - Used with exception , contain the code that create exception
    
# Python Operator :
    -->> Operator   Meaning
         -----------------------------------
            **      Exponentiation(power)
         -----------------------------------
            ~       Complement
            +       Unary plus
            -       Unary minus
         -----------------------------------
            *       multiply
            /       Divide
            %       Reminder(modulo-division)
            //      Floor division
         ------------------------------------
            +       Binary plus(addition)
            -       binary minus(substraction)
         -------------------------------------
            <<      Left shift
            >>      Right shift
         -------------------------------------
            &       Bitwise AND
            ^       bitwise Ex OR
            |       bitwise OR
         -------------------------------------
            <       Less than
            <=      less than or equal
            >       greater than
            >=      greater than or equal
            ==      equal to
            !=      not Equal to
         --------------------------------------
            =       Assignment operator
            %=
            /=
            //=
            -=
            +=
            *=
            **=
         ---------------------------------------
            is      identity operator
            is not  
         ---------------------------------------
            in      Membership operator
            not in  
         ---------------------------------------
            not     Logical NOT operator
         ---------------------------------------
            
# List :-
            List is a collection which is ordered and changeable.
            In list duplicate members are allowed.
            In python lists are written with square brackets.
            Ex.,  list=["milk","cotton","wheat"]
# Tuple :-
            A Tuple is a collection which is ordered and unchangeable.
            In tuple duplicate members are allowed.
            In python tuple are written with round brackets.
            Ex.,  tuple=("milk","cotton","wheat")
# Set :- 
            A set is a collection that is unordered and unindexed.
            In sets, duplicate members are omited.
            In python, sets are written with curly brackets.
            Ex.,  set={"milk","cotton","Wheat"}
# Dictionary :-
            A dictionary is an unordered,changeable and indexed collection that have keys and values.
            In dictionary duplicate keys are omited.
            In python dictionary are written with curly bracket.
            Ex.,  dict={"key":"value"}
# Function :-
            Function is a group of statements which performs predefined task.
# Module :-
        -->> In python, a module can defined as a file that  contains a python code including python functions,
                 class or variables.
        -->> Module allow as to logically organize our python code and grouping related code into a module makes
                 the code easier to understand and use.
        -->> It is similar to packages in java.
# Array :-
            Array is a collection of variables having similar data-types.
# Class :-
            Class is a blue-print from which objects are created.
            Class contains data member to store information & member function to operate upon data members.
# Object :-
            Object is an instance of a class.
            It is basically a real-world implementation of the class having all those property values which are
                defined or structured in the class.
# Inheritance :-
            When a class inherits or acquires the property of another class, this is known as inheritance.
# Base class :- Whose properties are inherited by  another class.
# derive class :- one who inherit the properties os the base class.
# Exception :-
            Run time errors are known as exception.
# Exception Handling :-
            Exception handling is a mechanism to handle runtime errors(exception).
# File Handling :-
            File handling is a way of dealing with the data on the secondary storage devices from a program.
            File handling operations include--- opening file, reading file, writing file, closing file,etc.... 

"""
