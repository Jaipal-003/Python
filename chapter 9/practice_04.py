with open ('simple.txt') as f:
    contact = f.read()


contact = contact.replace ("kaadu","$$#@^&@")


with open ('simple.txt' ,'w') as f:
    f.write(contact)