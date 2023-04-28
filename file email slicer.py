import re

# accepting file name from the user, default file is mbox-short.txt
filename = input("Enter a file name: ")

# if the user did not enter a filename, use the default filename
if len(filename) < 1:
    filename = 'mbox.txt'

# open the file and store a reference to the file object in filehandle
filehandle = open(filename)

# regex pattern for the email
email_pattern = r"[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# variable to track whether any emails were found in the file
found = False

# set to store unique email addresses
email_set = set()

# checking for emails in file
for line in filehandle:
    # search for an email pattern in the current line
    match = re.search(email_pattern, line)
    if match:
        found = True
        email = match.group()
        # check if the email is already in the email set, so duplicates aren't printed
        if email not in email_set:
            # add email to the set
            email_set.add(email)
            (username, domain) = email.split('@')
            (domain, extension) = domain.split(".", 1)

            # print out the email and its components
            print(email)
            print("Username:", username)
            print("Domain:", domain, "\n")

# if no emails were found in the file, print a message
if found == False:
    print("No emails found.")
