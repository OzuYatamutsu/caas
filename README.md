# Steakscorp CaaS
**Cat-facts as a Service!** This project provides a RESTful API to query a MongoDB database for cat-facts scraped across the web.

### Dependencies
**CaaS** is written in **Python 3**, **Django**, and assumes a **MongoDB** backend. As such, it depends on the following:
 * `django`
 * `mongoengine` version **0.9.0**.

##### Scrapers
 * `phantomjs`
 * `selenium`

Install them all at once:
`pip3 install django mongoengine==0.9.0 phantomjs selenium`

### Scrapers
Scrapers are used to scrape specific sources for cat-facts and output JSON files, ready to be inserted into the database. They are written in **Python 3** and can be found in the `scrapers/` directory.

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
