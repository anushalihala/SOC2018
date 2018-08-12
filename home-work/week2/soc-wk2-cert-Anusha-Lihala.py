import random
from nltk.corpus import brown
#________________________________DAY 1______________________________________________

def alice_word_count():
    fh=open('alice_in_wonderland.txt','r', encoding="utf8")
    text=fh.read().lower()
    chars = []

    for ch in text:
        if(ch.isalpha()):
        
            add_char = False
            for i,l in enumerate(chars):
                if(ch in l):
                    chars[i][1] += 1
                    add_char = True
                    break
                    
            if(add_char==False):
                chars.append([ch,1])
                
    #Printing results
    print("\nThe frequency distribution of alphabets in alice_in_wonderland.txt")
    print("(Using 2d lists)")
    for item in sorted(chars):
        print(item)
    fh.close()
#________________________________DAY 2______________________________________________
        
def numbers_to_letters():
    print("\nNumbers to letters function with correction;")
    count=0
    for i in range(65,65+2*26):
        char = chr(i)
        if(char.isalpha()):
            print(i, " stands for ", char)
        else:
            count+=1
            
    for j in range(i,i+count+1):
        print(j, " stands for ", chr(j))
        
def a_to_z():
    print("\nFunction that prints A-Z and a-z")
    s1=ord('A')
    for i in range(s1,s1+26):
        print(chr(i))
        
    s2=ord('a')
    for i in range(s2,s2+26):
        print(chr(i))
            
def cypher(message):
    encrypted_msg = []
    for ch in message:
        encrypted_msg.append(ord(ch))
    return encrypted_msg
    
def caeser_cypher(message, shift):
    encrypted_msg = ""
    for ch in message:
        encrypted_msg += chr(ord(ch)+shift)
    return encrypted_msg
    
def traverse_2dlist(lst):
    for row in lst:
        print()
        for item in row:
            print(item)
            
def reversed_traverse_2dlist(lst):
    for row in reversed(lst):
        print()
        for item in reversed(row):
            print(item)
        

def continent_counter(world, x, y):    
    n=len(world)
    if(x>=n or x<0 or y>=n or y<0):
        return 0
 
    if world[y][x]!='land':
        # Either it's water or we already counted it,​
        # but either way, we don't want to count it now.​
        return 0
  
    # So first we count this tile...​
    size = 1
    world[y][x]='counted land'
    # ...then we count all of the neighboring eight tiles​
    # (and, of course, their neighbors by way of the recursion).​
    size = size + continent_counter(world, x-1, y-1)
    size = size + continent_counter(world, x , y-1)
    size = size + continent_counter(world, x+1, y-1)
    size = size + continent_counter(world, x-1, y )
    size = size + continent_counter(world, x+1, y )
    size = size + continent_counter(world, x-1, y+1)
    size = size + continent_counter(world, x , y+1)
    size = size + continent_counter(world, x+1, y+1)
    return size
    
def random_world_generator(n):
    random_board = [[random.randint(0,1) for j in range(n)] for i in range(n)]
    return random_board

#________________________________DAY 3______________________________________________

def modify_dict():
    print("\nModifying existing dictionary to change key name;")
    my_dict = {
        "a": 35000,
        "b": 8000,
        "z": 450
    }
    print('Original dictionary; ',my_dict)
    
    val=my_dict['a']
    del(my_dict['a'])
    new_key=input("Enter new key for dictionary in place of 'a': ")
    my_dict[new_key]=val
    
    print('New dictionary; ',my_dict)
    
def alice_word_count_dict():
    fh=open('alice_in_wonderland.txt','r', encoding="utf8")
    text=fh.read().lower()
    chars = dict()

    for ch in text:
        if(ch.isalpha()):       
            chars[ch]=chars.get(ch,0)+1
                
    #Printing results
    print("\nThe frequency distribution of alphabets in alice_in_wonderland.txt")
    print("(Using a dictionary)")
    print(chars)
    for i in range(ord("a"),ord("z")+1):
        print(chr(i),"=",chars[chr(i)])
    fh.close()
    
def my_dict():
    print("\nCreating a dictionary with personal details;")
    d = dict()
    print("Dictionary before additions:",d)
    d["Name"]="Anusha Lihala"
    d["Country"]="India"
    d["Fav quote"]= "I have loved the stars too fondly to be fearful of the night. — Sarah Williams"
    d["Pet"]="None, sadly"
    print("Dictionary after additions:",d)
    print("Printing individual key value pairs;")
    for k,v in d.items():
        print(k,"=",v)
    

class Student():
    def __init__(self, name, discord_id, dream):
        self.name = name
        self.discord_id = discord_id
        self.dream = dream
        
    def __str__(self):
        str = "Name: " + self.name + "\n" + "Discord ID: " + self.discord_id + "\n" + "Dream: " + self.dream + "\n"
        return str
        

class Student_1MWTT():
    i_want_to = ['Find my next job', 'Become a freelancer', 'Start my own tech startup']
    coding_level = ['Beginner', 'Intermediate', 'Advanced']

    def __init__(self, first_name, last_name, email, phone_no, github, country, goals, level):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_no = phone_no
        self.github = github
        self.country = country
        self.goals = goals #list of integers representing indices
        self.level = level #integer between 0 and 2
        
    def __str__(self):
        str  = "First Name: " + self.first_name + "\n" 
        str += "Last Name: " + self.last_name + "\n" 
        str += "Email: " + self.email + "\n"
        str += "Phone No.: " + self.phone_no + "\n"
        str += "Github: " + self.github + "\n"
        str += "Country: " + self.country + "\n"
        str += "Goals;\n"
        for goal in self.goals:
            str += Student_1MWTT.i_want_to[goal] + "\n"
        str += "Coding Level: " + Student_1MWTT.coding_level[self.level] + "\n"

        return str
        
#________________________________DAY 4______________________________________________

def lexical_diversity(text):
    return len(set(text))/len(text)
    
def category_lexical_diversity(categories):
    for category in categories:
        print("Lexical diversity of", category , "is", str(lexical_diversity(brown.words(categories=category))))
#________________________________MAIN______________________________________________    
    
print('WEEK 2 HW SOLUTIONS')
print()

print('Day 1 Solutions'.center(75,'-'))
alice_word_count()


print('Day 2 Solutions'.center(75,'-'))
numbers_to_letters()
a_to_z()

print("\nCypher function - turns message into a list of numbers")
msg=input("Enter message: ")
print(cypher(msg))

print("\n(OPTIONAL) Ceaser Cypher function - shifts message by a given number during encryption")
msg=input("Enter message: ")
try:
    num=int(input("Enter number for shift: "))
    print(caeser_cypher(msg,num))
except:
    print("That's not a number :(")  
    
print("\nTraversing world in continent counter;")
o="water"
M="land"
world = [[o,o,o,o,o,o,o,o,o,o,o],
         [o,o,o,o,M,M,o,o,o,o,o],
         [o,o,o,o,o,o,o,o,M,M,o],
         [o,o,o,M,o,o,o,o,o,M,o],
         [o,o,o,M,o,M,M,o,o,o,o],
         [o,o,o,o,M,M,M,M,o,o,o],
         [o,o,o,M,M,M,M,M,M,M,o],
         [o,o,o,M,M,o,M,M,M,o,o],
         [o,o,o,o,o,o,M,M,o,o,o],
         [o,M,o,o,o,M,o,o,o,o,o],
         [o,o,o,o,o,o,o,o,o,o,o]]
traverse_2dlist(world)
print("\nTraversing world in continent counter in reverse order;")
reversed_traverse_2dlist(world)

print("\nContinent counter function with correction;")
new_world = world
new_world[6][10]=M
print("Printing new world;")
for row in new_world:
    print(row)
print(continent_counter(new_world,5,5))

print("\nGenerating random nxn world (where 1=land and 0=water);")
try:
    n=int(input("Enter n: "))
    for row in random_world_generator(n):
        print(row)
except:
    print("That's not a number :(") 
    

print('Day 3 Solutions'.center(75,'-'))
modify_dict()
alice_word_count_dict()
my_dict()

print("\nInstantiating a student variable for everyone who shared their dream in the live chat;")
students = []
students += [Student("Sandra", "sandra.bullock", "Support Sudanese women's equality in the home")]
students += [Student("​Marwa Qabeel", "​Marwa Qabeel [Gold]", "Data Analyst")]
students += [Student("Jessica​", "Jessi_RS [Gold]", "work as developer by end of the year")]
students += [Student("Bituin Callanta​", "bituin [gold]", "lessen the gender wage gap")]
for s in students:
    print(s)
print()
    
print("\nTranslating real world 1MWTT students into a Student class;\n")
s1=Student_1MWTT("Anusha","Lihala","anusha.lihala@gmail.com","123456789","github.com/anushalihala","India",[0,1,2],1)
print(s1)


print('Day 4 Solutions'.center(75,'-'))
print("\nFinding lexical diversity for genres humor and romance in the brown corpus.")
category_lexical_diversity(['humor','romance'])