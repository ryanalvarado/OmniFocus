import dropbox
import user

# link the account by passing the token
# to the dropbox object
dbx = dropbox.Dropbox(user.token)

# test the link
# dbx.users_get_current_account()

# define the path to the folder/file of interest
path = '/Users/ellyn/Dropbox/OF\ Templates'

for entry in dbx.files_list_folder('').entries:
    if entry.name == 'OF Templates':
        print (entry.name)
    else:
        continue
