# MentalPasswordEncrypt
MentalPasswordEncrypt is a set of python scripts to generate keys, test the mappings, and practice usage of Manuel Blum's Mental Password Hash function, described in the following link:

[Mental Cryptography and Good Passwords](https://scilogs.spektrum.de/hlf/mental-cryptography-and-good-passwords/)

NOTE: Rob Shearer has shown that Manuel Blum's Mental Hash is cryptographically weak as demonstrated by a naive attack with about 150 characters of ciphertext:

[The "Blum Mental Hash" Is A Lousy Idea](https://v.cx/2022/05/blum-mental-hash)

## Prerequisites
MentalPasswordEncrypt relies on the following prerequisites:

* Python version 3.9 or greater
* Git
* pip for installation of Python modules

## Installation

* In the installation directory run

```bash
git clone https://github.com/lmandres/MentalPasswordEncrypt.git
cd MentalPasswordEncrypt
git pull
```

* You can create a virtual environment to run the application (This step is optional).

```bash
python3 -m venv venv
source venv/bin/activate
```

* Install the prerequisite Python modules

```bash
pip install -r requirements.txt
```

## Creating Keys

* In the installation directory, if you have a virtual environment set up, run:

```bash
venv/bin/python create_encrypt_json.py
```

* Otherwise, run:

```bash
python3 create_encrypt_json.py
```

* You no longer need this script, as this generates the keys.  Therefor, you can optionally run:

```bash
rm create_encrypt_json.py
```

This will create your keys and necessary files to begin using Manuel Blum's Mental Hash function.

## Directions

* In the installation directory, open the `password_encrypt.json` file and memorize the sequence of digits under the `digits` key of the JSON file.
* Memorize the mapping between the `alphanumeric` sequence and `alphanumbmap` sequence.
* Test your memory of the mapping between `alphanumeric` and `alphanumbmap` by running the following script:

```bash
venv/bin/python test_mapping.py
```
or:
```bash
python3 test_mapping.py
```

* Once you have a good memory of the `digits` sequence and the alphanumeric mapping, then you are able to apply Manuel Blum's Mental Hash function.
* Test your use of the hash function by running:
  
```bash
venv/bin/python test_encrypt.py
```
or:
```bash
python3 test_encrypt.py
```

## Personal Notes
The Blum Mental Hash should not be used as it stands.  Instead, it should serve as a starting point to use the method.  However, you should add different ways to salt the password hash with different methods, for example, coming up with a salt value to use after each round of changing the password.  This should come with proficiency in using the method, but the Blum Mental Hash should not be used before then.  Certain methods that I have come up with are:

* adding and modding in hexadecimal instead of decimal
* salting the hash with a unique salt value after each round of changing the password
* salting the hash with the website value
* repeating the salt for each round of computing the value

These methods need to be used in the same order that was used when the password was set.  In addition, these intermediate calculations should not be output into the password.  In any case, there needs to exist several ways to mutate the password after each password change for each different site without compromising the hash keys in case of a password leak.

Lastly, the complexity of the steps to calculate the hash or password should be based on the sensitivity of the information kept on the website.  For example, I don't plan to use Blum's Mental Hash method for my most sensitive accounts.  However, for casual accounts like newspaper media or situations where I have to create an account but don't have my password manager available, I may use Blum's method with modifications.

Still, as of the date of this edit, I don't believe that I am proficient enough in the use of Blum's Mental Hash to use for casual or regular accounts. 