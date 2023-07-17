import estate_scraper.inital_scraper as scrape

def test_selenium_creation():
    scraper = scrape.Scraper()
    scraper.create_driver()
    
    res = scraper.get_source("https://www.realtor.ca/on/toronto/real-estate")
    assert "Toronto" in res.title

    # content = scraper.find_element_by_class_name("listingCardPrice")
    # print(content.get_attribute("title"))
    #
    # assert 1 == 0

def test_soup_creation():
    url = "http://toronto.listing.ca/"
    scraper = scrape.Scraper()
    scraper.init_bs4(url)

    result = scraper.find_sb4("div", {"class": "sl"})
    print(len(result))
    print(result[0].contents)

    assert 1 == 0
