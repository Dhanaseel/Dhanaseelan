Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def remove_vowels(string):
...     vowels = 'aeiouAEIOU'
...     without_vowels = ''
... 
...     for char in string:
...         if char not in vowels:
...             without_vowels += char
... 
