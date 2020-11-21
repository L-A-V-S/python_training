from model.contact import Contact

def test_modify_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    contact = Contact(firstname="test", middlename="modify", lastname="mod", nickname="test")
    contact.id = old_contacts[0].id
    app.contact.modify(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_firstname(app):
#    old_contacts = app.contact.get_contact_list()
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    app.contact.modify_first_contact(Contact(firstname="New firstname"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_modify_contact_middlename(app):
#    old_contacts = app.contact.get_contact_list()
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    app.contact.modify_first_contact(Contact(middlename="New middlename"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)

