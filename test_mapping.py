import json
import random

mappings = {}
with open("password_encrypt.json", "r") as filein:
    mappings = json.load(filein)

try:

    while True:

        index = random.randint(0, 35)
        print(mappings["alphanumeric"][index])
        varin = input("What is the mapping? ")

        if (varin == mappings["alphanumbmap"][index]):
            print("Correct!")
        else:
            print("Wrong.  Answer is: {}".format(mappings["alphanumbmap"][index]))

except KeyboardInterrupt:
    print("Exiting . . .")   
