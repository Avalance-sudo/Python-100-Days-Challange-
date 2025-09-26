# This is the first comment of a single line comment 
# This is the second comment 
#Python is the programing language I am learning.

# Multi-line comment
#''' Triple quotes are used for multi-line comments in Python if not assigned to a variable.
'''This is a multiline comment
multline comment takes multiple lines. 
Python is eating the world.'''

# Data types 
# Intger: (Negative,zero and postive) example -1,0,1,2,3
#float:(Decimal point number) example 1.5,2.5,3.5
#Complex:(Real and imaginary) example 1+2j,2+3j
# String( a collection of characters under a single or double quote)# Example:
'Batman'
"Nightwing"
'Red Hood'
'Nightwing is the coolest!!'
'Red Hood has a cool character design!!'

# Booleans: A data type that is either True or False. T and F are always capitalized.
# Example:
True # Is the sky blue? If it is, then the vaule is True
False # Is the sky green? If it is not, then the value is False

# List: Built in structure that can hold an orderd collection of items.
# Example:
{0,1,2,3,4,5} # all are the same data type 
{'Batman','Nightwing','Red Hood'} # all are the same data type - list of batman family
{'Hambunger,Pizza','Pasta'} # all are the same data type - list of food
{'Batman,10,,False,1.5'} # all are different data types - list of mixed data types

# Dictionary: Built in structure that can hold an unordered collection of data in key value pair format.
# Example:
{ 
 'first_name': 'Bruce',
 'last_name': 'Wayne',
 'hometown': 'Gotham',
 'age': 35,
    'is_billionaire': True,
    'skills': ['martial arts', 'detective', 'business']
 }

#Tuple: Order collection of diffent data typeslike list but tuplescan not be changed one they are created.
('Batman','Nightwing' ,'Red Hood','Batgirl','Robin') #Names
('Suit','Cape','Cowl','Utility Belt') #Gadgets

# Set: Collection of data types similar to list and tuple.Unlike list and tuple,set is not an ordered collection of items. 
{2,4,3,5}
{3.15,9.81,2.7} # ordr is not  important in set


# 3. Write differnet python data tpes such as number, string, boolean, list, dictionary, tuple and set.

#float 
my_float =10.5 
another_float= 5.15
print(my + another_float)

#String 
single_quote_string = 'Hello, Nightwing!'
double_quoted_string = "Hello, Red Hood!" 
multi_line_string = '''Hello Batman family,'''

# Boolean
is_Nightwing_avenger = False
is_Batmnan_Justice_League_Member =  True

# List 
Justice_League_Members = ['Batman', 'Superman', 'Flash' , 'Wonder Women', 'Aquaman']
Super_Hero_Skills = [' Martial Arts', 'Dective skills', 'Speed', 'Strenght']

# Dictionary
Justice_League_Members_Details ={
      'Batman': {
         'real_name': 'Bruce Wayne',
         'age': 35,
         'is_billionaire': True,
         'skills': ['martial arts', 'detective skills', 'business acumen']
      },
      'Superman': {
         'real name': 'Clark Kent'
         'age': 30,  
         'is_alien': True, 
         'family': ['Louis Lane', 'Superboy' , 'Supergirl']
}
}

# Tuple 
Nightwing_tuple=(1,"hero",3.5,True)
Gadgets_tuple = ('Batrang', 'Sword', 'Grappling Gun', 'Smoke Bombs') # Creating a truple with multiple elements 

Nightwing_emptu_tuple=() # Empty tuple 

# Set
Nightwing_set={1,2,3,4,5, "hello", True} 
empty_set=set() #Empty Set
unique_elements=set(my_list)  #unique elements will be {1,2,3,4,5}

