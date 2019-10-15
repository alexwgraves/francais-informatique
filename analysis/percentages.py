import sys
from comment_results import *

# input error handling
if len(sys.argv) is not 2:
    sys.exit('Please specify a result: all, js, python, java, py_js, france, switzerland, belgium, quebec, senegal, switzerland_js, belgium_js, quebec_js, quebec_py, quebec_py_js.')

def calc_total(dict):
    total = 0
    for key in dict:
        total += dict[key]
    return total

def calc_percentage(dict, language):
    return dict[language] / calc_total(dict)

# assign dictionary based on input
file = sys.argv[1]
dict = all
if file == 'js':
    dict = js
if file == 'python':
    dict = python
if file == 'java':
    dict = java
if file == 'py_js':
    dict = py_js
if file == 'france':
    dict = france
if file == 'switzerland':
    dict = switzerland
if file == 'belgium':
    dict = belgium
if file == 'quebec':
    dict = quebec
if file == 'senegal':
    dict = senegal
if file == 'switzerland_js':
    dict = switzerland_js
if file == 'belgium_js':
    dict = belgium_js
if file == 'quebec_js':
    dict = quebec_js
if file == 'quebec_py':
    dict = quebec_py
if file == 'quebec_py_js':
    dict = quebec_py_js

print(f'Percent English: {calc_percentage(dict, "en")}')
print(f'Percent French: {calc_percentage(dict, "fr")}')
