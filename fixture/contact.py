
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/index.php"):
            wd.find_element_by_link_text("home").click()

    def return_home_page_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.add_new_contact()
        # fill group form
        self.addinfo(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_home_page_contact()

    def add_new_contact(self):
        wd = self.app.wd
        # add new contact
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # ok dialog window
        wd.switch_to_alert().accept()
        # wait info
        wd.find_element_by_css_selector("div.msgbox")
        self.return_home_page_contact()

    def modify(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.select_first_contact()
        # Edit
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # modify
        self.addinfo(contact)
        # click update
        wd.find_element_by_name("update").click()
        self.return_home_page_contact()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.select_first_contact()
        # Edit
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # modify
        self.addinfo(contact)
        # click update
        wd.find_element_by_name("update").click()
        self.return_home_page_contact()

    def addinfo(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contact_page()
        contactrow = []
        #contact_table = wd.find_element_by_css_selector("tbody")
        for element in wd.find_elements_by_name("entry"):
            cells = element.find_elements_by_tag_name("td")
            text1 = cells[1].text
            text2 = cells[2].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contactrow.append(Contact(firstname=text2,lastname=text1, id=id))
        return contactrow
