#import addressbook_pb2 as addressbook
from python import addressbook_pb2 as addressbook
import sys
sys.path.append("../")
print sys.path
import decorator
sys.path = sys.path[0:-1]
print sys.path

person = addressbook.Person()
person.id = 666
person.name = 'amy'
person.email = '342323@vd.vom'
#phone = person.phones.add()
#phone.number = '12244234'
#phone.type = addressbook.Person.HOME

print person
print '==========='
s = person.SerializeToString()
print s
print '==========='

p = addressbook.Person()
p.ParseFromString(s)
print p
phones = p.phones
print "phones", len(phones), phones
print '==========='

print 'type(person)', type(person)
print 'type(s)', type(s)
print 'type(p)', type(p)

tmp = type(person)
print str(tmp)
print str(tmp).split('\'')[1]

book = addressbook.book__pb2.Book()
book.name = "huozhe"
print book