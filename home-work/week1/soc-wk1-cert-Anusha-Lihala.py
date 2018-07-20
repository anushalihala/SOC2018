import datetime 
import random
import pdb
#________________________________DAY 1______________________________________________

def hours_in_year():
    ans = 365*24
    return ans
    
def minutes_in_decade():
    ans = 10*365*24*60
    return ans
    
def age_in_seconds(bd_day,bd_month,bd_year):
    bday=datetime.datetime(bd_year,bd_month,bd_day)
    today=datetime.datetime.now()
    diff=today-bday
    return diff.total_seconds()
    
def system_timeout(word_size):
    #in days
    ans=(2**word_size)/(1000*60*60*24)
    return round(ans)
    
#________________________________DAY 3______________________________________________

def greeting():
    first=input("What's your first name?: ")
    middle=input("What's your middle name?: ")
    last=input("What's your last name?: ")
    full_name=first+' '+middle+' '+last
    print('Hello',full_name,'!')
    
def favourite_number():
    no_number=True
    while(no_number):
        try:
            fav_no=int(input("What's your favourite number?: "))
            no_number=False
        except:
            print("That's not a number!")
    new_fav_no=fav_no+1
    print('How about having',new_fav_no,'as your favourite number?')
    
def angry_boss():
    print("Boss: What do you want?")
    ans = input("You: ")
    ans_caps=ans.upper()
    print('Boss: WHADDAYA MEAN "'+ans_caps+'"?!? YOU\'RE FIRED!!')
    
def contents():
    print('Table of Contents'.center(70,'_'))
    print()
    
    chapters=[]
    pages=[]
    chapters+=['Chapter 1: Getting Started'.ljust(35,'.')] 
    chapters+=['Chapter 2: Numbers'.ljust(35,'.')] 
    chapters+=['Chapter 3: Letters'.ljust(35,'.')] 
    pages+=['page 1'.rjust(35,'.')] 
    pages+=['page 9'.rjust(35,'.')] 
    pages+=['page 13'.rjust(35,'.')] 

    for i in range(3):
        print(chapters[i]+pages[i])
        
#________________________________DAY 4______________________________________________

def bottles_of_beer(n):
    if(n>=2):
        for i in range(n,1,-1):
            print(i,"bottles of beer on the wall,",i,"bottles of beer.")
            print("Take one down and pass it around,",i,"bottles of beer on the wall.\n")
    
    if(n>=1):
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        
    if(n>=0):
        print("No more bottles of beer on the wall, no more bottles of beer. ")
        print("Go to the store and buy some more, 99 bottles of beer on the wall.\n")
    else:
        print("Negative bottles of beer on the wall, negative bottles of beer.")
        print("Please give them back to the store.\n")

def deaf_grandma():
    print('Visiting Grandma'.center(25,'-'))
    
    bye_count=0
    while(True):
        s=input('You: ')
        if(s!=s.upper()):
            print('HUH?! SPEAK UP, GIRL!')
            bye_count=0
        else:
            if('BYE' in s):
                bye_count+=1
                if(bye_count<3):
                    print('HUH?! SPEAK UP, GIRL!')            
                else:
                    break
            else:
                year=1930 + random.randint(0,20)
                print('NO, NOT SINCE',year,'!')
                bye_count=0

def leap_years():
    print('Finding leap years'.center(25,'-'))
    start=int(input('Please enter starting year: '))
    end=int(input('Please enter ending year: '))
    for i in range(start,end+1):
        if(i%400==0):
            print(i)
        elif(i%100==0):
            continue
        elif(i%4==0):
            print(i)

def calculation_in_life():
    print('Bonus real life calculation'.center(25,'-'))
    try:
        num=int(input('Please enter a number: '))
    except:
        print("That's not a number!")
        
    while(num>0):
        print('You have',num,'pieces of popcorn. Eat? (y/n)')
        ans=input()
        if(ans=='y'):
            num=num-1
        elif(ans=='n'):
            print('Full? (y/n)')
            ans2=input()
            if(ans2=='y'):
                break
           
    if(num<1):
        print('No more popcorn :(')
        
def sorting_an_array():
    print('Sorting lists'.center(25,'-'))
    arr=[]
    while(True):
        word=input('Enter a word: ')
        if(word==''):
            break
        else:
            arr.append(word)
            
    sorted_arr=sorted(arr)    
    for w in sorted_arr:
        print(w)
        
def contents2(total_chapters,pages_per_chapter):
    print('Table of Contents'.center(50,'_'))
    
    chapters=[]
    pages=[]
    
    #Creating table
    for i in range(total_chapters):
        chapters.append('Chapter '+str(i+1))
        pages.append((i+1)*pages_per_chapter)
    
    #Printing contents
    for i in range(total_chapters):
        left_str=chapters[i].ljust(25,'.') 
        right_str=str(pages[i]).rjust(25,'.')
        print(left_str+right_str)
        
def moo(n):
    for i in range(n):
        print('moo')
    print('( n=',n,')')
    
def old_roman_numerals(num):
    # I = 1 V = 5 X = 10 L = 50 C = 100 D = 500 M = 1000
    roman_num=''
    while(num>0):
        if(num>=1000):
            roman_num+='M'
            num=num-1000
        elif(num>=500):
            roman_num+='D'
            num=num-500
        elif(num>=100):
            roman_num+='C'
            num=num-100
        elif(num>=50):
            roman_num+='L'
            num=num-50
        elif(num>=10):
            roman_num+='X'
            num=num-10
        elif(num>=5):
            roman_num+='V'
            num=num-5
        else:
            roman_num+='I'
            num=num-1
    return roman_num
    
def roman_numerals(num):
    if(num<1):
        return ''
    
    roman_symbols_dict={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    roman_symbols=['I','V','X','L','C','D','M']
    
    old_roman_num=old_roman_numerals(num)
    largest_symbol=old_roman_num[0]
    largest_symbol_value=roman_symbols_dict[largest_symbol]
    
    ones_symbol_value=1
    temp_largest_symbol_value=largest_symbol_value
    while(temp_largest_symbol_value%10==0):
        temp_largest_symbol_value/=10
        ones_symbol_value*=10
    
    try:
        next_largest_symbol=roman_symbols[roman_symbols.index(largest_symbol)+1]
        next_largest_symbol_value=roman_symbols_dict[next_largest_symbol]
        diff=next_largest_symbol_value-num
    except:
        diff=ones_symbol_value+1 #execute else case of if condition below
       
    if(diff<=ones_symbol_value):
        roman_num = old_roman_numerals(ones_symbol_value)+next_largest_symbol 
        acc=next_largest_symbol_value-ones_symbol_value
    else:
        roman_num=largest_symbol
        acc=largest_symbol_value
        
    roman_num=roman_num+roman_numerals(num-acc)
    
    return roman_num
    
#________________________________MAIN______________________________________________    
    
print('WEEK 1 HW SOLUTIONS')
print()

print('Day 1 Solutions'.center(75,'-'))
print('A year is',hours_in_year(),'hours')
print('A decade is',minutes_in_decade(),'minutes')
print('I am',age_in_seconds(5,2,1997),'seconds old')
print('(OPTIONAL)')
print('A 32-bit system takes',system_timeout(32),'days to timeout if it has a bug with integer overflow')
print('A 64-bit system takes',system_timeout(64),'days to timeout if it has a bug with integer overflow')
print()

print('Day 2: No Home Work'.center(75,'-'))
print()

print('Day 3 Solutions'.center(75,'-'))
greeting()
print()
favourite_number()
print()
angry_boss()
print()
contents()
print()

print('Day 4 Solutions'.center(75,'-'))
bottles_of_beer(5)
print('(Sorry, 99 will make you ill)')
print()
deaf_grandma()
print()
leap_years()
print()
calculation_in_life()
print()
sorting_an_array()
print()
contents2(5,10)
print()
moo(6)
print()
print('Old-school Roman numerals'.center(35,'-'))
n=int(input('Enter a number: '))
print('Old-school Roman number:',old_roman_numerals(n))
print()
print('Roman numerals'.center(35,'-'))
n=int(input('Enter a number: '))
print('Roman number:',roman_numerals(n))
