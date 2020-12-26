from model.contact import Contact
from random import randrange
import re

def test_info_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test",address=""))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    address_from_home_page = app.contact.get_contact_list()[index]
    address_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert address_from_home_page.address == address_from_edit_page.address
    emails_from_home_page = app.contact.get_contact_list()[index]
    emails_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert emails_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(emails_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilphone,
                                        contact.workphone,  contact.secondaryphone]))))

def clear2(s):
    return re.sub("", "", s)

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear2(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))