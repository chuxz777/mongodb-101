import sys
import pymongo

connection= pymongo.MongoClient("mongodb://localhost")

db = connection.test
users = db.users

doc = {'firstname':'Nicolas','lastname':'Hefti'}
print doc
print 'About to insert the document'

try:
    users.insert(doc)
except:
    print 'Instert failed:', sys.exc_info()[0]
    
print doc
print 'Inserting again'

try:
    users.insert(doc)
except:
    print 'Second instert failed:', sys.exc_info()[0]
