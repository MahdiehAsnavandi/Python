import hashlib
import csv
from collections import OrderedDict


def hash_password_hack(input_file_name):
    with open (input_file_name , "r" ) as f:
        reader = csv.reader(f)
        name_hash = OrderedDict()
        for row in reader:
            username = str(row[0])
            hash = str(row[1])
            name_hash[hash] = username

    password_hash = OrderedDict()
    for n in range(1000 , 10000 ):
        password = str(n).zfill(4)
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        password_hash[hashed_password] = n

    for a in password_hash.keys():
        for b in name_hash.keys():
            if a == b:
                print("%s's password is %s"  %(name_hash[b] , password_hash[a]))

hash_password_hack("hashed_files")



    
