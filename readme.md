# datatypes 
@  Mutable datatypes
 * List 
 * Set 
 * Dictionary 
 * Bytearray
 * Array 

@ Immutable datatypes
 * Integer
 * floating-point numbers
 * Boolean
 * String
 * Tuples
 * Frozen set
* bytes

 std_info
{117: 'Vikas prajapati', 93: 'Pratik shirsat', 103: 'Sujal vende', 116: 'Atharv mane'}
>>> std_info[117]
'Vikas prajapati'
>>> std_info[103]
'Sujal vende'
>>> std_info[93]
'Pratik shirsat'
>>> std_info.get(117)
'Vikas prajapati'
>>> for stdInfo in std_info:
...     print(stdInfo)
...
117
93
103
116
>>> for stdInfo in std_info:
...     print(stdInfo, std_info[stdInfo])
...
117 Vikas prajapati
93 Pratik shirsat
103 Sujal vende
116 Atharv mane
>>> for key , values in std_info.items():
...     print(key , values)
...
117 Vikas prajapati
93 Pratik shirsat
103 Sujal vende
116 Atharv mane

>>> if 117 in std_info:
...     print("Yes,Student available in dictionary")
...
Yes,Student available in dictionary
>>>
how to key value pair in dictionary
>>> std_info[116] = "Atharv Mane"
>>> std_info
{89: 'Vaibhav', 117: 'Vikas Prajapati', 103: 'Sujal Vende', 116: 'Atharv Mane'}
>>>
how to remove key-values or items 
std_info.pop(103)
'Sujal Vende'
>>> std_info
{89: 'Vaibhav', 117: 'Vikas Prajapati', 116: 'Atharv Mane'}
>>> std_info.popitem()
(116, 'Atharv Mane')

how to delete an item in dectonary
 del std_info[89]
>>> std_info
{117: 'Vikas Prajapati'}
#Nesting of dictionary

>>> std_details
{117: {'name': 'Vikas', 'surname': 'Prajapati', 'age': 19}, 103: {'name': 'Sujal', 'surname': 'Vende', 'age': 19}}
>>> std_details[117]
{'name': 'Vikas', 'surname': 'Prajapati', 'age': 19}
>>> std_details[117]["age"]
19
>>> std_details[103]
{'name': 'Sujal', 'surname': 'Vende', 'age': 19}
>>> std_details[103]["surname"]
'Vende'
>>>
TUPLE IN PYTHON
>>> tupleVar = ("Mango" , "Apple" , "Banana" , "Pineapple")
>>> tupleVar
('Mango', 'Apple', 'Banana', 'Pineapple')
>>> for tpl in tupleVar:
...     print(tpl)
...
Mango
Apple
Banana
Pineapple
>>> tupleVar[4]
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    tupleVar[4]

IndexError: tuple index out of range
>>> tupleVar[2]
'Banana'

USER INPUT 
> input("Give me a number = ")
Give me a number = 100
'100'
>>> 100/2
50.0
>>> userInput = input("Give me a number = ")
Give me a number = 37
>>> userInput * 3
'373737'
>>> int(userInput) * 2
74
>>>

LOOPINT STATEMENTS IN PYTHON
>>> if userData < 13:
...     print("child")
... elif userData < 20:
...     print("Teenager")
... elif userData < 60:
...     print("Adult")
... else:
...     print("Senior")
...
Senior
>>> userData
92
>>> userData = 23
>>> if userData < 13:
...     print("child")                  [NOTE : INDENTATION ERROR]
... elif userData < 20:
...     print("Teenager")
... elif userData < 60:
...     print("Adult")
... else:
...     print("Senior")
...
Adult

