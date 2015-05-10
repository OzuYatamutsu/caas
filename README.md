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

Install them all at once:<br />
`pip install pymongo==2.8 mongoengine==0.9.0 django phantomjs selenium`

### Setup
 * Install MongoDB (if not done already) and add a new `caas` database from the MongoDB shell: `use caas`
 * Copy `django/db_auth.template.json` to `django/db_auth.json`, and edit the `username`, `password`, and any other required fields to match your database settings. Do the same in the `data/` directory.
 * Run `data/db-insert.py` against `data/db_auth.json` and all `.json` files in the `data/` directory to populate your database.
 * Hook up the `django/caas_app` Django application to the web server of your choice, or use `python manage.py startserver <ip>:<port>` to use the built-in Django web server to run the app.

### Scrapers
Scrapers are used to scrape specific sources for cat-facts and output JSON files, ready to be inserted into the database. They are written in **Python 2** (but compatible with Python 3) and can be found in the `scrapers/` directory. To be compatible with the `data/db-insert.py` insertion script, output filenames should be prefixed by `<coll_name>_`, where `coll_name` is one of the target collections detailed below (without the `db.` prefix).

### MongoDB collection schema
The database has six collections: **catfact**, **meta**, **intro**, **newsub**, **unsub**, and **notrecog**.

#### `db.catfact`
This collection contains the actual text of the cat-fact.

##### Fields
`_id` The MD5 hash of the cat-fact text, truncated to 24 characters.<br>
`text` The text cat-fact.

#### `db.meta`
This collection contains the metadata of the cat-fact.

##### Fields
`_id` The MD5 hash of the cat-fact text, truncated to 24 characters.<br>
`source` The human-readable source of the cat-fact. (e.g. "Steakscorp Labs") <br>
`url` The specific URL where the cat-fact text was scraped.

#### `db.intro`
This collection contains intro text (see [API|#API]) to be inserted before the response text if `intro=yes` was specified in the API query.

##### Fields
`text` The intro text to be inserted before the response text. The actual text included in the response will be chosen randomly from this collection.

#### `db.newsub`
This collection contains new subscription text (see [API|#API]) to be inserted before the response text if `newsub=yes` was specified in the API query.

##### Fields
`text` The new subscription text to be inserted before the response text. The actual text included in the response will be chosen randomly from this collection.

#### `db.unsub`
This collection contains unsubscription text (see [API|#API]) to be inserted after the response text if `unsub=yes` was specified in the API query.

##### Fields
`text` The unsubscription text to be inserted before the response text. The actual text included in the response will be chosen randomly from this collection.

#### `db.intro`
This collection contains "command not recognized" error messages (see [API|#API]) to be inserted before the response text if `notrecog=yes` was specified in the API query.

##### Fields
`text` The "command not recognized" text to be inserted before the response text. The actual text included in the response will be chosen randomly from this collection.

