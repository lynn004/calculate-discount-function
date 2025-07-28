#set theory
admins = {"lynn","ava"}
editors = {"lynn","joe"}
    #combine both groups
all_users = admins.union (editors)
print("All users", all_users)

    #who is both admin and editor?
both_roles =admins.intersection (editors)
print("userswith both roles:",both_roles)
 
    #admin only
admin_only = admins.difference (editors)
print("admin only:", admin_only)