from selenium import webdriver
from scraper_utils import *

source = "RandomHistory.com"
uri = "http://facts.randomhistory.com/interesting-facts-about-cats.html"

driver = webdriver.PhantomJS()
output_catfact_fname = "catfact_randomhistory.json"
output_metadata_fname = "meta_randomhistory.json"
err_retry_count = 3

def main():
    global uri
    global source

    catfact_set = []
    metadata_set = []

    print(info_tag + "Processing all facts in URL: " + uri)

    for result in scrape(uri):
        catfact_set.append(catfact_process(result))
        metadata_set.append(metadata_process(result, uri, source))

    output_json(output_catfact_fname, catfact_set)
    output_json(output_metadata_fname, metadata_set)
 
    print(info_tag + "Processing complete!")
    print(info_tag + "Cat-facts output to: " + output_catfact_fname)   
    print(info_tag + "Metadata output to: " + output_metadata_fname)

def scrape(uri):
    global driver

    driver.get(uri)
    results = driver.find_elements_by_class_name("content-td")[0]
    return [x.text[0:-1] for x in results.find_elements_by_tag_name("li")]

# Run on call
main() 
