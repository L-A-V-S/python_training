from model.contact import Contact
import random
import string

testdata = [
    Contact(firstname="firstname1",  middlename="middlename1", lastname="lastname1", nickname="nickname1"),
    Contact(firstname="firstname2",  middlename="middlename2", lastname="lastname2", nickname="nickname2")
]

#def random_string(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
#    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#testdata = [Contact(firstname="",  middlename="", lastname="", nickname="")] + [
#    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20), lastname=random_string("lastname", 20), nickname=random_string("nickname", 20))
#    for i in range(5)
#]
