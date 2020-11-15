# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test"))
    app.contact.delete_first_contact()
