from model.group import Group
from random import randrange

def test_modify_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    app.group.modify(Group(name="test2", header="modif2", footer="test2"))


def test_modify_group_name(app, db):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[index].id
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_group_by_index(index, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) != sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    group = Group(header="New header")
#    group.id = old_groups[0].id
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    app.group.modify_first_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

