import estate_scraper.inital_scraper as scrape

def test_scraper_creation():
    scraper = scrape.Scraper()
    scraper.create_driver()
    
    res = scraper.get_source("https://www.realtor.ca/on/toronto/real-estate")
    assert "Toronto" in res.title

    content = scraper.find_element_by_class_name("listingCardPrice")
    print(content.get_attribute("title"))

    assert 1 == 0

