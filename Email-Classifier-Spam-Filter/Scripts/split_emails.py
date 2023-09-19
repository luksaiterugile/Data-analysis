import sys
f = open(sys.argv[1], "r")
file_content = f.read()
list_of_emails = file_content.split("SUBJECT:")
list_of_emails = [ "SUBJECT:" + email for email in list_of_emails ] 
list_of_emails = list_of_emails[1:]

def generate_filename(index):
    return "laiskas_" + str(index) + ".txt"

for email in range(len(list_of_emails)):
    filename = generate_filename(email)
    file = open(filename, 'w')
    file.write(list_of_emails[email])
    file.close()