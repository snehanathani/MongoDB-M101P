import pymongo
import sys

connection = pymongo.Connection("localhost", safe=True)
db = connection.m101
people = db.people

person = {'name':'Barack Obama', 'role':'President',
          'address':
              {'address1':'The White House',
               'street':'1600 Pennsylvania Ave',
               'state':'DC',
               'city':'Washington' },
          'interests':['government','basketball','middle east']}


people.insert(person)

print person

try:
    people.insert(person)
except:
    print "insert failed:", sys.exc_info()[0],'--',sys.exc_info()[1]

