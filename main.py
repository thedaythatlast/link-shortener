from fastapi import FastAPI, Request
import hashlib
import base64
import validators
from fastapi.responses import RedirectResponse
from datetime import datetime, timedelta
from dataclasses import dataclass



app = FastAPI()

@dataclass
class Record:
    _url: str
    _hash: str
    _expire: str

url_table: list[Record] = []

#port = request.scope.get("server")[1]

# HOW TO USE THE API:
# Use the address localhost:{your_host}/shorten?url={url_address_you_want_to_shorten}
# => You will receive the shortened link

def is_valid_url(url: str) -> bool:
    url = url.strip()

    return validators.url(url) is True

@app.get("/shorten")
def shorten(url, request: Request):
    # check if the url starts with 'http://' or 'https://', add 'https://' otherwise:
    url = url.strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    # verify if url is valid, return warning if otherwise
    if is_valid_url(url) == False:
        return "Error: Can't shorten an invalid URL."

    # Calculate expiration: current time + 730 days (2 years)
    expire_date = datetime.now() + timedelta(days=730)

    # shortening url_table through hashes
    hash_object = hashlib.sha256(url.encode())
    url_table.append(Record(
        url, 
        hash_object.hexdigest()[:6], 
        expire_date.strftime("%Y-%m-%d")))
    #url_table[url] = hash_object.hexdigest()[:6]

    # getting the port of your own server
    port = request.scope.get("server")[1]
    return f"localhost:{port}/{hash_object.hexdigest()[:6]}"

@app.get("/debug")
def show_database():
    # returns the stored data to browser
    return url_table

@app.get("/{url}")
def redirect(url, request: Request):
    # getting the port of your own server
    port = request.scope.get("server")[1]


    # {key : value}
    # key = the full URL
    # value = the hashed URL
    for row in url_table:
        if row._hash == url:
            return RedirectResponse(row._url, status_code=302)

@app.get("/")
def home():
    return "Use localhost:{your_port}/shorten?url={url_address_you_want_to_shorten} to shorten a link of your choice."