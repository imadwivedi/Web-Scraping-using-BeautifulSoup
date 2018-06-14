from urllib import urlopen
from bs4 import BeautifulSoup as soup

my_url='https://www.newegg.com/global/in/Product/ProductList.aspx?Submit=ENE&N=100204377&IsNodeId=1&Description=video%20cards&name=Desktop%20Graphics%20Cards&Order=BESTMATCH&isdeptsrh=1'

uClient=urlopen(my_url)
page_html=uClient.read()
uClient.close();

page_soup=soup(page_html,"html.parser")

containers=page_soup.findAll("div",{"class":"item-container"})

for container in containers:
	brand=container.div.div.a.img["title"]
	title_container=container.findAll("a",{"class":"item-title"})
	product_name=title_container[0].text


	print "Brand is"+brand
	print "Product name is"+product_name
