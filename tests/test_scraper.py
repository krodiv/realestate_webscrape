import estate_scraper.inital_scraper as scrape

def test_scraper_creation():
    scraper = scrape.Scraper()
    
    assert scraper.create_driver() == 'hello'
    assert scraper.set_source('value') == 'value'

