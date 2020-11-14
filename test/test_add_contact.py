# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.add_new_contact()
    app.contact.create(Contact(firstname="ewre", middlename="eww", lastname="ewew", nickname="ewewc"))


def test_add_empty_contact(app):
    app.contact.add_new_contact()
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname=""))

