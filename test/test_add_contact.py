# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    app.contact.add_new_contact()
    app.contact.create(Contact(firstname="ewre", middlename="eww", lastname="ewew", nickname="ewewc"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)

def test_add_empty_contact(app):
    old_contact = app.contact.get_contact_list()
    app.contact.add_new_contact()
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname=""))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)

