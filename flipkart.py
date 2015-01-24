import urllib2
from bs4 import BeautifulSoup
import time
import mechanize
import re




#Getting the Source
def flipkart(isbn):
	f_link = "http://www.flipkart.com/search?q="+isbn
	br = mechanize.Browser()
	br.set_handle_robots(False)   # ignore robots
	br.set_handle_refresh(False)  # can sometimes hang without this
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]# [('User-agent', 'Firefox')]
	response = br.open(f_link)

	#Getting the soup

	f_soup = BeautifulSoup(response.read())

	#Getting the data
	f_name_temp =(f_soup.find(itemprop="name"))
	if(not f_name_temp):
		f_name = f_name_temp.string
		f_price = f_soup.find_all("span",class_="selling-price omniture-field")[0].string
		f_author = (f_soup.find_all(href=re.compile("/author/[\w\s,.$><?@#$%^&*()_:-]+"))[0]).string
		f_img = (f_soup.find_all("img",class_="productImage  current")[0])['data-src']

