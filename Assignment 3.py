#ASSIGNMENT 3

#__________Question 1__________


import collections

# Taking input from user.
inp_str=str(input('Enter a word/sentence: '))

# Splitting string
str_list=inp_str.split()

# For one word or character
if len(str_list)==1:
    str_letters=collections.Counter(inp_str)
    print(str_letters)

# For multiple words or sentence
if len(str_list)>1:    
    str_words=collections.Counter(str_list)
    print(str_words)

#__________Question 2__________


# Asking for input from user
day=int(input('Enter day (1-31):'))
month=int(input('Enter month (1-12):'))
year=int(input('Enter year (1800-2025):'))

# Inputs that are not possible for date
if day>31 or month>12 or year>2025 or year<1800:
    print('not possible')


else:
    # For months with 31 days 
    if 1<=day<31 and month in (1,3,5,7,8,10,12):
        nxt_day_31=day+1
        print('Next date is {}/{}/{}'.format(nxt_day_31,month,year))

    # For months with 30 days
    if 1<=day<30 and month in (4,6,9):
        nxt_day_30=day+1
        print('Next date is {}/{}/{}'.format(nxt_day_30,month,year))
    
    # For changing of months with 31 days
    if day==31 and month in (1,3,5,7,8,10):
        nxt_month_31=month+1
        print('Next date is 1/{}/{}'.format(nxt_month_31,year))

    # For changing of months with 30 days
    if day==30 and month in (4,6,9):
        nxt_month_30=month+1
        print('Next date is 1/{}/{}'.format(nxt_month_30,year))

    # For February
    if 1<=day<28 and month==2:
        feb_date=day+1
        print('Next date is {}/{}/{}'.format(feb_date,month,year))

    # For leap year
    if day==28 and month==2 and year%4==0:
        print('Next date is 29/02/{}'.format(year))
    
    # For non-leap year
    if day==28 and month==2 and year%4 in range(1,3):
        print('Next date is 1/3/{}'.format(year))
    
    # For changing of year
    if day==31 and month==12:
        nxt_year=year+1
        print('Next date is 1/1/{}'.format(nxt_year))


#__________Question 3__________


# Taking inputs
a=3
b=9
c=10

# List will be created with input and square of input
a=[(x,x**2)for x in[a,b,c]]
print(a)


#__________Question 4__________


#Input grade points
grade=float(input('Enter your grade points between 4 and 10:'))

#printing user's grade and performance
if 4<=grade<5:
    print("Your Grade is D and Poor Performance.")

if 5<=grade<6:
    print("Your Grade is C and Below Average Performance.")

if 6<=grade<7:
    print("Your Grade is C+ and Average Performance.")

if 7<=grade<8:
    print("Your Grade is B and Good Performance.")

if 8<=grade<9:
    print("Your Grade is B+ and Very Good Performance.")

if 9<=grade<10:
    print("Your Grade is A and Excellent Performance.")

if grade==10:
    print("Your Grade is A+ and Outstanding Performance.")
    
if grade>10 or grade<4:
    print('Error: value is out of range.')


#__________Question 5__________


# Input
n='ABCDEFGHIJKLM'

# Number of substrings to be reduced from main string
a=-2

# While loop to keep reducing string
while len(n)>1:

    # Print reduced string
    print(n[:a])

    # Reduce a in value to give smaller string
    a=a-2

    # To terminate while loop
    if -a>len(n):
        break


#__________Question 6__________


# Creating dict using inputs
class_list=dict()
SiD=(input('Enter SID:'))
Name=(input('Enter name:'))
class_list[SiD]=Name

# For continuation or termination
Decision=str(input('Do you want to continue ("y"- yes , "n"- no):'))

# For yes continue and for no terminate
while Decision=='y':

    # Taking inputs
    SiD=(input('Enter SID:'))
    Name=(input('Enter name:'))
    class_list[SiD]=Name

    # For continuation or termination
    Decision=str(input('Do you want to continue ("y"- yes , "n"- no):'))

    # Continue for yes
    if Decision=='y':
        continue
    # Terminate for no
    if Decision=='n':
        break
print(class_list)

# Ascending order of SIDs
print('Dictionary sorted according to student"s SIDs:')
for i in sorted (class_list) :
    print((i,class_list[i])) 

# Alphabetical order of names
print('Dictionary sorted according to student"s names:')
rev_class_list={ value:key for (key,value) in class_list.items()}
for x in sorted (rev_class_list):
    print((x,rev_class_list[x]))

# Function to search name of student using SID
def SIDsearch(class_list,SID):

    # If SID in dictionary
    if SID in class_list:
        print('Your entered SID:',SID)
        print('Name of Student:',class_list[SID])

    # If SID not in dictionary    
    else:
        print('SID not in dictionary')
    return

SID=input('Enter the SID you want to search:')
SIDsearch(class_list,SID)


#__________Question 7__________


# Input number of terms.
no_of_terms=int(input('Enter the number of terms to generate Fibonacci Sequence: '))

# Starting terms and count.
fib=0
fib1=1
count=0

# For invalid number of terms
if no_of_terms<1:
    print('invalid input')

# For input=1
if no_of_terms==1:
    print(fib)

# For valid number of terms
else:
    while count<no_of_terms:
        print(fib)
        temp_var = fib + fib1
        fib = fib1
        fib1 = temp_var
        count+=1

# For average of Fibonacci Sequence.
def FiboAvg(no_of_terms) :
    if no_of_terms <= 0 :
        return 
    
    if no_of_terms==1:
        return print('Average of Fibonacci Sequence: 1')
  
    fibo =[0] * (no_of_terms+1)
    fibo[1] = 1
  
    # Initialize result
    sm = fibo[0] + fibo[1]
  
    # Add remaining terms
    for i in range(2,no_of_terms) :
        fibo[i] = fibo[i-1] + fibo[i-2]
        sm = sm + fibo[i]
        avg=sm/no_of_terms

    return print('Average of Fibonacci Sequence:',avg)

FiboAvg(no_of_terms)


#__________Question 8__________


Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
Set1_10={1,2,3,4,5,6,7,8,9,10}

# Set of all elements that are in Set1 and Set2 but not both.
x=Set1.symmetric_difference(Set2)
print(x)

# New set of all elements that are in only one of the three sets Set1,
# Set2 and Set3.
s=Set1.symmetric_difference(Set2)
v=s.symmetric_difference(Set3)
print(v)

# New set of elements that are exactly two of the sets Set1, Set2 and Set3.

# Taking Intersection of all the sets.
S1nS2=Set1.intersection(Set2)
S2nS3=Set2.intersection(Set3)
S3nS1=Set3.intersection(Set1)
# Combining all intersections.
Combine={*S1nS2,*S2nS3,*S3nS1}
print(Combine)

# New set of all integers in the range 1 to 10 that are not in Set1.
c=Set1.symmetric_difference(Set1_10)
print(c)

# New set of all integers in the range 1 to 10 that are not in Set1,
# Set2 and Set3.

# Taking unions of all sets
S1US2=Set1.union(Set2)
S2US3=Set2.union(Set3)
S3US1=Set3.union(Set1)

# Adding all created sets
Union={*S1US2,*S3US1,*S2US3}

# Removing elements in Set1_10 which re present in Union
Set1_10.difference_update(Union)
print(Set1_10)


#___________________________OVER_____________________________

    


