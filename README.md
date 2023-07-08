# realestate_webscrape

What is it used for:
scraping popular realestate sources for all applicable data

What data will I get:
	house: 
		location
		price
		date listed
		date relisted?
		aspects:
			square footage
			number rooms
			number washrooms
			number kitches
			others?
		meta data:
			number views?
			who is selling it

Possible Tools:
	selinium
	beautiful soup
	xpath
	online database on azure
	local database to test
	containerized deployments?
		docker
		k8s

Project architecture
	1) scrape data from various websites
		a) seperate module for each website implementation
		b) automate the spin upp and scheduleing of each scrape (what tool?)
	2) stream and clean the data
		a) pyspark for streaming? or kafka?
		c) generate payload in a bulk manner to make data entries into db easy?
	3) input data for online database on azure
	4) develop analitics tools for data

