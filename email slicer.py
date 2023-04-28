import re

#accepting email from the user
email = input("Enter an email: ")

#regex pattern for the email
email_pattern = r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

#checking if the email matches the regex pattern
if re.match(email_pattern, email):
    (username, domain) = email.split('@')
    (domain, extension) = domain.split(".", 1)

    print("Username:", username)
    print("Domain:", domain)
    print("Extension:", extension)
else:
    print("Please enter a valid email next time.")