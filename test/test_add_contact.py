# -*- coding: utf-8 -*-
from model.contact import Contact
#import pytest
#from data.contacts import constant as testdata
#import random
#import string

#def random_string(prefix, maxlen):
#   symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
#    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#testdata = [Contact(firstname="",  middlename="", lastname="", nickname="")] + [
#    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20), lastname=random_string("lastname", 20), nickname=random_string("nickname", 20))
#    for i in range(5)
#]


#@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new_contact()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) != sorted(new_contacts, key=Contact.id_or_max)




