# Steakscorp CaaS
**Cat-facts as a Service!** This project provides a RESTful API to query a MongoDB database for cat-facts scraped across the web.

### API
See `index.html` in the `django/caas_app/templates/` directory.

### Dependencies
**CaaS** is written in **Python 2**, **Django**, and assumes a **MongoDB** backend. It depends on the following:
 * `django`
 * `pymongo` version **2.8**.
 * `mongoengine` version **0.9.0**.
##### Scrapers
 * `phantomjs`
 * `selenium`

Switch to the virtual environment packaged in the app:<br />
`source caas_virtualenv/bin/activate`

Install them all at once:<br />
`pip install pymongo==2.8 mongoengine==0.9.0 django phantomjs selenium`

### Setup
 * Install MongoDB (if not done already) and add a new `caas` database from the MongoDB shell: `use caas`
 * Copy `django/db-auth.template.json` to `django/db-auth.json`, and edit the `username`, `password`, and any other required fields to match your database settings. Do the same in the `data/` directory.
 * Run `data/db-insert.py` against `data/db-auth.json` and all `.json` files in the `data/` directory to populate your database.
 * Hook up the `django/caas_app` Django application to the web server of your choice, or use `python manage.py startserver <ip>:<port>` to use the built-in Django web server to run the app.

### Scrapers
Scrapers are used to scrape specific sources for cat-facts and output JSON files, ready to be inserted into the database. They are written in **Python 2** (but compatible with Python 3) and can be found in the `scrapers/` directory.

### MongoDB collection schema
The database has two collections: **catfact** and **meta**.

#### `db.catfact`
This table contains the actual text of the cat-fact.

##### Fields
`_id` The MD5 hash of the cat-fact text, truncated to 24 characters.<br>
`text` The text cat-fact.

#### `db.meta`
This table contains the metadata of the cat-fact.

##### Fields
`_id` The MD5 hash of the cat-fact text, truncated to 24 characters.<br>
`source` The human-readable source of the cat-fact. (e.g. "Steakscorp Labs") <br>
`url` The specific URL where the cat-fact text was scraped.
