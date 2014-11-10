# While loop
fruit = [ 'apple', 'orange', 'kiwi', 'apple',
        'banana', 'orange' ] # init array

i = 0
while (i < len(fruit)):
    # print fruit[i]
    i = i + 1

# Functions
def analyze_list(l):
    
    counts = {}
    for item in l:
        
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1
            
    return counts

# Analyze a list
counts = analyze_list(fruit)
print counts

# Exception Handling
import sys

try:
    print 5/0
except:
    print 'Exception ', sys.exc_info()[0]
    
print 'But life goes on'
