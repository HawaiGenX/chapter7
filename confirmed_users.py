# A list of users need to be verified
unconfirmed_users = ['alice john', 'brian carter', 'john malik', 'candace edwards', 'mary jacobs']

confirmed_users =[]

while unconfirmed_users:
    current_user = unconfirmed_users.pop(0) 
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
#Print confirmed users
print(f"\nThe following users have been confimed")
for confirmed_user in confirmed_users:
    print(f"{confirmed_user.title()}")
print("\n")