from json import dumps
from hashlib import md5

info_tag = "<info> "
warn_tag = "<warn> "
err_tag = "<error> "
succ_tag = "<success> "

def catfact_process(cat_fact):
    json_obj = {}
    json_obj["_id"] = md5(cat_fact.encode("utf-8")).hexdigest()[0:24]
    json_obj["text"] = cat_fact

    return json_obj

def metadata_process(cat_fact, uri, id, source):
    json_obj = {}
    json_obj["_id"] = md5(cat_fact.encode("utf-8")).hexdigest()[0:24]
    json_obj["source"] = source
    json_obj["url"] = uri + str(id)

    return json_obj

def output_json(fname, set):
    with open(fname, 'w') as f:
        f.write(dumps(set))
