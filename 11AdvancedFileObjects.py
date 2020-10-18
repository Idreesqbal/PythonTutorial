with open('test.txt', 'r') as f: # it is always a good practice to open files like this
f = open('test.txt', 'r') # this also a way to work with files but the problem is
f.mode
f.close() # if u forget to put this at the end of file operation, the file may go to error

# to make sure our file handeling is in the safe hands, it is always recommended to do it with 'with'

with open('text.txt', 'r') as f:
    f_contents = f.readlines() # reads the line of the file all
    f_contents = f.readline() # will read only the first line of the text
    f_contents = f.read() # this will read the entire text all at once
    # read() take arguments, e.g. read(100) will paste the first 100 character of the text
    f.seek(0) # it basically put the cursor back to position 0 everything we loop the text
    print(f_contents)

import os

os.chdir('Location of the file')
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    f_title, f_course, f_num = file_name.split('-')
    print('{}-{}-{}{}'.format((file_name, f_title)))