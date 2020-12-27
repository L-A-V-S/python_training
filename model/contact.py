from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, homephone=None, mobilphone=None ,
                 workphone=None, secondaryphone=None, id=None, all_phones_from_home_page=None,
                 address=None, all_emails_from_home_page=None, email=None, email2=None, email3=None):
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.nickname=nickname
        self.firstname = firstname
        self.lastname = lastname
        self.homephone = homephone
        self.mobilphone = mobilphone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.id, self.firstname, self.middlename, self.lastname, self.nickname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
