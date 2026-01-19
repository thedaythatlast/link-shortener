from fastapi import FastAPI, Request, HTTPException
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
    _date: str

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
        return {"error": "Error: Can't shorten an invalid URL."}

    # shortening url_table through hashes
    hash_object = hashlib.sha256(url.encode())
    url_table.append(Record(
        url, 
        hash_object.hexdigest()[:6], 
        datetime.now()))

    # getting the port of your own server
    port = request.scope.get("server")[1]
    return {"shortened_link": f"localhost:{port}/{hash_object.hexdigest()[:6]}"}

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
        # first check: if there's a row containing the url
        # second check: if more than 2 years have passed since the shortened link's generated date
        if (row._hash == url) & (datetime.now() - row._date <= timedelta(days=730)):
            return RedirectResponse(row._url, status_code=302)
        else:
            raise HTTPException(status_code=404, detail="Shortened link doesn't exist, or has expired.")

@app.get("/")
def home():
    return {"detail": "Use localhost:{your_port}/shorten?url={url_address_you_want_to_shorten} to shorten a link of your choice."}