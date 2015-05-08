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
            auth_set = decode_json(argv[1])
            data_set = decode_json(argv[2])
            auth_conn = connect_db(auth_set)
        bulk_insert(auth_conn, auth_set, data_set)
        except ValueError:
            print(ERR_JSON_MAL)
    except errors.ServerSelectionTimeoutError:
            print(ERR_MONGO_CONN)
    except errors.OperationFailure:
            print(ERR_MONGO_AUTH)   
    else: print(ERR_ARGS)

def decode_json(fname):
    json_dict = {}
    with open(fname, "r") as f:
        json_dict = loads(f.read())
    return json_dict

def connect_db(auth_set):
    conn = MongoClient(
        auth_set["hostname"], 
        auth_set["port"])
    conn[auth_set["auth_db"]].authenticate(
        auth_set["username"],
        auth_set["password"])
    return conn

def bulk_insert(auth_conn, auth_set, data_set):
    pass
