from model.contact import Contact

def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(Contact(firstname="test", middlename="modify", lastname="mod", nickname="test"))
    app.session.logout()