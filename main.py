import json
import time
import threading

key_value = {}
gb = 1024*1024*1024
kb16 = 16*1024*1024

def create(key,value,time_to_live=0):
    if key in key_value:
        print("Error! Already Exist")
    else:
        if key.isalpha():
            val = json.dumps(value)
            if len(key_value) <= gb and len(val) <= kb16:
                if len(key) <= 32:
                    time.sleep(1)
                    lst = [val, time.time()+time_to_live]
                    key_value[key] = lst
                    print("Sucessfully added")
                else:
                    print("Key Length limit exceeded")
            else:
                print("Length of key or Length of the key_value database is exceeded")
        else:
            print("Key should only be in string")

def read(key):
    if key not in key_value:
        print("Key doestn't exist in the database")
    else:
        lst = key_value[key]
        if time.time() > lst[1]:
            print("Time to live for the provided key is expired")
        else:
            print(lst[0])

def delete(key):
    if key not in key_length:
        print("Key doestn't exist in the database")
    else:
        lst = key_value[key]
        if time.time() > lst[1]:
            print("Time to live for the provided key is expired")
        else:
            del key_value[key]
            print("sucessfully deleted") 
