# Import JSON data to MongoDB
# mongoimport -d school -c students < students.json

# Write a program in the language of your choice that will remove the lowest 
# homework score for each student. Since there is a single document for each 
# student containing an array of scores, you will need to update the scores 
# array and remove the homework. 

# Hint/spoiler: With the new schema, this problem is a lot harder and that is 
# sort of the point. One way is to find the lowest homework in code and then 
# update the scores array with the low homework pruned.


import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.school
students = db.students


def find():

    print "HW3_1 running"
    
    all_students = students.find()

    for student in all_students:
    
      min_score = 100
      min_score_id = 0
      for key, score in enumerate(student['scores']):
        
        if (score['score'] < min_score and score['type'] == 'homework'):
          min_score = score['score']
          min_score_id = key
          
      del student['scores'][key]

      students.save(student)

            
find()
