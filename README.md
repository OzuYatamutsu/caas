# Steakscorp CaaS
**Cat-facts as a Service!** This project provides a RESTful API to query a MongoDB database for cat-facts scraped across the web.

### Dependencies
**CaaS** is written in **Python 2**, **Django**, and assumes a **MongoDB** backend. It depends on the following:
 * `django` version **1.5**
 * `pymongo` version **3.0.0**.
 * `django-nonrel`
 * `djangotoolbox`
 * `mongodb-engine`

##### Scrapers
 * `phantomjs`
 * `selenium`

Install them all at once:
`pip install pymongo==3.0.0 git+https://github.com/django-nonrel/django@nonrel-1.5 git+https://github.com/django-nonrel/djangotoolbox git+https://github.com/django-nonrel/mongodb-engine phantomjs selenium`

### Scrapers
Scrapers are used to scrape specific sources for cat-facts and output JSON files, ready to be inserted into the database. They are written in **Python 2** (but compatible with Python 3) and can be found in the `scrapers/` directory.

### MongoDB collection schema
The database has two tables: **catfact** and **meta**.

#### `db.catfact`
This table contains the actual text of the cat-fact.

##### Fields
`_id` The MD5 hash of the cat-fact text. <br>
`text` The text cat-fact.

#### `db.meta`
This table contains the metadata of the cat-fact.

##### Fields
`_id` The MD5 hash of the cat-fact text. <br>
`source` The human-readable source of the cat-fact. (e.g. "Steakscorp Labs") <br>
`url` The specific URL where the cat-fact text was scraped.
