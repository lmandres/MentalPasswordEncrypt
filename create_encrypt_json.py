import json
import random

digit_list = [str(i % 10) for i in range(0, 10, 1)]
map_list = [str(i % 10) for i in range(0, 36, 1)]

random.shuffle(digit_list)
random.shuffle(map_list)

password_json = {
    "digits": "".join(digit_list),
    "alphanumeric": "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    "alphanumbmap": "".join(map_list) 
}

with open("password_encrypt.json", "w") as fileout:
    json.dump(password_json, fileout)
