"""
13-FEB-2018

author: Alejandro Guevara
"""
s1 = "Hello World from Python"
s2 = "Alphabetic"
list = ['Hello','World','from','Python']

print('Original Strings')
print(s1)
print(s2)

print('----')
print(s1.lower()) # returns the lowercase version of the String
print(s1.upper()) # returns the uppercase version of the String
print(s1.strip()) # returns a string with whitespace removed from the start and end
print(s2.isalpha()) # test if all the string chars are alphabetic chars
print(s2.isdigit()) # test if all the string chars are digits
print(s2.isspace()) # test if al the string chars are spaces
print(s1.startswith('Hello')) # test if the string starts with the given other string
print(s1.endswith('Hello')) # test if the string ends with the given other string
print(s1.find('World')) # searches for the given other string (not regex) within s1, and returns the first
                        # index where it begins or -1 if not found
print(s1.replace('World', 'Everyone')) # returns a string where all occurrences of 'old' have been replaced by 'new'
print(s1.split())   # returns a list of substrings separated by the given delimiter. The delimiter is not a
                    # regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc'].
                    # As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
print(' '.join(list)) # opposite of split(), joins the elements in the given list together using the string as the
                    # delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc
