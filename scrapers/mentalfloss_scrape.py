from selenium import webdriver
from scraper_utils import *

source = "mental_floss"
uri = "http://mentalfloss.com/uk/science/25796/20-fun-facts-about-cats"

driver = webdriver.PhantomJS()
output_catfact_fname = "catfact_mentalfloss.json"
output_metadata_fname = "meta_mentalfloss.json"
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
    global driver

    driver.get(uri)
    results = driver.find_elements_by_class_name("field-name-body")[0]
    return [pronoun_replace(x.text[3:]) for x in results.find_elements_by_tag_name("h4")]

def pronoun_replace(text):
    print("BEFORE: " + text)
    text = text.replace("They're", "Cats are")
    text = text.replace("They'll", "Cats will")
    text = text.replace("Their", "Cats'")
    text = text.replace("they're", "cats are")
    text = text.replace("they'll", "cats will")
    text = text.replace("their", "cats'")
    text = text.replace("They", "Cats")
    text = text.replace("they", "cats")
    text = text.replace("And ", "")
    text = text if text[0] != " " else text[1:]
    
    text = text.capitalize()
    return text 
# Run on call
main()

