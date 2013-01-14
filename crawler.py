from bs4 import BeautifulSoup
import urllib2


def crawler(seedurl):
	# to_crawl list will contain all the urls that need to be crawled
	to_crawl = [seedurl]
	# crawled list will contain all the urls that are crawled
	crawled=[]
	# A loop that will go on till the condition is true 
	while True:
		if to_crawl:
			for eachurl in to_crawl:
				# page will have the HTML contents of the url that are read using urllib2
				page = urllib2.urlopen(eachurl).read()
				# HTML contents i.e. page is passed to soup object that will find all urls from the HTML page
				soup = BeautifulSoup(page)
				# soup.findAll will find all the href tags 
				for hreftags in soup.findAll('a'):
					if hreftags:
						# the http url is extracted from the href tags
						url=hreftags['href']
						# to check if the urls obtained are already in to crawl list or crawled list(they are crawled before)
						if url not in to_crawl and url not in crawled:
							#appending unique urls to to_crawl list
							to_crawl.append(url)
				#removing parent urls from the to_crawl list and appending them crawled list 
				to_crawl.remove(eachurl)
				crawled.append(eachurl)
		else:
			print "to crawl is empty", to_crawl
			return crawled












	
				
print crawler("http://www.udacity.com/cs101x/index.html")