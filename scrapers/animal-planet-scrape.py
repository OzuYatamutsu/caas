from selenium import webdriver
from hashlib import md5
from json import dumps

err_text = "Sorry"
base_uri = "http://www.animalplanet.com/pets/cat-facts/?fact_id="
source = "Animal Planet"
info_tag = "<info> "
err_tag = "<error> "
succ_tag = "<success> "

driver = webdriver.PhantomJS()
max_id = 49999
output_catfact_fname = "catfact.json"
output_metadata_fname = "metadata.json"

def main():
	catfact_set = []
	metadata_set = []

	for id in range(45000, max_id):
		cat_fact = False

		try:
			cat_fact = scrape(base_uri, id)
		except Exception:
			 print(err_tag + "Connection failure! Skipping ID " + str(id))
		
		if (cat_fact is not False):
			catfact_set.append(catfact_process(catfact))
			metadata_set.append(metadata_process(uri, id))
	output_json(output_catfact_fname, catfact_set)
	output_json(output_metadata_fname, metadata_set)
	print(info_tag + "Processing complete!")
	print(info_tag + "Cat-facts output to: " + output_catfact_fname)
	print(info_tag + "Metadata output to: " + output_metadata_fname)

def scrape(uri, id):
	# GET on URI + ID
	print(info_tag + "Processing ID " + str(id) + "...")
	driver.get(base_uri + str(id))

	# Check if usable result
	if ((err_text not in driver.title) and (driver.title.replace(" ", "") != "")):
		driver.find_elements_by_class_name("global-body-text")[0].text
	else:
		return False

def catfact_process(catfact):
	json_obj = {}
	json_obj["_id"] = md5(catfact.encode("utf-8")).hexdigest()
	json_obj["text"] = catfact
	
	return json_obj

def metadata_process(uri, id):
	global source

	json_obj = {}
	json_obj["_id"] = md5(catfact.encode("utf-8")).hexdigest()
	json_obj["source"] = source
	json_obj["url"] = uri + str(id)

	return json_obj

def output_json(fname, set):
	with open(fname, 'w') as f:
		f.write(dumps(set))
