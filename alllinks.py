# Modify the get_next_target procedure so that
# if there is a link it behaves as before, but
# if there is no link tag in the input string,
# it returns None, 0.

# Note that None is not a string and so should
# not be enclosed in quotes.

# Also note that your answer will appear in
# parentheses if you print it.

def get_next_target(page):
    start_link = page.find('<a href=')
    # check if the start_link has a proper match or not
    if start_link == -1:
    	url , end_quote = None,0
    else:
    	start_quote = page.find('"',start_link)
    	end_quote = page.find('"',start_quote+1)
    	url = page[start_quote+1:end_quote]
    return (url , end_quote)




#url, end_quote = get_next_target('be it anything and then bla bla bla " blhay , bhata "')
#print url, end_quote


def print_all_links(page):
    while get_next_target(page)!=(None,0):
        url,end_quote=get_next_target(page)
        page=page[end_quote:]
        print url
       
print_all_links('<a href="https://a248.e.akamai.net/assets.github.com/assets/github-136f905f03a0a6ce0292d2e017a31c4fe548e2d0.css" media="screen" rel="stylesheet" type="text/css" />  <a href="https://a248.e.akamai.net/assets.github.com/assets/github2-6fb37f4beb26b76fec8bcd25a34a112492a75cd5.css" media="screen" rel="stylesheet" type="text/css" />')


    

    
   
    
    
