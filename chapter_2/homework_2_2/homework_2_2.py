
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.students
grades = db.grades


def find():

    print "HW2 running"

    query = {'type':'homework'}

    hw_grades = grades.find(query).sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])

    
    student_id = ''
    new_id = False
    
    for grade in hw_grades:
        
        if (student_id != grade['student_id']):
            new_id = True
            student_id = grade['student_id']
            print "####### I will delete ", grade['_id']
            grades.remove({'_id':grade['_id']})
            
        new_id = False

            
find()
