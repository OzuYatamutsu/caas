from sys import argv
from os import path
from json import loads
from pymongo import *

ERR_ARGS = """Syntax: json-insert.py <auth-file.json> <data-file.json>
Please make sure your file exists!"""
ERR_JSON_MAL = "Error! Is JSON file malformed?"
ERR_MONGO_CONN = "Error! Couldn't connect to database."
ERR_MONGO_AUTH = "Error! Credentials were rejected!"

def main():
    if (len(argv) == 3 and path.isfile(argv[1])):
        try:
            auth_set = decode_json(argv[1])[0]
            data_set, type = decode_json(argv[2])
            auth_conn = connect_db(auth_set)
            bulk_insert(auth_conn, auth_set, data_set, type)
            print("Job done!")
        except ValueError:
            print(ERR_JSON_MAL)
        except errors.ServerSelectionTimeoutError:
            print(ERR_MONGO_CONN)
        except errors.OperationFailure:
            print(ERR_MONGO_AUTH)   
    else: print(ERR_ARGS)

def decode_json(fname):
    json_dict = {}
    type = fname.split("_")[0]
    with open(fname, "r") as f:
        json_dict = loads(f.read())
    return json_dict, type

def connect_db(auth_set):
    conn = MongoClient(
        auth_set["host"], 
        int(auth_set["port"]))
    conn[auth_set["auth_db"]].authenticate(
        auth_set["username"],
        auth_set["password"])
    return conn

def bulk_insert(auth_conn, auth_set, data_set, type):
    # Don't call this with db_auth.json!
    coll_target = ""
    if (type == "catfact"):
        coll_target = "catfact"
    elif (type == "meta"):
        coll_target = "meta"
    elif (type == "intro"):
        coll_target = "intro"
    elif (type == "newsub"):
        coll_target = "newsub"
    elif (type == "unsub"):
        coll_target = "unsub"
    elif (type == "notrecog"):
        coll_target = "notrecog"
    else:
        raise ValueError
    print("DEBUG: " + coll_target) 
    for doc in data_set:
        print("Inserting doc into " + coll_target + ": " + str(doc))
        try:
            auth_conn[auth_set["db"]][coll_target].insert(doc)
        except errors.DuplicateKeyError:
            # Should never happen on non-catfact and non-meta, as no explicit _id field
            print("Duplicate key on " + doc["_id"] + ", attempting update instead")
            auth_conn[auth_set["db"]][coll_target].update({"_id": doc["_id"]}, doc)

# Run on start
main()
