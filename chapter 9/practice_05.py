words =["kaadu","londe","Asshole"]

with open ('simple.txt') as f:
    contact = f.read()

for word in words:
    contact = contact.replace (word,"$$#@^&@")


    with open ('simple.txt' ,'w') as f:
        f.write(contact)