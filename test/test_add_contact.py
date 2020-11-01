# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application ()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.add_new_contact()
    app.create_contact(Contact(firstname="ewre", middlename="eww", lastname="ewew", nickname="ewewc"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.add_new_contact()
    app.create_contact(Contact(firstname="", middlename="", lastname="", nickname=""))
    app.session.logout()
