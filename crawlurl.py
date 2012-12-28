
#!/usr/bin/env python

# This code will find the first url from an HTML file.


contents = ('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

start = contents.find('<a href="')

#print link

start_quote = contents.find('"',start)
end_quote = contents.find('"',start_quote+1)
url = contents[start_quote+1:end_quote]
print url