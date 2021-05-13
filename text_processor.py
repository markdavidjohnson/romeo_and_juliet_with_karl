#created this to work with Karl on his Python learning, showing how 
# I would have done it optimizing for writing speed and line count

import urllib.request  # the lib that handles the url stuff

path = 'https://raw.githubusercontent.com/markdavidjohnson/romeo_and_juliet_with_karl/main/text_input.txt'
data = []
for line in urllib.request.urlopen(path):
    data += line.decode('utf-8').replace(',','').replace('!','').replace('?','').lower().split()  #this is a bit much for 1 line
data = list(dict.fromkeys(data))  #strip duplicates
data.sort()
print(data)
