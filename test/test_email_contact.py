import re
def test_emails_on_home_page(app):
    emails_from_home_page = app.contact.get_contact_list()[0]
    emails_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert emails_from_home_page.all_emails_from_home_page == merge_phones_like_on_home_page(emails_from_edit_page)

def clear(s):
    return re.sub("", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))