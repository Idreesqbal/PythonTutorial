import re  # re Stands for regular expression

searching = '''abc is the best starting point to learn any language'''
urls = '''
https://www.google.com
https://www.youtube.com
https://www.twitter.com
https://www.facebook.com
'''
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d]')  # here we declare our pattern so we our programm can look at
pattern1 = re.compile(r'\d{3}.\d{3}.\d{3}')  # look for exact 3 digit
pattern2 = re.compile(r'MR\.?\s[A-Z]\w*')  # * it looks for the occurrence of the object 0 or more than zero time
pattern3 = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')  # (r|r|rs) it is called grouping, which look any of the occurance of
# them
pattern4 = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z]+\.(com|org|edu|net)')  # Good for finding the emails
pattern5 = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') # this is what we call grouping
# it is so useful bcoz we can create a back reference to them later for example:
sub_url = pattern5.sub(r'\2\3', pattern5)
matches = pattern.finditer(searching)
matches = pattern.findall(searching)  # Findall method will look at all matches that it finds
# but if the pattern used grouping of re then it will return only the first occurrences of the
# the group inside that text
for match in matches:
    print(match)
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    match = pattern.finditer(content)
    for match in matches:
        print(match)

