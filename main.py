from fastapi import FastAPI, Request
import hashlib
import base64
import validators


app = FastAPI()

urls = {}

# HOW TO USE THE API:
# Use the address localhost:{your_host}/shorten?url={url_address_you_want_to_shorten}
# => You will receive the shortened link

def is_valid_url(url: str) -> bool:
    url = url.strip()

    return validators.url(url) is True

@app.get("/shorten")
def shorten(url, request: Request):
    # check if the url starts with 'http://' or 'https://', add them otherwise:
    url = url.strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    # verify if url is valid, return warning if otherwise
    if is_valid_url(url) == False:
        return "Error: Can't shorten an invalid URL."

    # shortening urls through hashes
    hash_object = hashlib.sha256(url.encode())
    urls[url] = hash_object.hexdigest()[:6]

    # getting the port of your own server
    port = request.scope.get("server")[1]

    return f"localhost:{port}/{urls[url]}"

@app.get("/debug")
def show_database():
    # returns the stored data to browser
    return urls

@app.get("/{url}")
def redirect(url):
    for key, value in urls.items():
        if value == url:
            return key