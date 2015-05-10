from selenium import webdriver
from hashlib import md5
from json import dumps

err_text = "Sorry"
base_uri = "http://www.animalplanet.com/pets/cat-facts/?fact_id="
source = "Animal Planet"
info_tag = "<info> "
warn_tag = "<warn> "
err_tag = "<error> "
succ_tag = "<success> "

driver = webdriver.PhantomJS()
max_id = 49999
output_catfact_fname = "catfact_animal-planet.json"
output_metadata_fname = "meta_animal-planet.json"
err_retry_count = 3

def main():
	catfact_set = []
	metadata_set = []

	for id in range(47000, max_id):
		cat_fact = False
		success = False
		retries = err_retry_count
	
		while not success and retries > 0:
			try:
				cat_fact = scrape(base_uri, id)
				success = True
			except Exception:
				print(warn_tag + "Connection failure! Trying again for ID " + str(id))
				retries = retries - 1
		if (retries == 0): print(err_tag + "Giving up on ID " + str(id))
		if (cat_fact is not False):
			print(succ_tag + "Adding ID " + str(id) + " to set: " + cat_fact)
			catfact_set.append(catfact_process(cat_fact))
			metadata_set.append(metadata_process(cat_fact, base_uri, id))
	output_json(output_catfact_fname, catfact_set)
	output_json(output_metadata_fname, metadata_set)
	print(info_tag + "Processing complete!")
	print(info_tag + "Cat-facts output to: " + output_catfact_fname)
	print(info_tag + "Metadata output to: " + output_metadata_fname)

def scrape(uri, id):
	global driver

	# GET on URI + ID
	print(info_tag + "Processing ID " + str(id) + "...")
	driver.get(base_uri + str(id))

	# Check if usable result
	if ((err_text not in driver.title) and (driver.title.split("|")[0].replace(" ", "") != "")):
		return driver.find_elements_by_class_name("global-body-text")[0].text
	else:
		return False

def catfact_process(cat_fact):
	json_obj = {}
	json_obj["_id"] = md5(cat_fact.encode("utf-8")).hexdigest()[0:24]
	json_obj["text"] = cat_fact
	
	return json_obj

def metadata_process(cat_fact, uri, id):
	global source

	json_obj = {}
	json_obj["_id"] = md5(cat_fact.encode("utf-8")).hexdigest()[0:24]
	json_obj["source"] = source
	json_obj["url"] = uri + str(id)

	return json_obj

def output_json(fname, set):
	with open(fname, 'w') as f:
		f.write(dumps(set))

# Run on call
main()
