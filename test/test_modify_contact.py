from model.contact import Contact

def test_modify_group(app):
    app.contact.modify(Contact(firstname="test", middlename="modify", lastname="mod", nickname="test"))
