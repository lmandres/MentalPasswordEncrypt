# MentalPasswordEncrypt
MentalPasswordEncrypt is a set of python scripts to generate keys, test the mappings, and practice usage of Manuel Blum's Mental Password Hash function, described in the following link:

[Mental Cryptography and Good Passwords](https://scilogs.spektrum.de/hlf/mental-cryptography-and-good-passwords/)

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
