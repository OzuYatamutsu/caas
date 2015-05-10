from selenium import webdriver
from scraper_utils import *

source = "Cornell Feline Health Center"
uri = "http://www.vet.cornell.edu/FHC/feline_fun/fun_facts.cfm"

driver = webdriver.PhantomJS()
output_catfact_fname = "catfact_cornell.json"
output_metadata_fname = "meta_cornell.json"
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

    driver.quit()
    print(info_tag + "Processing complete!")
    print(info_tag + "Cat-facts output to: " + output_catfact_fname)
    print(info_tag + "Metadata output to: " + output_metadata_fname)

def scrape(uri):
    # NOTE: For some reason, phantomjs <= 1.9.0 may hang here sometimes
    global driver

    driver.get(uri)
    results = driver.find_elements_by_class_name("contents")[0]
    return [x.text for x in results.find_elements_by_tag_name("p")[2:20]]

# Run on call
main()
