from model.group import Group

def test_modify_group(app):
    app.group.modify(Group(name="test2", header="modif2", footer="test2"))


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))
